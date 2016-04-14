402529: 44 0f b6 01           movzbl (%rcx),%r8d
  40252d: 66 c1 e8 08           shr    $0x8,%ax
  402531: 48 83 e9 04           sub    $0x4,%rcx
  402535: 41 c1 e0 08           shl    $0x8,%r8d
  402539: 44 09 c0              or     %r8d,%eax
  40253c: 44 0f b7 c0           movzwl %ax,%r8d
  402540: 66 c1 e8 08           shr    $0x8,%ax
  402544: 4e 8d 0c 87           lea    (%rdi,%r8,4),%r9
  402548: 41 8b 19              mov    (%r9),%ebx
  40254b: 44 8d 43 ff           lea    -0x1(%rbx),%r8d
  40254f: 45 89 01              mov    %r8d,(%r9)
  402552: 4d 63 c0              movslq %r8d,%r8
  402555: 42 89 14 86           mov    %edx,(%rsi,%r8,4)
  402559: 44 0f b6 41 03        movzbl 0x3(%rcx),%r8d
  40255e: 41 c1 e0 08           shl    $0x8,%r8d
  402562: 44 09 c0              or     %r8d,%eax
  402565: 44 0f b7 c0           movzwl %ax,%r8d
  402569: 66 c1 e8 08           shr    $0x8,%ax
  40256d: 4e 8d 0c 87           lea    (%rdi,%r8,4),%r9
  402571: 41 8b 19              mov    (%r9),%ebx
  402574: 44 8d 43 ff           lea    -0x1(%rbx),%r8d
  402578: 45 89 01              mov    %r8d,(%r9)
  40257b: 44 8d 4a ff           lea    -0x1(%rdx),%r9d
  40257f: 4d 63 c0              movslq %r8d,%r8
  402582: 46 89 0c 86           mov    %r9d,(%rsi,%r8,4)
  402586: 44 0f b6 41 02        movzbl 0x2(%rcx),%r8d
  40258b: 41 c1 e0 08           shl    $0x8,%r8d
  40258f: 44 09 c0              or     %r8d,%eax
  402592: 44 0f b7 c0           movzwl %ax,%r8d
  402596: 66 c1 e8 08           shr    $0x8,%ax
  40259a: 4e 8d 0c 87           lea    (%rdi,%r8,4),%r9
  40259e: 41 8b 19              mov    (%r9),%ebx
  4025a1: 44 8d 43 ff           lea    -0x1(%rbx),%r8d
  4025a5: 45 89 01              mov    %r8d,(%r9)
  4025a8: 44 8d 4a fe           lea    -0x2(%rdx),%r9d
  4025ac: 4d 63 c0              movslq %r8d,%r8
  4025af: 46 89 0c 86           mov    %r9d,(%rsi,%r8,4)
  4025b3: 44 0f b6 41 01        movzbl 0x1(%rcx),%r8d
  4025b8: 41 c1 e0 08           shl    $0x8,%r8d
  4025bc: 44 09 c0              or     %r8d,%eax
  4025bf: 44 0f b7 c0           movzwl %ax,%r8d
  4025c3: 4e 8d 0c 87           lea    (%rdi,%r8,4),%r9
  4025c7: 41 8b 19              mov    (%r9),%ebx
  4025ca: 44 8d 43 ff           lea    -0x1(%rbx),%r8d
  4025ce: 45 89 01              mov    %r8d,(%r9)
  4025d1: 44 8d 4a fd           lea    -0x3(%rdx),%r9d
  4025d5: 83 ea 04              sub    $0x4,%edx
  4025d8: 4d 63 c0              movslq %r8d,%r8
  4025db: 83 fa 02              cmp    $0x2,%edx
  4025de: 46 89 0c 86           mov    %r9d,(%rsi,%r8,4)
  4025e2: 0f 8f 41 ff ff ff     jg     402529 <mainSort+0x229>