#true cheater bot
from interface import *
from operator import *
if 64 - 64: i11iIiiIii
import random
import copy
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from collections import namedtuple , Counter
import itertools
if 73 - 73: II111iiii
IiII1IiiIiI1 = 6
iIiiiI1IiI1I1 = False
if 87 - 87: OoOoOO00
if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
class o0OOO ( Bot ) :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  if 13 - 13: ooOo + Ooo0O
 def start ( self ) :
  pass
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  if 97 - 97: oO0o0ooO0 - IIII / I1IiI - oO0o0ooO0
 def update_state ( self , states , hidden ) :
  self . states = states
  self . hidden = hidden
  if 21 - 21: OOOo0 / II111iiii % I1Ii111 / Ooo00oOo00o . IIII
 def take_action ( self ) :
  if 100 - 100: i1IIi
  if 27 - 27: o00O0oo * OoooooooOO + IiII * IIII - i11iIiiIii - ooOoO0o
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - Ooo0O
  if 72 - 72: II111iiii - Ooo00oOo00o
  if 91 - 91: Oo . i11iIiiIii / Ooo0O % IiII / Oo - i11iIiiIii
  if 8 - 8: I1IiI * ooOo * iIii1I11I1II1 . o00O0oo / o00O0oo % o00O0oo
  i11 = self . _other_players ( ) [ 0 ] . identifier
  if 41 - 41: oO0o0ooO0 . IIII * o00O0oo % i11iIiiIii
  o000o0o00o0Oo = self . states [ self . identifier ] . coins
  if 80 - 80: OoooooooOO . OoOoOO00
  OOO0O = [ ]
  for oo0ooO0oOOOOo in self . states :
   OOO0O += oo0ooO0oOOOOo . flipped
  OOO0O += self . hidden
  if 71 - 71: oO0o0ooO0
  if o000o0o00o0Oo >= 7 :
   return TargetedAction ( Action . coup , i11 )
  if Character . duke in self . hidden :
   return Action . tax
  elif Character . captain not in self . hidden and OOO0O . count ( Character . captain ) < 3 :
   return Action . exchange
  else :
   return TargetedAction ( Action . extort , i11 )
   if 54 - 54: iII111i % O0 + OoOoOO00 - ooOoO0o / IiII
 def block_action ( self , actor , action , character , target ) :
  if len ( self . hidden ) > 0 and action . blockable ( self . hidden [ 0 ] ) :
   return self . hidden [ 0 ]
   if 31 - 31: Oo + II111iiii
  if len ( self . hidden ) > 1 and action . blockable ( self . hidden [ 1 ] ) :
   return self . hidden [ 1 ]
   if 13 - 13: iII111i * Ooo0O * OoOoOO00
   if 55 - 55: II111iiii
   if 43 - 43: Ooo00oOo00o - i1IIi + oO0o0ooO0 + I1Ii111
   if 17 - 17: I1IiI
  return None
  if 64 - 64: I1Ii111 % i1IIi % OoooooooOO
 def challenge ( self , actor , action , character , target ) :
  if action == Action . exchange and Character . ambassador in self . hidden :
   return True
  if action == Action . extort and Character . captain in self . hidden :
   return True
  else :
   return False
   if 3 - 3: ooOoO0o + O0
 def flip ( self ) :
  I1Ii = self . _prioritize ( self . hidden )
  if 66 - 66: I1Ii111
  return I1Ii [ - 1 ]
  if 78 - 78: Oo
 def exchange ( self , drawn ) :
  I1Ii = self . _prioritize ( list ( self . hidden ) + list ( drawn ) )
  if 18 - 18: O0 - ooOoO0o / ooOoO0o + IIII % IIII - o00O0oo
  return I1Ii [ - 2 : ]
  if 62 - 62: ooOoO0o - o00O0oo - Ooo00oOo00o % i1IIi / Ooo0O
 def reveal ( self , challenger , action , character , taret ) :
  if character in self . hidden :
   return character
   if 77 - 77: II111iiii - II111iiii . OoOoOO00 / I1IiI
  return self . flip ( )
  if 14 - 14: IiII % O0
 def challenge ( self , actor , action , character , target ) :
  if target == self . identifier and action == Action . assassinate and Character . contessa not in self . hidden and len ( self . hidden ) == 1 :
   return True
   if 41 - 41: i1IIi + oO0o0ooO0 + iII111i - o00O0oo
  OOO0O = [ ]
  for oo0ooO0oOOOOo in self . states :
   OOO0O += oo0ooO0oOOOOo . flipped
  OOO0O += self . hidden
  if 77 - 77: OOOo0 . o00O0oo % IIII
  if OOO0O . count ( character ) == 3 :
   return True
   if 42 - 42: Ooo0O - i1IIi / i11iIiiIii + iII111i + Oo
  return False
  if 17 - 17: Ooo0O . OOOo0 . ooOo
 def _prioritize ( self , characters ) :
  I1Ii = [ ]
  I1Ii . extend (
 [ Character . captain ] * characters . count ( Character . captain ) )
  I1Ii . extend (
 [ Character . duke ] * characters . count ( Character . duke ) )
  I1Ii . extend (
 [ Character . ambassador ] * characters . count ( Character . ambassador ) )
  I1Ii . extend (
 [ Character . contessa ] * characters . count ( Character . contessa ) )
  I1Ii . extend (
 [ Character . assassin ] * characters . count ( Character . assassin ) )
  if 3 - 3: Ooo00oOo00o . OOOo0 . OoOoOO00 / I1Ii111
  return I1Ii
  if 38 - 38: II111iiii % i11iIiiIii . IIII - iII111i + I1Ii111
 def _other_players ( self ) :
  Ooooo0Oo00oO0 = [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . states if oo0ooO0oOOOOo . identifier != self . identifier and len ( oo0ooO0oOOOOo . flipped ) < 2 ]
  Ooooo0Oo00oO0 = sorted ( Ooooo0Oo00oO0 , key = attrgetter ( 'coins' ) , reverse = True )
  Ooooo0Oo00oO0 = sorted ( Ooooo0Oo00oO0 , key = lambda oo0ooO0oOOOOo : len ( oo0ooO0oOOOOo . flipped ) )
  if 12 - 12: iIii1I11I1II1 * OoOoOO00 . IIII % IiII + O0
  if 70 - 70: I1Ii111 . Ooo0O * IIII . I1Ii111
  return Ooooo0Oo00oO0
  if 35 - 35: I1IiI + ooOoO0o + ooOoO0o
