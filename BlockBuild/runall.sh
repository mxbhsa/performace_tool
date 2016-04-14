#!/bin/bash

rm  -r ./ans
mkdir ans



asmNum=0
nowNum=0
function plotFile()
{       
        as $1$2 -o ./section.o
        ld ./section.o -o section.exe

        
        runtime=10
        i=0
        return
        while [ $i -lt $runtime ]
        do      
                i=$(($i+1)) 
                rapl -s 0.2 -f $1rapl_$i.log -c 0,10 &
                pid=$!
                
                for j in {0..19}
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
}

function countDir()
{
    for file in `ls $1`
    do
        if [ -d $1"/"$file ]
        then
            countDir $1"/"$file
        else
            if echo "$file" | grep -q ".asm$"
            then
                asmNum=$(($asmNum+1))
            fi
        fi
    done
}

function plotDir()
{

    for file in `ls $1`
    do
        if [ -d $1"/"$file ]
        then
            plotDir $1"/"$file
        else
            nowNum=$(($nowNum+1))
            echo "cat"$1"/"$file"--$nowNum/$asmNum"
            if echo "$file" | grep -q ".asm$"
            then
                plotFile $1"/" $file
            fi
        fi
    done
}

countDir .
echo "File Num:\n$asmNum\n"
#plotDir .
echo "haha"