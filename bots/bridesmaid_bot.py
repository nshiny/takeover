from interface import *

import random

class DrawBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
        return Action.exchange
    
    def exchange(self, drawn):
        return drawn
        
    def block_action(self, actor, action, character, target):
        return None

    def flip(self):
        return self.hidden[0]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return DrawBot(identifier)