class I11I11i1I ( Bot ) :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . fuscat1 = [ ]
  self . Chri1 = { 0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 }
  self . Chri2 = { 0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 }
  self . Niswanob2 = { 0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 }
  self . fuscat2 = 0
  self . bitboostdotcom1 = False
  self . Chri4 = self . Chri1
  self . fuscat3 = { 0 : 1 , 1 : 4 , 2 : 6 , 3 : 3 , 4 : 3 }
  self . bitboostdotcom2 = { 0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 }
  self . ordemo1 = False
  self . bitboostdotcom3 = 0
  self . Chri3 = True
 def update_state ( self , fuscat5 , ordemo3 ) :
  self . fuscat5 = fuscat5
  self . ordemo3 = ordemo3
  self . Chri4 = self . Niswanob2
  ii11i1iIII = [ Ii1I . identifier for
 Ii1I in self . fuscat5 if ( len ( Ii1I . flipped ) < 2 ) ]
  if ( len ( ii11i1iIII ) <= 1 ) :
   self . Chri1 [ ii11i1iIII [ 0 ] ] += 1
   self . fuscat1 = [ ]
   if ( self . bitboostdotcom1 == False ) :
    self . Chri1 [ 0 ] += 1
    self . bitboostdotcom1 = True
 def start ( self ) :
  self . fuscat2 += 1
  self . bitboostdotcom1 = False
  self . ordemo2 = { 0 : [ ] , 1 : [ ] , 2 : [ ] , 3 : [ ] , 4 : [ ] , 5 : [ ] }
  self . Niswanob4 = 0
 def Chri5 ( self ) :
  Oo0o0 = [ ]
  for III1ii1iII in self . fuscat5 :
   Oo0o0 += III1ii1iII . flipped
  Oo0o0 += self . ordemo3
  Oo0o0 += self . fuscat1
  return Oo0o0
 def fuscat6 ( self , Chri6 ) :
  Chri6 . sort ( key = ( lambda oo0oooooO0 : oo0oooooO0 . coins ) , reverse = True )
  Chri6 . sort ( key = ( lambda i11Iiii : len ( i11Iiii . flipped ) ) )
  Chri6 . sort ( key = ( lambda iI : self . Chri1 [ iI . identifier ] ) , reverse = True )
  return Chri6
 def take_action ( self ) :
  I1i1I1II = self . Chri5 ( )
  i1 = [ ]
  for IiIiiI in self . fuscat5 :
   i1 += IiIiiI . flipped
  I1I = [ IiIiiI for IiIiiI in self . fuscat5 if
 ( ( len ( IiIiiI . flipped ) < 2 ) and ( IiIiiI . identifier != self . identifier ) ) ]
  oOO00oOO = self . fuscat6 ( I1I )
  OoOo = oOO00oOO [ 0 ] . identifier
  if ( len ( I1I ) == 2 ) :
   I1I . sort ( key = ( lambda iIo00O : iIo00O . coins ) , reverse = True )
   I1I . sort ( key = ( lambda OOO0OOO00oo : len ( OOO0OOO00oo . flipped ) ) )
   OoOo = I1I [ 0 ] . identifier
  elif ( len ( I1I ) == 1 ) :
   pass
  Iii111II = self . fuscat5 [ self . identifier ] . coins
  iiii11I = None
  Ooo0OO0oOO = None
  for ii11i1 in oOO00oOO [ 1 : ] :
   IIIii1II1II = ii11i1 . identifier
   if ( ( iiii11I == None ) and ( Character . assassin in self . ordemo2 [ IIIii1II1II ] ) ) :
    iiii11I = IIIii1II1II
   if ( ( Ooo0OO0oOO == None ) and ( Character . ambassador in self . ordemo2 [ IIIii1II1II ] ) and ( Character . captain in self . ordemo2 [ IIIii1II1II ] ) ) :
    Ooo0OO0oOO = IIIii1II1II
  self . Chri4 = self . Chri2
  if ( Iii111II >= 7 ) :
   return TargetedAction ( Action . coup , OoOo )
  elif ( ( Character . assassin in self . ordemo3 ) and ( Iii111II >= 3 ) and ( ( I1i1I1II . count ( Character . contessa ) == 3 ) or ( Character . contessa in self . ordemo2 [ OoOo ] ) ) ) :
   return TargetedAction ( Action . assassinate , OoOo )
  elif ( ( Character . captain in self . ordemo3 ) and ( self . fuscat5 [ OoOo ] . coins >= 1 ) and ( ( 6 == ( I1i1I1II . count ( Character . captain ) + I1i1I1II . count ( Character . ambassador ) ) ) or ( ( Character . captain in self . ordemo2 [ OoOo ] ) and ( Character . ambassador in self . ordemo2 [ OoOo ] ) ) ) ) :
   return TargetedAction ( Action . extort , OoOo )
  elif ( self . Chri3 and ( i1 . count ( Character . duke ) <= 1 ) ) :
   self . Niswanob4 += 1
   return Action . tax
  elif ( ( Character . ambassador in self . ordemo3 ) and ( len ( self . fuscat1 ) == 0 ) ) :
   return Action . exchange
  elif ( Character . duke in self . ordemo3 ) :
   return Action . tax
  elif ( ( iiii11I != None ) and ( Character . assassin in self . ordemo3 ) and ( Iii111II >= 3 ) ) :
   return TargetedAction ( Action . assassinate , iiii11I )
  elif ( ( Ooo0OO0oOO != None ) and ( Character . captain in self . ordemo3 ) ) :
   return TargetedAction ( Action . extort , Ooo0OO0oOO )
  elif ( I1i1I1II . count ( Character . duke ) == 3 ) :
   return Action . foreign_aid
  else :
   return Action . income
  return Action . income
 def notify_action ( self , bitboostdotcomF , Chri7 , NiswanobA , Chri8 ) :
  self . fuscat3 [ 0 ] = ( self . fuscat3 [ 1 ] * 2 )
  if ( ( NiswanobA == self . identifier ) and ( Chri7 == Action . coup ) ) :
   self . bitboostdotcom2 [ bitboostdotcomF ] += 1
  if ( bitboostdotcomF == self . identifier ) :
   return
  if ( ( Chri7 == Action . exchange ) and ( Chri8 == True ) ) :
   self . ordemo2 [ bitboostdotcomF ] = [ ]
   self . fuscat1 = [ ]
  if ( ( NiswanobA != None ) and ( self . Niswanob2 [ NiswanobA ] == 0 ) ) :
   if ( ( Chri7 == Action . assassinate ) and ( Chri8 == True ) ) :
    self . ordemo2 [ NiswanobA ] . append ( Character . contessa )
   if ( ( Chri7 == Action . extort ) and ( Chri8 == True ) ) :
    self . ordemo2 [ NiswanobA ] . append ( Character . captain )
    self . ordemo2 [ NiswanobA ] . append ( Character . ambassador )
  if ( ( Chri7 == Action . foreign_aid ) and ( Chri8 == True ) ) :
   for i1I1iI in range ( 5 ) :
    if ( self . Niswanob2 [ i1I1iI ] == 0 ) :
     self . ordemo2 [ i1I1iI ] . append ( Character . duke )
  self . fuscat3 [ 0 ] = ( self . fuscat3 [ 0 ] * 4 )
 def notify_challenge ( self , bitboostdotcomE , fuscatB , ordemo5 , ordemo7 , Chri9 , fuscatA ) :
  if ( fuscatB == self . identifier ) :
   pass
  if ( ordemo7 == fuscatA ) :
   self . fuscat1 = [ ]
  if ( Chri9 == None ) :
   pass
  if ( fuscatA in self . ordemo2 [ fuscatB ] ) :
   self . Niswanob2 [ fuscatB ] = 1
   self . ordemo2 [ fuscatB ] = [ ]
 def block_action ( self , Niswanob9 , ordemo8 , bitboostdotcom10 , fuscatC ) :
  oo0OooOOo0 = self . Chri5 ( )
  if ( ( len ( self . ordemo3 ) > 0 ) and ordemo8 . blockable ( self . ordemo3 [ 0 ] ) ) :
   return self . ordemo3 [ 0 ]
  if ( ( len ( self . ordemo3 ) > 1 ) and ordemo8 . blockable ( self . ordemo3 [ 1 ] ) ) :
   return self . ordemo3 [ 1 ]
  if ( ( ordemo8 == Action . assassinate ) and ( oo0OooOOo0 . count ( Character . contessa ) != 3 ) ) :
   return Character . contessa
  return None
 def ChriA ( self ) :
  o0O = 5
  for O00oO in self . fuscat5 :
   if ( len ( O00oO . flipped ) >= 2 ) :
    o0O -= 1
  self . Chri2 [ o0O ] += 1
  self . bitboostdotcom1 = True
 def flip ( self ) :
  if ( len ( self . ordemo3 ) == 1 ) :
   self . ChriA ( )
  I11i1I1I = self . NiswanobD ( self . ordemo3 )
  return I11i1I1I [ ( - 1 ) ]
 def exchange ( self , fuscatD ) :
  oO0Oo = self . NiswanobD ( ( list ( self . ordemo3 ) + list ( fuscatD ) ) )
  if ( len ( self . ordemo3 ) == 1 ) :
   self . fuscat1 = oO0Oo [ 1 : ]
  else :
   self . fuscat1 = oO0Oo [ 2 : ]
  return oO0Oo [ : 2 ]
 def reveal ( self , bitboostdotcom12 , bitboostdotcom11 , NiswanobC , ChriD ) :
  if ( NiswanobC in self . ordemo3 ) :
   return NiswanobC
  elif ( NiswanobC == Character . duke ) :
   if ( self . Niswanob4 == 1 ) :
    self . bitboostdotcom3 += 1
    if ( self . fuscat2 > 10 ) :
     if ( self . bitboostdotcom3 > ( self . fuscat2 / 2 ) ) :
      self . Chri3 = False
  return self . flip ( )
 def challenge ( self , NiswanobE , ChriF , ordemoA , NiswanobF ) :
  oOOoo0Oo = self . Chri5 ( )
  if ( oOOoo0Oo . count ( ordemoA ) == 3 ) :
   return True
  if ( ( ordemoA in self . ordemo2 [ NiswanobE ] ) and ( self . Niswanob2 [ NiswanobE ] == 0 ) ) :
   return True
  if ( ( NiswanobF == self . identifier ) and ( ChriF == Action . assassinate ) and ( Character . contessa not in self . ordemo3 ) and ( len ( self . ordemo3 ) == 1 ) ) :
   return True
  return False
 def NiswanobD ( self , bitboostdotcom13 ) :
  o00OO00OoO = [ ]
  OOOO0OOoO0O0 = [ ]
  O0Oo000ooO00 = [ oO0 for oO0 in self . fuscat5 if
 ( ( len ( oO0 . flipped ) < 2 ) and ( oO0 . identifier != self . identifier ) ) ]
  Ii1iIiII1ii1 = [ Character . contessa , Character . ambassador , Character . captain , Character . assassin , Character . duke ]
  ooOooo000oOO = self . Chri5 ( )
  if ( ooOooo000oOO . count ( Character . assassin ) == 3 ) :
   Ii1iIiII1ii1 . remove ( Character . contessa )
   Ii1iIiII1ii1 . append ( Character . contessa )
  if ( ooOooo000oOO . count ( Character . contessa ) == 3 ) :
   Ii1iIiII1ii1 . remove ( Character . assassin )
   Ii1iIiII1ii1 . insert ( 0 , Character . assassin )
  for Oo0oOOo in Ii1iIiII1ii1 :
   if ( Oo0oOOo in bitboostdotcom13 ) :
    o00OO00OoO . append ( Oo0oOOo )
    if ( bitboostdotcom13 . count ( Oo0oOOo ) > 1 ) :
     OOOO0OOoO0O0 . extend ( ( [ Oo0oOOo ] * ( bitboostdotcom13 . count ( Oo0oOOo ) - 1 ) ) )
  for Oo0oOOo in Ii1iIiII1ii1 :
   if ( Oo0oOOo in OOOO0OOoO0O0 ) :
    o00OO00OoO . extend ( ( [ Oo0oOOo ] * OOOO0OOoO0O0 . count ( Oo0oOOo ) ) )
  return o00OO00OoO
  if 58 - 58: II111iiii * iII111i * ooOo / iII111i
  if 75 - 75: Ooo0O
