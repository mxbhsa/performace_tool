.section .data
data_items:
 .long 233
.section .text
.globl _start
_start:
 mov $0, %rdi          # move 0 into the index register          # move 0 into the index register
 mov $0x6000e0, %rdx # load the first byte of data
start_loop:             # start loop

 inc %rdi
 cmp $10, %rdi          # check to see if we have hit the end
 je loop_exit 
 jmp start_loop
loop_exit:
 # %ebx is the status code for the _exit system call
 # and it already has the maximum number
 movl $1, %eax          #1 is the _exit() syscall
 int $0x80

