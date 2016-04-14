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
    low = 0
    high = len(blockList) - 1
    while cmp(blockList[low]["PC"],blockList[high]["PC"]) <= 0:
        mid = (low + high) >> 1
        midVal = blockList[mid]["PC"]
        if cmp(midVal,pc) < 0:
            low = mid
        elif cmp(midVal,pc) > 0:
            high = mid
        else:
            return mid
    return -1


if __name__ == '__main__':
    bb = processBasicBlock("bbv.pc", "bb.obj")
    ans = binSearchBlock("405013", bb)
    print ans, bb[ans]


