.global _start
_start:
	
	mov r0, #3
	mov r1, #3
	//compare = cmp
	loop:
	cmp r0, #5 //no need for destination register value stored at cpsr
	
	BGE exit
	
	add r0, r0, #1
	B loop
	
exit:
	
	

