  4040fb:	8b 83 88 02 00 00    	mov    0x288(%rbx),%eax
  404101:	89 c6                	mov    %eax,%esi
  404103:	c1 e0 08             	shl    $0x8,%eax
  404106:	c1 ee 18             	shr    $0x18,%esi
  404109:	31 d6                	xor    %edx,%esi
  40410b:	40 0f b6 f6          	movzbl %sil,%esi
  40410f:	33 04 b5 e0 f0 60 00 	xor    0x60f0e0(,%rsi,4),%eax
  404116:	89 83 88 02 00 00    	mov    %eax,0x288(%rbx)
  40411c:	89 d0                	mov    %edx,%eax
  40411e:	c6 84 03 80 00 00 00 	movb   $0x1,0x80(%rbx,%rax,1)
  404126:	48 8b 43 40          	mov    0x40(%rbx),%rax
  40412a:	88 14 08             	mov    %dl,(%rax,%rcx,1)
  40412d:	44 89 6b 5c          	mov    %r13d,0x5c(%rbx)
  404131:	83 43 6c 01          	addl   $0x1,0x6c(%rbx)
  404135:	48 8b 03             	mov    (%rbx),%rax
  404138:	e9 58 ff ff ff       	jmpq   404095 <handle_compress.isra.2+0x2e5>