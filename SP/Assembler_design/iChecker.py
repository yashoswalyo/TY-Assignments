#!/bin/python3
from pyrogram.emoji import *
class instructionSet(object):
	NO_OPERAND_INSTRUCTION = [
		'AAA','AAD','AAM','AAS','CBW'  ,'CLC'  ,'CLD'  ,'CLI'  ,'CMC'  ,'CMPSB' , 'CMPSW'  ,
		'CWD'  ,'DAA'  ,'DAS'  ,'DIV'  ,'HLT'  ,'INTO'  ,'IRET'  ,'LAHF' ,'LODSB' ,'LODSW' ,
		'MOVSB' ,'MOVSW' ,'NOP' ,'POPA' ,'POPF' ,'PUSHA' ,'PUSHF' ,'RET' ,'RETF' ,'SAHF' ,
		'SCASB' ,'SCASW' ,'STC' ,'STD' ,'STI' ,'STOSB' ,'STOSW' ,'XLATB' ,'XCHG' 
	]
	SINGLE_OPERAND_INSTRUCTION = [
		'CALL','DEC'  ,'IDIV'  ,'IMUL'  ,'INC'  ,'INT'  ,'JA'  ,'JAE'  ,'JB'  ,'JBE'  ,
		'JC'  ,'JCXZ' , 'JE'  ,'JG'  ,'JGE'  ,'JL'  ,'JLE'  ,'JMP'  ,'JNA'  ,'JNAE'  ,'JNB'  ,'JNBE'  ,
		'JNC'  ,'JNE'  ,'JNG'  ,'JNGE'  ,'JNL'  ,'JNLE'  ,'JNO'  ,'JNP'  ,'JNS'  ,'JNZ'  ,'JO'  ,'JP'  ,
		'JPE'  ,'JPO' ,'JS' ,'JZ' ,'LOOP' ,'LOOPE' ,
		'LOOPNE' ,'LOOPNZ' ,'LOOPZ' ,'MUL' ,'NEG' ,'NOT' ,'POP' ,'PUSH' ,'REP' ,'REPE' ,'REPNE' ,
		'REPNZ' ,'REPZ' 
	]
	TWO_OPERAND_INSTRUCTION = [
		'ADC' , 'ADD'  ,'AND'  ,
		'CMP'  ,
		'IN' ,'LDS' ,'LEA' ,'LES' ,'MOV' ,'OR' ,'OUT' ,
		'RCL' ,'RCR' ,'ROL' ,'ROR' ,'SAL' ,'SAR' ,'SBB' ,
		'SHL' ,'SHR' ,'SUB' ,'TEST' ,'XOR'
	]
	REGISTERS = [
		'AX', 'BX', 'CX', 'DX', 'AH', 'AL', 'BL', 'BH', 
		'CH', 'CL', 'DH', 'DL', 'DI', 'SI', 'BP', 'SP'
	]

if __name__ == '__main__':
	filename = input("Enter your file name to check(.asm): ")
	program = open(f'{filename}','r')
	lines = program.readlines()
	count = 0
	for line in lines:
		count+=1
		print('--------------------------------------\n')
		operands = ['-','-']
		label = "-"
		instruction = line.strip()
		print(f"Checking line {count}. .  .   .")
		instruction = instruction.upper()

		#Checking labels
		if ": " in instruction:
			instruction = instruction.split(": ")
			print(f'Label {CHECK_MARK_BUTTON}')
			label = instruction[0]
			instruction = instruction[1]
			pass
		else:
			pass

		#Checking instructions
		rest = instruction.split(" ")
		inst = rest[0]
		if inst in instructionSet.TWO_OPERAND_INSTRUCTION:
			print(f"Instruction {CHECK_MARK_BUTTON} ")
			operands = rest[1].split(",")
			i=1
			#Checking registers
			if operands[0]  in instructionSet.REGISTERS:
				print(f"Register {i} {CHECK_MARK_BUTTON} ")
				if operands[1] in instructionSet.REGISTERS:
					i=i+1
					print(f"Register {i} {CHECK_MARK_BUTTON} ")
					pass
				pass
			elif operands[1] in instructionSet.REGISTERS:
				print(f"Register {i} {CHECK_MARK_BUTTON} ")
			
				pass
			else:
				print(f"Register {CROSS_MARK} ")
				pass
			pass

		elif inst in instructionSet.SINGLE_OPERAND_INSTRUCTION:
			print(f"Instruction {CHECK_MARK_BUTTON} ")
			operands[0] = rest[1]
			i=1
			if operands[0]  in instructionSet.REGISTERS:
				print(f"Register {i} {CHECK_MARK_BUTTON} ")
				pass
			else:
				print(f"Register {CROSS_MARK} ")
				pass
			pass

		elif inst in instructionSet.NO_OPERAND_INSTRUCTION:
			print(f"Instruction {CHECK_MARK_BUTTON} ")
			pass
		else:
			print(f"Instruction {CROSS_MARK} ")
			continue
		print(f"\nLABEL: {label}\nINSTRUCTION: {inst} \nOPERAND 1: {operands[0]}\nOPERAND 2: {operands[1]} ")
			