def I1III ( target ) :
 def OO0O0OoOO0 ( self , * args , ** kwargs ) :
  self . listeners . invoke ( target . __name__ , * args , ** kwargs )
  return target ( self , * args , ** kwargs )
  if 10 - 10: OoooooooOO % iIii1I11I1II1
 return OO0O0OoOO0
 if 54 - 54: oO0o0ooO0 - II111iiii % Ooo00oOo00o % IiII % iIii1I11I1II1 + IIII
 if 15 - 15: IiII * IIII * OOOo0 % i11iIiiIii % Ooo00oOo00o - iII111i
def O0ooo0O0oo0 ( iterable ) :
 oo0oOo = 1
 for oo0ooO0oOOOOo in iterable :
  oo0oOo *= 1 - oo0ooO0oOOOOo
 return 1 - oo0oOo
 if 89 - 89: Ooo00oOo00o
 if 68 - 68: Oo * OoooooooOO % O0 + Oo + IIII
class i11i1I1 :
 def __init__ ( self , state , cards , challenges , dangers ) :
  self . _state = state
  self . _dangers = dangers
  self . _challenges = challenges
  self . _cards = cards
  if 36 - 36: iIii1I11I1II1 / Ooo00oOo00o * iII111i
  self . _current_action = { }
  self . _current_block = { }
  self . _current_response = { }
  if 65 - 65: I1Ii111 . iIii1I11I1II1 / O0 - I1Ii111
  self . _actions = [ ]
  self . _actions . append ( self . obvious_assassinate )
  self . _actions . append ( self . takeover )
  self . _actions . append ( self . early_assassinate )
  self . _actions . append ( self . unblockable_captain )
  self . _actions . append ( self . claim_duke )
  self . _actions . append ( self . obvious_foreign_aid )
  self . _actions . append ( self . income )
  if 21 - 21: OoOoOO00 * iIii1I11I1II1
  self . _blocks = [ ]
  self . _blocks . append ( self . obvious_block )
  self . _blocks . append ( self . final_contessa )
  if 91 - 91: o00O0oo
  self . _responses = [ ]
  self . _responses . append ( self . obvious_response )
  self . _responses . append ( self . repeat_response )
  if 15 - 15: II111iiii
  self . _outcomes = { x . __name__ : Counter ( ) for x in
 self . _actions + self . _blocks + self . _responses }
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 def decide_action ( self ) :
  self . _current_action = { "attempted" : 1 }
  return self . _decide ( self . _actions , self . _current_action )
  if 75 - 75: Ooo00oOo00o % I1IiI % I1IiI . oO0o0ooO0
 def decide_block ( self , * args ) :
  self . _current_block = { "attempted" : 1 }
  return self . _decide ( self . _blocks , self . _current_block , * args )
  if 5 - 5: I1IiI * IIII + Ooo00oOo00o . iII111i + Ooo00oOo00o
 def decide_response ( self , * args ) :
  self . _current_response = { "attempted" : 1 }
  return bool ( self . _decide (
 self . _responses , self . _current_response , * args ) )
  if 91 - 91: O0
 def _decide ( self , choices , current , * args ) :
  for oOOo0 in choices :
   oo0oOo = oOOo0 ( * args )
   if oo0oOo is not None :
    current [ "name" ] = oOOo0 . __name__
    return oo0oOo
    if 54 - 54: O0 - o00O0oo % iII111i
 def _claim_character ( self , character , target ) :
  if character in self . _state . hidden :
   return True
   if 77 - 77: Ooo00oOo00o / OoOoOO00 / Oo + Oo . iII111i
  if self . _state . influence ( ) == 1 :
   return False
   if 38 - 38: oO0o0ooO0
   if 7 - 7: O0 . ooOoO0o % ooOo - OoOoOO00 - iIii1I11I1II1
  if self . _cards . remaining ( character ) == 0 :
   return False
   if 36 - 36: o00O0oo % IIII % OOOo0 - ooOo
  Ii1IO000OOo00oo = 0
  if character is Character . duke :
   Ii1IO000OOo00oo = O0ooo0O0oo0 (
 [ self . _challenges . expect_challenge ( oo0ooO0oOOOOo , Character . duke )
 for oo0ooO0oOOOOo in self . _state . other_players ( ) ] )
  else :
   Ii1IO000OOo00oo = self . _challenges . expect_challenge ( target , character )
   if 71 - 71: i11iIiiIii + o00O0oo
  return Ii1IO000OOo00oo < 0.01
  if 57 - 57: Ooo0O . IiII . i1IIi
 def obvious_assassinate ( self ) :
  if self . _state . coins ( ) >= 3 :
   for i11 in self . _dangers . prioritized (
 self . _cards . without ( Character . contessa ) ) :
    if Character . assassin in self . _state . hidden :
     return TargetedAction ( Action . assassinate , i11 )
     if 42 - 42: IiII + ooOo % O0
 def early_assassinate ( self ) :
  i1iIIIi1i = self . _dangers . threats ( )
  if self . _state . coins ( ) >= 3 :
   for i11 in self . _dangers . prioritized (
 [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . _cards . unclaimed ( Character . contessa )
 if self . _state . influence ( oo0ooO0oOOOOo ) > 1 ] ) :
    if len ( i1iIIIi1i ) > 0 and i11 not in i1iIIIi1i :
     if Character . assassin in self . _state . hidden :
      return TargetedAction ( Action . assassinate , i11 )
      if 43 - 43: Ooo00oOo00o % iII111i
 def takeover ( self ) :
  if self . _state . coins ( ) >= 7 :
   i11 = self . _dangers . target ( )
   return TargetedAction ( Action . coup , i11 )
   if 5 - 5: i11iIiiIii - i1IIi / iIii1I11I1II1
 def unblockable_captain ( self ) :
  i1iI11i1ii11 = 2
  if len ( self . _state . other_players ( ) ) < 2 :
   i1iI11i1ii11 = 1
  for i11 in self . _dangers . prioritized (
 [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . _state . other_players ( )
 if self . _cards . absent ( oo0ooO0oOOOOo , Character . captain ) and
 self . _cards . absent ( oo0ooO0oOOOOo , Character . ambassador ) and
 self . _state . coins ( oo0ooO0oOOOOo ) >= i1iI11i1ii11 ] ) :
   if self . _claim_character ( Character . captain , i11 ) :
    return TargetedAction ( Action . extort , i11 )
    if 58 - 58: Oo % i11iIiiIii . ooOoO0o / Ooo0O
 def claim_duke ( self ) :
  if self . _claim_character ( Character . duke , None ) :
   return Action . tax
   if 84 - 84: ooOoO0o . ooOo / OOOo0 - OoOoOO00 / OoooooooOO / I1IiI
 def obvious_foreign_aid ( self ) :
  II111iiiI1Ii = len ( self . _cards . without ( Character . duke ) )
  if II111iiiI1Ii >= len ( self . _state . other_players ( ) ) :
   return Action . foreign_aid
   if 78 - 78: I1Ii111 % oO0o0ooO0 + ooOo
  if self . _cards . remaining ( Character . duke ) == 0 :
   return Action . foreign_aid
   if 64 - 64: Ooo0O * O0 . OoOoOO00 + II111iiii
 def income ( self ) :
  return Action . income
  if 6 - 6: Ooo00oOo00o / ooOoO0o . o00O0oo . o00O0oo
 def obvious_block ( self , actor , action , character , target ) :
  OO00O0O = [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . _state . hidden if action . blockable ( oo0ooO0oOOOOo ) ]
  if len ( OO00O0O ) > 0 :
   return OO00O0O [ 0 ]
   if 33 - 33: O0 . o00O0oo . OoOoOO00
 def final_contessa ( self , actor , action , character , target ) :
  if action == Action . assassinate and self . _state . influence ( ) == 1 :
   return Character . contessa
   if 72 - 72: i1IIi / Oo + OoooooooOO - OOOo0
 def obvious_response ( self , actor , action , character , target ) :
  if self . _cards . remaining ( character ) == 0 :
   return True
   if 29 - 29: ooOo + Ooo0O % O0
  if self . _cards . absent ( actor , character ) :
   return True
   if 10 - 10: IiII / oO0o0ooO0 - OoOoOO00 * iIii1I11I1II1 - OoOoOO00
 def repeat_response ( self , actor , action , character , target ) :
  if 97 - 97: ooOo + OoOoOO00 * I1Ii111 + iII111i % ooOoO0o
  if self . _cards . absent ( actor , character ) :
   return True
   if 74 - 74: Ooo0O - OOOo0 + OoooooooOO + oO0o0ooO0 / Ooo00oOo00o
 def notify_action ( self , actor , action , target , succeeded ) :
  if actor == self . _state . identifier :
   self . _current_action [ "succeeded" ] = int ( succeeded )
   if 23 - 23: O0
   o00oO0oOo00 = self . _current_action [ "name" ]
   del self . _current_action [ "name" ]
   self . _outcomes [ o00oO0oOo00 ] . update ( self . _current_action )
   if 81 - 81: Oo
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  if actor == self . _state . identifier :
   self . _current_action [ "blocked" ] = 1
   self . _current_action [ "denied" ] = int ( succeeded )
   if 42 - 42: Oo / IiII / I1IiI + ooOoO0o / Ooo00oOo00o
  if blocker == self . _state . identifier :
   self . _current_block [ "succeeded" ] = int ( succeeded )
   if 84 - 84: IIII * II111iiii + OOOo0
   o00oO0oOo00 = self . _current_block [ "name" ]
   del self . _current_block [ "name" ]
   self . _outcomes [ o00oO0oOo00 ] . update ( self . _current_block )
   if 53 - 53: ooOoO0o % II111iiii . o00O0oo - iIii1I11I1II1 - o00O0oo * II111iiii
 def notify_challenge ( self , challenger , actor , action ,
 character , target , revealed ) :
  if actor == self . _state . identifier :
   if action == Action . block :
    self . _current_block [ "challenged" ] = 1
    self . _current_block [ "sustained" ] = int ( character != revealed )
   else :
    self . _current_action [ "challenged" ] = 1
    self . _current_action [ "sustained" ] = int ( character != revealed )
    if 77 - 77: iIii1I11I1II1 * Oo
  if challenger == self . _state . identifier :
   self . _current_action [ "responded" ] = 1
   self . _current_action [ "smacked" ] = int ( character != revealed )
   if 95 - 95: OoOoOO00 + i11iIiiIii
   self . _current_response [ "succeeded" ] = int ( character != revealed )
   if 6 - 6: IIII / i11iIiiIii + ooOoO0o * Ooo0O
   o00oO0oOo00 = self . _current_response [ "name" ]
   del self . _current_response [ "name" ]
   self . _outcomes [ o00oO0oOo00 ] . update ( self . _current_response )
   if 80 - 80: II111iiii
   if 83 - 83: IiII . i11iIiiIii + II111iiii . I1IiI * IiII
 def notify_end ( self ) :
  if not iIiiiI1IiI1I1 :
   return
   if 53 - 53: II111iiii
  for i1Ii1Ii , oOO in self . _outcomes . items ( ) :
   print ( i1Ii1Ii )
   for oo0ooO0oOOOOo , ii1iII1II in oOO . items ( ) :
    print ( "   " , oo0ooO0oOOOOo , ii1iII1II )
   print ( "" )
   if 48 - 48: II111iiii * I1Ii111 . IiII + Ooo0O
  print ( "" )
  if 78 - 78: i11iIiiIii / ooOoO0o - I1Ii111 / iII111i + Ooo0O
  if 82 - 82: I1Ii111
