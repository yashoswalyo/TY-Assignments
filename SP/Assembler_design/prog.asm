	START 500
X  DC 65
	MOVER AREG, Y
	MOVEM BREG, ='11'
	ADD AREG, ='24'
	LTORG
	SUB BREG, ='15'
Y  DC 20 
	ORIGIN 800
	LTORG
	BC DOWN
	MOVER AREG, NUM
DOWN  MOVER CREG, NUM
	ADD BREG, ='17'
NUM DS 5
END 