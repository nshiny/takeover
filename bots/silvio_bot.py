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

    def start(self):
        self.turn = 0
        
    def notify_flip(self, player, flipped):
        pass

    def notify_action(self, actor, action, target, succeeded):
        if Action.exchange == action:
            self.aCards = []
        if Action.extort == action:
            if succeeded and target != self.identifier:
                self.freeMoneys.append(target)
    
    def notify_block(self, blocker, character, actor, action, succeeded):
        if Action.extort == action and succeeded:
            if blocker in self.freeMoneys:
                self.freeMoneys.remove(blocker)
    
    def take_action(self):
        self.turn += 1
        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        # TODO 1v1 ME BRO
        if len(active) != 0:
            return self.take_group_action()

    def take_group_action(self):
        tg = [x for x in self.states if len(x.flipped) == 0 and x.identifier != self.identifier]
        og = [x for x in self.states if len(x.flipped) == 1 and x.identifier != self.identifier]
        if len(tg) > 0:
            target = self.pick_richest(tg)
        else:
            target = self.pick_richest(og)

        active = [x.identifier for x in self.states if len(x.flipped) < 2]
        coins = self.states[self.identifier].coins
        if  coins >= 7:
            return TargetedAction(Action.coup, target)
        if Character.duke in self.hidden:
            return Action.tax
        if Character.ambassador in self.hidden:
            return Action.exchange
        if len(self.hidden) == 2 and self.hidden[0] == self.hidden[1]:
            if self.hidden[0] in [Character.duke, Character.assassin]:
                return Action.exchange
        if Character.assassin in self.hidden and coins >= 3:
                if self.count_known(Character.contessa) > 0:
                    return TargetedAction(Action.assassinate, target)
        if Character.captain in self.hidden:
            if len(self.freeMoneys) > 0 and self.freeMoneys[0] in active and self.states[self.freeMoneys[0]].coins > 1:
                return TargetedAction(Action.extort, self.freeMoneys[0])
            return TargetedAction(Action.extort, target)
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
        self.aCards = drawn
        prioritized = self._prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]

    def reveal(self, challenger, action, character, taret):
        if character in self.hidden:
            return character

        return self.flip()

    def _prioritize(self, characters):
        prioritized = []
        pc = [Character.duke, Character.captain, Character.ambassador, Character.assassin, Character.contessa]
        duplicates = []
        
        for char in pc:
            if char in characters:
                prioritized.append(char)
            if characters.count(char) > 1:
                duplicates.extend([char] * (characters.count(char) - 1))

        #protect from badness
        for char in pc:
            if char in duplicates:
                prioritized.extend([char] * duplicates.count(char))

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
