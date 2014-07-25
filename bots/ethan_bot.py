from interface import *
from operator import *

import random

class EthanBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def start(self):
        """Reset all the things!"""
        pass
        
    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
        # active = [x.identifier for x in self.states if x.identifier != self.identifier and len(x.flipped) < 2]
        # activeAndRich = active = [x.identifier for x in self.states if x.identifier != self.identifier and len(x.flipped) < 2 and x.coins > 0]
        # if len(activeAndRich) > 0:
            # target = activeAndRich[0]
        # else:
            # target = random.choice(active)
        target = self._other_players()[0].identifier

        coins = self.states[self.identifier].coins
        
        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden

        if coins >= 7:
            return TargetedAction(Action.coup, target)
        if Character.duke in self.hidden:
            return Action.tax
        elif Character.captain not in self.hidden and allKnown.count(Character.captain) < 3:
            return Action.exchange
        else:
            return TargetedAction(Action.extort, target)
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        # if action == Action.assassinate: #and Character.contessa in self.hidden:
            # return Character.contessa
            
        return None

    def challenge(self, actor, action, character, target):
        if action == Action.exchange and Character.ambassador in self.hidden:
            return True
        if action == Action.extort and Character.captain in self.hidden:
            return True
        else:
            return False
    
    def flip(self):
        prioritized = self._prioritize(self.hidden)
        # print("Prioritized: " + str(prioritized))
        return prioritized[-1]

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        # print("Prioritized: " + str(prioritized))
        return prioritized[-2:]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

    def challenge(self, actor, action, character, target):
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1:
            return True
        
        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden
        
        if allKnown.count(character) == 3:
            return True
        
        return False
        
    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        
        return prioritized
    
    def _other_players(self):
        targetList = [x for x in self.states if x.identifier != self.identifier and len(x.flipped) < 2]
        targetList = sorted(targetList, key=attrgetter('coins'), reverse=True)
        targetList = sorted(targetList, key=lambda x: len(x.flipped))
        #print("Target List is: " + str(targetList))
        
        return targetList

def make_bot(identifier):
    return EthanBot(identifier)
