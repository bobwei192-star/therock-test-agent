# parallel build is not working for llvm part of rocm:

> **Issue #1255**
> **状态**: closed
> **创建时间**: 2020-10-08T05:48:36Z
> **更新时间**: 2020-10-19T18:18:10Z
> **关闭时间**: 2020-10-19T18:18:10Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1255

## 描述

parallel build is not working for llvm part of rocm:

Taken from https://github.com/ROCm-Developer-Tools/llvm-project
...
Running a serial build will be slow. To improve speed, try running a parallel build. That's done by default in Ninja; for make, use the option -j NNN, where NNN is the number of parallel jobs, e.g. the number of CPUs you have.
...

However using -j 8 switch is not going through full build an appears to be skipping:

[build-j8.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345553/build-j8.txt)
[build-j8-1.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345554/build-j8-1.txt)
[build.txt](https://github.com/RadeonOpenCompute/ROCm/files/5345555/build.txt)





---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2020-10-08T06:06:58Z)

How about run `cmake` to generate Makefile. Then using `make -j8`?

---

### 评论 #2 — gggh000 (2020-10-08T17:10:22Z)

make -j 8 worked. However toward the end of build I see build error as following.
Note that this error happened with both 1. cmake --build and 2. make -j8. 

Scanning dependencies of target clang
[ 90%] Building CXX object tools/clang/tools/driver/CMakeFiles/clang.dir/driver.cpp.o
[ 90%] Building CXX object tools/clang/tools/driver/CMakeFiles/clang.dir/cc1_main.cpp.o
[ 90%] Building CXX object tools/clang/tools/driver/CMakeFiles/clang.dir/cc1as_main.cpp.o
[ 90%] Building CXX object tools/clang/tools/driver/CMakeFiles/clang.dir/cc1gen_reproducer_main.cpp.o
[ 90%] Linking CXX executable ../../../../bin/clang
collect2: fatal error: ld terminated with signal 9 [Killed]
compilation terminated.
tools/clang/tools/driver/CMakeFiles/clang.dir/build.make:362: recipe for target 'bin/clang-11' failed
make[2]: *** [bin/clang-11] Error 1
make[2]: *** Deleting file 'bin/clang-11'
CMakeFiles/Makefile2:34659: recipe for target 'tools/clang/tools/driver/CMakeFiles/clang.dir/all' failed
make[1]: *** [tools/clang/tools/driver/CMakeFiles/clang.dir/all] Error 2
Makefile:151: recipe for target 'all' failed
make: *** [all] Error 2


---

### 评论 #3 — b-sumner (2020-10-08T17:13:26Z)

Try running top and watch how much free memory you have.

---

### 评论 #4 — gggh000 (2020-10-08T23:41:06Z)

Here is information from top and part of /proc/meminfo. Note that I tried on two different systems each having at least 4G/8G memory.


