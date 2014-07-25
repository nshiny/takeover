from interface import *
from game import *
from operator import *
if 64 - 64: i11iIiiIii
import random
import time
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = list ( )
iIiiiI1IiI1I1 = Bot ( )
o0OoOoOO00 = ""
IiII1IiiIiI1 . append ( Player ( 0 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
IiII1IiiIiI1 . append ( Player ( 1 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
IiII1IiiIiI1 . append ( Player ( 2 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
IiII1IiiIiI1 . append ( Player ( 3 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
IiII1IiiIiI1 . append ( Player ( 4 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
IiII1IiiIiI1 . append ( Player ( 5 , iIiiiI1IiI1I1 , o0OoOoOO00 ) )
I11i = { Action . income : 0 , Action . foreign_aid : 0 , Action . coup : 0 , Action . tax : 0 , Action . assassinate : 0 , Action . exchange : 0 , Action . extort : 0 , Action . block : 0 }
if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
#allKnown = {"Duke": 0, "Assassin": 0, "Captain": 0, "Ambassador": 0, "Contessa": 0}
if 8 - 8: Oo / iII11iiIII111 % iiiIIii1I1Ii . O00oOoOoO0o0O
II1ii1II1iII1 = list ( )
II1ii1II1iII1 . append ( I11i )
II1ii1II1iII1 . append ( I11i )
II1ii1II1iII1 . append ( I11i )
II1ii1II1iII1 . append ( I11i )
II1ii1II1iII1 . append ( I11i )
II1ii1II1iII1 . append ( I11i )
if 16 - 16: Iii1iIIIII . II1i * o00ooo0 / o00 * O0IiiiIiI1iIiI1 - ooo0Oo0
if 56 - 56: O0 . O0IiiiIiI1iIiI1 * Oo
if 84 - 84: iIii1I11I1II1 . o00 / o00 % o00
if 22 - 22: II1i . o00
I11 = { }
if 98 - 98: i11iIiiIii * OOooo000oo0 % o00ooo0 * o00ooo0 * II111iiii
class o0o0Oo0oooo0 ( Bot ) :
 def __init__ ( self , identifier ) :
  self . identifier = identifier
  if 97 - 97: i1 - ooo0Oo0
  if 54 - 54: ooo0Oo0 . ooo0Oo0 / iIii1I11I1II1 / Iii1iIIIII + iiiIIii1I1Ii / Oo
  self . hidden = [ ]
  self . roundCount = 0
  self . gameCount = 0
  self . totalRoundCount = 1
  self . claims = { }
  if 39 - 39: Iii1iIIIII / O0IiiiIiI1iIiI1 . Iii1iIIIII - Iii1iIIIII
 def start ( self ) :
  self . roundCount = 1
  self . gameCount += 1
  if 68 - 68: O00oOoOoO0o0O . OOooo000oo0 / o00ooo0
 def update_state ( self , states , hidden ) :
  self . states = states
  self . hidden = hidden
  self . roundCount += 1
  I11 = self . _setKnownStates ( )
  if 72 - 72: ii1IiI1i / ii1IiI1i
  if 30 - 30: ii1IiI1i
  for OOoOooOOOOOo in states :
   IiII1IiiIiI1 [ OOoOooOOOOOo . identifier ] . PlayerState = OOoOooOOOOOo
   if 48 - 48: OoooooooOO % Oo . OOooo000oo0 - II1i % i1IIi % OoooooooOO
  i1iIIi1 = self . _prioritize ( hidden )
  if 50 - 50: i11iIiiIii - II1i
 def notify_action ( self , actor , action , target , succeeded ) :
  self . totalRoundCount += 1
  II1ii1II1iII1 [ actor ] [ action ] += 1
  if 78 - 78: ii1IiI1i
  if 18 - 18: O0 - o00ooo0 / o00ooo0 + ooo0Oo0 % ooo0Oo0 - o00
  if actor not in self . claims :
   self . claims [ actor ] = { }
  if action not in self . claims [ actor ] :
   self . claims [ actor ] [ action ] = 1
  else :
   self . claims [ actor ] [ action ] += 1
   if 62 - 62: o00ooo0 - o00 - IIIiiIIii % i1IIi / iiiIIii1I1Ii
   if 77 - 77: II111iiii - II111iiii . OOooo000oo0 / Oo
 def take_action ( self ) :
  I11 = self . _setKnownStates ( )
  i1iIIIiI1I = [ OOoO000O0OO . identifier for OOoO000O0OO in self . states if len ( OOoO000O0OO . flipped ) < 2 ]
  i1iIIIiI1I . remove ( self . identifier )
  if 23 - 23: i11iIiiIii + OOooo000oo0
  oOo = 7
  if 63 - 63: i1
  if 57 - 57: iiiIIii1I1Ii
  if 14 - 14: i1 . OOooo000oo0 / II1i
  if 38 - 38: II111iiii % i11iIiiIii . ooo0Oo0 - O00oOoOoO0o0O + II1i
  Ooooo0Oo00oO0 = random . choice ( i1iIIIiI1I )
  if 12 - 12: iIii1I11I1II1 * OOooo000oo0 . ooo0Oo0 % Iii1iIIIII + O0
  O00 = [ OOoO000O0OO for OOoO000O0OO in self . states if len ( OOoO000O0OO . flipped ) == 0 and OOoO000O0OO . coins >= 3 and OOoO000O0OO . identifier != self . identifier ]
  O00 = sorted ( O00 , key = attrgetter ( 'coins' ) , reverse = True )
  o0OOOOO00o0O0 = [ OOoO000O0OO for OOoO000O0OO in self . states if len ( OOoO000O0OO . flipped ) == 0 and OOoO000O0OO . identifier != self . identifier ]
  o0o0OOO0o0 = [ OOoO000O0OO for OOoO000O0OO in self . states if OOoO000O0OO . identifier != self . identifier and len ( OOoO000O0OO . flipped ) != 2 ]
  o0o0OOO0o0 = sorted ( o0o0OOO0o0 , key = attrgetter ( 'coins' ) , reverse = True )
  if 84 - 84: o00
  for iIi1ii1I1 in IiII1IiiIiI1 :
   if len ( O00 ) >= 1 :
    if 71 - 71: O0IiiiIiI1iIiI1 . O0
    Ooooo0Oo00oO0 = O00 [ 0 ] . identifier
   elif len ( o0OOOOO00o0O0 ) >= 1 :
    if 73 - 73: O00oOoOoO0o0O % IIIiiIIii - II1i
    Ooooo0Oo00oO0 = o0OOOOO00o0O0 [ 0 ] . identifier
   elif len ( o0o0OOO0o0 ) >= 1 :
    Ooooo0Oo00oO0 = o0o0OOO0o0 [ 0 ] . identifier
  if 10 - 10: OOooo000oo0 % iII11iiIII111
  if 48 - 48: Iii1iIIIII + Iii1iIIIII / II111iiii / iIii1I11I1II1
  if 20 - 20: Oo
  if 77 - 77: IIIiiIIii / Iii1iIIIII
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / Oo
  if 28 - 28: O00oOoOoO0o0O - o00 . o00 + IIIiiIIii - OoooooooOO + O0
  if 95 - 95: ii1IiI1i % iiiIIii1I1Ii . O0
  if 15 - 15: ooo0Oo0 / II1i . II1i - i1IIi
  if self . states [ self . identifier ] . coins >= oOo :
   if 53 - 53: o00 + OOooo000oo0 * iiiIIii1I1Ii
   if 61 - 61: i1IIi * O00oOoOoO0o0O / OoooooooOO . i11iIiiIii . IIIiiIIii
   if 60 - 60: Iii1iIIIII / Iii1iIIIII
   if 46 - 46: II1i * O00oOoOoO0o0O - ii1IiI1i * iiiIIii1I1Ii - O0IiiiIiI1iIiI1
   if 83 - 83: OoooooooOO
   if 31 - 31: II111iiii - O00oOoOoO0o0O . O0IiiiIiI1iIiI1 % IIIiiIIii - O0
   i1iIIIiI1I = [ OOoO000O0OO . identifier for OOoO000O0OO in self . states if len ( OOoO000O0OO . flipped ) < 2 ]
   i1iIIIiI1I . remove ( self . identifier )
   return TargetedAction ( Action . coup , Ooooo0Oo00oO0 )
  elif I11 [ Character . duke ] < 2 :
   return Action . tax
  elif Character . captain and I11 [ Character . captain ] < 3 :
   return TargetedAction ( Action . extort , Ooooo0Oo00oO0 )
  elif Character . assassin in self . hidden and self . states [ self . identifier ] . coins >= 3 :
   return TargetedAction ( Action . assassinate , Ooooo0Oo00oO0 )
  elif I11 [ Character . duke ] == 3 :
   return Action . foreign_aid
  else :
   return Action . income
   if 4 - 4: II111iiii / ooo0Oo0 . o00ooo0
   if 58 - 58: O00oOoOoO0o0O * i11iIiiIii / IIIiiIIii % O0IiiiIiI1iIiI1 - iII11iiIII111 / iiiIIii1I1Ii
 def block_action ( self , actor , action , character , target ) :
  if 50 - 50: OOooo000oo0
  Ii1i11IIii1I = None
  if 52 - 52: Oo - OoooooooOO + II1i + II1i - Oo / O0IiiiIiI1iIiI1
  I11 = self . _setKnownStates ( )
  if 44 - 44: ooo0Oo0 . i1IIi - iII11iiIII111 . O0 - ooo0Oo0
  if 92 - 92: o00ooo0 . Iii1iIIIII + Oo
  if target == self . identifier and action == Action . assassinate and len ( self . hidden ) == 1 and I11 [ Character . contessa ] < 3 :
   return Character . contessa
   if 28 - 28: i1IIi * i1 - Oo * o00 * II1i / ii1IiI1i
  if len ( self . hidden ) > 0 and action . blockable ( self . hidden [ 0 ] ) :
   if action == Action . assassinate and target != self . identifier :
    return None
   else :
    Ii1i11IIii1I = self . hidden [ 0 ]
  if len ( self . hidden ) > 1 and action . blockable ( self . hidden [ 1 ] ) and target == self . identifier :
   if action == Action . assassinate and target != self . identifier :
    return None
   else :
    Ii1i11IIii1I = self . hidden [ 1 ]
    if 94 - 94: II111iiii % iII11iiIII111 / IIIiiIIii * iIii1I11I1II1
  if action == Action . assassinate and I11 [ Character . contessa ] < 3 :
   if 54 - 54: Oo - OOooo000oo0 + OoooooooOO
   if 70 - 70: II1i / Iii1iIIIII . o00ooo0 % i1
   if 67 - 67: IIIiiIIii * Oo . o00 - ii1IiI1i * Oo
   if 46 - 46: O00oOoOoO0o0O + IIIiiIIii . OOooo000oo0 * iiiIIii1I1Ii % o00
   if 86 - 86: OOooo000oo0 + II1i % i11iIiiIii * iiiIIii1I1Ii . ooo0Oo0 * Iii1iIIIII
   if 44 - 44: iiiIIii1I1Ii
   Ii1i11IIii1I = Character . contessa
  elif len ( self . hidden ) == 1 and action == Action . assassinate and target == self . identifier :
   Ii1i11IIii1I = Character . contessa
  elif action == Action . extort and I11 [ Character . ambassador ] < 3 and target == self . identifier :
   Ii1i11IIii1I = Character . ambassador
  elif action == Action . extort and I11 [ Character . captain ] < 2 and target == self . identifier :
   Ii1i11IIii1I = Character . captain
   if 88 - 88: O0IiiiIiI1iIiI1 % II1i . II111iiii
  elif action == Action . assassinate and I11 [ Character . contessa ] < 3 :
   Ii1i11IIii1I = Character . contessa
   if 38 - 38: Oo
   if 57 - 57: O0 / iiiIIii1I1Ii * O0IiiiIiI1iIiI1 / IIIiiIIii . II111iiii
   if 26 - 26: o00ooo0
  if len ( self . hidden ) == 0 :
   if 91 - 91: ii1IiI1i . iII11iiIII111 + ii1IiI1i - o00ooo0 / OoooooooOO
   if 39 - 39: iII11iiIII111 / ooo0Oo0 - II111iiii
   Ii1i11IIii1I = None
   if 98 - 98: iII11iiIII111 / Iii1iIIIII % iiiIIii1I1Ii . IIIiiIIii
   if 91 - 91: iiiIIii1I1Ii % i1
   if 64 - 64: Iii1iIIIII % o00ooo0 - O0IiiiIiI1iIiI1 - iiiIIii1I1Ii
   if 31 - 31: Iii1iIIIII - II111iiii . Iii1iIIIII
   if 18 - 18: Oo
  return Ii1i11IIii1I
  if 98 - 98: o00ooo0 * o00ooo0 / o00ooo0 + Iii1iIIIII
 def challenge ( self , actor , action , character , target ) :
  if 34 - 34: ooo0Oo0
  if 15 - 15: Iii1iIIIII * ooo0Oo0 * i1 % i11iIiiIii % IIIiiIIii - O00oOoOoO0o0O
  I11 = self . _setKnownStates ( )
  if target == self . identifier and action == Action . assassinate and Character . contessa not in self . hidden and len ( self . hidden ) == 1 and I11 [ Character . contessa ] < 3 :
   return True
   if 68 - 68: O0IiiiIiI1iIiI1 % i1IIi . o00 . iII11iiIII111
  o0 = False
  if 91 - 91: iIii1I11I1II1 + O0IiiiIiI1iIiI1
  if I11 [ character ] == 3 :
   return True
   if 31 - 31: o00 . IIIiiIIii . O00oOoOoO0o0O
   if 75 - 75: Iii1iIIIII + ii1IiI1i . IIIiiIIii . ooo0Oo0 + i1 . ii1IiI1i
  if action == Action . block and character == Character . contessa and len ( self . states [ actor ] . flipped ) >= 1 and self . states [ actor ] . flipped [ 0 ] == Character . contessa :
   return True
   if 96 - 96: O00oOoOoO0o0O . ooo0Oo0 - i1 + iIii1I11I1II1 / IIIiiIIii * O00oOoOoO0o0O
   if 65 - 65: II1i . iIii1I11I1II1 / O0 - II1i
   if 21 - 21: OOooo000oo0 * iIii1I11I1II1
   if 91 - 91: o00
   if 15 - 15: II111iiii
   if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
   if 75 - 75: IIIiiIIii % Oo % Oo . O0IiiiIiI1iIiI1
   if 5 - 5: Oo * ooo0Oo0 + IIIiiIIii . O00oOoOoO0o0O + IIIiiIIii
   if 91 - 91: O0
   if 61 - 61: II111iiii
   if 64 - 64: ooo0Oo0 / IIIiiIIii - O0 - Iii1iIIIII
  if o0 :
   o0 = o0
   if 86 - 86: Iii1iIIIII % IIIiiIIii / OOooo000oo0 / IIIiiIIii
   if 42 - 42: ii1IiI1i
  return o0
  if 67 - 67: O0IiiiIiI1iIiI1 . o00ooo0 . O0
  if 10 - 10: iII11iiIII111 % iII11iiIII111 - iIii1I11I1II1 / O00oOoOoO0o0O + II1i
  if 87 - 87: iiiIIii1I1Ii * iII11iiIII111 + O00oOoOoO0o0O / iIii1I11I1II1 / o00ooo0
 def flip ( self ) :
  if len ( self . hidden ) > 1 :
   if Character . contessa in self . hidden :
    if self . hidden [ 0 ] == Character . contessa :
     return self . hidden [ 1 ]
     if 37 - 37: o00ooo0 - ooo0Oo0 * iiiIIii1I1Ii % i11iIiiIii - O0IiiiIiI1iIiI1
  i1iIIi1 = self . _prioritize ( self . hidden )
  return self . hidden [ 0 ]
  if 83 - 83: Iii1iIIIII / OOooo000oo0
 def reveal ( self , challenger , action , character , taret ) :
  if character in self . hidden :
   return character
   if 34 - 34: o00
  return self . flip ( )
  if 57 - 57: iiiIIii1I1Ii . Iii1iIIIII . i1IIi
 def exchange ( self , drawn ) :
  i1iIIi1 = self . _prioritize ( list ( self . hidden ) + list ( drawn ) )
  return i1iIIi1 [ - 2 : ]
  if 42 - 42: Iii1iIIIII + iII11iiIII111 % O0
 def _prioritize ( self , characters ) :
  i1iIIi1 = [ ]
  i1iIIi1 . extend (
 [ Character . duke ] * characters . count ( Character . duke ) )
  i1iIIi1 . extend (
 [ Character . contessa ] * characters . count ( Character . contessa ) )
  i1iIIi1 . extend (
 [ Character . assassin ] * characters . count ( Character . assassin ) )
  i1iIIi1 . extend (
 [ Character . ambassador ] * characters . count ( Character . ambassador ) )
  i1iIIi1 . extend (
 [ Character . captain ] * characters . count ( Character . captain ) )
  if 6 - 6: iiiIIii1I1Ii
  return i1iIIi1
  if 68 - 68: IIIiiIIii - ii1IiI1i
 def _probOfCharacter ( character ) :
  IIi = self . _setKnownStates ( )
  ooOOoooooo = 15
  II1I = ooOOoooooo - count ( IIi )
  O0i1II1Iiii1I11 = IIi . count ( character )
  if 9 - 9: iII11iiIII111 / i1 - OOooo000oo0 / OoooooooOO / iIii1I11I1II1 - Oo
 def _setKnownStates ( self ) :
  o00oooO0Oo = [ ]
  for OOoO000O0OO in self . states :
   o00oooO0Oo += OOoO000O0OO . flipped
   if 78 - 78: II1i % O0IiiiIiI1iIiI1 + iII11iiIII111
  o00oooO0Oo += self . hidden
  if 64 - 64: iiiIIii1I1Ii * O0 . OOooo000oo0 + II111iiii
  if 6 - 6: IIIiiIIii / o00ooo0 . o00 . o00
  if 62 - 62: iII11iiIII111 + o00 % o00ooo0 + O00oOoOoO0o0O
  if 33 - 33: O0 . o00 . OOooo000oo0
  IIi = { OOoO000O0OO : o00oooO0Oo . count ( OOoO000O0OO ) for OOoO000O0OO in Character }
  if 72 - 72: i1IIi / ii1IiI1i + OoooooooOO - i1
  if 29 - 29: iII11iiIII111 + iiiIIii1I1Ii % O0
  return IIi
  if 10 - 10: Iii1iIIIII / O0IiiiIiI1iIiI1 - OOooo000oo0 * iIii1I11I1II1 - OOooo000oo0
  if 97 - 97: iII11iiIII111 + OOooo000oo0 * II1i + O00oOoOoO0o0O % o00ooo0
  if 74 - 74: iiiIIii1I1Ii - i1 + OoooooooOO + O0IiiiIiI1iIiI1 / IIIiiIIii
  if 23 - 23: O0
  for OOoO000O0OO in self . states :
   for o00oO0oOo00 in OOoO000O0OO . flipped :
    if 81 - 81: ii1IiI1i
    if Character . duke == o00oO0oOo00 :
     I11 [ "Duke" ] += 1
    if Character . assassin == o00oO0oOo00 :
     I11 [ "Assassin" ] += 1
    if Character . captain == o00oO0oOo00 :
     I11 [ "Captain" ] += 1
    if Character . ambassador == o00oO0oOo00 :
     I11 [ "Ambassador" ] += 1
    if Character . contessa == o00oO0oOo00 :
     I11 [ "Contessa" ] += 1
   for o00oO0oOo00 in hidden :
    if 42 - 42: ii1IiI1i / Iii1iIIIII / Oo + o00ooo0 / IIIiiIIii
    if Character . duke == o00oO0oOo00 :
     I11 [ "Duke" ] += 1
    if Character . assassin == o00oO0oOo00 :
     I11 [ "Assassin" ] += 1
    if Character . captain == o00oO0oOo00 :
     I11 [ "Captain" ] += 1
    if Character . ambassador == o00oO0oOo00 :
     I11 [ "Ambassador" ] += 1
    if Character . contessa == o00oO0oOo00 :
     I11 [ "Contessa" ] += 1
     if 84 - 84: ooo0Oo0 * II111iiii + i1
  return I11
  if 53 - 53: o00ooo0 % II111iiii . o00 - iIii1I11I1II1 - o00 * II111iiii
 def _probOfCharacter ( self , character ) :
  IIi = self . _setKnownStates ( )
  ooOOoooooo = 15
  II1I = ooOOoooooo - len ( IIi )
  O0i1II1Iiii1I11 = 3 - ( self . _howManyOf ( character ) )
  ooO0oOOooOo0 = ( O0i1II1Iiii1I11 / ( II1I ) ) * 100.0 * 2
  if 38 - 38: O0IiiiIiI1iIiI1
  return ooO0oOOooOo0
  if 84 - 84: iIii1I11I1II1 % o00ooo0 / iIii1I11I1II1 % Iii1iIIIII
 def _howManyOf ( self , character ) :
  o00oooO0Oo = [ ]
  for OOoO000O0OO in self . states :
   o00oooO0Oo += OOoO000O0OO . flipped
  o00oooO0Oo += self . hidden
  return o00oooO0Oo . count ( character )
  if 45 - 45: O0
  if 26 - 26: Iii1iIIIII - iIii1I11I1II1 - OOooo000oo0 / ii1IiI1i . IIIiiIIii % iIii1I11I1II1
  if 91 - 91: Oo . iIii1I11I1II1 / iiiIIii1I1Ii + i1IIi
  if 42 - 42: ooo0Oo0 . Oo . ooo0Oo0 - iII11iiIII111
def make_bot ( identifier ) :
 return o0o0Oo0oooo0 ( identifier )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
