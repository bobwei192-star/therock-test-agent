# Problem running simplest program

> **Issue #50**
> **状态**: closed
> **创建时间**: 2016-11-16T18:16:44Z
> **更新时间**: 2016-11-20T00:25:50Z
> **关闭时间**: 2016-11-17T05:06:31Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/50

## 描述

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


---

## 评论 (5 条)

### 评论 #1 — jedwards-AMD (2016-11-16T23:03:04Z)

I have reproduced this issue and opened a internal ticket on HCC development to track it.


---

### 评论 #2 — scchan (2016-11-16T23:25:13Z)

@emerth  Could you try adding --amdgpu-target=AMD:AMDGPU:7:0:0 to your link step?


---

### 评论 #3 — nabar (2016-11-16T23:30:51Z)

I had the same problem on rocm 1.2, and haven't check the rocm 1.3 yet.

I could avoid this issue for adding the following option into the linking
process.

--amdgpu-target=<GCN ISA Version>

In my case, it is
--amdgpu-target=AMD:AMDGPU:8:0:1

Best,
Nandinbaatar

On 17 Nov 2016 00:03, "James Edwards" notifications@github.com wrote:

> I have reproduced this issue and opened a internal ticket on HCC
> development to track it.
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> https://github.com/RadeonOpenCompute/ROCm/issues/50#issuecomment-261101269,
> or mute the thread
> https://github.com/notifications/unsubscribe-auth/AAY6Osdkz3DWmdAmhrZBkv8pRKxCsjboks5q-4uogaJpZM4K0P6I
> .


---

### 评论 #4 — scchan (2016-11-16T23:35:47Z)

By default, hcc generates ISA code that is compatible to Fiji, Polaris...   If you need to target a different architecture then you'll have to specify the architecture 
https://github.com/RadeonOpenCompute/hcc/wiki#compiling-for-different-gpu-architectures


---

### 评论 #5 — ghost (2016-11-17T05:02:47Z)

Adding "--amdgpu-target=AMD:AMDGPU:7:0:0", to the link commandline solved my problem. 

I had tried this option but in the compile stage, to no effect. I did not realize it was a link option.

Thanks to all of you for helping! I think this issue should be closed now, as hcc-config has no way of knowing what the user's target will be.


---
