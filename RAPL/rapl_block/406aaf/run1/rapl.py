#!/usr/bin/python
import numpy as np
import os
import matplotlib.pyplot as plt
#logList = ["gcc_full","gcc_single"]
#logName = "gcc_full"

logList = [x for x in os.listdir("./") if ".log" in x]
#logList = ["rapl_416.gamess.log"]
print logList



#exit(0)

plt.figure(figsize=(18,6))

for nowLogName in logList:
	nowLogNum = 0
	
	print "plot log %s" % (nowLogName)
	logFile = open(nowLogName, 'r')
	linesList = logFile.readlines()
	linesList = [line.strip().split() for line in linesList if (not '-' in line)]
	linesList.pop(0)
	nCore = (len(linesList[0])-1) / 4;

	startTime = float(linesList[0][0])
	timeStamp = [float(x[0])-startTime for x in linesList]
	#print(timeStamp)
	nowCore = 0
	drawLabel = True
	while nowCore < nCore:
		P_PKG = [x[nowCore*4+2] for x in linesList]
		P_PP0 = [x[nowCore*4+3] for x in linesList]
		P_DRAM = [x[nowCore*4+4] for x in linesList]

		#if drawLabel:
		drawLabel = False
		plt.plot(timeStamp, P_PKG, 'b--',label="$P-PKG$")#,label=$cos(x^2)$)
		plt.plot(timeStamp, P_PP0, 'r-.',label="$P-PP0$")
		plt.plot(timeStamp, P_DRAM, "y:",label="$P-DRAM$")
		#else:
	#		plt.plot(timeStamp, P_PKG, 'b--')#,label=$cos(x^2)$)
	#		plt.plot(timeStamp, P_PP0, 'r-.')
	#		plt.plot(timeStamp, P_DRAM, "y:")

		nowCore += 1

		plt.xlabel('Time(s)')
		plt.ylabel('Power (W)')
		plt.title(nowLogName + ' power scale')
		plt.legend()
plt.savefig('./'+ nowLogName[0:-4]+ str(nowCore) +'.png')
plt.cla()

	#exit(0)

	


#plt.show()


exit(0)
