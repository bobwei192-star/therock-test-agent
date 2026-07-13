# Problem running simplest program

- **Issue #:** 50
- **State:** closed
- **Created:** 2016-11-16T18:16:44Z
- **Updated:** 2016-11-20T00:25:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/50

I have a test program that worked with ROCm 1.2 and which now fail with ROCm 1.3.

I upgraded to ROCm 1.3 using the instructions at https://github.com/RadeonOpenCompute/ROCm, being careful to uninstall previous version - even rebooted after each kernel change.

Just for the heck of it I also installed hcc_hsail. The problem is identical whether symlink /opt/rocm/hcc points to /opt/rocm/hcc-lc or to /opt/rocm/hcc-hsail.

It'd be great to have v1.3 work as I have been waiting to try out an RX470 that's still sitting in it's retail box...

Basically it looks like something fails in the program setup phase before main() is executed.

Minimal code that demonstrates problem:

> #include \<iostream\>
> #include \<hc.hpp\>
> using namespace hc;
> using namespace std;
> 
> int main(int argc, char **argv) {
>    return 0;
> }

> $ hcc \`hcc-config --cxxflags\` -c detect.cpp
> $ hcc \`hcc-config --ldflags\` detect.o
> $ ./a.out

> \#\#\# HCC STATUS_CHECK Error: HSA_STATUS_ERROR_INCOMPATIBLE_ARGUMENTS (0x100d) at file:/home/scchan/code/github/radeonopencompute/hcc.1.3/hcc/lib/hsa/mcwamp_hsa.cpp line:2504
> Aborted (core dumped)
> 

System/environment is:
--------------------------
Ubuntu 16.04, AMD A8-7600 APU, no AIB video card.

$uname -a
Linux quad 4.6.0-kfd-compute-rocm-rel-1.3-63 #1 SMP Fri Oct 28 13:14:45 CDT 2016 x86_64 x86_64 x86_64 GNU/Linux

$ echo $PATH
/opt/rocm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

$ echo $LD_LIBRARY_PATH
/opt/rocm/lib


$ head /proc/cpuinfo
processor       : 0
vendor_id       : AuthenticAMD
cpu family      : 21
model           : 48
model name      : AMD A8-7600 Radeon R7, 10 Compute Cores 4C+6G
stepping        : 1
microcode       : 0x6003104
cpu MHz         : 1400.000
cache size      : 2048 KB
physical id     : 0
