import pandas as pd
import numpy as np
import re
from tabulate import tabulate
	
with open('macos.asm') as f:
	lines = [line.rstrip() for line in f]

MNT = pd.DataFrame( columns=['MacroName', 'PP' ,'KP' ,'EV', "MDTP", 'KPT', 'SSTP'])
for i in range(0,len(lines)):
	if lines[i] == 'MACRO':
		MNT.loc[len(MNT.index)] = ["-","-","-","-","-","-","-"] 
	  

EV = pd.DataFrame(columns = ['EVNAME'])


KPDTAB = pd.DataFrame(columns=['KeywordParameter','Value'])
kpdlist = []

PNTAB = pd.DataFrame(columns=['ParameterName'])

SSNTAB = pd.DataFrame(columns=['SSName'])

APTAB = pd.DataFrame(columns=['ActualParameterName'])

def count(s, c) :
	res = 0
	for i in range(len(s)) :
		if (s[i] == c):
			res = res + 1
	return res



mpos = 0
pnlist = []
name_at_line=[]
for i in range(0,len(lines)):
	
	if lines[i].startswith('.'):
		li = list(lines[i].split(" "))
		SSNTAB = SSNTAB.append({'SSName': li[0].replace('.','') } , ignore_index=True)
		

	if lines[i] == 'MACRO':
		name_at_line.append(i+2)
		x = re.split("\s", lines[i+1], 1)
		MNT.MacroName[mpos] = x[0]   #Macroname

		cc = count(x[1],'=')
		li = list(x[1].split(","))
		for j in li:		# KPDATB , MNT KPT
			j = j.replace('&',"")
	
			
			if '=' in j:
				kval = j.split('=')
				KPDTAB = KPDTAB.append( { 'KeywordParameter': kval[0]  ,'Value': kval[1] },ignore_index=True)
				MNT.KPT[mpos] = int(KPDTAB[KPDTAB['KeywordParameter']==kval[0]].index.values) - cc + 2


			j = j.split('=',1)   
			PNTAB = PNTAB.append( {'ParameterName': j[0] }, ignore_index=True  )
			# PNTAB

		MNT.PP[mpos]= x[1].count('&') # PP
		MNT.PP[mpos] = int(MNT.PP[mpos]) - int( x[1].count('=') )

		MNT.KP[mpos] = x[1].count('=') # KP
		
		mpos = mpos + 1


MainCode = lines[lines.index('MEND')+1:]
MainCode = MainCode[MainCode.index('MEND')+1:]

count = 0
for i in range(len(MainCode)):
	mc = MainCode[i].split(' ')
	if mc[0] in MNT.values:
		mc.pop(0)
		for i in mc:
			if type(i) == str:
				APTAB = APTAB.append( {'ActualParameterName': i } , ignore_index=True)


mev = 0
mevc = 0
msstp = 0
msstpc = 0
for i in range(0,len(lines)):
	if 'LCL' in lines[i]:
		mevc = mevc + 1
		x = re.split("\s", lines[i], 1)
		EV.loc[len(EV.index)] =  x[1].replace('&','')
		EV
	MNT.EV[mev] = mevc 
	if lines[i] == 'MEND':  
		mev = mev +1 
		mevc = 0

	if lines[i].startswith('.'):
		msstpc = msstpc + 1
	MNT.SSTP[msstp] = msstpc 
	if lines[i] == 'MEND':  
		msstp = msstp +1 
		msstpc = 0

MNT = MNT.rename({'KPT': 'KPDTP'}, axis='columns')

#MDT Table

MDT = pd.DataFrame()
SSTAB = pd.DataFrame()

temp = lines[-1]



pnlistfull = PNTAB["ParameterName"].tolist()
pnlistsep = []
pnsplitcount = []

# print(pnlistfull)
for i in range(len(MNT)):
	pnsplitcount.append( int(MNT.PP[i]) + int(MNT.KP[i]) )

for i in range(len(pnsplitcount)):
	pnlistsep.append( pnlistfull[:pnsplitcount[i]] )
	pnlistfull = pnlistfull[pnsplitcount[i]:]

