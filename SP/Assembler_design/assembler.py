from io import open_code
import os
import sys
# import iChecker

MOT={
'PRINT':['01',1],
'STOP':['02',1],
'ADD':['03',1],
'SUB':['04',1],
'MUL':['05',1],
'MOVER':['06',1],
'MOVEM':['07',1],
'DEC':['08',1],
'DIV':['09',1],
'READ':['0A',1],
'END':['0B',-1],
'START':['0C',-1],
'ORIGIN':['0D'],   #address of next ins
'LTORG':['0F'],    #Assigns address to literals
'DS':['10'],
'DC':['11'],
'AREG':['12'],
'BREG':['13'],
'CREG':['14'],
'MREG':['15'],
'JZ':['16'],
'JNZ':['17'],
'JC':['18'],
'JNC':['19']
}

def isComment(line):
	if line.find("//")!=-1:
		return True
	return False

def isStart(line):
	l = str(line)
	l = l.split()
	if "START" in l:
		return True
	return False

def getStart(line):
	l = str(line)
	tokens = l.split()
	if "START" in tokens and len(tokens)==2:
		return tokens[1]
	elif "START" in tokens and len(tokens)!=2:
		return 0
	else:
		return False
	
def isEnd(line):
	l=str(line)
	token=l.split()
	if "END" in token:
		return True
	return False

def getLabel(line):
	l=str(line)
	label = False
	l = l.split()
	if hasLabel(line):
		return hasSymbol(line)
	else:
		return False

def hasLabel(line):
	if line.find(":")!=1:
		return True
	else:
		return False


def RepresentsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def hasSymbol(line):
	l=str(line)
	l=l.split()
	symbol = False
	for i in l:
		if i not in list(MOT.keys()) and not (RepresentsInt(i)):
			symbol=i
		break
	return symbol

def delAllFiles():
	os.remove("temp.txt")
	os.remove("label_table.txt")
	os.remove("tables/symbol_table.txt")
	os.remove("output.txt")

def hasVariable(line):
	l = str(line)
	tokens = l.split()
	if "DW" in tokens:
		return True
	else:
		return False


def getVariable(line):
	l = str(line)
	tokens = l.split()
	if hasVariable(line):
		return [tokens[0],tokens[2]]
	else:
		return False	


def getOpcode(line):
	l = str(line)
	temp = l.split()
	Opcode = None
	nOpcode = 0
	if ":" in temp:
		if temp[0] not in MOT and "DC" not in temp:
			print("[Error] Invalid OPCODE Used" , end =' ')
			return -2
		elif temp[2] not in MOT:
			print("[Error] Invalid OPCODE Used" , end =' ')
			return -2
	for i in temp:
		if i in MOT and nOpcode<0:
			Opcode = i
			nOpcode += 1
	if nOpcode>1:
		raise Exception("One of the Lines contains multiple OPCODES...")
	else:
		return Opcode

def getOperand(line):
	l = str(line)
	temp = l.split()
	opc = 0
	error_flag=False
	if ":" not in temp:
		opc = temp[0]
		if len(temp)>4:
			error_flag = True
	else:
		opc = temp[2]
		if len(temp)>4:
			error_flag = True
	if "DC" in temp:
		opc = temp[1]
	if error_flag:
		print("[Error] OPCODE "+str(temp[0]) +" Supplied with too many arguments thab required at Line" , end =' ')
		return -2
	if MOT[opc][1] == 1 and temp[-1] in MOT:
		print("[Error] OPCODE "+str(temp[-1]) +" Supplied with fewer arguments thab required at Line" , end =' ')
		return -2
	if temp[-1] not in MOT:
		return temp[-1]
	else:
		return False

def pass_one(alp):
	LC=0
	length = 20
	value = 0
	type = 'none'
	f1 = open('tables/symbol_table.txt','a+')
	f2 = open(file='tables/literal_table.txt',mode='a+')
	f3 = open(file='tables/temp.txt',mode='a+')
	f4 = open(file='tables/label_table.txt',mode='a+')
	label_table={}
	symbol_table={}
	end_flag = True
	start_flag = True
	tok = 0
	line_no=0
	print("Initializing Part 1 assembler")
	for line in alp:
		print(line_no)
		line.strip()
		k = line.split()
		if not(isComment(line)):
			line_no+=1
			label = 0
			symbol = 0
			tok = getStart(line)
			if isEnd(line):
				end_flag=False
				break
			if tok != False:
				LC = int(tok)
			if isStart(line):
				start_flag=False
				continue
			if getLabel(line) != False:
				label = getLabel(line)
				if getLabel(line) in label_table:
					print("[ERROR] multiple labels "+str(getLabel(line))+"at line "+str(line_no))
					# sys.exit(1)
					# delAllFiles()
				if getLabel(line) not in label_table:
					label_table[getLabel(line)]=LC
					f4.writelines(getLabel(line)+" "+str(LC)+"\n")
					print(getLabel(line)+" "+str(LC)+"\n")
			if hasSymbol(line) != False:
				symbol = hasSymbol(line)
				if hasSymbol(line) not in symbol_table:
					symbol_table[hasSymbol(line)]=LC
					f1.writelines(hasSymbol(line)+" "+str(LC)+"\n")
					print(getLabel(line)+" "+str(LC)+"\n")
			if getVariable(line) != False:
				var = getVariable(line)
				if var[0] in label_table:
					print("[Error] Multiple Declaration of Variable "+var[0]+" at line "+str(line_no))
					sys.exit(-1)
					delAllFiles()
				if var[0] not in label_table:
					try:
						label_table[var[0]] = LC
						f4.writelines(var[0]+" "+str(LC)+"\n")
					except:
						print("[Error] No inital value provided at Declaration of Variable "+str(getLabel(var[0]))+" at line "+str(line_no))
						sys.exit(-1)
						delAllFiles()
			opcode = getOpcode(line)
			if opcode==-2:
				print("at line "+str(line_no))
				sys.exit(-1)
				delAllFiles()
			if getOperand(line) == -2:
				print("at line "+str(line_no))
				sys.exit(1)
				delAllFiles()
			if "DS" in line:
				f1.writelines(str(LC)+" "+line[0]+" "+opcode+" " +str(getOperand(line)+" \n"))
			else:
				f1.writelines(str(LC)+ " " +opcode+ " " + "None" +"\n")
			if not(isComment(line)):
				if MOT[opcode][1]==0:
					LC += 4
				else:
					LC += 12
	if end_flag:
		print("[Error] Missing END statement...")
		sys.exit(-1)
		delAllFiles()
	if start_flag:
		print("[Error] Missing START statement...")
		sys.exit(-1)
		delAllFiles()
	error_flag = False
			

def getFile():
	fileName=input("Enter file name: ")
	alp = open(fileName,'r')
	return alp

if __name__=='__main__':
	alp=getFile()
	# iChecker.main()
	pass_one(alp)
