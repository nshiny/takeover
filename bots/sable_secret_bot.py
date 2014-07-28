from interface import*
from operator import*
import itertools
qgSiLCvryQ=False
class BillAndJake0(Enum):
    stopBeing0 = 1
    jerks0 = 2
    andTrying0 = 3
    toRead0 = 4
    myCode0 = 5
    stuYou0 = 6
    shouldStop0 = 7
class qgSiLCvryj:
 def __init__(qgSiLCvryK):
  qgSiLCvryK.wholeGameTargetBillAndJake0={}
  qgSiLCvryK.anyoneElse0={x:0 for x in range(6)}
  qgSiLCvryK.targetBillAndJake0Queue={x:[]for x in range(6)}
  qgSiLCvryK.BillAndJake1=10
  qgSiLCvryK.stopBeing1={x:0 for x in range(6)}
  qgSiLCvryK.jerks1=[]
  qgSiLCvryK.andTrying1=20
  qgSiLCvryK.toRead1={x:{y:0 for y in range(6)}for x in range(6)}
  for i in range(6):
   qgSiLCvryK.wholeGameTargetBillAndJake0[i]={}
   for qgSiLCvryX in(list(BillAndJake0)):
    qgSiLCvryK.wholeGameTargetBillAndJake0[i][qgSiLCvryX]=0
 def myCode1(qgSiLCvryK,qgSiLCvryB,qgSiLCvryN):
  qgSiLCvryI=len([x for x in qgSiLCvryB if len(x.flipped)==2])
  qgSiLCvryO=len(qgSiLCvryB)-qgSiLCvryI
  if(len(qgSiLCvryB[qgSiLCvryN].flipped)==2):
   qgSiLCvryK.toRead1[qgSiLCvryN][qgSiLCvryO]+=1
  if(qgSiLCvryI==len(qgSiLCvryB)-1):
   for qgSiLCvryH in qgSiLCvryB:
    if len(qgSiLCvryH.flipped)<2:
     qgSiLCvryK.toRead1[qgSiLCvryH.identifier][0]+=1
 def stuYou1(qgSiLCvryK,qgSiLCvryB,myID,qgSiLCvrym,qgSiLCvryJ):
  qgSiLCvryK.anyoneElse0[qgSiLCvrym]+=1
  qgSiLCvryW=[]
  if(qgSiLCvryJ==myID):
   qgSiLCvryK.stopBeing1[qgSiLCvrym]+=1
   qgSiLCvryK.jerks1.append(qgSiLCvrym)
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.stuYou0]+=1
   qgSiLCvryW.append(BillAndJake0.stuYou0)
   if(len(qgSiLCvryK.jerks1)>qgSiLCvryK.andTrying1):
    qgSiLCvryK.jerks1.pop(0)
  qgSiLCvryY=1
  qgSiLCvryV=2
  qgSiLCvryz=0
  qgSiLCvryk=999
  qgSiLCvryw=0
  qgSiLCvryf=[x for x in qgSiLCvryB if len(x.flipped)<2 and x.identifier!=qgSiLCvrym]
  for qgSiLCvryb in qgSiLCvryf:
   if qgSiLCvryb.coins>qgSiLCvryz:
    qgSiLCvryz=qgSiLCvryb.coins
   if qgSiLCvryb.coins<qgSiLCvryk:
    qgSiLCvryk=qgSiLCvryb.coins
   if len(qgSiLCvryb.flipped)==1:
    qgSiLCvryV=1
   if len(qgSiLCvryb.flipped)==0:
    qgSiLCvryY=2
   if qgSiLCvryK.toRead1[qgSiLCvryb.identifier][0]>qgSiLCvryw:
    qgSiLCvryw=qgSiLCvryK.toRead1[qgSiLCvryb.identifier][0]
  qgSiLCvryG=[x for x in qgSiLCvryB if x.identifier==qgSiLCvryJ][0]
  if(qgSiLCvryG.coins==qgSiLCvryz):
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.jerks0]+=1
   qgSiLCvryW.append(BillAndJake0.jerks0)
  if(qgSiLCvryG.coins==qgSiLCvryk):
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.stopBeing0]+=1
   qgSiLCvryW.append(BillAndJake0.stopBeing0)
  if(len(qgSiLCvryG.flipped)==1 and qgSiLCvryY==2):
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.andTrying0]+=1
   qgSiLCvryW.append(BillAndJake0.andTrying0)
  if(len(qgSiLCvryG.flipped)==0 and qgSiLCvryV==1):
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.toRead0]+=1
   qgSiLCvryW.append(BillAndJake0.toRead0)
  if(qgSiLCvryK.toRead1[qgSiLCvryG.identifier][0]==qgSiLCvryw):
   qgSiLCvryK.wholeGameTargetBillAndJake0[qgSiLCvrym][BillAndJake0.myCode0]+=1
   qgSiLCvryW.append(BillAndJake0.myCode0)
  qgSiLCvryK.targetBillAndJake0Queue[qgSiLCvrym].append(qgSiLCvryW)
  if(len(qgSiLCvryK.targetBillAndJake0Queue[qgSiLCvrym])>qgSiLCvryK.BillAndJake1):
   qgSiLCvryK.targetBillAndJake0Queue[qgSiLCvrym].pop(0)
 def shouldStop1(qgSiLCvryK,playerID):
  if(len(qgSiLCvryK.targetBillAndJake0Queue[playerID])<10):
   return[BillAndJake0.shouldStop0]
  qgSiLCvryx=list(itertools.chain(*qgSiLCvryK.targetBillAndJake0Queue[playerID]))
  qgSiLCvryt=[]
  for qgSiLCvryT in list(BillAndJake0):
   if(qgSiLCvryx.count(qgSiLCvryT)>len(qgSiLCvryK.targetBillAndJake0Queue[playerID])*.7):
    qgSiLCvryt.append(qgSiLCvryT)
  if len(qgSiLCvryt)==0:
   qgSiLCvryt.append(BillAndJake0.shouldStop0)
  return qgSiLCvryt
 def too1(qgSiLCvryK):
  pass
 def anyoneElse1(qgSiLCvryK,qgSiLCvryN):
  qgSiLCvryw=0
  for x in qgSiLCvryK.toRead1:
   if qgSiLCvryK.toRead1[x][0]>qgSiLCvryw:
    qgSiLCvryw=qgSiLCvryK.toRead1[x][0]
  if qgSiLCvryK.toRead1[myPlayer.identifier][0]==qgSiLCvryw:
   return True
  return False
 def shouldGoForIt1(qgSiLCvryK,qgSiLCvryB,qgSiLCvryN,ignore=None):
  if ignore==None:
   qgSiLCvryh=[x for x in opponents if len(x.flipped)<2]
  else:
   qgSiLCvryh=[x for x in opponents if len(x.flipped)<2 and x.identifier!=ignore]
  return qgSiLCvryN.coins==sorted(qgSiLCvryh,key=attrgetter('coins'),reverse=True)[0]
 def shouldGoForIt1NoTie(qgSiLCvryK,qgSiLCvryB,qgSiLCvryN,ignore=None):
  if ignore==None:
   qgSiLCvryh=[x for x in opponents if len(x.flipped)<2]
  else:
   qgSiLCvryh=[x for x in opponents if len(x.flipped)<2 and x.identifier!=ignore]
  qgSiLCvrye=sorted(qgSiLCvryh,key=attrgetter('coins'),reverse=True)
  return(qgSiLCvryN.coins==qgSiLCvrye[0])and qgSiLCvryN.coins!=qgSiLCvrye[1]
 def stopBeing2(qgSiLCvryK,myCharacter,opponents):
  qgSiLCvryn={}
  qgSiLCvrys=[x for x in opponents if x.identifier!=myCharacter.identifier and len(x.flipped)<2 and x.coins>=7]
  for qgSiLCvryu in qgSiLCvrys:
   qgSiLCvrya=[]
   qgSiLCvryU=[x for x in opponents if len(x.flipped)<2]
   qgSiLCvryU.append(myCharacter)
   qgSiLCvryE=qgSiLCvryK.shouldStop1(qgSiLCvryu.identifier)
   if BillAndJake0.stuYou0 in qgSiLCvryE:
    qgSiLCvrya.append(BillAndJake0.stuYou0)
   if BillAndJake0.myCode0 in qgSiLCvryE:
    qgSiLCvryw=0
    for x in qgSiLCvryU:
     if qgSiLCvryK.toRead1[x.identifier][0]>qgSiLCvryw:
      qgSiLCvryw=qgSiLCvryK.toRead1[x.identifier][0]
    if qgSiLCvryw==qgSiLCvryK.toRead1[myCharacter.identifier][0]:
     qgSiLCvrya.append(BillAndJake0.myCode0)
   if BillAndJake0.stopBeing0 in qgSiLCvryE:
    qgSiLCvryk=999
    for x in qgSiLCvryU:
     if x.coins<qgSiLCvryk:
      qgSiLCvryk=x.coins
    if myCharacter.coins==qgSiLCvryk:
     qgSiLCvrya.append(BillAndJake0.stopBeing0)
   if BillAndJake0.andTrying0 in qgSiLCvryE:
    qgSiLCvryV=999
    for x in qgSiLCvryU:
     if(2-len(x.flipped))<qgSiLCvryV:
      qgSiLCvryV=(2-len(x.flipped))
    if len(myCharacter.flipped)==qgSiLCvryV:
     qgSiLCvrya.append(BillAndJake0.andTrying0)
   if BillAndJake0.jerks0 in qgSiLCvryE:
    qgSiLCvryz=0
    for x in qgSiLCvryU:
     if x.coins>qgSiLCvryz:
      qgSiLCvryz=x.coins
    if myCharacter.coins==qgSiLCvryz:
     qgSiLCvrya.append(BillAndJake0.jerks0)
   if BillAndJake0.toRead0 in qgSiLCvryE:
    qgSiLCvryd=[x for x in qgSiLCvryU and len(x.flipped)==0]
    if(len(qgSiLCvryd)==1)and myCharacter in qgSiLCvryd:
     qgSiLCvrya.append(BillAndJake0.toRead0)
   if(len(qgSiLCvrya)>0):
    if(BillAndJake0.toRead0 in qgSiLCvrya and BillAndJake0.jerks0 in qgSiLCvrya):
     qgSiLCvrya.remove(BillAndJake0.jerks0)
    if(BillAndJake0.andTrying0 in qgSiLCvrya):
     qgSiLCvrya.remove(BillAndJake0.andTrying0)
    qgSiLCvryn[qgSiLCvryu]=qgSiLCvrya
  return qgSiLCvryn