class ii ( Bot ) :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . listeners = I1Ii1iI1 ( )
  if 87 - 87: OOOo0 . o00O0oo
  self . state = O0OO0O ( identifier )
  self . listeners . add ( self . state )
  if 81 - 81: Ooo0O . I1IiI % O0 / OoOoOO00 - Ooo0O
  self . cards = Ii1I1i ( self . state )
  self . listeners . add ( self . cards )
  if 99 - 99: Ooo0O . ooOoO0o + IIII % Ooo0O . i11iIiiIii % O0
  self . challenges = oOO00O ( )
  self . listeners . add ( self . challenges )
  if 77 - 77: OOOo0 - i1IIi - IiII . Ooo00oOo00o
  self . dangers = IiI1i ( self . state )
  self . listeners . add ( self . dangers )
  if 92 - 92: o00O0oo . o00O0oo + Oo
  self . tactics = i11i1I1 (
 self . state , self . cards , self . challenges , self . dangers )
  self . listeners . add ( self . tactics )
  if 9 - 9: OoOoOO00 * O0 + o00O0oo - IiII * oO0o0ooO0
 @ I1III
 def start ( self ) :
  pass
  if 64 - 64: iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % OOOo0 - ooOoO0o
 @ I1III
 def take_action ( self ) :
  return self . tactics . decide_action ( )
  if 56 - 56: OoOoOO00 . IiII * I1Ii111 - ooOoO0o
 @ I1III
 def block_action ( self , actor , action , character , target ) :
  return self . tactics . decide_block ( actor , action , character , target )
  if 8 - 8: Oo - OoOoOO00 % I1Ii111 * OoooooooOO - Oo * oO0o0ooO0
 @ I1III
 def challenge ( self , actor , action , character , target ) :
  return self . tactics . decide_response ( actor , action , character , target )
  if 6 - 6: OoooooooOO
 @ I1III
 def notify_action ( self , actor , action , target , succeeded ) :
  pass
  if 17 - 17: OoOoOO00 % oO0o0ooO0
 @ I1III
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  pass
  if 90 - 90: Ooo0O / iIii1I11I1II1 - I1IiI / OoooooooOO - OoooooooOO * iII111i
 @ I1III
 def notify_challenge ( self , challenger , actor , action ,
 character , target , revealed ) :
  pass
  if 73 - 73: ooOo * i11iIiiIii % Ooo0O . ooOo
 @ I1III
 def notify_flip ( self , player , flipped ) :
  pass
  if 66 - 66: Ooo0O + Ooo0O + IIII / ooOoO0o + iII111i
 @ I1III
 def notify_end ( self ) :
  pass
  if 30 - 30: O0
 @ I1III
 def update_state ( self , states , hidden ) :
  pass
  if 44 - 44: Ooo0O / IiII / IiII
 def flip ( self ) :
  OOO = [ Character . captain ,
 Character . duke ,
 Character . contessa ,
 Character . assassin ,
 Character . ambassador ]
  if 32 - 32: i1IIi / II111iiii . OOOo0
  for oooOo0OOOoo0 in reversed ( OOO ) :
   if oooOo0OOOoo0 in self . state . hidden :
    return oooOo0OOOoo0
    if 51 - 51: OOOo0 / Ooo00oOo00o . iII111i * I1IiI + Oo * o00O0oo
 def exchange ( self , drawn ) :
  pass
  if 73 - 73: Oo + OoooooooOO - O0 - I1Ii111 - II111iiii
 def reveal ( self , challenger , action , character , taret ) :
  if character in self . state . hidden :
   return character
   if 99 - 99: IIII . I1Ii111 + oO0o0ooO0 + OoooooooOO % I1IiI
  return self . flip ( )
  if 51 - 51: iIii1I11I1II1
  if 34 - 34: Ooo0O + OoOoOO00 - Ooo0O
