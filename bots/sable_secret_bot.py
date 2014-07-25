import random
from interface import *
class Niswanob1(Bot):
 def __init__(self,identifier):
  self.identifier=identifier
  self.fuscat1=[]
  self.Chri1={0: 0,1: 0,2: 0,3: 0,4: 0,5: 0}
  self.Chri2={0: 0,1: 0,2: 0,3: 0,4: 0,5: 0}
  self.Niswanob2={0: 0,1: 0,2: 0,3: 0,4: 0,5: 0}
  self.fuscat2=0
  self.bitboostdotcom1=False
  self.Chri4=self.Chri1
  self.fuscat3={0: 1,1: 4,2: 6,3: 3,4: 3}
  self.bitboostdotcom2={0: 0,1: 0,2: 0,3: 0,4: 0,5: 0}
  self.ordemo1=False
  self.bitboostdotcom3=0
  self.Chri3=True
 def update_state(self,fuscat5,ordemo3):
  self.fuscat5=fuscat5
  self.ordemo3=ordemo3
  self.Chri4=self.Niswanob2
  bitboostdotcom4=[bitboostdotcom5.identifier for 
bitboostdotcom5 in       self.fuscat5 if   (len(bitboostdotcom5.flipped)<2) ]
  if (len(bitboostdotcom4)<=1):
   self.Chri1[bitboostdotcom4[0]]+=1
   self.fuscat1=[]
   if (self.bitboostdotcom1==False):
    self.Chri1[0]+=1
    self.bitboostdotcom1=True
 def start(self):
  self.fuscat2+=1
  self.bitboostdotcom1=False
  self.ordemo2={0: [],1: [],2: [],3: [],4: [],5: []}
  self.Niswanob4=0
 def Chri5(self):
  bitboostdotcom6=[]
  for Niswanob3 in self.fuscat5:
   bitboostdotcom6+=Niswanob3.flipped
  bitboostdotcom6+=self.ordemo3
  bitboostdotcom6+=self.fuscat1
  return bitboostdotcom6
 def fuscat6(self,Chri6):
  Chri6.sort(key=(lambda bitboostdotcom8: bitboostdotcom8.coins),reverse=True)
  Chri6.sort(key=(lambda fuscat4: len(fuscat4.flipped)))
  Chri6.sort(key=(lambda bitboostdotcom9: self.Chri1[bitboostdotcom9.identifier]),reverse=True)
  return Chri6
 def take_action(self):
  Niswanob5=self.Chri5()
  Niswanob7=[]
  for fuscat8 in self.fuscat5:
   Niswanob7+=fuscat8.flipped
  Chri6=[fuscat8 for fuscat8 in       self.fuscat5 if 
((len(fuscat8.flipped)<2) and (fuscat8.identifier!=self.identifier)) ]
  fuscat7=self.fuscat6(Chri6)
  bitboostdotcomA=fuscat7[0].identifier
  if (len(Chri6)==2):
   Chri6.sort(key=(lambda Niswanob6: Niswanob6.coins),reverse=True)
   Chri6.sort(key=(lambda bitboostdotcomB: len(bitboostdotcomB.flipped)))
   bitboostdotcomA=Chri6[0].identifier
  elif (len(Chri6)==1):
   pass
  Niswanob8=self.fuscat5[self.identifier].coins
  bitboostdotcomC=None
  ordemo4=None
  for ordemo6 in fuscat7[1:]:
   bitboostdotcomD=ordemo6.identifier
   if ((bitboostdotcomC==None) and (Character.assassin	in	self.ordemo2[bitboostdotcomD])):
    bitboostdotcomC=bitboostdotcomD
   if ((ordemo4==None) and (Character.ambassador	in	self.ordemo2[bitboostdotcomD]) and (Character.captain	in	self.ordemo2[bitboostdotcomD])):
    ordemo4=bitboostdotcomD
  self.Chri4=self.Chri2
  if (Niswanob8>=7):
   return TargetedAction(Action.coup,bitboostdotcomA)
  elif ((Character.assassin	in	self.ordemo3) and (Niswanob8>=3) and ((Niswanob5.count(Character.contessa)==3) or (Character.contessa	in	self.ordemo2[bitboostdotcomA]))):
   return TargetedAction(Action.assassinate,bitboostdotcomA)
  elif ((Character.captain	in	self.ordemo3) and (self.fuscat5[bitboostdotcomA].coins>=1) and ((6==(Niswanob5.count(Character.captain) + Niswanob5.count(Character.ambassador))) or ((Character.captain	in	self.ordemo2[bitboostdotcomA]) and (Character.ambassador	in	self.ordemo2[bitboostdotcomA])))):
   return TargetedAction(Action.extort,bitboostdotcomA)
  elif (self.Chri3 and (Niswanob7.count(Character.duke)<=1)):
   self.Niswanob4+=1
   return Action.tax
  elif ((Character.ambassador	in	self.ordemo3) and (len(self.fuscat1)==0)):
   return Action.exchange
  elif (Character.duke	in	self.ordemo3):
   return Action.tax
  elif ((bitboostdotcomC!=None) and (Character.assassin	in	self.ordemo3) and (Niswanob8>=3)):
   return TargetedAction(Action.assassinate,bitboostdotcomC)
  elif ((ordemo4!=None) and (Character.captain	in	self.ordemo3)):
   return TargetedAction(Action.extort,ordemo4)
  elif (Niswanob5.count(Character.duke)==3):
   return Action.foreign_aid
  else:
   return Action.income
  return Action.income
 def notify_action(self,bitboostdotcomF,Chri7,NiswanobA,Chri8):
  self.fuscat3[0]=(self.fuscat3[1]*    2)
  if ((NiswanobA==self.identifier) and (Chri7==Action.coup)):
   self.bitboostdotcom2[bitboostdotcomF]+=1
  if (bitboostdotcomF==self.identifier):
   return 
  if ((Chri7==Action.exchange) and (Chri8==True)):
   self.ordemo2[bitboostdotcomF]=[]
   self.fuscat1=[]
  if ((NiswanobA!=None) and (self.Niswanob2[NiswanobA]==0)):
   if ((Chri7==Action.assassinate) and (Chri8==True)):
    self.ordemo2[NiswanobA].append(Character.contessa)
   if ((Chri7==Action.extort) and (Chri8==True)):
    self.ordemo2[NiswanobA].append(Character.captain)
    self.ordemo2[NiswanobA].append(Character.ambassador)
  if ((Chri7==Action.foreign_aid) and (Chri8==True)):
   for fuscat9 in range(5):
    if (self.Niswanob2[fuscat9]==0):
     self.ordemo2[fuscat9].append(Character.duke)
  self.fuscat3[0]=(self.fuscat3[0]*    4)
 def notify_challenge(self,bitboostdotcomE,fuscatB,ordemo5,ordemo7,Chri9,fuscatA):
  if (fuscatB==self.identifier):
   pass
  if (ordemo7==fuscatA):
   self.fuscat1=[]
  if (Chri9==None):
   pass
  if (fuscatA	in	self.ordemo2[fuscatB]):
   self.Niswanob2[fuscatB]=1
   self.ordemo2[fuscatB]=[]
 def block_action(self,Niswanob9,ordemo8,bitboostdotcom10,fuscatC):
  NiswanobB=self.Chri5()
  if ((len(self.ordemo3)>0) and ordemo8.blockable(self.ordemo3[0])):
   return self.ordemo3[0]
  if ((len(self.ordemo3)>1) and ordemo8.blockable(self.ordemo3[1])):
   return self.ordemo3[1]
  if ((ordemo8==Action.assassinate) and (NiswanobB.count(Character.contessa)!=3)):
   return Character.contessa
  return None
 def ChriA(self):
  ordemo9=5
  for ChriB in self.fuscat5:
   if (len(ChriB.flipped)>=2):
    ordemo9-=1
  self.Chri2[ordemo9]+=1
  self.bitboostdotcom1=True
 def flip(self):
  if (len(self.ordemo3)==1):
   self.ChriA()
  ChriC=self.NiswanobD(self.ordemo3)
  return ChriC[(-1)]
 def exchange(self,fuscatD):
  fuscatE=self.NiswanobD((list(self.ordemo3) + list(fuscatD)))
  if (len(self.ordemo3)==1):
   self.fuscat1=fuscatE[1:]
  else:
   self.fuscat1=fuscatE[2:]
  return fuscatE[:2]
 def reveal(self,bitboostdotcom12,bitboostdotcom11,NiswanobC,ChriD):
  if (NiswanobC	in	self.ordemo3):
   return NiswanobC
  elif (NiswanobC==Character.duke):
   if (self.Niswanob4==1):
    self.bitboostdotcom3+=1
    if (self.fuscat2>10):
     if (self.bitboostdotcom3>(self.fuscat2 / 2)):
      self.Chri3=False
  return self.flip()
 def challenge(self,NiswanobE,ChriF,ordemoA,NiswanobF):
  ChriE=self.Chri5()
  if (ChriE.count(ordemoA)==3):
   return True
  if ((ordemoA	in	self.ordemo2[NiswanobE]) and (self.Niswanob2[NiswanobE]==0)):
   return True
  if ((NiswanobF==self.identifier) and (ChriF==Action.assassinate) and (Character.contessa	not in	self.ordemo3) and (len(self.ordemo3)==1)):
   return True
  return False
 def NiswanobD(self,bitboostdotcom13):
  Niswanob10=[]
  Chri10=[]
  Niswanob12=[fuscat10 for fuscat10 in       self.fuscat5 if 
((len(fuscat10.flipped)<2) and (fuscat10.identifier!=self.identifier)) ]
  ordemoB=[Character.contessa,Character.ambassador,Character.captain,Character.assassin,Character.duke]
  ordemoC=self.Chri5()
  if (ordemoC.count(Character.assassin)==3):
   ordemoB.remove(Character.contessa)
   ordemoB.append(Character.contessa)
  if (ordemoC.count(Character.contessa)==3):
   ordemoB.remove(Character.assassin)
   ordemoB.insert(0,Character.assassin)
  for StopLookingJerk in ordemoB:
   if (StopLookingJerk	in	bitboostdotcom13):
    Niswanob10.append(StopLookingJerk)
    if (bitboostdotcom13.count(StopLookingJerk)>1):
     Chri10.extend(([StopLookingJerk]*    (bitboostdotcom13.count(StopLookingJerk) - 1)))
  for StopLookingJerk in ordemoB:
   if (StopLookingJerk	in	Chri10):
    Niswanob10.extend(([StopLookingJerk]*    Chri10.count(StopLookingJerk)))
  return Niswanob10
def make_bot(identifier):
 return Niswanob1(identifier)