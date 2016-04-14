.section .data
data_items:
 .long 0x6000e0
.section .text
.globl _start
_start:
 mov $0, %rdi          # move 0 into the index register          # move 0 into the index register
 mov $0x6000e0, %rdx # load the first byte of data
 mov $0x6000e0, %r10
 mov $0x6000e0, %edx
 mov $0, %rbx

start_loop:             # start loop
 inc %rdi
 cmp $200000000, %rdi          # check to see if we have hit the end
 je loop_exit 


movslq %r12d,%rax
add    $0x1,%rbx
lea    (%rdx,%rbx,4),%rax
mov    (%rax),%esi
mov    %esi,(%r10)
mov    %edx,(%rax) 


 jmp start_loop         # jump to loop beginning

loop_exit:
 # %ebx is the status code for the _exit system call
 # and it already has the maximum number
 movl $1, %eax          #1 is the _exit() syscall
 int $0x80

