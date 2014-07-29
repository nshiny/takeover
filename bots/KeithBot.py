from interface import *

import random

class KeithBot(Bot):
    def __init__(self, identifier):
        self.identifier = identifier
        self.turn = 0

    def start(self):
        self.claims = {}
        self.turn = 1

    def update_state(self, states, hidden):
        self.states = states
        self.hidden = hidden

    def notify_action(self, actor, action, target, succeeded):
        if action != Action.income and action != Action.foreign_aid:
            if actor not in self.claims:
                self.claims[actor] = {}
                self.claims[actor]["canBeExtorted"] = False
                self.claims[actor]["canBeAssassinated"] = False

            if target not in self.claims:
                self.claims[target] = {}
                self.claims[target]["canBeExtorted"] = False
                self.claims[target]["canBeAssassinated"] = False
            if action not in self.claims[actor]:
                self.claims[actor][action] = 1
            else:
                self.claims[actor][action] += 1
        #if you exchange, all bets are off
        if action == Action.exchange:
            self.claims[actor] = {}
            self.claims[actor]["canBeExtorted"] = False
            self.claims[actor]["canBeAssassinated"] = False

        if succeeded and action == Action.extort:
            self.claims[target]["canBeExtorted"] = True

        if succeeded and action == Action.assassinate:
            self.claims[target]["canBeAssassinated"] = True

    def challenge(self, actor, action, character, target):
        #Mostly shamelessly stolen from Jake's bot
        if target == self.identifier and action == Action.assassinate and Character.contessa not in self.hidden and len(self.hidden) == 1:
            return True

        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden

        if allKnown.count(character) == 3:
            return True

        return False

    def take_action(self):
        self.turn += 1

        active = [x for x in self.states if len(x.flipped) < 2 and x.identifier != self.identifier]
        active.sort(key=lambda x: x.coins, reverse=True)
        active.sort(key=lambda x: len(x.flipped))
        target = active[0]

        #If you have 10+ dollars, you must coup some dude
        if self.states[self.identifier].coins >= 10:
            return TargetedAction(Action.coup, target.identifier)

        allKnown = []
        for x in self.states:
            allKnown += x.flipped
        allKnown += self.hidden

        #oh snap! I'm close to winning
        if len(active) == 1:
            #oh snap! they only have one influence left!
            if len(target.flipped) == 1:
                #well look at that, I can coup you now, DIE!
                if self.states[self.identifier].coins >= 7:
                    return TargetedAction(Action.coup, target.identifier)
            #if I'm pretty sure I can assassinate the last dude. Do so
            if Character.assassin in self.hidden and self.states[self.identifier].coins >= 3 and allKnown.count(Character.assassin) == 3:
                return TargetedAction(Action.assassinate, target.identifier)
            #if I'm pretty sure I can extort the last dude. Do so
            if Character.captain in self.hidden and (allKnown.count(Character.captain) == 3 or self.claims[target.identifier]["canBeExtorted"]) and target.coins >= 2:
                return TargetedAction(Action.extort, target.identifier)

        #ABD: Always Be Duking (round 1)
        if self.turn == 1 or (self.turn == 3 and Character.duke in self.hidden):
            return Action.tax
        #If you have a duke use it. But only if you won't be forced to coup
        if Character.duke in self.hidden and self.states[self.identifier].coins <= 6:
            return Action.tax
        #If you have the captain, extort someone who's been extorted before
        if Character.captain in self.hidden and allKnown.count(Character.captain) == 3:
            for y in active:
                if y.identifier in self.claims and self.claims[y.identifier]["canBeExtorted"] and y.coins >= 2:
                    return TargetedAction(Action.extort, y.identifier)
        #If you have 7 dollars, coup some dude
        if self.states[self.identifier].coins >= 7:
            return TargetedAction(Action.coup, target.identifier)
        #Turtle Turtle Turtle
        if allKnown.count(Character.duke) == 3:
            return Action.foreign_aid
        else:
            return Action.income
        
    def block_action(self, actor, action, character, target):
        if len(self.hidden) > 0 and action.blockable(self.hidden[0]):
            return self.hidden[0]

        if len(self.hidden) > 1 and action.blockable(self.hidden[1]):
            return self.hidden[1]

        return None

    def flip(self):
        if len(self.hidden) > 1:
            if Character.contessa in self.hidden:
                if self.hidden[0] == Character.contessa:
                    return self.hidden[1]

        return self.hidden[0]

    def reveal(self, challenger, action, character, target):
        if character in self.hidden:
            return character

        return self.flip()

    def prioritize(self, characters):
        prioritized = []
        prioritized.extend(
            [Character.contessa] * characters.count(Character.contessa))
        prioritized.extend(
            [Character.duke] * characters.count(Character.duke))
        prioritized.extend(
            [Character.captain] * characters.count(Character.captain))
        prioritized.extend(
            [Character.assassin] * characters.count(Character.assassin))
        prioritized.extend(
            [Character.ambassador] * characters.count(Character.ambassador))

        return prioritized

    def exchange(self, drawn):
        prioritized = self.prioritize(list(self.hidden) + list(drawn))
        return prioritized[-2:]

def make_bot(identifier):
    return KeithBot(identifier)
