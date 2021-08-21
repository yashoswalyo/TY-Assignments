import os
import sys

from pyrogram.emoji import MOTOR_BOAT

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


def pass_one(alp):
	LC=0
	length = 20
	value = 0
	type = 'none'

	return


def getFile():
	fileName=input("Enter file name: ")
	alp = open(fileName,'r')
	return alp

if __name__=='__main__':
	alp=getFile()
	pass_one(alp)
	print(MOT[1][2])
