"""Chris's first bot"""
__author__ = 'chriskwan'

from interface import *

import random

class ChrisBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden

    def take_action(self):
        if self.states[self.identifier].coins >= 7:
            active = [x.identifier for x in self.states if len(x.flipped) < 2]
            active.remove(self.identifier)
            target = random.choice(active)
            return TargetedAction(Action.coup, target)
        else:
            return Action.income

    def block_action(self, actor, action, character, target):
        block_with = None

        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            block_with = self.hidden[0]

        elif len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            block_with = self.hidden[1]

        # if you are targeted, but you don't have it, just lie
        elif len(self.hidden) > 0 and target == self.identifier:
            # if you don't have it, just lie
            if (action == Action.assassinate):
                block_with = Character.contessa
            elif (action == Action.extort):
                block_with = Character.captain

        return block_with

    def flip(self):
        if len(self.hidden) > 1:
            return self.hidden[1]
        return self.hidden[0]

    def reveal(self, challenger, action, character, target):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return ChrisBot(identifier)