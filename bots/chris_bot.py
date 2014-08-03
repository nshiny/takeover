"""Chris's first bot"""
__author__ = 'chriskwan'

from interface import *

import random

class ChrisBot(Bot):
    def __init__(self, identifier, verbose=False):
        self.verbose = verbose # whether to print output
        self.identifier = identifier
        self.last_actor = None # person that last acted, i.e. person to your right
        self.last_couped_me = None

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden

    def take_action(self):
        if self.last_couped_me is None:
            self.log_print("### No one last couped me")
        else:
            self.log_print("### Last couped me: %d" % self.last_couped_me)
        if self.states[self.identifier].coins >= 7:
            target = self.choose_target()
            return TargetedAction(Action.coup, target)
        else:
            return Action.income

    def choose_target(self):
        # play with emotions
        if self.is_active(self.last_couped_me):
            self.log_print("### Coup for a coup")
            return self.last_couped_me
        # the person to your right
        elif self.is_active(self.last_actor):
            self.log_print("### Couping the person on my right")
            return self.last_actor
        else:
            self.log_print("### Couping some poor random soul")
            return self.choose_random_target()

    def is_active(self, player_id):
        if player_id is None:
            return False
        return len(self.states[player_id].flipped) < 2

    def choose_random_target(self):
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)
        target = random.choice(active)
        return target

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

    def notify_action(self, actor, action, target, succeeded):
        self.last_actor = actor

        if (action == Action.coup and target == self.identifier):
            self.log_print("### I've been couped!")
            self.last_couped_me = actor

    def flip(self):
        if len(self.hidden) > 1:
            return self.hidden[1]
        return self.hidden[0]

    def reveal(self, challenger, action, character, target):
        if character in self.hidden:
            return character

        return self.flip()

    def log_print(self, message):
        if self.verbose:
            print(message)

def make_bot(identifier):
    return ChrisBot(identifier)
