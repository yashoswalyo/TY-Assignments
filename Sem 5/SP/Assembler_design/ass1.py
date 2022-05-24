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
	'DC':('02','DL',1),
	'GT':('00','CC',0)
}

REG={
	'R1':1,
	'R2':2,
	'R3':3,
	'R4':4
}

		

class vars():
	LC=0
	ifp=open("tables/inter_code.txt",mode="a")
	ifp.truncate(0)
	tmp=open("tables/temp.txt","a+")
	tmp.truncate(0)
	symtab={}
	words=[]
	symindex=0


def END():
	vars.ifp.write("\t(AD,02)\n")

def ORIGIN(addr):
	vars.ifp.write("\t(AD,03)\t(C,"+str(addr)+")\n")
	vars.LC =int(addr)

def DS(size):
	vars.ifp.write("\t(DL,01)\t(C,"+size+")\n")
	vars.LC=vars.LC+int(size)

def DC(value):
	vars.ifp.write("\t(DL,02)\t(C,"+value+")\n")
	vars.LC+=1

def OTHERS(key,k):
	z=MOT[key]
	vars.ifp.write("\t("+z[1]+","+z[0]+")\t")
	i=0
	y=z[-1]
	for i in range(1,y+1):
		vars.words[k+i]=vars.words[k+i].replace(",","")
		if(vars.words[k+i] in REG.keys()):
			vars.ifp.write("(RG,"+str(REG[vars.words[k+i]])+")")
		else:
			if(vars.words[k+i] not in vars.symtab.keys()):
				vars.symtab[vars.words[k+i]]=("**",vars.symindex)
				vars.ifp.write("(S,"+str(vars.symindex)+")")
				vars.symindex+=1
			else:
				w=vars.symtab[vars.words[k+i]]
				vars.ifp.write("(S,"+str(w[-1])+")")
	vars.ifp.write("\n")
	vars.LC+=z[-1]

def detect_mn(k):
	if(vars.words[k]=="START"):
		vars.LC=int(vars.words[1])
		vars.ifp.write("\t(AD,01)\t(C,"+str(vars.LC)+')\n')
	elif(vars.words[k]=='END'):
		END()
	elif(vars.words[k]=="ORIGIN"):
		ORIGIN(vars.words[k+1])
	elif(vars.words[k]=="DS"):
		DS(vars.words[k+1])
	elif(vars.words[k]=="DC"):
		DC(vars.words[k+1])
	else:
		OTHERS(vars.words[k],k)

def pass_one(alp:TextIOWrapper):
	lc=1
	for line in alp:
		error_handler(line,lc)
		lc+=1
		vars.words=line.split()
		if (vars.LC>0):
			vars.ifp.write(str(vars.LC))
		k=0
		if vars.words[0] in MOT.keys():
			val = MOT[vars.words[0]]
			detect_mn(k)
		else:
			if vars.words[k] not in vars.symtab.keys():
				vars.symtab[vars.words[k]]=(vars.LC,vars.symindex)
				#ifp.write("\t(S,"+str(symindex)+")\t")	
				vars.symindex+=1
			else:
				x = vars.symtab[vars.words[k]]
				if x[0] == "**":
					vars.symtab[vars.words[k]] = (vars.LC,x[1])
			k=1
			detect_mn(k)
	vars.ifp.close()
	vars.tmp.close()
	sym=open("tables/symbol_table.txt","a+")
	sym.truncate(0)
	for x in vars.symtab:
		sym.write(x+"\t"+str(vars.symtab[x][0])+"\n")
	sym.close()
	
def error_handler(line:str,lc:int):
	print(f"\nChecking line {lc} for errors")
	l=line.split()
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
	fileName=input("Enter file name: ")
	alp = open(fileName,'r')
	return alp

if __name__=='__main__':
	alp=getFile()
	pass_one(alp)
