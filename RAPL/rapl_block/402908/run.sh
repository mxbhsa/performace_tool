#!/bin/bash


as ./section.asm -o section.o
ld ./section.o -o section.exe


runtime=10
i=0

while [ $i -lt $runtime ]
do
	i=$(($i+1))
	rapl -s 0.2 -f rapl_$i.log &
	pid=$!

	./section.exe

	kill -9  $pid
done
