from interface import *
import random

class Kerpowski(Bot):

    def __init__(self, identifier):
        self.identifier = identifier
        self._characterValueMap = {
            Character.duke:10,
            Character.assassin:9,
            Character.contessa:8,
            Character.captain:7,
            Character.ambassador:1}
        self._contessaMap = None

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = list(hidden)
        if self._contessaMap is None:
            self._contessaMap = {x.identifier:False for x in states}

                
    def take_action(self):
        active = [x for x in self.states if len(x.flipped) < 2 and x.identifier != self.identifier]
        
        # primarily attack players with two cards, secondarily attack the player with the most coins 
        active.sort(key=lambda x: x.coins, reverse=True)
        active.sort(key=lambda x: len(x.flipped))
        target = active[0].identifier

        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden
        
        if self.states[self.identifier].coins >= 7:
            return TargetedAction(Action.coup, target)
        elif (Character.assassin in self.hidden and self.states[self.identifier].coins >= 3 and 
                (self._contessaMap[target] == False or allKnown.count(Character.contessa) == 3)):
            return TargetedAction(Action.assassinate, target)
        elif Character.captain in self.hidden and 6 == (allKnown.count(Character.captain) + allKnown.count(Character.ambassador)):
            # we have an unblockable captain!
            return TargetedAction(Action.extort, target)
        elif Character.duke not in self.hidden and allKnown.count(Character.duke) < 3:
            if Character.ambassador in self.hidden or random.uniform(0, 1) < 0.05:
                return Action.exchange
            elif random.uniform(0, 1) < 0.05:
                return Action.tax
            else:
                return Action.income
        elif Character.duke in self.hidden:
            return Action.tax
        elif allKnown.count(Character.duke) == 3:
            return Action.foreign_aid
        else:
            return Action.income
            

    def block_action(self, actor, action, character, target):
        if action == Action.assassinate: #and Character.contessa in self.hidden:
            return Character.contessa                                    
        else:
            return None

    def notify_action(self, actor, action, target, succeeded):
        pass    
            
    # TODO: not used currently, may be implemented later
    def notify_block(self, blocker, character, actor, action, succeeded):
        if action == Action.assassinate:
            self._contessaMap[blocker] = succeeded

    def reveal(self, challenger, action, character, target):
        if character in self.hidden:
            return character

        return self.flip()

    def challenge(self, actor, action, character, target):
        if action == Action.block and character == Character.assassin:
            self._contessaMap[blocker] = succeeded
        
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1:
            return True
        return False
    
    def flip(self):            
        self.hidden.sort(key=lambda x: self._characterValueMap[x], reverse=True) 
        return self.hidden[-1]
    
    def exchange(self, drawn):
        totalCards = self.hidden + list(drawn)
        totalCards.sort(key=lambda x: self._characterValueMap[x], reverse=True)
        if totalCards[0] == totalCards[1]:
            totalCards[1], totalCards[2] = totalCards[2], totalCards[1]
            
        return totalCards[-2:]
            
            
            

def make_bot(identifier):
    return Kerpowski(identifier)
