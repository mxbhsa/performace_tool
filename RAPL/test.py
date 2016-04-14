#!/usr/bin/python
stt = "400.perlbench  416.gamess  435.gromacs    445.gobmk   454.calculix  462.libquantum  471.omnetpp  483.xalancbmk   401.bzip2      429.mcf     436.cactusADM  447.dealII  456.hmmer     464.h264ref     473.astar    998.specrand   403.gcc        433.milc    437.leslie3d   450.soplex  458.sjeng     465.tonto       481.wrf      999.specrand   410.bwaves     434.zeusmp  444.namd       453.povray  459.GemsFDTD  470.lbm         482.sphinx3  "
st2 = stt.split(" ")
st1 = []
print("(")
for t in st2:
	if len(t) > 0:
		st1.append(t)
		print t+" "
print ")"