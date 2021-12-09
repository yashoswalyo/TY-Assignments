from io import TextIOWrapper

MOT={
	'BEGIN' : ('#R1', 'AD', 1),
	'STOP' : ('#R2', 'AD', 0),
	'ORIGIN' : ('#R3', 'AD', 0),
	'MVR' : ('01', 'IS', 2),
	'MVM' : ('02', 'IS', 2),
	'AD' : ('03', 'IS', 2),
	'RD' : ('04', 'IS', 1),
	'SB' : ('05', 'IS', 2),
	'JP' : ('06', 'IS', 3),
	'ML' : ('07', 'IS', 2),
	'DCN' : ('#R4', 'DL', 1),
	'DST' : ('#R5', 'DL', 1),
}

REG={
	'R1':1,
	'R2':2,
	'R3':3,
	'R4':4
}

		

class vars():
	LC=0
	ifp=open("LC_Code.txt",mode="a")
	ifp.truncate(0)
	symtab={}
	words=[]
	symindex=0

def listToString(s): 
	str1 = " " 
	return (str1.join(s))

def STOP():
	vars.ifp.write(f"\t{listToString(vars.words)}\n")

def ORIGIN(addr):
	vars.ifp.write(f"\t{listToString(vars.words)}\n")
	vars.LC =int(addr)

def DS(size):
	vars.ifp.write(f"\t{listToString(vars.words)}\n")
	vars.LC=vars.LC+int(size)

def DC(value):
	vars.ifp.write(f"\t{listToString(vars.words)}\n")
	vars.LC+=1

def JP(label):
	print(label)
	vars.ifp.write(f"\t{listToString(vars.words)}\n")

	vars.LC+=3

def OTHERS(key,k):
	z=MOT[key]
	# vars.ifp.write("IN others func()\n")
	i=0
	y=z[-1]
	for i in range(1,y+1):
		vars.words[k+i]=vars.words[k+i].replace(",","")
		if(vars.words[k+i] in REG.keys()):
			vars.ifp.write(f"\t{listToString(vars.words)}\n")
			vars.LC+=z[-1]
			return
		else:
			if(vars.words[k+i] not in vars.symtab.keys()):
				vars.symtab[vars.words[k+i]]=("**",vars.symindex)
				vars.ifp.write(f"\t{listToString(vars.words)}\n")
				vars.symindex+=1
	# vars.ifp.write("\n")
	vars.LC+=z[-1]

def detect_mn(k):
	if(vars.words[k]=="BEGIN"):
		vars.LC = int(vars.words[1])
		vars.ifp.write(f"\t{listToString(vars.words)}\n")
	elif(vars.words[k]=='STOP'):
		STOP()
	elif(vars.words[k]=="ORIGIN"):
		ORIGIN(vars.words[k+1])
	elif(vars.words[k]=="DST"):
		DS(vars.words[k+1])
	elif(vars.words[k]=="DCN"):
		DC(vars.words[k+1])
	elif(vars.words[k]=="JP"):
		JP(vars.words[k+1])
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
	sym=open("symbol_table.txt","a+")
	sym.truncate(0)
	for x in vars.symtab:
		sym.write(x+"\t"+str(vars.symtab[x][0])+"\n")
	sym.close()
	
def error_handler(line:str,lc:int):
	print(f"\nChecking line {lc} for errors")
	l=line.split()
	print(l)
	if l[0] == 'JP':
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
	# fileName=input("Enter file name: ")
	alp = open('ese.asm','r')
	return alp

if __name__=='__main__':
	alp=getFile()
	pass_one(alp)
