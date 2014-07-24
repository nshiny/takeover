from interface import *

import random

class SilvioBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.known = []
        self.aCards = []
        self.freeMoneys = []

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden

    def notify_flip(self, player, flipped):
        pass

    def notify_action(self, actor, action, target, succeeded):
        if Action.exchange == action:
            self.aCards = []
        if Action.extort == action:
            if succeeded:
                self.freeMoneys.append(target)
            else:
                if target in self.freeMoneys:
                    self.freeMoneys.remove(target)
        
    def take_action(self):
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        if len(active) != 0:
            return self.take_group_action()

    def take_group_action(self):
        tg = [x for x in self.states if len(x.flipped) == 0]
        if self in tg: tg.remove(self)
        og = [x for x in self.states if len(x.flipped) == 1]
        if self in og: og.remove(self)
        if len(og) > 0:
            target = self.pick_richest(og)
        else:
            target = self.pick_richest(tg)

        coins = self.states[self.identifier].coins
        if len(self.freeMoneys) > 0:
            if self.freeMoneys[0].coins > 0:
                return TargetedAction(Action.extort, self.freeMoneys[0])
        if  coins >= 7:
            return TargetedAction(Action.coup, target)
        if Character.duke in self.hidden:
            return Action.tax
        if Character.ambassador in self.hidden:
            #love dat tess
            if Character.contessa not in self.hidden:
                return Action.exchange
        if len(self.hidden) == 2 and self.hidden[0] == self.hidden[1]:
            if self.hidden[0] in [Character.duke, Character.assassin]:
                return Action.exchange
        if Character.captain in self.hidden:
            return TargetedAction(Action.extort, target)
        if Character.assassin in self.hidden and coins >= 3:
                if self.count_known(Character.contessa) > 0:
                    return TargetedAction(Action.assassinate, target)
        if self.count_known(Character.duke) == 3:
            return Action.foreign_aid
        return Action.income

    def take_one_vs_one_action(self):
        print('yes')
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        if Action.assassinate == action and self.count_known(Character.contessa) == 0:
            return Character.contessa

        return None

    def challenge(self, actor, action, character, target):
        if self.count_known(character) == 3: return True
        return False

    def flip(self):
        if len(self.hidden) > 1:
            if Character.contessa in self.hidden:
                if self.hidden[0] == Character.contessa:
                    return self.hidden[1]

        return self.hidden[0]

    def exchange(self, drawn):
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        self.aCards = drawn
        return prioritized[-2:]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

    def _prioritize(self, characters):
        prioritized = []
        groi = None
        if len(self.hidden) == 2 and self.hidden[0] == self.hidden[1]:
            groi = self.hidden[0]

        pc = [Character.contessa, Character.duke, Character.ambassador, Character.captain, Character.assassin]

        for char in pc:
            if groi != char and char in characters:
                prioritized.extend([char])

        #protect from badness
        if len(prioritized) == 1:
            prioritized.extend([groi])

        return prioritized		
		
    def pick_richest(self, dudes):
        theDude = 'derp'
        mm = -100
        for dude in dudes:
            if dude.coins > mm:
                mm = dude.coins
                theDude = dude
        return theDude.identifier

    def count_known(self, character):
        count = 0
        knowns = []
        if len(self.hidden) == 2:
            knowns.extend([self.hidden[0], self.hidden[1]])
        if len(self.hidden) == 1:
            knowns.extend([self.hidden[0]])
        if len(self.aCards) > 0:
            knowns.extend(self.aCards)
        for state in self.states:
            knowns += state.flipped
        for char in knowns:
            if char == character:
                count+=1

        return count
			

def make_bot(identifier):
    return SilvioBot(identifier)
