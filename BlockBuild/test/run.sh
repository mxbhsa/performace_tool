#!/bin/bash


as ./section.asm -o section.o
ld ./section.o -o section.exe


runtime=10
i=0

while [ $i -lt $runtime ]
do
	i=$(($i+1))
	rapl -s 0.2 -f rapl_$i.log -c 0,10 &
	pid=$!
	
	for j in {0..20}
	do
		if [ "$j" = 19 ];
		then
			taskset -c $j ./section.exe
		else
			taskset -c $j ./section.exe &
		fi
		echo "now pid $j"
	done
	kill -9  $pid
done
