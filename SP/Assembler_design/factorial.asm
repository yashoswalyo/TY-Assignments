MOV AX,05H 
MOV CX,AX 
Back: DEC CX 
MUL CX 
LOOP back 
; results stored in AX 
; to store the result at D000H 
MOV [D000],AX 
HLT