class oOO00O :
 def __init__ ( self ) :
  self . _attempted_challenges = { x : Counter ( ) for x in range ( IiII1IiiIiI1 ) }
  self . _potential_challenges = { x : Counter ( ) for x in range ( IiII1IiiIiI1 ) }
  if 17 - 17: II111iiii % ooOoO0o + IiII - ooOoO0o / iII111i + IIII
 def expect_challenge ( self , challenger , character ) :
  if self . _potential_challenges [ challenger ] [ character ] > 0 :
   if ( self . _attempted_challenges [ challenger ] [ character ] > 5 or
 self . _potential_challenges [ challenger ] [ character ] > 50 ) :
    return ( self . _attempted_challenges [ challenger ] [ character ] /
 self . _potential_challenges [ challenger ] [ character ] )
    if 59 - 59: iII111i % Ooo00oOo00o . I1Ii111 * ooOo % IiII
    if 59 - 59: Ooo0O - ooOoO0o
  return 0
  if 15 - 15: oO0o0ooO0 . i11iIiiIii . OoooooooOO / Oo % I1Ii111
 def challenge ( self , actor , action , character , target ) :
  if 93 - 93: O0 % i1IIi . iII111i / OoOoOO00 - oO0o0ooO0 / OoOoOO00
  if 36 - 36: Ooo0O % Ooo0O % i1IIi / i1IIi - IIII
  if target is not None :
   if 30 - 30: IiII / OoOoOO00
   self . _potential_challenges [ target ] . update ( [ character ] )
  else :
   for oo0ooO0oOOOOo in range ( IiII1IiiIiI1 ) :
    self . _potential_challenges [ oo0ooO0oOOOOo ] . update ( [ character ] )
    if 35 - 35: II111iiii % iII111i . IIII + IIII % II111iiii % II111iiii
 def notify_challenge ( self , challenger , actor , action ,
 character , target , revealed ) :
  if target is None or challenger == target :
   self . _attempted_challenges [ challenger ] . update ( [ character ] )
   if 72 - 72: II111iiii + i1IIi + I1IiI
 def notify_end ( self ) :
  if not iIiiiI1IiI1I1 :
   return
   if 94 - 94: Ooo0O . i1IIi - I1IiI % O0 - Oo
  for oo0ooO0oOOOOo in range ( IiII1IiiIiI1 ) :
   for ooO0O00Oo0o in Character :
    print ( oo0ooO0oOOOOo , "expect challenge" , ooO0O00Oo0o ,
 self . expect_challenge ( oo0ooO0oOOOOo , ooO0O00Oo0o ) )
   print ( "" )
   if 65 - 65: ooOo . IiII - oO0o0ooO0 * o00O0oo / oO0o0ooO0 / IIII
   if 40 - 40: IIII * o00O0oo * i11iIiiIii
class IiI1i :
 def __init__ ( self , state ) :
  self . _state = state
  self . _placed = Counter ( )
  self . _killers = Counter ( )
  self . _attacks = Counter ( )
  self . _survived = Counter ( )
  self . _last = None
  if 57 - 57: IIII
 def threats ( self ) :
  return [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . _state . other_players ( )
 if self . killer ( oo0ooO0oOOOOo ) > 1.2 ]
  if 29 - 29: Ooo00oOo00o - o00O0oo * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
 def target ( self , players = None ) :
  if players is None :
   players = self . _state . other_players ( )
   if 74 - 74: I1Ii111 - o00O0oo / ooOoO0o * O0 - iII111i
  I1Ii = self . prioritized ( players )
  if len ( I1Ii ) > 0 :
   return I1Ii [ 0 ]
   if 19 - 19: OoOoOO00
  return None
  if 25 - 25: I1Ii111 / IIII
 def prioritized ( self , players ) :
  II = { }
  for ooO in players :
   Ooo0oOooo0 = self . _state . coins ( ooO )
   if 61 - 61: Ooo00oOo00o - iII111i - i1IIi
   if self . _state . influence ( ooO ) > 1 :
    Ooo0oOooo0 += 6
    if 25 - 25: O0 * IiII + ooOo . I1IiI . I1IiI
   if ooO in self . threats ( ) :
    Ooo0oOooo0 += 12
    if 58 - 58: OoOoOO00
   if self . killer ( ooO ) > 1.05 :
    Ooo0oOooo0 += 3
   elif self . survival ( ooO ) > 1.05 :
    Ooo0oOooo0 += 2
    if 53 - 53: i1IIi
   II [ ooO ] = Ooo0oOooo0
   if 59 - 59: I1IiI
  return [ oo0ooO0oOOOOo [ 0 ] for oo0ooO0oOOOOo in sorted (
 II . items ( ) , key = lambda oo0ooO0oOOOOo : oo0ooO0oOOOOo [ 1 ] , reverse = True ) ]
  if 81 - 81: Ooo00oOo00o - Ooo00oOo00o . ooOoO0o
 def survival ( self , player ) :
  o0OoOo00o0o = sum ( self . _survived . values ( ) )
  if o0OoOo00o0o == 0 or player not in self . _survived :
   return 1
   if 41 - 41: IIII % Oo - OOOo0 * oO0o0ooO0 * OOOo0
  OOOoOO0o = { x [ 0 ] : x [ 1 ] / o0OoOo00o0o for x in self . _survived . items ( ) }
  i1II1 = sum ( x for x in OOOoOO0o . values ( ) ) / len ( OOOoOO0o )
  oo0oOo = OOOoOO0o [ player ] / i1II1
  return oo0oOo
  if 25 - 25: oO0o0ooO0 / iIii1I11I1II1 % ooOoO0o
 def killer ( self , player ) :
  o0OoOo00o0o = sum ( self . _killers . values ( ) )
  if o0OoOo00o0o == 0 or player not in self . _killers :
   return 1
   if 42 - 42: i11iIiiIii * iIii1I11I1II1 / ooOo . i11iIiiIii % IiII
  i1iI = { x [ 0 ] : x [ 1 ] / o0OoOo00o0o for x in self . _killers . items ( ) }
  i1II1 = sum ( x for x in i1iI . values ( ) ) / len ( i1iI )
  return i1iI [ player ] / i1II1
  if 29 - 29: OoOoOO00 % iII111i - OoOoOO00 / iII111i . i1IIi
 def notify_action ( self , actor , action , target , succeeded ) :
  if self . _state . turn == self . _last :
   if target == self . _state . identifier and succeeded :
    if action in [ Action . coup , Action . assassinate ] :
     self . _killers . update ( [ actor ] )
     self . _attacks . update ( [ action ] )
     if 31 - 31: oO0o0ooO0
 def notify_flip ( self , player , flipped ) :
  if player == self . _state . identifier :
   if self . _state . influence ( ) == 0 :
    self . _last = self . _state . turn
    self . _survived . update ( self . _state . other_players ( ) )
    self . _placed . update ( [ len ( self . _state . other_players ( ) ) ] )
    if 88 - 88: Oo - IIII + iII111i * OoOoOO00 % iIii1I11I1II1 + OOOo0
  if self . _state . other_players ( ) == 0 :
   self . _placed . update ( [ 0 ] )
   if 76 - 76: OoOoOO00 * ooOoO0o % oO0o0ooO0
 def notify_end ( self ) :
  if not iIiiiI1IiI1I1 :
   return
   if 57 - 57: iIii1I11I1II1 - i1IIi / oO0o0ooO0 - O0 * OoooooooOO % II111iiii
  print ( "placed" )
  for i1Ii1Ii , oOO in self . _placed . items ( ) :
   print ( "   " , i1Ii1Ii , oOO )
  print ( "" )
  if 68 - 68: OoooooooOO * IiII % Ooo00oOo00o - o00O0oo
  print ( "killers" )
  for i1Ii1Ii , oOO in self . _killers . items ( ) :
   print ( "   " , i1Ii1Ii , oOO )
  print ( "" )
  if 34 - 34: oO0o0ooO0 . iIii1I11I1II1 * Ooo00oOo00o * Ooo0O / oO0o0ooO0 / ooOo
  print ( "survivals" )
  for i1Ii1Ii , oOO in self . _survived . items ( ) :
   print ( "   " , i1Ii1Ii , oOO )
  print ( "" )
  if 78 - 78: OOOo0 - I1IiI / Ooo00oOo00o
  print ( "attacks" )
  for i1Ii1Ii , oOO in self . _attacks . items ( ) :
   print ( "   " , i1Ii1Ii , oOO )
  print ( "" )
  if 10 - 10: ooOoO0o + OOOo0 * ooOo + iIii1I11I1II1 / oO0o0ooO0 / ooOo
  if 42 - 42: OoOoOO00
