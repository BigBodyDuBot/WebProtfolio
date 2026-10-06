.global _start
_start:
	
	mov r0, #0
	mov r1, #2
	mov r2, #5
	mov r3, #6
	mov r4, #0
	mov r5, #0
	// 2+5
	
	//5*2
	mul r4, r2, r1
	//5+2
	add r0, r2, r1
	//
	//5+2-5*2
	sub r3, r0, r4