class jerks2(Bot):
 def __init__(qgSiLCvryK,qgSiLCvryc):
  qgSiLCvryK.identifier=qgSiLCvryc
  qgSiLCvryK.andTrying2=0
  qgSiLCvryK.toRead2=[]
  qgSiLCvryK.myCode2=False
  qgSiLCvryK.stuYou2=qgSiLCvryj()
  qgSiLCvryK.shouldStop2=0
 def start(qgSiLCvryK):
  qgSiLCvryK.andTrying2+=1
  qgSiLCvryK.toRead2=[]
 def notify_end(qgSiLCvryK):
  if qgSiLCvryQ:
   for qgSiLCvryp in qgSiLCvryK.stuYou2.toRead1:
    if(qgSiLCvryK.myCode2 or qgSiLCvryp==qgSiLCvryK.identifier):
     if(qgSiLCvryK.myCode2 and qgSiLCvryp==qgSiLCvryK.identifier):
      print("mee ",end=""),
     print(str(qgSiLCvryp)+":"+str(qgSiLCvryK.stuYou2.toRead1[qgSiLCvryp]))
   for qgSiLCvryD in qgSiLCvryK.stuYou2.wholeGameTargetBillAndJake0:
    qgSiLCvryK.stuYou2.shouldStop1(qgSiLCvryD)
    print(qgSiLCvryK.stuYou2.anyoneElse0[qgSiLCvryD])
    print(str(qgSiLCvryD)+" : "+str(qgSiLCvryK.stuYou2.wholeGameTargetBillAndJake0[qgSiLCvryD]))
 def update_state(qgSiLCvryK,qgSiLCvryB,qgSiLCvryl):
  qgSiLCvryK.states=qgSiLCvryB
  qgSiLCvryK.hidden=qgSiLCvryl
  qgSiLCvryK.player=[x for x in qgSiLCvryK.states if x.identifier==qgSiLCvryK.identifier][0]
 def notify_action(qgSiLCvryK,qgSiLCvrym,action,qgSiLCvryJ,succeeded):
  if action==Action.coup:
   qgSiLCvryK.stuYou2.stuYou1(qgSiLCvryK.states,qgSiLCvryK.identifier,qgSiLCvrym,qgSiLCvryJ)
  if Action.exchange==action and qgSiLCvrym!=qgSiLCvryK.identifier:
   qgSiLCvryK.toRead2=[]
 def notify_challenge(qgSiLCvryK,challenger,qgSiLCvrym,action,qgSiLCvrQN,qgSiLCvryJ,revealed):
  if(revealed==qgSiLCvrQN and qgSiLCvrym!=qgSiLCvryK.identifier):
   qgSiLCvryK.toRead2=[]
 def notify_flip(qgSiLCvryK,qgSiLCvryN,flipped):
  qgSiLCvryK.stuYou2.myCode1(qgSiLCvryK.states,qgSiLCvryN)
 def too2(qgSiLCvryK):
  qgSiLCvryR=[]
  for x in qgSiLCvryK.states:
   qgSiLCvryR+=x.flipped
  qgSiLCvryR+=qgSiLCvryK.hidden
  qgSiLCvryR+=qgSiLCvryK.toRead2
  return qgSiLCvryR
 def too2NoAmbass(qgSiLCvryK):
  qgSiLCvryR=[]
  for x in qgSiLCvryK.states:
   qgSiLCvryR+=x.flipped
  qgSiLCvryR+=qgSiLCvryK.hidden
  return qgSiLCvryR
 def shouldGoForIt2(qgSiLCvryK):
  qgSiLCvryA=qgSiLCvryK.states[qgSiLCvryK.identifier].coins
  qgSiLCvryJ=qgSiLCvryK.toRead3()[0].identifier
  qgSiLCvrQy=[x for x in qgSiLCvryK.states if x.identifier!=qgSiLCvryK.identifier and len(x.flipped)<2]
  qgSiLCvrys=[x for x in qgSiLCvryK.states if x.identifier!=qgSiLCvryK.identifier and len(x.flipped)<2 and x.coins>=7]
  qgSiLCvryn=qgSiLCvryK.stuYou2.stopBeing2(qgSiLCvryK.player,qgSiLCvrQy)
  if(len(qgSiLCvryn)==1):
   for qgSiLCvryp in qgSiLCvryn:
    qgSiLCvrya=qgSiLCvryn[qgSiLCvryp]
    if(len(qgSiLCvrya)==1 and BillAndJake0.jerks0 in qgSiLCvrya):
     if(qgSiLCvryA>=7):
      return TargetedAction(Action.coup,qgSiLCvryJ)
     elif(len(qgSiLCvryK.hidden)==1):
      return TargetedAction(Action.assassinate,qgSiLCvryJ)
    else:
     if(qgSiLCvryA>=7):
      return TargetedAction(Action.assassinate,qgSiLCvryp.identifier)
     if(len(qgSiLCvryK.hidden)==1):
      if(qgSiLCvryA>=3):
       return TargetedAction(Action.assassinate,qgSiLCvryJ)
      else:
       return TargetedAction(Action.extort,qgSiLCvryJ)
  if(qgSiLCvryA>=7):
   return TargetedAction(Action.coup,qgSiLCvryJ)
  qgSiLCvrQk=qgSiLCvryK.too2NoAmbass()
  qgSiLCvryR=qgSiLCvryK.too2()
  if(Character.ambassador in qgSiLCvryK.hidden or(qgSiLCvrQk.count(Character.ambassador)!=3 and not(qgSiLCvrQk.count(Character.ambassador)==2 and qgSiLCvryR.count(Character.ambassador)==2))):
   return Action.exchange
  elif(Character.duke in qgSiLCvryK.hidden or(qgSiLCvrQk.count(Character.duke)!=3 and not(qgSiLCvrQk.count(Character.duke)==2 and qgSiLCvryR.count(Character.duke)==2))):
   return Action.tax
  elif(qgSiLCvrQk.count(Character.duke)==3):
   return Action.foreign_aid
  else:
   return Action.income
 def BillAndJake3(qgSiLCvryK):
  qgSiLCvrQz=qgSiLCvryK.toRead3()
  qgSiLCvryJ=qgSiLCvrQz[0].identifier
  qgSiLCvryA=qgSiLCvryK.states[qgSiLCvryK.identifier].coins
  qgSiLCvryR=qgSiLCvryK.too2()
  qgSiLCvrQk=qgSiLCvryK.too2NoAmbass()
  qgSiLCvrQV=0
  qgSiLCvrQY=[]
  for qgSiLCvrQw in qgSiLCvrQz:
   if qgSiLCvrQw.coins>=7:
    qgSiLCvrQV+=1
   qgSiLCvrQY.append(qgSiLCvrQw.coins)
  qgSiLCvrQY.sort()
  if(len(qgSiLCvrQY)==2):
   qgSiLCvrQP=qgSiLCvrQY[1]
  else:
   qgSiLCvrQP=qgSiLCvrQY[2]
  if qgSiLCvryA>=7:
   return TargetedAction(Action.coup,qgSiLCvryJ)
  elif Character.duke in qgSiLCvryK.hidden and(qgSiLCvrQV==0 or(qgSiLCvryA+3)<qgSiLCvrQP):
   return Action.tax
  elif(Character.captain in qgSiLCvryK.hidden)and(qgSiLCvrQV==0 or(qgSiLCvryA+3)<qgSiLCvrQP):
   return TargetedAction(Action.extort,qgSiLCvryJ)
  elif(Character.captain not in qgSiLCvryK.hidden)and(qgSiLCvrQk.count(Character.captain)<3)and(qgSiLCvrQk.count(Character.ambassador)<3):
   return Action.exchange
  return Action.income
 def stopBeing3(qgSiLCvryK):
  qgSiLCvrQz=qgSiLCvryK.toRead3()
  qgSiLCvryJ=qgSiLCvrQz[0].identifier
  qgSiLCvryA=qgSiLCvryK.states[qgSiLCvryK.identifier].coins
  qgSiLCvryR=qgSiLCvryK.too2()
  qgSiLCvrQk=qgSiLCvryK.too2NoAmbass()
  if qgSiLCvryA>=7:
   return TargetedAction(Action.coup,qgSiLCvryJ)
  elif qgSiLCvryA>=3 and Character.assassin in qgSiLCvryK.hidden and qgSiLCvryR.count(Character.contessa)==3:
   return TargetedAction(Action.assassinate,qgSiLCvryJ)
  elif(qgSiLCvrQk.count(Character.duke)!=3 and not(qgSiLCvrQk.count(Character.duke)==2 and qgSiLCvryR.count(Character.duke)==2)):
   return Action.tax
  elif(Character.captain in qgSiLCvryK.hidden and qgSiLCvryR.count(Character.ambassador)==3 and qgSiLCvryR.count(Character.captain)==3):
   return TargetedAction(Action.extort,qgSiLCvryJ)
  elif(qgSiLCvrQk.count(Character.duke)==3):
   return Action.foreign_aid
  else:
   return Action.income
 def take_action(qgSiLCvryK):
  qgSiLCvrQz=qgSiLCvryK.toRead3()
  qgSiLCvryA=qgSiLCvryK.states[qgSiLCvryK.identifier].coins
  if(len(qgSiLCvrQz)>1):
   return qgSiLCvryK.shouldGoForIt2()
  else:
   return qgSiLCvryK.stopBeing3()
 def block_action(qgSiLCvryK,qgSiLCvrym,action,qgSiLCvrQN,qgSiLCvryJ):
  if len(qgSiLCvryK.hidden)>0 and action.blockable(qgSiLCvryK.hidden[0]):
   return qgSiLCvryK.hidden[0]
  if len(qgSiLCvryK.hidden)>1 and action.blockable(qgSiLCvryK.hidden[1]):
   return qgSiLCvryK.hidden[1]
  if action==Action.assassinate and len(qgSiLCvryK.hidden)==1:
   return Character.contessa
  return None
 def challenge(qgSiLCvryK,qgSiLCvrym,action,qgSiLCvrQN,qgSiLCvryJ):
  qgSiLCvryR=qgSiLCvryK.too2()
  if qgSiLCvryR.count(qgSiLCvrQN)==3:
   return True
  if qgSiLCvryJ==qgSiLCvryK.identifier and action==Action.assassinate and Character.contessa not in qgSiLCvryK.hidden and len(qgSiLCvryK.hidden)==1:
   if qgSiLCvryR.count(Character.assassin)>qgSiLCvryR.count(Character.contessa):
    return True
  return False
 def flip(qgSiLCvryK):
  qgSiLCvrQo=qgSiLCvryK.andTrying3(qgSiLCvryK.hidden)
  return qgSiLCvrQo[-1]
 def jerks3(qgSiLCvryK,qgSiLCvrQK):
  if(len(qgSiLCvryK.toRead2)==0):
   qgSiLCvryK.toRead2=qgSiLCvrQK
   return
  if qgSiLCvrQK[0]==qgSiLCvrQK[1]:
   if qgSiLCvryK.toRead2.count(qgSiLCvrQK[0])==1:
    qgSiLCvryK.toRead2.append(qgSiLCvrQK[0])
   elif qgSiLCvryK.toRead2.count(qgSiLCvrQK[0])==0:
    qgSiLCvryK.toRead2+qgSiLCvrQK
  else:
   for qgSiLCvrQX in qgSiLCvrQK:
    if qgSiLCvrQX not in qgSiLCvryK.toRead2:
     qgSiLCvryK.toRead2.append(qgSiLCvrQX)
  if(len(qgSiLCvryK.toRead2)>qgSiLCvryK.shouldStop2 and qgSiLCvryK.shouldStop2>=2):
   pass
  qgSiLCvryK.shouldStop2=len(qgSiLCvryK.toRead2)
 def exchange(qgSiLCvryK,drawn):
  qgSiLCvrQo=qgSiLCvryK.andTrying3(list(qgSiLCvryK.hidden)+list(drawn))
  qgSiLCvryt=qgSiLCvrQo[-2:]
  qgSiLCvryK.jerks3(qgSiLCvryt)
  return qgSiLCvryt
 def reveal(qgSiLCvryK,challenger,action,qgSiLCvrQN,qgSiLCvryJ):
  if qgSiLCvrQN in qgSiLCvryK.hidden:
   return qgSiLCvrQN
  return qgSiLCvryK.flip()
 def andTrying3(qgSiLCvryK,characters):
  qgSiLCvrQI=[Character.ambassador,Character.contessa,Character.captain,Character.duke,Character.assassin]
  qgSiLCvryR=qgSiLCvryK.too2()
  qgSiLCvrQo=[]
  qgSiLCvrQO=[]
  if(qgSiLCvryR.count(Character.assassin)==3):
   qgSiLCvrQI.remove(Character.contessa)
   qgSiLCvrQI.append(Character.contessa)
  if(qgSiLCvryR.count(Character.contessa)==3):
   qgSiLCvrQI.remove(Character.assassin)
   qgSiLCvrQI.insert(0,Character.assassin)
  for qgSiLCvrQN in qgSiLCvrQI:
   if(qgSiLCvrQN in characters):
    qgSiLCvrQo.append(qgSiLCvrQN)
    if(characters.count(qgSiLCvrQN)>1):
     qgSiLCvrQO.extend([qgSiLCvrQN]*(characters.count(qgSiLCvrQN)-1))
  for qgSiLCvrQN in qgSiLCvrQI:
   if(qgSiLCvrQN in qgSiLCvrQO):
    qgSiLCvrQo.extend([qgSiLCvrQN]*qgSiLCvrQO.count(qgSiLCvrQN))
  return qgSiLCvrQo
 def toRead3(qgSiLCvryK):
  qgSiLCvrQH=[x for x in qgSiLCvryK.states if x.identifier!=qgSiLCvryK.identifier and len(x.flipped)<2]
  qgSiLCvrQH=sorted(qgSiLCvrQH,key=attrgetter('coins'),reverse=True)
  qgSiLCvrQH=sorted(qgSiLCvrQH,key=lambda x:len(x.flipped))
  return qgSiLCvrQH
 def myCode3(qgSiLCvryK,opponents):
  qgSiLCvrQH=[x for x in opponents if x.identifier!=qgSiLCvryK.identifier and len(x.flipped)<2]
  qgSiLCvrQH=sorted(qgSiLCvrQH,key=attrgetter('coins'),reverse=True)
  qgSiLCvrQH=sorted(qgSiLCvrQH,key=lambda x:len(x.flipped))
  return qgSiLCvrQH
def make_bot(qgSiLCvryc):
 return jerks2(qgSiLCvryc)