# print(pnsplitcount)
# print(pnlistsep)
# PN tabs 
for i in range(len(pnsplitcount)):
	PNTABSEP = pd.DataFrame(pnlistsep[i] , columns=["ParameterName"]  )
	print(f'PNTAB FOR {MNT.MacroName[i]} MACRO' )
	print(tabulate(PNTABSEP, headers="keys",tablefmt="grid"),"\n")
	PNTAB_df = PNTABSEP.to_csv(f"{MNT.MacroName[i]}.csv", index=True)



macroc = 0
mendc = 0
for i in range(len(lines)):

	if 'MACRO' == lines[i]:
		macroc = macroc + 1
	if 'MEND' == lines[i]:
		mendc = mendc + 1



mdrlines = lines[:-1]


for i in range(len(mdrlines)):
	if '&' or ',' in mdrlines[i]:
		mdrlines[i] = mdrlines[i].replace('&', " ")

	if 'MACRO' in mdrlines[i]:
		mdrlines[i] = ''
		mdrlines[i+1] = ''
	

while("" in mdrlines) :
	mdrlines.remove("")


ssval = []

# MDT Processing main
for i in range(len(mdrlines)):
	mc = mdrlines[i].split(' ')
	# for parameters in MDT
	for j in range(len(mc)):
		for subarray in pnlistsep:
			if mc[j].replace(',','') in subarray:
				#print(pnlistsep.index(subarray), '-', subarray.index(mc[j].replace(',','')))
				mc[j] = f'(P,{subarray.index(mc[j].replace(",",""))})'


   
		if mc[j] in EV.values:
			mc[j] = f'(E,{EV[EV["EVNAME"]== mc[j] ].index.values + 1 })'

		if mc[j].startswith('.'):
			ssval.append(i + 1)


		if mc[j].replace('.','') in SSNTAB.values :
			mc[j] = ''

		if mc[-1].replace('.','') in SSNTAB.values:
			mc[-1] = f'(S,{SSNTAB[SSNTAB["SSName"]== mc[-1].replace(".","") ].index.values + 1 })'
		

	mc = " ".join(mc)
	mc = mc.replace('[','')
	mc = mc.replace(']','')
	mdrlines[i] = mc

mdrlines.append("MEND")
SSTAB['SSTAB'] = ssval
MDT['MDT TABLE'] = mdrlines


for i in range(len(MNT)):
	if i ==0:
			MNT.MDTP[0] = 1
			continue 
	
	MNT.MDTP[i] = (MDT[MDT["MDT TABLE"]== 'MEND' ].index.values[i-1] + 2)



print("Error checking ")
if macroc == mendc:
	print( macroc ," properly defined Macro(s)")
	
mn = list(MNT.MacroName)

dupes = [x for n, x in enumerate(mn) if x in mn[:n]]

#index at which error was found
flag =1
for i in range(len(dupes)):
	found = mn.index(dupes[i])
	print("DUPLICATE MACRO-NAME DEFINITION: ",dupes[i]," at line ", name_at_line[found],"\n\n")

MDT.index += 1
EV.index += 1
KPDTAB.index += 1


print("MNT TABLE")
print(tabulate(MNT, headers="keys",tablefmt="grid"))
print("EVN TABLE")
print(tabulate(EV, headers="keys",tablefmt="grid"))
print("\nKPDTAB TABLE")
print(tabulate(KPDTAB, headers="keys",tablefmt="grid"))
print("\nSSNTAB TABLE")
print(tabulate(SSNTAB, headers="keys",tablefmt="grid"))
print("\nMDT TABLE")
print(tabulate(MDT, headers="keys",tablefmt="grid"))
print("\n SSTAB")
print(tabulate(SSTAB, headers="keys",tablefmt="grid"))

MNT_df = MNT.to_csv('MNT.csv',index=True)
KPDTAB_df = KPDTAB.to_csv('KPDTAB.csv',index=True)
MDT_df = MDT.to_csv('MDT.csv',index=True)
