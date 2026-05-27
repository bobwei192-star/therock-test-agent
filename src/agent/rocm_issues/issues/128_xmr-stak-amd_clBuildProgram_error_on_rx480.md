# xmr-stak-amd clBuildProgram error on rx480

> **Issue #128**
> **状态**: closed
> **创建时间**: 2017-06-15T11:00:48Z
> **更新时间**: 2018-10-11T23:40:09Z
> **关闭时间**: 2018-10-11T00:41:44Z
> **作者**: gsedej
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/128

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

I am getting clBuildProgram error when running xmr-stak-amd (opencl monero miner).
The issue is reported also here: https://github.com/fireice-uk/xmr-stak-amd/issues/48

The error is
```
[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
```
here is the full log
```
$ ./bin/xmr-stak-amd config.txt 
[2017-06-13 12:25:12] : Compiling code and initializing GPUs. This will take a while...
Profiling is not available
[2017-06-13 12:25:12] : Device 0 work size 8 / 256.
clang version 4.0 
Target: amdgcn-amd-amdhsa-opencl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
Build log:
warning: argument unused during compilation: '-I .'
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
/opt/rocm/opencl/bin/x86_64/clang[0x217c00a]
/opt/rocm/opencl/bin/x86_64/clang[0x217a3be]
/opt/rocm/opencl/bin/x86_64/clang[0x217a510]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7f19c6640390]
/opt/rocm/opencl/bin/x86_64/clang[0x13d53e4]
/opt/rocm/opencl/bin/x86_64/clang[0x13b88aa]
/opt/rocm/opencl/bin/x86_64/clang[0x1743007]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbcea]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbd83]
/opt/rocm/opencl/bin/x86_64/clang[0x20cc77f]
/opt/rocm/opencl/bin/x86_64/clang[0x598456]
/opt/rocm/opencl/bin/x86_64/clang[0x59a8a3]
/opt/rocm/opencl/bin/x86_64/clang[0x576ceb]
/opt/rocm/opencl/bin/x86_64/clang[0x8ed2ae]
/opt/rocm/opencl/bin/x86_64/clang[0x8c2ad5]
/opt/rocm/opencl/bin/x86_64/clang[0x5720bd]
/opt/rocm/opencl/bin/x86_64/clang[0x56f208]
/opt/rocm/opencl/bin/x86_64/clang[0x52326a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f19c6286830]
/opt/rocm/opencl/bin/x86_64/clang[0x5694c1]
Stack dump:
0.	Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-opencl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name t_19803_47.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu fiji -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/gsedej/git/xmr-stak-amd -ferror-limit 19 -fmessage-length 192 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -o /tmp/t_19803_47-8cf830.o -x ir /tmp/AMD_19803_32/t_19803_47.bc 
1.	Code generation
2.	Running pass 'Function Pass Manager' on module '/tmp/AMD_19803_32/t_19803_47.bc'.
3.	Running pass 'SI Fix SGPR copies' on function '@cn0'
Error: Creating the executable failed: Compiling LLVM IRs to executable
```

Can I get more log/debug?



---

## 评论 (9 条)

### 评论 #1 — gstoner (2017-06-15T12:41:28Z)

Thanks we look into it,.


On Jun 15, 2017, at 6:00 AM, gsedej <notifications@github.com<mailto:notifications@github.com>> wrote:


I am getting clBuildProgram error when running xmr-stak-amd (opencl monero miner).
The issue is reported also here: fireice-uk/xmr-stak-amd#48<https://github.com/fireice-uk/xmr-stak-amd/issues/48>

The error is

[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)


here is the full log

