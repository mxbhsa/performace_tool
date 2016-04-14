 # -*- coding: utf-8 -*-
import re, random

dataSize = 2033
randomReg = ['bx','cx','dx','ax','8','si','13','14','15']
randomRegFig = ['r8','r13','r14','r15']
randomReg32 = ['ebx','ecx','edx','eax','r8d','esi','r13d','r14d','r15d']
randomRegLett = ['bx','cx','dx','ax','si']


def asmSmooth(asmLines):
	ans = ''
	if __name__ != '__main__':
		asmLines = asmLines.strip().split('\n')
	for line in asmLines:
		line = line.strip()
		if re.search('(ret)|(<.+>)', line):
			continue


		asm = line.split()
		newStr = asm[-1]
		if (len(asm[-2]) < 3 and len([x for x in asm[-2] if x > 'f']) == 0 ):
			ans = ans + (newStr+'\n')
			continue
		#hanle memory access
		#r9 outer cycler
		#r10 black hole addr
		#r11 zero
		#rdi inner cycle counter
		#读取内存
		pt = re.compile("\(%(\w)+\),")
		pt2 = re.compile(",\(%(\w)+\)")
		newStr = pt.sub('(%r10),',newStr)
		newStr = pt2.sub(',(%r10)',newStr)

		#读取便偏移内存
		pt = re.compile("(0x(\w)+)\(%(\w)+\),")
		pt2 = re.compile(",(0x(\w)+)\(%(\w)+\)")
		newStr = pt.sub(hex(random.randint(0,dataSize))+'(%r10),',newStr)
		newStr = pt2.sub(','+hex(random.randint(0,dataSize))+'(%r10)',newStr)
		#读取基指偏移内存
		pt = re.compile("\(%(\w)+,%(\w)+,\w\),")
		pt2 = re.compile(",\(%(\w)+,%(\w)+,[0-9]\)")
		newStr = pt.sub('(%r10,%r11,1),',newStr)
		newStr = pt2.sub(',(%r10,%r11,1)',newStr)

		#读取基指偏移内存
		pt = re.compile("(0x(\w)+)\((%(\w)+)?,%(\w)+,\w\),")
		pt2 = re.compile(",(0x(\w)+)\((%(\w)+)?,%(\w)+,[0-9]\)")

		newStr = pt.sub(hex(random.randint(0,dataSize))+'(%r10,%r11,1),',newStr)
		newStr = pt2.sub(','+hex(random.randint(0,dataSize))+'(%r10,%r11,1)',newStr)
		#
		#pt = re.compile(",((\()%r(9|(11))(d)?(\)))$")
		#newStr = pt.sub(',(%r10)',newStr)

		#不要写入变量
		newReg =  randomReg[random.randint(0,len(randomReg)-1)]
		pt = re.compile(",%r(9|10|11)$")
		newStr = pt.sub(',%r'+newReg,newStr)

		newReg =  randomReg32[random.randint(0,len(randomReg32)-1)]
		pt = re.compile(",%r(9|10|11)d$")
		newStr = pt.sub(',%'+newReg,newStr)

		#防止写入变量
		newReg =  randomReg32[random.randint(0,len(randomReg32)-1)]
		newStr = newStr.replace("(edi)|(r9d)", newReg)

		newReg =  randomRegFig[random.randint(0,len(randomRegFig)-1)]
		newStr = newStr.replace("r9", newReg)
		newReg =  randomRegLett[random.randint(0,len(randomRegLett)-1)]
		newStr = newStr.replace("di", newReg)

		asm = asm[-2]+ "\t" + newStr
		ans = ans+ (asm+'\n')
		#raw_input()
	print ans
	return ans

if __name__ == '__main__':
	f = open("convert.asm","r")
	lines = f.readlines()
	asmSmooth(lines)