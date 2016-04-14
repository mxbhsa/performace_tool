import sys

fp = open(sys.argv[1])

powerDomain = 0
PKGPower = []
PKGAvg = 0.0
PP0Power = []
PP0Avg = 0.0
DRAMPower = []

for line in fp:
        if "Power consumed" in line:
                if powerDomain == 0:
                        PKGAvg = PKGAvg + float(line.split(" ")[2])
                        PKGPower.append(float(line.split(" ")[2]))
                elif powerDomain == 1:
                        PP0Avg = PP0Avg + float(line.split(" ")[2])
                        PP0Power.append(float(line.split(" ")[2]))
                else:
                        DRAMPower.append(float(line.split(" ")[2]))
                powerDomain = (powerDomain +1) %3
PP0Avg = PP0Avg / float(len(PP0Power))
PKGAvg = PKGAvg / float(len(PP0Power))

print PKGAvg, PP0Avg
