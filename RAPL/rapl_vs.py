#!/usr/bin/python
import numpy as np
import os
import matplotlib.pyplot as plt
logList = ["gcc_full","gcc_single"]
#logName = "gcc_full"

plt.figure(figsize=(18,6))
12
subNum = 0
for logName in logList:
	nowLogNum = 0
	nowLogName = "./"+logName   +"_"+  str(nowLogNum)+".log"
	drawLabel = True

	while os.path.exists(nowLogName):
		print "plot log %s" % (logName   +"_"+  str(nowLogNum)+".log")
		logFile = open(nowLogName, 'r')
		linesList = logFile.readlines()
		linesList = [line.strip().split() for line in linesList]
		#print (linesList)
		nowLogNum += 1
		nowLogName = "./"+logName+"_"+str(nowLogNum)+".log"
		linesList.pop(0)

		startTime = float(linesList[0][0])
		timeStamp = [float(x[0])-startTime for x in linesList]
		#print(timeStamp)
		pl = plt.subplot((len(logList)+1)/2,2,subNum)

		nCore = (len(linesList[0])-1) / 4;
		for x in xrange(0,nCore):
			pass
		P_PKG = [x[2] for x in linesList]
		P_PP0 = [x[3] for x in linesList]
		P_DRAM = [x[4] for x in linesList]

		if drawLabel:
			drawLabel = False
			pl.plot(timeStamp, P_PKG, 'b--',label="$P-PKG$")#,label=$cos(x^2)$)
			pl.plot(timeStamp, P_PP0, 'c-.',label="$P-PP0$")
			pl.plot(timeStamp, P_DRAM, "g:",label="$P-DRAM$")
		else:
			pl.plot(timeStamp, P_PKG, 'b--')#,label=$cos(x^2)$)
			pl.plot(timeStamp, P_PP0, 'c-.')
			pl.plot(timeStamp, P_DRAM, "g:")
			
		pl.set_xlabel('Time(s)')
		pl.set_ylabel('Power (W)')
		pl.set_title(logName   +"_"+  str(nowLogNum)+".log"+' power scale')
		pl.legend()

	subNum += 1

plt.savefig('./plot/2333.png')
plt.show()


exit(0)
