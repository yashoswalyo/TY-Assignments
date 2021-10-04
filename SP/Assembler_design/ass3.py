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

class file(object):
    ifp=open("tables/inter_code.txt",mode="r")
    lit=open("tables/literal_table.txt","r")
    sym=open("tables/symbol_table.txt","r")
    output=open("tables/output.txt","a+")
    output.truncate(0)

def pass_two(intermediateCode: TextIOWrapper):
    for line in intermediateCode:
        if "(AD,01)" in line:
            pass
        elif "DL" in line:
            pass
        else:
            words = line.split()
            print(words)


pass_two(intermediateCode=file.ifp)