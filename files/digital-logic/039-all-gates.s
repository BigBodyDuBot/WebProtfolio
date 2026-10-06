.global _start
_start:
	
	mov r0, # 1//00000100
	mov r1, #0 //00000011
	
	eor r2,r1,r0 //
	and r3,r2,r0
	mvn r6,r1
	orr r5, r1,r3

	//nor gate= or+not
	orr r2,r0,r1
	mvn r3, r2
	
	//nand = and+not
	and r2,r1,r0
	mvn r3, r2
	
	//xnor = xor+not
	eor r2,r1,r0
	mvn r3, r2