# Memory access fault by GPU with ROCm 3.3

> **Issue #1103**
> **状态**: closed
> **创建时间**: 2020-05-08T13:59:31Z
> **更新时间**: 2021-03-04T09:59:05Z
> **关闭时间**: 2021-03-04T09:59:05Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1103

## 描述

Mfakto is a trial factoring program: https://github.com/preda/mfakto
Parameters are -d 02 second GPU, --perftest 1 do a performance test once.
to compile go to ./mfakto/src and do 'make'


```
 ./mfakto -d 02 --perftest 1
mfakto 0.15pre6 (64bit build)


Runtime options
  Inifile                   mfakto.ini
  Verbosity                 1
  SieveOnGPU                yes
  MoreClasses               yes
  GPUSievePrimes            81157
  GPUSieveProcessSize       24Ki bits
  GPUSieveSize              96Mi bits
  FlushInterval             0
  WorkFile                  worktodo.txt
  ResultsFile               results.txt
  Checkpoints               enabled
  CheckpointDelay           300s
  Stages                    enabled
  StopAfterFactor           class
  PrintMode                 compact
  V5UserID                  none
  ComputerID                none
  TimeStampInResults        yes
  VectorSize                2
  GPUType                   AUTO
  SmallExp                  no
  UseBinfile                
Select device - Get device info:
WARNING: Unknown GPU name, assuming GCN. Please post the device name "gfx900 (Advanced Micro Devices, Inc.)" to http://www.mersenneforum.org/showthread.php?t=15646 to have it added to mfakto. Set GPUType in mfakto.ini to select a GPU type yourself to avoid this warning.

OpenCL device info
  name                      gfx900 (Advanced Micro Devices, Inc.)
  device (driver) version   OpenCL 2.0  (3098.0 (HSA1.1,LC))
  maximum threads per block 1024
  maximum threads per grid  1073741824
  number of multiprocessors 64 (4096 compute elements)
  clock rate                1630MHz

Automatic parameters
  threads per grid          2097152
  optimizing kernels for    GCN

Compiling kernels.


Perftest

Generate list of the first 1075766 primes: 115.81 ms

1. CPU-Sieve-Init (once per class, 960 times per test, avg. for 1 iterations)
	Init_class(sieveprimes=   5000):     0.40 ms
	Init_class(sieveprimes=  20000):     1.66 ms
	Init_class(sieveprimes=  80000):     7.17 ms
	Init_class(sieveprimes= 200000):    19.00 ms
	Init_class(sieveprimes= 500000):    50.22 ms
	Init_class(sieveprimes=1000000):   104.54 ms

2. CPU-Sieve (output rate M/s)
Sieve size is fixed at compile time, cannot test with variable sizes. Just running 3 fixed tests.

SievePrimes:     254     396     611     945    1460    2257    3487    5389    8328   12871   19890   30738   47503   73411  113449  175323  270944  418716  647083 1000000
SieveSizeLimit
    36 kiB     554.3   519.8   481.7   443.5   407.8   374.3   343.4   313.6   284.1   253.4   220.5   198.2   161.8   125.3   100.1    80.8    65.4    52.5    40.7    31.6
    36 kiB     559.6   520.8   482.0   433.5   397.9   370.7   338.0   313.3   284.3   255.6   224.8   201.5   163.4   125.8   100.7    80.6    65.2    51.6    41.2    31.6
    36 kiB     561.2   521.1   479.8   439.9   404.9   372.1   337.2   311.9   283.3   254.7   224.5   201.4   163.8   127.0   100.8    81.0    65.5    51.8    40.7    31.2

Best SieveSizeLimit for
SievePrimes:     254     396     611     945    1460    2257    3487    5389    8328   12871   19890   30738   47503   73411  113449  175323  270944  418716  647083 1000000
at kiB:           36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36
max M/s:       561.2   521.1   482.0   443.5   407.8   374.3   343.4   313.6   284.3   255.6   224.8   201.5   163.8   127.0   100.8    81.0    65.5    52.5    41.2    31.6
Survivors:    36.41%  34.06%  32.06%  30.28%  28.69%  27.27%  26.00%  24.84%  23.78%  22.82%  21.94%  21.12%  20.36%  19.66%  19.01%  18.40%  17.83%  17.29%  16.79%  16.32%
removal rate   980.0  1009.0  1021.5  1021.3  1013.5   998.3   977.4   949.0   911.1   864.6   800.1   753.0   640.7   519.0   429.2   359.1   301.8   251.3   204.2   161.8


3. Memory copy to GPU (blocks of 8388608 bytes)

  Standard copy, standard queue:
      80 MB in   18.8 ms (4469.4 MB/s) (real)

  Standard copy, profiled queue:
      80 MB in   18.5 ms (4544.5 MB/s) (real)
      80 MB in   18.4 ms (4550.3 MB/s) (profiled data)
       8 MB in    1.7 ms (4885.5 MB/s) (profiled data, peak)

  Standard copy, two queues:
      80 MB in   17.2 ms (4884.8 MB/s) (real)

Reinitializing with gpu_sieving enabled.
Select device - Get device info:

OpenCL device info
  name                      gfx900 (Advanced Micro Devices, Inc.)
  device (driver) version   OpenCL 2.0  (3098.0 (HSA1.1,LC))
  maximum threads per block 1024
  maximum threads per grid  1073741824
  number of multiprocessors 64 (4096 compute elements)
  clock rate                1630MHz

Automatic parameters
  threads per grid          2097152
  optimizing kernels for    GCN

Compiling kernels.

4. GPU sieve, 1 iterations each
  GPUSievePrimes (adjusted) 52534
  GPUsieve minimum exponent 646182

 gpusieve_init: 31.683000 ms (CPU work)
 gpusieve_init_exponent: 0.077500 ms (CalcModularInverses)
Memory access fault by GPU node-2 (Agent handle: 0x5655578ffa70) on address 0x7efaf0674000. Reason: Page not present or supervisor privilege.
Aborted

```

