from collections import namedtuple
from enum import Enum


class Character(Enum):
    duke = 1
    assassin = 2
    ambassador = 3
    captain = 4
    contessa = 5

    def short(self):
        return short_characters[self]


class Action(Enum):
    income = 1
    foreign_aid = 2
    coup = 3
    tax = 4
    assassinate = 5
    exchange = 6
    extort = 7
    block = 8

    def challengeable(self):
        """Returns true if this action can be challenged."""
        return self in required_characters

    def required_character(self):
        """Returns the Character required for this action, or None."""
        if not self.challengeable():
            return None

        return required_characters[self]

    def blockable(self, character=None):
        """With no arguments, returns if this action is blockable."
        Otherwise, returns if the specified Character blocks this action."""
        if character is None:
            return self in blocked_actions.values()

        if character not in blocked_actions:
            return False
        
        return blocked_actions[character] == self


short_characters = {Character.duke : "Dk",
                    Character.assassin : "As",
                    Character.ambassador : "Am",
                    Character.captain : "Cp",
                    Character.contessa : "Cn"}


required_characters = {Action.tax : Character.duke,
                       Action.assassinate: Character.assassin,
                       Action.exchange : Character.ambassador,
                       Action.extort : Character.captain}


blocked_actions = {Character.duke : Action.foreign_aid,
                   Character.ambassador : Action.extort,
                   Character.captain : Action.extort,
                   Character.contessa : Action.assassinate}


TargetedAction = namedtuple("TargetedAction", ["action", "target"])


PlayerState = namedtuple("PlayerState", ["identifier", "coins", "flipped"])


class Bot:
    def start(self):
        """Invoked on each bot at the start of a new game.
        Followed by the first update_state call."""
        pass
    
    def take_action(self):
        """Invoked at the beginning of this bot's turn.
        Return an Action or a TargetedAction."""
        pass

    def block_action(self, actor, action, character, target):
        """Invoked whenever there's an opportunity for this bot to block.
        Return the character to block with if desired, otherwise None."""
        pass

    def challenge(self, actor, action, character, target):
        """Invoked for each bot after a challengable action is declared.
        If multiple bots attempt to challenge, the closest clockwise to
        the actor will issue the challenge.
        This method doubles as notification for attemped actions and
        blocks, and is still called even on eliminated bots.
        Return true to challenge, false otherwise."""           
        return False

    def notify_action(self, actor, action, target, succeeded):
        """Invoked for each bot after an action resolves. Succeeded
        is false if the action was blocked or successfully challenged,
        and true otherwise."""
        pass

    def notify_challenge(self, challenger, actor, action,
                         character, target, revealed):
        """Invoked for each bot after a challenge has been decided.
        If revealed != character, the challenge was sustained."""
        pass

    def notify_flip(self, player, flipped):
        """Invoked for each bot after a player loses influence."""
        pass

    def update_state(self, states, hidden):
        """Invoked for each bot whenever the game state changes.
        States is an iterable of the PlayerState for each player.
        Hidden is an iterable of Characters that are this bot's hand."""
        pass

    def flip(self):
        """Invoked when this bot loses influence.
        Return the Character to flip."""
        pass

    def exchange(self, drawn):
        """Invoked when this bot resolves an exchange action.
        Drawn is an iterable of Characters.
        Return a sequence of two Characters to discard."""
        pass

    def reveal(self, challenger, action, character, target):
        """Invoked when this bot must reveal a character for a challenge.
        If the revealed character is not the required one, it is flipped.
        If it is the required one, it is replaced with a new card.
        Returns a character from this bot's hidden hand."""
        pass
