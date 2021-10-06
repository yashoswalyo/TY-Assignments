from io import TextIOWrapper

MOT={
	'STOP':('00','IS',0),
	'ADD':('01','IS',2),
	'SUB':('02','IS',2),
	'MUL':('03','IS',2),
	'MOVER':('04','IS',2),
	'MOVEM':('05','IS',2),
	'COMP':('06','IS',2),
	'BC':('07','IS',1),
	'DIV':('08','IS',2),
	'READ':('09','IS',1),
	'#print':('10','IS',1),
	'DEC':('11','IS',1),
	'START':('01','AD',1),
	'END':('AD',0),
	'ORIGIN':('03','AD',1),
	'EQU':('04','AD',2),
	'LTORG':('05','AD',0),
	'DS':('01','DL',1),
	'DC':('02','DL',1)
}

REG={
	'AREG':1,
	'BREG':2,
	'CREG':3,
	'DREG':4
}

class files(object):
	ifp=open("tables/inter_code.txt",mode="r")
	lit=open("tables/literal_table.txt","r")
	litline = lit.read().splitlines()
	sym=open("tables/symbol_table.txt","r")
	symline = sym.read().splitlines()
	output=open("tables/output.txt","a+")
	output.truncate(0)

def getInst(s:str):
	i = s.removeprefix('(').removesuffix(')').split(sep=',')[-1]
	return "("+i+")\t"

def getS(s:str):
	a = s.split(sep=',')[-1]
	a = files.symline[int(a)].split(sep='\t')[-1]
	return a

def getL(s:str):
	a = s.split(sep=',')[-1]
	a = files.litline[int(a)-1].split(sep='\t')[-1]
	return a

def getC(s:str):
	a = s.split(sep=',')[-1]
	if len(a)<3:
		if len(a)<2:
			a = " (00"+a+")"
		else:
			a = " (0"+a+")"
	return a

def getRest(s:str):
	a='(000)'
	s=s.replace(')(',' ').removeprefix('(').removesuffix(')').split()
	if 'RG' in s[0]:
		a = "(00"+s[0].split(',')[-1]+")"
	elif 'DL' in s[0]:
		a = "(000)"
	elif 'S' in s[0]:
			a = "("+getS(s[0])+")"
	else:
		a = s[0].split(',')[-1]
		if len(a)<3:
			if len(a)<2:
				a = "(00"+a+")"
			else:
				a = "(0"+a+")"
		else :
			a = "("+a+")"
	if len(s) > 1:
		if 'S' in s[1]:
			a += " ("+getS(s[1])+")"
		if 'L' in s[1]:
			a += " ("+getL(s[1])+")"
		if 'C' in s[1]:
			a += getC(s[1])
	return a

def pass_two(intermediateCode: TextIOWrapper):
	objctCode=''
	i=''
	r=''
	l=0
	for line in intermediateCode:
		l+=1
		if "(AD,01)" in line or "(AD,02)" in line:
			pass
		elif "DL" in line.split()[1]:
			pass
		else:
			words = line.split()
			#print(words)
			i=getInst(words[1])
			r=getRest(words[2])
			print(words[0]+"\t"+i+r)
			#print("Line: "+str(l)+" "+i+r)
			#print("Line: "+str(l)+" "+i+r)
			
	return

pass_two(intermediateCode=files.ifp)