$ ./bin/xmr-stak-amd config.txt
[2017-06-13 12:25:12] : Compiling code and initializing GPUs. This will take a while...
Profiling is not available
[2017-06-13 12:25:12] : Device 0 work size 8 / 256.
clang version 4.0
Target: amdgcn-amd-amdhsa-opencl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
Build log:
warning: argument unused during compilation: '-I .'
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
/opt/rocm/opencl/bin/x86_64/clang[0x217c00a]
/opt/rocm/opencl/bin/x86_64/clang[0x217a3be]
/opt/rocm/opencl/bin/x86_64/clang[0x217a510]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7f19c6640390]
/opt/rocm/opencl/bin/x86_64/clang[0x13d53e4]
/opt/rocm/opencl/bin/x86_64/clang[0x13b88aa]
/opt/rocm/opencl/bin/x86_64/clang[0x1743007]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbcea]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbd83]
/opt/rocm/opencl/bin/x86_64/clang[0x20cc77f]
/opt/rocm/opencl/bin/x86_64/clang[0x598456]
/opt/rocm/opencl/bin/x86_64/clang[0x59a8a3]
/opt/rocm/opencl/bin/x86_64/clang[0x576ceb]
/opt/rocm/opencl/bin/x86_64/clang[0x8ed2ae]
/opt/rocm/opencl/bin/x86_64/clang[0x8c2ad5]
/opt/rocm/opencl/bin/x86_64/clang[0x5720bd]
/opt/rocm/opencl/bin/x86_64/clang[0x56f208]
/opt/rocm/opencl/bin/x86_64/clang[0x52326a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f19c6286830]
/opt/rocm/opencl/bin/x86_64/clang[0x5694c1]
Stack dump:
0.      Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-opencl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name t_19803_47.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu fiji -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/gsedej/git/xmr-stak-amd -ferror-limit 19 -fmessage-length 192 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -o /tmp/t_19803_47-8cf830.o -x ir /tmp/AMD_19803_32/t_19803_47.bc
1.      Code generation
2.      Running pass 'Function Pass Manager' on module '/tmp/AMD_19803_32/t_19803_47.bc'.
3.      Running pass 'SI Fix SGPR copies' on function '@cn0'
Error: Creating the executable failed: Compiling LLVM IRs to executable


Can I get more log/debug?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/128>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudpQKs9CZbg4xu9wS83maKjsezrcks5sEQ7igaJpZM4N7DVA>.



---

### 评论 #2 — gstoner (2017-06-24T19:33:40Z)

Quick update.  CQE was able to reproduce.  It was observed a slight change in an array reference in a statement ( replace  st[i + 2] by st[i + 1]) will hide the compiler crash.   We are looking at the root cause.
 


---

### 评论 #3 — gstoner (2017-07-02T17:44:39Z)

We rolled out ROCm 1.6 on Thursday here are new install instructions https://rocm.github.io/ROCmInstall.html.  I need to see if this fix made into 1.6 

---

### 评论 #4 — gsedej (2017-07-03T11:47:04Z)

The ROCm-1.6 does not fix. The error is now `segmentatio fault`.  (I did remove repo and re-pulled and rebuild)
_btw: which line did you correct (st[i +2]) in which file?_

the error output
```
$ ./xmr-stak-amd 
[2017-07-03 13:29:43] : Compiling code and initializing GPUs. This will take a while...
Profiling is not available
/usr/share/libdrm/amdgpu.ids: No such file or directory
amdgpu_device_initialize: Cannot parse ASIC IDs, 0xffffffea.[2017-07-03 13:29:43] : Device 0 work size 8 / 256.
clang version 4.0 
Target: amdgcn-amd-amdhsa-opencl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
[2017-07-03 13:29:49] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
Build log:
warning: argument unused during compilation: '-I .'
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
/opt/rocm/opencl/bin/x86_64/clang[0x2241bfa]
/opt/rocm/opencl/bin/x86_64/clang[0x223ff8e]
/opt/rocm/opencl/bin/x86_64/clang[0x22400e0]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7fa746dd0390]
/opt/rocm/opencl/bin/x86_64/clang[0x1435fb4]
/opt/rocm/opencl/bin/x86_64/clang[0x1418179]
/opt/rocm/opencl/bin/x86_64/clang[0x17c3897]
/opt/rocm/opencl/bin/x86_64/clang[0x218aaaa]
/opt/rocm/opencl/bin/x86_64/clang[0x218ab43]
/opt/rocm/opencl/bin/x86_64/clang[0x218b53f]
/opt/rocm/opencl/bin/x86_64/clang[0x58fe76]
/opt/rocm/opencl/bin/x86_64/clang[0x592303]
/opt/rocm/opencl/bin/x86_64/clang[0x56e619]
/opt/rocm/opencl/bin/x86_64/clang[0x8fd75e]
/opt/rocm/opencl/bin/x86_64/clang[0x8d0495]
/opt/rocm/opencl/bin/x86_64/clang[0x5699fd]
/opt/rocm/opencl/bin/x86_64/clang[0x566968]
/opt/rocm/opencl/bin/x86_64/clang[0x51934a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7fa746a15830]
/opt/rocm/opencl/bin/x86_64/clang[0x560c01]
Stack dump:
0.	Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-opencl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name t_6269_43.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu fiji -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/gsedej/git/xmr-stak-amd/bin -ferror-limit 19 -fmessage-length 153 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -o /tmp/t_6269_43-ebbdf3.o -x ir /tmp/AMD_6269_28/t_6269_43.bc 
1.	Code generation
2.	Running pass 'Function Pass Manager' on module '/tmp/AMD_6269_28/t_6269_43.bc'.
3.	Running pass 'SI Fix SGPR copies' on function '@cn0'
Error: Creating the executable failed: Compiling LLVM IRs to executable

```

