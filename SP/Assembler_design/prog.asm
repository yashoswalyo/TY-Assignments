START 100
	MOVER AREG, A
	MOVER BREG, B
	SUB BREG
	DIV AREG
	JZ L1
	PRINT A
	JC L2
L1 : PRINT B
	DEC B 
	ADD BREG
	JNZ L2
L2 : STOP
A DC 120
B DC 125
END