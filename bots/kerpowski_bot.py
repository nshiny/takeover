from interface import *
import random
import copy

class Kerpowski(Bot):

    def __init__(self, identifier):
        self.identifier = identifier
        self._characterValueMap = {
            Character.duke:10,
            Character.captain:8,
            Character.contessa:2,
            Character.assassin:4,
            Character.ambassador:1}
        
        self._contessaMap = None
        self._numExchanges = 0
        self._gameID = 0
        self._turn = 0
        
    def start(self):
        self._gameID += 1
        self._turn = 1
        
    def update_state(self, states, hidden):
        self.states = states
        self.hidden = list(hidden)
        if self._contessaMap is None:
            self._contessaMap = {x.identifier:False for x in states}

                
    def take_action(self):
        self._turn += 1
        
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
                ((self._contessaMap[target] == False and allKnown.count(Character.contessa) == 2) or allKnown.count(Character.contessa) == 3)):
            return TargetedAction(Action.assassinate, target)
        elif Character.captain in self.hidden and 6 == (allKnown.count(Character.captain) + allKnown.count(Character.ambassador)):
            # we have an unblockable captain!
            return TargetedAction(Action.extort, target)
        elif (Character.duke not in self.hidden) and self._numExchanges < 1 and len(self.hidden) > 1:
            if Character.ambassador in self.hidden or random.uniform(0, 1) < 0.25:
                self._numExchanges += 1
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
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]
        
        if action == Action.assassinate: #and Character.contessa in self.hidden:
            return Character.contessa                                    


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
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1:
            return True
            
        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden
        
        if allKnown.count(character) == 3:
            return True
            
        return False
    
    def flip(self):            
        self._rankCards(self.hidden)
        return self.hidden[-1]
    
    def exchange(self, drawn):
        totalCards = self.hidden + list(drawn)
        self._rankCards(totalCards)
        
        if totalCards[0] == totalCards[1]:
            totalCards[1], totalCards[2] = totalCards[2], totalCards[1]
    
        return totalCards[-2:]

    def _rankCards(self, cardList):
        valueMap = copy.deepcopy(self._characterValueMap)

        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden

        if len([x for x in self.states if len(x.flipped) < 2 and x.identifier != self.identifier]) < 4:
            if allKnown.count(Character.contessa) == 3:
                valueMap[Character.assassin] = 11
            if (allKnown.count(Character.captain) + allKnown.count(Character.ambassador)) == 6:
                valueMap[Character.captain] = 11
        
        cardList.sort(key=lambda x: valueMap[x], reverse=True)
        return cardList
            
            

def make_bot(identifier):
    return Kerpowski(identifier)