---

### 评论 #5 — gstoner (2017-07-03T15:03:08Z)

Thanks.  I will work with the team to get this into ROCm 1.6.1 patch.  

---

### 评论 #6 — JustinTArthur (2017-07-26T07:42:55Z)

I was getting this on Vega FE. Fixed for me in rocm on master and rocm-opencl on amd-master.

---

### 评论 #7 — changpeng (2017-09-01T15:24:46Z)

Thanks for reporting the issue. The reported issue has been fixed.  However, the test is launching though without pool login unable to progress.
Need to have wallet address for this mining app.
/*
 * pool_address   - Pool address should be in the form "pool.supportxmr.com:3333". Only stratum pools are supported.
 * wallet_address - Your wallet, or pool login.
 * pool_password  - Can be empty in most cases or "x".
*/
 
[2017-09-01 14:52:07] : Starting GPU thread, no affinity.
[2017-09-01 14:52:07] : Connecting to pool pool.supportxmr.com:3333 ...
[2017-09-01 14:52:08] : Connected. Logging in...
[2017-09-01 14:52:08] : SOCKET ERROR - No login/password specified
[2017-09-01 14:52:08] : SOCKET ERROR - RECEIVE error: socket closed
[2017-09-01 14:52:08] : Pool connection lost. Waiting 10 s before retry (attempt 1).
[2017-09-01 14:52:18] : Connecting to pool pool.supportxmr.com:3333 ...
[2017-09-01 14:52:18] : Connected. Logging in...
[2017-09-01 14:52:18] : SOCKET ERROR - No login/password specified
[2017-09-01 14:52:18] : SOCKET ERROR - RECEIVE error: socket closed
[2017-09-01 14:52:18] : Pool connection lost. Waiting 10 s before retry (attempt 2).

Please retry to see whether the test can run successfully or advise on how to proceed with the login credentials. Thanks.  


---

### 评论 #8 — rhlug (2017-09-30T06:21:58Z)

@gstoner  So the "fix" allows it to compile, but breaks the cryptonight implemention.

```
# diff -Naur cryptonight.cl.orig cryptonight.cl
--- cryptonight.cl.orig	2017-09-30 01:18:28.440919272 -0500
+++ cryptonight.cl	2017-09-29 23:43:10.774085196 -0500
@@ -278,7 +278,7 @@
 			ulong tmp1 = st[i], tmp2 = st[i + 1];
 			
 			st[i] = bitselect(st[i] ^ st[i + 2], st[i], st[i + 1]);
-			st[i + 1] = bitselect(st[i + 1] ^ st[i + 3], st[i + 1], st[i + 2]);
+			st[i + 1] = bitselect(st[i + 1] ^ st[i + 3], st[i + 1], st[i + 1]);
 			st[i + 2] = bitselect(st[i + 2] ^ st[i + 4], st[i + 2], st[i + 3]);
 			st[i + 3] = bitselect(st[i + 3] ^ tmp1, st[i + 3], st[i + 4]);
 			st[i + 4] = bitselect(st[i + 4] ^ tmp2, st[i + 4], tmp1);

```


HASHRATE REPORT
| ID |   10s |   60s |   15m |
|  0 | 759.7 | 764.2 | 763.1 |
---------------------------
Totals:   759.7 764.2 763.1 H/s
Highest:  770.5 H/s
RESULT REPORT
Difficulty       : 2000
**Good results     : 0 / 551 (0.0 %)**
Pool-side hashes : 0

Top 10 best results found:
|  0 |                0 |  1 |                0 |
|  2 |                0 |  3 |                0 |
|  4 |                0 |  5 |                0 |
|  6 |                0 |  7 |                0 |
|  8 |                0 |  9 |                0 |







---

### 评论 #9 — jlgreathouse (2018-10-11T00:41:44Z)

This has been open for a while, and I think it is no longer valid. I downloaded the [latest xmr-stak release](https://github.com/fireice-uk/xmr-stak/releases/tag/2.4.7) and tested on  Polaris 10 GPU on ROCm 1.9.1. I was able to run tests for cryptonight_v7, monero7, and some others without any problems. Closing this issue -- if you believe the problem still exists, please open another and we can restart the debugging process.

---
