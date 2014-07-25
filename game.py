from enum import Enum
from itertools import cycle

import collections
import random
import time
import traceback

from interface import Action, TargetedAction, Character, PlayerState


class Log:
    def __init__(self):
        self.verbose = True
    
    def warn(self, *args):
        print("Warning: " + self._format(*args))

    def event(self, *args):
        if self.verbose:
            print(self._format(*args))

    def summary(self, *args):
        print(self._format(*args)) 
              
    def _format(self, *args):
        parts = []
        for arg in args:
            if isinstance(arg, Enum):
                parts.append(arg.name.capitalize())
            else:
                parts.append(str(arg))
        return " ".join(parts)
    
log = Log()


def _try(function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except Exception as e:
        log.warn(traceback.format_exc())


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

    def __str__(self):
        text = self.name + "@" + str(self.identifier)
        text += "[" + str(self.coins) + "]"
        text += "[" + ",".join([x.short() for x in self.hidden]) + "]"
        text += "[" + ",".join([x.short() for x in self.flipped]) + "]"
        return text

    @property
    def active(self):
        return len(self.flipped) < 2

    def start(self):
        self._bot.start()

    def take_action(self, valid_targets):
        result = _try(self._bot.take_action)

        if isinstance(result, Action):
            result = TargetedAction(result, None)

        if (not isinstance(result, TargetedAction) or
            not isinstance(result.action, Action)):
            log.warn(self, "take_action returned an invalid type")
            return self._default_action()

        if result.action is Action.block:
            log.warn(self, "take_action specified block")
            return self._default_action()
        
        if result.target is not None and result.target not in valid_targets:
            log.warn(self, "take_action specified an invalid target")
            return self._default_action()

        target_required = [Action.coup, Action.assassinate, Action.extort]
        if result.target is None and result.action in target_required:
            log.warn(self, "take_action did not specify a target")
            return self._default_action()

        minimum_coin = {Action.coup : 7, Action.assassinate: 3}
        if minimum_coin.get(result.action, 0) > self.coins:
            log.warn(self, "take_action returned an unfunded mandate")
            return self._default_action()

        if self.coins >= 10 and result.action != Action.coup:
            log.warn(self, "take_action did not coup with more than 10 coins")
            return self._default_action()
    
        return result

    def block_action(self, actor, action, character, target):
        result = _try(
            self._bot.block_action, actor, action, character, target)
        
        if result is not None and not isinstance(result, Character):
            log.warn(self, "block_action returned an invalid character")
            return None

        if not action.blockable(result):
            log.warn(self, "block_action returned an illegal character")
            return None

        return result

    def challenge(self, actor, action, character, target):
        result = _try(
            self._bot.challenge, actor, action, character, target)
        
        if not isinstance(result, bool):
            log.warn(self, "challenge returned an invalid bool")
            return False

        return result

    def notify_action(self, actor, action, target, succeeded):
        _try(self._bot.notify_action, actor, action, target, succeeded)

    def notify_block(self, blocker, character, actor, action, succeeded):
        _try(self._bot.notify_block, blocker,
                  character, actor, action, succeeded)

    def notify_challenge(self, challenger, actor, action,
                         character, target, sustained):
        _try(self._bot.notify_challenge, challenger, actor,
                  action, character, target, sustained)

    def notify_flip(self, player, flipped):
        _try(self._bot.notify_flip, player, flipped)

    def update_state(self, states):
        _try(self._bot.update_state, states[:], tuple(self.hidden))
    
    def flip(self):
        result = _try(self._bot.flip)
        
        if not isinstance(result, Character) or result not in self.hidden:
            log.warn(self, "flip returned an invalid character")
            result = self.hidden[0]

        log.event(self, "flips", result)
        self.hidden.remove(result)
        self.flipped.append(result)

        if len(self.hidden) == 0:
            log.event(self, "loses")

    def exchange(self, drawn):
        result = _try(self._bot.exchange, tuple(drawn))

        if not isinstance(result, collections.Sequence):
            log.warn(self, "exchange did not return a sequence")
            return drawn
        elif len(result) != 2:
            log.warn(self, "exchange returned a sequence not of length 2")
            return drawn
        elif (not isinstance(result[0], Character) or
              not isinstance(result[1], Character)):
            log.warn(self, "exchange returned a sequence without characters")
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
        result = _try(
            self._bot.reveal, challenger, action, character, target)

        if not isinstance(result, Character) or result not in self.hidden:
            log.warn(self, "reveal returned an invalid character")
            result = self.hidden[0]

        return result

    def _default_action(self):
        # Default to slow suicide!
        if self.coins < 10:
            return TargetedAction(Action.income, None)
        else:
            return TargetedAction(Action.coup, self.identifier)
            

class DataScraper:
    def __init__(self, keepStats=False):
        self._trackData = keepStats
        if keepStats:
            global pandas
            global matplotlib
            import pandas
            import matplotlib
            
            self._playerDataFrame = pandas.DataFrame()

        self._playerDict = {}        
    
    def startRound(self, players):
        if self._trackData:
            for i, x in enumerate(players):
                self._playerDict[x.identifier] = {
                    'player':x.name, 
                    'card1':x.hidden[0],
                    'card2':x.hidden[1],
                    'seat':i}

    def playerEliminated(self, playerID, position):
        if self._trackData:
            self._playerDict[playerID]['position'] = position
            
    def endRound(self):
        if self._trackData:
            for x in self._playerDict.values():
                self._playerDataFrame = self._playerDataFrame.append(pandas.DataFrame([x]))
                
    def endMatch(self):
        if self._trackData:
            self._playerDataFrame.to_csv('matchData.csv', index=False)
        
class Match:
    """A set of bots in a fixed table order playing a series of rounds."""
    
    def __init__(self, bot_modules,keepStats=False):
        self._stalemate_limit = 600
        self._bots = []
        self._currentRoundPlaces = {}
        
        for index, module in enumerate(bot_modules):
            self._bots.append(module.make_bot(index))
        
        self._dataScraper = DataScraper(keepStats)

    def repeat(self, count):
        started = time.clock()
        winners = []
        for x in range(count):
            result = self.play()
            if result is not None:
                winners.append(result)

        for bot in self._bots:
            _try(bot.notify_end)

        log.summary("Completed in", str(int(time.clock() - started)), "seconds")
        log.summary("")
        for i, x in enumerate(self._bots):
            wins = sum(1 for w in winners if w.identifier == i)
            name = x.__module__ + "@" + str(i)
            log.summary(name, float(wins) / float(count))
        log.summary("draws", float(count - len(winners)) / float(count))
        
        self._dataScraper.endMatch()

    def play(self):
        self.deck = Deck()
        self.players = [Player(i, x, self.deck.draw(2))
                        for i, x in enumerate(self._bots)]

        self._dataScraper.startRound(self.players)
        for player in self.players:
            player.start()
        self.update_state()

        turn_count = 0
        order = self.players[:]
        random.shuffle(order)
        for player in cycle(order):
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
            log.event(winner, "wins")
            self._dataScraper.playerEliminated(self.active_players()[0].identifier, len(self.active_players()))
        else:
            for player in self.active_players():
                self._dataScraper.playerEliminated(player.identifier, len(self.active_players()))
                log.event(player, "draws")

        log.event("\n\n")
        self._dataScraper.endRound()
        return winner

    def turn(self, actor):
        valid_targets = [x.identifier for x in self.active_players()]
        action, target = actor.take_action(valid_targets)

        message = [actor, "selects", action]
        if target is not None:
            target = self.players[target]
            message.extend(["on", target])
        
        log.event(*message)

        succeeded = True
        
        if action.challengeable():
            if self.challenge(actor, action,
                              action.required_character(), target):
                succeeded = False

        if succeeded:
            if action == Action.income:
                actor.coins += 1
            elif action == Action.foreign_aid:
                if not self.block(actor, action, target):
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
                        count = min(target.coins, 2)
                        target.coins -= count
                        actor.coins += count
                else:
                    succeeded = False
            else:
                raise NotImplemented(action)

        self.update_state()
        for player in self.players:
            player.notify_action(self.identifier(actor), action,
                                 self.identifier(target), succeeded)
            
    def block(self, actor, action, target):
        sustained = False
        blocker = None
        character = None

        players = []
        if target is not None:
            players.append(target)
        else:
            players.extend(self.clockwise_players(actor))
            
        for potential in players:
            result = potential.block_action(
                self.identifier(actor), action,
                action.required_character(), self.identifier(target))
            if potential.active and result is not None:
                blocker = potential
                character = result

        if blocker is not None:
            log.event(blocker, "blocks", actor, "with", (character))
            if not self.challenge(blocker, Action.block, character, actor):
                sustained = True

            for player in self.players:
                player.notify_block(self.identifier(blocker), character,
                                    self.identifier(actor), action, sustained)
        
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
            log.event(challenger, "challenges", actor)
            revealed = actor.reveal(self.identifier(challenger), action,
                                    character, self.identifier(target))
            log.event(actor, "reveals", revealed)
            if character == revealed:
                log.event(actor, "wins the challenge")
                
                actor.hidden.remove(revealed)
                self.deck.place([revealed])
                actor.hidden.extend(self.deck.draw(1))
            else:
                log.event(challenger, "wins the challenge")
                actor.hidden.remove(revealed)
                actor.flipped.append(revealed)
                sustained = True
                
            self.update_state()
            for player in self.players:
                player.notify_challenge(
                    self.identifier(challenger), self.identifier(actor),
                    action, character, self.identifier(target), revealed)

            if sustained:
                self.flip(actor, revealed)
            else:
                self.flip(challenger)
                
        return sustained

    def flip(self, loser, character=None):
        if character is None:
            character = loser.flip()

        self.update_state()
        for player in self.players:
            player.notify_flip(self.identifier(loser), character)
            
        if len(loser.flipped) == 2:
            self._dataScraper.playerEliminated(loser.identifier, len(self.active_players()) + 1)
            
    
    def update_state(self):
        states = [PlayerState(x.identifier, x.coins, tuple(x.flipped))
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

