from io import TextIOWrapper

MOT={
	'BEGIN' : ('#R1', 'AD', 1),
	'STOP'  : ('#R2', 'AD', 0),
	'ORIGIN': ('#R3', 'AD', 0),
	'MVR'   : ('01', 'IS', 2),
	'MVM'   : ('02', 'IS', 3),
	'AD'    : ('03', 'IS', 2),
	'RD'    : ('04', 'IS', 2),
	'SB'    : ('05', 'IS', 2),
	'JP'    : ('06', 'IS', 3),
	'ML'    : ('07', 'IS', 2),
	'DCN'   : ('#R4', 'DL', 1),
	'DST'   : ('#R5', 'DL', 1),
}

REG={
	'R1':1,
	'R2':2,
	'R3':3,
	'R4':4
}

class vars():
	LC=0
	opt=open("LC_Code.txt",mode="a+")
	opt.truncate(0)
	symtab={}
	words=[]
	symindex=0

def listToString(s): 
	str1 = " "
	return (str1.join(s))

def STOP():
	vars.opt.write(f"\t{listToString(vars.words)}\n")

def ORIGIN(addr):
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC =int(addr)

def DS(size):
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC=vars.LC+int(size)

def DC(value):
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC+=1

def JP():
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC+=3

def RD():
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC+=2

def MVM():
	vars.opt.write(f"\t{listToString(vars.words)}\n")
	vars.LC+=3

def OTHERS(key,k):
	z=MOT[key]
	i=0
	y=z[-1]
	for i in range(1,y+1):
		vars.words[k+i]=vars.words[k+i].replace(",","")
		if(vars.words[k+i] in REG.keys()):
			vars.opt.write(f"\t{listToString(vars.words)}\n")
			vars.LC+=z[-1]
			return
		else:
			if(vars.words[k+i] not in vars.symtab.keys()):
				vars.symtab[vars.words[k+i]]=("**",vars.symindex)
				vars.opt.write(f"\t{listToString(vars.words)}\n")
				vars.symindex+=1
	vars.LC+=z[-1]


def detect_mn(k):
	if(vars.words[k]=="BEGIN"):
		vars.LC = int(vars.words[1])
		vars.opt.write(f"\t{listToString(vars.words)}\n")

	elif(vars.words[k]=='STOP'):
		STOP()

	elif(vars.words[k]=="ORIGIN"):
		ORIGIN(vars.words[k+1])

	elif(vars.words[k]=="DST"):
		DS(vars.words[k+1])

	elif(vars.words[k]=="DCN"):
		DC(vars.words[k+1])

	elif(vars.words[k]=="JP"):
		JP()

	elif(vars.words[k]=="RD"):
		RD()

	elif(vars.words[k]=="MVM"):
		MVM()

	else:
		OTHERS(vars.words[k],k)

def pass_one(alp:TextIOWrapper):
	lc = 1
	for line in alp:
		error_handler(line,lc)
		lc+=1
		vars.words=line.split()
		if (vars.LC>0):
			vars.opt.write(str(vars.LC))
		k=0
		if vars.words[0] in MOT.keys():
			val = MOT[vars.words[0]]
			detect_mn(k)
		else:
			if vars.words[k] not in vars.symtab.keys():
				vars.symtab[vars.words[k]]=(vars.LC,vars.symindex) #=> symtab = {'NEXT': 800,0}
				vars.symindex+=1
			else:
				x = vars.symtab[vars.words[k]]
				if x[0] == "**":
					vars.symtab[vars.words[k]] = (vars.LC,x[1])
			k=1
			detect_mn(k)
	vars.opt.close()
	sym=open("symbol_table.txt","a+")
	sym.truncate(0)
	
	for x in vars.symtab:
		sym.write(str(vars.symtab[x][1])+"\t"+x+"\t"+str(vars.symtab[x][0])+"\n")
	sym.close()
	

def error_handler(line:str,lc:int):
	print(f"\nChecking line {lc} for errors")
	l=line.split() #=> ['NEXT' 'RD' 'Sum']
	print(l)
	try:
		if l[0] == 'JP' or l[1] == 'RD' or l[0] == 'MVM':
			return
	except IndexError:
		return
	if l[0] in MOT.keys():
		op = MOT[l[0]]
		if (len(l)-1) < op[-1]:
			print(f"[-] Error at line {lc}: Less operands than expcted")
			exit(-1)
		elif (len(l)-1) > op[-1]:
			print(f"[-] Error at line {lc}: More operands than expcted")
			exit(-1)
		else:
			print(f"[+] No errors at line {lc}")
	elif l[1] in MOT.keys():
		op = MOT[l[1]]
		if (len(l)-2) < op[-1]:
			print(f"[-] Error at line {lc}: Less operands than expcted")
			exit(-1)
		elif (len(l)-2) > op[-1]:
			print(f"[-] Error at line {lc}: More operands than expcted")
			exit(-1)
		else:
			print(f"[+] No errors at line {lc}")
	else:
		print(f"[-] Invalid Instruction at line {lc}: {line}")
		exit(-1)


def getFile():	
	alp = open('ese.asm','r')
	return alp


if __name__=='__main__':
	alp=getFile()
	pass_one(alp)
