#!/bin/sh
a="hello world"
#cat "./section.asm"

if [ $# -lt 2 ];then
    cat <<ERROR
USAGE:
./testlist.sh [runtime] [program name]
ERROR
exit 0
fi

runtime=$(($1))
echo ${2##"{[^/]*/$}"}

i=0
while [ "$i" -lt "$runtime" ]
do
	i=`expr $i + 1`
	likwid-powermeter "./${2}" >> "likwid-pm_${2}_${1}"
	echo $i
done

python ./power.py "./likwid-pm_${2}_${1}"

echo "Hi,$a"
