from interface import *
from operator import itemgetter, attrgetter
import random

class SamBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.samTurn = 0
        self.coinage = []
        self.revealed = []
        self.active_fancy = []
        self.fancy_pantsers = []
        self.ordered_fancies = []
        self.them_not_me = []
        
    def start(self):
        self.samTurn = 0
        self.coinage = []
        self.revealed = []
        self.active_fancy = []
        self.fancy_pantsers = []
        self.ordered_fancies = []
        self.them_not_me = []

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        # self.revealed.extend([x.flipped for x in states])

    def take_action(self):
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)
        self.coinage = []
        self.revealed = []
        self.active_fancy = []
        self.fancy_pantsers = []
        self.ordered_fancies = []
        self.them_not_me = []
        coins = self.states[self.identifier].coins #determine how many coins I have
        for x in self.states: 
            self.coinage.append([x.coins, x.identifier]) # populate self.coinage with a list of [COINS, PLAYERS] lists
        self.ordered_fancies =  (sorted(self.coinage, key=itemgetter(0), reverse=True)) # sort coinage into sorted_coinage
        for x in self.ordered_fancies: #delete the coins out of ordered_fancies
            del x[0]
        self.them_not_me = self.ordered_fancies
        if ([self.identifier]) in self.them_not_me: self.them_not_me.remove([self.identifier]) # remove myself from self.them_not_me
        #self.fancy_pantser = (((sorted(self.sorted_coinage, key=itemgetter(0), reverse=True))[0])[1])
        #for x in self.fancy_pantser:
            #del x[1]
        #if ([self.identifier]) in self.fancy_pantser: self.fancy_pantser.remove([self.identifier])
        for x in active and self.them_not_me: #target only the active folks
            self.active_fancy.append(x)
        self.active_fanciest = self.active_fancy[0] #get only the richest
        target = ''.join(map(str, self.active_fanciest)) # turn it into a useable INT

        for x in self.states:
            self.revealed.extend(x.flipped)

        self.samTurn += 1 # every turn, increment the turn number
        target = random.choice(active)

        if coins >= 7: # coup if we have 7 coins
            return TargetedAction(Action.coup, target)
        elif self.samTurn == 1:
            return TargetedAction(Action.extort, target)
        elif Character.assassin in self.hidden and coins > 2: # assassinate if we can
            return TargetedAction(Action.assassinate, target)
        elif Character.captain in self.hidden: # if we have the captain, extort
            return TargetedAction(Action.extort, target)
        elif Character.duke in self.hidden: # if we have the duke, tax
            return Action.tax
        elif Character.captain not in self.hidden and len(self.hidden) >2 and self.samTurn % 2 == 0:
            return Action.exchange
        #elif Character.duke not in self.hidden: # if we don't have a duke, exchange until we do
            #return Action.exchange
        else:
            return Action.income

    def challenge(self, actor, action, character, target):
        #if action == Action.exchange and self.samTurn > 7 and Character.ambassador in self.hidden:
            #return True
        if action == Action.foreign_aid:
            if Character.duke in self.hidden:
                return True
        #if action == Action.block and character == Character.ambassador and self.samTurn > 7:
            #return True
        #if action == Action.block and character == Character.contessa and len(self.hidden) > 1:
            #return True
        return False
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]
            
        if action == Action.assassinate and len(self.hidden) > 1:
            return Character.contessa    

        return None

    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))

        
        return prioritized 

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]

    def flip(self):
        if Character.ambassador in self.hidden:
            return Character.ambassador
        if Character.captain in self.hidden:
            return Character.captain
        if Character.duke in self.hidden:
            return Character.duke
        if Character.assassin in self.hidden:
            return Character.assassin
        if Character.contessa in self.hidden:
            return Character.contessa

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

def make_bot(identifier):
    return SamBot(identifier)