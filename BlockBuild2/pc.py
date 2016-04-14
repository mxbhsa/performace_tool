import   commands

objList = ['milc.obj','libc.so.6.obj','libm.so.6.obj','ld-linux.obj']

def getObjandOffset(pcFn, symbol):
    objFn = ''
    searchCmd = 'cat ' + obj + ' | grep  \''+ symbol + '>:\''
    if symbol == '':
        searchCmd = 'cat ' + obj + ' | grep  \'0000'+  + '>:\''
    for obj in objList:
        a,b = commands.getstatusoutput()
        if a == 0:
            print a, b
        objFn = obj

    objFh = open (objFn, 'r')
    pcFh = open (pcFn, 'r')
    for line in pcFh:
        pass 

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
    pcBlockDic = []
    for line in fblock:
        ele = line.split(":")
        pcBlockDic.append((ele[1],ele[2]))
        

    basicBlockList = []

    for line in fobj:
        ele = line.split("\t")
        if len(ele) != 3:
            continue
        flag = ele[0].replace(" ","").replace(":","") == pcBlockDic[i+1][1]
        codeType = ele[2].split(" ")[0]
        if flag:
            #if i > -1:
                #print basicBlockList[i]
            basicBlockList.append({"PC":pcBlockDic[i+1][1],"CODE":line})
            i = i+1
            basicBlockList[i]["TYPE"] = {codeType:1}
            #raw_input()
        else:
            basicBlockList[i]["CODE"] = basicBlockList[i]["CODE"] + line
            if(basicBlockList[i]["TYPE"].has_key(codeType)):
                basicBlockList[i]["TYPE"][codeType] += 1
            else:
                basicBlockList[i]["TYPE"][codeType] = 1

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


if __name__ == '__main__':
    bb = processBasicBlock("bbv.pc", "bb.obj")
    ans = binSearchBlock("405013", bb)
    print ans, bb[ans]


