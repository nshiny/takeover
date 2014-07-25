from interface import *

import random

class DukeOrDie(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.dukeTurn = 0
        
    def start(self):
        self.dukeTurn = 0

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
        self.dukeTurn += 1 # every turn, increment the turn number
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)
        target = random.choice(active)

        coins = self.states[self.identifier].coins

        if coins >= 7: # coup if we have 7 coins
            return TargetedAction(Action.coup, target)
        elif self.dukeTurn % 2 == 0 and Character.duke not in self.hidden:
            return Action.exchange
        else:
            return Action.tax

    def challenge(self, actor, action, character, target):
        if action == Action.foreign_aid:
            return True
        return False
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        return None

    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        
        return prioritized  

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]

    def flip(self):
        if Character.assassin in self.hidden:
            return Character.assassin
        if Character.contessa in self.hidden:
            return Character.contessa
        if Character.captain in self.hidden:
            return Character.captain
        if Character.ambassador in self.hidden:
            return Character.ambassador
        if Character.duke in self.hidden:
            return Character.duke

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return DukeOrDie(identifier)