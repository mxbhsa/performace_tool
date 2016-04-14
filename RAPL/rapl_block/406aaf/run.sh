#!/bin/bash


as ./section.asm -o section.o
ld ./section.o -o section.exe


runtime=10
i=0

while [ $i -lt $runtime ]
do
	echo $i
	i=$(($i+1))
	rapl -s 0.2 -f rapl_$i.log &
	pid=$!

	taskset -c 0 ./section.exe &
	taskset -c 1 ./section.exe &
	taskset -c 2 ./section.exe &
        taskset -c 3 ./section.exe &
        taskset -c 4 ./section.exe &
        taskset -c 5 ./section.exe &
        taskset -c 6 ./section.exe &
        taskset -c 7 ./section.exe &
        taskset -c 8 ./section.exe &
        taskset -c 9 ./section.exe &
        taskset -c 10 ./section.exe 

	kill -9  $pid
done
