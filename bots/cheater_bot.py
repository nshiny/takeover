from interface import *
from game import *
from operator import *

import random
import time


players = list()
b = Bot()
drawn = ""
players.append(Player(0,b,drawn))
players.append(Player(1,b,drawn))
players.append(Player(2,b,drawn))
players.append(Player(3,b,drawn))
players.append(Player(4,b,drawn))
players.append(Player(5,b,drawn))
actions = { Action.income: 0, Action.foreign_aid: 0, Action.coup: 0, Action.tax: 0, Action.assassinate: 0, Action.exchange : 0, Action.extort : 0, Action.block : 0 }

#allKnown = {"Duke": 0, "Assassin": 0, "Captain": 0, "Ambassador": 0, "Contessa": 0}

actionList = list()
actionList.append(actions)
actionList.append(actions)
actionList.append(actions)
actionList.append(actions)
actionList.append(actions)
actionList.append(actions)


# TODO record character actions to figure out strategies and adapt.

allKnown = {}

class StuBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        #print("I AM: " + str(identifier) + ": cheater_bot")
        #return 0
        self.hidden = []
        self.roundCount = 0
        self.gameCount = 0
        self.totalRoundCount = 1
        self.claims = {}
        self.myActions = {}
        self.winners = {}
        self.winners[0] = 0
        self.winners[1] = 0
        self.winners[2] = 0
        self.winners[3] = 0
        self.winners[4] = 0
        self.winners[5] = 0
        self.winners[6] = 0
        self.winners.pop(self.identifier, None)
 
        for x in actions:
            self.myActions[x] = {}
            self.myActions[x]["success"] = 0
        #print (self.myActions)
        #time.sleep(5)

    def start(self):
        self.roundCount = 1
        self.gameCount += 1
        #print(self.winners)
        #time.sleep(15)
        #maxWinner = max(self.winners.keys, key=lambda x: self.winners[x] )
        maxWinner = max(self.winners.keys() , key=lambda x: self.winners[x] )

        #print(maxWinner)
        #time.sleep(5)
        
    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden
        self.roundCount += 1
        allKnown = self._setKnownStates()
        ##print(allKnown)
        
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        #print (active)
        #print ("len:" +str(len(active)))
        if len(active) == 1:
            #print ("winner:" + str(active[0]))
            self.winners[active[0]] += 1
            #time.sleep(5)
        
        for state in states:
           players[state.identifier].PlayerState = state

        
        prioritized = self._prioritize(hidden)

    def notify_action(self, actor, action, target, succeeded):
        self.totalRoundCount += 1
        actionList[actor][action] += 1
        #print (actionList[actor])
        
        #Shamelessly stolen from Keiths's bot
        if actor not in self.claims:
            self.claims[actor] = {}
        if action not in self.claims[actor]:
            self.claims[actor][action] = 1
        else:
            self.claims[actor][action] += 1
        #print (self.claims[actor])

    def take_action(self):
        allKnown = self._setKnownStates()
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        active.remove(self.identifier)

        numberOfCoins = 7
        ##print("numberOfCoins: " + str(numberOfCoins))
	
	#TODO, duke if i have duke, if 2 dukes, exchange.

        target = random.choice(active)
        
        targets = [x for x in self.states if len(x.flipped) == 0 and x.coins >= 3 and x.identifier != self.identifier ]
        targets = sorted(targets, key=attrgetter('coins'), reverse=True)
        targets2 = [x for x in self.states if len(x.flipped) == 0 and x.identifier != self.identifier ]
        targets3 = [x for x in self.states if x.identifier != self.identifier and len(x.flipped) != 2]
        targets3 = sorted(targets3, key=attrgetter('coins'), reverse=True)

        coupTarget = None
        try:
            #remove all non valid keys
            #coupTargets = [x for x in self.winners if x.key != self.identifier ]
            coupTargets = []
            coupUser = -1
            for x in self.winners:
                #print (x)
                if x != self.identifier and x in active and self.winners[x] > coupUser:
                   coupUser = x 
            #print (coupUser)
            coupTarget = coupUser #max(coupTargets.keys() , key=lambda x: coupTargets[x] )
            #print("HERE!!!!!!!!!!!")
            #print (self.winners)
                            
        except:
            print("oops")
                    
        #print (coupTarget)
        for mytarget in players:
            if len(targets) >= 1:
                #print("found a good sucker")
                target = random.choice(targets).identifier
                
            elif len(targets2) >= 1:
                #print("found an ok sucker")
                target = random.choice(targets2).identifier
            elif len(targets3) >= 1:
                target = random.choice(targets3).identifier
                #print (self.states[targets3[0].identifier].flipped[0] == Character.captain)
                #print (self.states[targets3[0].identifier].flipped)
                #time.sleep(5)
                #print("found a sucker")
        '''
        targets = [x for x in self.states if x.identifier != self.identifier and len(x.flipped) < 2]
        targets = sorted(targets, key=attrgetter('coins'), reverse=True)
        targets = sorted(targets, key=lambda x: len(x.flipped))
        target = targets[0].identifier
	'''
        if coupTarget == None:
            time.sleep(5)
            print("no coup target")
            coupTarget = target
           
	#coup mode
        #if Character.assassin in self.hidden and self.states[self.identifier].coins >= 3 and allKnown[Character.contessa] == 3 and len(active) == 1:
        #    #print ("XXXXXXX   no risk assassin    XXXXXXXX")
        #    return TargetedAction(Action.assassinate, target)
        if(self.gameCount % 3 == 0):
            coupTarget = target
            target = coupTarget
        if self.states[self.identifier].coins >= numberOfCoins:
            active = [x.identifier for x in self.states if len(x.flipped) < 2]
            active.remove(self.identifier)
            #print("coup")
            return TargetedAction(Action.coup, coupTarget)
        elif Character.captain not in self.hidden and allKnown[Character.captain] < 2:
            return Action.exchange
        elif allKnown[Character.duke] < 2:
            return Action.tax
        elif Character.captain in self.hidden:
            return TargetedAction(Action.extort, target)
        elif Character.assassin in self.hidden and self.states[self.identifier].coins >= 3:
            return TargetedAction(Action.assassinate, target)
        elif allKnown[Character.duke] == 3:
            return Action.foreign_aid
        else:
            return Action.income


    def block_action(self, actor, action, character, target):
        ##print("got here")
        willBlock = None
        
       	allKnown = self._setKnownStates()
        if target == actor:
            return None
        # block with Contessa if only one card
        if target == self.identifier and action == Action.assassinate and len(self.hidden) == 1:
            return Character.contessa
       	
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            if action == Action.assassinate and target != self.identifier:
                return None
            else:
                willBlock = self.hidden[0]
        if len(self.hidden) > 1 and action.blockable(self.hidden[1]) and target == self.identifier:
            if action == Action.assassinate and target != self.identifier:
                return None
            else:
                willBlock = self.hidden[1]
        #always challenge with 1 card left???
        '''if len(self.hidden) > 1 and action.challengeable() and allKnown[action.required_character()] <= 2 and target == self.identifier:
            ##print("got here!!!!!")
            ##print (action.required_character())
            #willBlock = action.required_character()
            willBlock = None
        '''

        if action == Action.extort and allKnown[Character.ambassador] < 3 and target == self.identifier:
           willBlock = Character.ambassador
        elif action == Action.extort and allKnown[Character.captain] < 2 and target == self.identifier:
           willBlock = Character.captain


        #if action == Action.export and target == self.identifier
        
        if len(self.hidden) == 0:
            ##print (self.hidden)
            #time.sleep(30)
            willBlock = None
            #print("cannot block: out of game :(")
            
        #if willBlock != None:
        #   ##print ("ACTION WILLBLOCK:character: " + str(character) + " - action: " +str(action))

        return willBlock

    def challenge(self, actor, action, character, target):
        ##print ("CHALLENGE:character: " + str(character) + " - action: " +str(action))

       	allKnown = self._setKnownStates()
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1 and allKnown[Character.contessa] < 3:
            return True

       	willChallenge = False

       	if allKnown[character] == 3:
       	    return True
       	    #print("can't fool me")

       	if action == Action.block and character == Character.contessa and len(self.states[actor].flipped) >= 1 and  self.states[actor].flipped[0] == Character.contessa:
            return True
            # probably didn't have double contessa
            #print(actor)
            #print(target)
            #print(self.states[actor].flipped)
            #time.sleep(10)
       	
       	#XXXXXtesting::::
       	#if action == Action.tax and allKnown[Character.duke] >= 2 and target != self.identifier:
       	#    willChallenge = True
       	#willChallenge = False
       	
       	if willChallenge:
       	   willChallenge = willChallenge
       	   #print ("CHALLENGE:character: " + str(character) + " - action: " +str(action) + ": " + str(willChallenge))
           #time.sleep(5)
       	return willChallenge
 
   
        
    def flip(self):
        
        prioritized = self._prioritize(self.hidden)
        return prioritized[-1]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]

    def _prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        
        return prioritized

    def _probOfCharacter(character):
       knownCharacterCounts = self._setKnownStates()
       totalCards = 15
       unknownCards = totalCards -  count(knownCharacterCounts)
       countOfUnknownCharacterCard = knownCharacterCounts.count(character)

    def _setKnownStates(self):
       foo = []
       for x in self.states:
           foo += x.flipped
           
       foo += self.hidden
       
       #dukeCount = foo.count(Character.duke)
       ##print (dukeCount)
       
       knownCharacterCounts = {x:foo.count(x) for x in Character} # TODO this is wrong, get how to enumerate states from an Enum
       
       ##print (knownCharacterCounts[Character.assassin])
       return knownCharacterCounts 
       #knownCharacterCounts[Character.duke]
       
       #allKnown = {"Duke": 0, "Assassin": 0, "Captain": 0, "Ambassador": 0, "Contessa": 0}

       for x in self.states:
              for y in x.flipped:
       	       ##print (y)
       	       if Character.duke == y:
       	          allKnown["Duke"] += 1
       	       if Character.assassin == y:
       	          allKnown["Assassin"] += 1
       	       if Character.captain == y:
       	          allKnown["Captain"] += 1
       	       if Character.ambassador == y:
       	          allKnown["Ambassador"] += 1
       	       if Character.contessa == y:
       	          allKnown["Contessa"] += 1
              for y in hidden:
       	       ##print (y)
       	       if Character.duke == y:
       	          allKnown["Duke"] += 1
       	       if Character.assassin == y:
       	          allKnown["Assassin"] += 1
       	       if Character.captain == y:
       	          allKnown["Captain"] += 1
       	       if Character.ambassador == y:
       	          allKnown["Ambassador"] += 1
       	       if Character.contessa == y:
       	          allKnown["Contessa"] += 1

       return allKnown

    def _probOfCharacter(self,character):
        knownCharacterCounts = self._setKnownStates()
        totalCards = 15
        unknownCards = totalCards -  len(knownCharacterCounts)
        countOfUnknownCharacterCard = 3 - (self._howManyOf(character))
        probabiliityOfCharacter = (countOfUnknownCharacterCard/(unknownCards)) * 100.0 * 2
        #print("#unknowncards:" + str(unknownCards) + "----unknownforchar:" + str(countOfUnknownCharacterCard))
        return probabiliityOfCharacter

    def _howManyOf(self,character):
        foo = []
        for x in self.states:
            foo += x.flipped
        foo += self.hidden
        return foo.count(character)


#find probability of influence card

def make_bot(identifier):
    return StuBot(identifier)
