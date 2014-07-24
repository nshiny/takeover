from interface import *

import random


class SteffBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.steffTurn = 0
        
    def start(self):
        self.steffTurn = 0

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
        self.steffTurn += 1 # every turn, increment the turn number

        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)
        target = random.choice(active)

        coins = self.states[self.identifier].coins

        if coins >= 7: # if we have at least 7 coins, always coup
            return TargetedAction(Action.coup, target)

        elif self.steffTurn <= 2: # for the first 2 turns, always tax (I don't understand why this is only 2 turns when it looks to me like I'm indicating 3)
            return Action.tax

        elif Character.duke in self.hidden: # if we have the duke, tax
            return Action.tax

        elif len(self.hidden) > 1: # if we have only one card left, exchange
            return Action.exchange

        else:
            return TargetedAction(Action.extort, target) # else: extort

    def challenge(self, actor, action, character, target):
        if action == Action.foreign_aid:
            if Character.duke in self.hidden:
               	return True
        else:
            return False
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        elif len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

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
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        
        return prioritized  

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]


    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return SteffBot(identifier)