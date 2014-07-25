from interface import *

import random

class KeithBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def start(self):
        self.claims = {}

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden

    def notify_action(self, actor, action, target, succeeded):
        if action != Action.income and action != Action.foreign_aid:
            if actor not in self.claims:
                self.claims[actor] = {}
            if action not in self.claims[actor]:
                self.claims[actor][action] = 1
            else:
                self.claims[actor][action] += 1
        #if you exchange, all bets are off
        if action == Action.exchange:
            self.claims[actor] = {}

    def challenge(self, actor, action, character, target):
        #Mostly shamelessly stolen from Jake's bot
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1:
            return True

        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden

        if allKnown.count(character) == 3:
            return True

        #if the player has made more claims than they have cards,
        #they are clearly lying this most recent time
        if actor in self.claims:
            if len(self.claims[actor]) > 2:
                return True

        return False

    def take_action(self):
        if self.states[self.identifier].coins >= 7:
            active = [x.identifier for x in self.states if len(x.flipped) < 2]
            active.remove(self.identifier)
            target = random.choice(active)
            return TargetedAction(Action.coup, target)
        else:
            return Action.income
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        return None

    def flip(self):
        if len(self.hidden) > 1:
            if Character.contessa in self.hidden:
                if self.hidden[0] == Character.contessa:
                    return self.hidden[1]

        return self.hidden[0]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return KeithBot(identifier)
