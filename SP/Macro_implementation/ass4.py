import re

def prototype_processing(prototype,MDTP,KPDTP):
	KP = 0
	PP = 0
	i = 0
	pwords = [x.upper() for x in prototype ]
	for i in range(len(pwords)):
		s=1
		if pwords[i].startswith('&') and not pwords[i].__contains__('=') :
			parameter = pwords[i]
			temp[parameter] = list()
			temp[parameter].append(f"(P,{str(i)})")
			PP+=1
			PNTAB.write(f"{str(pwords[i])}\n")
		
		if pwords[i].startswith('&') and pwords[i].__contains__("="):
			twords = pwords[i].split("=")
			k_parameter = twords[0]
			temp[k_parameter] = list()
			temp[k_parameter].append(f"(P,{str(i)})")
			if len(twords) == 2 and twords[1] != '':
				KPDTAB.write(f"{str(KPDTP)} {str(twords[0])} {str(words[0])}")
				KPDTP += KP
				KP += 1
				PNTAB.write(f"{str(twords[0])} \n")
			else:
				KP += 1
				PNTAB.write(f"{str(twords[0])} \n")
	MNT.write(f"{str(prototype[0])}\t{str(PP)}\t{str(KP)} \t{str(MDTP)} \t{str(KPDTP)}\n")


def process_MDT(words):
	global MDTP
	for i in words.split():
		if i == 'MACRO' or i == 'MEND':
			continue
		else:
			if i.__contains__('&') and not i.__contains__('='):
				var = i.split(',')
				char = temp[var[0]]
				MDT.write(f"{char[0]} ")
			else:
				MDT.write(f"{i} ")
	MDTP+=1
	MDT.write('\n')
#pointers
##ass4 file hehe
import re
import os
#Global Pointers
MDTP = 0 #Macro Definition Table Pointer
KPDTP = 0 #Keyword Parameter Default Table Pointer
#Open Maro Input File
macro = open('input.txt','r')
#Macro Name Table
MNT = open('MNT.txt','a+')
MNT.truncate(0)
#Macro Definition Table
MDT = open('MDT.txt','a+')
MDT.truncate(0)
#Keyword Parameter Default Table
KPDTAB = open('KPDTAB.txt','a+')
KPDTAB.truncate(0)
#Parameter Name Table
PNTAB = open('PNTAB.txt','a+')
PNTAB.truncate(0)
lines = macro.readlines()
#Temporary MDT
mdt = []
temp = {}
macroName = []

i=0
while i < len(lines):
	words = re.split(r'[\s,]+', lines[i])
	words.pop()
	for j in range(len(words)):
		word = words[j]
		if word == 'MACRO':
			# print(words)
			prototype = re.split(r'[\s,]+', lines[i + 1])
			prototype_processing(prototype, MDTP, KPDTP)
	process_MDT(lines[i])
	i += 1
