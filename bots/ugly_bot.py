from interface import *

from collections import namedtuple, Counter
import itertools
import random


NUM_PLAYERS = 6
DIAGNOSTICS = False


def invoke_listeners(target):
    def internal(self, *args, **kwargs):
        self.listeners.invoke(target.__name__, *args, **kwargs)
        return target(self, *args, **kwargs)

    return internal


def combine_probabilities(iterable):
    result = 1
    for x in iterable:
        result *= 1 - x
    return 1 - result


class Tactics:
    def __init__(self, state, cards, challenges, dangers):
        self._state = state
        self._dangers = dangers
        self._challenges = challenges
        self._cards = cards
        
        self._current_choice = None
        self._current_outcome = None
        
        self._choices = []
        self._choices.append(self.easy_assassinate)
        self._choices.append(self.early_assassinate)
        self._choices.append(self.takeover)
        self._choices.append(self.unblockable_captain)
        self._choices.append(self.claim_duke)
        self._choices.append(self.easy_foreign_aid)
        self._choices.append(self.income)
        
        self._outcomes = {x.__name__ : Counter() for x in self._choices}

    def decide(self):
        self._current_outcome = {"attempted" : 1}
        for choice in self._choices:
            result = choice()
            if result is not None:
                self._current_name = choice.__name__
                return result

    def _claim_character(self, character, target):
        if character in self._state.hidden:
            return True

        if self._state.influence() == 1:
            return False

        # Bots will eventually not be this braindead.
        if self._cards.remaining(character) == 0:
            return False

        challenged = 0
        if character is Character.duke:
            challenged = combine_probabilities(
                [self._challenges.expect_challenge(x, Character.duke)
                 for x in self._state.other_players()])
        else:
            challenged = self._challenges.expect_challenge(target, character)

        return challenged < 0.01

    def easy_assassinate(self):
        if self._state.coins() >= 3:
            for target in self._dangers.prioritized(
                self._cards.without(Character.contessa)):
                if Character.assassin in self._state.hidden:
                    return TargetedAction(Action.assassinate, target)

    def early_assassinate(self):
        if self._state.coins() >= 3:
            for target in self._dangers.prioritized(
                [x for x in self._state.other_players()
                 if self._state.influence(x) > 1]):
                if Character.assassin in self._state.hidden:
                    return TargetedAction(Action.assassinate, target)

    def takeover(self):
        if self._state.coins() >= 7:
            target = self._dangers.target()
            return TargetedAction(Action.coup, target)

    def unblockable_captain(self):
        captain_target = self._dangers.target(
            [x for x in self._state.other_players()
             if self._cards.absent(x, Character.captain) and
             self._cards.absent(x, Character.ambassador) and
             self._state.coins(x) >= 2])
        if captain_target is not None:
            if self._claim_character(Character.captain, captain_target):              
                return TargetedAction(Action.extort, captain_target)

    def claim_duke(self):
        if self._claim_character(Character.duke, None):
            return Action.tax

    def easy_foreign_aid(self):
        if self._cards.remaining(Character.duke) == 0:
            return Action.foreign_aid
        
    def income(self):
        return Action.income

    def notify_action(self, actor, action, target, succeeded):
        if actor == self._state.identifier:
            self._current_outcome["succeeded"] = int(succeeded)
            self._outcomes[self._current_name].update(self._current_outcome)

    def notify_block(self, blocker, character, actor, action, succeeded):
        if actor == self._state.identifier:
            self._current_outcome["blocked"] = 1
            self._current_outcome["denied"] = int(succeeded)
        
    def notify_challenge(self, challenger, actor, action,
                         character, target, revealed):
        if actor == self._state.identifier:
            self._current_outcome["challenged"] = 1
            self._current_outcome["sustained"] = int(character != revealed)

        if challenger == self._state.identifier:
            self._current_outcome["responded"] = 1
            self._current_outcome["smacked"] = int(character != revealed)

    def notify_end(self):
        if not DIAGNOSTICS:
            return
        
        for k, v in self._outcomes.items():
            print(k)
            for x, y in v.items():
                print("   ", x, y)
            print("")

        print("")


class UglyBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.listeners = ListenerManager()

        self.state = StateTracker(identifier)
        self.listeners.add(self.state)
        
        self.cards = CardTracker()
        self.listeners.add(self.cards)

        self.challenges = ChallengeTracker()
        self.listeners.add(self.challenges)

        self.dangers = DangerTracker(self.state)
        self.listeners.add(self.dangers)

        self.tactics = Tactics(
            self.state, self.cards, self.challenges, self.dangers)
        self.listeners.add(self.tactics)

    @invoke_listeners
    def start(self):
        pass

    @invoke_listeners
    def take_action(self):     
        return self.tactics.decide()

    @invoke_listeners
    def block_action(self, actor, action, character, target):
        blockers = [x for x in self.state.hidden if action.blockable(x)]
        if len(blockers) > 0:
            return blockers[0]

        if action == Action.assassinate and self.state.influence() == 1:
            return Character.contessa

        return None

    @invoke_listeners
    def challenge(self, actor, action, character, target):        
        remaining = self.cards.remaining(character)
        
        if remaining == 0:
            return True

        # It's okay to fall for the long Kwan.
        if self.cards.absent(actor, character):
            return True
        
        return False

    @invoke_listeners
    def notify_action(self, actor, action, target, succeeded):
        pass

    @invoke_listeners
    def notify_block(self, blocker, character, actor, action, succeeded):
        pass
        
    @invoke_listeners
    def notify_challenge(self, challenger, actor, action,
                         character, target, revealed):
        pass                

    @invoke_listeners
    def notify_flip(self, player, flipped):
        pass

    @invoke_listeners
    def notify_end(self):
        pass

    @invoke_listeners
    def update_state(self, states, hidden):
        pass

    def flip(self): 
        priority = [Character.duke,
                    Character.captain,
                    Character.contessa,
                    Character.assassin,
                    Character.ambassador]

        for worst in reversed(priority):
            if worst in self.state.hidden:
                return worst

    def exchange(self, drawn):
        pass

    def reveal(self, challenger, action, character, taret):
        if character in self.state.hidden:
            return character

        return self.flip()


class ChallengeTracker:
    def __init__(self):
        self._attempted_challenges = {x : Counter() for x in range(NUM_PLAYERS)}
        self._potential_challenges = {x : Counter() for x in range(NUM_PLAYERS)}

    def expect_challenge(self, challenger, character):
        if self._potential_challenges[challenger][character] > 0:
            if(self._attempted_challenges[challenger][character] > 5 or
                self._potential_challenges[challenger][character] > 50):
                return (self._attempted_challenges[challenger][character] /
                        self._potential_challenges[challenger][character])

        # Definitely the current meta; might not be correct.
        return 0

    def challenge(self, actor, action, character, target):
        # Conflates challenging actions with challenging blocks.
        
        if target is not None:
            # Pretends nobody will challenge actions that target others.
            self._potential_challenges[target].update([character])
        else:
            for x in range(NUM_PLAYERS):
                self._potential_challenges[x].update([character])
        
    def notify_challenge(self, challenger, actor, action,
                         character, target, revealed):
        if target is None or challenger == target:
            self._attempted_challenges[challenger].update([character])


class DangerTracker:
    def __init__(self, state):
        self._state = state
        self._placed = Counter()
        self._killers = Counter()
        self._attacks = Counter()
        self._survived = Counter()
        self._last = None

    def target(self, players=None):
        if players is None:
            players = self._state.other_players()
            
        prioritized = self.prioritized(players)
        if len(prioritized) > 0:
            return prioritized[0]

        return None

    def prioritized(self, players):
        scores = {}
        for player in players:
            score = self._state.coins(player)
            
            if self._state.influence(player) > 1:
                score += 6

            if self.killer(player) > 1.05:
                score += 3
            elif self.survival(player) > 1.05:
                score += 2

            scores[player] = score
        
        return [x[0] for x in sorted(
            scores.items(), key=lambda x: x[1], reverse=True)]

    def survival(self, player):
        total = sum(self._survived.values())
        if total == 0 or player not in self._survived:
            return 1

        survivors = {x[0] : x[1] / total for x in self._survived.items()}
        mean = sum(x for x in survivors.values()) / len(survivors)
        result = survivors[player] / mean
        
        return result

    def killer(self, player):
        total = sum(self._killers.values())
        if total == 0 or player not in self._killers:
            return 1

        killers = {x[0] : x[1] / total for x in self._killers.items()}
        mean = sum(x for x in killers.values()) / len(killers)
        return killers[player] / mean 
        print(result)
        return result

    def notify_action(self, actor, action, target, succeeded):
        if self._state.turn == self._last:
            if target == self._state.identifier and succeeded:
                if action in [Action.coup, Action.assassinate]:
                    self._killers.update([actor])
                    self._attacks.update([action])

    def notify_flip(self, player, flipped):
        if player == self._state.identifier:
            if self._state.influence() == 0:
                self._last = self._state.turn
                self._survived.update(self._state.other_players())
                self._placed.update([len(self._state.other_players())])

        if self._state.other_players() == 0:
             self._placed.update([0])

    def notify_end(self):
        if not DIAGNOSTICS:
            return
        
        print("placed")
        for k, v in self._placed.items():
            print("   ", k, v)
        print("")
        
        print("killers")
        for k, v in self._killers.items():
            print("   ", k, v)
        print("")

        print("survivals")
        for k, v in self._survived.items():
            print("   ", k, v)
        print("")

        print("attacks")
        for k, v in self._attacks.items():
            print("   ", k, v)
        print("")