I have found that this is an old known issue on ROCm and I would like to know if there is already a fix.


---

## 评论 (7 条)

### 评论 #1 — valeriob01 (2020-05-08T14:00:50Z)

For more information https://github.com/Bdot42/mfakto/issues/18

---

### 评论 #2 — preda (2020-05-09T06:40:54Z)

This could be application error, the app simply accessing memory out of bounds. This is the first place I would look into, the first suspect. Only after ruling out a genuine memory access fault by the app would the framework become a suspect; as is, I don't see enough material here to suspect ROCm of any wrongdoing at this point.


---

### 评论 #3 — valeriob01 (2020-05-09T08:26:20Z)

> This could be application error, the app simply accessing memory out of bounds. This is the first place I would look into, the first suspect. Only after ruling out a genuine memory access fault by the app would the framework become a suspect; as is, I don't see enough material here to suspect ROCm of any wrongdoing at this point.

Previously to posting I have searched the web for previous occurrences of the error, and there it is: https://github.com/RadeonOpenCompute/hcc/issues/1024


---

### 评论 #4 — a-repko (2020-05-11T13:34:25Z)

I have a similar error, but instead of "Memory access fault", the calculation just freezes at the same point (it freezes also during the selftest at the beginning of a normal run). However, it responds to Ctrl+C with `press ^C again to exit immediately`, and then Ctrl+C ends the program.
The error shows up when going from ROCm 3.1 to 3.3. I have Gentoo Linux with 4.19 kernel, running on a Vega embedded in APU Ryzen Pro 2700U (11 CU, gfx902). However, when I utilize an old mfakto_Kernels.elf (compiled previously by ROCm 3.1), the calculation proceeds normally.
I'm attaching here the compiled kernels if somebody is able to debug them.
[mfakto_Kernels.zip](https://github.com/RadeonOpenCompute/ROCm/files/4609869/mfakto_Kernels.zip)

---

### 评论 #5 — valeriob01 (2020-05-11T15:39:09Z)

> I have a similar error, but instead of "Memory access fault", the calculation just freezes at the same point (it freezes also during the selftest at the beginning of a normal run). However, it responds to Ctrl+C with `press ^C again to exit immediately`, and then Ctrl+C ends the program.
> The error shows up when going from ROCm 3.1 to 3.3. I have Gentoo Linux with 4.19 kernel, running on a Vega embedded in APU Ryzen Pro 2700U (11 CU, gfx902). However, when I utilize an old mfakto_Kernels.elf (compiled previously by ROCm 3.1), the calculation proceeds normally.
> I'm attaching here the compiled kernels if somebody is able to debug them.
> [mfakto_Kernels.zip](https://github.com/RadeonOpenCompute/ROCm/files/4609869/mfakto_Kernels.zip)

I have downgraded to ROCm 3.1, and the old mfakto_Kernels_3.1.elf that you posted just works fine. Thus now the suspect moves to ROCm 3.3


---

### 评论 #6 — a-repko (2020-10-09T14:17:51Z)

Just a quick recap: mfakto again works for me on ROCm 3.5.1 (APU Ryzen 7 Pro 2700U; however, here gpuowl has some problems), and also on ROCm 3.8 (R9 Nano; but segfaults on Raven Ridge, together with clinfo - but this is a different topic). So, perhaps, this issue can be closed.

---

### 评论 #7 — ROCmSupport (2021-03-04T09:59:05Z)

Thanks all.
As per the latest comment, I am closing this issue.
Feel free to open a new issue, if any, for quick responses.
Thank you.

---
