START 100
	MOVER AREG, A
	SUB BREG, B
	DIV AREG, 12
	EZ L1
	PRINT A
	LT L2
L1 : PRINT B
	DEC B 
	ADD BREG
	GT L2
L2 : STOP
A DC 120
B DC 125
END