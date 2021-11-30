import pandas as pd
import numpy as np
import re
from tabulate import tabulate

MNT = pd.read_csv("MNT.csv")

MDT = pd.read_csv("MDT.csv")
mdt = list(MDT["MDT TABLE"])
MacroName = list(MNT.MacroName)
MDTP = list(MNT.MDTP)
mdtp=[]
PP = list(MNT.PP)
KP = list(MNT.KP)


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
    


def preprocess(mdt2):
    mdt_new=[]  #a preprocessed mdt
    for i in mdt2:
        i=i.strip()
        if "MEND" in i:
            break
        elif "LCL" in i or "SET" in i or "AIF" in i or "MEND" in i:
            pass
        else:
            mdt_new.append(i)
   
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
	#'''Get Actual Parameters'''
    #split params
    flag =  " "
    count=0
    x = call.split(" ")[1]
    ap.append(x.split(","))
    for i in range(len(ap)):
        for j in range(len(ap[i])):
            if "=" in str(ap[i][j]):
                count+=1
                ap[i][j] = ap[i][j].split("=")[1]
    kp_declared.append(count)
    for i in range(len(total_kp)):
        if kp_declared[i] < total_kp[i]:
            flag = i
            if kpdtp[found] !='-':
                while len(ap[int(flag)])<total_param[flag]:
                    ap[int(flag)].append(kpdtab_value[int(kpdtp[found])-1])
            
    return ap
  
               
      

for i in range(len(calls)):
    macro_call = calls[i].split(" ")[0]
    if macro_call not in MacroName:
        print("Macro ",macro_call, " not found")
        pass
    else:
        found = MacroName.index(macro_call)
        mdtp.append(MDTP[found])
        total_param.append(PP[found]+KP[found])
        total_kp.append(KP[found])
        getAcParams(calls[i])
        

mdtp.append(len(mdt))  
#mdtp = [15,18]
for i in range(len(calls)):
    mdt_new.append(preprocess(mdt[int(mdtp[i])-1:]))



print("APTAB")
for i in ap:
    print(tabulate(pd.DataFrame(i,columns = ["ActualParameter"]),headers="keys",tablefmt="grid"))
    print("\n")

print("*EXPANDED CODE*\n")
for i in range(len(ap)):
    final.append((expand(mdt_new[i],ap[i])))
    final[i] = "\n".join(final[i])

for i in final:
    print(i)

