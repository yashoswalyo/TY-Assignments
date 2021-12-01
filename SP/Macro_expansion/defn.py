import pandas as pd
import numpy as np
import re
from tabulate import tabulate

MNT = pd.read_csv("MNT.csv")
MDT = pd.read_csv("MDT.csv")

mdt = list(MDT["MDT TABLE"]) #=> 
MacroName = list(MNT.MacroName) #=> CLRMEM,DOMATH,DESCOR

MDTP = list(MNT.MDTP) #=> 1,8,15
mdtp=[]

PP = list(MNT.PP) #positional param -> 2,2,2
KP = list(MNT.KP)	#keyword param -> 1,2,0

KPDTAB = pd.read_csv('KPDTAB.csv')
kpdtab_value = list(KPDTAB.Value)
ap=[]
total_param=[]
kp_declared = []

kpdtp = list(MNT.KPDTP)
x=[]
mdt_new=[]
final=[]
total_kp=[]
with open("calls.asm") as f:
		calls = [call.rstrip() for call in f]
		print(calls)
	


def preprocess(mdt2): #=> 'MOVER BREG (P,0)'
	mdt_new=[]  #a preprocessed mdt
	for i in mdt2: #=> i=['MOVER' 'BREG' '(P,0)']
		i=i.strip()
		if "MEND" in i:
			break
		elif "LCL" in i or "SET" in i or "AIF" in i or "MEND" in i:
			pass
		else:
			mdt_new.append(i)  #=> ['MOVER','BREG','(P,0)']
   
	return mdt_new # we get separated mdts
	
	

def expand(mdt_new,ap2):
	expanded = []
	
	for i in range(len(mdt_new)):
		token = mdt_new[i].split(" ")
		
		for p in range(len(token)):
			if token[p].startswith('('):
				index = token[p].strip('()').split(',')
				if(index[0].lower()=='p'):
					
					token[p] = ap2[int(index[1])]
		expanded.append(' '.join(token))
	return expanded
	
def getAcParams(call):
	'''Get Actual Parameters'''
	#split params
	flag =  " "
	count=0
	x = call.split(" ")[1] #-> ['A,10,&REG=DREG']
	ap.append(x.split(",")) #-> ap = ['15','30','A',10','&REG=DREG']
	for i in range(len(ap)): #-> 4 TO 5
		for j in range(len(ap[i])):  #-> 4 TO 9
			if "=" in str(ap[i][j]): #-> ap[4][4]= '&REG=DREG'
				count+=1
				ap[i][j] = ap[i][j].split("=")[1] 

	kp_declared.append(count) #->[0,1]
	for i in range(len(total_kp)): # 0 TO 2
		if kp_declared[i] < total_kp[i]:  #0<0, 1<1
			flag = i
			if kpdtp[found] !='-':
				while len(ap[int(flag)])<total_param[flag]:
					ap[int(flag)].append(kpdtab_value[int(kpdtp[found])-1])
			
	return ap
	
			   
	

for i in range(len(calls)):
	#i=0 , len(calls)=5
	#i=1 , len(calls)=5
	macro_call = calls[i].split(" ")[0] #-> CLRMEM
	if macro_call not in MacroName:
		print("Macro ",macro_call, " not found")
		pass
	else:
		found = MacroName.index(macro_call) #-> 2 , 0
		mdtp.append(MDTP[found])  #-> [15,1,1,8,15]
		total_param.append(PP[found]+KP[found]) #-> [2,3]
		total_kp.append(KP[found]) #-> [0,1]
		getAcParams(calls[i])
		

mdtp.append(len(mdt))   # LEN=18
#mdtp = [15,1,1,8,15,18]
for i in range(len(calls)): #=> 4 TO 5
	mdt_new.append(preprocess(mdt[int(mdtp[i])-1:])) #=> []



print("APTAB")
for i in ap:
	print(tabulate(pd.DataFrame(i,columns = ["ActualParameter"]),headers="keys",tablefmt="grid")) # IDK
	print("\n")

print("*EXPANDED CODE*\n")
for i in range(len(ap)):
	final.append((expand(mdt_new[i],ap[i])))
	final[i] = "\n".join(final[i])

for i in final:
	print(i)

