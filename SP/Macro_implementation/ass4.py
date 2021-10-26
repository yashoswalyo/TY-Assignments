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
#Function To Process Macro Prototype
def prototype_processing(prototype,MDTP,KPDTP):
	KP = 0 #Number Of Keyword Parameter
	PP = 0 #Number Of Positional Parameter
	i=0
	macroName = prototype[0]
	pwords = [x.upper() for x in prototype]
	for i in range(len(pwords)):
	#Positional Parameters
		if pwords[i].startswith('&') and not pwords[i].__contains__('='):
			parameter = pwords[i]
			temp[parameter] = list()
			temp[parameter].append('(P,' + str(i) + ')')
			PP += 1
			PNTAB.write(str(pwords[i])+'\n')
	#Keyword and Default Parameters
		if pwords[i].startswith('&') and pwords[i].__contains__('='):
			twords = re.split('=', pwords[i])
			key_parameter = twords[0]
			temp[key_parameter] = list()
			temp[key_parameter].append('(P,' + str(i) + ')')
			if len(twords) == 2 and twords[1] != '':
				KPDTAB.write(str(KPDTP) + ' ' + str(twords[0]) + ' ' +str(words[1]))
				KPDTP += KP
				KP += 1
				PNTAB.write(str(twords[0]) + '\n')
			else:
				KP += 1
				PNTAB.write(str(twords[0]) + '\n')
	MNT.write(str(prototype[0]) + '\t' + str(PP) + '\t' + str(KP) + ' \t' +str(MDTP) + ' \t' + str(KPDTP) + ' \n')
	prototype_done = True
#Function To Process MDT
def process_MDT(words):
	global MDTP
	for i in words.split():
		if i == 'MACRO' or i == 'MEND':
			continue
		else:
			if i.__contains__('&') and not i.__contains__('='):
				var = i.split(',')
				char = temp[var[0]]
				MDT.write(char[0] + ' ')
			else:
				MDT.write(i + ' ')
	MDTP += 1
	MDT.write('\n')
#Calculate MNT, PP, KP, KPDTP
i=0
while i < len(lines):
	words = re.split(r'[\s,]+', lines[i])
	words.pop()
	for j in range(len(words)):
		word = words[j]
		if word == 'MACRO':
	#print(words)
			prototype = re.split(r'[\s,]+', lines[i + 1])
			prototype_processing(prototype, MDTP, KPDTP)
	process_MDT(lines[i])
	i += 1
