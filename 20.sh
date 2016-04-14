#!/bin/bash
rapl -s 0.2  &
benchmarklist=(
400.perlbench 
416.gamess 
435.gromacs 
445.gobmk 
454.calculix 
462.libquantum 
471.omnetpp 
483.xalancbmk 
401.bzip2 
429.mcf 
436.cactusADM 
447.dealII 
456.hmmer 
464.h264ref 
473.astar 
998.specrand 
403.gcc 
433.milc 
437.leslie3d 
450.soplex 
458.sjeng 
465.tonto 
481.wrf 
999.specrand 
410.bwaves 
434.zeusmp 
444.namd 
453.povray 
459.GemsFDTD 
470.lbm 
482.sphinx3 
)

echo ${#array_name[@]}
rapl_pid=$!
taskset -c 0   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid0=$!
taskset -c 1   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid1=$!
taskset -c 2   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid2=$!
taskset -c 3   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid3=$!
taskset -c 4   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid4=$!
taskset -c 5   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid5=$!
taskset -c 6   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid6=$!
taskset -c 7   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid7=$!
taskset -c 8   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid8=$!
taskset -c 9   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid9=$!
taskset -c 10   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid10=$!
taskset -c 11   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid11=$!
taskset -c 12   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid12=$!
taskset -c 13   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid13=$!
taskset -c 14   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid14=$!
taskset -c 15   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid15=$!
taskset -c 16   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid16=$!
taskset -c 17   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid17=$!
taskset -c 18   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1  &
my_pid18=$!
taskset -c 19   /home/zhihui/SPEC/spec2k6-v1.1/bin/runspec --config=my.cfg --nobuild --action onlyrun --size=test --noreportable --iterations=1 $1
kill ${rapl_pid}
kill ${my_pid0}
kill ${my_pid1}
kill ${my_pid2}
kill ${my_pid3}
kill ${my_pid4}
kill ${my_pid5}
kill ${my_pid6}
kill ${my_pid7}
kill ${my_pid8}
kill ${my_pid9}
kill ${my_pid10}
kill ${my_pid11}
kill ${my_pid12}
kill ${my_pid13}
kill ${my_pid14}
kill ${my_pid15}
kill ${my_pid16}
kill ${my_pid17}
kill ${my_pid18}