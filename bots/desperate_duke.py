from interface import *

import random

class DesperateDuke(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)
        target = random.choice(active)

        coins = self.states[self.identifier].coins

        if coins >= 7:
            return TargetedAction(Action.coup, target)
        elif Character.assassin in self.hidden and coins >= 3:
            return TargetedAction(Action.assassinate, target)
        elif Character.duke not in self.hidden:
            return Action.exchange
        else:
            return Action.tax
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        return None

    def flip(self):
        prioritized = self._prioritize(self.hidden)
        return prioritized[-1]

    def exchange(self, drawn):
        prioritized = self._prioritize(self.hidden + drawn)
        return prioritized[-2:]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        
        return prioritized

def make_bot(identifier):
    return DesperateDuke(identifier)
