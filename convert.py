 # -*- coding: utf-8 -*-
import re, random


randomReg = ['bx','cx','dx','ax','8','si','13','14','15']
randomReg32 = ['ebx','ecx','edx','eax','r8d','esi','r13d','r14d','r15d']


def asmSmooth(asmLines):

	for line in asmLines:
		line = line.strip()

		if re.search('<.+>', line):
			continue
		#hanle memory access
		#r9 outer cycler
		#r10 black hole addr
		#r11 zero
		#rdi inner cycle counter

		#读取内存
		pt = re.compile("\(%(\w)+\),")
		pt2 = re.compile(",\(%(\w)+\)")
		newStr = pt.sub('(%r10),',line)
		newStr = pt2.sub(',(%r10)',newStr)

		#读取便偏移内存
		pt = re.compile("(0x(\w)+)\(%(\w)+\),")
		pt2 = re.compile(",(0x(\w)+)\(%(\w)+\)")
		newStr = pt.sub('0x4(%r10),',newStr)
		newStr = pt2.sub(',0x4(%r10)',newStr)

		#读取基指偏移内存
		pt = re.compile("\(%(\w)+,%(\w)+,\w\),")
		pt2 = re.compile(",\(%(\w)+,%(\w)+,[0-9]\)")
		newStr = pt.sub('(%r10,%r11,1),',newStr)
		newStr = pt2.sub(',(%r10,%r11,1)',newStr)

		#读取基指偏移内存
		pt = re.compile("(0x(\w)+)\((%(\w)+)?,%(\w)+,\w\),")
		pt2 = re.compile(",(0x(\w)+)\((%(\w)+)?,%(\w)+,[0-9]\)")
		newStr = pt.sub('0x4(%r10,%r11,1),',newStr)
		newStr = pt2.sub(',0x4(%r10,%r11,1)',newStr)

		#
		#pt = re.compile(",((\()%r(9|(11))(d)?(\)))$")
		#newStr = pt.sub(',(%r10)',newStr)

		#不要写入变量
		newReg =  randomReg[random.randint(0,len(randomReg)-1)]
		pt = re.compile(",%r(9|10|11)$")
		newStr = pt.sub(','+newReg,newStr)

		newReg =  randomReg32[random.randint(0,len(randomReg)-1)]
		pt = re.compile(",%r(9|10|11)d$")
		newStr = pt.sub(',%'+newReg,newStr)

		#防止写入变量
		newReg =  randomReg[random.randint(0,len(randomReg)-1)]
		pt = re.compile("(di)|(9(d)?)")
		newStr = pt.sub(newReg,newStr)

		print '%s' % newStr.split('\t')[2]


if __name__ == '__main__':
	f = open("convert.asm","r")
	lines = f.readlines()
	asmSmooth(lines)