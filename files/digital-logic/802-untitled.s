.global _start
_start:
mov r0, #0 //I made r0 = 0
mov r1, #5 //I made r1 = 5
	loop: //this is the loop
		cmp r0, r1 //this compares r1 and r0
		BEQ exit //I exit the loop with a branch only when r0 and r1 are equal
		add r0, r0, #1 // in the loop, when r0 does != r1, it adds #1 to r0
	
		b loop // this makes my program loop
exit:
	and r2, r1,r0 // when r1 and r0 are equal, the branch breaks into the the and
				  // and makes r2 the value of r0 and r1
		
	