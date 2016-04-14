.section .data
data_items:
 .long 233
.section .text
.globl _start
_start:
 mov $0, %r9
 mov $0, %rdi          # move 0 into the index register          # move 0 into the index register
 mov $0x6000e0, %rdx # load the first byte of data
start_loop_1:             # start loop
 inc %rdi
 cmp  $2147483647, %rdi          # check to see if we have hit the end
 je again
 mov    %esi,%eax
 movzbl (%rdx,%rax,1),%eax
 mov    %esi,%r10d
 cmp    %al,(%rdx,%r10,1)    
 jmp start_loop_1         # jump to loop beginning
again:
inc %r9
cmp $10, %r9
je loop_exit
mov $0, %rdi
jmp start_loop_1
loop_exit:
 # %ebx is the status code for the _exit system call
 # and it already has the maximum number
 movl $1, %eax          #1 is the _exit() syscall
 int $0x80

