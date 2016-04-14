fg = open("genasm.txt","w+")

for x in xrange(0,100000):
    fg.write( "mov    %esi,%eax\nmov    %esi,%r10d\nmovzbl (%rdx,%rax,1), %eax\ncmp    %al,(%rdx,%r10,1) \nje\tstart_loop \n")


fg.close()
