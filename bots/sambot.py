from interface import *

import random

class SamBot(Bot):
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

        if coins >= 7: #coup if we have 7 coins
            return TargetedAction(Action.coup, target)
        elif Character.assassin in self.hidden and coins >= 3: #if we have the assasin and we have between 3 and 6 coin, assassinate
            return TargetedAction(Action.assassinate, target)
        elif Character.duke in self.hidden: # if we have the duke, tax
            return Action.tax
        elif Character.captain in self.hidden: # if we have the captain, extort
            return TargetedAction(Action.extort, target)
        elif Character.contessa not in self.hidden: # if we don't have a contessa, exchange until we do
            return Action.exchange
        else:
            return Action.income

    def challenge(self, actor, action, character, target):
        if action == Action.foreign_aid:
            if Character.duke in self.hidden:
               	return True
        if action == Action.extort:
            if Character.captain in self.hidden:
                return True
        if action == Action.tax:
            if Character.duke in self.hidden:
                return True
        if action == Action.block and character == Character.contessa and Character.contessa in self.hidden:
            return True
        if action == Action.block and character == Character.contessa and len(self.hidden) > 1:
            return True
        return False
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]
            
        if action == Action.assassinate and len(self.hidden) > 1:
            return Character.contessa    

        return None

    def flip(self):
        if len(self.hidden) > 1:
            if Character.contessa in self.hidden:
                if self.hidden[0] == Character.contessa:
                    return self.hidden[1]

        return self.hidden[0]

    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))

        
        return prioritized  

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]


    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return SamBot(identifier)