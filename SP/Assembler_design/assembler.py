import os
import sys
# import iChecker

MOT=[
['PRINT','01',1],
['STOP','02',1],
['ADD','03',1],
['SUB','04',1],
['MUL','05',1],
['MOVER','06',1],
['MOVEM','07',1],
['DEC','08',1],
['DIV','09',1],
['READ','0A',1],
['END','0B'],
['START','0C'],
['ORIGIN','0D'],   #address of next ins
['LTORG','0F'],    #Assigns address to literals
['DS','10'],
['DC','11'],
['AREG','12'],
['BREG','13'],
['CREG','14'],
['MREG','15'],
['JZ','16'],
['JNZ','17'],
['JC','18'],
['JNC','19']
]

def isComment(line):
	if line.find("//"):
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
	l=l.split()
	for "END" in l:
		return True
	return False

def pass_one(alp):
	LC=0
	length = 20
	value = 0
	type = 'none'
	f1 = open('tables/symbol_table.txt','a+')
	f2 = open(file='tables/literal_table.txt',mode='a+')
	f3 = open(file='tables/temp.txt',mode='a+')
	label_table={}
	symbol_table={}
	end_flag = True
	start_flag = True
	tok = 0
	line_no=0
	for line in alp:
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


	return


def getFile():
	fileName=input("Enter file name: ")
	alp = open(fileName,'r')
	return alp

if __name__=='__main__':
	alp=getFile()
	# iChecker.main()
	pass_one(alp)
	print(MOT[1][2])
