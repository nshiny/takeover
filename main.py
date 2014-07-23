# TODO: Wrap bot invocations in exception handling with warnings.
# TODO: Match output suitable for analysis.
# TODO: Flag to disable debug and warning printing.
# TODO: Paramater to force certain bots into the matches.
# TODO: Select bots without replacement when there are enough.
# TODO: Optimize deepcopy by doing it less.
# TODO: Consider removing update_state calls when state hasn't changed.

from copy import deepcopy
from enum import Enum
from itertools import cycle

import random
import os
import sys

sys.path.append("bots")
from interface import Action, TargetedAction, Character, PlayerState


class Log:
    def warn(self, *args):
        print("Warning: " + self._format(*args))

    def debug(self, *args):
        print(self._format(*args))
              
    def _format(self, *args):
        parts = []
        for arg in args:
            if isinstance(arg, Player):
                parts.append(self._player(arg))
            elif isinstance(arg, Enum):
                parts.append(arg.name.capitalize())
            else:
                parts.append(str(arg))
        return " ".join(parts)

    def _player(self, player):
        text = player.name + "@" + str(player.identifier)
        text += "[" + str(player.coins) + "]"
        text += "[" + ",".join([self._short(x) for x in player.hidden]) + "]"
        text += "[" + ",".join([self._short(x) for x in player.flipped]) + "]"
        return text

    def _short(self, character):
        short = {Character.duke : "Dk",
                 Character.assassin : "As",
                 Character.ambassador : "Am",
                 Character.captain : "Cp",
                 Character.contessa : "Cn"}
        return short[character]
    
log = Log()


class Deck:
    """Represents a deck of cards with automatically managed shuffling."""
    
    def __init__(self):
        self._cards = []
        for character in Character:
            self._cards.extend([character for x in range(3)])

        random.shuffle(self._cards)

    def draw(self, count):
        # Skip bounds checking, because the deck isn't exhaustable.
        return [self._cards.pop() for x in range(count)]
        
    def place(self, cards):
        self._cards.extend(cards)
        random.shuffle(self._cards)


