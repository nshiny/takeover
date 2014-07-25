from interface import *
import random
import copy
if 64 - 64: i11iIiiIii
class Kerpowski ( Bot ) :
 if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . _characterValueMap = {
 Character . duke : 10 ,
 Character . captain : 8 ,
 Character . contessa : 0 ,
 Character . assassin : 9 ,
 Character . ambassador : 3 }
  if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
  self . _contessaMap = None
  self . _likelyDukeMap = None
  if 87 - 87: OoOoOO00
  self . _numExchanges = 0
  self . _gameID = 0
  self . _turn = 0
  self . _winnerMap = None
  self . _earlyChallengeCount = 0
  if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
  self . _privateKnownExchangeCards = [ ]
  self . _publicKnownExchangeCards = [ ]
  if 73 - 73: OOooOOo / ii11ii1ii
  self . _newGame = True
  if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 def start ( self ) :
  self . _gameID += 1
  self . _turn = 1
  self . _newGame = True
  self . _contessaMap = None
  self . _likelyDukeMap = None
  if 97 - 97: oO0o0ooO0 - OO0O0O / ii1I * Ooo00oOo00o
  self . _privateKnownExchangeCards = [ ]
  self . _publicKnownExchangeCards = [ ]
  if 62 - 62: Oo - ii1I * ii11ii1ii
 def update_state ( self , states , hidden ) :
  self . states = states
  self . hidden = list ( hidden )
  if self . _contessaMap is None :
   self . _contessaMap = { x . identifier : False for x in states }
   if 24 - 24: ooO0OO000o % OoOO / Iii1I1
  if self . _winnerMap is None :
   self . _winnerMap = { x . identifier : 0 for x in states }
   if 46 - 46: Iii1I1 * ooO0OO000o / o0000oOoOoO0o * iIiiiI1IiI1I1 * OoOO0ooOOoo0O . ii11ii1ii
  Oo0oO0ooo = self . _get_active_players ( )
  if 56 - 56: ii11ii1ii - ii1I
  if self . _newGame == True :
   o00oOoo = None
   if len ( Oo0oO0ooo ) == 1 and len ( self . hidden ) == 0 :
    o00oOoo = Oo0oO0ooo [ 0 ] . identifier
   elif len ( Oo0oO0ooo ) == 0 :
    o00oOoo = self . identifier
    if 78 - 78: ii11ii1ii / OoOoOO00 - Iii1I1 . o0000oOoOoO0o
   if o00oOoo is not None :
    self . _winnerMap [ o00oOoo ] += 1
    self . _newGame = False
    if 91 - 91: Ooo00oOo00o * OO0O0O . o0000oOoOoO0o / OoOO
    if 87 - 87: ii1I / OoOO . OoOoOO00 * iiiii - o0000oOoOoO0o * oO0o0ooO0
 def _get_active_players ( self ) :
  return [ O0 for O0 in self . states if len ( O0 . flipped ) < 2 and O0 . identifier != self . identifier ]
  if 34 - 34: o0000oOoOoO0o % ooO0OO000o % OO0O0O % o0000oOoOoO0o * OoOO0ooOOoo0O / OOOo0
 def _safe_to_duke ( self ) :
  Iiii = self . _get_active_players ( )
  OOO0O = sorted ( Iiii , key = lambda O0 : O0 . coins , reverse = True )
  if len ( OOO0O ) <= 1 :
   return True
   if 94 - 94: oO0o0ooO0
  if OOO0O [ 1 ] . coins <= self . states [ self . identifier ] . coins :
   return True
   if 18 - 18: OO0O0O / ii11ii1ii + I1IiI / iIiiiI1IiI1I1 - ooO0OO000o - ii11ii1ii
  if OOO0O [ 0 ] . coins >= 7 and ( OOO0O [ 1 ] . coins - 3 <= self . states [ self . identifier ] . coins ) :
   return False
   if 1 - 1: ii11ii1ii - OOooOOo % Iii1I1 + IiII1IiiIiI1 - OoOO0ooOOoo0O / ii11ii1ii
  return True
  if 31 - 31: OoOoOO00 + ooO0OO000o
 def _easy_assassin ( self ) :
  if self . _get_public_known_cards ( ) . count ( Character . assassin ) < 2 and self . _get_known_cards ( ) . count ( Character . contessa ) == 3 and self . states [ self . identifier ] . coins >= 3 :
   return Action . assassinate
  return None
  if 13 - 13: OOooOOo * I1IiI * IiII1IiiIiI1
 def take_action ( self ) :
  self . _turn += 1
  if 55 - 55: ooO0OO000o
  Iiii = self . _get_active_players ( )
  if 43 - 43: OOOo0 - ii1I + o00O0oo + OoOO
  Iiii . sort ( key = lambda O0 : len ( O0 . flipped ) )
  Iiii . sort ( key = lambda O0 : self . _winnerMap [ O0 . identifier ] , reverse = True )
  if 17 - 17: Oo
  o00ooooO0oO = Iiii [ 0 ] . identifier
  if 63 - 63: OOOo0 % ii1I
  o0oOo0Ooo0O = self . _get_known_cards ( )
  if 81 - 81: Ooo00oOo00o * o0000oOoOoO0o * ii11ii1ii - OoOO0ooOOoo0O - Oo
  if self . _easy_assassin ( ) is not None :
   return TargetedAction ( Action . assassinate , o00ooooO0oO )
   if 90 - 90: ooO0OO000o + I1IiI / Oo % ooO0OO000o - Iii1I1
  if self . states [ self . identifier ] . coins >= 7 :
   return TargetedAction ( Action . coup , o00ooooO0oO )
  elif ( Character . assassin in self . hidden and self . states [ self . identifier ] . coins >= 3 and
 ( ( self . _contessaMap [ o00ooooO0oO ] == False and o0oOo0Ooo0O . count ( Character . contessa ) == 2 ) or o0oOo0Ooo0O . count ( Character . contessa ) == 3 ) ) :
   return TargetedAction ( Action . assassinate , o00ooooO0oO )
  elif Character . captain in self . hidden and 6 == ( o0oOo0Ooo0O . count ( Character . captain ) + o0oOo0Ooo0O . count ( Character . ambassador ) ) :
   if 29 - 29: Oo / OO0O0O
   return TargetedAction ( Action . extort , o00ooooO0oO )
  elif ( Character . duke not in self . hidden ) and self . _numExchanges < 1 and len ( self . hidden ) > 1 :
   if Character . ambassador in self . hidden or ( self . _earlyChallengeCount / self . _gameID < 0.1 and random . uniform ( 0 , 1 ) < 0.1 ) :
    self . _numExchanges += 1
    return Action . exchange
   elif self . _safe_to_duke ( ) and self . _earlyChallengeCount / self . _gameID < 0.1 and random . uniform ( 0 , 1 ) < 0.1 :
    return Action . tax
   else :
    return Action . income
  elif self . _safe_to_duke ( ) and ( Character . duke in self . hidden or ( o0oOo0Ooo0O . count ( Character . duke ) < 2 and self . _earlyChallengeCount / self . _gameID < 0.1 and random . uniform ( 0 , 1 ) < 0.9 ) ) :
   return Action . tax
  elif o0oOo0Ooo0O . count ( Character . duke ) == 3 :
   return Action . foreign_aid
   if 24 - 24: Iii1I1 % Oo + ii1I + o00O0oo + Ooo00oOo00o
  return Action . income
  if 70 - 70: iIiiiI1IiI1I1 % iIiiiI1IiI1I1 . o0000oOoOoO0o % OoOoOO00 * Oo % I1IiI
  if 23 - 23: i11iIiiIii + IiII1IiiIiI1
 def block_action ( self , actor , action , character , target ) :
  if 68 - 68: OOOo0 . I1IiI . i11iIiiIii
  if len ( self . hidden ) > 0 and action . blockable ( self . hidden [ 0 ] ) :
   return self . hidden [ 0 ]
   if 40 - 40: I1IiI . OOOo0 . iIiiiI1IiI1I1 . ii1I
  if len ( self . hidden ) > 1 and action . blockable ( self . hidden [ 1 ] ) :
   return self . hidden [ 1 ]
   if 33 - 33: OoOO + ooO0OO000o % i11iIiiIii . oO0o0ooO0 - IiII1IiiIiI1
  O00oooo0O = self . _get_public_known_cards ( )
  if 22 - 22: iiiii % ii11ii1ii - OoOO0ooOOoo0O . OO0O0O * i11iIiiIii
  if action == Action . extort and O00oooo0O . count ( Character . ambassador ) < 2 :
   return Character . ambassador
   if 32 - 32: iIiiiI1IiI1I1 * Iii1I1 % I1IiI % OoOO . o0000oOoOoO0o
  if action == Action . extort and O00oooo0O . count ( Character . captain ) < 2 :
   return Character . captain
   if 61 - 61: oO0o0ooO0
  if action == Action . assassinate :
   if Character . contessa in self . _privateKnownExchangeCards :
    return Character . contessa
   elif self . _turn < 6 :
    return Character . contessa
    if 79 - 79: iIiiiI1IiI1I1 + IiII1IiiIiI1 - OoOO0ooOOoo0O
    if 83 - 83: oO0o0ooO0
    if 64 - 64: OoOoOO00 % oO0o0ooO0 % OoOO0ooOOoo0O / OOOo0 - OoOoOO00
 def notify_action ( self , actor , action , target , succeeded ) :
  pass
  if 74 - 74: OoOO0ooOOoo0O * Iii1I1
  if 89 - 89: I1IiI + iIiiiI1IiI1I1
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  if action == Action . assassinate :
   self . _contessaMap [ blocker ] = succeeded
   if 3 - 3: ii1I / IiII1IiiIiI1 % ii11ii1ii * i11iIiiIii / Iii1I1 * ii11ii1ii
 def notify_flip ( self , player , flipped ) :
  pass
  if 49 - 49: I1IiI % OoOO + ii1I . IiII1IiiIiI1 % Ooo00oOo00o
 def notify_challenge ( self , challenger , actor , action ,
 character , target , revealed ) :
  if self . _turn < 3 :
   self . _earlyChallengeCount += 1
   if 48 - 48: ii11ii1ii + ii11ii1ii / ooO0OO000o / OO0O0O
  if character == revealed :
   self . _publicKnownExchangeCards = [ revealed ]
   self . _privateKnownExchangeCards = [ ]
   if 20 - 20: Oo
 def reveal ( self , challenger , action , character , target ) :
  if character in self . hidden :
   return character
   if 77 - 77: OOOo0 / ii11ii1ii
  return self . flip ( )
  if 98 - 98: OO0O0O / ii1I / i11iIiiIii / Oo
 def challenge ( self , actor , action , character , target ) :
  if target == self . identifier and action == Action . assassinate and Character . contessa not in self . hidden and len ( self . hidden ) == 1 :
   return True
   if 28 - 28: OOooOOo - o0000oOoOoO0o . o0000oOoOoO0o + OOOo0 - iiiii + Iii1I1
  if self . _get_known_cards ( ) . count ( character ) == 3 :
   return True
   if 95 - 95: OoOoOO00 % I1IiI . Iii1I1
  return False
  if 15 - 15: oO0o0ooO0 / OoOO . OoOO - ii1I
 def flip ( self ) :
  self . _rankCards ( self . hidden )
  return self . hidden [ - 1 ]
  if 53 - 53: o0000oOoOoO0o + IiII1IiiIiI1 * I1IiI
 def exchange ( self , drawn ) :
  OooOooooOOoo0 = self . hidden + list ( drawn )
  if 71 - 71: o00O0oo % I1IiI % OOooOOo
  self . _privateKnownExchangeCards = list ( drawn )
  self . _rankCards ( OooOooooOOoo0 )
  if 94 - 94: I1IiI - OoOO0ooOOoo0O * Iii1I1
  if OooOooooOOoo0 [ 0 ] == OooOooooOOoo0 [ 1 ] :
   OooOooooOOoo0 [ 1 ] , OooOooooOOoo0 [ 2 ] = OooOooooOOoo0 [ 2 ] , OooOooooOOoo0 [ 1 ]
   if 17 - 17: Ooo00oOo00o % ooO0OO000o
  self . _privateKnownExchangeCards = copy . copy ( OooOooooOOoo0 [ - 2 : ] )
  self . _publicKnownExchangeCards = [ ]
  if 13 - 13: o00O0oo % OOOo0 - i11iIiiIii . IiII1IiiIiI1 + ooO0OO000o
  if 10 - 10: Ooo00oOo00o * oO0o0ooO0 * ooO0OO000o % OoOO . OOooOOo + o00O0oo
  return OooOooooOOoo0 [ - 2 : ]
  if 19 - 19: OOOo0 - IiII1IiiIiI1 . OOooOOo / o0000oOoOoO0o
 def _get_public_known_cards ( self ) :
  I11II = [ ]
  for O0 in self . states :
   I11II += O0 . flipped
  I11II += self . _publicKnownExchangeCards
  return I11II
  if 32 - 32: OoOoOO00 * Oo
 def _get_known_cards ( self ) :
  o0oOo0Ooo0O = self . _get_public_known_cards ( )
  o0oOo0Ooo0O += self . _privateKnownExchangeCards
  return o0oOo0Ooo0O
  if 99 - 99: OoOoOO00 - iIiiiI1IiI1I1 / I1IiI % OoOO
 def _rankCards ( self , cardList ) :
  II1i1IiiIIi11 = copy . deepcopy ( self . _characterValueMap )
  if 47 - 47: OoOO0ooOOoo0O
  o0oOo0Ooo0O = self . _get_known_cards ( )
  if 50 - 50: ooO0OO000o - oO0o0ooO0 * Ooo00oOo00o / o00O0oo + Oo
  if o0oOo0Ooo0O . count ( Character . contessa ) == 3 :
   II1i1IiiIIi11 [ Character . assassin ] = 20
  if ( o0oOo0Ooo0O . count ( Character . captain ) + o0oOo0Ooo0O . count ( Character . ambassador ) ) == 6 :
   II1i1IiiIIi11 [ Character . captain ] = 20
   if 88 - 88: OoOO / o00O0oo + OoOO0ooOOoo0O - ooO0OO000o / oO0o0ooO0 - OOOo0
  cardList . sort ( key = lambda O0 : II1i1IiiIIi11 [ O0 ] , reverse = True )
  return cardList
  if 15 - 15: Ooo00oOo00o + OOOo0 - iiiii / OOooOOo
  if 58 - 58: i11iIiiIii % ii11ii1ii
  if 71 - 71: OOooOOo + oO0o0ooO0 % i11iIiiIii + Ooo00oOo00o - o0000oOoOoO0o

def make_bot ( identifier ) :
 return Kerpowski ( identifier )