.section .data
data_items:
 .long 0x6000f8
.section .text
.globl _start
_start:
 mov $0, %rdi          # move 0 into the index register          # move 0 into the index register
 mov $0x6000f9, %rdx # load the first byte of data
 mov $0x6000f9, %r10
 mov $0x6000f9, %edx
 mov $0, %rbx

start_loop:             # start loop
 inc %rdi
 cmp $20000000, %rdi          # check to see if we have hit the end
 je loop_exit 

 mov    (%r10),%edx
 lea    (%rdx,%rbx,1),%eax
 movzbl 0x0(%rbx,%rax,1),%eax
 sub    %ebx,%eax
 cmp    $0x0,%eax
 jne    start_loop        # jump to loop beginning

loop_exit:
 # %ebx is the status code for the _exit system call
 # and it already has the maximum number
 movl $1, %eax          #1 is the _exit() syscall
 int $0x80