class Player:
    """Tracks player state for a single round and wraps Bots to manage their
    invocation and prevent them from making illegal moves. If an illegal move
    is detected, Player ignores the underlying Bot's request and falls back
    to default behavior."""
    
    def __init__(self, identifier, bot, drawn):
        self.identifier = identifier
        self.name = bot.__module__
        self._bot = bot
        self.coins = 2
        self.flipped = []
        self.hidden = drawn

    @property
    def active(self):
        return len(self.flipped) < 2

    def start(self):
        self._bot.start()

    def take_action(self, valid_targets):
        result = self._bot.take_action()
        
        if isinstance(result, Action):
            result = TargetedAction(result, None)

        if (not isinstance(result, TargetedAction) or
            not isinstance(result.action, Action)):
            log.warn(self, "take_action returned an invalid type")
            return self.default_action()

        if result.action is Action.block:
            log.warn(self, "take_action specified block")
            return self.default_action()
        
        if result.target is not None and result.target not in valid_targets:
            log.warn(self, "take_action specified an invalid target")
            return self.default_action()

        target_required = [Action.coup, Action.assassinate, Action.extort]
        if result.target is None and result.action in target_required:
            log.warn(self, "take_action did not specify a target")
            return self.default_action()

        minimum_coin = {Action.coup : 7, Action.assassinate: 3}
        if minimum_coin.get(result.action, 0) > self.coins:
            log.warn(self, "take_action returned an unfunded mandate")
            return self.default_action()

        if self.coins >= 10 and result.action != Action.coup:
            log.warn(self, "take_action did not coup with more than 10 coins")
            return self.default_action()
    
        return result

    def default_action(self):
        # Default to slow suicide!
        if self.coins < 10:
            return TargetedAction(Action.income, None)
        else:
            return TargetedAction(Action.coup, self.identifier)

    def block_action(self, actor, action, character, target):
        result = self._bot.block_action(actor, action, character, target)

        if result is not None and not isinstance(result, Character):
            log.warn(self, "block_action returned an invalid character")
            return None

        if not action.blockable(result):
            log.warn(self, "block_action returned an illegal character")
            return None

        return result

    def challenge(self, actor, action, character, target):
        result = self._bot.challenge(actor, action, character, target)

        if not isinstance(result, bool):
            log.warn(self, "challenge returned an invalid bool")
            return False

        return result

    def notify_action(self, actor, action, target, succeeded):
        self._bot.notify_action(actor, action, target, succeeded)

    def notify_challenge(self, challenger, actor, action,
                         character, target, sustained):
        self._bot.notify_challenge(
            challenger, actor, action, character, target, sustained)

    def notify_flip(self, player, flipped):
        self._bot.notify_flip(player, flipped)

    def update_state(self, states):
        self._bot.update_state(deepcopy(states), deepcopy(self.hidden))
    
    def flip(self):
        result = self._bot.flip()
        if not isinstance(result, Character) or result not in self.hidden:
            log.warn(self, "flip returned an invalid character")
            result = self.hidden[0]

        log.debug(self, "flips", result)
        self.hidden.remove(result)
        self.flipped.append(result)

        if len(self.hidden) == 0:
            log.debug(self, "loses")

    def exchange(self, drawn):
        result = self._bot.exchange(deepcopy(drawn))

        if not isinstance(result, list):
            log.warn(self, "exchange did not return a list")
            return drawn
        elif len(result) != 2:
            log.warn(self, "exchange returned a list not of length 2")
            return drawn
        elif (not isinstance(result[0], Character) or
              not isinstance(result[1], Character)):
            log.warn(self, "exchange returned a list without characters")
            return drawn

        merged = self.hidden + drawn
        if result[0] in merged:
            merged.remove(result[0])
        else:
            log.warn(self, "exchange returned invalid characters")
            return drawn

        if result[1] in merged:
            merged.remove(result[1])
        else:
            log.warn(self, "exchange returned invalid characters")
            return drawn

        self.hidden = merged
        return result

    def reveal(self, challenger, action, character, target):
        result = self._bot.reveal(challenger, action, character, target)

        if not isinstance(result, Character) or result not in self.hidden:
            log.warn(self, "reveal returned an invalid character")
            result = self.hidden[0]

        return result
            

