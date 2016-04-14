	
	jmp start_loop_1         # jump to loop beginning
again:      
	inc %r9     
	cmp $1, %r9
	je loop_exit 
	mov $0, %rdi 
	jmp start_loop_1
loop_exit:
 	movl $1, %eax          #1 is the _exit() syscall
 	int $0x80