class CardTracker:
    def __init__(self):
        self.start()
        
    def without(self, character):
        return [k for k, v in self._absent.items() if v == character]

    def absent(self, player, character):
        return character in self._absent[player]

    def remaining(self, character):
        deck = 15 - (NUM_PLAYERS * 2)
        return deck - sum(1 for x in self.unavailable() if x == character)

    def unavailable(self):
        return itertools.chain(self._hidden, self.visible())

    def visible(self):
        return [x for x in self._visible.values()]

    def start(self):
        self._hidden = None
        self._visible = None
        self._absent = None
        self._claimed = None
    
    def challenge(self, actor, action, character, target):
        self._claimed[actor].add(action.required_character())    

    def notify_action(self, actor, action, target, succeeded):
        if succeeded and action == Action.exchange:
            self._reset_cards(actor)

        if succeeded and action.blockable() and target is not None:
            blockers = [x[0] for x in blocked_actions.items()
                        if x[1] == action]
            self._absent[target].update(blockers)

    def notify_block(self, blocker, character, actor, action, succeeded):
        self._claimed[blocker].add(character)

    def notify_challenge(self, challenger, actor, action,
                         character, target, revealed):
        if revealed != character:
            self._lose_card(actor, revealed)
            # Nobody would dare pull the long Kwan!
            self._absent[actor].add(character)
        else:
            self._reset_cards(actor)

    def notify_flip(self, player, flipped):
        self._lose_card(player, flipped)
        
    def update_state(self, states, hidden):
        if self._hidden is None:
            self._hidden = []
            self._visible = {x.identifier : [] for x in states}
            self._absent = {x.identifier : set() for x in states}
            self._claimed = {x.identifier : set() for x in states}
            
        self._visible = {x.identifier : x.flipped for x in states}
        self._hidden = list(hidden)
        
    def _reset_cards(self, player):
        self._absent[player] = set()
        self._claimed[player] = set()
        
    def _lose_card(self, player, character):
        # Doesn't account for the chance they had a pair.
        self._claimed[player].discard(character)

        if len(self._visible[player]) >= 2:
            self._reset_cards(player)


class StateTracker:
    def __init__(self, identifier):
        self.identifier = identifier
        self.round = -1
        self.hidden = None
        self._states = None
        self.start()

    def coins(self, player=None):
        if player is None:
            player = self.identifier
                          
        return [x.coins for x in self._states
                if x.identifier == player][0]
    
    def influence(self, player=None):
        if player is None:
            player = self.identifier
                          
        return [2 - len(x.flipped) for x in self._states
                if x.identifier == player][0]

    def other_players(self):
        return [x.identifier for x in self._states if len(x.flipped) < 2
                and x.identifier != self.identifier]

    def start(self):
        self.turn = 0

    def update_state(self, states, hidden):
        self._states = states
        self.hidden = hidden
    

class ListenerManager:
    def __init__(self):
        self._listeners = []

    def add(self, listener):
        self._listeners.append(listener)

    def invoke(self, name, *args, **kwargs):
        for listener in self._listeners:
            method = getattr(listener, name, None)
            if method is not None:
                method(*args, **kwargs)


def make_bot(identifier):
    return UglyBot(identifier)
