import   commands

objList = ['ld-linux.obj','libc.so.6.obj','libm.so.6.obj']
objOffset = [0,0,0]
pcBlockList = []
offsetDic = {}

def getObjandOffset(pc, symbol):
    findList = []
    for obj in objList:
        f = open(obj, 'r')
        for line in f:
            if '<'+ symbol + '>:' in line or '<__'+ symbol + '>:' in line:
                offset = int(pc, 16) - int(line.split(" ")[0], 16)
                findList.append((f, offset, obj))
                break
    if len(findList) == 1 and not offsetDic.has_key(findList[0][2]):
        offsetDic[findList[0][2]] = findList[0][1]
    return findList


def searchDynamic(pc, symbol, offset, objFn):
    objFh = open (objFn, 'r')
    pc = int(pc, 16)
    offset = int(offset, 16)

    funcStart = symbol + '>:'
    ansList = []
    for line in objFh:
        if funcStart in line:
            nowOffset = int(line.split(' ')[0], 16)
            if nowOffset == pc - offset:
                print '-----', hex(nowOffset)
            ansList.append(nowOffset)
    print ansList
    
def processBasicBlock(pcFn, objFn):
    fblock = open(pcFn)
    fobj = open(objFn)

    i = -1
    for line in fblock:
        ele = line.strip().split(":")
        pcBlockList.append([ele[1],ele[2],ele[3],int(ele[4]),0])
        

    basicBlockList = []

    for line in fobj:
        ele = line.split("\t")
        if len(ele) != 3:
            continue
        flag = ele[0].replace(" ","").replace(":","") == pcBlockList[i+1][1]
        codeType = ele[2].split(" ")[0]
        if flag:
            #if i > -1:
                #print basicBlockList[i]
            basicBlockList.append({"PC":pcBlockList[i+1][0],"CODE":line})
            pcBlockList[i+1][-1] = 1
            i = i+1
            basicBlockList[i]["TYPE"] = {codeType:1}
            #raw_input()
        else:
            basicBlockList[i]["CODE"] = basicBlockList[i]["CODE"] + line
            if(basicBlockList[i]["TYPE"].has_key(codeType)):
                basicBlockList[i]["TYPE"][codeType] += 1
            else:
                basicBlockList[i]["TYPE"][codeType] = 1

    #return basicBlockList


    lastSymbol = ''
    objFile = None
    offset = 0
    nowBlockNum = 0
    lenPcBlockList = len(pcBlockList)
    for block in pcBlockList:
        if block[-1] == 0 and not block[2] == '':
            #print block
            if not block[2] == lastSymbol:
                #new function
                findList = getObjandOffset(block[1],block[2])
                #print findList
                if len(findList) == 0:
                    continue
                elif len(findList) > 1:
                    right = False
                    for ans in findList:
                        if offsetDic.has_key(ans[2]):
                            #print ans
                            objFile, offset, fn = ans
                            right = True
                            break
                    #print objFile
                    #raw_input()
                else:
                    objFile, offset, fn= findList[0]
                lastSymbol = block[2]
                

            i += 1
            basicBlockList.append({"PC":block[0],"CODE":'', 'TYPE': {}})
            


            objFile.seek(0)
            objPc = str(hex(int(block[1], 16)-offset))[2:]+":\t"
            lineNum = -1
            for line in objFile:
                if len(line.split('\t')) == 3:
                    #if pcBlockList[nowBlockNum][3] > 100 and nowBlockNum < lenPcBlockList-1 and str(hex(int(line.split(':')[0].strip(), 16)+offset))[2:] == pcBlockList[nowBlockNum+1][1]:
                        #print str(hex(int(line.split(':')[0].strip(), 16)+offset))[2:], '--', pcBlockList[nowBlockNum+1][1]
                        #
                        #i += 1
                        #basicBlockList.append({"PC":pcBlockList[nowBlockNum+1][0],"CODE":'', 'TYPE': {codeType:1}})
                        #lineNum = pcBlockList[nowBlockNum+1][3]
                    if objPc in line and lineNum == -1:
                        lineNum = block[3]
                    if lineNum > 0:
                        lineNum -= 1
                        ele = line.split("\t")
                        codeType = ele[2].split(" ")[0]
                        basicBlockList[i]["CODE"] = basicBlockList[i]["CODE"] + line

                        if not basicBlockList[i].has_key("TYPE"):
                            basicBlockList[i]["TYPE"] = {codeType:1}
                        else:
                            if(basicBlockList[i]["TYPE"].has_key(codeType)):
                                basicBlockList[i]["TYPE"][codeType] += 1
                            else:
                                basicBlockList[i]["TYPE"][codeType] = 1
                        #print line.strip(), codeType
                    if lineNum == 0:
                        break
            #print basicBlockList[i-1]["CODE"]
            #if len(basicBlockList[i-1]["CODE"]) < 10:
            #    print basicBlockList[i-1]["CODE"], basicBlockList[i-1]["PC"]
            #    raw_input()
            #raw_input()
        nowBlockNum += 1
        if nowBlockNum % 100 == 0:
            print nowBlockNum,'/',lenPcBlockList
    #print basicBlockList
    #raw_input()
    return basicBlockList

def binSearchBlock(pc, blockList):
    print "search" ,pc, "in"
    low = 0
    high = len(blockList) - 1
    while not cmp(blockList[low]["PC"],blockList[high]["PC"]) == 0:
        mid = (low + high) >> 1
        midVal = blockList[mid]["PC"]
        if low+1 == high:
            return -1
        #print midVal, high, low
        if cmp(midVal,pc) < 0:
            low = mid
        elif cmp(midVal,pc) > 0:
            high = mid
        else:
            return mid

def saveBB2File(fn, bb):
    f = open(fn , 'w+')
    for block in bb:
        f.write("#"+block['PC']+'\n'+block['CODE']+'-\n')
        for key in block['TYPE']:
            #print block['TYPE']
            f.write(key + '@' + str(block['TYPE'][key])+'\n')
    f.close()

if __name__ == '__main__':
    bb = processBasicBlock("433.pc", "milc.obj")
    #ans = binSearchBlock("3000", bb)
    saveBB2File("433.blocklist", bb)
    #print ans, bb[ans]


