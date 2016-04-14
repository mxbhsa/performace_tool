.section .data
data_items:
 .long 233
.section .text
.globl _start
_start:
 mov $0, %r9
 mov $0, %rdi          # move 0 into the index register          # move 0 into the index register
 mov $0x600128, %r11 # load the first byte of data
 mov %r11, %rcx
 mov %r11, %r8
 mov $0, %rbx
 mov $214783641, %rdi
start_loop_1:             # start loop
 
 mov    (%r11),%ecx
 sub    $0x1,%rdi
 lea    (%rcx,%rbx,1),%r10d
 test   %ecx,%ecx
 cmovs  %r10d,%ecx
 movslq %ecx,%rcx
 movzbl (%r8,%rbx,1),%ecx
 movzbl 0x180(%r11,%rbx,1),%ebp
 movzbl 0x80(%r11),%ecx
 cmp    $0 , %rdi          # check to see if we have hit the end
 je again 



 jmp start_loop_1         # jump to loop beginning
again:
 inc %r9
 cmp $10, %r9
 je loop_exit
 mov $214783641, %rdi
 jmp start_loop_1
loop_exit:
 # %ebx is the status code for the _exit system call
 # and it already has the maximum number
 movl $1, %eax          #1 is the _exit() syscall
 int $0x80