class Ii1I1i :
 def __init__ ( self , state ) :
  self . _state = state
  self . start ( )
  if 38 - 38: iII111i + II111iiii % IIII % Ooo00oOo00o - I1Ii111 / OoooooooOO
 def without ( self , character ) :
  return [ i1Ii1Ii for i1Ii1Ii , oOO in self . _absent . items ( )
 if character in oOO and i1Ii1Ii in self . _state . other_players ( ) ]
  if 73 - 73: I1IiI * O0 - i11iIiiIii
 def unclaimed ( self , character ) :
  return [ i1Ii1Ii for i1Ii1Ii , oOO in self . _claimed . items ( )
 if character not in oOO and i1Ii1Ii in self . _state . other_players ( ) ]
  if 85 - 85: I1Ii111 % ooOoO0o + IiII / I1IiI . Ooo0O + iII111i
 def absent ( self , player , character ) :
  return character in self . _absent [ player ]
  if 62 - 62: i11iIiiIii + i11iIiiIii - I1IiI
 def claimed ( self , player , character ) :
  return character in self . _claimed [ player ]
  if 28 - 28: ooOoO0o . ooOoO0o % iIii1I11I1II1 * iIii1I11I1II1 . I1IiI / ooOoO0o
 def remaining ( self , character ) :
  return 3 - sum ( 1 for x in self . unavailable ( ) if x == character )
  if 27 - 27: Oo + IIII - i1IIi
 def unavailable ( self ) :
  return itertools . chain ( self . _hidden , self . visible ( ) )
  if 69 - 69: o00O0oo - O0 % ooOo + i11iIiiIii . Ooo00oOo00o / Oo
 def visible ( self ) :
  return [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . _visible . values ( ) ]
  if 79 - 79: O0 * i11iIiiIii - o00O0oo / o00O0oo
 def start ( self ) :
  self . _hidden = None
  self . _visible = None
  self . _absent = None
  self . _claimed = None
  if 48 - 48: O0
 def challenge ( self , actor , action , character , target ) :
  self . _claimed [ actor ] . add ( action . required_character ( ) )
  if 93 - 93: i11iIiiIii - OoOoOO00 * ooOo * IiII % O0 + OoooooooOO
 def notify_action ( self , actor , action , target , succeeded ) :
  if succeeded and action == Action . exchange :
   self . _reset_cards ( actor )
   if 25 - 25: o00O0oo + I1Ii111 / IIII . I1IiI % O0 * Oo
  if succeeded and action . blockable ( ) and target is not None :
   OO00O0O = [ oo0ooO0oOOOOo [ 0 ] for oo0ooO0oOOOOo in blocked_actions . items ( )
 if oo0ooO0oOOOOo [ 1 ] == action ]
   self . _absent [ target ] . update ( OO00O0O )
   if 84 - 84: IIII % I1Ii111 + i11iIiiIii
  if succeeded and action == Action . foreign_aid :
   for ooO in self . _state . other_players ( ) :
    self . _absent [ ooO ] . update ( [ Character . duke ] )
    if 28 - 28: OOOo0 + Oo * iII111i % Ooo0O . IiII % O0
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  self . _claimed [ blocker ] . add ( character )
  if 16 - 16: IiII - iIii1I11I1II1 / OoOoOO00 . II111iiii + iIii1I11I1II1
 def notify_challenge ( self , challenger , actor , action ,
 character , target , revealed ) :
  if revealed != character :
   self . _lose_card ( actor , revealed )
   if 19 - 19: Oo - OOOo0 . O0
   self . _absent [ actor ] . add ( character )
  else :
   self . _reset_cards ( actor )
   if 60 - 60: II111iiii + OOOo0
 def notify_flip ( self , player , flipped ) :
  self . _lose_card ( player , flipped )
  if 9 - 9: IIII * OoooooooOO - iIii1I11I1II1 + Ooo00oOo00o / Oo . Oo
 def update_state ( self , states , hidden ) :
  if self . _hidden is None :
   self . _hidden = [ ]
   self . _visible = { x . identifier : [ ] for x in states }
   self . _absent = { x . identifier : set ( ) for x in states }
   self . _claimed = { x . identifier : set ( ) for x in states }
   if 49 - 49: II111iiii
  self . _visible = { x . identifier : x . flipped for x in states }
  self . _hidden = list ( hidden )
  if 25 - 25: OoooooooOO - OoOoOO00 . OoOoOO00 * Ooo0O
 def _reset_cards ( self , player ) :
  self . _absent [ player ] = set ( )
  self . _claimed [ player ] = set ( )
  if 81 - 81: ooOoO0o + o00O0oo
 def _lose_card ( self , player , character ) :
  if 98 - 98: OoOoOO00
  self . _claimed [ player ] . discard ( character )
  if 95 - 95: IIII / IIII
  if len ( self . _visible [ player ] ) >= 2 :
   self . _reset_cards ( player )
   if 30 - 30: ooOo + OOOo0 / OOOo0 % ooOo . ooOo
   if 55 - 55: IIII - IiII + II111iiii + ooOoO0o % I1Ii111
class O0OO0O :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . round = - 1
  self . hidden = None
  self . _states = None
  self . start ( )
  if 41 - 41: i1IIi - IiII - I1Ii111
 def coins ( self , player = None ) :
  if player is None :
   player = self . identifier
   if 8 - 8: Oo + oO0o0ooO0 - I1IiI % OOOo0 % I1IiI * Ooo0O
  return [ oo0ooO0oOOOOo . coins for oo0ooO0oOOOOo in self . _states
 if oo0ooO0oOOOOo . identifier == player ] [ 0 ]
  if 9 - 9: OOOo0 - i11iIiiIii - iII111i * I1Ii111 + IIII
 def influence ( self , player = None ) :
  if player is None :
   player = self . identifier
   if 44 - 44: II111iiii
  return [ 2 - len ( oo0ooO0oOOOOo . flipped ) for oo0ooO0oOOOOo in self . _states
 if oo0ooO0oOOOOo . identifier == player ] [ 0 ]
  if 52 - 52: ooOo - OOOo0 + ooOo % I1IiI
 def other_players ( self ) :
  return [ oo0ooO0oOOOOo . identifier for oo0ooO0oOOOOo in self . _states if len ( oo0ooO0oOOOOo . flipped ) < 2
 and oo0ooO0oOOOOo . identifier != self . identifier ]
  if 35 - 35: iIii1I11I1II1
 def start ( self ) :
  self . turn = 0
  if 42 - 42: oO0o0ooO0 . OoOoOO00 . i1IIi + Ooo00oOo00o + iII111i + OoOoOO00
 def update_state ( self , states , hidden ) :
  self . _states = states
  self . hidden = hidden
  if 31 - 31: ooOoO0o . iII111i - IIII . OoooooooOO / OoooooooOO
  if 56 - 56: Oo / Ooo0O / i11iIiiIii + OoooooooOO - OOOo0 - IiII
