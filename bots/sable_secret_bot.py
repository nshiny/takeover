from enum import Enum
from collections import namedtuple
from interface import Character,Action,Bot,TargetedAction
from operator import*
import itertools
import copy
import random
CayKAnSMjY=6
CayKAnSMjL=False

class TimeWimey3(Enum):
    YouWontFigureItOut3 = 10
    OkMaybeYouWill3 = 20
    Tichu3 = 5
    random = 1
    Rekt3 = 21

class AndAnyoneElse2(Bot):
 def WhoIsReading2(CayKAnSMjU,WhoIsReading3,CayKAnSMjJ):
  CayKAnSMjp=namedtuple("PlayerState",["identifier","coins","flipped"])
  CayKAnSMjp.identifier=CayKAnSMjJ.identifier
  CayKAnSMjp.coins=CayKAnSMjJ.coins
  CayKAnSMjp.flipped=[1 for x in range(len(CayKAnSMjJ.flipped)-1)]
  CayKAnSMjm=CayKAnSMjU.YouWontFigureItOut2()
  if(CayKAnSMjJ in CayKAnSMjm):
   CayKAnSMjm.remove(CayKAnSMjJ)
  CayKAnSMjm.append(CayKAnSMjp)
  if(WhoIsReading3 in CayKAnSMjm):
   CayKAnSMjm.remove(WhoIsReading3)
  if len(CayKAnSMjm)==1:
   return
  if CayKAnSMjp.identifier==CayKAnSMjU.identifier:
   CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Rekt3].append([1]*len(CayKAnSMjm))
  elif CayKAnSMjU.Gallifrey3 in CayKAnSMjm:
   CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Rekt3].append([0]*(CayKAnSMjY-(len(CayKAnSMjm)-1)))
  if len(CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Rekt3])>CayKAnSMjU.WhoIsReading1:
   CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Rekt3].pop(0)
  CayKAnSMjI=sorted(CayKAnSMjm,key=lambda x:len(x.flipped))
  CayKAnSMjz=[x for x in CayKAnSMjI if len(x.flipped)==len(CayKAnSMjI[0].flipped)]
  if len(CayKAnSMjI[0].flipped)!=len(CayKAnSMjI[-1].flipped):
   if len(CayKAnSMjp.flipped)==len(CayKAnSMjI[0].flipped):
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.OkMaybeYouWill3].append([1]*(len(CayKAnSMjm)-len(CayKAnSMjz)))
   else:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.OkMaybeYouWill3].append([0]*len(CayKAnSMjz))
   if len(CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.OkMaybeYouWill3])>CayKAnSMjU.WhoIsReading1:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.OkMaybeYouWill3].pop(0)
  CayKAnSMjr=sorted(CayKAnSMjm,key=lambda x:x.coins,reverse=True)
  if CayKAnSMjr[0].coins!=CayKAnSMjr[-1].coins:
   if CayKAnSMjp.coins==CayKAnSMjr[0].coins:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.YouWontFigureItOut3].append([1]*len(CayKAnSMjm))
   else:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.YouWontFigureItOut3].append([0]*(CayKAnSMjY-(len(CayKAnSMjm)-1)))
   if len(CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.YouWontFigureItOut3])>CayKAnSMjU.WhoIsReading1:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.YouWontFigureItOut3].pop(0)
  CayKAnSMjR=sorted(CayKAnSMjm,key=lambda x:CayKAnSMjU.ButMostlyKillBill3[x.identifier],reverse=True)
  if CayKAnSMjU.ButMostlyKillBill3[CayKAnSMjR[0].identifier]!=CayKAnSMjU.ButMostlyKillBill3[CayKAnSMjR[-1].identifier]:
   if CayKAnSMjU.ButMostlyKillBill3[CayKAnSMjp.identifier]==CayKAnSMjU.ButMostlyKillBill3[CayKAnSMjR[0].identifier]:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Tichu3].append([1]*len(CayKAnSMjm))
   else:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Tichu3].append([0]*(CayKAnSMjY-(len(CayKAnSMjm)-1)))
   if len(CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Tichu3])>CayKAnSMjU.WhoIsReading1:
    CayKAnSMjU.ThisMessOfCode2[WhoIsReading3.identifier][TimeWimey3.Tichu3].pop(0)
 def GetPlayersTimeWimey3(CayKAnSMjU,AllImDoing3):
  CayKAnSMjX=[]
  for CayKAnSMjN in list(TimeWimey3):
   CayKAnSMju=CayKAnSMjU.ThisMessOfCode2[AllImDoing3.identifier][CayKAnSMjN]
   if len(CayKAnSMju)==0 or len(CayKAnSMju)<CayKAnSMjU.WhoIsReading1:
    continue
   CayKAnSMjw=list(itertools.chain(*CayKAnSMju))
   if(sum(CayKAnSMjw)/len(CayKAnSMjw)>.9):
    CayKAnSMjX.append(CayKAnSMjN)
  if len(CayKAnSMjX)==0:
   CayKAnSMjX.append(TimeWimey3.random)
  return CayKAnSMjX
 def ThisMessOfCode0(CayKAnSMjU,actorID,action,targetID,succeeded):
  if action==Action.assassinate:
   CayKAnSMjU.Gallifrey2(actorID,Character.assassin)
   if succeeded:
    CayKAnSMjU.KillJakeToo2(targetID,Character.contessa)
  if action==Action.exchange:
   CayKAnSMjU.Gallifrey2(actorID,Character.ambassador)
  if action==Action.extort:
   CayKAnSMjU.Gallifrey2(actorID,Character.captain)
   if succeeded:
    CayKAnSMjU.KillJakeToo2(targetID,Character.ambassador)
    CayKAnSMjU.KillJakeToo2(targetID,Character.captain)
  if action==Action.tax:
   CayKAnSMjU.Gallifrey2(actorID,Character.duke)
  if action==Action.foreign_aid:
   if succeeded:
    for CayKAnSMjQ in CayKAnSMjU.BillAndJake2():
     if CayKAnSMjQ.identifier!=actorID:
      CayKAnSMjU.KillJakeToo2(CayKAnSMjQ.identifier,Character.duke)
 def Gallifrey2(CayKAnSMjU,GrandTichu3,CayKAnSMjV):
  if CayKAnSMjV not in CayKAnSMjU.GrandTichu1[GrandTichu3]:
   CayKAnSMjU.GrandTichu1[GrandTichu3]
  CayKAnSMjU.DontBlink1(GrandTichu3,CayKAnSMjV)
 def KillJakeToo2(CayKAnSMjU,GrandTichu3,CayKAnSMjV):
  if CayKAnSMjV in CayKAnSMjU.NowHereAreSomeWords1[GrandTichu3]:
   CayKAnSMjU.NowHereAreSomeWords1[GrandTichu3].append(CayKAnSMjV)
 def DontBlink1(CayKAnSMjU,GrandTichu3,CayKAnSMjV):
  if CayKAnSMjV in CayKAnSMjU.NowHereAreSomeWords1[GrandTichu3]:
   CayKAnSMjU.NowHereAreSomeWords1[GrandTichu3].remove(CayKAnSMjV)
 def Shrekt2(CayKAnSMjU,GrandTichu3,CayKAnSMjV):
  if CayKAnSMjV in CayKAnSMjU.GrandTichu1[GrandTichu3]:
   CayKAnSMjU.GrandTichu1[GrandTichu3].remove(CayKAnSMjV)
 def ButMostlyKillBill1(CayKAnSMjU,player1,player2):
  CayKAnSMjO=CayKAnSMjU.ThisMessOfCode3.index(CayKAnSMjU.identifier)
  CayKAnSMje=0
  while 1:
   CayKAnSMjO+=1
   if CayKAnSMjO>=len(CayKAnSMjU.ThisMessOfCode3):
    CayKAnSMjO=0
   if CayKAnSMjU.ThisMessOfCode3[CayKAnSMjO]==player1.identifier:
    return True
   if CayKAnSMjU.ThisMessOfCode3[CayKAnSMjO]==player2.identifier:
    return False
   CayKAnSMje+=1
  pass
 def Tichu0(CayKAnSMjU,AllImDoing3,likelyToGetHit={}):
  CayKAnSMjx=CayKAnSMjU.Gallifrey1(CayKAnSMjU.YouWontFigureItOut2(),AllImDoing3)
  CayKAnSMjH={}
  CayKAnSMjb=CayKAnSMjU.GetPlayersTimeWimey3(AllImDoing3)
  if TimeWimey3.random in CayKAnSMjb:
   return{}
  if TimeWimey3.Rekt3 in CayKAnSMjb:
   return{CayKAnSMjU.Gallifrey3:[TimeWimey3.Rekt3]}
  if TimeWimey3.OkMaybeYouWill3 in CayKAnSMjb or TimeWimey3.YouWontFigureItOut3:
   CayKAnSMjz=CayKAnSMjU.YouWontFigureItOut1(CayKAnSMjx,likelyToGetHit)
   if len(CayKAnSMjz)==1:
    CayKAnSMjH[CayKAnSMjz[0]]=[TimeWimey3.OkMaybeYouWill3]
   else:
    CayKAnSMjq=CayKAnSMjU.IsTargettingBill1(CayKAnSMjz)
    CayKAnSMjl=[x for x in CayKAnSMjq if x.coins==CayKAnSMjq[0].coins]
    for CayKAnSMjo in CayKAnSMjl:
     if CayKAnSMjo.coins>=7 and CayKAnSMjU.ButMostlyKillBill1(CayKAnSMjo,AllImDoing3):
      pass
     else:
      if CayKAnSMjo not in CayKAnSMjH:
       CayKAnSMjH[CayKAnSMjo]=[]
      CayKAnSMjH[CayKAnSMjo]+=[TimeWimey3.OkMaybeYouWill3,TimeWimey3.YouWontFigureItOut3]
    while len(CayKAnSMjH)==0 and len(CayKAnSMjq)>0:
     for CayKAnSMjo in CayKAnSMjz:
      CayKAnSMjq.remove(CayKAnSMjo)
     if len(CayKAnSMjq)>0:
      CayKAnSMjl=[x for x in CayKAnSMjq if x.coins==CayKAnSMjq[0].coins]
      for CayKAnSMjo in CayKAnSMjl:
       if CayKAnSMjo.coins>=7 and CayKAnSMjU.ButMostlyKillBill1(CayKAnSMjo,AllImDoing3):
        pass
       else:
        if CayKAnSMjo not in CayKAnSMjH:
         CayKAnSMjH[CayKAnSMjo]=[]
        CayKAnSMjH[CayKAnSMjo]+=[TimeWimey3.OkMaybeYouWill3,TimeWimey3.YouWontFigureItOut3]
  return CayKAnSMjH
 def TimeWimey1(CayKAnSMjU,Shrekt3):
  CayKAnSMjT=CayKAnSMjU.ThisMessOfCode1()
  if isinstance(Shrekt3,list):
   for CayKAnSMjV in Shrekt3:
    if CayKAnSMjT.count(CayKAnSMjV)<3:
     return False
   return True
  else:
   if CayKAnSMjT.count(Shrekt3)==3:
    return True
 def DontBlink0(CayKAnSMjU,Shrekt3,AllImDoing3):
  CayKAnSMjT=CayKAnSMjU.ThisMessOfCode1()
  if isinstance(Shrekt3,list):
   for CayKAnSMjV in Shrekt3:
    if CayKAnSMjT.count(CayKAnSMjV)<3 or CayKAnSMjV in CayKAnSMjU.GrandTichu1[AllImDoing3.identifier]:
     return False
   return True
  else:
   if CayKAnSMjT.count(Shrekt3)==3 or Shrekt3 in CayKAnSMjU.NowHereAreSomeWords1[AllImDoing3.identifier]:
    return True
 def AndAnyoneElse1(CayKAnSMjU,CayKAnSMjV):
  CayKAnSMjg=CayKAnSMjU.ThisMessOfCode1()
  CayKAnSMji=CayKAnSMjg.count(CayKAnSMjV)
  for CayKAnSMjW in CayKAnSMjU.GrandTichu1:
   if CayKAnSMjV in CayKAnSMjU.GrandTichu1[CayKAnSMjW]:
    CayKAnSMji+=1
  return CayKAnSMji
 def IsTargettingBill0(CayKAnSMjU,BillAndJake3,AndAnyoneElse3):
  CayKAnSMjh=0
  CayKAnSMjF=0
  for CayKAnSMjV in BillAndJake3:
   CayKAnSMjh+=CayKAnSMjU.AndAnyoneElse1(CayKAnSMjV)
  for CayKAnSMjV in AndAnyoneElse3:
   CayKAnSMjF+=CayKAnSMjU.AndAnyoneElse1(CayKAnSMjV)
  return CayKAnSMjh<CayKAnSMjF
 def KillJakeToo0(CayKAnSMjU,CayKAnSMjc,CayKAnSMjf):
  if CayKAnSMjc in CayKAnSMjU.hidden:
   return True
  if CayKAnSMjf in CayKAnSMjU.hidden:
   return True
  CayKAnSMjd=CayKAnSMjU.ThisMessOfCode1()
  for CayKAnSMjt in CayKAnSMjU.GrandTichu1:
   CayKAnSMjd+=CayKAnSMjU.GrandTichu1[CayKAnSMjt]
  CayKAnSMjD=0
  CayKAnSMjs=0
  if CayKAnSMjU.IsTargettingBill2[CayKAnSMjc]==1:
   CayKAnSMjD-=1000
  if CayKAnSMjU.IsTargettingBill2[CayKAnSMjf]==1:
   CayKAnSMjs-=1000
  if CayKAnSMjc in CayKAnSMjU.DontBlink3:
   CayKAnSMjD+=100
  if CayKAnSMjf in CayKAnSMjU.DontBlink3:
   CayKAnSMjs+=100
  CayKAnSMjD-=CayKAnSMjd.count(CayKAnSMjc)
  CayKAnSMjs-=CayKAnSMjd.count(CayKAnSMjf)
  if CayKAnSMjD==CayKAnSMjs:
   return random.choice([CayKAnSMjc,CayKAnSMjf])
  return CayKAnSMjD>CayKAnSMjs
 def IsTargettingBill3(CayKAnSMjU,characterToBluff):
  if characterToBluff in CayKAnSMjU.hidden:
   return True
  CayKAnSMjd=CayKAnSMjU.ThisMessOfCode1()
  for CayKAnSMjt in CayKAnSMjU.GrandTichu1:
   CayKAnSMjd+=CayKAnSMjU.GrandTichu1[CayKAnSMjt]
  if CayKAnSMjU.IsTargettingBill2[characterToBluff]==1:
   return False
  if characterToBluff in CayKAnSMjU.DontBlink3:
   return True
  if CayKAnSMjd.count(characterToBluff)<2:
   return True
  return False
 def Rekt1(CayKAnSMjU):
  CayKAnSMjg=[]
  for x in CayKAnSMjU.states:
   CayKAnSMjg+=x.flipped
  return CayKAnSMjg
 def ThisMessOfCode1(CayKAnSMjU):
  CayKAnSMjg=CayKAnSMjU.Rekt1()
  CayKAnSMjg+=CayKAnSMjU.hidden
  CayKAnSMjg+=CayKAnSMjU.DontBlink3
  return CayKAnSMjg
 def DontBlink2(CayKAnSMjU,GrandTichu3):
  CayKAnSMjB=CayKAnSMjU.BillAndJake2()
  if GrandTichu3==CayKAnSMjU.identifier and len(CayKAnSMjU.hidden)==0 or len(CayKAnSMjB)==0:
   CayKAnSMjk=len(CayKAnSMjB)
   CayKAnSMjU.NowHereAreSomeWords3[CayKAnSMjk]+=1
 def ButMostlyKillBill2(CayKAnSMjU):
  CayKAnSMjP=CayKAnSMjU.YouWontFigureItOut2()
  if(len(CayKAnSMjP)==1):
   CayKAnSMjU.ButMostlyKillBill3[CayKAnSMjP[0].identifier]+=1
 def OkMaybeYouWill2(CayKAnSMjU,GrandTichu3):
  for x in CayKAnSMjU.states:
   if x.identifier==GrandTichu3:
    return x
 def Shrekt1(CayKAnSMjU,actor):
  if len(CayKAnSMjU.ThisMessOfCode3)==CayKAnSMjY:
   return
  if actor not in CayKAnSMjU.ThisMessOfCode3:
   CayKAnSMjU.ThisMessOfCode3.append(actor)
 def JustKillBill3(CayKAnSMjU,Shrekt3ToRank):
  CayKAnSMjE=[]
  CayKAnSMjG=[]
  for CayKAnSMjV in Shrekt3ToRank:
   if CayKAnSMjV not in CayKAnSMjE:
    CayKAnSMjE.append(CayKAnSMjV)
   else:
    CayKAnSMjG.append(CayKAnSMjV)
  CayKAnSMYj=sorted(CayKAnSMjE,key=lambda x:CayKAnSMjU.GrandTichu2[x],reverse=True)
  CayKAnSMYj+=sorted(CayKAnSMjG,key=lambda x:CayKAnSMjU.GrandTichu2[x],reverse=True)
  return CayKAnSMYj
 def Gallifrey1(CayKAnSMjU,listOfPlayers,playerToRemove):
  CayKAnSMYp=[]
  for CayKAnSMjt in listOfPlayers:
   if CayKAnSMjt.identifier!=playerToRemove.identifier:
    CayKAnSMYp.append(CayKAnSMjt)
  return CayKAnSMYp
 def AndAnyoneElse0(CayKAnSMjU,KillJakeToo3,AllImDoing3,excludePlayer):
  CayKAnSMYJ=CayKAnSMjU.Gallifrey1(KillJakeToo3,excludePlayer)
  CayKAnSMYJ=[x for x in CayKAnSMYJ if len(x.flipped)==len(AllImDoing3.flipped)]
  CayKAnSMYJ=CayKAnSMjU.IsTargettingBill1(CayKAnSMYJ)
  if len(CayKAnSMYJ)==0:
   return 0
  if AllImDoing3.coins==CayKAnSMYJ[0].coins:
   if len(CayKAnSMYJ)==1:
    return 0
   return(AllImDoing3.coins-CayKAnSMYJ[1].coins)+1
  else:
   return 0
 def YouWontFigureItOut0(CayKAnSMjU,KillJakeToo3,player):
  if len(KillJakeToo3)==0 or len(CayKAnSMjU.ThisMessOfCode3)<CayKAnSMjY:
   return[]
  CayKAnSMYm=[]
  CayKAnSMYU=[]
  CayKAnSMYI=[]
  CayKAnSMYz=CayKAnSMjU.ThisMessOfCode3.index(player.identifier)
  for CayKAnSMYr in KillJakeToo3:
   if CayKAnSMjU.ThisMessOfCode3.index(CayKAnSMYr.identifier)<CayKAnSMYz:
    CayKAnSMYU.append(CayKAnSMYr)
   elif CayKAnSMjU.ThisMessOfCode3.index(CayKAnSMYr.identifier)>CayKAnSMYz:
    CayKAnSMYI.append(CayKAnSMYr)
  CayKAnSMYU=sorted(CayKAnSMYU,key=lambda x:CayKAnSMjU.ThisMessOfCode3.index(x.identifier))
  CayKAnSMYI=sorted(CayKAnSMYI,key=lambda x:CayKAnSMjU.ThisMessOfCode3.index(x.identifier))
  return CayKAnSMYI+CayKAnSMYU
 def BillAndJake2(CayKAnSMjU):
  return[x for x in CayKAnSMjU.states if len(x.flipped)<2 and x.identifier!=CayKAnSMjU.identifier]
 def YouWontFigureItOut2(CayKAnSMjU):
  return[x for x in CayKAnSMjU.states if len(x.flipped)<2]
 def JustKillBill0(CayKAnSMjU):
  return[x for x in CayKAnSMjU.states if len(x.flipped)<2 and x.identifier!=CayKAnSMjU.identifier and x.coins>=7]
 def NowHereAreSomeWords2(CayKAnSMjU,originalCards,drawnCards,keptCards,CayKAnSMYR):
  if(len(CayKAnSMjU.DontBlink3)==0):
   CayKAnSMjU.DontBlink3=CayKAnSMYR
   return
  for CayKAnSMjV in drawnCards:
   if CayKAnSMjV in CayKAnSMjU.DontBlink3:
    CayKAnSMjU.DontBlink3.remove(CayKAnSMjV)
  for CayKAnSMjV in CayKAnSMYR:
   CayKAnSMjU.DontBlink3.append(CayKAnSMjV)
 def TimeWimey0(CayKAnSMjU):
  CayKAnSMYX=CayKAnSMjU.BillAndJake2()
  for CayKAnSMjt in CayKAnSMYX:
   if TimeWimey3.Rekt3 in CayKAnSMjU.GetPlayersTimeWimey3(CayKAnSMjt):
    return True
  return False
 def Rekt0(CayKAnSMjU):
  CayKAnSMYN=[]
  CayKAnSMYX=CayKAnSMjU.BillAndJake2()
  for CayKAnSMjt in CayKAnSMYX:
   if TimeWimey3.Rekt3 in CayKAnSMjU.GetPlayersTimeWimey3(CayKAnSMjt):
    CayKAnSMYN.append(CayKAnSMjt)
  return CayKAnSMYN
 def Shrekt0(CayKAnSMjU,peopleToCompeteWith):
  CayKAnSMYu=CayKAnSMjU.IsTargettingBill1(peopleToCompeteWith)
  return(CayKAnSMjU._myCoins-CayKAnSMYu[0].coins)+1
 def AllImDoing2(CayKAnSMjU,CayKAnSMYv,Rekt2,CayKAnSMYQ,CayKAnSMYO,CayKAnSMYe,CayKAnSMYm,CayKAnSMYx,desperate):
  if desperate and not(len(CayKAnSMjU.hidden)==2 and CayKAnSMYx):
   if CayKAnSMYQ and CayKAnSMYO and CayKAnSMjU._myCoins>=3:
    if Character.assassin in CayKAnSMjU.hidden and CayKAnSMjU.IsTargettingBill3(Character.captain):
     if CayKAnSMjU.IsTargettingBill0([Character.contessa],[Character.assassin,Character.captain]):
      return TargetedAction(Action.extort,Rekt2.identifier)
     else:
      return TargetedAction(Action.assassinate,Rekt2.identifier)
    if Character.assassin in CayKAnSMjU.hidden:
     return TargetedAction(Action.assassinate,Rekt2.identifier)
    if CayKAnSMjU.IsTargettingBill3(Character.captain):
     return TargetedAction(Action.extort,Rekt2.identifier)
   if CayKAnSMYQ and CayKAnSMjU._myCoins>=3:
    return TargetedAction(Action.assassinate,Rekt2.identifier)
   if CayKAnSMYO:
    return TargetedAction(Action.extort,Rekt2.identifier)
  if(CayKAnSMYQ):
   if CayKAnSMjU._myCoins>=7:
    return TargetedAction(Action.coup,Rekt2.identifier)
   if CayKAnSMjU._myCoins>=3 and Character.assassin in CayKAnSMjU.hidden and CayKAnSMjU.DontBlink0(Character.contessa,Rekt2):
    return TargetedAction(Action.assassinate,Rekt2.identifier)
  if(CayKAnSMYe):
   if TimeWimey3.OkMaybeYouWill3 in CayKAnSMYv:
    CayKAnSMYw=CayKAnSMjU.Shrekt0(CayKAnSMjU.YouWontFigureItOut1(CayKAnSMjU.Gallifrey1(CayKAnSMjU.BillAndJake2(),Rekt2)))
   else:
    CayKAnSMYw=CayKAnSMjU.Shrekt0(CayKAnSMjU.Gallifrey1(CayKAnSMjU.BillAndJake2(),Rekt2))
   if CayKAnSMYw<=7 and CayKAnSMjU._myCoins>=7:
    return TargetedAction(Action.coup,CayKAnSMYm[0].identifier)
   if CayKAnSMYw<=3 and CayKAnSMjU._myCoins>=3:
    for CayKAnSMjt in CayKAnSMYm:
     if Character.assassin in CayKAnSMjU.hidden and CayKAnSMjU.DontBlink0(Character.contessa,CayKAnSMjt):
      return TargetedAction(Action.assassinate,CayKAnSMjt.identifier)
    if Character.assassin in CayKAnSMjU.hidden:
     return TargetedAction(Action.assassinate,CayKAnSMYm[0].identifier)
  if(CayKAnSMYO):
   if CayKAnSMjU.IsTargettingBill3(Character.captain)and CayKAnSMjU.DontBlink0([Character.ambassador,Character.captain],Rekt2):
    return TargetedAction(Action.extort,Rekt2.identifier)
  return None
 def BillAndJake1(CayKAnSMjU,Rekt2,CayKAnSMYv,CayKAnSMYm,likelyToHaveOneLife):
  if Rekt2.identifier==CayKAnSMjU.identifier:
   pass
  if CayKAnSMjU._myCoins>=10:
   return TargetedAction(Action.coup,Rekt2.identifier)
  CayKAnSMYQ=(len(Rekt2.flipped)==1 or likelyToHaveOneLife)and CayKAnSMjU._myCoins>=3
  CayKAnSMYO=Rekt2.coins<=8
  CayKAnSMYe=TimeWimey3.YouWontFigureItOut3 in CayKAnSMYv
  CayKAnSMYx=TimeWimey3.Rekt3 in CayKAnSMYv
  CayKAnSMYH=CayKAnSMjU.AllImDoing2(CayKAnSMYv,Rekt2,CayKAnSMYQ,CayKAnSMYO,CayKAnSMYe,CayKAnSMYm,CayKAnSMYx,False)
  if CayKAnSMYH!=None:
   return CayKAnSMYH
  CayKAnSMYH=CayKAnSMjU.AllImDoing2(CayKAnSMYv,Rekt2,CayKAnSMYQ,CayKAnSMYO,CayKAnSMYe,CayKAnSMYm,CayKAnSMYx,True)
  if CayKAnSMYH!=None:
   return CayKAnSMYH
  return None
 def StopItNow3(CayKAnSMjU):
  CayKAnSMYm=CayKAnSMjU.WhoIsReading0(CayKAnSMjU.BillAndJake2())
  CayKAnSMYb=CayKAnSMjU.YouWontFigureItOut0(CayKAnSMjU.JustKillBill0(),CayKAnSMjU.Gallifrey3)
  CayKAnSMYq={x:0 for x in CayKAnSMYm}
  for CayKAnSMYl in CayKAnSMYb:
   CayKAnSMjH=CayKAnSMjU.Tichu0(CayKAnSMYl,CayKAnSMYq)
   if len(CayKAnSMjH)>=1:
    CayKAnSMYo=sorted(list(CayKAnSMjH.keys()),key=lambda x:x.identifier)
    CayKAnSMjJ=CayKAnSMYo[0]
    CayKAnSMYv=CayKAnSMjH[CayKAnSMjJ]
    if CayKAnSMjJ==CayKAnSMjU.Gallifrey3:
     CayKAnSMYH=CayKAnSMjU.BillAndJake1(CayKAnSMYl,CayKAnSMYv,CayKAnSMYm,CayKAnSMYq[CayKAnSMYl])
     if CayKAnSMYH!=None:
      return CayKAnSMYH
    elif CayKAnSMjJ in CayKAnSMYb:
     if len(CayKAnSMjJ.flipped)==1:
      CayKAnSMYb.remove(CayKAnSMjJ)
     else:
      CayKAnSMYq[CayKAnSMjJ]=1
  if(CayKAnSMjU._myCoins>=7):
   return TargetedAction(Action.coup,CayKAnSMYm[0].identifier)
  if(Character.assassin in CayKAnSMjU.hidden and CayKAnSMjU._myCoins>=3):
   for CayKAnSMjt in CayKAnSMYm:
    if CayKAnSMjU.DontBlink0(Character.contessa,CayKAnSMjt):
     return TargetedAction(Action.assassinate,CayKAnSMjt.identifier)
  if(Character.captain in CayKAnSMjU.hidden):
   for CayKAnSMjt in CayKAnSMYm:
    if CayKAnSMjU.DontBlink0([Character.ambassador,Character.captain],CayKAnSMjt)and CayKAnSMjt.coins>=2:
     return TargetedAction(Action.extort,CayKAnSMjt.identifier)
  if(Character.duke in CayKAnSMjU.hidden):
   return Action.tax
  if(Character.ambassador in CayKAnSMjU.hidden or CayKAnSMjU.IsTargettingBill3(Character.ambassador))and ((len(CayKAnSMjU.DontBlink3)<3 and CayKAnSMjU._myCoins>=3 and CayKAnSMjU.TimeWimey0()==False)):
   return Action.exchange
  if CayKAnSMjU.TimeWimey1(Character.duke):
   return Action.foreign_aid
  return Action.income
 def TimeWimey2(CayKAnSMjU):
  CayKAnSMYT=CayKAnSMjU.BillAndJake2()[0]
  if(CayKAnSMjU._myCoins>=7):
   return TargetedAction(Action.coup,CayKAnSMYT.identifier)
  if(Character.assassin in CayKAnSMjU.hidden and CayKAnSMjU._myCoins>=3):
   if CayKAnSMjU.DontBlink0(Character.contessa,CayKAnSMYT):
    return TargetedAction(Action.assassinate,CayKAnSMYT.identifier)
  if(Character.captain in CayKAnSMjU.hidden):
   if CayKAnSMjU.DontBlink0([Character.ambassador,Character.captain],CayKAnSMYT)and CayKAnSMYT.coins>=1:
    return TargetedAction(Action.extort,CayKAnSMYT.identifier)
  if(Character.duke in CayKAnSMjU.hidden):
   return Action.tax
  if CayKAnSMjU.DontBlink0(Character.duke,CayKAnSMYT):
   return Action.foreign_aid
  if(Character.ambassador in CayKAnSMjU.hidden and len(CayKAnSMjU.DontBlink3)<3):
   return Action.exchange
  return Action.income
 def Tichu2(CayKAnSMjU):
  pass
 def YouWontFigureItOut1(CayKAnSMjU,playersToPickFrom,likelyToGetHit={}):
  CayKAnSMYN=[]
  for CayKAnSMYV in playersToPickFrom:
   CayKAnSMYV in likelyToGetHit and likelyToGetHit[CayKAnSMYV]==1
   if len(CayKAnSMYV.flipped)==0 and not(CayKAnSMYV in likelyToGetHit and likelyToGetHit[CayKAnSMYV]==1):
    CayKAnSMYN.append(CayKAnSMYV)
  if len(CayKAnSMYN)==0:
   for CayKAnSMYV in playersToPickFrom:
    if not(CayKAnSMYV in likelyToGetHit and likelyToGetHit[CayKAnSMYV]==1):
     CayKAnSMYN.append(CayKAnSMYV)
  return CayKAnSMYN
 def OkMaybeYouWill1(CayKAnSMjU,playersToPickFrom):
  CayKAnSMYN=[]
  CayKAnSMYg=0
  for CayKAnSMYV in playersToPickFrom:
   if CayKAnSMYV.coins>CayKAnSMYg:
    CayKAnSMYN=[]
    CayKAnSMYN.append(CayKAnSMYV)
    CayKAnSMYg=CayKAnSMYV.coins
   elif CayKAnSMYV.coins==CayKAnSMYg:
    CayKAnSMYN.append(CayKAnSMYV)
  return CayKAnSMYN
 def WhoIsReading0(CayKAnSMjU,playersToSort):
  CayKAnSMYi=CayKAnSMjU.OkMaybeYouWill0(playersToSort)
  CayKAnSMYW=CayKAnSMjU.Rekt0()
  CayKAnSMYh=[]
  for CayKAnSMjt in CayKAnSMYi:
   if CayKAnSMjt in CayKAnSMYW:
    CayKAnSMYi.remove(CayKAnSMjt)
    CayKAnSMYh.append(CayKAnSMjt)
  return CayKAnSMYh+CayKAnSMYi
 def BillAndJake0(CayKAnSMjU,playersToSort):
  CayKAnSMYi=CayKAnSMjU.OkMaybeYouWill0(playersToSort)
  CayKAnSMYW=CayKAnSMjU.Rekt0()
  CayKAnSMYF=[]
  for CayKAnSMjt in CayKAnSMYi:
   if CayKAnSMjt in CayKAnSMYW:
    CayKAnSMYi.remove(CayKAnSMjt)
    CayKAnSMYF.append(CayKAnSMjt)
  for CayKAnSMjt in CayKAnSMYi:
   if CayKAnSMjt.coins>=7 and TimeWimey3.random in CayKAnSMjU.GetPlayersTimeWimey3(CayKAnSMjt):
    CayKAnSMYi.remove(CayKAnSMjt)
    CayKAnSMYF.append(CayKAnSMjt)
  return CayKAnSMYF+CayKAnSMYi
 def OkMaybeYouWill0(CayKAnSMjU,playersToSort):
  CayKAnSMYi=sorted(playersToSort,key=lambda x:CayKAnSMjU.ButMostlyKillBill3[x.identifier],reverse=True)
  CayKAnSMYi=sorted(CayKAnSMYi,key=lambda x:x.coins,reverse=True)
  CayKAnSMYi=sorted(CayKAnSMYi,key=lambda x:len(x.flipped))
  return CayKAnSMYi
 def AllImDoing1(CayKAnSMjU,playersToSort):
  CayKAnSMYi=sorted(playersToSort,key=lambda x:len(x.flipped))
  return CayKAnSMYi
 def IsTargettingBill1(CayKAnSMjU,playersToSort):
  CayKAnSMYi=sorted(playersToSort,key=lambda x:x.coins,reverse=True)
  return CayKAnSMYi
 def NowHereAreSomeWords0(CayKAnSMjU,playersToSort):
  CayKAnSMYi=sorted(playersToSort,key=lambda x:x.coins,reverse=True)
  CayKAnSMYi=sorted(CayKAnSMYi,key=lambda x:len(x.flipped))
  return CayKAnSMYi
 def __init__(CayKAnSMjU,CayKAnSMYd):
  CayKAnSMjU.identifier=CayKAnSMYd
  CayKAnSMjU._gameCount=0
  CayKAnSMjU.ButMostlyKillBill3={x:0 for x in range(CayKAnSMjY)}
  CayKAnSMjU.NowHereAreSomeWords3={x:0 for x in range(CayKAnSMjY)}
  CayKAnSMjU.ThisMessOfCode2={x:{y:[]for y in list(TimeWimey3)}for x in range(CayKAnSMjY)}
  CayKAnSMjU.WhoIsReading1=10
 def start(CayKAnSMjU):
  CayKAnSMjU._gameCount+=1
  CayKAnSMjU.GrandTichu2={Character.duke:10,Character.captain:8,Character.contessa:2,Character.assassin:4,Character.ambassador:1}
  CayKAnSMjU.DontBlink3=[]
  CayKAnSMjU.GrandTichu1={x:[]for x in range(CayKAnSMjY)}
  CayKAnSMjU.NowHereAreSomeWords1={x:[]for x in range(CayKAnSMjY)}
  CayKAnSMjU.IsTargettingBill2={x:0 for x in list(Character)}
  CayKAnSMjU.ThisMessOfCode3=[]
 def update_state(CayKAnSMjU,CayKAnSMYD,CayKAnSMYs):
  CayKAnSMjU.states=CayKAnSMYD
  CayKAnSMjU.hidden=list(CayKAnSMYs)
  CayKAnSMjU.Gallifrey3=CayKAnSMjU.states[CayKAnSMjU.identifier]
  CayKAnSMjU._myCoins=CayKAnSMjU.states[CayKAnSMjU.identifier].coins
 def take_action(CayKAnSMjU):
  if(len(CayKAnSMjU.BillAndJake2())==1):
   return CayKAnSMjU.TimeWimey2()
  else:
   return CayKAnSMjU.StopItNow3()
 def block_action(CayKAnSMjU,actor,action,character,target):
  CayKAnSMYc=CayKAnSMjU.YouWontFigureItOut2()
  CayKAnSMYf=CayKAnSMjU.NowHereAreSomeWords0(CayKAnSMjU.Gallifrey1(CayKAnSMYc,CayKAnSMjU.OkMaybeYouWill2(actor)))
  if len(CayKAnSMYf)==0:
   return None
  if target==CayKAnSMjU.identifier and action==Action.extort and CayKAnSMjU.TimeWimey0()==False and CayKAnSMYf[0]!=CayKAnSMjU.Gallifrey3 and len(CayKAnSMYc)>3:
   CayKAnSMjU.IsTargettingBill2[Character.ambassador]=1
   CayKAnSMjU.IsTargettingBill2[Character.captain]=1
   return None
  if len(CayKAnSMjU.hidden)>0 and action.blockable(CayKAnSMjU.hidden[0]):
   return CayKAnSMjU.hidden[0]
  if len(CayKAnSMjU.hidden)>1 and action.blockable(CayKAnSMjU.hidden[1]):
   return CayKAnSMjU.hidden[1]
  if action==Action.assassinate and len(CayKAnSMjU.hidden)==1:
   return Character.contessa
  if target==CayKAnSMjU.identifier and(len(CayKAnSMYc)<=3 or CayKAnSMjU.TimeWimey0()==True):
   if action==Action.assassinate:
    if CayKAnSMjU.IsTargettingBill3(Character.contessa):
     return Character.contessa
   if action==Action.extort:
    if CayKAnSMjU.IsTargettingBill3(Character.ambassador)and CayKAnSMjU.IsTargettingBill3(Character.captain):
     if CayKAnSMjU.KillJakeToo0(Character.ambassador,Character.captain):
      return Character.ambassador
     else:
      return Character.captain
    elif CayKAnSMjU.IsTargettingBill3(Character.ambassador):
     return Character.ambassador
    elif CayKAnSMjU.IsTargettingBill3(Character.captain):
     return Character.captain
  if(action==Action.extort):
   CayKAnSMjU.IsTargettingBill2[Character.captain]=1
   CayKAnSMjU.IsTargettingBill2[Character.ambassador]=1
  if(action==Action.foreign_aid):
   CayKAnSMjU.IsTargettingBill2[Character.duke]=1
  return None
 def challenge(CayKAnSMjU,actor,action,character,target):
  if target==CayKAnSMjU.identifier and action==Action.assassinate and CayKAnSMjU.IsTargettingBill3(Character.contessa)==False and len(CayKAnSMjU.hidden)==1:
   return True
  if target==CayKAnSMjU.identifier:
   if CayKAnSMjU.ThisMessOfCode1().count(character)==3:
    return True
  if action==Action.block and target==CayKAnSMjU.identifier:
   return True
  return False
 def notify_action(CayKAnSMjU,actor,action,target,succeeded):
  CayKAnSMjU.Shrekt1(actor)
  CayKAnSMjU.ThisMessOfCode0(actor,action,target,succeeded)
  if action==Action.coup:
   CayKAnSMjU.WhoIsReading2(CayKAnSMjU.OkMaybeYouWill2(actor),CayKAnSMjU.OkMaybeYouWill2(target))
  if action==Action.exchange and actor!=CayKAnSMjU.identifier:
   CayKAnSMjU.DontBlink3=[]
 def notify_block(CayKAnSMjU,blocker,character,actor,action,succeeded):
  CayKAnSMjU.Gallifrey2(blocker,character)
 def notify_challenge(CayKAnSMjU,challenger,actor,action,character,target,revealed):
  if actor==CayKAnSMjU.identifier and revealed!=character:
   pass
  if revealed==character and actor!=CayKAnSMjU.identifier:
   CayKAnSMjU.DontBlink3=[]
 def notify_flip(CayKAnSMjU,player,flipped):
  CayKAnSMjU.Shrekt2(player,flipped)
  CayKAnSMjU.ButMostlyKillBill2()
  CayKAnSMYB=CayKAnSMjU.Rekt1()
  if CayKAnSMYB.count(flipped)==3:
   if flipped==Character.contessa:
    CayKAnSMjU.GrandTichu2[Character.assassin]*=10
   if flipped==Character.assassin:
    CayKAnSMjU.GrandTichu2[Character.contessa]*=-1
 def notify_end(CayKAnSMjU):
  pass
 def flip(CayKAnSMjU):
  CayKAnSMYj=CayKAnSMjU.JustKillBill3(CayKAnSMjU.hidden)
  return CayKAnSMYj[-1]
 def exchange(CayKAnSMjU,drawn):
  CayKAnSMYj=CayKAnSMjU.JustKillBill3(CayKAnSMjU.hidden+list(drawn))
  CayKAnSMjU.NowHereAreSomeWords2(CayKAnSMjU.hidden,drawn,CayKAnSMYj[:-2],CayKAnSMYj[-2:])
  return CayKAnSMYj[-2:]
 def reveal(CayKAnSMjU,challenger,action,character,target):
  if character in CayKAnSMjU.hidden:
   return character
  return CayKAnSMjU.flip()
def make_bot(CayKAnSMYd):
 return AndAnyoneElse2(CayKAnSMYd)