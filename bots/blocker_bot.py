from interface import *

import random

class TurtleBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        
    def take_action(self):
            return Action.exchange
        
    def block_action(self, actor, action, character, target):
        if action == Action.assassinate:
           print("blocker bot: blocking assassinate")
           return Character.contessa
        return None

    def flip(self):
        prioritized = self._prioritize(self.hidden)
        if len(self.hidden) > 1:
            if Character.contessa in self.hidden:
                if self.hidden[0] == Character.contessa:
                    return self.hidden[1]

        return self.hidden[0]

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]
        

    def challenge(self, actor, action, character, target):
       	return False
        
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
    return TurtleBot(identifier)