class I1Ii1iI1 :
 def __init__ ( self ) :
  self . _listeners = [ ]
  if 21 - 21: O0 % o00O0oo . OoOoOO00 / II111iiii + o00O0oo
 def add ( self , listener ) :
  self . _listeners . append ( listener )
  if 53 - 53: Ooo0O - OoOoOO00 - Ooo0O * ooOoO0o
 def invoke ( self , name , * args , ** kwargs ) :
  for oooooo0OO in self . _listeners :
   iI1I = getattr ( oooooo0OO , name , None )
   if iI1I is not None :
    iI1I ( * args , ** kwargs )
    if 100 - 100: iIii1I11I1II1 + Ooo00oOo00o / OOOo0 . i11iIiiIii
class III1I1Iii1iiI ( Bot ) :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . known = [ ]
  self . aCards = [ ]
  self . freeMoneys = [ ]
  if 17 - 17: I1Ii111 % iIii1I11I1II1 - iIii1I11I1II1
 def update_state ( self , states , hidden ) :
  self . states = states
  self . hidden = hidden
  if 78 - 78: ooOoO0o + IiII . IIII - ooOoO0o . I1Ii111
 def start ( self ) :
  self . turn = 0
  if 30 - 30: OoOoOO00 + Oo % I1Ii111 * ooOoO0o / OOOo0 - IiII
 def notify_flip ( self , player , flipped ) :
  pass
  if 64 - 64: iIii1I11I1II1
 def notify_action ( self , actor , action , target , succeeded ) :
  if Action . exchange == action :
   self . aCards = [ ]
  if Action . extort == action :
   if succeeded and target != self . identifier :
    self . freeMoneys . append ( target )
    if 21 - 21: OOOo0 . II111iiii
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  if Action . extort == action and succeeded :
   if blocker in self . freeMoneys :
    self . freeMoneys . remove ( blocker )
    if 54 - 54: II111iiii % II111iiii
 def take_action ( self ) :
  self . turn += 1
  Oo00000o0o = [ oo0ooO0oOOOOo . identifier for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) < 2 ]
  if 72 - 72: iII111i % ooOo + Oo / Ooo0O + o00O0oo
  if len ( Oo00000o0o ) != 0 :
   return self . take_group_action ( )
   if 10 - 10: oO0o0ooO0 / IIII + i11iIiiIii / I1Ii111
 def take_group_action ( self ) :
  OOOoOoO = [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) == 0 and oo0ooO0oOOOOo . identifier != self . identifier ]
  iIIIII1ii1I = [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) == 1 and oo0ooO0oOOOOo . identifier != self . identifier ]
  if len ( OOOoOoO ) > 0 :
   i11 = self . pick_richest ( OOOoOoO )
  else :
   i11 = self . pick_richest ( iIIIII1ii1I )
   if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * iII111i
  Oo00000o0o = [ oo0ooO0oOOOOo . identifier for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) < 2 ]
  o000o0o00o0Oo = self . states [ self . identifier ] . coins
  if o000o0o00o0Oo >= 7 :
   return TargetedAction ( Action . coup , i11 )
  if Character . duke in self . hidden :
   return Action . tax
  if Character . ambassador in self . hidden :
   return Action . exchange
  if len ( self . hidden ) == 2 and self . hidden [ 0 ] == self . hidden [ 1 ] :
   if self . hidden [ 0 ] in [ Character . duke , Character . assassin ] :
    return Action . exchange
  if Character . assassin in self . hidden and o000o0o00o0Oo >= 3 :
   if self . count_known ( Character . contessa ) > 0 :
    return TargetedAction ( Action . assassinate , i11 )
  if Character . captain in self . hidden :
   if len ( self . freeMoneys ) > 0 and self . freeMoneys [ 0 ] in Oo00000o0o and self . states [ self . freeMoneys [ 0 ] ] . coins > 1 :
    return TargetedAction ( Action . extort , self . freeMoneys [ 0 ] )
   return TargetedAction ( Action . extort , i11 )
  if self . count_known ( Character . duke ) == 3 :
   return Action . foreign_aid
  return Action . income
  if 26 - 26: OoooooooOO * OoOoOO00 + iII111i
 def take_one_vs_one_action ( self ) :
  print ( 'yes' )
  if 24 - 24: i11iIiiIii % iIii1I11I1II1 + iII111i / i11iIiiIii
 def block_action ( self , actor , action , character , target ) :
  if len ( self . hidden ) > 0 and action . blockable ( self . hidden [ 0 ] ) :
   return self . hidden [ 0 ]
   if 70 - 70: Oo * O0 . IiII + OoOoOO00 . o00O0oo
  if len ( self . hidden ) > 1 and action . blockable ( self . hidden [ 1 ] ) :
   return self . hidden [ 1 ]
   if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - Oo - IiII
  if Action . assassinate == action and self . count_known ( Character . contessa ) == 0 :
   return Character . contessa
   if 63 - 63: Oo
  return None
  if 69 - 69: iIii1I11I1II1 . ooOo % IIII + iIii1I11I1II1 / O0 / ooOo
 def challenge ( self , actor , action , character , target ) :
  if self . count_known ( character ) == 3 : return True
  return False
  if 61 - 61: iII111i % iII111i * I1IiI / I1IiI
 def flip ( self ) :
  if len ( self . hidden ) > 1 :
   if Character . contessa in self . hidden :
    if self . hidden [ 0 ] == Character . contessa :
     return self . hidden [ 1 ]
     if 75 - 75: o00O0oo . IIII
  return self . hidden [ 0 ]
  if 50 - 50: Ooo00oOo00o
 def exchange ( self , drawn ) :
  I1Ii = self . _prioritize ( list ( self . hidden ) + list ( drawn ) )
  self . aCards = drawn
  return I1Ii [ - 2 : ]
  if 60 - 60: IIII * iIii1I11I1II1 * ooOo * OOOo0
 def reveal ( self , challenger , action , character , taret ) :
  if character in self . hidden :
   return character
   if 69 - 69: I1Ii111 * O0 . i11iIiiIii / I1Ii111 . I1IiI
  return self . flip ( )
  if 63 - 63: IiII + I1IiI . II111iiii - OoOoOO00
 def _prioritize ( self , characters ) :
  I1Ii = [ ]
  oOOO00o000o = None
  if len ( self . hidden ) == 2 and self . hidden [ 0 ] == self . hidden [ 1 ] :
   oOOO00o000o = self . hidden [ 0 ]
   if 9 - 9: Ooo0O + IiII / IiII
  Ii1I11ii1i = [ Character . duke , Character . captain , Character . ambassador , Character . assassin , Character . contessa ]
  if 89 - 89: ooOoO0o . O0 / ooOo % Ooo00oOo00o . OOOo0
  for IiiI1i in Ii1I11ii1i :
   if oOOO00o000o != IiiI1i and IiiI1i in characters :
    I1Ii . extend ( [ IiiI1i ] )
    if 51 - 51: o00O0oo
    if 25 - 25: OoooooooOO + o00O0oo * ooOo
  if len ( I1Ii ) == 1 :
   I1Ii . extend ( [ oOOO00o000o ] )
   if 92 - 92: OoOoOO00 + IiII + O0 / I1IiI + oO0o0ooO0
  return I1Ii
  if 18 - 18: IIII * Ooo00oOo00o . ooOoO0o / ooOo / i11iIiiIii
 def pick_richest ( self , dudes ) :
  IIIII = 'derp'
  o0ooOoO000oO = - 100
  for OOo in dudes :
   if OOo . coins > o0ooOoO000oO :
    o0ooOoO000oO = OOo . coins
    IIIII = OOo
  return IIIII . identifier
  if 50 - 50: IIII
 def count_known ( self , character ) :
  o0O0O0ooo0oOO = 0
  oo000 = [ ]
  if len ( self . hidden ) == 2 :
   oo000 . extend ( [ self . hidden [ 0 ] , self . hidden [ 1 ] ] )
  if len ( self . hidden ) == 1 :
   oo000 . extend ( [ self . hidden [ 0 ] ] )
  if len ( self . aCards ) > 0 :
   oo000 . extend ( self . aCards )
  for iiOoO in self . states :
   oo000 += iiOoO . flipped
  for IiiI1i in oo000 :
   if IiiI1i == character :
    o0O0O0ooo0oOO += 1
    if 41 - 41: i1IIi * II111iiii / OoooooooOO . iII111i
  return o0O0O0ooo0oOO
  if 83 - 83: ooOoO0o . O0 / OOOo0 / iII111i - II111iiii