class Match:
    """A set of bots in a fixed table order playing a series of rounds."""
    
    def __init__(self, bot_modules):
        self._stalemate_limit = 600
        self._bots = []
        for index, module in enumerate(bot_modules):
            self._bots.append(module.make_bot(index))

    def repeat(self, count):
        winners = []
        for x in range(count):
            result = self.play()
            if result is not None:
                winners.append(result)

        print("")
        for i, x in enumerate(self._bots):
            wins = sum(1 for w in winners if w.identifier == i)
            name = x.__module__ + " (" + str(i) + "):"
            print(name, str(float(wins) / float(count)))

    def play(self):
        self.deck = Deck()
        self.players = [Player(i, x, self.deck.draw(2))
                        for i, x in enumerate(self._bots)]

        for player in self.players:
            player.start()
        self.update_state()

        turn_count = 0
        for player in cycle(self.players):
            if player.active:
                if len(self.active_players()) <= 1:
                    break

                if turn_count >= self._stalemate_limit:
                    break
                
                self.turn(player)
                turn_count += 1

        winner = None
        if len(self.active_players()) == 1:
            winner = self.active_players()[0]
            log.debug(winner, "wins")
        else:
            for player in self.active_players():
                log.debug(player, "draws")
        return winner

    def turn(self, actor):
        valid_targets = [x.identifier for x in self.active_players()]
        action, target = actor.take_action(valid_targets)

        message = [actor, "selects", action]
        if target is not None:
            target = self.players[target]
            message.extend(["on", target])
        
        log.debug(*message)

        succeeded = True
        
        if action.challengeable():
            if self.challenge(actor, action,
                              action.required_character(), target):
                succeeded = False

        if succeeded:
            if action == Action.income:
                actor.coins += 1
            elif action == Action.foreign_aid:
                if not self.block(player, action, target):
                    if actor.active:
                        actor.coins += 2
                else:
                    succeeded = False
            elif action == Action.coup:
                actor.coins -= 7
                self.flip(target)
            elif action == Action.tax:
                actor.coins += 3
            elif action == Action.assassinate:
                actor.coins -=3
                if not self.block(actor, action, target):
                    if actor.active and target.active:
                        self.flip(target)
                else:
                    succeeded = False
            elif action == Action.exchange:
                discarded = actor.exchange(self.deck.draw(2))
                self.deck.place(discarded)
            elif action == Action.extort:
                if not self.block(actor, action, target):
                    if actor.active and target.active:
                        count = max(target.coins, 2)
                        target.coins -= count
                        actor.coins += count
                else:
                    succeeded = False
            else:
                raise NotImplemented(action)

        self.update_state()
        for player in self.active_players():
            player.notify_action(actor, action, target, succeeded)
            
    def block(self, actor, action, target):
        sustained = False
        blocker = None
        character = None

        players = []
        if target is not None:
            players.append(target)
        else:
            players.append(clockwise_players(actor))
            
        for potential in players:
            character = potential.block_action(
                self.identifier(actor), action,
                action.required_character(), self.identifier(target))
            if potential.active and character is not None:
                blocker = potential

        if blocker is not None:
            log.debug(blocker, "blocks", actor, "with", (character))
            if not self.challenge(blocker, Action.block, character, actor):
                sustained = True

        return sustained
                
    def challenge(self, actor, action, character, target):
        sustained = False
        challenger = None

        for player in self.clockwise_players(actor):
            if player.challenge(self.identifier(actor), action,
                                character, self.identifier(target)):
                if player.active and challenger is None:
                    challenger = player

        if challenger is not None:
            log.debug(challenger, "challenges", actor)
            revealed = actor.reveal(self.identifier(challenger), action,
                                    character, self.identifier(target))
            log.debug(actor, "reveals", revealed)
            if character == revealed:
                log.debug(actor, "wins the challenge")
                self.flip(challenger)
                
                actor.hidden.remove(revealed)
                self.deck.place([revealed])
                actor.hidden.extend(self.deck.draw(1))
            else:
                log.debug(challenger, "wins the challenge")
                actor.hidden.remove(revealed)
                actor.flipped.append(revealed)
                sustained = True
                
            self.update_state()
            for player in self.players:
                player.notify_challenge(
                    self.identifier(challenger), self.identifier(actor),
                    action, character, self.identifier(target), revealed)

        return sustained

    def flip(self, flipper):
        flipped = flipper.flip()

        self.update_state()
        for player in self.active_players():
            player.notify_flip(self.identifier(flipper), flipped)
    
    def update_state(self):
        states = [PlayerState(x.identifier, x.coins, x.flipped)
                  for x in self.players]
        for player in self.players:
            player.update_state(states)

    def active_players(self):
        return [x for x in self.players if x.active]

    def clockwise_players(self, start):
        key = lambda x: (x.identifier - start.identifier) % len(self.players)
        clockwise = sorted(self.players, key=key)
        clockwise.remove(start)
        return clockwise

    def identifier(self, player):
        if player is None:
            return None

        return player.identifier


def get_bots(path):
    names = [x[:-3] for x in os.listdir(path) if x[-3:] == ".py"]
    names.remove("__init__")

    return [__import__(x) for x in names]


def main(argv):
    bots = get_bots("bots")
    match = Match([random.choice(bots) for x in range(6)])
    match.repeat(1)

            
if __name__ == "__main__":
    sys.exit(main(sys.argv))
