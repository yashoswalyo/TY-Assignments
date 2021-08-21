import os
import sys

from pyrogram.emoji import MOTOR_BOAT

MOT=[
['PRINT','IS','01',1],
['STOP','IS','02',1],
['ADD','IS','03',1],
['SUB','IS','04',1],
['MUL','IS','05',1],
['MOVER','IS','06',1],
['MOVEM','IS','07',1],
['DEC','IS','08',1],
['DIV','IS','09',1],
['READ','IS','0A',1],
['END','AD','01'],
['START','AD','02'],
['ORIGIN','AD','03'], #address of next ins
['EQU','AD','04'],
['LTORG','AD','05'],    #Assigns address to literals
['DS','DL','01'],
['DC','DL','02'],
['AREG','RG','01'],
['BREG','RG','02'],
['CREG','RG','03'],
['MREG','RG','04'],
['EQ','CC','01'],
['LT','CC','02'],
['GT','CC','03'],
['LE','CC','04'],
['GE','CC','05'],
['NE','CC','06']
]


def pass_one(alp):
    LC=0
    length = 20
    return


def getFile():
    fileName=input("Enter file name: ")
    alp = open(fileName,'r')
    return alp

if __name__=='__main__':
    alp=getFile()
    pass_one(alp)
    print(MOT[1][2])