class oO0oO0 ( Bot ) :
 if 14 - 14: ooOoO0o
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  self . _characterValueMap = {
 Character . duke : 10 ,
 Character . captain : 8 ,
 Character . contessa : 2 ,
 Character . assassin : 4 ,
 Character . ambassador : 1 }
  if 99 - 99: ooOoO0o
  self . _contessaMap = None
  self . _numExchanges = 0
  self . _gameID = 0
  self . _turn = 0
  if 38 - 38: ooOo - ooOoO0o / O0 . oO0o0ooO0
 def start ( self ) :
  self . _gameID += 1
  self . _turn = 1
  if 45 - 45: oO0o0ooO0
 def update_state ( self , states , hidden ) :
  self . states = states
  self . hidden = list ( hidden )
  if self . _contessaMap is None :
   self . _contessaMap = { x . identifier : False for x in states }
   if 83 - 83: Ooo00oOo00o . OoooooooOO
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / o00O0oo / i11iIiiIii
 def take_action ( self ) :
  self . _turn += 1
  if 62 - 62: Oo / ooOo
  Oo00000o0o = [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) < 2 and oo0ooO0oOOOOo . identifier != self . identifier ]
  if 7 - 7: OoooooooOO . o00O0oo
  if 53 - 53: I1Ii111 % I1Ii111 * I1IiI + Ooo00oOo00o
  Oo00000o0o . sort ( key = lambda oo0ooO0oOOOOo : oo0ooO0oOOOOo . coins , reverse = True )
  Oo00000o0o . sort ( key = lambda oo0ooO0oOOOOo : len ( oo0ooO0oOOOOo . flipped ) )
  i11 = Oo00000o0o [ 0 ] . identifier
  if 92 - 92: OoooooooOO + i1IIi / I1Ii111 * O0
  OOO0O = [ ]
  for oo0ooO0oOOOOo in self . states :
   OOO0O += oo0ooO0oOOOOo . flipped
  OOO0O += self . hidden
  if 100 - 100: IIII % iIii1I11I1II1 * II111iiii - ooOoO0o
  if 92 - 92: IIII
  if self . states [ self . identifier ] . coins >= 7 :
   return TargetedAction ( Action . coup , i11 )
  elif ( Character . assassin in self . hidden and self . states [ self . identifier ] . coins >= 3 and
 ( ( self . _contessaMap [ i11 ] == False and OOO0O . count ( Character . contessa ) == 2 ) or OOO0O . count ( Character . contessa ) == 3 ) ) :
   return TargetedAction ( Action . assassinate , i11 )
  elif Character . captain in self . hidden and 6 == ( OOO0O . count ( Character . captain ) + OOO0O . count ( Character . ambassador ) ) :
   if 22 - 22: OOOo0 % ooOoO0o * ooOo / iII111i % i11iIiiIii * IiII
   return TargetedAction ( Action . extort , i11 )
  elif ( Character . duke not in self . hidden ) and self . _numExchanges < 1 and len ( self . hidden ) > 1 :
   if Character . ambassador in self . hidden or random . uniform ( 0 , 1 ) < 0.25 :
    self . _numExchanges += 1
    return Action . exchange
   elif random . uniform ( 0 , 1 ) < 0.05 :
    return Action . tax
   else :
    return Action . income
  elif Character . duke in self . hidden :
   return Action . tax
  elif OOO0O . count ( Character . duke ) == 3 :
   return Action . foreign_aid
  else :
   return Action . income
   if 95 - 95: OoooooooOO - o00O0oo * OoOoOO00 + Ooo00oOo00o
   if 10 - 10: I1IiI / i11iIiiIii
 def block_action ( self , actor , action , character , target ) :
  if len ( self . hidden ) > 0 and action . blockable ( self . hidden [ 0 ] ) :
   return self . hidden [ 0 ]
   if 92 - 92: IiII . oO0o0ooO0
  if len ( self . hidden ) > 1 and action . blockable ( self . hidden [ 1 ] ) :
   return self . hidden [ 1 ]
   if 85 - 85: ooOo . oO0o0ooO0
  if action == Action . assassinate :
   return Character . contessa
   if 78 - 78: IIII * oO0o0ooO0 + iIii1I11I1II1 + iIii1I11I1II1 / oO0o0ooO0 . I1Ii111
   if 97 - 97: IIII / oO0o0ooO0 % i1IIi % ooOo
 def notify_action ( self , actor , action , target , succeeded ) :
  pass
  if 18 - 18: iIii1I11I1II1 % IiII
  if 95 - 95: IIII + i11iIiiIii * oO0o0ooO0 - i1IIi * oO0o0ooO0 - iIii1I11I1II1
 def notify_block ( self , blocker , character , actor , action , succeeded ) :
  if action == Action . assassinate :
   self . _contessaMap [ blocker ] = succeeded
   if 75 - 75: OoooooooOO * o00O0oo
 def reveal ( self , challenger , action , character , target ) :
  if character in self . hidden :
   return character
   if 9 - 9: o00O0oo - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  return self . flip ( )
  if 39 - 39: o00O0oo * OOOo0 + iIii1I11I1II1 - o00O0oo + iII111i
 def challenge ( self , actor , action , character , target ) :
  if target == self . identifier and action == Action . assassinate and Character . contessa not in self . hidden and len ( self . hidden ) == 1 :
   return True
   if 69 - 69: O0
  OOO0O = [ ]
  for oo0ooO0oOOOOo in self . states :
   OOO0O += oo0ooO0oOOOOo . flipped
  OOO0O += self . hidden
  if 85 - 85: IIII / O0
  if OOO0O . count ( character ) == 3 :
   return True
   if 18 - 18: I1IiI % O0 * ooOo
  return False
  if 62 - 62: oO0o0ooO0 . o00O0oo . OoooooooOO
 def flip ( self ) :
  self . _rankCards ( self . hidden )
  return self . hidden [ - 1 ]
  if 11 - 11: iII111i / IiII
 def exchange ( self , drawn ) :
  oooO0 = self . hidden + list ( drawn )
  self . _rankCards ( oooO0 )
  if 16 - 16: II111iiii + Ooo0O - OoooooooOO
  if oooO0 [ 0 ] == oooO0 [ 1 ] :
   oooO0 [ 1 ] , oooO0 [ 2 ] = oooO0 [ 2 ] , oooO0 [ 1 ]
   if 3 - 3: O0 / ooOoO0o
  return oooO0 [ - 2 : ]
  if 31 - 31: iII111i + I1IiI . OoooooooOO
 def _rankCards ( self , cardList ) :
  ooOooo0 = copy . deepcopy ( self . _characterValueMap )
  if 67 - 67: OoOoOO00
  OOO0O = [ ]
  for oo0ooO0oOOOOo in self . states :
   OOO0O += oo0ooO0oOOOOo . flipped
  OOO0O += self . hidden
  if 55 - 55: ooOo - ooOoO0o * I1IiI + Ooo00oOo00o * Ooo00oOo00o * O0
  if len ( [ oo0ooO0oOOOOo for oo0ooO0oOOOOo in self . states if len ( oo0ooO0oOOOOo . flipped ) < 2 and oo0ooO0oOOOOo . identifier != self . identifier ] ) < 4 :
   if OOO0O . count ( Character . contessa ) == 3 :
    ooOooo0 [ Character . assassin ] = 11
   if ( OOO0O . count ( Character . captain ) + OOO0O . count ( Character . ambassador ) ) == 6 :
    ooOooo0 [ Character . captain ] = 11
    if 91 - 91: oO0o0ooO0 - iII111i % iIii1I11I1II1 - OoooooooOO % IIII
  cardList . sort ( key = lambda oo0ooO0oOOOOo : ooOooo0 [ oo0ooO0oOOOOo ] , reverse = True )
  return cardList
  if 98 - 98: Oo . Oo * Ooo0O * II111iiii * oO0o0ooO0
  if 92 - 92: OOOo0
def iI11I ( identifier ) :
 ooO000 = [ ]
 ooO000 . append ( I11I11i1I ( identifier ) )
 ooO000 . append ( ii ( identifier ) )
 ooO000 . append ( III1I1Iii1iiI ( identifier ) )
 ooO000 . append ( o0OOO ( identifier ) )
 ooO000 . append ( oO0oO0 ( identifier ) )
 if 57 - 57: II111iiii
 return random . choice ( ooO000 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