root@i58400-u1804:/git.co# top
top - 16:39:24 up  6:40,  2 users,  load average: 0.07, 0.02, 0.00
Tasks: 185 total,   1 running, 123 sleeping,   0 stopped,   0 zombie
%Cpu(s):  8.4 us,  0.5 sy,  0.0 ni, 88.8 id,  2.3 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 32825124 total, 31182764 free,   144548 used,  1497812 buff/cache
KiB Swap:  2097148 total,  2033200 free,    63948 used. 32279488 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  450 root      20   0       0      0      0 I   5.3  0.0   0:00.76 kworker/4:3-eve
29133 root      20   0   44220   3984   3292 R   5.3  0.0   0:00.02 top
    1 root      20   0  225568   4920   3564 S   0.0  0.0   0:02.31 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
    3 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 rcu_gp
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 rcu_par_gp
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H-kb
    7 root      20   0       0      0      0 I   0.0  0.0   0:00.41 kworker/0:1-eve
    9 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
   10 root      20   0       0      0      0 S   0.0  0.0   0:00.19 ksoftirqd/0
   11 root      20   0       0      0      0 I   0.0  0.0   0:03.67 rcu_sched
   12 root      rt   0       0      0      0 S   0.0  0.0   0:00.10 migration/0
   13 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/0
   14 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/0
   15 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/1
   16 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/1
   17 root      rt   0       0      0      0 S   0.0  0.0   0:00.42 migration/1
   18 root      20   0       0      0      0 S   0.0  0.0   0:00.19 ksoftirqd/1
   19 root      20   0       0      0      0 I   0.0  0.0   0:00.62 kworker/1:0-eve
   20 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/1:0H-kb
   21 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/2
   22 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/2
   23 root      rt   0       0      0      0 S   0.0  0.0   0:00.43 migration/2
   24 root      20   0       0      0      0 S   0.0  0.0   0:00.19 ksoftirqd/2
   26 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/2:0H-kb
   27 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/3
   28 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/3
   29 root      rt   0       0      0      0 S   0.0  0.0   0:00.43 migration/3
   30 root      20   0       0      0      0 S   0.0  0.0   0:00.17 ksoftirqd/3
   31 root      20   0       0      0      0 I   0.0  0.0   0:00.49 kworker/3:0-eve
   32 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/3:0H-kb
   33 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/4
   34 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/4
   35 root      rt   0       0      0      0 S   0.0  0.0   0:00.43 migration/4
   36 root      20   0       0      0      0 S   0.0  0.0   0:00.20 ksoftirqd/4
   38 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/4:0H-kb
   39 root      20   0       0      0      0 S   0.0  0.0   0:00.00 cpuhp/5
   40 root     -51   0       0      0      0 S   0.0  0.0   0:00.00 idle_inject/5
   41 root      rt   0       0      0      0 S   0.0  0.0   0:00.44 migration/5
root@i58400-u1804:/git.co# cat /proc/meminfo
MemTotal:       32825124 kB
MemFree:        31182148 kB
MemAvailable:   32279180 kB
Buffers:           10852 kB
Cached:          1422556 kB


---

### 评论 #5 — rkothako (2020-10-13T10:19:04Z)

Hi @gggh000 
I tried in 2 different machines and not able to reproduce the problem. Both times make successful.

Can you please share the exact steps you followed, if any.
If make -j8 throws problem, recommend to try with make -j4 also once.

I got the below output with make -j8:

[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/BreakpointPrinter.cpp.o
[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/GraphPrinters.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceBasicBlocks.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceFunctionBodies.cpp.o
[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/NewPMDriver.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceFunctions.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceGlobalVars.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceInstructions.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceMetadata.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/deltas/ReduceOperandBundles.cpp.o
[ 98%] Building CXX object tools/llvm-reduce/CMakeFiles/llvm-reduce.dir/llvm-reduce.cpp.o
[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/PassPrinters.cpp.o
[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/PrintSCC.cpp.o
[ 98%] Building CXX object tools/opt/CMakeFiles/opt.dir/opt.cpp.o
[ 98%] Linking CXX executable ../../bin/llvm-reduce
[ 98%] Built target bugpoint
Scanning dependencies of target BugpointPasses
[100%] Building CXX object tools/bugpoint-passes/CMakeFiles/BugpointPasses.dir/TestPasses.cpp.o
[100%] Linking CXX executable ../../bin/opt
[100%] Built target llvm-reduce
[100%] Linking CXX shared module ../../lib/BugpointPasses.so
[100%] Built target dsymutil
[100%] Built target BugpointPasses
[100%] Built target llvm-isel-fuzzer
[100%] Built target llvm-opt-fuzzer
[100%] Built target llvm-lto2
[100%] Built target opt
master@ixt-rack-105:~/llvm-project/llvm/build$


---

### 评论 #6 — gggh000 (2020-10-19T18:18:10Z)

It appears building in VM guest env is problem. I am able to build on host server so this is no longer issue, can close. Thanks., 

---
