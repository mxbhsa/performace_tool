#!/usr/bin/python
from operator import itemgetter, attrgetter
from pc import *
from convert import *
import os

PCFile = "bb.429.pc"
SimpointsFile = "429.simpoints"
ASMFile = "mcf.d.obj"
BBVFile = "bb.out.15977"
SimWeightFile = "429.weights"

fb = open(BBVFile,'r')
fw = open(SimWeightFile,'r')
fp = open(SimpointsFile,'r')
fpc = open(PCFile,'r')
fblock = open("bbv.block",'w+')
fsample = open("bbv.sample",'w+')

asmpre = open("pre.asm",'r')
asmpost = open("post.asm",'r')
asmpreText = asmpre.read( )
asmpostText = asmpost.read( )
asmpre.close()
asmpost.close()

tWCluster = []
wCluster = []
nCluster = 0
try:  
  for line in fw:  
         nCluster += 1
         tWCluster.append(float(line.split(" ")[0]))
finally:  
      fw.close( ) 


intList = []
try:  
  for line in fp:  
    ele = line.split(" ")
    intList.append(int(ele[0]))
finally:  
      fp.close( ) 


clusterIntList = []
finalIntList = []
nowLine = 0
for line in fb:
    posi = nowLine in intList
    if posi:
         clusterIntList.append(line)
         wCluster.append(tWCluster[intList.index(nowLine)])
         finalIntList.append(nowLine)
    nowLine += 1

print finalIntList

clusterIntDic = []
maxClusterIntDic = []
i = 0
for ele in clusterIntList:
    clusterIntDic.append([])
    maxClusterIntDic.append([])
    blockList = ele.split(':')
    blockList.pop(0)
    j = 0
    for block in blockList:
        if j % 2 == 1:
            j += 1
            continue
        blockList[j] = int(blockList[j])
        clusterIntDic[i].append((int(blockList[j]),int(blockList[j+1])))
        j += 1
    clusterIntDic[i] = sorted(clusterIntDic[i], key=itemgetter(1),reverse=True)  
    maxClusterIntDic[i] = clusterIntDic[i][0:5]
    i += 1
    #break
print maxClusterIntDic
#block mark
pcBlockDic = {}
try:  
  for line in fpc:  
    ele = line.split(":")
    pcBlockDic[int(ele[1])] = ele[2]
finally:  
      fpc.close( ) 

bb = processBasicBlock(PCFile, ASMFile)
i = 0
for ele in maxClusterIntDic:
    fblock.write("-------------\n")
    fsample.write("------------- "+ str(finalIntList[i]) + " -------------\n")
    if os.path.exists('./sample/'+str(finalIntList[i])):
      pass
    else:
      os.makedirs('./sample/'+str(finalIntList[i]))
    for ele2 in ele:
        fblock.write(pcBlockDic[ele2[0]] + " " + str(int(ele2[1]*wCluster[i] + 0.5)) + "\n")
        #print pcBlockDic[ele2[0]], ele2[1]
        ans = binSearchBlock(pcBlockDic[ele2[0]], bb)
        print ans 
        if ans == -1:
          continue
        fsample.write(bb[ans]["PC"] + "\n" + bb[ans]["CODE"] +  str(bb[ans]["TYPE"]) + "\n")
        nowBlock = open('./sample/'+str(finalIntList[i])+"/"+bb[ans]["PC"]+".asm",'w+')
        sgBlock = asmSmooth(bb[ans]["CODE"])
        nowBlock.write(asmpreText + sgBlock + sgBlock + sgBlock + sgBlock + sgBlock +  asmpostText)
        nowBlock.close()
        #raw_input()
    i += 1
fblock.close()
fsample.close()


#finally:  
#    print 233
#    fb.close( ) 

#print nCluster, clusterIntList