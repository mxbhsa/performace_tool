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

def getBlockCode(pcFn):
	pcFh = open (pcFn, 'r')
	ansFh = open(pcFn + ".code", 'w+')
	if :
		pass
	for line in pcFh:
		elem = line.split(":")
		line_blockID = elem[1]
		line_pc = elem[2]
		line_symbol = elem[3]
		searchCmd = 'cat ' + obj + ' | grep  \'0000'+  + '>:\''

if __name__ == '__main__':
	
	searchDynamic('4c362d0','__exp_finite','0x4c26000','libm.so.6.obj')