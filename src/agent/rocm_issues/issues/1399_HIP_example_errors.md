# HIP example errors

> **Issue #1399**
> **状态**: closed
> **创建时间**: 2021-03-02T06:45:37Z
> **更新时间**: 2021-05-11T04:51:52Z
> **关闭时间**: 2021-05-11T03:14:47Z
> **作者**: dshm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1399

## 描述

I tired HIP-Example，the code tested is tag rocm-4.0.0，the environment I do the test is official docker image rocm/pytorch:rocm4.0_ubuntu18.04_py3.6_pytorch_1.7.0. 
I run the test using the following command
git clone https://github.com/ROCm-Developer-Tools/HIP-Examples.git
cd HIP-Examples
git submodule init
git submodule update
./test_all.sh 2>&1 | tee testlog

the error is shown in log below.


==== vectorAdd ====
rm -f ./vectoradd_hip.exe
rm -f vectoradd_hip.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
/opt/rocm/hip/bin/hipcc vectoradd_hip.o -o vectoradd_hip.exe
./vectoradd_hip.exe
 System minor 0
 System major 9
 agent prop name Device 6868
hip Device prop succeeded 
FAILED: 983040 errors

==== gpu-burn ====
rm -rf build
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/BurnKernel.o BurnKernel.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/common.o common.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/AmdGpuMonitor.o AmdGpuMonitor.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/gpuburn.o gpuburn.cpp  
/opt/rocm/hip/bin/hipcc -lm -lpthread -o build/gpuburn-hip build/BurnKernel.o build/common.o build/AmdGpuMonitor.o build/gpuburn.o
Total no. of GPUs found: 1
Init Burn Thread for device (0)
Temps: [GPU2: 30 C] 5s
Burn Thread using device (0)
Temps: [GPU2: 32 C] 4s
Temps: [GPU2: 33 C] 3s
Temps: [GPU2: 34 C] 2s
Temps: [GPU2: 35 C] 1s
Stopping burn thread on device (0)

==== strided-access ====
rm -f strided-access *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o strided-access benchmark-hip.cpp 
# Using device: Device 6868
# stride     time       GB/sec
   0        0.000766        313.316
   1        0.003871        61.9995
   2        0.009085        26.4172
   3        0.004068        58.9971
   4        0.005346        44.8934
   5        0.006601        36.3581
   6        0.007756        30.9438
   7        0.009054        26.5076
   8        0.00927        25.89
   9        0.008541        28.0998
   10        0.009242        25.9684
   11        0.010155        23.6337
   12        0.010995        21.8281
   13        0.011867        20.2242
   14        0.012634        18.9964
   15        0.013689        17.5323
   16        0.014515        16.5346
   17        0.015318        15.6678
   18        0.015669        15.3169
   19        0.016175        14.8377
   20        0.016574        14.4805
   21        0.016817        14.2713
   22        0.017012        14.1077
   23        0.017263        13.9026
   24        0.017474        13.7347
   25        0.01737        13.8169
   26        0.017144        13.9991
   27        0.016937        14.1702
   28        0.016727        14.3481
   29        0.01648        14.5631
   30        0.016154        14.857
   31        0.015696        15.2905
   32        0.014334        16.7434

==== rtm8 ====
Using HIP_PATH=/opt/rocm/hip
hipcc -std=c++11 -O3 -o rtm8_hip rtm8.cpp
memory (MB) = 984.096000
pts (billions) = 1.122751
Tflops = 0.075224
dt = 0.731243
pt_rate (millions/sec) = 1535.400518
flop_rate (Gflops) = 102.871835
speedup = 0.434197

==== reduction ====
rm -f reduction *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o reduction reduction.cpp 
./reduction 1024*1024*4
ARRAYSIZE: 1024
Array size: 0.00390625 MB
The average performance of reduction is 0.0249941 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 8388608
ARRAYSIZE: 8388608
Array size: 32 MB
The average performance of reduction is 28.9185 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 16777216
ARRAYSIZE: 16777216
Array size: 64 MB
The average performance of reduction is 40.6363 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 33554432
ARRAYSIZE: 33554432
Array size: 128 MB
The average performance of reduction is 62.0686 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 67108864
ARRAYSIZE: 67108864
Array size: 256 MB
The average performance of reduction is 90.4151 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 134217728
ARRAYSIZE: 134217728
Array size: 512 MB
The average performance of reduction is 144.868 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 268435456
ARRAYSIZE: 268435456
Array size: 1024 MB
The average performance of reduction is 198.619 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 536870912
ARRAYSIZE: 536870912
Array size: 2048 MB
The average performance of reduction is 262.084 GBytes/sec
VERIFICATION: result is CORRECT


==== mini-nbody ====
hipcc -I../ -DSHMOO nbody-orig.cpp -o nbody-orig
./nbody-orig 1024
1024, 1.632
./nbody-orig 2048
2048, 3.645
./nbody-orig 4096
4096, 7.330
./nbody-orig 8192
8192, 17.133
./nbody-orig 16384
16384, 30.724
./nbody-orig 32768
32768, 53.791
./nbody-orig 65536
65536, 71.070
./nbody-orig 131072
131072, 73.593
./nbody-orig 262144
262144, 77.941
./nbody-orig 524288
524288, 80.171
hipcc -I../ -DSHMOO nbody-soa.cpp -o nbody-soa
./nbody-soa 1024
1024, 1.714
./nbody-soa 2048
2048, 3.891
./nbody-soa 4096
4096, 7.852
./nbody-soa 8192
8192, 17.837
./nbody-soa 16384
16384, 31.413
./nbody-soa 32768
32768, 54.564
./nbody-soa 65536
65536, 71.204
./nbody-soa 131072
131072, 73.354
hipcc -I../ -DSHMOO nbody-block.cpp -o nbody-block
./nbody-block 1024
1024, 1.959
./nbody-block 2048
2048, 4.474
./nbody-block 4096
4096, 9.049
./nbody-block 8192
8192, 20.412
./nbody-block 16384
16384, 33.372
./nbody-block 32768
32768, 57.124
./nbody-block 65536
65536, 72.337
./nbody-block 131072
131072, 73.093

==== add4 ====
rm -f   gpu-stream-hip *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -c hip-stream.cpp -o hip-stream.o
g++ -std=c++11 -O3   -c -o common.o common.cpp
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 common.o hip-stream.o -lm -o gpu-stream-hip
./gpu-stream-hip
GPU-STREAM
Version: 1.0
Implementation: HIP
GridSize: 26214400 work-items
GroupSize: 1024 work-items
Operations/Work-item: 1
Precision: double

Running kernels 10 times
Array size: 200.0 MB (=0.2 GB) 0 bytes padding
Total size: 1000.0 MB (=1.0 GB)
Using HIP device Device 6868 (compute_units=56)
Driver: 321200
d_a=0x7fa98ce00000
d_b=0x7fa980400000
d_c=0x7fa973a00000
d_d=0x7fa967000000
d_e=0x7fa95a600000
Validation failed on a[]. Average error 28585402504.791607
Validation failed on b[]. Average error 1125853808.831025
Validation failed on c[]. Average error 9116584840.453053
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        348989.925  0.00120     0.00167     0.00144     
Mul         364966.456  0.00115     0.00168     0.00141     
Add4        350674.259  0.00299     0.00414     0.00351     
Triad       334824.314  0.00188     0.00259     0.00221     
GEOMEAN     349700.843  
double free or corruption (out)
./runhip.sh: line 2:  4752 Aborted                 (core dumped) ./gpu-stream-hip
./gpu-stream-hip --groups 256 --groupSize 256
GPU-STREAM
Version: 1.0
Implementation: HIP
GridSize: 65536 work-items
GroupSize: 256 work-items
Operations/Work-item: 400
Using looper kernels:
Precision: double

Running kernels 10 times
Array size: 200.0 MB (=0.2 GB) 0 bytes padding
Total size: 1000.0 MB (=1.0 GB)
Using HIP device Device 6868 (compute_units=56)
Driver: 321200
d_a=0x7f84a8e00000
d_b=0x7f849c400000
d_c=0x7f848fa00000
d_d=0x7f8483000000
d_e=0x7f8476600000
Validation failed on a[]. Average error 14910550383.854282
Validation failed on b[]. Average error 686501130.270962
Validation failed on c[]. Average error 4723058054.589461
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        347347.752  0.00121     0.00168     0.00147     
Mul         366428.048  0.00114     0.00168     0.00140     
Add4        340854.118  0.00308     0.00427     0.00360     
Triad       333259.669  0.00189     0.00262     0.00222     
GEOMEAN     346757.711  
double free or corruption (out)
./runhip.sh: line 4:  4756 Aborted                 (core dumped) ./gpu-stream-hip --groups 256 --groupSize 256
./gpu-stream-hip --float
GPU-STREAM
Version: 1.0
Implementation: HIP
Warning: If number of iterations set >= 8, expect rounding errors with single precision
GridSize: 26214400 work-items
GroupSize: 1024 work-items
Operations/Work-item: 1
Precision: float

Running kernels 10 times
Array size: 100.0 MB (=0.1 GB) 0 bytes padding
Total size: 500.0 MB (=0.5 GB)
Using HIP device Device 6868 (compute_units=56)
Driver: 321200
d_a=0x7f0ba6600000
d_b=0x7f0ba0000000
d_c=0x7f0b99a00000
d_d=0x7f0b93400000
d_e=0x7f0b8ce00000
Validation failed on a[]. Average error 59642165028.980003
Validation failed on b[]. Average error 2745978952.442500
Validation failed on c[]. Average error 18892199786.830002
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        250834.500  0.00084     0.00085     0.00085     
Mul         250559.686  0.00084     0.00085     0.00084     
Add4        248292.859  0.00211     0.00218     0.00214     
Triad       235879.947  0.00133     0.00138     0.00135     
GEOMEAN     246313.621  
munmap_chunk(): invalid pointer
./runhip.sh: line 6:  4760 Aborted                 (core dumped) ./gpu-stream-hip --float
./gpu-stream-hip --float --groups 256 --groupSize 256
GPU-STREAM
Version: 1.0
Implementation: HIP
Warning: If number of iterations set >= 8, expect rounding errors with single precision
GridSize: 65536 work-items
GroupSize: 256 work-items
Operations/Work-item: 400
Using looper kernels:
Precision: float

Running kernels 10 times
Array size: 100.0 MB (=0.1 GB) 0 bytes padding
Total size: 500.0 MB (=0.5 GB)
Using HIP device Device 6868 (compute_units=56)
Driver: 321200
d_a=0x7f1ada600000
d_b=0x7f1ad4000000
d_c=0x7f1acda00000
d_d=0x7f1ac7400000
d_e=0x7f1ac0e00000
Validation failed on a[]. Average error 57170805090.419998
Validation failed on b[]. Average error 2251706768.122500
Validation failed on c[]. Average error 18233170426.189999
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        266392.291  0.00079     0.00081     0.00080     
Mul         265744.506  0.00079     0.00081     0.00080     
Add4        248175.093  0.00211     0.00216     0.00214     
Triad       300506.396  0.00105     0.00133     0.00129     
GEOMEAN     269556.287  
munmap_chunk(): invalid pointer
./runhip.sh: line 8:  4764 Aborted                 (core dumped) ./gpu-stream-hip --float --groups 256 --groupSize 256

==== cuda-stream ====
rm -f stream *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o stream stream.cpp 
 STREAM Benchmark implementation in HIP
 Array size (double precision) = 536.87 MB
 using 192 threads per block, 349526 blocks
 output in IEC units (KiB = 1024 B)

Function      Rate (GiB/s)  Avg time(s)  Min time(s)  Max time(s)
-----------------------------------------------------------------
Copy:         354.2486      0.00294810   0.00282288   0.00406599
Scale:        354.3384      0.00295042   0.00282216   0.00399494
Add:          332.8108      0.00462769   0.00450706   0.00618815
Triad:        333.1810      0.00460458   0.00450206   0.00568986

==== Rodinia ====
[0;35m--CLEAN: nw[0m
[0;35m--CLEAN: gaussian[0m
[0;35m--CLEAN: myocyte[0m
[0;35m--CLEAN: hybridsort[0m
[0;35m--CLEAN: hotspot[0m
[0;35m--CLEAN: nn[0m
[0;35m--CLEAN: pathfinder[0m
[0;35m--CLEAN: streamcluster[0m
[0;35m--CLEAN: kmeans[0m
[0;35m--CLEAN: heartwall[0m
[0;35m--CLEAN: bfs[0m
[0;35m--CLEAN: b+tree[0m
[0;35m--CLEAN: dwt2d[0m
[0;35m--CLEAN: lud[0m
[0;35m--CLEAN: srad[0m
[0;35m--CLEAN: backprop[0m
[0;35m--CLEAN: lavaMD[0m
[0;35m--CLEAN: cfd[0m
[0;35m--TESTING: nw[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:101: recipe for target 'needle_hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: gaussian[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:11: recipe for target 'gaussian.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: myocyte[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:37: recipe for target 'main.hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: hybridsort[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:16: recipe for target 'bucketsort.hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: hotspot[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:7: recipe for target 'hotspot.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: nn[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:14: recipe for target 'nn.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: pathfinder[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:103: recipe for target 'pathfinder.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: streamcluster[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:111: recipe for target 'streamcluster_hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: kmeans[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:29: recipe for target 'kmeans_cuda.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: heartwall[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:11: recipe for target 'main.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: bfs[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:11: recipe for target 'bfs.hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: b+tree[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:115: recipe for target 'main.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: dwt2d[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:24: recipe for target 'main.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: lud[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:18: recipe for target 'lud_kernel.hip.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: srad[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:21: recipe for target 'main.o' failed
Makefile:6: recipe for target 'SRAD_V1' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: backprop[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:23: recipe for target 'backprop_cuda.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: lavaMD[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:43: recipe for target 'kernel/kernel_gpu_cuda_wrapper.o' failed
[0;31mBUILD FAILURE!![0m
[0;35m--TESTING: cfd[0m
error: unknown HIP_PLATFORM = 'clang'       or HIP_COMPILER = 'clang'Makefile:14: recipe for target 'euler3d.o' failed
[0;31mBUILD FAILURE!![0m

the card I use is [AMD/ATI] Vega 10 [Radeon PRO WX 8100], rocminfo is shown below
Agent 3
Name: gfx900
Uuid: GPU-021544ce42504164
Marketing Name: Device 6868
Vendor Name: AMD
Feature: KERNEL_DISPATCH
Profile: BASE_PROFILE
Float Round Mode: NEAR
Max Queue Number: 128(0x80)
Queue Min Size: 4096(0x1000)
Queue Max Size: 131072(0x20000)
Queue Type: MULTI
Node: 2
Device Type: GPU
Cache Info:
L1: 16(0x10) KB
Chip ID: 26728(0x6868)
Cacheline Size: 64(0x40)
Max Clock Freq. (MHz): 1500
BDFID: 15616
Internal Node ID: 2
Compute Unit: 56
SIMDs per CU: 4
Shader Engines: 4
Shader Arrs. per Eng.: 1
WatchPts on Addr. Ranges:4
Features: KERNEL_DISPATCH
Fast F16 Operation: FALSE
Wavefront Size: 64(0x40)
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Max Waves Per CU: 40(0x28)
Max Work-item Per CU: 2560(0xa00)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 4294967295(0xffffffff)
y 4294967295(0xffffffff)
z 4294967295(0xffffffff)
Max fbarriers/Workgrp: 32
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 8372224(0x7fc000) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Alignment: 4KB
Accessible by all: FALSE
Pool 2
Segment: GROUP
Size: 64(0x40) KB
Allocatable: FALSE
Alloc Granule: 0KB
Alloc Alignment: 0KB
Accessible by all: FALSE
ISA Info:
ISA 1
Name: amdgcn-amd-amdhsa--gfx900
Machine Models: HSA_MACHINE_MODEL_LARGE
Profiles: HSA_PROFILE_BASE
Default Rounding Mode: NEAR
Default Rounding Mode: NEAR
Fast f16: TRUE
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 4294967295(0xffffffff)
y 4294967295(0xffffffff)
z 4294967295(0xffffffff)
FBarrier Max Size: 32

I run the test mainly because I get memory access fault error when running pytorch-example using rocm/pytorch on AMD GPU, and I push an issue in corresponding github, then I get an answer as below
“Hi @dshm , from your description the issue should be system configuration related.
I'd suggest you to create an issue in the ROCm repo and use HIP examples to reproduce the issue:
https://github.com/ROCm-Developer-Tools/HIP-Examples
https://github.com/RadeonOpenCompute/ROCm/issues
Once you're able to execute the HIP examples, please reopen the this issue and we can try PyTorch from there, thanks.”
the link to the issus is https://github.com/ROCmSoftwarePlatform/pytorch/issues/797

Could someone please help me to solve the errors in HIP-Example? or give me some advice? Thanks a lot!

---

## 评论 (21 条)

### 评论 #1 — ROCmSupport (2021-03-02T07:02:25Z)

Thanks @dshm for reaching out.
Can you please share the output for below commands to understand the problem better.
_/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
/opt/rocm/bin/rocm-smi -a
dmesg_

Thank you.

---

### 评论 #2 — dshm (2021-03-02T07:39:25Z)

the information you need is shown below, thanks a lot!

root@ACT103:/var/lib/jenkins# /opt/rocm/bin/rocminfo                            
ROCk module is loaded                            
Able to open /dev/kfd read-write                                                                         
=====================                                                                    
HSA System Attributes                                                           
=====================                                       
Runtime Version:         1.1                                                    
System Timestamp Freq.:  1000.000000MHz                                         
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)                
Machine Model:           LARGE                                                                        
System Endianness:       LITTLE                                                 
                                                                 
==========                                                                      
HSA Agents                                                                      
==========                                                                      
*******                                                                         
Agent 1                                                                         
*******                                                                         
  Name:                    Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz             
  Uuid:                    CPU-XX                                               
  Marketing Name:          Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz                                                 
  Vendor Name:             CPU                                                  
  Feature:                 None specified                                       
  Profile:                 FULL_PROFILE                                         
  Float Round Mode:        NEAR                                                 
  Max Queue Number:        0(0x0)                                               
  Queue Min Size:          0(0x0)                                               
  Queue Max Size:          0(0x0)                                               
  Queue Type:              MULTI                                                                           
  Node:                    0                                                    
  Device Type:             CPU                                                                                 
  Cache Info:                                                                   
    L1:                      32768(0x8000) KB                                   
  Chip ID:                 0(0x0)                                               
  Cacheline Size:          64(0x40)                                                                            
  Max Clock Freq. (MHz):   0                                                    
  BDFID:                   0                                                    
  Internal Node ID:        0                                                    
  Compute Unit:            40                                                                                  
  SIMDs per CU:            0                                                    
  Shader Engines:          0                                                    
  Shader Arrs. per Eng.:   0                                                    
  WatchPts on Addr. Ranges:1                                                                                   
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    388737852(0x172bab3c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    388737852(0x172bab3c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        1
  Compute Unit:            40
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    390133660(0x1740f79c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    390133660(0x1740f79c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 3
*******
  Name:                    gfx900
  Uuid:                    GPU-021544ce42504164
  Marketing Name:          Device 6868
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 26728(0x6868)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1500
  BDFID:                   15616
  Internal Node ID:        2
  Compute Unit:            56
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224(0x7fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***



root@ACT103:/var/lib/jenkins# /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1             
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3212.0) 
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback
                                                           
                                                                                                                                                      
  Platform Name:                                 AMD Accelerated Parallel Processing                                                                  Number of devices:                               1                                                                                                      Device Type:                                   CL_DEVICE_TYPE_GPU  Vendor ID:                                     1002h
  Board name:                                    Device 6868
  Device Topology:                               PCI[ B#61, D#0, F#0 ]
  Max compute units:                             56
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1500Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183768
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    26728
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8573157376
  Constant buffer size:                          7287183768
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216472
  Max global variable size:                      7287183768
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f580820bcf0
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3212.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_
base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressabl
e_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_
khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program



root@ACT103:/var/lib/jenkins# /opt/rocm/bin/rocm-smi -a                                                                                               
                                                                                                                                                      
                                                                                                                                                      
======================= ROCm System Management Interface =======================                                                                      
========================= Version of System Component ==========================                                                                      
Driver version: 5.6.19                                                                                                                                
================================================================================                                                                      
====================================== ID ======================================                                                                      
GPU[0]          : GPU ID: 0x6868                                                                                                                      
================================================================================                                                                      
================================== Unique ID ===================================                                                                      
GPU[0]          : Unique ID: 0x21544ce42504164                                                                                                        
================================================================================                                                                      
==================================== VBIOS =====================================                                                                      
GPU[0]          : VBIOS version: 113-D0511100-109                                                                                                     
================================================================================                                                                      
================================= Temperature ==================================                                                                      
GPU[0]          : Temperature (Sensor edge) (C): 21.0                                                                                                 
GPU[0]          : Temperature (Sensor junction) (C): 22.0                                                                                             
GPU[0]          : Temperature (Sensor memory) (C): 30.0                                                                                               
================================================================================                                                                      
========================== Current clock frequencies ===========================                                                                      
GPU[0]          : dcefclk clock level: 0: (600Mhz)                                                                                                    
GPU[0]          : mclk clock level: 0: (167Mhz)                                                                                                       
GPU[0]          : sclk clock level: 3: (1269Mhz)                                                                                                      
GPU[0]          : socclk clock level: 3: (960Mhz)                                                                                                     
GPU[0]          : pcie clock level: 1 (8.0GT/s x16)                                                                                                   
================================================================================                                                                      
============================== Current Fan Metric ==============================                                                                      
GPU[0]          : Fan Level: 38 (15%)                                                                                                                 
GPU[0]          : Fan RPM: 754                                                                                                                        
================================================================================                                                                      
============================ Show Performance Level ============================                                                                      
GPU[0]          : Performance Level: auto
================================================================================
=============================== OverDrive Level ================================
ERROR: GPU[0]           : Unable to retrieve mclk OverDrive level
================================== Power Cap ===================================
GPU[0]          : Max Graphics Package Power (W): 170.0
================================================================================
============================= Show Power Profiles ==============================
GPU[0]          : 1. Available power profile (#1 of 7): CUSTOM
GPU[0]          : 2. Available power profile (#2 of 7): VIDEO
GPU[0]          : 3. Available power profile (#3 of 7): POWER SAVING
GPU[0]          : 4. Available power profile (#4 of 7): COMPUTE
GPU[0]          : 5. Available power profile (#5 of 7): VR
GPU[0]          : 6. Available power profile (#6 of 7): 3D FULL SCREEN
GPU[0]          : 7. Available power profile (#7 of 7): BOOTUP DEFAULT*
================================================================================
============================== Power Consumption ===============================
GPU[0]          : Average Graphics Package Power (W): 12.0
================================================================================
========================= Supported clock frequencies ==========================
GPU[0]          : Supported dcefclk frequencies on GPU0
GPU[0]          : 0: 600Mhz *
GPU[0]          : 1: 720Mhz
GPU[0]          : 2: 847Mhz
GPU[0]          : 3: 900Mhz
GPU[0]          :
GPU[0]          : Supported mclk frequencies on GPU0
GPU[0]          : 0: 167Mhz *
GPU[0]          : 1: 500Mhz
GPU[0]          : 2: 700Mhz
GPU[0]          : 3: 1000Mhz
GPU[0]          :
GPU[0]          : Supported sclk frequencies on GPU0
GPU[0]          : 0: 852Mhz
GPU[0]          : 1: 991Mhz
GPU[0]          : 2: 1138Mhz
GPU[0]          : 3: 1269Mhz *
GPU[0]          : 4: 1348Mhz
GPU[0]          : 5: 1399Mhz
GPU[0]          : 6: 1440Mhz
GPU[0]          : 7: 1500Mhz
GPU[0]          :
GPU[0]          : Supported socclk frequencies on GPU0
GPU[0]          : 0: 600Mhz
GPU[0]          : 1: 720Mhz
GPU[0]          : 2: 847Mhz
GPU[0]          : 3: 960Mhz *
GPU[0]          : 4: 1028Mhz
GPU[0]          : 5: 1107Mhz
GPU[0]          :
GPU[0]          : Supported PCIe frequencies on GPU0
GPU[0]          : 0: 8.0GT/s x16
GPU[0]          : 1: 8.0GT/s x16 *
GPU[0]          :
--------------------------------------------------------------------------------
================================================================================
============================== % time GPU is busy ==============================
GPU[0]          : GPU use (%): 0
================================================================================
============================== Current Memory Use ==============================
ERROR: 2 GPU[0]: % memory use: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
================================================================================
================================ Memory Vendor =================================
GPU[0]          : GPU memory vendor: hynix
================================================================================
============================= PCIe Replay Counter ==============================
GPU[0]          : PCIe Replay Count: 0
================================================================================
================================ Serial Number =================================
GPU[0]          : Serial Number: N/A
================================================================================
================================ KFD Processes =================================
No KFD PIDs currently running
================================================================================
============================= GPUs Indexed by PID ==============================
No KFD PIDs currently running
================================================================================
================== GPU Memory clock frequencies and voltages ===================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
================================================================================
=============================== Current voltage ================================
GPU[0]          : Voltage (mV): 987
================================================================================
================================== PCI Bus ID ==================================
GPU[0]          : PCI Bus: 0000:3D:00.0
================================================================================
============================= Firmware Information =============================
GPU[0]          : ASD firmware version:         1446554
GPU[0]          : CE firmware version:          74
GPU[0]          : DMCU firmware version:        0
GPU[0]          : MC firmware version:          0
GPU[0]          : ME firmware version:          148
GPU[0]          : MEC firmware version:         352
GPU[0]          : MEC2 firmware version:        352
GPU[0]          : PFP firmware version:         164
GPU[0]          : RLC firmware version:         88
GPU[0]          : RLC SRLC firmware version:    0
GPU[0]          : RLC SRLG firmware version:    0
GPU[0]          : RLC SRLS firmware version:    0
GPU[0]          : SDMA firmware version:        407
GPU[0]          : SDMA2 firmware version:       407
GPU[0]          : SMC firmware version:         00.28.40.00
GPU[0]          : SOS firmware version:         0x00161a92
GPU[0]          : TA RAS firmware version:      00.00.00.00
GPU[0]          : TA XGMI firmware version:     00.00.00.00
GPU[0]          : UVD firmware version:         0x01571100
GPU[0]          : VCE firmware version:         0x352d0400
GPU[0]          : VCN firmware version:         0x00000000
================================================================================
================================= Product Info =================================
GPU[0]          : Card series:          0x1002
GPU[0]          : Card model:           0x1002
GPU[0]          : Card vendor:          0x1002
GPU[0]          : Card SKU:             D05111
================================================================================
================================== Pages Info ==================================
ERROR: 2 GPU[0]: ras: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
============================ Show Valid sclk Range =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display sclk range
================================================================================
============================ Show Valid mclk Range =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display mclk range
================================================================================
=========================== Show Valid voltage Range ===========================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Unable to display voltage range
================================================================================
============================= Voltage Curve Points =============================
ERROR: 2 GPU[0]: od volt: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.
GPU[0]          : Voltage Curve is not supported
================================================================================
WARNING:                 One or more commands failed
============================= End of ROCm SMI Log ==============================


---

### 评论 #3 — dshm (2021-03-02T07:40:17Z)

root@ACT103:/var/lib/jenkins/HIP-Examples# dmesg 2>&1 | tee  dmesgnewlog
[    0.000000] microcode: microcode updated early to revision 0x5003003, date = 2020-06-18
[    0.000000] Linux version 5.4.53-050453-generic (kernel@kathleen) (gcc version 9.3.0 (Ubuntu 9.3.0-13ubuntu1)) #202007220833 SMP Wed Jul 22 08:37:14 UTC 2020
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.53-050453-generic root=UUID=dbbcdeef-155d-426c-8e00-e8e7cb408150 ro quiet splash iommu=pt intel_iommu=on default_hugepagesz=2M hugepagesz=1G hugepages=16 hugepagesz=2M hugepages=4096 vt.handoff=1
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Hygon HygonGenuine
[    0.000000]   Centaur CentaurHauls
[    0.000000]   zhaoxin   Shanghai  
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x020: 'AVX-512 opmask'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x040: 'AVX-512 Hi256'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x080: 'AVX-512 ZMM_Hi256'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x200: 'Protection Keys User registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
[    0.000000] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
[    0.000000] x86/fpu: xstate_offset[5]:  960, xstate_sizes[5]:   64
[    0.000000] x86/fpu: xstate_offset[6]: 1024, xstate_sizes[6]:  512
[    0.000000] x86/fpu: xstate_offset[7]: 1536, xstate_sizes[7]: 1024
[    0.000000] x86/fpu: xstate_offset[9]: 2560, xstate_sizes[9]:    8
[    0.000000] x86/fpu: Enabled xstate features 0x2ff, context size is 2568 bytes, using 'compacted' format.
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000000a0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000050263fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000050264000-0x00000000503e5fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000503e6000-0x00000000682fefff] usable
[    0.000000] BIOS-e820: [mem 0x00000000682ff000-0x000000006ebfefff] reserved
[    0.000000] BIOS-e820: [mem 0x000000006ebff000-0x000000006f9fefff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000006f9ff000-0x000000006fffefff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000006ffff000-0x000000006fffffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000070000000-0x000000008fffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000bd3fffffff] usable
[    0.000000] BIOS-e820: [mem 0x000000bd40000000-0x000000bd6fffffff] reserved
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] e820: update [mem 0x4fc2a020-0x4fc5be5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fc2a020-0x4fc5be5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbf8020-0x4fc29e5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbf8020-0x4fc29e5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbef020-0x4fbf705f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbef020-0x4fbf705f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbd6020-0x4fbee65f] usable ==> usable
[    0.000000] e820: update [mem 0x4fbd6020-0x4fbee65f] usable ==> usable
[    0.000000] e820: update [mem 0x4fba6020-0x4fbd505f] usable ==> usable
[    0.000000] e820: update [mem 0x4fba6020-0x4fbd505f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb76020-0x4fba505f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb76020-0x4fba505f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb5c020-0x4fb75c5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb5c020-0x4fb75c5f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb27020-0x4fb5b25f] usable ==> usable
[    0.000000] e820: update [mem 0x4fb27020-0x4fb5b25f] usable ==> usable
[    0.000000] e820: update [mem 0x4faf2020-0x4fb2625f] usable ==> usable
[    0.000000] e820: update [mem 0x4faf2020-0x4fb2625f] usable ==> usable
[    0.000000] extended physical RAM map:
[    0.000000] reserve setup_data: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] reserve setup_data: [mem 0x00000000000a0000-0x00000000000fffff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000000100000-0x000000004faf201f] usable
[    0.000000] reserve setup_data: [mem 0x000000004faf2020-0x000000004fb2625f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb26260-0x000000004fb2701f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb27020-0x000000004fb5b25f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb5b260-0x000000004fb5c01f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb5c020-0x000000004fb75c5f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb75c60-0x000000004fb7601f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fb76020-0x000000004fba505f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fba5060-0x000000004fba601f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fba6020-0x000000004fbd505f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbd5060-0x000000004fbd601f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbd6020-0x000000004fbee65f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbee660-0x000000004fbef01f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbef020-0x000000004fbf705f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbf7060-0x000000004fbf801f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fbf8020-0x000000004fc29e5f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fc29e60-0x000000004fc2a01f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fc2a020-0x000000004fc5be5f] usable
[    0.000000] reserve setup_data: [mem 0x000000004fc5be60-0x0000000050263fff] usable
[    0.000000] reserve setup_data: [mem 0x0000000050264000-0x00000000503e5fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000503e6000-0x00000000682fefff] usable
[    0.000000] reserve setup_data: [mem 0x00000000682ff000-0x000000006ebfefff] reserved
[    0.000000] reserve setup_data: [mem 0x000000006ebff000-0x000000006f9fefff] ACPI NVS
[    0.000000] reserve setup_data: [mem 0x000000006f9ff000-0x000000006fffefff] ACPI data
[    0.000000] reserve setup_data: [mem 0x000000006ffff000-0x000000006fffffff] usable
[    0.000000] reserve setup_data: [mem 0x0000000070000000-0x000000008fffffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fe000000-0x00000000fe010fff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000100000000-0x000000bd3fffffff] usable
[    0.000000] reserve setup_data: [mem 0x000000bd40000000-0x000000bd6fffffff] reserved
[    0.000000] efi: EFI v2.70 by Dell Inc.
[    0.000000] efi:  ACPI=0x6fffe000  ACPI 2.0=0x6fffe014  SMBIOS=0x68d36000  SMBIOS 3.0=0x68d34000  MEMATTR=0x652016a0 
[    0.000000] SMBIOS 3.2.0 present.
[    0.000000] DMI: Dell Inc. PowerEdge R740/0WXD1Y, BIOS 2.6.4 04/09/2020
[    0.000000] tsc: Detected 2500.000 MHz processor
[    0.000013] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000014] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000021] last_pfn = 0xbd40000 max_arch_pfn = 0x400000000
[    0.000024] MTRR default type: uncachable
[    0.000025] MTRR fixed ranges enabled:
[    0.000026]   00000-9FFFF write-back
[    0.000027]   A0000-BFFFF uncachable
[    0.000027]   C0000-FFFFF write-protect
[    0.000028] MTRR variable ranges enabled:
[    0.000029]   0 base 000000000000 mask 3F8000000000 write-back
[    0.000030]   1 base 008000000000 mask 3FC000000000 write-back
[    0.000031]   2 base 00BD40000000 mask 3FFFC0000000 uncachable
[    0.000031]   3 base 00BD80000000 mask 3FFF80000000 uncachable
[    0.000032]   4 base 00BE00000000 mask 3FFE00000000 uncachable
[    0.000033]   5 base 000080000000 mask 3FFF80000000 uncachable
[    0.000033]   6 base 000070000000 mask 3FFFFC000000 uncachable
[    0.000034]   7 disabled
[    0.000034]   8 disabled
[    0.000034]   9 disabled
[    0.000596] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000855] total RAM covered: 773056M
[    0.000957]  gran_size: 64K 	chunk_size: 64K 	num_reg: 10  	lose cover RAM: 629G
[    0.000958]  gran_size: 64K 	chunk_size: 128K 	num_reg: 10  	lose cover RAM: 629G
[    0.000959]  gran_size: 64K 	chunk_size: 256K 	num_reg: 10  	lose cover RAM: 629G
[    0.000960]  gran_size: 64K 	chunk_size: 512K 	num_reg: 10  	lose cover RAM: 629G
[    0.000961]  gran_size: 64K 	chunk_size: 1M 	num_reg: 10  	lose cover RAM: 629G
[    0.000962]  gran_size: 64K 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.000962]  gran_size: 64K 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.000963]  gran_size: 64K 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.000964]  gran_size: 64K 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.000964]  gran_size: 64K 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.000965]  gran_size: 64K 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.000966]  gran_size: 64K 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.000966]  gran_size: 64K 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.000967]  gran_size: 64K 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.000968]  gran_size: 64K 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.000968]  gran_size: 64K 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.000969]  gran_size: 128K 	chunk_size: 128K 	num_reg: 10  	lose cover RAM: 629G
[    0.000970]  gran_size: 128K 	chunk_size: 256K 	num_reg: 10  	lose cover RAM: 629G
[    0.000970]  gran_size: 128K 	chunk_size: 512K 	num_reg: 10  	lose cover RAM: 629G
[    0.000971]  gran_size: 128K 	chunk_size: 1M 	num_reg: 10  	lose cover RAM: 629G
[    0.000972]  gran_size: 128K 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.000972]  gran_size: 128K 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.000973]  gran_size: 128K 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.000974]  gran_size: 128K 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.000974]  gran_size: 128K 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.000975]  gran_size: 128K 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.000976]  gran_size: 128K 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.000976]  gran_size: 128K 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.000977]  gran_size: 128K 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.000978]  gran_size: 128K 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.000978]  gran_size: 128K 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.000979]  gran_size: 256K 	chunk_size: 256K 	num_reg: 10  	lose cover RAM: 629G
[    0.000980]  gran_size: 256K 	chunk_size: 512K 	num_reg: 10  	lose cover RAM: 629G
[    0.000980]  gran_size: 256K 	chunk_size: 1M 	num_reg: 10  	lose cover RAM: 629G
[    0.000981]  gran_size: 256K 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.000982]  gran_size: 256K 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.000982]  gran_size: 256K 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.000983]  gran_size: 256K 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.000984]  gran_size: 256K 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.000984]  gran_size: 256K 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.000985]  gran_size: 256K 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.000986]  gran_size: 256K 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.000986]  gran_size: 256K 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.000987]  gran_size: 256K 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.000988]  gran_size: 256K 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.000988]  gran_size: 512K 	chunk_size: 512K 	num_reg: 10  	lose cover RAM: 629G
[    0.000989]  gran_size: 512K 	chunk_size: 1M 	num_reg: 10  	lose cover RAM: 629G
[    0.000990]  gran_size: 512K 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.000991]  gran_size: 512K 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.000991]  gran_size: 512K 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.000992]  gran_size: 512K 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.000993]  gran_size: 512K 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.000994]  gran_size: 512K 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.000995]  gran_size: 512K 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.000995]  gran_size: 512K 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.000996]  gran_size: 512K 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.000997]  gran_size: 512K 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.000997]  gran_size: 512K 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.000998]  gran_size: 1M 	chunk_size: 1M 	num_reg: 10  	lose cover RAM: 629G
[    0.000999]  gran_size: 1M 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.000999]  gran_size: 1M 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.001000]  gran_size: 1M 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.001001]  gran_size: 1M 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.001001]  gran_size: 1M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001002]  gran_size: 1M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001003]  gran_size: 1M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001004]  gran_size: 1M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001004]  gran_size: 1M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001005]  gran_size: 1M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001006]  gran_size: 1M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001006]  gran_size: 2M 	chunk_size: 2M 	num_reg: 10  	lose cover RAM: 629G
[    0.001007]  gran_size: 2M 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.001007]  gran_size: 2M 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.001008]  gran_size: 2M 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.001009]  gran_size: 2M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001009]  gran_size: 2M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001010]  gran_size: 2M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001011]  gran_size: 2M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001011]  gran_size: 2M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001012]  gran_size: 2M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001013]  gran_size: 2M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001013]  gran_size: 4M 	chunk_size: 4M 	num_reg: 10  	lose cover RAM: 629G
[    0.001014]  gran_size: 4M 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.001015]  gran_size: 4M 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.001015]  gran_size: 4M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001016]  gran_size: 4M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001017]  gran_size: 4M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001017]  gran_size: 4M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001018]  gran_size: 4M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001019]  gran_size: 4M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001019]  gran_size: 4M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001020]  gran_size: 8M 	chunk_size: 8M 	num_reg: 10  	lose cover RAM: 629G
[    0.001021]  gran_size: 8M 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.001021]  gran_size: 8M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001022]  gran_size: 8M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001023]  gran_size: 8M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001024]  gran_size: 8M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001024]  gran_size: 8M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001025]  gran_size: 8M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001026]  gran_size: 8M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001027]  gran_size: 16M 	chunk_size: 16M 	num_reg: 10  	lose cover RAM: 629G
[    0.001028]  gran_size: 16M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001028]  gran_size: 16M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001029]  gran_size: 16M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001030]  gran_size: 16M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001030]  gran_size: 16M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001031]  gran_size: 16M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001032]  gran_size: 16M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001032]  gran_size: 32M 	chunk_size: 32M 	num_reg: 10  	lose cover RAM: 629G
[    0.001033]  gran_size: 32M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001034]  gran_size: 32M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001034]  gran_size: 32M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001035]  gran_size: 32M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001036]  gran_size: 32M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001036]  gran_size: 32M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001037]  gran_size: 64M 	chunk_size: 64M 	num_reg: 10  	lose cover RAM: 629G
[    0.001038]  gran_size: 64M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 725G
[    0.001038]  gran_size: 64M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 725G
[    0.001039]  gran_size: 64M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001040]  gran_size: 64M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001040]  gran_size: 64M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001041]  gran_size: 128M 	chunk_size: 128M 	num_reg: 10  	lose cover RAM: 644160M
[    0.001042]  gran_size: 128M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 644160M
[    0.001043]  gran_size: 128M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001043]  gran_size: 128M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001044]  gran_size: 128M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001045]  gran_size: 256M 	chunk_size: 256M 	num_reg: 10  	lose cover RAM: 251072M
[    0.001045]  gran_size: 256M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 117G
[    0.001046]  gran_size: 256M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 117G
[    0.001047]  gran_size: 256M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 117G
[    0.001047]  gran_size: 512M 	chunk_size: 512M 	num_reg: 10  	lose cover RAM: 120256M
[    0.001048]  gran_size: 512M 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 251136M
[    0.001049]  gran_size: 512M 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 251136M
[    0.001049]  gran_size: 1G 	chunk_size: 1G 	num_reg: 10  	lose cover RAM: 55232M
[    0.001050]  gran_size: 1G 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 513792M
[    0.001051]  gran_size: 2G 	chunk_size: 2G 	num_reg: 10  	lose cover RAM: 23488M
[    0.001051] mtrr_cleanup: can not find optimal value
[    0.001052] please specify mtrr_gran_size/mtrr_chunk_size
[    0.001055] e820: update [mem 0x70000000-0x73ffffff] usable ==> reserved
[    0.001056] e820: update [mem 0x80000000-0xffffffff] usable ==> reserved
[    0.001058] x2apic: enabled by BIOS, switching to x2apic ops
[    0.001059] last_pfn = 0x70000 max_arch_pfn = 0x400000000
[    0.007603] check: Scanning 1 areas for low memory corruption
[    0.007607] Using GB pages for direct mapping
[    0.008028] Secure boot disabled
[    0.008029] RAMDISK: [mem 0x2f570000-0x31df1fff]
[    0.008038] ACPI: Early table checksum verification disabled
[    0.008042] ACPI: RSDP 0x000000006FFFE014 000024 (v02 DELL  )
[    0.008045] ACPI: XSDT 0x000000006FC13188 00010C (v01 DELL   PE_SC3   00000000      01000013)
[    0.008050] ACPI: FACP 0x000000006FFF8000 000114 (v06 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008055] ACPI: DSDT 0x000000006FCFA000 2ECF86 (v02 DELL   PE_SC3   00000003 DELL 00000001)
[    0.008057] ACPI: FACS 0x000000006EF6E000 000040
[    0.008059] ACPI: SSDT 0x000000006FFFC000 00046C (v02 INTEL  ADDRXLAT 00000001 INTL 20180508)
[    0.008061] ACPI: MCEJ 0x000000006FFFB000 000130 (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008063] ACPI: WD__ 0x000000006FFFA000 000134 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008065] ACPI: SLIC 0x000000006FFF9000 000024 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008067] ACPI: HMAT 0x000000006FFF7000 0000E0 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008069] ACPI: HPET 0x000000006FFF6000 000038 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008071] ACPI: APIC 0x000000006FFF4000 0016DE (v04 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008073] ACPI: MCFG 0x000000006FFF3000 00003C (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008075] ACPI: MIGT 0x000000006FFF2000 000040 (v01 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008077] ACPI: MSCT 0x000000006FFF1000 000090 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008079] ACPI: PCAT 0x000000006FFF0000 000088 (v02 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008081] ACPI: PCCT 0x000000006FFEF000 00006E (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008083] ACPI: PMTT 0x000000006FFEE000 000538 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008085] ACPI: RASF 0x000000006FFED000 000030 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008087] ACPI: SLIT 0x000000006FFEC000 00042C (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008089] ACPI: SRAT 0x000000006FFE9000 002D30 (v03 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008091] ACPI: SVOS 0x000000006FFE8000 000032 (v01 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008093] ACPI: WSMT 0x000000006FFE7000 000028 (v01 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008095] ACPI: OEM4 0x000000006FC4C000 0AD1C1 (v02 INTEL  CPU  CST 00003000 INTL 20180508)
[    0.008097] ACPI: SSDT 0x000000006FC14000 037465 (v02 INTEL  SSDT  PM 00004000 INTL 20180508)
[    0.008099] ACPI: SSDT 0x000000006FC12000 000A1F (v02 DELL   PE_SC3   00000000 DELL 00000001)
[    0.008101] ACPI: SSDT 0x000000006FC0E000 00357F (v02 INTEL  SpsNm    00000002 INTL 20180508)
[    0.008103] ACPI: NFIT 0x000000006FFFD000 000430 (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008105] ACPI: DMAR 0x000000006FC0D000 0001B0 (v01 DELL   PE_SC3   00000001 DELL 00000001)
[    0.008107] ACPI: HEST 0x000000006FC0C000 00017C (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008109] ACPI: BERT 0x000000006FC0B000 000030 (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008111] ACPI: ERST 0x000000006FC0A000 000230 (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008113] ACPI: EINJ 0x000000006FC09000 000150 (v01 DELL   PE_SC3   00000002 DELL 00000001)
[    0.008121] ACPI: Local APIC address 0xfee00000
[    0.008124] Setting APIC routing to cluster x2apic.
[    0.008204] SRAT: PXM 0 -> APIC 0x0000 -> Node 0
[    0.008204] SRAT: PXM 1 -> APIC 0x0040 -> Node 1
[    0.008205] SRAT: PXM 0 -> APIC 0x0008 -> Node 0
[    0.008205] SRAT: PXM 1 -> APIC 0x0048 -> Node 1
[    0.008206] SRAT: PXM 0 -> APIC 0x0002 -> Node 0
[    0.008206] SRAT: PXM 1 -> APIC 0x0042 -> Node 1
[    0.008206] SRAT: PXM 0 -> APIC 0x0006 -> Node 0
[    0.008207] SRAT: PXM 1 -> APIC 0x0046 -> Node 1
[    0.008207] SRAT: PXM 0 -> APIC 0x0004 -> Node 0
[    0.008208] SRAT: PXM 1 -> APIC 0x0044 -> Node 1
[    0.008208] SRAT: PXM 0 -> APIC 0x0018 -> Node 0
[    0.008209] SRAT: PXM 1 -> APIC 0x0058 -> Node 1
[    0.008209] SRAT: PXM 0 -> APIC 0x0010 -> Node 0
[    0.008210] SRAT: PXM 1 -> APIC 0x0050 -> Node 1
[    0.008210] SRAT: PXM 0 -> APIC 0x0016 -> Node 0
[    0.008210] SRAT: PXM 1 -> APIC 0x0056 -> Node 1
[    0.008211] SRAT: PXM 0 -> APIC 0x0012 -> Node 0
[    0.008212] SRAT: PXM 1 -> APIC 0x0052 -> Node 1
[    0.008212] SRAT: PXM 0 -> APIC 0x0014 -> Node 0
[    0.008213] SRAT: PXM 1 -> APIC 0x0054 -> Node 1
[    0.008213] SRAT: PXM 0 -> APIC 0x0020 -> Node 0
[    0.008214] SRAT: PXM 1 -> APIC 0x0060 -> Node 1
[    0.008214] SRAT: PXM 0 -> APIC 0x0028 -> Node 0
[    0.008214] SRAT: PXM 1 -> APIC 0x0068 -> Node 1
[    0.008215] SRAT: PXM 0 -> APIC 0x0022 -> Node 0
[    0.008215] SRAT: PXM 1 -> APIC 0x0062 -> Node 1
[    0.008216] SRAT: PXM 0 -> APIC 0x0026 -> Node 0
[    0.008216] SRAT: PXM 1 -> APIC 0x0066 -> Node 1
[    0.008217] SRAT: PXM 0 -> APIC 0x0024 -> Node 0
[    0.008217] SRAT: PXM 1 -> APIC 0x0064 -> Node 1
[    0.008217] SRAT: PXM 0 -> APIC 0x0038 -> Node 0
[    0.008218] SRAT: PXM 1 -> APIC 0x0078 -> Node 1
[    0.008218] SRAT: PXM 0 -> APIC 0x0030 -> Node 0
[    0.008219] SRAT: PXM 1 -> APIC 0x0070 -> Node 1
[    0.008219] SRAT: PXM 0 -> APIC 0x0036 -> Node 0
[    0.008220] SRAT: PXM 1 -> APIC 0x0076 -> Node 1
[    0.008220] SRAT: PXM 0 -> APIC 0x0032 -> Node 0
[    0.008220] SRAT: PXM 1 -> APIC 0x0072 -> Node 1
[    0.008221] SRAT: PXM 0 -> APIC 0x0034 -> Node 0
[    0.008221] SRAT: PXM 1 -> APIC 0x0074 -> Node 1
[    0.008222] SRAT: PXM 0 -> APIC 0x0001 -> Node 0
[    0.008222] SRAT: PXM 1 -> APIC 0x0041 -> Node 1
[    0.008222] SRAT: PXM 0 -> APIC 0x0009 -> Node 0
[    0.008223] SRAT: PXM 1 -> APIC 0x0049 -> Node 1
[    0.008223] SRAT: PXM 0 -> APIC 0x0003 -> Node 0
[    0.008224] SRAT: PXM 1 -> APIC 0x0043 -> Node 1
[    0.008224] SRAT: PXM 0 -> APIC 0x0007 -> Node 0
[    0.008225] SRAT: PXM 1 -> APIC 0x0047 -> Node 1
[    0.008225] SRAT: PXM 0 -> APIC 0x0005 -> Node 0
[    0.008225] SRAT: PXM 1 -> APIC 0x0045 -> Node 1
[    0.008226] SRAT: PXM 0 -> APIC 0x0019 -> Node 0
[    0.008226] SRAT: PXM 1 -> APIC 0x0059 -> Node 1
[    0.008227] SRAT: PXM 0 -> APIC 0x0011 -> Node 0
[    0.008227] SRAT: PXM 1 -> APIC 0x0051 -> Node 1
[    0.008227] SRAT: PXM 0 -> APIC 0x0017 -> Node 0
[    0.008228] SRAT: PXM 1 -> APIC 0x0057 -> Node 1
[    0.008228] SRAT: PXM 0 -> APIC 0x0013 -> Node 0
[    0.008229] SRAT: PXM 1 -> APIC 0x0053 -> Node 1
[    0.008229] SRAT: PXM 0 -> APIC 0x0015 -> Node 0
[    0.008230] SRAT: PXM 1 -> APIC 0x0055 -> Node 1
[    0.008230] SRAT: PXM 0 -> APIC 0x0021 -> Node 0
[    0.008230] SRAT: PXM 1 -> APIC 0x0061 -> Node 1
[    0.008231] SRAT: PXM 0 -> APIC 0x0029 -> Node 0
[    0.008231] SRAT: PXM 1 -> APIC 0x0069 -> Node 1
[    0.008232] SRAT: PXM 0 -> APIC 0x0023 -> Node 0
[    0.008232] SRAT: PXM 1 -> APIC 0x0063 -> Node 1
[    0.008232] SRAT: PXM 0 -> APIC 0x0027 -> Node 0
[    0.008233] SRAT: PXM 1 -> APIC 0x0067 -> Node 1
[    0.008233] SRAT: PXM 0 -> APIC 0x0025 -> Node 0
[    0.008234] SRAT: PXM 1 -> APIC 0x0065 -> Node 1
[    0.008234] SRAT: PXM 0 -> APIC 0x0039 -> Node 0
[    0.008235] SRAT: PXM 1 -> APIC 0x0079 -> Node 1
[    0.008235] SRAT: PXM 0 -> APIC 0x0031 -> Node 0
[    0.008235] SRAT: PXM 1 -> APIC 0x0071 -> Node 1
[    0.008236] SRAT: PXM 0 -> APIC 0x0037 -> Node 0
[    0.008236] SRAT: PXM 1 -> APIC 0x0077 -> Node 1
[    0.008237] SRAT: PXM 0 -> APIC 0x0033 -> Node 0
[    0.008237] SRAT: PXM 1 -> APIC 0x0073 -> Node 1
[    0.008237] SRAT: PXM 0 -> APIC 0x0035 -> Node 0
[    0.008238] SRAT: PXM 1 -> APIC 0x0075 -> Node 1
[    0.008244] ACPI: SRAT: Node 0 PXM 0 [mem 0x00000000-0x7fffffff]
[    0.008245] ACPI: SRAT: Node 0 PXM 0 [mem 0x100000000-0x5ebfffffff]
[    0.008246] ACPI: SRAT: Node 1 PXM 1 [mem 0x5ec0000000-0xbd3fffffff]
[    0.008253] NUMA: Initialized distance table, cnt=2
[    0.008256] NUMA: Node 0 [mem 0x00000000-0x7fffffff] + [mem 0x100000000-0x5ebfffffff] -> [mem 0x00000000-0x5ebfffffff]
[    0.008264] NODE_DATA(0) allocated [mem 0x5ebffd5000-0x5ebfffffff]
[    0.008366] NODE_DATA(1) allocated [mem 0xbd3ffd4000-0xbd3fffefff]
[    0.009461] Zone ranges:
[    0.009462]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.009463]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.009464]   Normal   [mem 0x0000000100000000-0x000000bd3fffffff]
[    0.009465]   Device   empty
[    0.009466] Movable zone start for each node
[    0.009468] Early memory node ranges
[    0.009469]   node   0: [mem 0x0000000000001000-0x000000000009ffff]
[    0.009470]   node   0: [mem 0x0000000000100000-0x0000000050263fff]
[    0.009471]   node   0: [mem 0x00000000503e6000-0x00000000682fefff]
[    0.009471]   node   0: [mem 0x000000006ffff000-0x000000006fffffff]
[    0.009472]   node   0: [mem 0x0000000100000000-0x0000005ebfffffff]
[    0.009495]   node   1: [mem 0x0000005ec0000000-0x000000bd3fffffff]
[    0.010421] Zeroed struct page in unavailable ranges: 32483 pages
[    0.010423] Initmem setup node 0 [mem 0x0000000000001000-0x0000005ebfffffff]
[    0.010424] On node 0 totalpages: 98730269
[    0.010425]   DMA zone: 64 pages used for memmap
[    0.010426]   DMA zone: 1094 pages reserved
[    0.010426]   DMA zone: 3999 pages, LIFO batch:0
[    0.010558]   DMA32 zone: 6598 pages used for memmap
[    0.010558]   DMA32 zone: 422270 pages, LIFO batch:63
[    0.026352]   Normal zone: 1536000 pages used for memmap
[    0.026352]   Normal zone: 98304000 pages, LIFO batch:63
[    3.216339] Initmem setup node 1 [mem 0x0000005ec0000000-0x000000bd3fffffff]
[    3.216340] On node 1 totalpages: 99090432
[    3.216341]   Normal zone: 1548288 pages used for memmap
[    3.216341]   Normal zone: 99090432 pages, LIFO batch:63
[    6.668774] ACPI: PM-Timer IO Port: 0x508
[    6.668776] ACPI: Local APIC address 0xfee00000
[    6.668798] ACPI: X2APIC_NMI (uid[0xffffffff] high level lint[0x1])
[    6.668801] ACPI: LAPIC_NMI (acpi_id[0xff] high level lint[0x1])
[    6.668821] IOAPIC[0]: apic_id 8, version 32, address 0xfec00000, GSI 0-23
[    6.668825] IOAPIC[1]: apic_id 9, version 32, address 0xfec01000, GSI 24-31
[    6.668829] IOAPIC[2]: apic_id 10, version 32, address 0xfec08000, GSI 32-39
[    6.668832] IOAPIC[3]: apic_id 11, version 32, address 0xfec10000, GSI 40-47
[    6.668836] IOAPIC[4]: apic_id 12, version 32, address 0xfec18000, GSI 48-55
[    6.668840] IOAPIC[5]: apic_id 15, version 32, address 0xfec20000, GSI 72-79
[    6.668844] IOAPIC[6]: apic_id 16, version 32, address 0xfec28000, GSI 80-87
[    6.668848] IOAPIC[7]: apic_id 17, version 32, address 0xfec30000, GSI 88-95
[    6.668853] IOAPIC[8]: apic_id 18, version 32, address 0xfec38000, GSI 96-103
[    6.668857] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    6.668858] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
[    6.668861] ACPI: IRQ0 used by override.
[    6.668862] ACPI: IRQ9 used by override.
[    6.668866] Using ACPI (MADT) for SMP configuration information
[    6.668867] ACPI: HPET id: 0x8086a701 base: 0xfed00000
[    6.668871] TSC deadline timer available
[    6.668872] smpboot: Allowing 80 CPUs, 0 hotplug CPUs
[    6.668896] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    6.668897] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    6.668898] PM: Registered nosave memory: [mem 0x4faf2000-0x4faf2fff]
[    6.668900] PM: Registered nosave memory: [mem 0x4fb26000-0x4fb26fff]
[    6.668900] PM: Registered nosave memory: [mem 0x4fb27000-0x4fb27fff]
[    6.668901] PM: Registered nosave memory: [mem 0x4fb5b000-0x4fb5bfff]
[    6.668902] PM: Registered nosave memory: [mem 0x4fb5c000-0x4fb5cfff]
[    6.668903] PM: Registered nosave memory: [mem 0x4fb75000-0x4fb75fff]
[    6.668903] PM: Registered nosave memory: [mem 0x4fb76000-0x4fb76fff]
[    6.668905] PM: Registered nosave memory: [mem 0x4fba5000-0x4fba5fff]
[    6.668906] PM: Registered nosave memory: [mem 0x4fba6000-0x4fba6fff]
[    6.668907] PM: Registered nosave memory: [mem 0x4fbd5000-0x4fbd5fff]
[    6.668907] PM: Registered nosave memory: [mem 0x4fbd6000-0x4fbd6fff]
[    6.668909] PM: Registered nosave memory: [mem 0x4fbee000-0x4fbeefff]
[    6.668910] PM: Registered nosave memory: [mem 0x4fbef000-0x4fbeffff]
[    6.668911] PM: Registered nosave memory: [mem 0x4fbf7000-0x4fbf7fff]
[    6.668911] PM: Registered nosave memory: [mem 0x4fbf8000-0x4fbf8fff]
[    6.668913] PM: Registered nosave memory: [mem 0x4fc29000-0x4fc29fff]
[    6.668914] PM: Registered nosave memory: [mem 0x4fc2a000-0x4fc2afff]
[    6.668915] PM: Registered nosave memory: [mem 0x4fc5b000-0x4fc5bfff]
[    6.668917] PM: Registered nosave memory: [mem 0x50264000-0x503e5fff]
[    6.668918] PM: Registered nosave memory: [mem 0x682ff000-0x6ebfefff]
[    6.668919] PM: Registered nosave memory: [mem 0x6ebff000-0x6f9fefff]
[    6.668919] PM: Registered nosave memory: [mem 0x6f9ff000-0x6fffefff]
[    6.668921] PM: Registered nosave memory: [mem 0x70000000-0x8fffffff]
[    6.668922] PM: Registered nosave memory: [mem 0x90000000-0xfdffffff]
[    6.668922] PM: Registered nosave memory: [mem 0xfe000000-0xfe010fff]
[    6.668923] PM: Registered nosave memory: [mem 0xfe011000-0xffffffff]
[    6.668925] [mem 0x90000000-0xfdffffff] available for PCI devices
[    6.668926] Booting paravirtualized kernel on bare hardware
[    6.668930] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    6.668938] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:80 nr_cpu_ids:80 nr_node_ids:2
[    6.684095] percpu: Embedded 54 pages/cpu s184320 r8192 d28672 u262144
[    6.684107] pcpu-alloc: s184320 r8192 d28672 u262144 alloc=1*2097152
[    6.684108] pcpu-alloc: [0] 00 02 04 06 08 10 12 14 [0] 16 18 20 22 24 26 28 30 
[    6.684111] pcpu-alloc: [0] 32 34 36 38 40 42 44 46 [0] 48 50 52 54 56 58 60 62 
[    6.684114] pcpu-alloc: [0] 64 66 68 70 72 74 76 78 [1] 01 03 05 07 09 11 13 15 
[    6.684117] pcpu-alloc: [1] 17 19 21 23 25 27 29 31 [1] 33 35 37 39 41 43 45 47 
[    6.684120] pcpu-alloc: [1] 49 51 53 55 57 59 61 63 [1] 65 67 69 71 73 75 77 79 
[    6.684169] Built 2 zonelists, mobility grouping on.  Total pages: 194728657
[    6.684169] Policy zone: Normal
[    6.684171] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.4.53-050453-generic root=UUID=dbbcdeef-155d-426c-8e00-e8e7cb408150 ro quiet splash iommu=pt intel_iommu=on default_hugepagesz=2M hugepagesz=1G hugepages=16 hugepagesz=2M hugepages=4096 vt.handoff=1
[    6.684283] DMAR: IOMMU enabled
[    6.684419] printk: log_buf_len individual max cpu contribution: 4096 bytes
[    6.684420] printk: log_buf_len total cpu_extra contributions: 323584 bytes
[    6.684421] printk: log_buf_len min size: 262144 bytes
[    6.685192] printk: log_buf_len: 1048576 bytes
[    6.685193] printk: early log buf free: 226244(86%)
[    6.685861] mem auto-init: stack:off, heap alloc:on, heap free:off
[    6.696241] Calgary: detecting Calgary via BIOS EBDA area
[    6.696242] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    8.412702] Memory: 761873400K/791282804K available (14339K kernel code, 2396K rwdata, 4932K rodata, 2704K init, 5000K bss, 29409404K reserved, 0K cma-reserved)
[    8.412712] random: get_random_u64 called from kmem_cache_open+0x2d/0x410 with crng_init=0
[    8.413858] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=80, Nodes=2
[    8.413915] ftrace: allocating 44445 entries in 174 pages
[    8.432547] rcu: Hierarchical RCU implementation.
[    8.432549] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=80.
[    8.432550] 	Tasks RCU enabled.
[    8.432550] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    8.432551] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=80
[    8.435154] NR_IRQS: 524544, nr_irqs: 2424, preallocated irqs: 16
[    8.435657] random: crng done (trusting CPU's manufacturer)
[    8.435849] Console: colour dummy device 80x25
[    8.435864] printk: console [tty0] enabled
[    8.436058] mempolicy: Enabling automatic NUMA balancing. Configure with numa_balancing= or the kernel.numa_balancing sysctl
[    8.436061] ACPI: Core revision 20190816
[    8.438828] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 79635855245 ns
[    8.438876] APIC: Switch to symmetric I/O mode setup
[    8.438879] DMAR: Host address width 46
[    8.438880] DMAR: DRHD base: 0x000000d37fc000 flags: 0x0
[    8.438891] DMAR: dmar0: reg_base_addr d37fc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438892] DMAR: DRHD base: 0x000000e0ffc000 flags: 0x0
[    8.438896] DMAR: dmar1: reg_base_addr e0ffc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438897] DMAR: DRHD base: 0x000000ee7fc000 flags: 0x0
[    8.438900] DMAR: dmar2: reg_base_addr ee7fc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438901] DMAR: DRHD base: 0x000000fbffc000 flags: 0x0
[    8.438904] DMAR: dmar3: reg_base_addr fbffc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438905] DMAR: DRHD base: 0x000000aaffc000 flags: 0x0
[    8.438908] DMAR: dmar4: reg_base_addr aaffc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438908] DMAR: DRHD base: 0x000000b87fc000 flags: 0x0
[    8.438911] DMAR: dmar5: reg_base_addr b87fc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438912] DMAR: DRHD base: 0x000000c5ffc000 flags: 0x0
[    8.438917] DMAR: dmar6: reg_base_addr c5ffc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438918] DMAR: DRHD base: 0x0000009d7fc000 flags: 0x1
[    8.438925] DMAR: dmar7: reg_base_addr 9d7fc000 ver 1:0 cap 8d2078c106f0466 ecap f020df
[    8.438926] DMAR: RMRR base: 0x0000006ef60000 end: 0x0000006ef62fff
[    8.438927] DMAR: ATSR flags: 0x0
[    8.438928] DMAR: ATSR flags: 0x0
[    8.438930] DMAR-IR: IOAPIC id 12 under DRHD base  0xc5ffc000 IOMMU 6
[    8.438931] DMAR-IR: IOAPIC id 11 under DRHD base  0xb87fc000 IOMMU 5
[    8.438931] DMAR-IR: IOAPIC id 10 under DRHD base  0xaaffc000 IOMMU 4
[    8.438932] DMAR-IR: IOAPIC id 18 under DRHD base  0xfbffc000 IOMMU 3
[    8.438932] DMAR-IR: IOAPIC id 17 under DRHD base  0xee7fc000 IOMMU 2
[    8.438933] DMAR-IR: IOAPIC id 16 under DRHD base  0xe0ffc000 IOMMU 1
[    8.438934] DMAR-IR: IOAPIC id 15 under DRHD base  0xd37fc000 IOMMU 0

---

### 评论 #4 — dshm (2021-03-02T07:40:52Z)

[    8.438934] DMAR-IR: IOAPIC id 8 under DRHD base  0x9d7fc000 IOMMU 7
[    8.438935] DMAR-IR: IOAPIC id 9 under DRHD base  0x9d7fc000 IOMMU 7
[    8.438935] DMAR-IR: HPET id 0 under DRHD base 0x9d7fc000
[    8.438936] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
[    8.444300] DMAR-IR: Enabled IRQ remapping in x2apic mode
[    8.445466] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    8.462808] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x240939f1bb2, max_idle_ns: 440795263295 ns
[    8.462812] Calibrating delay loop (skipped), value calculated using timer frequency.. 5000.00 BogoMIPS (lpj=10000000)
[    8.462814] pid_max: default: 81920 minimum: 640
[    8.467093] LSM: Security Framework initializing
[    8.467132] Yama: becoming mindful.
[    8.467834] AppArmor: AppArmor initialized
[    8.596544] Dentry cache hash table entries: 33554432 (order: 16, 268435456 bytes, vmalloc)
[    8.659760] Inode-cache hash table entries: 16777216 (order: 15, 134217728 bytes, vmalloc)
[    8.661884] Mount-cache hash table entries: 524288 (order: 10, 4194304 bytes, vmalloc)
[    8.663859] Mountpoint-cache hash table entries: 524288 (order: 10, 4194304 bytes, vmalloc)
[    8.663947] *** VALIDATE tmpfs ***
[    8.664371] *** VALIDATE proc ***
[    8.664631] *** VALIDATE cgroup1 ***
[    8.664632] *** VALIDATE cgroup2 ***
[    8.664760] mce: CPU0: Thermal monitoring enabled (TM1)
[    8.664788] process: using mwait in idle threads
[    8.664790] Last level iTLB entries: 4KB 64, 2MB 8, 4MB 8
[    8.664791] Last level dTLB entries: 4KB 64, 2MB 0, 4MB 0, 1GB 4
[    8.664795] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    8.664797] Spectre V2 : Mitigation: Enhanced IBRS
[    8.664797] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    8.664799] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    8.664800] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    8.664800] TAA: Mitigation: TSX disabled
[    8.665106] Freeing SMP alternatives memory: 40K
[    8.671123] smpboot: CPU0: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz (family: 0x6, model: 0x55, stepping: 0x7)
[    8.671476] Performance Events: PEBS fmt3+, Skylake events, 32-deep LBR, full-width counters, Intel PMU driver.
[    8.671483] ... version:                4
[    8.671483] ... bit width:              48
[    8.671483] ... generic registers:      4
[    8.671484] ... value mask:             0000ffffffffffff
[    8.671484] ... max period:             00007fffffffffff
[    8.671485] ... fixed-purpose events:   3
[    8.671485] ... event mask:             000000070000000f
[    8.671584] rcu: Hierarchical SRCU implementation.
[    8.684922] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    8.686975] smp: Bringing up secondary CPUs ...
[    8.687278] x86: Booting SMP configuration:
[    8.687280] .... node  #1, CPUs:        #1
[    0.003212] smpboot: CPU 1 Converting physical 0 to logical die 1
[    8.791058] .... node  #0, CPUs:    #2
[    8.806278] .... node  #1, CPUs:    #3
[    8.823073] .... node  #0, CPUs:    #4
[    8.835980] .... node  #1, CPUs:    #5
[    8.852700] .... node  #0, CPUs:    #6
[    8.865328] .... node  #1, CPUs:    #7
[    8.881883] .... node  #0, CPUs:    #8
[    8.897013] .... node  #1, CPUs:    #9
[    8.913584] .... node  #0, CPUs:   #10
[    8.927133] .... node  #1, CPUs:   #11
[    8.943556] .... node  #0, CPUs:   #12
[    8.959104] .... node  #1, CPUs:   #13
[    8.973595] .... node  #0, CPUs:   #14
[    8.988705] .... node  #1, CPUs:   #15
[    9.003056] .... node  #0, CPUs:   #16
[    9.018018] .... node  #1, CPUs:   #17
[    9.034830] .... node  #0, CPUs:   #18
[    9.047611] .... node  #1, CPUs:   #19
[    9.064179] .... node  #0, CPUs:   #20
[    9.079404] .... node  #1, CPUs:   #21
[    9.093901] .... node  #0, CPUs:   #22
[    9.109310] .... node  #1, CPUs:   #23
[    9.126205] .... node  #0, CPUs:   #24
[    9.140817] .... node  #1, CPUs:   #25
[    9.155882] .... node  #0, CPUs:   #26
[    9.169352] .... node  #1, CPUs:   #27
[    9.186173] .... node  #0, CPUs:   #28
[    9.199998] .... node  #1, CPUs:   #29
[    9.215092] .... node  #0, CPUs:   #30
[    9.230088] .... node  #1, CPUs:   #31
[    9.247076] .... node  #0, CPUs:   #32
[    9.261032] .... node  #1, CPUs:   #33
[    9.276028] .... node  #0, CPUs:   #34
[    9.289419] .... node  #1, CPUs:   #35
[    9.306160] .... node  #0, CPUs:   #36
[    9.321248] .... node  #1, CPUs:   #37
[    9.335663] .... node  #0, CPUs:   #38
[    9.351129] .... node  #1, CPUs:   #39
[    9.367572] .... node  #0, CPUs:   #40
[    9.369191] .... node  #1, CPUs:   #41
[    9.375172] .... node  #0, CPUs:   #42
[    9.379146] .... node  #1, CPUs:   #43
[    9.383444] .... node  #0, CPUs:   #44
[    9.387815] .... node  #1, CPUs:   #45
[    9.392238] .... node  #0, CPUs:   #46
[    9.396446] .... node  #1, CPUs:   #47
[    9.400766] .... node  #0, CPUs:   #48
[    9.405004] .... node  #1, CPUs:   #49
[    9.409328] .... node  #0, CPUs:   #50
[    9.413679] .... node  #1, CPUs:   #51
[    9.418109] .... node  #0, CPUs:   #52
[    9.423066] .... node  #1, CPUs:   #53
[    9.427039] .... node  #0, CPUs:   #54
[    9.431258] .... node  #1, CPUs:   #55
[    9.435672] .... node  #0, CPUs:   #56
[    9.439875] .... node  #1, CPUs:   #57
[    9.444212] .... node  #0, CPUs:   #58
[    9.448430] .... node  #1, CPUs:   #59
[    9.452760] .... node  #0, CPUs:   #60
[    9.457232] .... node  #1, CPUs:   #61
[    9.461665] .... node  #0, CPUs:   #62
[    9.466034] .... node  #1, CPUs:   #63
[    9.471149] .... node  #0, CPUs:   #64
[    9.475180] .... node  #1, CPUs:   #65
[    9.479299] .... node  #0, CPUs:   #66
[    9.483652] .... node  #1, CPUs:   #67
[    9.488073] .... node  #0, CPUs:   #68
[    9.492506] .... node  #1, CPUs:   #69
[    9.496893] .... node  #0, CPUs:   #70
[    9.501307] .... node  #1, CPUs:   #71
[    9.505801] .... node  #0, CPUs:   #72
[    9.510147] .... node  #1, CPUs:   #73
[    9.515045] .... node  #0, CPUs:   #74
[    9.519187] .... node  #1, CPUs:   #75
[    9.523326] .... node  #0, CPUs:   #76
[    9.527712] .... node  #1, CPUs:   #77
[    9.532042] .... node  #0, CPUs:   #78
[    9.536327] .... node  #1, CPUs:   #79
[    9.540698] smp: Brought up 2 nodes, 80 CPUs
[    9.540698] smpboot: Max logical packages: 2
[    9.540698] smpboot: Total of 80 processors activated (400060.62 BogoMIPS)
[    9.570847] devtmpfs: initialized
[    9.570864] x86/mm: Memory block size: 1024MB
[    9.589152] PM: Registering ACPI NVS region [mem 0x6ebff000-0x6f9fefff] (14680064 bytes)
[    9.589152] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    9.591822] futex hash table entries: 32768 (order: 9, 2097152 bytes, vmalloc)
[    9.592503] pinctrl core: initialized pinctrl subsystem
[    9.592645] PM: RTC time: 04:50:22, date: 2021-02-24
[    9.592970] NET: Registered protocol family 16
[    9.593109] audit: initializing netlink subsys (disabled)
[    9.593115] audit: type=2000 audit(1614142221.156:1): state=initialized audit_enabled=0 res=1
[    9.593115] EISA bus registered
[    9.593115] cpuidle: using governor ladder
[    9.593115] cpuidle: using governor menu
[    9.593115] Detected 1 PCC Subspaces
[    9.593115] Registering PCC driver as Mailbox controller
[    9.593115] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
[    9.593115] ACPI: bus type PCI registered
[    9.593115] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    9.593115] PCI: MMCONFIG for domain 0000 [bus 00-ff] at [mem 0x80000000-0x8fffffff] (base 0x80000000)
[    9.593115] PCI: MMCONFIG at [mem 0x80000000-0x8fffffff] reserved in E820
[    9.593115] pmd_set_huge: Cannot satisfy [mem 0x80000000-0x80200000] with a huge-page mapping due to MTRR override.
[    9.593115] PCI: Using configuration type 1 for base access
[    9.593115] PCI: Dell System detected, enabling pci=bfsort.
[   16.232626] HugeTLB registered 1.00 GiB page size, pre-allocated 16 pages
[   16.232628] HugeTLB registered 2.00 MiB page size, pre-allocated 4096 pages
[   16.239242] ACPI: Added _OSI(Module Device)
[   16.239242] ACPI: Added _OSI(Processor Device)
[   16.239243] ACPI: Added _OSI(3.0 _SCP Extensions)
[   16.239243] ACPI: Added _OSI(Processor Aggregator Device)
[   16.239244] ACPI: Added _OSI(Linux-Dell-Video)
[   16.239245] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[   16.239246] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[   16.327760] ACPI: 5 ACPI AML tables successfully acquired and loaded
[   16.335534] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[   16.342841] ACPI: Dynamic OEM Table Load:
[   16.536385] ACPI: Interpreter enabled
[   16.536406] ACPI: (supports S0 S5)
[   16.536407] ACPI: Using IOAPIC for interrupt routing
[   16.536650] HEST: Table parsing has been initialized.
[   16.536653] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[   16.537794] ACPI: Enabled 5 GPEs in block 00 to 7F
[   16.604768] ACPI: PCI Root Bridge [PC00] (domain 0000 [bus 00-16])
[   16.604774] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.604824] acpi PNP0A08:00: PCIe AER handled by firmware
[   16.604874] acpi PNP0A08:00: _OSC: platform does not support [SHPCHotplug LTR]
[   16.604964] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.604964] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.606597] PCI host bridge to bus 0000:00
[   16.606599] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
[   16.606600] pci_bus 0000:00: root bus resource [io  0x1000-0x3fff window]
[   16.606601] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[   16.606602] pci_bus 0000:00: root bus resource [mem 0x000c4000-0x000c7fff window]
[   16.606602] pci_bus 0000:00: root bus resource [mem 0xfe010000-0xfe010fff window]
[   16.606603] pci_bus 0000:00: root bus resource [mem 0x90000000-0x9d7fffff window]
[   16.606604] pci_bus 0000:00: root bus resource [mem 0x380000000000-0x380fffffffff window]
[   16.606606] pci_bus 0000:00: root bus resource [bus 00-16]
[   16.606615] pci 0000:00:00.0: [8086:2020] type 00 class 0x060000
[   16.607338] pci 0000:00:05.0: [8086:2024] type 00 class 0x088000
[   16.608015] pci 0000:00:05.2: [8086:2025] type 00 class 0x088000
[   16.608683] pci 0000:00:05.4: [8086:2026] type 00 class 0x080020
[   16.608691] pci 0000:00:05.4: reg 0x10: [mem 0x92b20000-0x92b20fff]
[   16.609353] pci 0000:00:08.0: [8086:2014] type 00 class 0x088000
[   16.610014] pci 0000:00:08.1: [8086:2015] type 00 class 0x110100
[   16.610659] pci 0000:00:08.2: [8086:2016] type 00 class 0x088000
[   16.611350] pci 0000:00:11.0: [8086:a1ec] type 00 class 0xff0000
[   16.611355] pci 0000:00:11.0: device has non-compliant BARs; disabling IO/MEM decoding
[   16.612039] pci 0000:00:11.5: [8086:a1d2] type 00 class 0x010601
[   16.612054] pci 0000:00:11.5: reg 0x10: [mem 0x92b16000-0x92b17fff]
[   16.612060] pci 0000:00:11.5: reg 0x14: [mem 0x92b1f000-0x92b1f0ff]
[   16.612066] pci 0000:00:11.5: reg 0x18: [io  0x2068-0x206f]
[   16.612072] pci 0000:00:11.5: reg 0x1c: [io  0x2074-0x2077]
[   16.612078] pci 0000:00:11.5: reg 0x20: [io  0x2040-0x205f]
[   16.612084] pci 0000:00:11.5: reg 0x24: [mem 0x92a80000-0x92afffff]
[   16.612119] pci 0000:00:11.5: PME# supported from D3hot
[   16.612806] pci 0000:00:14.0: [8086:a1af] type 00 class 0x0c0330
[   16.612825] pci 0000:00:14.0: reg 0x10: [mem 0x92b00000-0x92b0ffff 64bit]
[   16.612881] pci 0000:00:14.0: PME# supported from D3hot D3cold
[   16.613566] pci 0000:00:14.2: [8086:a1b1] type 00 class 0x118000
[   16.613585] pci 0000:00:14.2: reg 0x10: [mem 0x92b1c000-0x92b1cfff 64bit]
[   16.614297] pci 0000:00:16.0: [8086:a1ba] type 00 class 0x078000
[   16.614323] pci 0000:00:16.0: reg 0x10: [mem 0x92b1b000-0x92b1bfff 64bit]
[   16.614399] pci 0000:00:16.0: PME# supported from D3hot
[   16.615061] pci 0000:00:16.1: [8086:a1bb] type 00 class 0x078000
[   16.615086] pci 0000:00:16.1: reg 0x10: [mem 0x92b1a000-0x92b1afff 64bit]
[   16.615163] pci 0000:00:16.1: PME# supported from D3hot
[   16.615823] pci 0000:00:16.4: [8086:a1be] type 00 class 0x078000
[   16.615849] pci 0000:00:16.4: reg 0x10: [mem 0x92b19000-0x92b19fff 64bit]
[   16.615925] pci 0000:00:16.4: PME# supported from D3hot
[   16.616583] pci 0000:00:17.0: [8086:a182] type 00 class 0x010601
[   16.616598] pci 0000:00:17.0: reg 0x10: [mem 0x92b14000-0x92b15fff]
[   16.616604] pci 0000:00:17.0: reg 0x14: [mem 0x92b1e000-0x92b1e0ff]
[   16.616610] pci 0000:00:17.0: reg 0x18: [io  0x2060-0x2067]
[   16.616616] pci 0000:00:17.0: reg 0x1c: [io  0x2070-0x2073]
[   16.616622] pci 0000:00:17.0: reg 0x20: [io  0x2020-0x203f]
[   16.616628] pci 0000:00:17.0: reg 0x24: [mem 0x92a00000-0x92a7ffff]
[   16.616661] pci 0000:00:17.0: PME# supported from D3hot
[   16.617371] pci 0000:00:1c.0: [8086:a190] type 01 class 0x060400
[   16.617436] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
[   16.618169] pci 0000:00:1c.4: [8086:a194] type 01 class 0x060400
[   16.618231] pci 0000:00:1c.4: PME# supported from D0 D3hot D3cold
[   16.618986] pci 0000:00:1f.0: [8086:a1c1] type 00 class 0x060100
[   16.619757] pci 0000:00:1f.2: [8086:a1a1] type 00 class 0x058000
[   16.619771] pci 0000:00:1f.2: reg 0x10: [mem 0x92b10000-0x92b13fff]
[   16.620498] pci 0000:00:1f.4: [8086:a1a3] type 00 class 0x0c0500
[   16.620516] pci 0000:00:1f.4: reg 0x10: [mem 0x92b18000-0x92b180ff 64bit]
[   16.620536] pci 0000:00:1f.4: reg 0x20: [io  0x2000-0x201f]
[   16.621201] pci 0000:00:1f.5: [8086:a1a4] type 00 class 0x0c8000
[   16.621215] pci 0000:00:1f.5: reg 0x10: [mem 0xfe010000-0xfe010fff]
[   16.621968] pci 0000:01:00.0: [14e4:165f] type 00 class 0x020000
[   16.621996] pci 0000:01:00.0: reg 0x10: [mem 0x92930000-0x9293ffff 64bit pref]
[   16.622010] pci 0000:01:00.0: reg 0x18: [mem 0x92940000-0x9294ffff 64bit pref]
[   16.622023] pci 0000:01:00.0: reg 0x20: [mem 0x92950000-0x9295ffff 64bit pref]
[   16.622032] pci 0000:01:00.0: reg 0x30: [mem 0xfffc0000-0xffffffff pref]
[   16.622114] pci 0000:01:00.0: PME# supported from D0 D3hot D3cold
[   16.622226] pci 0000:01:00.1: [14e4:165f] type 00 class 0x020000
[   16.622254] pci 0000:01:00.1: reg 0x10: [mem 0x92900000-0x9290ffff 64bit pref]
[   16.622268] pci 0000:01:00.1: reg 0x18: [mem 0x92910000-0x9291ffff 64bit pref]
[   16.622282] pci 0000:01:00.1: reg 0x20: [mem 0x92920000-0x9292ffff 64bit pref]
[   16.622291] pci 0000:01:00.1: reg 0x30: [mem 0xfffc0000-0xffffffff pref]
[   16.622372] pci 0000:01:00.1: PME# supported from D0 D3hot D3cold
[   16.622501] pci 0000:00:1c.0: PCI bridge to [bus 01]
[   16.622507] pci 0000:00:1c.0:   bridge window [mem 0x92900000-0x929fffff 64bit pref]
[   16.622557] pci 0000:02:00.0: [1556:be00] type 01 class 0x060400
[   16.634836] pci 0000:00:1c.4: PCI bridge to [bus 02-03]
[   16.634843] pci 0000:00:1c.4:   bridge window [mem 0x92000000-0x928fffff]
[   16.634849] pci 0000:00:1c.4:   bridge window [mem 0x91000000-0x91ffffff 64bit pref]
[   16.634892] pci_bus 0000:03: extended config space not accessible
[   16.634929] pci 0000:03:00.0: [102b:0536] type 00 class 0x030000
[   16.634955] pci 0000:03:00.0: reg 0x10: [mem 0x91000000-0x91ffffff pref]
[   16.634969] pci 0000:03:00.0: reg 0x14: [mem 0x92808000-0x9280bfff]
[   16.634983] pci 0000:03:00.0: reg 0x18: [mem 0x92000000-0x927fffff]
[   16.635051] pci 0000:03:00.0: BAR 0: assigned to efifb
[   16.635210] pci 0000:02:00.0: PCI bridge to [bus 03]
[   16.635219] pci 0000:02:00.0:   bridge window [mem 0x92000000-0x928fffff]
[   16.635226] pci 0000:02:00.0:   bridge window [mem 0x91000000-0x91ffffff 64bit pref]
[   16.635244] pci_bus 0000:00: on NUMA node 0
[   16.635837] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
[   16.635987] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 *6 10 11 12 14 15)
[   16.636134] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 *5 6 10 11 12 14 15)
[   16.636280] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 5 6 10 *11 12 14 15)
[   16.636426] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 *11 12 14 15)
[   16.636571] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 *6 10 11 12 14 15)
[   16.636716] ACPI: PCI Interrupt Link [LNKG] (IRQs 3 4 *5 6 10 11 12 14 15)
[   16.636861] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
[   16.637639] ACPI: PCI Root Bridge [PC01] (domain 0000 [bus 17-39])
[   16.637646] acpi PNP0A08:01: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.637800] acpi PNP0A08:01: PCIe AER handled by firmware
[   16.638011] acpi PNP0A08:01: _OSC: platform does not support [SHPCHotplug LTR]
[   16.638397] acpi PNP0A08:01: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.638399] acpi PNP0A08:01: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.638931] PCI host bridge to bus 0000:17
[   16.638934] pci_bus 0000:17: root bus resource [io  0x4000-0x5fff window]
[   16.638937] pci_bus 0000:17: root bus resource [mem 0x9d800000-0xaaffffff window]
[   16.638939] pci_bus 0000:17: root bus resource [mem 0x381000000000-0x381fffffffff window]
[   16.638941] pci_bus 0000:17: root bus resource [bus 17-39]
[   16.638958] pci 0000:17:00.0: [8086:2030] type 01 class 0x060400
[   16.639065] pci 0000:17:00.0: PME# supported from D0 D3hot D3cold
[   16.639403] pci 0000:17:02.0: [8086:2032] type 01 class 0x060400
[   16.639487] pci 0000:17:02.0: PME# supported from D0 D3hot D3cold
[   16.639675] pci 0000:17:05.0: [8086:2034] type 00 class 0x088000
[   16.639848] pci 0000:17:05.2: [8086:2035] type 00 class 0x088000
[   16.640014] pci 0000:17:05.4: [8086:2036] type 00 class 0x080020
[   16.640027] pci 0000:17:05.4: reg 0x10: [mem 0x9dd00000-0x9dd00fff]
[   16.640189] pci 0000:17:08.0: [8086:208d] type 00 class 0x088000
[   16.640371] pci 0000:17:08.1: [8086:208d] type 00 class 0x088000
[   16.640504] pci 0000:17:08.2: [8086:208d] type 00 class 0x088000
[   16.640627] pci 0000:17:08.3: [8086:208d] type 00 class 0x088000
[   16.640758] pci 0000:17:08.4: [8086:208d] type 00 class 0x088000
[   16.640881] pci 0000:17:08.5: [8086:208d] type 00 class 0x088000
[   16.641012] pci 0000:17:08.6: [8086:208d] type 00 class 0x088000
[   16.641144] pci 0000:17:08.7: [8086:208d] type 00 class 0x088000
[   16.641267] pci 0000:17:09.0: [8086:208d] type 00 class 0x088000
[   16.641445] pci 0000:17:09.1: [8086:208d] type 00 class 0x088000
[   16.641577] pci 0000:17:09.2: [8086:208d] type 00 class 0x088000
[   16.641700] pci 0000:17:09.3: [8086:208d] type 00 class 0x088000
[   16.641832] pci 0000:17:09.4: [8086:208d] type 00 class 0x088000
[   16.641964] pci 0000:17:09.5: [8086:208d] type 00 class 0x088000
[   16.642088] pci 0000:17:09.6: [8086:208d] type 00 class 0x088000
[   16.642219] pci 0000:17:09.7: [8086:208d] type 00 class 0x088000
[   16.642343] pci 0000:17:0a.0: [8086:208d] type 00 class 0x088000
[   16.642529] pci 0000:17:0a.1: [8086:208d] type 00 class 0x088000
[   16.642661] pci 0000:17:0a.2: [8086:208d] type 00 class 0x088000
[   16.642785] pci 0000:17:0a.3: [8086:208d] type 00 class 0x088000
[   16.642925] pci 0000:17:0a.4: [8086:208d] type 00 class 0x088000
[   16.643059] pci 0000:17:0a.5: [8086:208d] type 00 class 0x088000
[   16.643184] pci 0000:17:0a.6: [8086:208d] type 00 class 0x088000
[   16.643317] pci 0000:17:0a.7: [8086:208d] type 00 class 0x088000
[   16.643449] pci 0000:17:0b.0: [8086:208d] type 00 class 0x088000
[   16.643625] pci 0000:17:0b.1: [8086:208d] type 00 class 0x088000
[   16.643756] pci 0000:17:0b.2: [8086:208d] type 00 class 0x088000
[   16.643887] pci 0000:17:0b.3: [8086:208d] type 00 class 0x088000
[   16.644019] pci 0000:17:0e.0: [8086:208e] type 00 class 0x088000
[   16.644170] pci 0000:17:0e.1: [8086:208e] type 00 class 0x088000
[   16.644301] pci 0000:17:0e.2: [8086:208e] type 00 class 0x088000
[   16.644424] pci 0000:17:0e.3: [8086:208e] type 00 class 0x088000
[   16.644553] pci 0000:17:0e.4: [8086:208e] type 00 class 0x088000
[   16.644699] pci 0000:17:0e.5: [8086:208e] type 00 class 0x088000
[   16.644831] pci 0000:17:0e.6: [8086:208e] type 00 class 0x088000
[   16.644961] pci 0000:17:0e.7: [8086:208e] type 00 class 0x088000
[   16.645084] pci 0000:17:0f.0: [8086:208e] type 00 class 0x088000
[   16.645236] pci 0000:17:0f.1: [8086:208e] type 00 class 0x088000
[   16.645367] pci 0000:17:0f.2: [8086:208e] type 00 class 0x088000
[   16.645490] pci 0000:17:0f.3: [8086:208e] type 00 class 0x088000
[   16.645621] pci 0000:17:0f.4: [8086:208e] type 00 class 0x088000
[   16.645780] pci 0000:17:0f.5: [8086:208e] type 00 class 0x088000
[   16.645904] pci 0000:17:0f.6: [8086:208e] type 00 class 0x088000
[   16.646035] pci 0000:17:0f.7: [8086:208e] type 00 class 0x088000
[   16.646159] pci 0000:17:10.0: [8086:208e] type 00 class 0x088000
[   16.646335] pci 0000:17:10.1: [8086:208e] type 00 class 0x088000
[   16.646466] pci 0000:17:10.2: [8086:208e] type 00 class 0x088000
[   16.646590] pci 0000:17:10.3: [8086:208e] type 00 class 0x088000
[   16.646722] pci 0000:17:10.4: [8086:208e] type 00 class 0x088000
[   16.646880] pci 0000:17:10.5: [8086:208e] type 00 class 0x088000
[   16.646993] pci 0000:17:10.6: [8086:208e] type 00 class 0x088000
[   16.647050] pci 0000:17:10.7: [8086:208e] type 00 class 0x088000
[   16.647109] pci 0000:17:11.0: [8086:208e] type 00 class 0x088000
[   16.647177] pci 0000:17:11.1: [8086:208e] type 00 class 0x088000
[   16.647236] pci 0000:17:11.2: [8086:208e] type 00 class 0x088000
[   16.647295] pci 0000:17:11.3: [8086:208e] type 00 class 0x088000
[   16.647358] pci 0000:17:1d.0: [8086:2054] type 00 class 0x088000
[   16.647449] pci 0000:17:1d.1: [8086:2055] type 00 class 0x088000
[   16.647508] pci 0000:17:1d.2: [8086:2056] type 00 class 0x088000
[   16.647562] pci 0000:17:1d.3: [8086:2057] type 00 class 0x088000
[   16.647625] pci 0000:17:1e.0: [8086:2080] type 00 class 0x088000
[   16.647693] pci 0000:17:1e.1: [8086:2081] type 00 class 0x088000
[   16.647746] pci 0000:17:1e.2: [8086:2082] type 00 class 0x088000
[   16.647804] pci 0000:17:1e.3: [8086:2083] type 00 class 0x088000
[   16.647919] pci 0000:17:1e.4: [8086:2084] type 00 class 0x088000
[   16.647995] pci 0000:17:1e.5: [8086:2085] type 00 class 0x088000
[   16.648055] pci 0000:17:1e.6: [8086:2086] type 00 class 0x088000
[   16.648140] pci 0000:18:00.0: [1000:005d] type 00 class 0x010400
[   16.648151] pci 0000:18:00.0: reg 0x10: [io  0x4000-0x40ff]
[   16.648157] pci 0000:18:00.0: reg 0x14: [mem 0x9dc00000-0x9dc0ffff 64bit]
[   16.648164] pci 0000:18:00.0: reg 0x1c: [mem 0x9db00000-0x9dbfffff 64bit]
[   16.648172] pci 0000:18:00.0: reg 0x30: [mem 0xfff00000-0xffffffff pref]
[   16.648212] pci 0000:18:00.0: supports D1 D2
[   16.648254] pci 0000:17:00.0: PCI bridge to [bus 18]
[   16.648256] pci 0000:17:00.0:   bridge window [io  0x4000-0x4fff]
[   16.648257] pci 0000:17:00.0:   bridge window [mem 0x9db00000-0x9dcfffff]
[   16.648379] pci 0000:19:00.0: [14e4:16d6] type 00 class 0x020000
[   16.648401] pci 0000:19:00.0: reg 0x10: [mem 0x9da10000-0x9da1ffff 64bit pref]
[   16.648410] pci 0000:19:00.0: reg 0x18: [mem 0x9d900000-0x9d9fffff 64bit pref]
[   16.648419] pci 0000:19:00.0: reg 0x20: [mem 0x9da22000-0x9da23fff 64bit pref]
[   16.648425] pci 0000:19:00.0: reg 0x30: [mem 0xfff80000-0xffffffff pref]
[   16.648485] pci 0000:19:00.0: PME# supported from D0 D3hot D3cold
[   16.648647] pci 0000:19:00.1: [14e4:16d6] type 00 class 0x020000
[   16.648667] pci 0000:19:00.1: reg 0x10: [mem 0x9da00000-0x9da0ffff 64bit pref]
[   16.648676] pci 0000:19:00.1: reg 0x18: [mem 0x9d800000-0x9d8fffff 64bit pref]
[   16.648685] pci 0000:19:00.1: reg 0x20: [mem 0x9da20000-0x9da21fff 64bit pref]
[   16.648691] pci 0000:19:00.1: reg 0x30: [mem 0xfff80000-0xffffffff pref]
[   16.648744] pci 0000:19:00.1: PME# supported from D0 D3hot D3cold
[   16.648873] pci 0000:17:02.0: PCI bridge to [bus 19]
[   16.648877] pci 0000:17:02.0:   bridge window [mem 0x9d800000-0x9dafffff 64bit pref]
[   16.648888] pci_bus 0000:17: on NUMA node 0
[   16.649032] ACPI: PCI Root Bridge [PC02] (domain 0000 [bus 3a-5c])
[   16.649035] acpi PNP0A08:02: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.649102] acpi PNP0A08:02: PCIe AER handled by firmware
[   16.649178] acpi PNP0A08:02: _OSC: platform does not support [SHPCHotplug LTR]
[   16.649318] acpi PNP0A08:02: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.649318] acpi PNP0A08:02: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.649472] PCI host bridge to bus 0000:3a
[   16.649473] pci_bus 0000:3a: root bus resource [io  0x6000-0x7fff window]
[   16.649474] pci_bus 0000:3a: root bus resource [mem 0xab000000-0xb87fffff window]
[   16.649475] pci_bus 0000:3a: root bus resource [mem 0x382000000000-0x382fffffffff window]
[   16.649476] pci_bus 0000:3a: root bus resource [bus 3a-5c]
[   16.649483] pci 0000:3a:00.0: [8086:2030] type 01 class 0x060400
[   16.649533] pci 0000:3a:00.0: PME# supported from D0 D3hot D3cold
[   16.649666] pci 0000:3a:05.0: [8086:2034] type 00 class 0x088000
[   16.649748] pci 0000:3a:05.2: [8086:2035] type 00 class 0x088000
[   16.649869] pci 0000:3a:05.4: [8086:2036] type 00 class 0x080020
[   16.649876] pci 0000:3a:05.4: reg 0x10: [mem 0xab200000-0xab200fff]
[   16.649945] pci 0000:3a:08.0: [8086:2066] type 00 class 0x088000
[   16.650018] pci 0000:3a:09.0: [8086:2066] type 00 class 0x088000
[   16.650091] pci 0000:3a:0a.0: [8086:2040] type 00 class 0x088000
[   16.650163] pci 0000:3a:0a.1: [8086:2041] type 00 class 0x088000
[   16.650225] pci 0000:3a:0a.2: [8086:2042] type 00 class 0x088000
[   16.650288] pci 0000:3a:0a.3: [8086:2043] type 00 class 0x088000
[   16.650344] pci 0000:3a:0a.4: [8086:2044] type 00 class 0x088000
[   16.650429] pci 0000:3a:0a.5: [8086:2045] type 00 class 0x088000
[   16.650491] pci 0000:3a:0a.6: [8086:2046] type 00 class 0x088000
[   16.650547] pci 0000:3a:0a.7: [8086:2047] type 00 class 0x088000
[   16.650609] pci 0000:3a:0b.0: [8086:2048] type 00 class 0x088000
[   16.650680] pci 0000:3a:0b.1: [8086:2049] type 00 class 0x088000
[   16.650741] pci 0000:3a:0b.2: [8086:204a] type 00 class 0x088000
[   16.650798] pci 0000:3a:0b.3: [8086:204b] type 00 class 0x088000
[   16.650864] pci 0000:3a:0c.0: [8086:2040] type 00 class 0x088000
[   16.650960] pci 0000:3a:0c.1: [8086:2041] type 00 class 0x088000
[   16.651025] pci 0000:3a:0c.2: [8086:2042] type 00 class 0x088000
[   16.651083] pci 0000:3a:0c.3: [8086:2043] type 00 class 0x088000
[   16.651147] pci 0000:3a:0c.4: [8086:2044] type 00 class 0x088000
[   16.651211] pci 0000:3a:0c.5: [8086:2045] type 00 class 0x088000
[   16.651269] pci 0000:3a:0c.6: [8086:2046] type 00 class 0x088000
[   16.651333] pci 0000:3a:0c.7: [8086:2047] type 00 class 0x088000
[   16.651397] pci 0000:3a:0d.0: [8086:2048] type 00 class 0x088000
[   16.651492] pci 0000:3a:0d.1: [8086:2049] type 00 class 0x088000
[   16.651556] pci 0000:3a:0d.2: [8086:204a] type 00 class 0x088000
[   16.651620] pci 0000:3a:0d.3: [8086:204b] type 00 class 0x088000
[   16.651727] pci 0000:3b:00.0: [1022:1470] type 01 class 0x060400
[   16.651742] pci 0000:3b:00.0: reg 0x10: [mem 0xab100000-0xab103fff]
[   16.652058] pci 0000:3b:00.0: PME# supported from D0 D3hot D3cold
[   16.652145] pci 0000:3a:00.0: PCI bridge to [bus 3b-3d]
[   16.652147] pci 0000:3a:00.0:   bridge window [io  0x6000-0x6fff]
[   16.652149] pci 0000:3a:00.0:   bridge window [mem 0xab000000-0xab1fffff]
[   16.652151] pci 0000:3a:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.652209] pci 0000:3c:00.0: [1022:1471] type 01 class 0x060400
[   16.652421] pci 0000:3c:00.0: PME# supported from D0 D3hot D3cold
[   16.652491] pci 0000:3b:00.0: PCI bridge to [bus 3c-3d]
[   16.652495] pci 0000:3b:00.0:   bridge window [io  0x6000-0x6fff]
[   16.652497] pci 0000:3b:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   16.652500] pci 0000:3b:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.652536] pci 0000:3d:00.0: [1002:6868] type 00 class 0x030000
[   16.652554] pci 0000:3d:00.0: reg 0x10: [mem 0x382fe0000000-0x382fefffffff 64bit pref]
[   16.652561] pci 0000:3d:00.0: reg 0x18: [mem 0x382ff0000000-0x382ff01fffff 64bit pref]
[   16.652565] pci 0000:3d:00.0: reg 0x20: [io  0x6000-0x60ff]
[   16.652569] pci 0000:3d:00.0: reg 0x24: [mem 0xab000000-0xab07ffff]
[   16.652574] pci 0000:3d:00.0: reg 0x30: [mem 0xfffe0000-0xffffffff pref]
[   16.652765] pci 0000:3d:00.0: PME# supported from D1 D2 D3hot D3cold
[   16.652832] pci 0000:3d:00.1: [1002:aaf8] type 00 class 0x040300
[   16.652846] pci 0000:3d:00.1: reg 0x10: [mem 0xab080000-0xab083fff]
[   16.653052] pci 0000:3d:00.1: PME# supported from D1 D2 D3hot D3cold
[   16.653116] pci 0000:3c:00.0: PCI bridge to [bus 3d]
[   16.653119] pci 0000:3c:00.0:   bridge window [io  0x6000-0x6fff]
[   16.653121] pci 0000:3c:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   16.653125] pci 0000:3c:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.653137] pci_bus 0000:3a: on NUMA node 0
[   16.653257] ACPI: PCI Root Bridge [PC03] (domain 0000 [bus 5d-7f])
[   16.653259] acpi PNP0A08:03: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.653322] acpi PNP0A08:03: PCIe AER handled by firmware
[   16.653398] acpi PNP0A08:03: _OSC: platform does not support [SHPCHotplug LTR]
[   16.653538] acpi PNP0A08:03: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.653539] acpi PNP0A08:03: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.653743] PCI host bridge to bus 0000:5d
[   16.653744] pci_bus 0000:5d: root bus resource [io  0x8000-0x9fff window]
[   16.653745] pci_bus 0000:5d: root bus resource [mem 0xb8800000-0xc5ffffff window]
[   16.653745] pci_bus 0000:5d: root bus resource [mem 0x383000000000-0x383fffffffff window]
[   16.653746] pci_bus 0000:5d: root bus resource [bus 5d-7f]
[   16.653755] pci 0000:5d:05.0: [8086:2034] type 00 class 0x088000
[   16.653859] pci 0000:5d:05.2: [8086:2035] type 00 class 0x088000
[   16.653936] pci 0000:5d:05.4: [8086:2036] type 00 class 0x080020
[   16.653944] pci 0000:5d:05.4: reg 0x10: [mem 0xb8800000-0xb8800fff]
[   16.654017] pci 0000:5d:0e.0: [8086:2058] type 00 class 0x110100
[   16.654089] pci 0000:5d:0e.1: [8086:2059] type 00 class 0x088000
[   16.654151] pci 0000:5d:0f.0: [8086:2058] type 00 class 0x110100
[   16.654229] pci 0000:5d:0f.1: [8086:2059] type 00 class 0x088000
[   16.654292] pci 0000:5d:10.0: [8086:2058] type 00 class 0x110100
[   16.654363] pci 0000:5d:10.1: [8086:2059] type 00 class 0x088000
[   16.654443] pci 0000:5d:12.0: [8086:204c] type 00 class 0x110100
[   16.654512] pci 0000:5d:12.1: [8086:204d] type 00 class 0x110100
[   16.654562] pci 0000:5d:12.2: [8086:204e] type 00 class 0x088000
[   16.654608] pci 0000:5d:12.4: [8086:204c] type 00 class 0x110100
[   16.654668] pci 0000:5d:12.5: [8086:204d] type 00 class 0x110100
[   16.654720] pci 0000:5d:15.0: [8086:2018] type 00 class 0x088000
[   16.654785] pci 0000:5d:15.1: [8086:2088] type 00 class 0x110100
[   16.654833] pci 0000:5d:16.0: [8086:2018] type 00 class 0x088000
[   16.654938] pci 0000:5d:16.1: [8086:2088] type 00 class 0x110100
[   16.654990] pci 0000:5d:16.4: [8086:2018] type 00 class 0x088000
[   16.655035] pci 0000:5d:16.5: [8086:2088] type 00 class 0x110100
[   16.655087] pci 0000:5d:17.0: [8086:2018] type 00 class 0x088000
[   16.655147] pci 0000:5d:17.1: [8086:2088] type 00 class 0x110100
[   16.655196] pci_bus 0000:5d: on NUMA node 0
[   16.655414] ACPI: PCI Root Bridge [PC06] (domain 0000 [bus 80-84])
[   16.655417] acpi PNP0A08:06: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.655479] acpi PNP0A08:06: PCIe AER handled by firmware
[   16.655555] acpi PNP0A08:06: _OSC: platform does not support [SHPCHotplug LTR]
[   16.655694] acpi PNP0A08:06: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.655695] acpi PNP0A08:06: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.655736] acpi PNP0A08:06: host bridge window [io  0x0000 window] (ignored, not CPU addressable)
[   16.655832] PCI host bridge to bus 0000:80
[   16.655833] pci_bus 0000:80: root bus resource [mem 0xc6000000-0xd37fffff window]
[   16.655834] pci_bus 0000:80: root bus resource [mem 0x384000000000-0x384fffffffff window]
[   16.655835] pci_bus 0000:80: root bus resource [bus 80-84]
[   16.655856] pci 0000:80:05.0: [8086:2024] type 00 class 0x088000
[   16.655951] pci 0000:80:05.2: [8086:2025] type 00 class 0x088000
[   16.656032] pci 0000:80:05.4: [8086:2026] type 00 class 0x080020
[   16.656041] pci 0000:80:05.4: reg 0x10: [mem 0xc6000000-0xc6000fff]
[   16.656146] pci 0000:80:08.0: [8086:2014] type 00 class 0x088000
[   16.656222] pci 0000:80:08.1: [8086:2015] type 00 class 0x110100
[   16.656280] pci 0000:80:08.2: [8086:2016] type 00 class 0x088000
[   16.656355] pci_bus 0000:80: on NUMA node 1
[   16.656448] ACPI: PCI Root Bridge [PC07] (domain 0000 [bus 85-ad])
[   16.656450] acpi PNP0A08:07: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.656516] acpi PNP0A08:07: PCIe AER handled by firmware
[   16.656591] acpi PNP0A08:07: _OSC: platform does not support [SHPCHotplug LTR]
[   16.656730] acpi PNP0A08:07: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.656731] acpi PNP0A08:07: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.656990] PCI host bridge to bus 0000:85
[   16.656991] pci_bus 0000:85: root bus resource [io  0xa000-0xbfff window]
[   16.656992] pci_bus 0000:85: root bus resource [mem 0xd3800000-0xe0ffffff window]
[   16.656993] pci_bus 0000:85: root bus resource [mem 0x385000000000-0x385fffffffff window]
[   16.656994] pci_bus 0000:85: root bus resource [bus 85-ad]
[   16.657003] pci 0000:85:05.0: [8086:2034] type 00 class 0x088000
[   16.657087] pci 0000:85:05.2: [8086:2035] type 00 class 0x088000
[   16.657173] pci 0000:85:05.4: [8086:2036] type 00 class 0x080020
[   16.657181] pci 0000:85:05.4: reg 0x10: [mem 0xd3800000-0xd3800fff]
[   16.657277] pci 0000:85:08.0: [8086:208d] type 00 class 0x088000
[   16.657347] pci 0000:85:08.1: [8086:208d] type 00 class 0x088000
[   16.657423] pci 0000:85:08.2: [8086:208d] type 00 class 0x088000
[   16.657482] pci 0000:85:08.3: [8086:208d] type 00 class 0x088000
[   16.657540] pci 0000:85:08.4: [8086:208d] type 00 class 0x088000
[   16.657599] pci 0000:85:08.5: [8086:208d] type 00 class 0x088000
[   16.657658] pci 0000:85:08.6: [8086:208d] type 00 class 0x088000
[   16.657711] pci 0000:85:08.7: [8086:208d] type 00 class 0x088000
[   16.657769] pci 0000:85:09.0: [8086:208d] type 00 class 0x088000
[   16.657836] pci 0000:85:09.1: [8086:208d] type 00 class 0x088000
[   16.657911] pci 0000:85:09.2: [8086:208d] type 00 class 0x088000
[   16.657970] pci 0000:85:09.3: [8086:208d] type 00 class 0x088000
[   16.658023] pci 0000:85:09.4: [8086:208d] type 00 class 0x088000
[   16.658106] pci 0000:85:09.5: [8086:208d] type 00 class 0x088000
[   16.658165] pci 0000:85:09.6: [8086:208d] type 00 class 0x088000
[   16.658218] pci 0000:85:09.7: [8086:208d] type 00 class 0x088000
[   16.658278] pci 0000:85:0a.0: [8086:208d] type 00 class 0x088000
[   16.658346] pci 0000:85:0a.1: [8086:208d] type 00 class 0x088000
[   16.658421] pci 0000:85:0a.2: [8086:208d] type 00 class 0x088000
[   16.658480] pci 0000:85:0a.3: [8086:208d] type 00 class 0x088000
[   16.658539] pci 0000:85:0a.4: [8086:208d] type 00 class 0x088000
[   16.658592] pci 0000:85:0a.5: [8086:208d] type 00 class 0x088000
[   16.658655] pci 0000:85:0a.6: [8086:208d] type 00 class 0x088000
[   16.658708] pci 0000:85:0a.7: [8086:208d] type 00 class 0x088000
[   16.658766] pci 0000:85:0b.0: [8086:208d] type 00 class 0x088000
[   16.658836] pci 0000:85:0b.1: [8086:208d] type 00 class 0x088000
[   16.658913] pci 0000:85:0b.2: [8086:208d] type 00 class 0x088000
[   16.658973] pci 0000:85:0b.3: [8086:208d] type 00 class 0x088000
[   16.659037] pci 0000:85:0e.0: [8086:208e] type 00 class 0x088000
[   16.659106] pci 0000:85:0e.1: [8086:208e] type 00 class 0x088000
[   16.659158] pci 0000:85:0e.2: [8086:208e] type 00 class 0x088000
[   16.659217] pci 0000:85:0e.3: [8086:208e] type 00 class 0x088000
[   16.659275] pci 0000:85:0e.4: [8086:208e] type 00 class 0x088000
[   16.659334] pci 0000:85:0e.5: [8086:208e] type 00 class 0x088000
[   16.659415] pci 0000:85:0e.6: [8086:208e] type 00 class 0x088000
[   16.659467] pci 0000:85:0e.7: [8086:208e] type 00 class 0x088000
[   16.659525] pci 0000:85:0f.0: [8086:208e] type 00 class 0x088000
[   16.659594] pci 0000:85:0f.1: [8086:208e] type 00 class 0x088000
[   16.659647] pci 0000:85:0f.2: [8086:208e] type 00 class 0x088000
[   16.659707] pci 0000:85:0f.3: [8086:208e] type 00 class 0x088000
[   16.659760] pci 0000:85:0f.4: [8086:208e] type 00 class 0x088000
[   16.659821] pci 0000:85:0f.5: [8086:208e] type 00 class 0x088000
[   16.659910] pci 0000:85:0f.6: [8086:208e] type 00 class 0x088000
[   16.659963] pci 0000:85:0f.7: [8086:208e] type 00 class 0x088000
[   16.660041] pci 0000:85:10.0: [8086:208e] type 00 class 0x088000
[   16.660109] pci 0000:85:10.1: [8086:208e] type 00 class 0x088000
[   16.660163] pci 0000:85:10.2: [8086:208e] type 00 class 0x088000
[   16.660223] pci 0000:85:10.3: [8086:208e] type 00 class 0x088000
[   16.660284] pci 0000:85:10.4: [8086:208e] type 00 class 0x088000
[   16.660337] pci 0000:85:10.5: [8086:208e] type 00 class 0x088000
[   16.660421] pci 0000:85:10.6: [8086:208e] type 00 class 0x088000
[   16.660474] pci 0000:85:10.7: [8086:208e] type 00 class 0x088000
[   16.660534] pci 0000:85:11.0: [8086:208e] type 00 class 0x088000
[   16.660602] pci 0000:85:11.1: [8086:208e] type 00 class 0x088000
[   16.660656] pci 0000:85:11.2: [8086:208e] type 00 class 0x088000
[   16.660716] pci 0000:85:11.3: [8086:208e] type 00 class 0x088000
[   16.660787] pci 0000:85:1d.0: [8086:2054] type 00 class 0x088000
[   16.660857] pci 0000:85:1d.1: [8086:2055] type 00 class 0x088000
[   16.660936] pci 0000:85:1d.2: [8086:2056] type 00 class 0x088000
[   16.660997] pci 0000:85:1d.3: [8086:2057] type 00 class 0x088000
[   16.661061] pci 0000:85:1e.0: [8086:2080] type 00 class 0x088000
[   16.661130] pci 0000:85:1e.1: [8086:2081] type 00 class 0x088000
[   16.661190] pci 0000:85:1e.2: [8086:2082] type 00 class 0x088000
[   16.661243] pci 0000:85:1e.3: [8086:2083] type 00 class 0x088000
[   16.661304] pci 0000:85:1e.4: [8086:2084] type 00 class 0x088000
[   16.661365] pci 0000:85:1e.5: [8086:2085] type 00 class 0x088000
[   16.661443] pci 0000:85:1e.6: [8086:2086] type 00 class 0x088000
[   16.661505] pci_bus 0000:85: on NUMA node 1
[   16.661624] ACPI: PCI Root Bridge [PC08] (domain 0000 [bus ae-d6])
[   16.661626] acpi PNP0A08:08: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.661685] acpi PNP0A08:08: PCIe AER handled by firmware
[   16.661756] acpi PNP0A08:08: _OSC: platform does not support [SHPCHotplug LTR]
[   16.661886] acpi PNP0A08:08: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.661887] acpi PNP0A08:08: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.662062] PCI host bridge to bus 0000:ae
[   16.662063] pci_bus 0000:ae: root bus resource [io  0xc000-0xdfff window]
[   16.662064] pci_bus 0000:ae: root bus resource [mem 0xe1000000-0xee7fffff window]
[   16.662064] pci_bus 0000:ae: root bus resource [mem 0x386000000000-0x386fffffffff window]
[   16.662065] pci_bus 0000:ae: root bus resource [bus ae-d6]
[   16.662073] pci 0000:ae:00.0: [8086:2030] type 01 class 0x060400
[   16.662130] pci 0000:ae:00.0: PME# supported from D0 D3hot D3cold
[   16.662268] pci 0000:ae:05.0: [8086:2034] type 00 class 0x088000
[   16.662347] pci 0000:ae:05.2: [8086:2035] type 00 class 0x088000
[   16.662422] pci 0000:ae:05.4: [8086:2036] type 00 class 0x080020
[   16.662430] pci 0000:ae:05.4: reg 0x10: [mem 0xe3100000-0xe3100fff]
[   16.662501] pci 0000:ae:08.0: [8086:2066] type 00 class 0x088000
[   16.662578] pci 0000:ae:09.0: [8086:2066] type 00 class 0x088000
[   16.662654] pci 0000:ae:0a.0: [8086:2040] type 00 class 0x088000
[   16.662756] pci 0000:ae:0a.1: [8086:2041] type 00 class 0x088000
[   16.662822] pci 0000:ae:0a.2: [8086:2042] type 00 class 0x088000
[   16.662889] pci 0000:ae:0a.3: [8086:2043] type 00 class 0x088000
[   16.662948] pci 0000:ae:0a.4: [8086:2044] type 00 class 0x088000
[   16.663013] pci 0000:ae:0a.5: [8086:2045] type 00 class 0x088000
[   16.663079] pci 0000:ae:0a.6: [8086:2046] type 00 class 0x088000
[   16.663138] pci 0000:ae:0a.7: [8086:2047] type 00 class 0x088000
[   16.663204] pci 0000:ae:0b.0: [8086:2048] type 00 class 0x088000
[   16.663311] pci 0000:ae:0b.1: [8086:2049] type 00 class 0x088000
[   16.663370] pci 0000:ae:0b.2: [8086:204a] type 00 class 0x088000
[   16.663442] pci 0000:ae:0b.3: [8086:204b] type 00 class 0x088000
[   16.663509] pci 0000:ae:0c.0: [8086:2040] type 00 class 0x088000
[   16.663584] pci 0000:ae:0c.1: [8086:2041] type 00 class 0x088000
[   16.663644] pci 0000:ae:0c.2: [8086:2042] type 00 class 0x088000
[   16.663711] pci 0000:ae:0c.3: [8086:2043] type 00 class 0x088000
[   16.663779] pci 0000:ae:0c.4: [8086:2044] type 00 class 0x088000
[   16.663864] pci 0000:ae:0c.5: [8086:2045] type 00 class 0x088000
[   16.663932] pci 0000:ae:0c.6: [8086:2046] type 00 class 0x088000
[   16.663998] pci 0000:ae:0c.7: [8086:2047] type 00 class 0x088000
[   16.664058] pci 0000:ae:0d.0: [8086:2048] type 00 class 0x088000
[   16.664132] pci 0000:ae:0d.1: [8086:2049] type 00 class 0x088000
[   16.664199] pci 0000:ae:0d.2: [8086:204a] type 00 class 0x088000
[   16.664269] pci 0000:ae:0d.3: [8086:204b] type 00 class 0x088000
[   16.664407] pci 0000:af:00.0: [8086:158b] type 00 class 0x020000
[   16.664426] pci 0000:af:00.0: reg 0x10: [mem 0xe2000000-0xe2ffffff 64bit pref]
[   16.664439] pci 0000:af:00.0: reg 0x1c: [mem 0xe3008000-0xe300ffff 64bit pref]
[   16.664450] pci 0000:af:00.0: reg 0x30: [mem 0xfff80000-0xffffffff pref]
[   16.664797] pci 0000:af:00.0: PME# supported from D0 D3hot D3cold
[   16.664818] pci 0000:af:00.0: reg 0x184: [mem 0x00000000-0x0000ffff 64bit pref]
[   16.664820] pci 0000:af:00.0: VF(n) BAR0 space: [mem 0x00000000-0x003fffff 64bit pref] (contains BAR0 for 64 VFs)
[   16.664831] pci 0000:af:00.0: reg 0x190: [mem 0x00000000-0x00003fff 64bit pref]
[   16.664832] pci 0000:af:00.0: VF(n) BAR3 space: [mem 0x00000000-0x000fffff 64bit pref] (contains BAR3 for 64 VFs)
[   16.665045] pci 0000:af:00.1: [8086:158b] type 00 class 0x020000
[   16.665063] pci 0000:af:00.1: reg 0x10: [mem 0xe1000000-0xe1ffffff 64bit pref]
[   16.665076] pci 0000:af:00.1: reg 0x1c: [mem 0xe3000000-0xe3007fff 64bit pref]
[   16.665086] pci 0000:af:00.1: reg 0x30: [mem 0xfff80000-0xffffffff pref]
[   16.665267] pci 0000:af:00.1: PME# supported from D0 D3hot D3cold
[   16.665285] pci 0000:af:00.1: reg 0x184: [mem 0x00000000-0x0000ffff 64bit pref]
[   16.665286] pci 0000:af:00.1: VF(n) BAR0 space: [mem 0x00000000-0x003fffff 64bit pref] (contains BAR0 for 64 VFs)
[   16.665297] pci 0000:af:00.1: reg 0x190: [mem 0x00000000-0x00003fff 64bit pref]
[   16.665298] pci 0000:af:00.1: VF(n) BAR3 space: [mem 0x00000000-0x000fffff 64bit pref] (contains BAR3 for 64 VFs)
[   16.665469] pci 0000:ae:00.0: PCI bridge to [bus af]
[   16.665473] pci 0000:ae:00.0:   bridge window [mem 0xe1000000-0xe30fffff 64bit pref]
[   16.665479] pci_bus 0000:ae: on NUMA node 1
[   16.665648] ACPI: PCI Root Bridge [PC09] (domain 0000 [bus d7-ff])
[   16.665651] acpi PNP0A08:09: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[   16.665709] acpi PNP0A08:09: PCIe AER handled by firmware
[   16.665781] acpi PNP0A08:09: _OSC: platform does not support [SHPCHotplug LTR]
[   16.665911] acpi PNP0A08:09: _OSC: OS now controls [PCIeHotplug PME PCIeCapability]
[   16.665912] acpi PNP0A08:09: FADT indicates ASPM is unsupported, using BIOS configuration
[   16.666073] PCI host bridge to bus 0000:d7
[   16.666074] pci_bus 0000:d7: root bus resource [io  0xe000-0xffff window]
[   16.666075] pci_bus 0000:d7: root bus resource [mem 0xee800000-0xfbffffff window]
[   16.666076] pci_bus 0000:d7: root bus resource [mem 0x387000000000-0x387fffffffff window]
[   16.666077] pci_bus 0000:d7: root bus resource [bus d7-ff]
[   16.666086] pci 0000:d7:05.0: [8086:2034] type 00 class 0x088000
[   16.666168] pci 0000:d7:05.2: [8086:2035] type 00 class 0x088000
[   16.666239] pci 0000:d7:05.4: [8086:2036] type 00 class 0x080020
[   16.666248] pci 0000:d7:05.4: reg 0x10: [mem 0xee800000-0xee800fff]
[   16.666331] pci 0000:d7:0e.0: [8086:2058] type 00 class 0x110100
[   16.666404] pci 0000:d7:0e.1: [8086:2059] type 00 class 0x088000
[   16.666464] pci 0000:d7:0f.0: [8086:2058] type 00 class 0x110100
[   16.666543] pci 0000:d7:0f.1: [8086:2059] type 00 class 0x088000
[   16.666632] pci 0000:d7:10.0: [8086:2058] type 00 class 0x110100
[   16.666706] pci 0000:d7:10.1: [8086:2059] type 00 class 0x088000
[   16.666773] pci 0000:d7:12.0: [8086:204c] type 00 class 0x110100
[   16.666848] pci 0000:d7:12.1: [8086:204d] type 00 class 0x110100
[   16.666894] pci 0000:d7:12.2: [8086:204e] type 00 class 0x088000
[   16.666947] pci 0000:d7:12.4: [8086:204c] type 00 class 0x110100
[   16.667010] pci 0000:d7:12.5: [8086:204d] type 00 class 0x110100
[   16.667057] pci 0000:d7:15.0: [8086:2018] type 00 class 0x088000
[   16.667138] pci 0000:d7:15.1: [8086:2088] type 00 class 0x110100
[   16.667190] pci 0000:d7:16.0: [8086:2018] type 00 class 0x088000
[   16.667249] pci 0000:d7:16.1: [8086:2088] type 00 class 0x110100
[   16.667294] pci 0000:d7:16.4: [8086:2018] type 00 class 0x088000
[   16.667346] pci 0000:d7:16.5: [8086:2088] type 00 class 0x110100
[   16.667392] pci 0000:d7:17.0: [8086:2018] type 00 class 0x088000
[   16.667451] pci 0000:d7:17.1: [8086:2088] type 00 class 0x110100
[   16.667507] pci_bus 0000:d7: on NUMA node 1
[   16.670814] HMAT: Memory (0x0 length 0x80000000) Flags:0003 Processor Domain:0 Memory Domain:0
[   16.670814] HMAT: Memory (0x100000000 length 0x5dc0000000) Flags:0003 Processor Domain:0 Memory Domain:0
[   16.670814] HMAT: Memory (0x5ec0000000 length 0x5e80000000) Flags:0003 Processor Domain:1 Memory Domain:1
[   16.670814] HMAT: Cache: Domain:0 Size:103079215104 Attrs:00401111 SMBIOS Handles:0
[   16.670814] HMAT: Cache: Domain:1 Size:103079215104 Attrs:00401111 SMBIOS Handles:0
[   16.670854] iommu: Default domain type: Passthrough (set via kernel command line)
[   16.670899] pci 0000:03:00.0: vgaarb: setting as boot VGA device
[   16.670899] pci 0000:03:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[   16.670899] pci 0000:3d:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[   16.670899] pci 0000:03:00.0: vgaarb: bridge control possible
[   16.670899] pci 0000:3d:00.0: vgaarb: bridge control possible
[   16.670899] vgaarb: loaded
[   16.671239] SCSI subsystem initialized
[   16.671383] libata version 3.00 loaded.
[   16.671383] ACPI: bus type USB registered
[   16.671383] usbcore: registered new interface driver usbfs
[   16.671383] usbcore: registered new interface driver hub
[   16.671383] usbcore: registered new device driver usb
[   16.671383] pps_core: LinuxPPS API ver. 1 registered
[   16.671383] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[   16.671383] PTP clock support registered
[   16.671383] EDAC MC: Ver: 3.0.0
[   16.671383] Registered efivars operations
[   16.671383] PCI: Using ACPI for IRQ routing
[   16.673658] PCI: pci_cache_line_size set to 64 bytes
[   16.673914] e820: reserve RAM buffer [mem 0x4faf2020-0x4fffffff]
[   16.673916] e820: reserve RAM buffer [mem 0x4fb27020-0x4fffffff]
[   16.673917] e820: reserve RAM buffer [mem 0x4fb5c020-0x4fffffff]
[   16.673918] e820: reserve RAM buffer [mem 0x4fb76020-0x4fffffff]
[   16.673919] e820: reserve RAM buffer [mem 0x4fba6020-0x4fffffff]
[   16.673920] e820: reserve RAM buffer [mem 0x4fbd6020-0x4fffffff]
[   16.673921] e820: reserve RAM buffer [mem 0x4fbef020-0x4fffffff]
[   16.673921] e820: reserve RAM buffer [mem 0x4fbf8020-0x4fffffff]
[   16.673922] e820: reserve RAM buffer [mem 0x4fc2a020-0x4fffffff]
[   16.673923] e820: reserve RAM buffer [mem 0x50264000-0x53ffffff]
[   16.673923] e820: reserve RAM buffer [mem 0x682ff000-0x6bffffff]
[   16.674307] NetLabel: Initializing
[   16.674308] NetLabel:  domain hash size = 128
[   16.674308] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[   16.674320] NetLabel:  unlabeled traffic allowed by default
[   16.675624] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
[   16.675627] hpet0: 8 comparators, 64-bit 24.000000 MHz counter
[   16.678943] clocksource: Switched to clocksource tsc-early
[   16.697101] *** VALIDATE bpf ***
[   16.697399] VFS: Disk quotas dquot_6.6.0
[   16.697490] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[   16.697513] *** VALIDATE ramfs ***
[   16.697542] *** VALIDATE hugetlbfs ***
[   16.697817] AppArmor: AppArmor Filesystem Enabled
[   16.697844] pnp: PnP ACPI init
[   16.698795] pnp 00:00: Plug and Play ACPI device, IDs PNP0b00 (active)
[   16.698977] system 00:01: [io  0x0500-0x05fe] has been reserved
[   16.698978] system 00:01: [io  0x0400-0x047f] has been reserved
[   16.698980] system 00:01: [io  0x0600-0x061f] has been reserved
[   16.698981] system 00:01: [io  0x0ca0-0x0ca5] has been reserved
[   16.698982] system 00:01: [io  0x0880-0x0883] has been reserved
[   16.698983] system 00:01: [io  0x0800-0x081f] has been reserved
[   16.698985] system 00:01: [mem 0xfed1c000-0xfed3ffff] has been reserved
[   16.698985] system 00:01: [mem 0xfed45000-0xfed8bfff] has been reserved
[   16.698986] system 00:01: [mem 0xff000000-0xffffffff] has been reserved
[   16.698987] system 00:01: [mem 0xfee00000-0xfeefffff] has been reserved
[   16.698988] system 00:01: [mem 0xfed12000-0xfed1200f] has been reserved
[   16.698989] system 00:01: [mem 0xfed12010-0xfed1201f] has been reserved
[   16.698990] system 00:01: [mem 0xfed1b000-0xfed1bfff] has been reserved
[   16.698993] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[   16.699238] pnp 00:02: Plug and Play ACPI device, IDs PNP0501 (active)
[   16.699432] pnp 00:03: Plug and Play ACPI device, IDs PNP0501 (active)
[   16.699595] system 00:04: [mem 0xfd000000-0xfdabffff] has been reserved
[   16.699596] system 00:04: [mem 0xfdad0000-0xfdadffff] has been reserved
[   16.699597] system 00:04: [mem 0xfdb00000-0xfdffffff] has been reserved
[   16.699598] system 00:04: [mem 0xfe000000-0xfe00ffff] has been reserved
[   16.699599] system 00:04: [mem 0xfe011000-0xfe01ffff] has been reserved
[   16.699600] system 00:04: [mem 0xfe036000-0xfe03bfff] has been reserved
[   16.699601] system 00:04: [mem 0xfe03d000-0xfe3fffff] has been reserved
[   16.699602] system 00:04: [mem 0xfe410000-0xfe7fffff] has been reserved
[   16.699605] system 00:04: Plug and Play ACPI device, IDs PNP0c02 (active)
[   16.699944] system 00:05: [io  0x1000-0x10fe] has been reserved
[   16.699947] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[   16.700791] pnp: PnP ACPI: found 6 devices
[   16.702364] thermal_sys: Registered thermal governor 'fair_share'
[   16.702364] thermal_sys: Registered thermal governor 'bang_bang'
[   16.702365] thermal_sys: Registered thermal governor 'step_wise'
[   16.702365] thermal_sys: Registered thermal governor 'user_space'
[   16.702366] thermal_sys: Registered thermal governor 'power_allocator'
[   16.706857] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[   16.706886] pci 0000:01:00.0: can't claim BAR 6 [mem 0xfffc0000-0xffffffff pref]: no compatible bridge window
[   16.706887] pci 0000:01:00.1: can't claim BAR 6 [mem 0xfffc0000-0xffffffff pref]: no compatible bridge window
[   16.706888] pci 0000:18:00.0: can't claim BAR 6 [mem 0xfff00000-0xffffffff pref]: no compatible bridge window
[   16.706889] pci 0000:19:00.0: can't claim BAR 6 [mem 0xfff80000-0xffffffff pref]: no compatible bridge window
[   16.706890] pci 0000:19:00.1: can't claim BAR 6 [mem 0xfff80000-0xffffffff pref]: no compatible bridge window
[   16.706893] pci 0000:3d:00.0: can't claim BAR 6 [mem 0xfffe0000-0xffffffff pref]: no compatible bridge window
[   16.706898] pci 0000:af:00.0: can't claim BAR 6 [mem 0xfff80000-0xffffffff pref]: no compatible bridge window
[   16.706898] pci 0000:af:00.1: can't claim BAR 6 [mem 0xfff80000-0xffffffff pref]: no compatible bridge window
[   16.706910] pci 0000:00:1c.0: BAR 14: assigned [mem 0x90000000-0x900fffff]
[   16.706913] pci 0000:01:00.0: BAR 6: assigned [mem 0x90000000-0x9003ffff pref]
[   16.706914] pci 0000:01:00.1: BAR 6: assigned [mem 0x90040000-0x9007ffff pref]
[   16.706915] pci 0000:00:1c.0: PCI bridge to [bus 01]
[   16.706918] pci 0000:00:1c.0:   bridge window [mem 0x90000000-0x900fffff]
[   16.706920] pci 0000:00:1c.0:   bridge window [mem 0x92900000-0x929fffff 64bit pref]
[   16.706924] pci 0000:02:00.0: PCI bridge to [bus 03]
[   16.706928] pci 0000:02:00.0:   bridge window [mem 0x92000000-0x928fffff]
[   16.706931] pci 0000:02:00.0:   bridge window [mem 0x91000000-0x91ffffff 64bit pref]
[   16.706936] pci 0000:00:1c.4: PCI bridge to [bus 02-03]
[   16.706939] pci 0000:00:1c.4:   bridge window [mem 0x92000000-0x928fffff]
[   16.706941] pci 0000:00:1c.4:   bridge window [mem 0x91000000-0x91ffffff 64bit pref]
[   16.706944] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
[   16.706945] pci_bus 0000:00: resource 5 [io  0x1000-0x3fff window]
[   16.706946] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
[   16.706947] pci_bus 0000:00: resource 7 [mem 0x000c4000-0x000c7fff window]
[   16.706948] pci_bus 0000:00: resource 8 [mem 0xfe010000-0xfe010fff window]
[   16.706948] pci_bus 0000:00: resource 9 [mem 0x90000000-0x9d7fffff window]
[   16.706949] pci_bus 0000:00: resource 10 [mem 0x380000000000-0x380fffffffff window]
[   16.706950] pci_bus 0000:01: resource 1 [mem 0x90000000-0x900fffff]
[   16.706951] pci_bus 0000:01: resource 2 [mem 0x92900000-0x929fffff 64bit pref]
[   16.706952] pci_bus 0000:02: resource 1 [mem 0x92000000-0x928fffff]
[   16.706953] pci_bus 0000:02: resource 2 [mem 0x91000000-0x91ffffff 64bit pref]
[   16.706953] pci_bus 0000:03: resource 1 [mem 0x92000000-0x928fffff]
[   16.706954] pci_bus 0000:03: resource 2 [mem 0x91000000-0x91ffffff 64bit pref]
[   16.707066] pci 0000:17:02.0: BAR 14: assigned [mem 0x9de00000-0x9defffff]
[   16.707068] pci 0000:18:00.0: BAR 6: no space for [mem size 0x00100000 pref]
[   16.707069] pci 0000:18:00.0: BAR 6: failed to assign [mem size 0x00100000 pref]
[   16.707070] pci 0000:17:00.0: PCI bridge to [bus 18]
[   16.707071] pci 0000:17:00.0:   bridge window [io  0x4000-0x4fff]
[   16.707073] pci 0000:17:00.0:   bridge window [mem 0x9db00000-0x9dcfffff]
[   16.707077] pci 0000:19:00.0: BAR 6: assigned [mem 0x9de00000-0x9de7ffff pref]
[   16.707077] pci 0000:19:00.1: BAR 6: assigned [mem 0x9de80000-0x9defffff pref]
[   16.707078] pci 0000:17:02.0: PCI bridge to [bus 19]
[   16.707080] pci 0000:17:02.0:   bridge window [mem 0x9de00000-0x9defffff]
[   16.707082] pci 0000:17:02.0:   bridge window [mem 0x9d800000-0x9dafffff 64bit pref]
[   16.707085] pci_bus 0000:17: resource 4 [io  0x4000-0x5fff window]
[   16.707086] pci_bus 0000:17: resource 5 [mem 0x9d800000-0xaaffffff window]
[   16.707087] pci_bus 0000:17: resource 6 [mem 0x381000000000-0x381fffffffff window]
[   16.707088] pci_bus 0000:18: resource 0 [io  0x4000-0x4fff]
[   16.707088] pci_bus 0000:18: resource 1 [mem 0x9db00000-0x9dcfffff]
[   16.707089] pci_bus 0000:19: resource 1 [mem 0x9de00000-0x9defffff]
[   16.707090] pci_bus 0000:19: resource 2 [mem 0x9d800000-0x9dafffff 64bit pref]
[   16.707112] pci 0000:3d:00.0: BAR 6: assigned [mem 0xab0a0000-0xab0bffff pref]
[   16.707113] pci 0000:3c:00.0: PCI bridge to [bus 3d]
[   16.707114] pci 0000:3c:00.0:   bridge window [io  0x6000-0x6fff]
[   16.707117] pci 0000:3c:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   16.707119] pci 0000:3c:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707122] pci 0000:3b:00.0: PCI bridge to [bus 3c-3d]
[   16.707124] pci 0000:3b:00.0:   bridge window [io  0x6000-0x6fff]
[   16.707126] pci 0000:3b:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   16.707128] pci 0000:3b:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707132] pci 0000:3a:00.0: PCI bridge to [bus 3b-3d]
[   16.707133] pci 0000:3a:00.0:   bridge window [io  0x6000-0x6fff]
[   16.707135] pci 0000:3a:00.0:   bridge window [mem 0xab000000-0xab1fffff]
[   16.707137] pci 0000:3a:00.0:   bridge window [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707140] pci_bus 0000:3a: resource 4 [io  0x6000-0x7fff window]
[   16.707140] pci_bus 0000:3a: resource 5 [mem 0xab000000-0xb87fffff window]
[   16.707141] pci_bus 0000:3a: resource 6 [mem 0x382000000000-0x382fffffffff window]
[   16.707142] pci_bus 0000:3b: resource 0 [io  0x6000-0x6fff]
[   16.707143] pci_bus 0000:3b: resource 1 [mem 0xab000000-0xab1fffff]
[   16.707143] pci_bus 0000:3b: resource 2 [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707144] pci_bus 0000:3c: resource 0 [io  0x6000-0x6fff]
[   16.707145] pci_bus 0000:3c: resource 1 [mem 0xab000000-0xab0fffff]
[   16.707146] pci_bus 0000:3c: resource 2 [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707146] pci_bus 0000:3d: resource 0 [io  0x6000-0x6fff]
[   16.707147] pci_bus 0000:3d: resource 1 [mem 0xab000000-0xab0fffff]
[   16.707148] pci_bus 0000:3d: resource 2 [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   16.707162] pci_bus 0000:5d: resource 4 [io  0x8000-0x9fff window]
[   16.707163] pci_bus 0000:5d: resource 5 [mem 0xb8800000-0xc5ffffff window]
[   16.707164] pci_bus 0000:5d: resource 6 [mem 0x383000000000-0x383fffffffff window]
[   16.707185] pci_bus 0000:80: resource 4 [mem 0xc6000000-0xd37fffff window]
[   16.707185] pci_bus 0000:80: resource 5 [mem 0x384000000000-0x384fffffffff window]
[   16.707199] pci_bus 0000:85: resource 4 [io  0xa000-0xbfff window]
[   16.707200] pci_bus 0000:85: resource 5 [mem 0xd3800000-0xe0ffffff window]
[   16.707201] pci_bus 0000:85: resource 6 [mem 0x385000000000-0x385fffffffff window]
[   16.707214] pci_bus 0000:ae: max bus depth: 1 pci_try_num: 2
[   16.707219] pci 0000:ae:00.0: BAR 14: assigned [mem 0xe3200000-0xe3cfffff]
[   16.707221] pci 0000:af:00.0: BAR 6: assigned [mem 0xe3200000-0xe327ffff pref]
[   16.707222] pci 0000:af:00.1: BAR 6: assigned [mem 0xe3280000-0xe32fffff pref]
[   16.707224] pci 0000:af:00.0: BAR 7: assigned [mem 0xe3300000-0xe36fffff 64bit pref]
[   16.707228] pci 0000:af:00.1: BAR 7: assigned [mem 0xe3700000-0xe3afffff 64bit pref]
[   16.707231] pci 0000:af:00.0: BAR 10: assigned [mem 0xe3b00000-0xe3bfffff 64bit pref]
[   16.707234] pci 0000:af:00.1: BAR 10: assigned [mem 0xe3c00000-0xe3cfffff 64bit pref]
[   16.707237] pci 0000:ae:00.0: PCI bridge to [bus af]
[   16.707239] pci 0000:ae:00.0:   bridge window [mem 0xe3200000-0xe3cfffff]
[   16.707241] pci 0000:ae:00.0:   bridge window [mem 0xe1000000-0xe30fffff 64bit pref]
[   16.707244] pci_bus 0000:ae: resource 4 [io  0xc000-0xdfff window]
[   16.707245] pci_bus 0000:ae: resource 5 [mem 0xe1000000-0xee7fffff window]
[   16.707246] pci_bus 0000:ae: resource 6 [mem 0x386000000000-0x386fffffffff window]
[   16.707247] pci_bus 0000:af: resource 1 [mem 0xe3200000-0xe3cfffff]
[   16.707247] pci_bus 0000:af: resource 2 [mem 0xe1000000-0xe30fffff 64bit pref]
[   16.707276] pci_bus 0000:d7: resource 4 [io  0xe000-0xffff window]
[   16.707277] pci_bus 0000:d7: resource 5 [mem 0xee800000-0xfbffffff window]
[   16.707278] pci_bus 0000:d7: resource 6 [mem 0x387000000000-0x387fffffffff window]
[   16.707470] NET: Registered protocol family 2
[   16.709756] tcp_listen_portaddr_hash hash table entries: 65536 (order: 8, 1048576 bytes, vmalloc)
[   16.713478] TCP established hash table entries: 524288 (order: 10, 4194304 bytes, vmalloc)
[   16.714859] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, vmalloc)
[   16.714927] TCP: Hash tables configured (established 524288 bind 65536)
[   16.717004] UDP hash table entries: 65536 (order: 9, 2097152 bytes, vmalloc)
[   16.719009] UDP-Lite hash table entries: 65536 (order: 9, 2097152 bytes, vmalloc)
[   16.719504] NET: Registered protocol family 1
[   16.719509] NET: Registered protocol family 44
[   16.719860] pci 0000:03:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[   16.719867] pci 0000:17:05.0: disabled boot interrupts on device [8086:2034]
[   16.719950] pci 0000:3a:05.0: disabled boot interrupts on device [8086:2034]
[   16.720004] pci 0000:3d:00.1: D0 power state depends on 0000:3d:00.0
[   16.720009] pci 0000:5d:05.0: disabled boot interrupts on device [8086:2034]
[   16.720042] pci 0000:85:05.0: disabled boot interrupts on device [8086:2034]
[   16.720126] pci 0000:ae:05.0: disabled boot interrupts on device [8086:2034]
[   16.720165] pci 0000:d7:05.0: disabled boot interrupts on device [8086:2034]
[   16.720191] PCI: CLS 0 bytes, default 64
[   16.720272] Trying to unpack rootfs image as initramfs...
[   17.263738] Freeing initrd memory: 41480K
[   17.265605] DMAR: dmar5: Using Queued invalidation
[   17.265612] DMAR: dmar4: Using Queued invalidation
[   17.265617] DMAR: dmar2: Using Queued invalidation
[   17.265649] DMAR: dmar7: Using Queued invalidation
[   17.267761] pci 0000:00:00.0: Adding to iommu group 0
[   17.267806] pci 0000:00:05.0: Adding to iommu group 1
[   17.267849] pci 0000:00:05.2: Adding to iommu group 2
[   17.267899] pci 0000:00:05.4: Adding to iommu group 3
[   17.267943] pci 0000:00:08.0: Adding to iommu group 4
[   17.268020] pci 0000:00:08.1: Adding to iommu group 5
[   17.268060] pci 0000:00:08.2: Adding to iommu group 6
[   17.268181] pci 0000:00:11.0: Adding to iommu group 7
[   17.268223] pci 0000:00:11.5: Adding to iommu group 7
[   17.268337] pci 0000:00:14.0: Adding to iommu group 8
[   17.268379] pci 0000:00:14.2: Adding to iommu group 8
[   17.268526] pci 0000:00:16.0: Adding to iommu group 9
[   17.268568] pci 0000:00:16.1: Adding to iommu group 9
[   17.268610] pci 0000:00:16.4: Adding to iommu group 9
[   17.268651] pci 0000:00:17.0: Adding to iommu group 10
[   17.268698] pci 0000:00:1c.0: Adding to iommu group 11
[   17.268749] pci 0000:00:1c.4: Adding to iommu group 12
[   17.268936] pci 0000:00:1f.0: Adding to iommu group 13
[   17.268980] pci 0000:00:1f.2: Adding to iommu group 13
[   17.269053] pci 0000:00:1f.4: Adding to iommu group 13
[   17.269097] pci 0000:00:1f.5: Adding to iommu group 13
[   17.269228] pci 0000:01:00.0: Adding to iommu group 14
[   17.269287] pci 0000:01:00.1: Adding to iommu group 14
[   17.269338] pci 0000:02:00.0: Adding to iommu group 15
[   17.272529] pci 0000:02:00.0: Using iommu dma mapping
[   17.272537] pci 0000:03:00.0: Adding to iommu group 15
[   17.272591] pci 0000:17:00.0: Adding to iommu group 16
[   17.272644] pci 0000:17:02.0: Adding to iommu group 17
[   17.272692] pci 0000:17:05.0: Adding to iommu group 18
[   17.272735] pci 0000:17:05.2: Adding to iommu group 19
[   17.272778] pci 0000:17:05.4: Adding to iommu group 20
[   17.273098] pci 0000:17:08.0: Adding to iommu group 21
[   17.273140] pci 0000:17:08.1: Adding to iommu group 21
[   17.273186] pci 0000:17:08.2: Adding to iommu group 21
[   17.273228] pci 0000:17:08.3: Adding to iommu group 21
[   17.273270] pci 0000:17:08.4: Adding to iommu group 21
[   17.273312] pci 0000:17:08.5: Adding to iommu group 21
[   17.273354] pci 0000:17:08.6: Adding to iommu group 21
[   17.273402] pci 0000:17:08.7: Adding to iommu group 21
[   17.273709] pci 0000:17:09.0: Adding to iommu group 22
[   17.273752] pci 0000:17:09.1: Adding to iommu group 22
[   17.273795] pci 0000:17:09.2: Adding to iommu group 22
[   17.273838] pci 0000:17:09.3: Adding to iommu group 22
[   17.273880] pci 0000:17:09.4: Adding to iommu group 22
[   17.273923] pci 0000:17:09.5: Adding to iommu group 22
[   17.273965] pci 0000:17:09.6: Adding to iommu group 22
[   17.274007] pci 0000:17:09.7: Adding to iommu group 22
[   17.274310] pci 0000:17:0a.0: Adding to iommu group 23
[   17.274359] pci 0000:17:0a.1: Adding to iommu group 23
[   17.274403] pci 0000:17:0a.2: Adding to iommu group 23
[   17.274446] pci 0000:17:0a.3: Adding to iommu group 23
[   17.274496] pci 0000:17:0a.4: Adding to iommu group 23
[   17.274540] pci 0000:17:0a.5: Adding to iommu group 23
[   17.274583] pci 0000:17:0a.6: Adding to iommu group 23
[   17.274626] pci 0000:17:0a.7: Adding to iommu group 23
[   17.274796] pci 0000:17:0b.0: Adding to iommu group 24
[   17.274842] pci 0000:17:0b.1: Adding to iommu group 24
[   17.274885] pci 0000:17:0b.2: Adding to iommu group 24
[   17.274928] pci 0000:17:0b.3: Adding to iommu group 24
[   17.275230] pci 0000:17:0e.0: Adding to iommu group 25
[   17.275274] pci 0000:17:0e.1: Adding to iommu group 25
[   17.275318] pci 0000:17:0e.2: Adding to iommu group 25
[   17.275361] pci 0000:17:0e.3: Adding to iommu group 25
[   17.275405] pci 0000:17:0e.4: Adding to iommu group 25
[   17.275455] pci 0000:17:0e.5: Adding to iommu group 25
[   17.275502] pci 0000:17:0e.6: Adding to iommu group 25
[   17.275546] pci 0000:17:0e.7: Adding to iommu group 25
[   17.275848] pci 0000:17:0f.0: Adding to iommu group 26
[   17.275893] pci 0000:17:0f.1: Adding to iommu group 26
[   17.275938] pci 0000:17:0f.2: Adding to iommu group 26
[   17.275982] pci 0000:17:0f.3: Adding to iommu group 26
[   17.276027] pci 0000:17:0f.4: Adding to iommu group 26
[   17.276072] pci 0000:17:0f.5: Adding to iommu group 26
[   17.276116] pci 0000:17:0f.6: Adding to iommu group 26
[   17.276161] pci 0000:17:0f.7: Adding to iommu group 26
[   17.276462] pci 0000:17:10.0: Adding to iommu group 27
[   17.276509] pci 0000:17:10.1: Adding to iommu group 27
[   17.276561] pci 0000:17:10.2: Adding to iommu group 27
[   17.276607] pci 0000:17:10.3: Adding to iommu group 27
[   17.276652] pci 0000:17:10.4: Adding to iommu group 27
[   17.276697] pci 0000:17:10.5: Adding to iommu group 27
[   17.276743] pci 0000:17:10.6: Adding to iommu group 27
[   17.276788] pci 0000:17:10.7: Adding to iommu group 27
[   17.276957] pci 0000:17:11.0: Adding to iommu group 28
[   17.277004] pci 0000:17:11.1: Adding to iommu group 28
[   17.277050] pci 0000:17:11.2: Adding to iommu group 28
[   17.277095] pci 0000:17:11.3: Adding to iommu group 28
[   17.277260] pci 0000:17:1d.0: Adding to iommu group 29
[   17.277307] pci 0000:17:1d.1: Adding to iommu group 29
[   17.277353] pci 0000:17:1d.2: Adding to iommu group 29
[   17.277406] pci 0000:17:1d.3: Adding to iommu group 29
[   17.277670] pci 0000:17:1e.0: Adding to iommu group 30
[   17.277717] pci 0000:17:1e.1: Adding to iommu group 30
[   17.277763] pci 0000:17:1e.2: Adding to iommu group 30
[   17.277809] pci 0000:17:1e.3: Adding to iommu group 30
[   17.277856] pci 0000:17:1e.4: Adding to iommu group 30
[   17.277902] pci 0000:17:1e.5: Adding to iommu group 30
[   17.277952] pci 0000:17:1e.6: Adding to iommu group 30
[   17.277995] pci 0000:18:00.0: Adding to iommu group 31
[   17.278116] pci 0000:19:00.0: Adding to iommu group 32

---

### 评论 #5 — dshm (2021-03-02T07:41:56Z)

[   17.278179] pci 0000:19:00.1: Adding to iommu group 32
[   17.278229] pci 0000:3a:00.0: Adding to iommu group 33
[   17.278272] pci 0000:3a:05.0: Adding to iommu group 34
[   17.278318] pci 0000:3a:05.2: Adding to iommu group 35
[   17.278357] pci 0000:3a:05.4: Adding to iommu group 36
[   17.278396] pci 0000:3a:08.0: Adding to iommu group 37
[   17.278435] pci 0000:3a:09.0: Adding to iommu group 38
[   17.278473] pci 0000:3a:0a.0: Adding to iommu group 39
[   17.278511] pci 0000:3a:0a.1: Adding to iommu group 40
[   17.278558] pci 0000:3a:0a.2: Adding to iommu group 41
[   17.278597] pci 0000:3a:0a.3: Adding to iommu group 42
[   17.278635] pci 0000:3a:0a.4: Adding to iommu group 43
[   17.278673] pci 0000:3a:0a.5: Adding to iommu group 44
[   17.278711] pci 0000:3a:0a.6: Adding to iommu group 45
[   17.278750] pci 0000:3a:0a.7: Adding to iommu group 46
[   17.278789] pci 0000:3a:0b.0: Adding to iommu group 47
[   17.278839] pci 0000:3a:0b.1: Adding to iommu group 48
[   17.278878] pci 0000:3a:0b.2: Adding to iommu group 49
[   17.278917] pci 0000:3a:0b.3: Adding to iommu group 50
[   17.278956] pci 0000:3a:0c.0: Adding to iommu group 51
[   17.278995] pci 0000:3a:0c.1: Adding to iommu group 52
[   17.279034] pci 0000:3a:0c.2: Adding to iommu group 53
[   17.279073] pci 0000:3a:0c.3: Adding to iommu group 54
[   17.279112] pci 0000:3a:0c.4: Adding to iommu group 55
[   17.279158] pci 0000:3a:0c.5: Adding to iommu group 56
[   17.279198] pci 0000:3a:0c.6: Adding to iommu group 57
[   17.279236] pci 0000:3a:0c.7: Adding to iommu group 58
[   17.279276] pci 0000:3a:0d.0: Adding to iommu group 59
[   17.279314] pci 0000:3a:0d.1: Adding to iommu group 60
[   17.279357] pci 0000:3a:0d.2: Adding to iommu group 61
[   17.279396] pci 0000:3a:0d.3: Adding to iommu group 62
[   17.279449] pci 0000:3b:00.0: Adding to iommu group 63
[   17.279495] pci 0000:3c:00.0: Adding to iommu group 64
[   17.279552] pci 0000:3d:00.0: Adding to iommu group 65
[   17.279600] pci 0000:3d:00.1: Adding to iommu group 66
[   17.279650] pci 0000:5d:05.0: Adding to iommu group 67
[   17.279689] pci 0000:5d:05.2: Adding to iommu group 68
[   17.279727] pci 0000:5d:05.4: Adding to iommu group 69
[   17.279766] pci 0000:5d:0e.0: Adding to iommu group 70
[   17.279813] pci 0000:5d:0e.1: Adding to iommu group 71
[   17.279853] pci 0000:5d:0f.0: Adding to iommu group 72
[   17.279891] pci 0000:5d:0f.1: Adding to iommu group 73
[   17.279930] pci 0000:5d:10.0: Adding to iommu group 74
[   17.279969] pci 0000:5d:10.1: Adding to iommu group 75
[   17.280012] pci 0000:5d:12.0: Adding to iommu group 76
[   17.280146] pci 0000:5d:12.1: Adding to iommu group 77
[   17.280201] pci 0000:5d:12.2: Adding to iommu group 77
[   17.280246] pci 0000:5d:12.4: Adding to iommu group 78
[   17.280300] pci 0000:5d:12.5: Adding to iommu group 77
[   17.280399] pci 0000:5d:15.0: Adding to iommu group 79
[   17.280453] pci 0000:5d:15.1: Adding to iommu group 79
[   17.280616] pci 0000:5d:16.0: Adding to iommu group 80
[   17.280670] pci 0000:5d:16.1: Adding to iommu group 80
[   17.280724] pci 0000:5d:16.4: Adding to iommu group 80
[   17.280778] pci 0000:5d:16.5: Adding to iommu group 80
[   17.280878] pci 0000:5d:17.0: Adding to iommu group 81
[   17.280934] pci 0000:5d:17.1: Adding to iommu group 81
[   17.280983] pci 0000:80:05.0: Adding to iommu group 82
[   17.281023] pci 0000:80:05.2: Adding to iommu group 83
[   17.281063] pci 0000:80:05.4: Adding to iommu group 84
[   17.281103] pci 0000:80:08.0: Adding to iommu group 85
[   17.281179] pci 0000:80:08.1: Adding to iommu group 86
[   17.281219] pci 0000:80:08.2: Adding to iommu group 87
[   17.281262] pci 0000:85:05.0: Adding to iommu group 88
[   17.281301] pci 0000:85:05.2: Adding to iommu group 89
[   17.281348] pci 0000:85:05.4: Adding to iommu group 90
[   17.281650] pci 0000:85:08.0: Adding to iommu group 91
[   17.281707] pci 0000:85:08.1: Adding to iommu group 91
[   17.281762] pci 0000:85:08.2: Adding to iommu group 91
[   17.281816] pci 0000:85:08.3: Adding to iommu group 91
[   17.281870] pci 0000:85:08.4: Adding to iommu group 91
[   17.281924] pci 0000:85:08.5: Adding to iommu group 91
[   17.281978] pci 0000:85:08.6: Adding to iommu group 91
[   17.282031] pci 0000:85:08.7: Adding to iommu group 91
[   17.282325] pci 0000:85:09.0: Adding to iommu group 92
[   17.282382] pci 0000:85:09.1: Adding to iommu group 92
[   17.282438] pci 0000:85:09.2: Adding to iommu group 92
[   17.282501] pci 0000:85:09.3: Adding to iommu group 92
[   17.282556] pci 0000:85:09.4: Adding to iommu group 92
[   17.282611] pci 0000:85:09.5: Adding to iommu group 92
[   17.282666] pci 0000:85:09.6: Adding to iommu group 92
[   17.282721] pci 0000:85:09.7: Adding to iommu group 92
[   17.283015] pci 0000:85:0a.0: Adding to iommu group 93
[   17.283075] pci 0000:85:0a.1: Adding to iommu group 93
[   17.283131] pci 0000:85:0a.2: Adding to iommu group 93
[   17.283187] pci 0000:85:0a.3: Adding to iommu group 93
[   17.283243] pci 0000:85:0a.4: Adding to iommu group 93
[   17.283299] pci 0000:85:0a.5: Adding to iommu group 93
[   17.283354] pci 0000:85:0a.6: Adding to iommu group 93
[   17.283409] pci 0000:85:0a.7: Adding to iommu group 93
[   17.283584] pci 0000:85:0b.0: Adding to iommu group 94
[   17.283644] pci 0000:85:0b.1: Adding to iommu group 94
[   17.283702] pci 0000:85:0b.2: Adding to iommu group 94
[   17.283763] pci 0000:85:0b.3: Adding to iommu group 94
[   17.284057] pci 0000:85:0e.0: Adding to iommu group 95
[   17.284117] pci 0000:85:0e.1: Adding to iommu group 95
[   17.284175] pci 0000:85:0e.2: Adding to iommu group 95
[   17.284233] pci 0000:85:0e.3: Adding to iommu group 95
[   17.284290] pci 0000:85:0e.4: Adding to iommu group 95
[   17.284347] pci 0000:85:0e.5: Adding to iommu group 95
[   17.284404] pci 0000:85:0e.6: Adding to iommu group 95
[   17.284461] pci 0000:85:0e.7: Adding to iommu group 95
[   17.284755] pci 0000:85:0f.0: Adding to iommu group 96
[   17.284825] pci 0000:85:0f.1: Adding to iommu group 96
[   17.284885] pci 0000:85:0f.2: Adding to iommu group 96
[   17.284945] pci 0000:85:0f.3: Adding to iommu group 96
[   17.285004] pci 0000:85:0f.4: Adding to iommu group 96
[   17.285063] pci 0000:85:0f.5: Adding to iommu group 96
[   17.285123] pci 0000:85:0f.6: Adding to iommu group 96
[   17.285182] pci 0000:85:0f.7: Adding to iommu group 96
[   17.285479] pci 0000:85:10.0: Adding to iommu group 97
[   17.285541] pci 0000:85:10.1: Adding to iommu group 97
[   17.285602] pci 0000:85:10.2: Adding to iommu group 97
[   17.285663] pci 0000:85:10.3: Adding to iommu group 97
[   17.285723] pci 0000:85:10.4: Adding to iommu group 97
[   17.285783] pci 0000:85:10.5: Adding to iommu group 97
[   17.285844] pci 0000:85:10.6: Adding to iommu group 97
[   17.285912] pci 0000:85:10.7: Adding to iommu group 97
[   17.286079] pci 0000:85:11.0: Adding to iommu group 98
[   17.286147] pci 0000:85:11.1: Adding to iommu group 98
[   17.286210] pci 0000:85:11.2: Adding to iommu group 98
[   17.286271] pci 0000:85:11.3: Adding to iommu group 98
[   17.286445] pci 0000:85:1d.0: Adding to iommu group 99
[   17.286510] pci 0000:85:1d.1: Adding to iommu group 99
[   17.286574] pci 0000:85:1d.2: Adding to iommu group 99
[   17.286641] pci 0000:85:1d.3: Adding to iommu group 99
[   17.286939] pci 0000:85:1e.0: Adding to iommu group 100
[   17.287004] pci 0000:85:1e.1: Adding to iommu group 100
[   17.287068] pci 0000:85:1e.2: Adding to iommu group 100
[   17.287139] pci 0000:85:1e.3: Adding to iommu group 100
[   17.287203] pci 0000:85:1e.4: Adding to iommu group 100
[   17.287266] pci 0000:85:1e.5: Adding to iommu group 100
[   17.287329] pci 0000:85:1e.6: Adding to iommu group 100
[   17.287374] pci 0000:ae:00.0: Adding to iommu group 101
[   17.287419] pci 0000:ae:05.0: Adding to iommu group 102
[   17.287460] pci 0000:ae:05.2: Adding to iommu group 103
[   17.287500] pci 0000:ae:05.4: Adding to iommu group 104
[   17.287541] pci 0000:ae:08.0: Adding to iommu group 105
[   17.287590] pci 0000:ae:09.0: Adding to iommu group 106
[   17.287631] pci 0000:ae:0a.0: Adding to iommu group 107
[   17.287676] pci 0000:ae:0a.1: Adding to iommu group 108
[   17.287717] pci 0000:ae:0a.2: Adding to iommu group 109
[   17.287757] pci 0000:ae:0a.3: Adding to iommu group 110
[   17.287798] pci 0000:ae:0a.4: Adding to iommu group 111
[   17.287838] pci 0000:ae:0a.5: Adding to iommu group 112
[   17.287879] pci 0000:ae:0a.6: Adding to iommu group 113
[   17.287926] pci 0000:ae:0a.7: Adding to iommu group 114
[   17.287967] pci 0000:ae:0b.0: Adding to iommu group 115
[   17.288008] pci 0000:ae:0b.1: Adding to iommu group 116
[   17.288048] pci 0000:ae:0b.2: Adding to iommu group 117
[   17.288088] pci 0000:ae:0b.3: Adding to iommu group 118
[   17.288129] pci 0000:ae:0c.0: Adding to iommu group 119
[   17.288170] pci 0000:ae:0c.1: Adding to iommu group 120
[   17.288218] pci 0000:ae:0c.2: Adding to iommu group 121
[   17.288259] pci 0000:ae:0c.3: Adding to iommu group 122
[   17.288300] pci 0000:ae:0c.4: Adding to iommu group 123
[   17.288341] pci 0000:ae:0c.5: Adding to iommu group 124
[   17.288385] pci 0000:ae:0c.6: Adding to iommu group 125
[   17.288425] pci 0000:ae:0c.7: Adding to iommu group 126
[   17.288466] pci 0000:ae:0d.0: Adding to iommu group 127
[   17.288506] pci 0000:ae:0d.1: Adding to iommu group 128
[   17.288554] pci 0000:ae:0d.2: Adding to iommu group 129
[   17.288595] pci 0000:ae:0d.3: Adding to iommu group 130
[   17.288655] pci 0000:af:00.0: Adding to iommu group 131
[   17.288705] pci 0000:af:00.1: Adding to iommu group 132
[   17.288748] pci 0000:d7:05.0: Adding to iommu group 133
[   17.288788] pci 0000:d7:05.2: Adding to iommu group 134
[   17.288829] pci 0000:d7:05.4: Adding to iommu group 135
[   17.288877] pci 0000:d7:0e.0: Adding to iommu group 136
[   17.288917] pci 0000:d7:0e.1: Adding to iommu group 137
[   17.288957] pci 0000:d7:0f.0: Adding to iommu group 138
[   17.288996] pci 0000:d7:0f.1: Adding to iommu group 139
[   17.289041] pci 0000:d7:10.0: Adding to iommu group 140
[   17.289081] pci 0000:d7:10.1: Adding to iommu group 141
[   17.289122] pci 0000:d7:12.0: Adding to iommu group 142
[   17.289260] pci 0000:d7:12.1: Adding to iommu group 143
[   17.289337] pci 0000:d7:12.2: Adding to iommu group 143
[   17.289377] pci 0000:d7:12.4: Adding to iommu group 144
[   17.289447] pci 0000:d7:12.5: Adding to iommu group 143
[   17.289552] pci 0000:d7:15.0: Adding to iommu group 145
[   17.289623] pci 0000:d7:15.1: Adding to iommu group 145
[   17.289794] pci 0000:d7:16.0: Adding to iommu group 146
[   17.289864] pci 0000:d7:16.1: Adding to iommu group 146
[   17.289935] pci 0000:d7:16.4: Adding to iommu group 146
[   17.290005] pci 0000:d7:16.5: Adding to iommu group 146
[   17.290110] pci 0000:d7:17.0: Adding to iommu group 147
[   17.290181] pci 0000:d7:17.1: Adding to iommu group 147
[   17.290193] DMAR: Intel(R) Virtualization Technology for Directed I/O
[   17.297575] check: Scanning for low memory corruption every 60 seconds
[   17.300168] Initialise system trusted keyrings
[   17.300179] Key type blacklist registered
[   17.300307] workingset: timestamp_bits=36 max_order=28 bucket_order=0
[   17.301903] zbud: loaded
[   17.302600] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[   17.302956] fuse: init (API version 7.31)
[   17.302982] *** VALIDATE fuse ***
[   17.302984] *** VALIDATE fuse ***
[   17.303248] Platform Keyring initialized
[   17.305996] Key type asymmetric registered
[   17.305998] Asymmetric key parser 'x509' registered
[   17.306004] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 244)
[   17.306180] io scheduler mq-deadline registered
[   17.307893] pcieport 0000:00:1c.0: PME: Signaling with IRQ 24
[   17.308324] pcieport 0000:00:1c.4: PME: Signaling with IRQ 25
[   17.308964] pcieport 0000:17:00.0: PME: Signaling with IRQ 27
[   17.309578] pcieport 0000:17:02.0: PME: Signaling with IRQ 28
[   17.310134] pcieport 0000:3a:00.0: PME: Signaling with IRQ 30
[   17.311379] pcieport 0000:ae:00.0: PME: Signaling with IRQ 34
[   17.311604] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[   17.311849] efifb: probing for efifb
[   17.311893] efifb: No BGRT, not showing boot graphics
[   17.311895] efifb: framebuffer at 0x91000000, using 3072k, total 3072k
[   17.311898] efifb: mode is 1024x768x32, linelength=4096, pages=1
[   17.311898] efifb: scrolling: redraw
[   17.311901] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[   17.311995] fbcon: Deferring console take-over
[   17.311997] fb0: EFI VGA frame buffer device
[   17.312012] intel_idle: MWAIT substates: 0x2020
[   17.312013] intel_idle: v0.4.1 model 0x55
[   17.317770] intel_idle: lapic_timer_reliable_states 0xffffffff
[   17.318237] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
[   17.318295] ACPI: Power Button [PWRF]
[   17.321273] ERST: Error Record Serialization Table (ERST) support is initialized.
[   17.321275] pstore: Registered erst as persistent store backend
[   17.323146] GHES: APEI firmware first mode is enabled by APEI bit and WHEA _OSC.
[   17.323294] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[   17.344037] 00:02: ttyS1 at I/O 0x2f8 (irq = 3, base_baud = 115200) is a 16550A
[   17.364832] 00:03: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[   17.366318] Linux agpgart interface v0.103
[   17.397438] loop: module loaded
[   17.397779] libphy: Fixed MDIO Bus: probed
[   17.397780] tun: Universal TUN/TAP device driver, 1.6
[   17.397851] PPP generic driver version 2.4.2
[   17.397909] VFIO - User Level meta-driver version: 0.3
[   17.398142] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[   17.398144] ehci-pci: EHCI PCI platform driver
[   17.398177] ehci-platform: EHCI generic platform driver
[   17.398184] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[   17.398186] ohci-pci: OHCI PCI platform driver
[   17.398218] ohci-platform: OHCI generic platform driver
[   17.398223] uhci_hcd: USB Universal Host Controller Interface driver
[   17.398799] xhci_hcd 0000:00:14.0: xHCI Host Controller
[   17.398834] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
[   17.400071] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000000009810
[   17.400079] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
[   17.400443] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[   17.400447] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   17.400449] usb usb1: Product: xHCI Host Controller
[   17.400452] usb usb1: Manufacturer: Linux 5.4.53-050453-generic xhci-hcd
[   17.400454] usb usb1: SerialNumber: 0000:00:14.0
[   17.400702] hub 1-0:1.0: USB hub found
[   17.400726] hub 1-0:1.0: 16 ports detected
[   17.405159] xhci_hcd 0000:00:14.0: xHCI Host Controller
[   17.405168] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 2
[   17.405172] xhci_hcd 0000:00:14.0: Host supports USB 3.0 SuperSpeed
[   17.405218] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[   17.405220] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[   17.405222] usb usb2: Product: xHCI Host Controller
[   17.405223] usb usb2: Manufacturer: Linux 5.4.53-050453-generic xhci-hcd
[   17.405225] usb usb2: SerialNumber: 0000:00:14.0
[   17.405438] hub 2-0:1.0: USB hub found
[   17.405458] hub 2-0:1.0: 10 ports detected
[   17.406710] usb: port power management may be unreliable
[   17.407689] i8042: PNP: No PS/2 controller found.
[   17.407813] mousedev: PS/2 mouse device common for all mice
[   17.407896] rtc_cmos 00:00: RTC can wake from S4
[   17.408202] rtc_cmos 00:00: registered as rtc0
[   17.408214] rtc_cmos 00:00: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[   17.408219] i2c /dev entries driver
[   17.408265] device-mapper: uevent: version 1.0.3
[   17.408320] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
[   17.408333] platform eisa.0: Probing EISA bus 0
[   17.408334] platform eisa.0: EISA: Cannot allocate resource for mainboard
[   17.408336] platform eisa.0: Cannot allocate resource for EISA slot 1
[   17.408336] platform eisa.0: Cannot allocate resource for EISA slot 2
[   17.408337] platform eisa.0: Cannot allocate resource for EISA slot 3
[   17.408338] platform eisa.0: Cannot allocate resource for EISA slot 4
[   17.408339] platform eisa.0: Cannot allocate resource for EISA slot 5
[   17.408340] platform eisa.0: Cannot allocate resource for EISA slot 6
[   17.408341] platform eisa.0: Cannot allocate resource for EISA slot 7
[   17.408341] platform eisa.0: Cannot allocate resource for EISA slot 8
[   17.408342] platform eisa.0: EISA: Detected 0 cards
[   17.408348] intel_pstate: P-states controlled by the platform
[   17.413285] ledtrig-cpu: registered to indicate activity on CPUs
[   17.413296] EFI Variables Facility v0.08 2004-May-17
[   17.509558] drop_monitor: Initializing network drop monitor service
[   17.509760] NET: Registered protocol family 10
[   17.514312] Segment Routing with IPv6
[   17.514323] NET: Registered protocol family 17
[   17.514403] Key type dns_resolver registered
[   17.526568] RAS: Correctable Errors collector initialized.
[   17.526663] microcode: sig=0x50657, pf=0x80, revision=0x5003003
[   17.531004] microcode: Microcode Update Driver: v2.2.
[   17.536283] *** VALIDATE rdt ***
[   17.536292] resctrl: MB allocation detected
[   17.536293] resctrl: L3 monitoring detected
[   17.536298] IPI shorthand broadcast: enabled
[   17.536310] sched_clock: Marking stable (17537044075, -787637)->(17634615388, -98358950)
[   17.536551] registered taskstats version 1
[   17.536595] Loading compiled-in X.509 certificates
[   17.538082] Loaded X.509 cert 'Build time autogenerated kernel key: 6776b524d6f1e83a583e25deb09d656a28cd135f'
[   17.539755] zswap: loaded using pool lzo/zbud
[   17.540278] Key type ._fscrypt registered
[   17.540280] Key type .fscrypt registered
[   17.540683] pstore: Using crash dump compression: deflate
[   17.548858] Key type big_key registered
[   17.552739] Key type encrypted registered
[   17.552744] AppArmor: AppArmor sha1 policy hashing enabled
[   17.557827] integrity: Loading X.509 certificate: UEFI:db
[   17.557899] integrity: Loaded X.509 cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4'
[   17.557900] integrity: Loading X.509 certificate: UEFI:db
[   17.557941] integrity: Loaded X.509 cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53'
[   17.557942] integrity: Loading X.509 certificate: UEFI:db
[   17.558206] integrity: Loaded X.509 cert 'VMware, Inc.: 4ad8ba0472073d28127706ddc6ccb9050441bbc7'
[   17.558207] integrity: Loading X.509 certificate: UEFI:db
[   17.558677] integrity: Loaded X.509 cert 'VMware, Inc.: VMware Secure Boot Signing: 04597f3e1ffb240bba0ff0f05d5eb05f3e15f6d7'
[   17.562133] integrity: Loading X.509 certificate: UEFI:MokListRT
[   17.562167] integrity: Loaded X.509 cert 'SomeOrg: shim: a01ee84e9b37ace407961cc468c5909447878469'
[   17.562169] integrity: Loading X.509 certificate: UEFI:MokListRT
[   17.562645] integrity: Loaded X.509 cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63'
[   17.566346] ima: No TPM chip found, activating TPM-bypass!
[   17.566350] ima: Allocated hash algorithm: sha1
[   17.566356] ima: No architecture policies found
[   17.566365] evm: Initialising EVM extended attributes:
[   17.566365] evm: security.selinux
[   17.566366] evm: security.SMACK64
[   17.566367] evm: security.SMACK64EXEC
[   17.566367] evm: security.SMACK64TRANSMUTE
[   17.566368] evm: security.SMACK64MMAP
[   17.566368] evm: security.apparmor
[   17.566368] evm: security.ima
[   17.566369] evm: security.capability
[   17.566370] evm: HMAC attrs: 0x1
[   17.569038] PM:   Magic number: 9:986:818
[   17.569244] acpi device:a7: hash matches
[   17.569624] rtc_cmos 00:00: setting system clock to 2021-02-24T04:50:30 UTC (1614142230)
[   17.586082] Freeing unused decrypted memory: 2040K
[   17.587397] Freeing unused kernel image memory: 2704K
[   17.606926] Write protecting the kernel read-only data: 22528k
[   17.608555] Freeing unused kernel image memory: 2008K
[   17.609389] Freeing unused kernel image memory: 1212K
[   17.627359] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[   17.627362] Run /init as init process
[   17.738900] usb 1-14: new high-speed USB device number 2 using xhci_hcd
[   17.845941] wmi_bus wmi_bus-PNP0C14:00: WQBC data block query control method not found
[   17.875382] ahci 0000:00:11.5: version 3.0
[   17.875992] ahci 0000:00:11.5: AHCI 0001.0301 32 slots 6 ports 6 Gbps 0x3f impl SATA mode
[   17.875995] ahci 0000:00:11.5: flags: 64bit ncq sntf pm led clo only pio slum part ems deso sadm sds apst 
[   17.877956] i40e: Intel(R) Ethernet Connection XL710 Network Driver - version 2.8.20-k
[   17.877957] i40e: Copyright (c) 2013 - 2019 Intel Corporation.
[   17.877994] Broadcom NetXtreme-C/E driver bnxt_en v1.10.0
[   17.878100] megasas: 07.710.50.00-rc1
[   17.878607] tg3.c:v3.137 (May 11, 2014)
[   17.880329] megaraid_sas 0000:18:00.0: BAR:0x1  BAR's base_addr(phys):0x000000009dc00000  mapped virt_addr:0x00000000d87521bd
[   17.880331] megaraid_sas 0000:18:00.0: FW now in Ready state
[   17.880333] megaraid_sas 0000:18:00.0: 63 bit DMA mask and 32 bit consistent mask
[   17.882209] megaraid_sas 0000:18:00.0: Using iommu dma mapping
[   17.882210] megaraid_sas 0000:18:00.0: DMAR: 32bit DMA uses non-identity mapping
[   17.883095] megaraid_sas 0000:18:00.0: firmware supports msix	: (96)
[   17.890928] usb 1-14: New USB device found, idVendor=1604, idProduct=10c0, bcdDevice= 0.00
[   17.890930] usb 1-14: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[   17.891788] hub 1-14:1.0: USB hub found
[   17.891809] hub 1-14:1.0: 4 ports detected
[   17.892903] i40e 0000:af:00.0: fw 6.0.48442 api 1.7 nvm 6.01 0x80003554 1.1747.0 [8086:158b] [8086:0001]
[   17.895279] bnxt_en 0000:19:00.0 eth0: Broadcom BCM57412 NetXtreme-E 10Gb Ethernet found at mem 9da10000, node addr bc:97:e1:53:b3:5c
[   17.895285] bnxt_en 0000:19:00.0: 63.008 Gb/s available PCIe bandwidth (8 GT/s x8 link)
[   17.895804] megaraid_sas 0000:18:00.0: requested/available msix 81/81
[   17.895811] megaraid_sas 0000:18:00.0: current msix/online cpus	: (81/80)
[   17.895811] megaraid_sas 0000:18:00.0: RDPQ mode	: (disabled)
[   17.895813] megaraid_sas 0000:18:00.0: Current firmware supports maximum commands: 928	 LDIO threshold: 0
[   17.898780] megaraid_sas 0000:18:00.0: Configured max firmware commands: 927
[   17.912835] tg3 0000:01:00.0 eth1: Tigon3 [partno(BCM95720) rev 5720000] (PCI Express) MAC address bc:97:e1:53:b3:5a
[   17.912837] tg3 0000:01:00.0 eth1: attached PHY is 5720C (10/100/1000Base-T Ethernet) (WireSpeed[1], EEE[1])
[   17.912838] tg3 0000:01:00.0 eth1: RXcsums[1] LinkChgREG[0] MIirq[0] ASF[1] TSOcap[1]
[   17.912839] tg3 0000:01:00.0 eth1: dma_rwctrl[00000001] dma_mask[64-bit]
[   17.914063] megaraid_sas 0000:18:00.0: Performance mode :Latency
[   17.914063] megaraid_sas 0000:18:00.0: FW supports sync cache	: No
[   17.914065] megaraid_sas 0000:18:00.0: megasas_disable_intr_fusion is called outbound_intr_mask:0x40000009
[   17.927732] bnxt_en 0000:19:00.1 eth2: Broadcom BCM57412 NetXtreme-E 10Gb Ethernet found at mem 9da00000, node addr bc:97:e1:53:b3:5d
[   17.927739] bnxt_en 0000:19:00.1: 63.008 Gb/s available PCIe bandwidth (8 GT/s x8 link)
[   17.929566] bnxt_en 0000:19:00.0 eno1np0: renamed from eth0
[   17.952341] scsi host1: ahci
[   17.952753] scsi host2: ahci
[   17.953062] scsi host3: ahci
[   17.953348] scsi host4: ahci
[   17.953675] scsi host5: ahci
[   17.953970] scsi host6: ahci
[   17.954097] ata1: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80100 irq 36
[   17.954100] ata2: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80180 irq 36
[   17.954103] ata3: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80200 irq 36
[   17.954105] ata4: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80280 irq 36
[   17.954107] ata5: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80300 irq 36
[   17.954110] ata6: SATA max UDMA/133 abar m524288@0x92a80000 port 0x92a80380 irq 36
[   17.954783] ahci 0000:00:17.0: AHCI 0001.0301 32 slots 8 ports 6 Gbps 0xff impl SATA mode
[   17.954788] ahci 0000:00:17.0: flags: 64bit ncq sntf pm led clo only pio slum part ems deso sadm sds apst 
[   17.971028] megaraid_sas 0000:18:00.0: FW provided supportMaxExtLDs: 1	max_lds: 64
[   17.971031] megaraid_sas 0000:18:00.0: controller type	: MR(2048MB)
[   17.971033] megaraid_sas 0000:18:00.0: Online Controller Reset(OCR)	: Enabled
[   17.971035] megaraid_sas 0000:18:00.0: Secure JBOD support	: No
[   17.971037] megaraid_sas 0000:18:00.0: NVMe passthru support	: No
[   17.971039] megaraid_sas 0000:18:00.0: FW provided TM TaskAbort/Reset timeout	: 0 secs/0 secs
[   17.971041] megaraid_sas 0000:18:00.0: JBOD sequence map support	: No
[   17.971042] megaraid_sas 0000:18:00.0: PCI Lane Margining support	: No
[   18.004096] megaraid_sas 0000:18:00.0: megasas_enable_intr_fusion is called outbound_intr_mask:0x40000000
[   18.004099] megaraid_sas 0000:18:00.0: INIT adapter done
[   18.004102] megaraid_sas 0000:18:00.0: JBOD sequence map is disabled megasas_setup_jbod_map 5658
[   18.008824] megaraid_sas 0000:18:00.0: pci id		: (0x1000)/(0x005d)/(0x1028)/(0x1f42)
[   18.008827] megaraid_sas 0000:18:00.0: unevenspan support	: yes
[   18.008829] megaraid_sas 0000:18:00.0: firmware crash dump	: no
[   18.008831] megaraid_sas 0000:18:00.0: JBOD sequence map	: disabled
[   18.009035] scsi host0: Avago SAS based MegaRAID driver
[   18.044966] scsi 0:2:0:0: Direct-Access     DELL     PERC H730P Adp   4.30 PQ: 0 ANSI: 5
[   18.059867] scsi host7: ahci
[   18.060112] scsi host8: ahci
[   18.060358] scsi host9: ahci
[   18.062843] scsi host10: ahci
[   18.066870] scsi host11: ahci
[   18.067113] scsi host12: ahci
[   18.067304] scsi host13: ahci
[   18.067617] scsi host14: ahci
[   18.067696] ata7: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00100 irq 146
[   18.067698] ata8: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00180 irq 146
[   18.067699] ata9: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00200 irq 146
[   18.067701] ata10: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00280 irq 146
[   18.067702] ata11: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00300 irq 146
[   18.067703] ata12: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00380 irq 146
[   18.067705] ata13: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00400 irq 146
[   18.067706] ata14: SATA max UDMA/133 abar m524288@0x92a00000 port 0x92a00480 irq 146
[   18.084914] scsi 0:2:0:0: Attached scsi generic sg0 type 0
[   18.085046] sd 0:2:0:0: [sda] 3512991744 512-byte logical blocks: (1.80 TB/1.64 TiB)
[   18.085062] sd 0:2:0:0: [sda] Write Protect is off
[   18.085063] sd 0:2:0:0: [sda] Mode Sense: 1f 00 00 08
[   18.085089] sd 0:2:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[   18.130042] i40e 0000:af:00.0: MAC address: 3c:fd:fe:bb:1d:98
[   18.130178] i40e 0000:af:00.0: FW LLDP is enabled
[   18.159940] bnxt_en 0000:19:00.1 eno2np1: renamed from eth2
[   18.160713] tg3 0000:01:00.1 eth0: Tigon3 [partno(BCM95720) rev 5720000] (PCI Express) MAC address bc:97:e1:53:b3:5b
[   18.160719] tg3 0000:01:00.1 eth0: attached PHY is 5720C (10/100/1000Base-T Ethernet) (WireSpeed[1], EEE[1])
[   18.160723] tg3 0000:01:00.1 eth0: RXcsums[1] LinkChgREG[0] MIirq[0] ASF[1] TSOcap[1]
[   18.160726] tg3 0000:01:00.1 eth0: dma_rwctrl[00000001] dma_mask[64-bit]
[   18.204475] tg3 0000:01:00.0 eno3: renamed from eth1
[   18.210754] i40e 0000:af:00.0 eth2: NIC Link is Up, 25 Gbps Full Duplex, Requested FEC: CL108 RS-FEC, Negotiated FEC: CL108 RS-FEC, Autoneg: False, Flow Control: RX/TX
[   18.230187] i40e 0000:af:00.0: PCI-Express: Speed 8.0GT/s Width x8
[   18.239431] i40e 0000:af:00.0: Features: PF-id[0] VFs: 64 VSIs: 66 QP: 80 RSS FD_ATR FD_SB NTUPLE DCB VxLAN Geneve PTP VEPA
[   18.246501]  sda: sda1 sda2
[   18.247886] sd 0:2:0:0: [sda] Attached SCSI disk
[   18.252958] i40e 0000:af:00.1: fw 6.0.48442 api 1.7 nvm 6.01 0x80003554 1.1747.0 [8086:158b] [8086:0000]
[   18.259434] tg3 0000:01:00.1 eno4: renamed from eth0
[   18.269450] ata3: SATA link down (SStatus 0 SControl 300)
[   18.273258] ata1: SATA link down (SStatus 0 SControl 300)
[   18.273607] ata6: SATA link down (SStatus 0 SControl 300)
[   18.273666] ata4: SATA link down (SStatus 0 SControl 300)
[   18.273689] ata5: SATA link down (SStatus 0 SControl 300)
[   18.273713] ata2: SATA link down (SStatus 0 SControl 300)
[   18.318898] tsc: Refined TSC clocksource calibration: 2494.140 MHz
[   18.318955] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x23f39a1d859, max_idle_ns: 440795326830 ns
[   18.486422] ata7: SATA link down (SStatus 0 SControl 300)
[   18.486423] clocksource: Switched to clocksource tsc
[   18.486439] ata13: SATA link down (SStatus 0 SControl 300)
[   18.486455] ata12: SATA link down (SStatus 0 SControl 300)
[   18.486471] ata9: SATA link down (SStatus 0 SControl 300)
[   18.486488] ata11: SATA link down (SStatus 0 SControl 300)
[   18.486504] ata14: SATA link down (SStatus 0 SControl 300)
[   18.486521] ata10: SATA link down (SStatus 0 SControl 300)
[   18.486536] ata8: SATA link down (SStatus 0 SControl 300)
[   18.487199] i40e 0000:af:00.1: MAC address: 3c:fd:fe:bb:1d:99
[   18.487334] i40e 0000:af:00.1: FW LLDP is enabled
[   18.542321] i40e 0000:af:00.1 eth0: NIC Link is Up, 25 Gbps Full Duplex, Requested FEC: CL108 RS-FEC, Negotiated FEC: CL108 RS-FEC, Autoneg: False, Flow Control: RX/TX
[   18.561712] i40e 0000:af:00.1: PCI-Express: Speed 8.0GT/s Width x8
[   18.570923] i40e 0000:af:00.1: Features: PF-id[1] VFs: 64 VSIs: 66 QP: 80 RSS FD_ATR FD_SB NTUPLE DCB VxLAN Geneve PTP VEPA
[   18.572726] i40e 0000:af:00.0 enp175s0f0: renamed from eth2
[   18.611685] i40e 0000:af:00.1 enp175s0f1: renamed from eth0
[   18.667309] usb 1-14.1: new high-speed USB device number 3 using xhci_hcd
[   18.771266] raid6: avx512x4 gen() 32986 MB/s
[   18.771403] usb 1-14.1: New USB device found, idVendor=1604, idProduct=10c0, bcdDevice= 0.00
[   18.771406] usb 1-14.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[   18.772027] hub 1-14.1:1.0: USB hub found
[   18.772049] hub 1-14.1:1.0: 4 ports detected
[   18.839269] raid6: avx512x4 xor() 22796 MB/s
[   18.855293] usb 1-14.4: new high-speed USB device number 4 using xhci_hcd
[   18.907269] raid6: avx512x2 gen() 32925 MB/s
[   18.955400] usb 1-14.4: New USB device found, idVendor=1604, idProduct=10c0, bcdDevice= 0.00
[   18.955404] usb 1-14.4: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[   18.956086] hub 1-14.4:1.0: USB hub found
[   18.956107] hub 1-14.4:1.0: 4 ports detected
[   18.975266] raid6: avx512x2 xor() 24273 MB/s
[   19.043268] raid6: avx512x1 gen() 30642 MB/s
[   19.111268] raid6: avx512x1 xor() 19490 MB/s
[   19.179278] raid6: avx2x4   gen() 28949 MB/s
[   19.247270] raid6: avx2x4   xor() 20238 MB/s
[   19.315264] raid6: avx2x2   gen() 28013 MB/s
[   19.383267] raid6: avx2x2   xor() 19779 MB/s
[   19.451270] raid6: avx2x1   gen() 19162 MB/s
[   19.519268] raid6: avx2x1   xor() 17946 MB/s
[   19.587271] raid6: sse2x4   gen() 12097 MB/s
[   19.655272] raid6: sse2x4   xor()  8013 MB/s
[   19.723267] raid6: sse2x2   gen() 11953 MB/s
[   19.791271] raid6: sse2x2   xor()  7551 MB/s
[   19.859269] raid6: sse2x1   gen() 10610 MB/s
[   19.927268] raid6: sse2x1   xor()  6078 MB/s
[   19.927268] raid6: using algorithm avx512x4 gen() 32986 MB/s
[   19.927269] raid6: .... xor() 22796 MB/s, rmw enabled
[   19.927269] raid6: using avx512x2 recovery algorithm
[   19.929551] xor: automatically using best checksumming function   avx       
[   19.932036] async_tx: api initialized (async)
[   19.988758] Btrfs loaded, crc32c=crc32c-intel
[   20.121370] fbcon: Taking over console
[   20.121521] Console: switching to colour frame buffer device 128x48
[   20.743698] EXT4-fs (sda2): mounted filesystem with ordered data mode. Opts: (null)
[   22.374692] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
[   22.403487] systemd[1]: Detected architecture x86-64.
[   22.435460] systemd[1]: Set hostname to <ACT103>.
[   24.116401] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[   24.116915] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[   24.116941] systemd[1]: Reached target User and Group Name Lookups.
[   24.119192] systemd[1]: Created slice System Slice.
[   24.119345] systemd[1]: Listening on RPCbind Server Activation Socket.
[   24.119427] systemd[1]: Listening on /dev/initctl Compatibility Named Pipe.
[   24.119581] systemd[1]: Listening on Journal Socket.
[   24.211856] EXT4-fs (sda2): re-mounted. Opts: errors=remount-ro
[   24.363790] RPC: Registered named UNIX socket transport module.
[   24.363791] RPC: Registered udp transport module.
[   24.363792] RPC: Registered tcp transport module.
[   24.363792] RPC: Registered tcp NFSv4.1 backchannel transport module.
[   24.375266] Adding 2097148k swap on /swapfile.  Priority:-2 extents:6 across:2260988k FS
[   24.405577] systemd-journald[1066]: Received request to flush runtime journal from PID 1
[   24.415562] lp: driver loaded but no devices found
[   24.423628] ppdev: user-space parallel port driver
[   25.956347] ACPI Error: No handler for Region [SYSI] (000000006560f6cd) [IPMI] (20190816/evregion-127)
[   25.956618] ACPI Error: Region IPMI (ID=7) has no handler (20190816/exfldio-261)
[   25.956837] No Local Variables are initialized for Method [_GHL]
[   25.956838] No Arguments are initialized for method [_GHL]
[   25.956839] ACPI Error: Aborting method \_SB.PMI0._GHL due to previous error (AE_NOT_EXIST) (20190816/psparse-529)
[   25.957138] ACPI Error: Aborting method \_SB.PMI0._PMC due to previous error (AE_NOT_EXIST) (20190816/psparse-529)
[   25.957439] ACPI Error: AE_NOT_EXIST, Evaluating _PMC (20190816/power_meter-743)
[   26.126231] IPMI message handler: version 39.2
[   26.139260] ipmi device interface
[   26.166396] ipmi_si: IPMI System Interface driver
[   26.166689] ipmi_si dmi-ipmi-si.0: ipmi_platform: probing via SMBIOS
[   26.166691] ipmi_platform: ipmi_si: SMBIOS: io 0xca8 regsize 1 spacing 4 irq 10
[   26.166692] ipmi_si: Adding SMBIOS-specified kcs state machine
[   26.168529] ipmi_si IPI0001:00: ipmi_platform: probing via ACPI
[   26.168554] ipmi_si IPI0001:00: ipmi_platform: [io  0x0ca8] regsize 1 spacing 4 irq 10
[   26.168555] ipmi_si dmi-ipmi-si.0: Removing SMBIOS-specified kcs state machine in favor of ACPI
[   26.168556] ipmi_si: Adding ACPI-specified kcs state machine
[   26.169622] ipmi_si: Trying ACPI-specified kcs state machine at i/o address 0xca8, slave address 0x20, irq 10
[   26.178285] lpc_ich 0000:00:1f.0: I/O space for ACPI uninitialized
[   26.178286] lpc_ich 0000:00:1f.0: No MFD cells added
[   26.367995] dcdbas dcdbas: Dell Systems Management Base Driver (version 5.6.0-3.3)
[   26.368052] RAPL PMU: API unit is 2^-32 Joules, 2 fixed counters, 655360 ms ovfl timer
[   26.368053] RAPL PMU: hw unit of domain package 2^-14 Joules
[   26.368054] RAPL PMU: hw unit of domain dram 2^-16 Joules
[   26.495974] cryptd: max_cpu_qlen set to 1000
[   26.575354] ipmi_si IPI0001:00: The BMC does not support setting the recv irq bit, compensating, but the BMC needs to be fixed.
[   26.579244] mei 0000:00:16.0-55213584-9a29-4916-badf-0fb7ed682aeb: Could not read FW version
[   26.579246] mei 0000:00:16.0-55213584-9a29-4916-badf-0fb7ed682aeb: FW version command failed -5
[   26.593169] ipmi_si IPI0001:00: Using irq 10
[   26.621095] AVX2 version of gcm_enc/dec engaged.
[   26.621095] AES CTR mode by8 optimization enabled
[   26.627536] amdkcl: loading out-of-tree module taints kernel.
[   26.627568] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   26.638256] ipmi_si IPI0001:00: IPMI message handler: Found new BMC (man_id: 0x0002a2, prod_id: 0x0100, dev_id: 0x20)
[   26.705340] mgag200 0000:03:00.0: remove_conflicting_pci_framebuffers: bar 0: 0x91000000 -> 0x91ffffff
[   26.705344] mgag200 0000:03:00.0: remove_conflicting_pci_framebuffers: bar 1: 0x92808000 -> 0x9280bfff
[   26.705347] mgag200 0000:03:00.0: remove_conflicting_pci_framebuffers: bar 2: 0x92000000 -> 0x927fffff
[   26.705351] checking generic (91000000 300000) vs hw (91000000 1000000)
[   26.705353] fb0: switching to mgag200drmfb from EFI VGA
[   26.705536] Console: switching to colour dummy device 80x25
[   26.705574] mgag200 0000:03:00.0: vgaarb: deactivate vga console
[   26.706848] ipmi_si IPI0001:00: IPMI kcs interface initialized
[   26.711017] [TTM] Zone  kernel: Available graphics memory: 389435756 KiB
[   26.711019] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
[   26.711020] [TTM] Initializing pool allocator
[   26.711027] [TTM] Initializing DMA pool allocator
[   26.753513] fbcon: mgag200drmfb (fb0) is primary device
[   26.780454] AMD-Vi: AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[   26.780456] AMD-Vi: AMD IOMMUv2 functionality not available on this system
[   26.898655] ipmi_ssif: IPMI SSIF Interface driver
[   27.105079] snd_hda_intel 0000:3d:00.1: Handle vga_switcheroo audio client
[   27.123283] Console: switching to colour frame buffer device 128x48
[   27.125391] mgag200 0000:03:00.0: fb0: mgag200drmfb frame buffer device
[   27.156764] [drm] Initialized mgag200 1.0.0 20110418 for 0000:03:00.0 on minor 0
[   27.172886] input: HD-Audio Generic HDMI/DP,pcm=3 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input1
[   27.172927] input: HD-Audio Generic HDMI/DP,pcm=7 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input2
[   27.172962] input: HD-Audio Generic HDMI/DP,pcm=8 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input3
[   27.173003] input: HD-Audio Generic HDMI/DP,pcm=9 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input4
[   27.173038] input: HD-Audio Generic HDMI/DP,pcm=10 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input5
[   27.173074] input: HD-Audio Generic HDMI/DP,pcm=11 as /devices/pci0000:3a/0000:3a:00.0/0000:3b:00.0/0000:3c:00.0/0000:3d:00.1/sound/card0/input6
[   27.494881] [drm] amdgpu kernel modesetting enabled.
[   27.494883] [drm] amdgpu version: 5.6.19
[   27.494884] [drm] OS DRM version: 5.4.0
[   27.495087] amdgpu: CRAT table not found
[   27.495090] amdgpu: Virtual CRAT table created for CPU
[   27.495112] amdgpu: Topology: Add CPU node
[   27.536874] amdgpu 0000:3d:00.0: remove_conflicting_pci_framebuffers: bar 0: 0x382fe0000000 -> 0x382fefffffff
[   27.536878] amdgpu 0000:3d:00.0: remove_conflicting_pci_framebuffers: bar 2: 0x382ff0000000 -> 0x382ff01fffff
[   27.536882] amdgpu 0000:3d:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xab000000 -> 0xab07ffff
[   27.536943] amdgpu 0000:3d:00.0: enabling device (0000 -> 0003)
[   27.537165] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6868 0x1002:0x0A0C 0x00).
[   27.537169] amdgpu 0000:3d:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[   27.537171] amdgpu 0000:3d:00.0: amdgpu: set kernel compute queue number to 8 due to invalid parameter provided by user
[   27.537201] [drm] register mmio base: 0xAB000000
[   27.537202] [drm] register mmio size: 524288
[   27.537223] [drm] add ip block number 0 <soc15_common>
[   27.537224] [drm] add ip block number 1 <gmc_v9_0>
[   27.537226] [drm] add ip block number 2 <vega10_ih>
[   27.537227] [drm] add ip block number 3 <psp>
[   27.537229] [drm] add ip block number 4 <gfx_v9_0>
[   27.537230] [drm] add ip block number 5 <sdma_v4_0>
[   27.537232] [drm] add ip block number 6 <powerplay>
[   27.537233] [drm] add ip block number 7 <dm>
[   27.537235] [drm] add ip block number 8 <uvd_v7_0>
[   27.537236] [drm] add ip block number 9 <vce_v4_0>
[   29.258472] amdgpu 0000:3d:00.0: amdgpu: Fetched VBIOS from ROM BAR
[   29.258474] amdgpu: ATOM BIOS: 113-D0511100-109
[   29.291764] [drm] UVD(0) is enabled in VM mode
[   29.291766] [drm] UVD(0) ENC is enabled in VM mode
[   29.291767] [drm] VCE enabled in VM mode
[   29.291793] [drm] GPU posting now...
[   29.841470] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[   29.841482] amdgpu 0000:3d:00.0: BAR 2: releasing [mem 0x382ff0000000-0x382ff01fffff 64bit pref]
[   29.841483] amdgpu 0000:3d:00.0: BAR 0: releasing [mem 0x382fe0000000-0x382fefffffff 64bit pref]
[   29.841496] pcieport 0000:3c:00.0: BAR 15: releasing [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   29.841497] pcieport 0000:3b:00.0: BAR 15: releasing [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   29.841498] pcieport 0000:3a:00.0: BAR 15: releasing [mem 0x382fe0000000-0x382ff01fffff 64bit pref]
[   29.841504] pcieport 0000:3a:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841505] pcieport 0000:3b:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841506] pcieport 0000:3c:00.0: BAR 15: assigned [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841508] amdgpu 0000:3d:00.0: BAR 0: assigned [mem 0x382000000000-0x3821ffffffff 64bit pref]
[   29.841513] amdgpu 0000:3d:00.0: BAR 2: assigned [mem 0x382200000000-0x3822001fffff 64bit pref]
[   29.841519] pcieport 0000:3a:00.0: PCI bridge to [bus 3b-3d]
[   29.841520] pcieport 0000:3a:00.0:   bridge window [io  0x6000-0x6fff]
[   29.841522] pcieport 0000:3a:00.0:   bridge window [mem 0xab000000-0xab1fffff]
[   29.841524] pcieport 0000:3a:00.0:   bridge window [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841526] pcieport 0000:3b:00.0: PCI bridge to [bus 3c-3d]
[   29.841527] pcieport 0000:3b:00.0:   bridge window [io  0x6000-0x6fff]
[   29.841529] pcieport 0000:3b:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   29.841531] pcieport 0000:3b:00.0:   bridge window [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841534] pcieport 0000:3c:00.0: PCI bridge to [bus 3d]
[   29.841535] pcieport 0000:3c:00.0:   bridge window [io  0x6000-0x6fff]
[   29.841538] pcieport 0000:3c:00.0:   bridge window [mem 0xab000000-0xab0fffff]
[   29.841539] pcieport 0000:3c:00.0:   bridge window [mem 0x382000000000-0x3822ffffffff 64bit pref]
[   29.841552] amdgpu 0000:3d:00.0: amdgpu: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[   29.841553] amdgpu 0000:3d:00.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   29.841553] amdgpu 0000:3d:00.0: amdgpu: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[   29.841558] [drm] Detected VRAM RAM=8176M, BAR=8192M
[   29.841559] [drm] RAM width 2048bits HBM
[   29.841762] [TTM] Zone  kernel: Available graphics memory: 389435756 KiB
[   29.841762] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
[   29.841762] [TTM] Initializing pool allocator
[   29.841766] [TTM] Initializing DMA pool allocator
[   29.841801] [drm] amdgpu: 8176M of VRAM memory ready
[   29.841803] [drm] amdgpu: 760616M of GTT memory ready.
[   29.841805] [drm] GART: num cpu pages 131072, num gpu pages 131072
[   29.841892] [drm] PCIE GART of 512M enabled (table at 0x000000F400000000).
[   30.066390] [drm] CP firmware version too old, please update!
[   30.068629] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega10_smu
[   30.142139] [drm] Found UVD firmware Version: 1.87 Family ID: 17
[   30.142156] [drm] PSP loading UVD firmware
[   30.169613] [drm] Found VCE firmware Version: 53.45 Binary ID: 4
[   30.169781] [drm] PSP loading VCE firmware
[   30.686358] [drm] reserve 0x400000 from 0xf5fec00000 for PSP TMR
[   30.868981] [drm] kiq ring mec 2 pipe 1 q 0
[   30.872187] [drm] Display Core initialized with v3.2.99!
[   30.872588] snd_hda_intel 0000:3d:00.1: bound 0000:3d:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[   30.873436] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   30.873437] [drm] Driver supports precise vblank timestamp query.
[   30.894612] [drm] UVD and UVD ENC initialized successfully.
[   30.995219] [drm] VCE initialized successfully.
[   30.996989] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[   30.998122] amdgpu: Virtual CRAT table created for GPU
[   30.998245] amdgpu: Topology: Add dGPU node [0x6868:0x1002]
[   30.998247] kfd kfd: amdgpu: added device 1002:6868
[   30.998249] amdgpu 0000:3d:00.0: amdgpu: SE 4, SH per SE 1, CU per SH 16, active_cu_number 56
[   30.998277] [drm] Cannot find any crtc or sizes
[   30.998416] amdgpu 0000:3d:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
[   30.998417] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   30.998418] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   30.998420] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   30.998421] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   30.998422] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   30.998423] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   30.998424] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   30.998425] amdgpu 0000:3d:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   30.998427] amdgpu 0000:3d:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   30.998428] amdgpu 0000:3d:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
[   30.998429] amdgpu 0000:3d:00.0: amdgpu: ring sdma1 uses VM inv eng 1 on hub 1
[   30.998430] amdgpu 0000:3d:00.0: amdgpu: ring uvd_0 uses VM inv eng 4 on hub 1
[   30.998432] amdgpu 0000:3d:00.0: amdgpu: ring uvd_enc_0.0 uses VM inv eng 5 on hub 1
[   30.998433] amdgpu 0000:3d:00.0: amdgpu: ring uvd_enc_0.1 uses VM inv eng 6 on hub 1
[   30.998434] amdgpu 0000:3d:00.0: amdgpu: ring vce0 uses VM inv eng 7 on hub 1
[   30.998435] amdgpu 0000:3d:00.0: amdgpu: ring vce1 uses VM inv eng 8 on hub 1
[   30.998436] amdgpu 0000:3d:00.0: amdgpu: ring vce2 uses VM inv eng 9 on hub 1
[   30.998437] [drm] ECC is active.
[   30.998437] [drm] SRAM ECC is not present.
[   30.999480] [drm] Initialized amdgpu 3.40.0 20150101 for 0000:3d:00.0 on minor 1
[   31.231132] audit: type=1400 audit(1614142244.156:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=1680 comm="apparmor_parser"
[   31.239962] audit: type=1400 audit(1614142244.168:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oopslash" pid=1679 comm="apparmor_parser"
[   31.246179] audit: type=1400 audit(1614142244.172:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=1682 comm="apparmor_parser"
[   31.251344] audit: type=1400 audit(1614142244.180:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=1686 comm="apparmor_parser"
[   31.252001] audit: type=1400 audit(1614142244.180:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/bin/man" pid=1678 comm="apparmor_parser"
[   31.252009] audit: type=1400 audit(1614142244.180:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_filter" pid=1678 comm="apparmor_parser"
[   31.252013] audit: type=1400 audit(1614142244.180:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="man_groff" pid=1678 comm="apparmor_parser"
[   31.264630] audit: type=1400 audit(1614142244.192:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=1684 comm="apparmor_parser"
[   31.277690] audit: type=1400 audit(1614142244.204:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=1688 comm="apparmor_parser"
[   31.287482] audit: type=1400 audit(1614142244.216:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=1675 comm="apparmor_parser"
[   35.823900] NET: Registered protocol family 15
[   37.167201] nfit ACPI0012:00: Error found in NVDIMM nmem0 flags: flush_fail not_armed
[   37.626049] nfit ACPI0012:00: Error found in NVDIMM nmem1 flags: flush_fail not_armed
[   38.000032] IPv6: ADDRCONF(NETDEV_CHANGE): enp175s0f0: link becomes ready
[   38.000174] IPv6: ADDRCONF(NETDEV_CHANGE): enp175s0f1: link becomes ready
[   38.286230] nfit ACPI0012:00: Error found in NVDIMM nmem2 flags: flush_fail not_armed
[   38.670320] nfit ACPI0012:00: Error found in NVDIMM nmem3 flags: flush_fail not_armed
[   39.067055] nfit ACPI0012:00: Error found in NVDIMM nmem4 flags: flush_fail not_armed
[   39.489934] nfit ACPI0012:00: Error found in NVDIMM nmem5 flags: flush_fail not_armed
[   41.152255] tg3 0000:01:00.1 eno4: Link is up at 1000 Mbps, full duplex
[   41.152272] tg3 0000:01:00.1 eno4: Flow control is off for TX and off for RX
[   41.152276] tg3 0000:01:00.1 eno4: EEE is disabled
[   41.152309] IPv6: ADDRCONF(NETDEV_CHANGE): eno4: link becomes ready
[   45.266838] EDAC MC0: Giving out device to module skx_edac controller Skylake Socket#0 IMC#0: DEV 0000:3a:0a.0 (INTERRUPT)
[   45.266884] EDAC MC1: Giving out device to module skx_edac controller Skylake Socket#0 IMC#1: DEV 0000:3a:0c.0 (INTERRUPT)
[   45.267045] EDAC MC2: Giving out device to module skx_edac controller Skylake Socket#1 IMC#0: DEV 0000:ae:0a.0 (INTERRUPT)
[   45.267082] EDAC MC3: Giving out device to module skx_edac controller Skylake Socket#1 IMC#1: DEV 0000:ae:0c.0 (INTERRUPT)
[   45.380865] intel_rapl_common: Found RAPL domain package
[   45.380873] intel_rapl_common: Found RAPL domain dram
[   45.380876] intel_rapl_common: DRAM domain energy unit 15300pj
[   45.381066] intel_rapl_common: Found RAPL domain package
[   45.381073] intel_rapl_common: Found RAPL domain dram
[   45.381076] intel_rapl_common: DRAM domain energy unit 15300pj
[   47.141823] mgag200 0000:03:00.0: Video card doesn't support cursors with partial transparency.
[   47.141826] mgag200 0000:03:00.0: Not enabling hardware cursor.
[ 1268.816726] kauditd_printk_skb: 45 callbacks suppressed
[ 1268.816729] audit: type=1400 audit(1614143481.423:57): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=4788 comm="apparmor_parser"
[ 1276.449358] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[ 1276.460927] Bridge firewalling registered
[ 1276.512461] bpfilter: Loaded bpfilter_umh pid 5012
[ 1276.513042] Started bpfilter
[ 1276.713559] Initializing XFRM netlink socket
[ 1304.168164] cgroup: cgroup: disabling cgroup2 socket matching due to net_prio or net_cls activation
[ 1326.733933] amdgpu: Started evicting pasid 0x8002
[ 1326.733945] amdgpu: Finished evicting pasid 0x8002
[ 1326.834448] amdgpu: Started restoring pasid 0x8002
[ 1326.834466] amdgpu: Finished restoring pasid 0x8002
[ 1326.892006] amdgpu: Started evicting pasid 0x8002
[ 1326.892017] amdgpu: Finished evicting pasid 0x8002
[ 1327.376054] amdgpu: Started evicting pasid 0x8002
[ 1327.376069] amdgpu: Finished evicting pasid 0x8002
[ 1330.690639] amdgpu: Started evicting pasid 0x8002
[ 1330.690652] amdgpu: Finished evicting pasid 0x8002
[ 1440.782075] amdgpu: Started evicting pasid 0x8002
[ 1440.782086] amdgpu: Finished evicting pasid 0x8002
[ 1440.884225] amdgpu: Started restoring pasid 0x8002
[ 1440.884241] amdgpu: Finished restoring pasid 0x8002
[ 1440.941288] amdgpu: Started evicting pasid 0x8002
[ 1440.941298] amdgpu: Finished evicting pasid 0x8002
[ 1441.169941] amdgpu: Started evicting pasid 0x8002
[ 1441.169954] amdgpu: Finished evicting pasid 0x8002
[ 1442.830880] amdgpu: Started evicting pasid 0x8002
[ 1442.830893] amdgpu: Finished evicting pasid 0x8002
[ 1444.738486] amdgpu: Started evicting pasid 0x8002
[ 1444.738501] amdgpu: Finished evicting pasid 0x8002
[ 1444.903277] amdgpu: Started evicting pasid 0x8002
[ 1444.903291] amdgpu: Finished evicting pasid 0x8002
[ 1445.065080] amdgpu: Started evicting pasid 0x8002
[ 1445.065094] amdgpu: Finished evicting pasid 0x8002
[ 1445.226852] amdgpu: Started evicting pasid 0x8002
[ 1445.226867] amdgpu: Finished evicting pasid 0x8002
[ 1445.427772] amdgpu: Started evicting pasid 0x8002
[ 1445.427785] amdgpu: Finished evicting pasid 0x8002
[ 1445.590912] amdgpu: Started evicting pasid 0x8002
[ 1445.590926] amdgpu: Finished evicting pasid 0x8002
[ 1445.751948] amdgpu: Started evicting pasid 0x8002
[ 1445.751963] amdgpu: Finished evicting pasid 0x8002
[ 1445.920605] amdgpu: Started evicting pasid 0x8002
[ 1445.920620] amdgpu: Finished evicting pasid 0x8002
[ 1446.086054] amdgpu: Started evicting pasid 0x8002
[ 1446.086068] amdgpu: Finished evicting pasid 0x8002
[ 1446.247270] amdgpu: Started evicting pasid 0x8002
[ 1446.247284] amdgpu: Finished evicting pasid 0x8002
[ 1446.408345] amdgpu: Started evicting pasid 0x8002
[ 1446.408359] amdgpu: Finished evicting pasid 0x8002
[ 1446.572099] amdgpu: Started evicting pasid 0x8002
[ 1446.572114] amdgpu: Finished evicting pasid 0x8002
[ 1446.735199] amdgpu: Started evicting pasid 0x8002
[ 1446.735214] amdgpu: Finished evicting pasid 0x8002
[ 1446.938436] amdgpu: Started evicting pasid 0x8002
[ 1446.938451] amdgpu: Finished evicting pasid 0x8002
[ 1447.106217] amdgpu: Started evicting pasid 0x8002
[ 1447.106240] amdgpu: Finished evicting pasid 0x8002
[ 1447.270384] amdgpu: Started evicting pasid 0x8002
[ 1447.270398] amdgpu: Finished evicting pasid 0x8002
[ 1447.432492] amdgpu: Started evicting pasid 0x8002
[ 1447.432506] amdgpu: Finished evicting pasid 0x8002
[ 1447.595427] amdgpu: Started evicting pasid 0x8002
[ 1447.595440] amdgpu: Finished evicting pasid 0x8002
[ 1447.756918] amdgpu: Started evicting pasid 0x8002
[ 1447.756932] amdgpu: Finished evicting pasid 0x8002
[ 1447.919201] amdgpu: Started evicting pasid 0x8002
[ 1447.919215] amdgpu: Finished evicting pasid 0x8002
[ 1448.079728] amdgpu: Started evicting pasid 0x8002
[ 1448.079742] amdgpu: Finished evicting pasid 0x8002
[ 1448.240177] amdgpu: Started evicting pasid 0x8002
[ 1448.240192] amdgpu: Finished evicting pasid 0x8002
[ 1448.402093] amdgpu: Started evicting pasid 0x8002
[ 1448.402108] amdgpu: Finished evicting pasid 0x8002
[ 1448.563396] amdgpu: Started evicting pasid 0x8002
[ 1448.563410] amdgpu: Finished evicting pasid 0x8002
[ 1448.725844] amdgpu: Started evicting pasid 0x8002
[ 1448.725858] amdgpu: Finished evicting pasid 0x8002
[ 1448.887450] amdgpu: Started evicting pasid 0x8002
[ 1448.887504] amdgpu: Finished evicting pasid 0x8002
[ 1449.057555] amdgpu: Started evicting pasid 0x8002
[ 1449.057569] amdgpu: Finished evicting pasid 0x8002
[ 1449.221591] amdgpu: Started evicting pasid 0x8002
[ 1449.221605] amdgpu: Finished evicting pasid 0x8002
[ 1449.443920] amdgpu: Started evicting pasid 0x8002
[ 1449.443933] amdgpu: Finished evicting pasid 0x8002
[ 1449.636225] amdgpu: Started evicting pasid 0x8002
[ 1449.636241] amdgpu: Finished evicting pasid 0x8002
[ 1449.798212] amdgpu: Started evicting pasid 0x8002
[ 1449.798226] amdgpu: Finished evicting pasid 0x8002
[ 1449.958731] amdgpu: Started evicting pasid 0x8002
[ 1449.958746] amdgpu: Finished evicting pasid 0x8002
[ 1450.121792] amdgpu: Started evicting pasid 0x8002
[ 1450.121806] amdgpu: Finished evicting pasid 0x8002
[ 1450.285390] amdgpu: Started evicting pasid 0x8002
[ 1450.285405] amdgpu: Finished evicting pasid 0x8002
[ 1450.446483] amdgpu: Started evicting pasid 0x8002
[ 1450.446498] amdgpu: Finished evicting pasid 0x8002
[ 1450.608714] amdgpu: Started evicting pasid 0x8002
[ 1450.608729] amdgpu: Finished evicting pasid 0x8002
[ 1450.771164] amdgpu: Started evicting pasid 0x8002
[ 1450.771179] amdgpu: Finished evicting pasid 0x8002
[ 1450.936231] amdgpu: Started evicting pasid 0x8002
[ 1450.936246] amdgpu: Finished evicting pasid 0x8002
[ 1451.103804] amdgpu: Started evicting pasid 0x8002
[ 1451.103819] amdgpu: Finished evicting pasid 0x8002
[ 1451.267625] amdgpu: Started evicting pasid 0x8002
[ 1451.267641] amdgpu: Finished evicting pasid 0x8002
[ 1451.434475] amdgpu: Started evicting pasid 0x8002
[ 1451.434490] amdgpu: Finished evicting pasid 0x8002
[ 1451.597714] amdgpu: Started evicting pasid 0x8002
[ 1451.597729] amdgpu: Finished evicting pasid 0x8002
[ 1451.759123] amdgpu: Started evicting pasid 0x8002
[ 1451.759137] amdgpu: Finished evicting pasid 0x8002
[ 1451.920038] amdgpu: Started evicting pasid 0x8002
[ 1451.920052] amdgpu: Finished evicting pasid 0x8002
[ 1452.086525] amdgpu: Started evicting pasid 0x8002
[ 1452.086539] amdgpu: Finished evicting pasid 0x8002
[ 1452.252813] amdgpu: Started evicting pasid 0x8002
[ 1452.252826] amdgpu: Finished evicting pasid 0x8002
[ 1452.799404] amdgpu: Started evicting pasid 0x8002
[ 1452.799417] amdgpu: Finished evicting pasid 0x8002
[ 1452.968362] amdgpu: Started evicting pasid 0x8002
[ 1452.968377] amdgpu: Finished evicting pasid 0x8002
[ 1453.133411] amdgpu: Started evicting pasid 0x8002
[ 1453.133426] amdgpu: Finished evicting pasid 0x8002
[ 1453.297158] amdgpu: Started evicting pasid 0x8002
[ 1453.297173] amdgpu: Finished evicting pasid 0x8002
[ 1453.465314] amdgpu: Started evicting pasid 0x8002
[ 1453.465327] amdgpu: Finished evicting pasid 0x8002
[ 1453.627048] amdgpu: Started evicting pasid 0x8002
[ 1453.627064] amdgpu: Finished evicting pasid 0x8002
[ 1453.797660] amdgpu: Started evicting pasid 0x8002
[ 1453.797675] amdgpu: Finished evicting pasid 0x8002
[ 1453.961752] amdgpu: Started evicting pasid 0x8002
[ 1453.961767] amdgpu: Finished evicting pasid 0x8002
[ 1454.125556] amdgpu: Started evicting pasid 0x8002
[ 1454.125571] amdgpu: Finished evicting pasid 0x8002
[ 1454.286984] amdgpu: Started evicting pasid 0x8002
[ 1454.286999] amdgpu: Finished evicting pasid 0x8002
[ 1454.457715] amdgpu: Started evicting pasid 0x8002
[ 1454.457729] amdgpu: Finished evicting pasid 0x8002
[ 1454.624206] amdgpu: Started evicting pasid 0x8002
[ 1454.624221] amdgpu: Finished evicting pasid 0x8002
[ 1454.790899] amdgpu: Started evicting pasid 0x8002
[ 1454.790914] amdgpu: Finished evicting pasid 0x8002
[ 1454.954207] amdgpu: Started evicting pasid 0x8002
[ 1454.954221] amdgpu: Finished evicting pasid 0x8002
[ 1455.115324] amdgpu: Started evicting pasid 0x8002
[ 1455.115340] amdgpu: Finished evicting pasid 0x8002
[ 1455.328845] amdgpu: Started evicting pasid 0x8002
[ 1455.328861] amdgpu: Finished evicting pasid 0x8002
[ 1455.496682] amdgpu: Started evicting pasid 0x8002
[ 1455.496697] amdgpu: Finished evicting pasid 0x8002
[ 1455.662330] amdgpu: Started evicting pasid 0x8002
[ 1455.662345] amdgpu: Finished evicting pasid 0x8002
[ 1455.824455] amdgpu: Started evicting pasid 0x8002
[ 1455.824469] amdgpu: Finished evicting pasid 0x8002
[ 1455.986140] amdgpu: Started evicting pasid 0x8002
[ 1455.986154] amdgpu: Finished evicting pasid 0x8002
[ 1456.148233] amdgpu: Started evicting pasid 0x8002
[ 1456.148248] amdgpu: Finished evicting pasid 0x8002
[ 1456.309650] amdgpu: Started evicting pasid 0x8002
[ 1456.309664] amdgpu: Finished evicting pasid 0x8002
[ 1456.471971] amdgpu: Started evicting pasid 0x8002
[ 1456.471985] amdgpu: Finished evicting pasid 0x8002
[ 1456.634293] amdgpu: Started evicting pasid 0x8002
[ 1456.634308] amdgpu: Finished evicting pasid 0x8002
[ 1456.795885] amdgpu: Started evicting pasid 0x8002
[ 1456.795899] amdgpu: Finished evicting pasid 0x8002
[ 1456.963681] amdgpu: Started evicting pasid 0x8002
[ 1456.963695] amdgpu: Finished evicting pasid 0x8002
[ 1457.130557] amdgpu: Started evicting pasid 0x8002
[ 1457.130572] amdgpu: Finished evicting pasid 0x8002
[ 1457.292845] amdgpu: Started evicting pasid 0x8002
[ 1457.292859] amdgpu: Finished evicting pasid 0x8002
[ 1457.462540] amdgpu: Started evicting pasid 0x8002
[ 1457.462554] amdgpu: Finished evicting pasid 0x8002
[ 1457.625908] amdgpu: Started evicting pasid 0x8002
[ 1457.625922] amdgpu: Finished evicting pasid 0x8002
[ 1457.789309] amdgpu: Started evicting pasid 0x8002
[ 1457.789324] amdgpu: Finished evicting pasid 0x8002
[ 1457.951222] amdgpu: Started evicting pasid 0x8002
[ 1457.951237] amdgpu: Finished evicting pasid 0x8002
[ 1458.113008] amdgpu: Started evicting pasid 0x8002
[ 1458.113023] amdgpu: Finished evicting pasid 0x8002
[ 1458.272741] amdgpu: Started evicting pasid 0x8002
[ 1458.272761] amdgpu: Finished evicting pasid 0x8002
[ 1458.434051] amdgpu: Started evicting pasid 0x8002
[ 1458.434065] amdgpu: Finished evicting pasid 0x8002
[ 1459.478065] amdgpu: Started evicting pasid 0x8002
[ 1459.478080] amdgpu: Finished evicting pasid 0x8002
[ 1460.878243] amdgpu: Started evicting pasid 0x8002
[ 1460.878258] amdgpu: Finished evicting pasid 0x8002
[ 1461.087038] amdgpu: Started evicting pasid 0x8002
[ 1461.087053] amdgpu: Finished evicting pasid 0x8002
[ 1461.250773] amdgpu: Started evicting pasid 0x8002
[ 1461.250788] amdgpu: Finished evicting pasid 0x8002
[ 1461.417633] amdgpu: Started evicting pasid 0x8002
[ 1461.417647] amdgpu: Finished evicting pasid 0x8002
[ 1461.582175] amdgpu: Started evicting pasid 0x8002
[ 1461.582190] amdgpu: Finished evicting pasid 0x8002
[ 1461.746894] amdgpu: Started evicting pasid 0x8002
[ 1461.746908] amdgpu: Finished evicting pasid 0x8002
[ 1462.261461] amdgpu: Started evicting pasid 0x8002
[ 1462.261475] amdgpu: Finished evicting pasid 0x8002
[ 1464.004208] amdgpu: Started evicting pasid 0x8002
[ 1464.004222] amdgpu: Finished evicting pasid 0x8002
[ 1464.162834] amdgpu: Started evicting pasid 0x8002
[ 1464.162848] amdgpu: Finished evicting pasid 0x8002
[ 1464.324025] amdgpu: Started evicting pasid 0x8002
[ 1464.324039] amdgpu: Finished evicting pasid 0x8002
[ 1464.485012] amdgpu: Started evicting pasid 0x8002
[ 1464.485025] amdgpu: Finished evicting pasid 0x8002
[ 1464.646599] amdgpu: Started evicting pasid 0x8002
[ 1464.646614] amdgpu: Finished evicting pasid 0x8002
[ 1465.405333] amdgpu: Started evicting pasid 0x8002
[ 1465.405346] amdgpu: Finished evicting pasid 0x8002
[ 1465.557757] amdgpu: Started evicting pasid 0x8002
[ 1465.557771] amdgpu: Finished evicting pasid 0x8002
[ 1465.717032] amdgpu: Started evicting pasid 0x8002
[ 1465.717046] amdgpu: Finished evicting pasid 0x8002
[ 1465.885809] amdgpu: Started evicting pasid 0x8002
[ 1465.885824] amdgpu: Finished evicting pasid 0x8002
[ 1465.894911] amdgpu: Started evicting pasid 0x8003
[ 1465.894925] amdgpu: Finished evicting pasid 0x8003
[ 1466.070887] amdgpu: Started evicting pasid 0x8002
[ 1466.070902] amdgpu: Finished evicting pasid 0x8002
[ 1466.222448] amdgpu: Started evicting pasid 0x8002
[ 1466.222462] amdgpu: Finished evicting pasid 0x8002
[ 1466.394375] amdgpu: Started evicting pasid 0x8002
[ 1466.394389] amdgpu: Finished evicting pasid 0x8002
[ 1466.537905] amdgpu: Started evicting pasid 0x8002
[ 1466.537920] amdgpu: Finished evicting pasid 0x8002
[ 1466.699118] amdgpu: Started evicting pasid 0x8002
[ 1466.699132] amdgpu: Finished evicting pasid 0x8002
[ 1466.869216] amdgpu: Started evicting pasid 0x8002
[ 1466.869230] amdgpu: Finished evicting pasid 0x8002
[ 1467.033128] amdgpu: Started evicting pasid 0x8002
[ 1467.033143] amdgpu: Finished evicting pasid 0x8002
[ 1467.196820] amdgpu: Started evicting pasid 0x8002
[ 1467.196835] amdgpu: Finished evicting pasid 0x8002
[ 1467.356022] amdgpu: Started evicting pasid 0x8002
[ 1467.356036] amdgpu: Finished evicting pasid 0x8002
[ 1467.517816] amdgpu: Started evicting pasid 0x8002
[ 1467.517830] amdgpu: Finished evicting pasid 0x8002
[ 1467.751926] amdgpu: Started evicting pasid 0x8002
[ 1467.751941] amdgpu: Finished evicting pasid 0x8002
[ 1467.917610] amdgpu: Started evicting pasid 0x8002
[ 1467.917624] amdgpu: Finished evicting pasid 0x8002
[ 1468.076243] amdgpu: Started evicting pasid 0x8002
[ 1468.076257] amdgpu: Finished evicting pasid 0x8002
[ 1468.240939] amdgpu: Started evicting pasid 0x8002
[ 1468.240953] amdgpu: Finished evicting pasid 0x8002
[ 1468.398267] amdgpu: Started evicting pasid 0x8002
[ 1468.398281] amdgpu: Finished evicting pasid 0x8002
[ 1468.910412] amdgpu: Started evicting pasid 0x8002
[ 1468.910426] amdgpu: Finished evicting pasid 0x8002
[ 1469.075087] amdgpu: Started evicting pasid 0x8002
[ 1469.075102] amdgpu: Finished evicting pasid 0x8002
[ 1469.241799] amdgpu: Started evicting pasid 0x8002
[ 1469.241813] amdgpu: Finished evicting pasid 0x8002
[ 1469.401324] amdgpu: Started evicting pasid 0x8002
[ 1469.401338] amdgpu: Finished evicting pasid 0x8002
[ 1469.562939] amdgpu: Started evicting pasid 0x8002
[ 1469.562954] amdgpu: Finished evicting pasid 0x8002
[ 1469.735878] amdgpu: Started evicting pasid 0x8002
[ 1469.735887] amdgpu: Finished evicting pasid 0x8002
[ 1469.898315] amdgpu: Started evicting pasid 0x8002
[ 1469.898329] amdgpu: Finished evicting pasid 0x8002
[ 1470.061619] amdgpu: Started evicting pasid 0x8002
[ 1470.061634] amdgpu: Finished evicting pasid 0x8002
[ 1470.540376] amdgpu: Started evicting pasid 0x8002
[ 1470.540440] amdgpu: Finished evicting pasid 0x8002
[ 1472.123750] amdgpu: Started evicting pasid 0x8002
[ 1472.123816] amdgpu: Finished evicting pasid 0x8002
[ 1474.481532] amdgpu: Started evicting pasid 0x8002
[ 1474.481587] amdgpu: Finished evicting pasid 0x8002
[ 1474.973696] amdgpu: Started evicting pasid 0x8002
[ 1474.973710] amdgpu: Finished evicting pasid 0x8002
[ 1475.385303] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385311] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8200000 from client 18
[ 1475.385315] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 1475.385318] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385321] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 1475.385323] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385326] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 1475.385329] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385332] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 1475.385343] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385347] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8201000 from client 18
[ 1475.385350] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 1475.385353] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385356] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 1475.385359] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385362] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 1475.385365] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385367] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 1475.385375] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385378] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8202000 from client 18
[ 1475.385381] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 1475.385384] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385387] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 1475.385390] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385393] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 1475.385396] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385398] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 1475.385405] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385409] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8203000 from client 18
[ 1475.385411] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385414] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385417] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385420] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385423] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385426] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385429] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385438] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385441] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8204000 from client 18
[ 1475.385444] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385447] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385450] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385453] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385455] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385458] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385461] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385471] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385474] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8205000 from client 18
[ 1475.385476] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385479] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385482] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385485] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385488] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385490] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385493] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385502] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385504] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8206000 from client 18
[ 1475.385507] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385509] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385511] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385513] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385515] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385518] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385520] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385527] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385530] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8207000 from client 18
[ 1475.385532] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385534] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385536] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385539] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385541] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385543] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385546] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385551] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385554] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8208000 from client 18
[ 1475.385557] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385560] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385563] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385565] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385568] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385571] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385573] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.385584] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 8737 thread hipMemsetAsyncM pid 8737)
[ 1475.385587] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f96f8200000 from client 18
[ 1475.385588] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 1475.385590] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 1475.385592] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 1475.385594] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 1475.385595] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 1475.385597] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 1475.385599] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 1475.477607] amdgpu: Started evicting pasid 0x8002
[ 1475.477621] amdgpu: Finished evicting pasid 0x8002
[ 1475.971869] amdgpu: Started evicting pasid 0x8002
[ 1475.971885] amdgpu: Finished evicting pasid 0x8002
[ 1476.135482] amdgpu: Started evicting pasid 0x8002
[ 1476.135497] amdgpu: Finished evicting pasid 0x8002
[ 1476.946484] amdgpu: Started evicting pasid 0x8002
[ 1476.946499] amdgpu: Finished evicting pasid 0x8002
[ 1477.107786] amdgpu: Started evicting pasid 0x8002
[ 1477.107800] amdgpu: Finished evicting pasid 0x8002
[ 1477.268534] amdgpu: Started evicting pasid 0x8002
[ 1477.268547] amdgpu: Finished evicting pasid 0x8002
[ 1477.501848] amdgpu: Started evicting pasid 0x8002
[ 1477.501862] amdgpu: Finished evicting pasid 0x8002
[ 1477.901871] amdgpu: Started evicting pasid 0x8002
[ 1477.901942] amdgpu: Finished evicting pasid 0x8002
[ 1478.309124] amdgpu: Started evicting pasid 0x8002
[ 1478.309180] amdgpu: Finished evicting pasid 0x8002
[ 1478.715998] amdgpu: Started evicting pasid 0x8002
[ 1478.716058] amdgpu: Finished evicting pasid 0x8002
[ 1479.146188] amdgpu: Started evicting pasid 0x8002
[ 1479.146244] amdgpu: Finished evicting pasid 0x8002
[ 1479.625719] amdgpu: Started evicting pasid 0x8002
[ 1479.625779] amdgpu: Finished evicting pasid 0x8002
[ 1480.099063] amdgpu: Started evicting pasid 0x8002
[ 1480.099112] amdgpu: Finished evicting pasid 0x8002
[ 1480.574791] amdgpu: Started evicting pasid 0x8002
[ 1480.574840] amdgpu: Finished evicting pasid 0x8002
[ 1480.746968] amdgpu: Started evicting pasid 0x8002
[ 1480.746983] amdgpu: Finished evicting pasid 0x8002
[ 1480.909476] amdgpu: Started evicting pasid 0x8002
[ 1480.909491] amdgpu: Finished evicting pasid 0x8002
[ 1481.072911] amdgpu: Started evicting pasid 0x8002
[ 1481.072926] amdgpu: Finished evicting pasid 0x8002
[ 1481.638845] amdgpu: Started evicting pasid 0x8002
[ 1481.638860] amdgpu: Finished evicting pasid 0x8002
[ 1481.808649] amdgpu: Started evicting pasid 0x8002
[ 1481.808664] amdgpu: Finished evicting pasid 0x8002
[ 1481.970944] amdgpu: Started evicting pasid 0x8002
[ 1481.970962] amdgpu: Finished evicting pasid 0x8002
[ 1482.139663] amdgpu: Started evicting pasid 0x8002
[ 1482.139677] amdgpu: Finished evicting pasid 0x8002
[ 1482.304477] amdgpu: Started evicting pasid 0x8002
[ 1482.304492] amdgpu: Finished evicting pasid 0x8002
[ 1482.466321] amdgpu: Started evicting pasid 0x8002
[ 1482.466342] amdgpu: Finished evicting pasid 0x8002
[ 1482.699892] amdgpu: Started evicting pasid 0x8002
[ 1482.699906] amdgpu: Finished evicting pasid 0x8002
[ 1482.863407] amdgpu: Started evicting pasid 0x8002
[ 1482.863421] amdgpu: Finished evicting pasid 0x8002
[ 1515.130496] amdgpu: Started evicting pasid 0x8002
[ 1515.130510] amdgpu: Finished evicting pasid 0x8002
[ 1515.292774] amdgpu: Started evicting pasid 0x8002
[ 1515.292789] amdgpu: Finished evicting pasid 0x8002
[ 1515.454998] amdgpu: Started evicting pasid 0x8002
[ 1515.455012] amdgpu: Finished evicting pasid 0x8002
[ 1515.619317] amdgpu: Started evicting pasid 0x8002
[ 1515.619332] amdgpu: Finished evicting pasid 0x8002
[ 1515.781272] amdgpu: Started evicting pasid 0x8002
[ 1515.781286] amdgpu: Finished evicting pasid 0x8002
[ 1515.939962] amdgpu: Started evicting pasid 0x8002
[ 1515.939976] amdgpu: Finished evicting pasid 0x8002
[ 1516.101122] amdgpu: Started evicting pasid 0x8002
[ 1516.101135] amdgpu: Finished evicting pasid 0x8002
[ 1516.263067] amdgpu: Started evicting pasid 0x8002
[ 1516.263080] amdgpu: Finished evicting pasid 0x8002
[ 1527.030165] amdgpu: Started evicting pasid 0x8002
[ 1527.030180] amdgpu: Finished evicting pasid 0x8002
[ 1527.201835] amdgpu: Started evicting pasid 0x8002
[ 1527.201849] amdgpu: Finished evicting pasid 0x8002
[ 1527.364342] amdgpu: Started evicting pasid 0x8002
[ 1527.364357] amdgpu: Finished evicting pasid 0x8002
[ 1527.530310] amdgpu: Started evicting pasid 0x8002
[ 1527.530326] amdgpu: Finished evicting pasid 0x8002
[ 1527.697380] amdgpu: Started evicting pasid 0x8002
[ 1527.697394] amdgpu: Finished evicting pasid 0x8002
[ 1527.864342] amdgpu: Started evicting pasid 0x8002
[ 1527.864357] amdgpu: Finished evicting pasid 0x8002
[ 1533.691394] amdgpu: Started evicting pasid 0x8002
[ 1533.691410] amdgpu: Finished evicting pasid 0x8002
[ 1535.367721] amdgpu: Started evicting pasid 0x8002
[ 1535.367735] amdgpu: Finished evicting pasid 0x8002
[ 1535.528591] amdgpu: Started evicting pasid 0x8002
[ 1535.528606] amdgpu: Finished evicting pasid 0x8002
[ 1535.689716] amdgpu: Started evicting pasid 0x8002
[ 1535.689730] amdgpu: Finished evicting pasid 0x8002
[ 1535.852509] amdgpu: Started evicting pasid 0x8002
[ 1535.852523] amdgpu: Finished evicting pasid 0x8002
[ 1536.322039] amdgpu: Started evicting pasid 0x8002
[ 1536.322054] amdgpu: Finished evicting pasid 0x8002
[ 1536.488886] amdgpu: Started evicting pasid 0x8002
[ 1536.488901] amdgpu: Finished evicting pasid 0x8002
[ 4052.139961] amdgpu: Started evicting pasid 0x8002
[ 4052.139972] amdgpu: Finished evicting pasid 0x8002
[ 4052.242056] amdgpu: Started restoring pasid 0x8002
[ 4052.242072] amdgpu: Finished restoring pasid 0x8002
[ 4052.291148] amdgpu: Started evicting pasid 0x8002
[ 4052.291158] amdgpu: Finished evicting pasid 0x8002
[ 4052.518692] amdgpu: Started evicting pasid 0x8002
[ 4052.518706] amdgpu: Finished evicting pasid 0x8002
[ 4054.137056] amdgpu: Started evicting pasid 0x8002
[ 4054.137070] amdgpu: Finished evicting pasid 0x8002
[ 4055.873744] amdgpu: Started evicting pasid 0x8002
[ 4055.873758] amdgpu: Finished evicting pasid 0x8002
[ 4056.039440] amdgpu: Started evicting pasid 0x8002
[ 4056.039454] amdgpu: Finished evicting pasid 0x8002
[ 4056.198877] amdgpu: Started evicting pasid 0x8002
[ 4056.198891] amdgpu: Finished evicting pasid 0x8002
[ 4056.364222] amdgpu: Started evicting pasid 0x8002
[ 4056.364236] amdgpu: Finished evicting pasid 0x8002
[ 4056.555148] amdgpu: Started evicting pasid 0x8002
[ 4056.555162] amdgpu: Finished evicting pasid 0x8002
[ 4056.721399] amdgpu: Started evicting pasid 0x8002
[ 4056.721414] amdgpu: Finished evicting pasid 0x8002
[ 4056.879625] amdgpu: Started evicting pasid 0x8002
[ 4056.879638] amdgpu: Finished evicting pasid 0x8002
[ 4057.038506] amdgpu: Started evicting pasid 0x8002
[ 4057.038520] amdgpu: Finished evicting pasid 0x8002
[ 4057.199752] amdgpu: Started evicting pasid 0x8002
[ 4057.199766] amdgpu: Finished evicting pasid 0x8002
[ 4057.361404] amdgpu: Started evicting pasid 0x8002
[ 4057.361418] amdgpu: Finished evicting pasid 0x8002
[ 4057.523290] amdgpu: Started evicting pasid 0x8002
[ 4057.523304] amdgpu: Finished evicting pasid 0x8002
[ 4057.685884] amdgpu: Started evicting pasid 0x8002
[ 4057.685898] amdgpu: Finished evicting pasid 0x8002
[ 4057.854878] amdgpu: Started evicting pasid 0x8002
[ 4057.854892] amdgpu: Finished evicting pasid 0x8002
[ 4058.048242] amdgpu: Started evicting pasid 0x8002
[ 4058.048255] amdgpu: Finished evicting pasid 0x8002
[ 4058.210730] amdgpu: Started evicting pasid 0x8002
[ 4058.210744] amdgpu: Finished evicting pasid 0x8002
[ 4058.374334] amdgpu: Started evicting pasid 0x8002
[ 4058.374348] amdgpu: Finished evicting pasid 0x8002
[ 4058.542947] amdgpu: Started evicting pasid 0x8002
[ 4058.542960] amdgpu: Finished evicting pasid 0x8002
[ 4058.705809] amdgpu: Started evicting pasid 0x8002
[ 4058.705823] amdgpu: Finished evicting pasid 0x8002
[ 4058.869139] amdgpu: Started evicting pasid 0x8002
[ 4058.869153] amdgpu: Finished evicting pasid 0x8002
[ 4059.031129] amdgpu: Started evicting pasid 0x8002
[ 4059.031143] amdgpu: Finished evicting pasid 0x8002
[ 4059.192405] amdgpu: Started evicting pasid 0x8002
[ 4059.192418] amdgpu: Finished evicting pasid 0x8002
[ 4059.354393] amdgpu: Started evicting pasid 0x8002
[ 4059.354407] amdgpu: Finished evicting pasid 0x8002
[ 4059.518418] amdgpu: Started evicting pasid 0x8002
[ 4059.518432] amdgpu: Finished evicting pasid 0x8002
[ 4059.678299] amdgpu: Started evicting pasid 0x8002
[ 4059.678313] amdgpu: Finished evicting pasid 0x8002
[ 4059.842641] amdgpu: Started evicting pasid 0x8002
[ 4059.842656] amdgpu: Finished evicting pasid 0x8002
[ 4060.010527] amdgpu: Started evicting pasid 0x8002
[ 4060.010541] amdgpu: Finished evicting pasid 0x8002
[ 4060.175075] amdgpu: Started evicting pasid 0x8002
[ 4060.175089] amdgpu: Finished evicting pasid 0x8002
[ 4060.340100] amdgpu: Started evicting pasid 0x8002
[ 4060.340114] amdgpu: Finished evicting pasid 0x8002
[ 4060.530769] amdgpu: Started evicting pasid 0x8002
[ 4060.530783] amdgpu: Finished evicting pasid 0x8002
[ 4060.722277] amdgpu: Started evicting pasid 0x8002
[ 4060.722291] amdgpu: Finished evicting pasid 0x8002
[ 4060.889115] amdgpu: Started evicting pasid 0x8002
[ 4060.889129] amdgpu: Finished evicting pasid 0x8002
[ 4061.048140] amdgpu: Started evicting pasid 0x8002
[ 4061.048153] amdgpu: Finished evicting pasid 0x8002
[ 4061.206734] amdgpu: Started evicting pasid 0x8002
[ 4061.206747] amdgpu: Finished evicting pasid 0x8002
[ 4061.366307] amdgpu: Started evicting pasid 0x8002
[ 4061.366321] amdgpu: Finished evicting pasid 0x8002
[ 4061.527840] amdgpu: Started evicting pasid 0x8002
[ 4061.527854] amdgpu: Finished evicting pasid 0x8002
[ 4061.688634] amdgpu: Started evicting pasid 0x8002
[ 4061.688648] amdgpu: Finished evicting pasid 0x8002
[ 4061.848324] amdgpu: Started evicting pasid 0x8002
[ 4061.848338] amdgpu: Finished evicting pasid 0x8002
[ 4062.010290] amdgpu: Started evicting pasid 0x8002
[ 4062.010304] amdgpu: Finished evicting pasid 0x8002
[ 4062.173997] amdgpu: Started evicting pasid 0x8002
[ 4062.174010] amdgpu: Finished evicting pasid 0x8002
[ 4062.338129] amdgpu: Started evicting pasid 0x8002
[ 4062.338143] amdgpu: Finished evicting pasid 0x8002
[ 4062.498575] amdgpu: Started evicting pasid 0x8002
[ 4062.498588] amdgpu: Finished evicting pasid 0x8002
[ 4062.659077] amdgpu: Started evicting pasid 0x8002
[ 4062.659092] amdgpu: Finished evicting pasid 0x8002
[ 4062.820882] amdgpu: Started evicting pasid 0x8002
[ 4062.820895] amdgpu: Finished evicting pasid 0x8002
[ 4062.982060] amdgpu: Started evicting pasid 0x8002
[ 4062.982073] amdgpu: Finished evicting pasid 0x8002
[ 4063.146064] amdgpu: Started evicting pasid 0x8002
[ 4063.146079] amdgpu: Finished evicting pasid 0x8002
[ 4063.306180] amdgpu: Started evicting pasid 0x8002
[ 4063.306192] amdgpu: Finished evicting pasid 0x8002
[ 4063.840901] amdgpu: Started evicting pasid 0x8002
[ 4063.840915] amdgpu: Finished evicting pasid 0x8002
[ 4064.003006] amdgpu: Started evicting pasid 0x8002
[ 4064.003020] amdgpu: Finished evicting pasid 0x8002
[ 4064.164486] amdgpu: Started evicting pasid 0x8002
[ 4064.164500] amdgpu: Finished evicting pasid 0x8002
[ 4064.323496] amdgpu: Started evicting pasid 0x8002
[ 4064.323510] amdgpu: Finished evicting pasid 0x8002
[ 4064.486300] amdgpu: Started evicting pasid 0x8002
[ 4064.486314] amdgpu: Finished evicting pasid 0x8002
[ 4064.648513] amdgpu: Started evicting pasid 0x8002
[ 4064.648527] amdgpu: Finished evicting pasid 0x8002
[ 4064.813608] amdgpu: Started evicting pasid 0x8002
[ 4064.813622] amdgpu: Finished evicting pasid 0x8002
[ 4064.973625] amdgpu: Started evicting pasid 0x8002
[ 4064.973638] amdgpu: Finished evicting pasid 0x8002
[ 4065.135854] amdgpu: Started evicting pasid 0x8002
[ 4065.135868] amdgpu: Finished evicting pasid 0x8002
[ 4065.299670] amdgpu: Started evicting pasid 0x8002
[ 4065.299684] amdgpu: Finished evicting pasid 0x8002
[ 4065.460060] amdgpu: Started evicting pasid 0x8002
[ 4065.460074] amdgpu: Finished evicting pasid 0x8002
[ 4065.621374] amdgpu: Started evicting pasid 0x8002
[ 4065.621387] amdgpu: Finished evicting pasid 0x8002
[ 4065.783635] amdgpu: Started evicting pasid 0x8002
[ 4065.783650] amdgpu: Finished evicting pasid 0x8002
[ 4065.946671] amdgpu: Started evicting pasid 0x8002
[ 4065.946685] amdgpu: Finished evicting pasid 0x8002
[ 4066.111051] amdgpu: Started evicting pasid 0x8002
[ 4066.111065] amdgpu: Finished evicting pasid 0x8002
[ 4066.278047] amdgpu: Started evicting pasid 0x8002
[ 4066.278061] amdgpu: Finished evicting pasid 0x8002
[ 4066.441710] amdgpu: Started evicting pasid 0x8002
[ 4066.441724] amdgpu: Finished evicting pasid 0x8002
[ 4066.603789] amdgpu: Started evicting pasid 0x8002
[ 4066.603803] amdgpu: Finished evicting pasid 0x8002
[ 4066.766295] amdgpu: Started evicting pasid 0x8002
[ 4066.766310] amdgpu: Finished evicting pasid 0x8002
[ 4066.929534] amdgpu: Started evicting pasid 0x8002
[ 4066.929547] amdgpu: Finished evicting pasid 0x8002
[ 4067.090080] amdgpu: Started evicting pasid 0x8002
[ 4067.090094] amdgpu: Finished evicting pasid 0x8002
[ 4067.252831] amdgpu: Started evicting pasid 0x8002
[ 4067.252845] amdgpu: Finished evicting pasid 0x8002
[ 4067.414430] amdgpu: Started evicting pasid 0x8002
[ 4067.414444] amdgpu: Finished evicting pasid 0x8002
[ 4067.576762] amdgpu: Started evicting pasid 0x8002
[ 4067.576775] amdgpu: Finished evicting pasid 0x8002
[ 4067.738260] amdgpu: Started evicting pasid 0x8002
[ 4067.738274] amdgpu: Finished evicting pasid 0x8002
[ 4067.902267] amdgpu: Started evicting pasid 0x8002
[ 4067.902281] amdgpu: Finished evicting pasid 0x8002
[ 4068.061626] amdgpu: Started evicting pasid 0x8002
[ 4068.061639] amdgpu: Finished evicting pasid 0x8002
[ 4068.223550] amdgpu: Started evicting pasid 0x8002
[ 4068.223564] amdgpu: Finished evicting pasid 0x8002
[ 4068.382218] amdgpu: Started evicting pasid 0x8002
[ 4068.382233] amdgpu: Finished evicting pasid 0x8002
[ 4068.546931] amdgpu: Started evicting pasid 0x8002
[ 4068.546946] amdgpu: Finished evicting pasid 0x8002
[ 4068.709812] amdgpu: Started evicting pasid 0x8002
[ 4068.709826] amdgpu: Finished evicting pasid 0x8002
[ 4068.876322] amdgpu: Started evicting pasid 0x8002
[ 4068.876336] amdgpu: Finished evicting pasid 0x8002
[ 4069.040969] amdgpu: Started evicting pasid 0x8002
[ 4069.040983] amdgpu: Finished evicting pasid 0x8002
[ 4069.206007] amdgpu: Started evicting pasid 0x8002
[ 4069.206029] amdgpu: Finished evicting pasid 0x8002
[ 4069.372760] amdgpu: Started evicting pasid 0x8002
[ 4069.372774] amdgpu: Finished evicting pasid 0x8002
[ 4069.940357] amdgpu: Started evicting pasid 0x8002
[ 4069.940371] amdgpu: Finished evicting pasid 0x8002
[ 4070.855607] amdgpu: Started evicting pasid 0x8002
[ 4070.855621] amdgpu: Finished evicting pasid 0x8002
[ 4071.065970] amdgpu: Started evicting pasid 0x8002
[ 4071.065983] amdgpu: Finished evicting pasid 0x8002
[ 4071.234354] amdgpu: Started evicting pasid 0x8002
[ 4071.234369] amdgpu: Finished evicting pasid 0x8002
[ 4071.397036] amdgpu: Started evicting pasid 0x8002
[ 4071.397049] amdgpu: Finished evicting pasid 0x8002
[ 4071.562477] amdgpu: Started evicting pasid 0x8002
[ 4071.562492] amdgpu: Finished evicting pasid 0x8002
[ 4071.723237] amdgpu: Started evicting pasid 0x8002
[ 4071.723251] amdgpu: Finished evicting pasid 0x8002
[ 4072.244701] amdgpu: Started evicting pasid 0x8002
[ 4072.244715] amdgpu: Finished evicting pasid 0x8002
[ 4073.976443] amdgpu: Started evicting pasid 0x8002
[ 4073.976457] amdgpu: Finished evicting pasid 0x8002
[ 4074.145538] amdgpu: Started evicting pasid 0x8002
[ 4074.145552] amdgpu: Finished evicting pasid 0x8002
[ 4074.308390] amdgpu: Started evicting pasid 0x8002
[ 4074.308404] amdgpu: Finished evicting pasid 0x8002
[ 4074.469062] amdgpu: Started evicting pasid 0x8002
[ 4074.469076] amdgpu: Finished evicting pasid 0x8002
[ 4074.630632] amdgpu: Started evicting pasid 0x8002
[ 4074.630646] amdgpu: Finished evicting pasid 0x8002
[ 4075.360762] amdgpu: Started evicting pasid 0x8002
[ 4075.360776] amdgpu: Finished evicting pasid 0x8002
[ 4075.526412] amdgpu: Started evicting pasid 0x8002
[ 4075.526425] amdgpu: Finished evicting pasid 0x8002
[ 4075.692771] amdgpu: Started evicting pasid 0x8002
[ 4075.692785] amdgpu: Finished evicting pasid 0x8002
[ 4075.861847] amdgpu: Started evicting pasid 0x8002
[ 4075.861862] amdgpu: Finished evicting pasid 0x8002
[ 4075.871822] amdgpu: Started evicting pasid 0x8003
[ 4075.871835] amdgpu: Finished evicting pasid 0x8003
[ 4076.038767] amdgpu: Started evicting pasid 0x8002
[ 4076.038781] amdgpu: Finished evicting pasid 0x8002
[ 4076.178560] amdgpu: Started evicting pasid 0x8002
[ 4076.178572] amdgpu: Finished evicting pasid 0x8002
[ 4076.349997] amdgpu: Started evicting pasid 0x8002
[ 4076.350011] amdgpu: Finished evicting pasid 0x8002
[ 4076.493871] amdgpu: Started evicting pasid 0x8002
[ 4076.493884] amdgpu: Finished evicting pasid 0x8002
[ 4076.653926] amdgpu: Started evicting pasid 0x8002
[ 4076.653939] amdgpu: Finished evicting pasid 0x8002
[ 4076.816082] amdgpu: Started evicting pasid 0x8002
[ 4076.816096] amdgpu: Finished evicting pasid 0x8002
[ 4076.981974] amdgpu: Started evicting pasid 0x8002
[ 4076.981988] amdgpu: Finished evicting pasid 0x8002
[ 4077.140312] amdgpu: Started evicting pasid 0x8002
[ 4077.140326] amdgpu: Finished evicting pasid 0x8002
[ 4077.306023] amdgpu: Started evicting pasid 0x8002
[ 4077.306037] amdgpu: Finished evicting pasid 0x8002
[ 4077.472540] amdgpu: Started evicting pasid 0x8002
[ 4077.472554] amdgpu: Finished evicting pasid 0x8002
[ 4077.709659] amdgpu: Started evicting pasid 0x8002
[ 4077.709673] amdgpu: Finished evicting pasid 0x8002
[ 4077.876206] amdgpu: Started evicting pasid 0x8002
[ 4077.876220] amdgpu: Finished evicting pasid 0x8002
[ 4078.040319] amdgpu: Started evicting pasid 0x8002
[ 4078.040333] amdgpu: Finished evicting pasid 0x8002
[ 4078.208326] amdgpu: Started evicting pasid 0x8002
[ 4078.208339] amdgpu: Finished evicting pasid 0x8002
[ 4078.372143] amdgpu: Started evicting pasid 0x8002
[ 4078.372157] amdgpu: Finished evicting pasid 0x8002
[ 4078.884059] amdgpu: Started evicting pasid 0x8002
[ 4078.884074] amdgpu: Finished evicting pasid 0x8002
[ 4079.050468] amdgpu: Started evicting pasid 0x8002
[ 4079.050481] amdgpu: Finished evicting pasid 0x8002
[ 4079.214254] amdgpu: Started evicting pasid 0x8002
[ 4079.214268] amdgpu: Finished evicting pasid 0x8002
[ 4079.377610] amdgpu: Started evicting pasid 0x8002
[ 4079.377623] amdgpu: Finished evicting pasid 0x8002
[ 4079.542149] amdgpu: Started evicting pasid 0x8002
[ 4079.542164] amdgpu: Finished evicting pasid 0x8002
[ 4079.718126] amdgpu: Started evicting pasid 0x8002
[ 4079.718147] amdgpu: Finished evicting pasid 0x8002
[ 4079.880495] amdgpu: Started evicting pasid 0x8002
[ 4079.880509] amdgpu: Finished evicting pasid 0x8002
[ 4080.044948] amdgpu: Started evicting pasid 0x8002
[ 4080.044962] amdgpu: Finished evicting pasid 0x8002
[ 4080.561099] show_signal: 26 callbacks suppressed
[ 4080.561101] traps: hipMemset[59668] general protection fault ip:7f3d2745bb25 sp:7fff276a3170 error:0 in libamdhip64.so.4.0.20496-4f163c68[7f3d272f8000+2f1000]
[ 4080.646657] amdgpu: Started evicting pasid 0x8002
[ 4080.646718] amdgpu: Finished evicting pasid 0x8002
[ 4082.221387] amdgpu: Started evicting pasid 0x8002
[ 4082.221451] amdgpu: Finished evicting pasid 0x8002
[ 4084.570744] amdgpu: Started evicting pasid 0x8002
[ 4084.570758] amdgpu: Finished evicting pasid 0x8002
[ 4085.059300] amdgpu: Started evicting pasid 0x8002
[ 4085.059313] amdgpu: Finished evicting pasid 0x8002
[ 4085.415659] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415664] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050200000 from client 18
[ 4085.415667] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 4085.415669] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415671] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 4085.415673] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415675] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 4085.415676] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415678] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 4085.415686] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415689] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050201000 from client 18
[ 4085.415691] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 4085.415693] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415694] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 4085.415696] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415698] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 4085.415700] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415702] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 4085.415707] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415709] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050202000 from client 18
[ 4085.415711] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 4085.415713] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415715] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 4085.415717] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415719] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 4085.415721] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415723] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 4085.415728] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415730] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050203000 from client 18
[ 4085.415732] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 4085.415734] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415735] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 4085.415737] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415739] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 4085.415741] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415743] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 4085.415748] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415750] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050204000 from client 18
[ 4085.415752] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 4085.415754] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415756] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 4085.415758] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415760] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 4085.415761] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415763] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 4085.415770] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415772] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050205000 from client 18
[ 4085.415774] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 4085.415776] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415778] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 4085.415780] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415781] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 4085.415783] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415785] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 4085.415792] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415794] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050208000 from client 18
[ 4085.415796] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 4085.415798] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415800] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 4085.415802] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415804] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 4085.415806] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415807] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 4085.415813] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415815] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050206000 from client 18
[ 4085.415816] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 4085.415818] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415819] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 4085.415821] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415822] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 4085.415823] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415825] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 4085.415829] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 59857 thread hipMemsetAsyncM pid 59857)
[ 4085.415830] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9050207000 from client 18
[ 4085.415832] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 4085.415833] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 4085.415834] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 4085.415836] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 4085.415837] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 4085.415838] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 4085.415840] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 4085.503552] amdgpu: Started evicting pasid 0x8002
[ 4085.503563] amdgpu: Finished evicting pasid 0x8002
[ 4085.988207] amdgpu: Started evicting pasid 0x8002
[ 4085.988219] amdgpu: Finished evicting pasid 0x8002
[ 4086.148176] amdgpu: Started evicting pasid 0x8002
[ 4086.148190] amdgpu: Finished evicting pasid 0x8002
[ 4086.949219] amdgpu: Started evicting pasid 0x8002
[ 4086.949234] amdgpu: Finished evicting pasid 0x8002
[ 4087.108621] amdgpu: Started evicting pasid 0x8002
[ 4087.108635] amdgpu: Finished evicting pasid 0x8002
[ 4087.273142] amdgpu: Started evicting pasid 0x8002
[ 4087.273156] amdgpu: Finished evicting pasid 0x8002
[ 4087.499495] amdgpu: Started evicting pasid 0x8002
[ 4087.499509] amdgpu: Finished evicting pasid 0x8002
[ 4087.895550] amdgpu: Started evicting pasid 0x8002
[ 4087.895606] amdgpu: Finished evicting pasid 0x8002
[ 4088.301721] amdgpu: Started evicting pasid 0x8002
[ 4088.301775] amdgpu: Finished evicting pasid 0x8002
[ 4088.703538] amdgpu: Started evicting pasid 0x8002
[ 4088.703594] amdgpu: Finished evicting pasid 0x8002
[ 4089.132227] amdgpu: Started evicting pasid 0x8002
[ 4089.132283] amdgpu: Finished evicting pasid 0x8002
[ 4089.593276] amdgpu: Started evicting pasid 0x8002
[ 4089.593325] amdgpu: Finished evicting pasid 0x8002
[ 4090.057569] amdgpu: Started evicting pasid 0x8002
[ 4090.057621] amdgpu: Finished evicting pasid 0x8002
[ 4090.530368] amdgpu: Started evicting pasid 0x8002
[ 4090.530421] amdgpu: Finished evicting pasid 0x8002
[ 4090.703537] amdgpu: Started evicting pasid 0x8002
[ 4090.703552] amdgpu: Finished evicting pasid 0x8002
[ 4090.864734] amdgpu: Started evicting pasid 0x8002
[ 4090.864748] amdgpu: Finished evicting pasid 0x8002
[ 4091.030483] amdgpu: Started evicting pasid 0x8002
[ 4091.030498] amdgpu: Finished evicting pasid 0x8002
[ 4091.583352] amdgpu: Started evicting pasid 0x8002
[ 4091.583367] amdgpu: Finished evicting pasid 0x8002
[ 4091.751739] amdgpu: Started evicting pasid 0x8002
[ 4091.751753] amdgpu: Finished evicting pasid 0x8002
[ 4091.915483] amdgpu: Started evicting pasid 0x8002
[ 4091.915497] amdgpu: Finished evicting pasid 0x8002
[ 4092.080905] amdgpu: Started evicting pasid 0x8002
[ 4092.080920] amdgpu: Finished evicting pasid 0x8002
[ 4092.248722] amdgpu: Started evicting pasid 0x8002
[ 4092.248736] amdgpu: Finished evicting pasid 0x8002
[ 4092.410011] amdgpu: Started evicting pasid 0x8002
[ 4092.410025] amdgpu: Finished evicting pasid 0x8002
[ 4092.643527] amdgpu: Started evicting pasid 0x8002
[ 4092.643541] amdgpu: Finished evicting pasid 0x8002
[ 4092.804729] amdgpu: Started evicting pasid 0x8002
[ 4092.804750] amdgpu: Finished evicting pasid 0x8002
[ 4128.948694] amdgpu: Started evicting pasid 0x8002
[ 4128.948708] amdgpu: Finished evicting pasid 0x8002
[ 4129.110681] amdgpu: Started evicting pasid 0x8002
[ 4129.110695] amdgpu: Finished evicting pasid 0x8002
[ 4129.272178] amdgpu: Started evicting pasid 0x8002
[ 4129.272192] amdgpu: Finished evicting pasid 0x8002
[ 4129.438551] amdgpu: Started evicting pasid 0x8002
[ 4129.438565] amdgpu: Finished evicting pasid 0x8002
[ 4129.597075] amdgpu: Started evicting pasid 0x8002
[ 4129.597089] amdgpu: Finished evicting pasid 0x8002
[ 4129.766717] amdgpu: Started evicting pasid 0x8002
[ 4129.766731] amdgpu: Finished evicting pasid 0x8002
[ 4129.928277] amdgpu: Started evicting pasid 0x8002
[ 4129.928291] amdgpu: Finished evicting pasid 0x8002
[ 4130.093207] amdgpu: Started evicting pasid 0x8002
[ 4130.093220] amdgpu: Finished evicting pasid 0x8002
[ 4140.818328] amdgpu: Started evicting pasid 0x8002
[ 4140.818343] amdgpu: Finished evicting pasid 0x8002
[ 4140.980145] amdgpu: Started evicting pasid 0x8002
[ 4140.980158] amdgpu: Finished evicting pasid 0x8002
[ 4141.140677] amdgpu: Started evicting pasid 0x8002
[ 4141.140691] amdgpu: Finished evicting pasid 0x8002
[ 4141.301789] amdgpu: Started evicting pasid 0x8002
[ 4141.301803] amdgpu: Finished evicting pasid 0x8002
[ 4141.462706] amdgpu: Started evicting pasid 0x8002
[ 4141.462720] amdgpu: Finished evicting pasid 0x8002
[ 4141.626103] amdgpu: Started evicting pasid 0x8002
[ 4141.626117] amdgpu: Finished evicting pasid 0x8002
[ 4147.432833] amdgpu: Started evicting pasid 0x8002
[ 4147.432847] amdgpu: Finished evicting pasid 0x8002
[ 4149.088190] amdgpu: Started evicting pasid 0x8002
[ 4149.088204] amdgpu: Finished evicting pasid 0x8002
[ 4149.249257] amdgpu: Started evicting pasid 0x8002
[ 4149.249272] amdgpu: Finished evicting pasid 0x8002
[ 4149.410672] amdgpu: Started evicting pasid 0x8002
[ 4149.410686] amdgpu: Finished evicting pasid 0x8002
[ 4149.572348] amdgpu: Started evicting pasid 0x8002
[ 4149.572363] amdgpu: Finished evicting pasid 0x8002
[ 4150.044303] amdgpu: Started evicting pasid 0x8002
[ 4150.044317] amdgpu: Finished evicting pasid 0x8002
[ 4150.203888] amdgpu: Started evicting pasid 0x8002
[ 4150.203902] amdgpu: Finished evicting pasid 0x8002
[ 6024.130611] amdgpu: Started evicting pasid 0x8002
[ 6024.130622] amdgpu: Finished evicting pasid 0x8002
[ 6024.231689] amdgpu: Started restoring pasid 0x8002
[ 6024.231705] amdgpu: Finished restoring pasid 0x8002
[ 6024.280880] amdgpu: Started evicting pasid 0x8002
[ 6024.280890] amdgpu: Finished evicting pasid 0x8002
[ 6024.513517] amdgpu: Started evicting pasid 0x8002
[ 6024.513532] amdgpu: Finished evicting pasid 0x8002
[ 6026.169726] amdgpu: Started evicting pasid 0x8002
[ 6026.169740] amdgpu: Finished evicting pasid 0x8002
[ 6027.928427] amdgpu: Started evicting pasid 0x8002
[ 6027.928442] amdgpu: Finished evicting pasid 0x8002
[ 6028.098203] amdgpu: Started evicting pasid 0x8002
[ 6028.098216] amdgpu: Finished evicting pasid 0x8002
[ 6028.263066] amdgpu: Started evicting pasid 0x8002
[ 6028.263081] amdgpu: Finished evicting pasid 0x8002
[ 6028.424475] amdgpu: Started evicting pasid 0x8002
[ 6028.424489] amdgpu: Finished evicting pasid 0x8002
[ 6028.619372] amdgpu: Started evicting pasid 0x8002
[ 6028.619386] amdgpu: Finished evicting pasid 0x8002
[ 6028.787932] amdgpu: Started evicting pasid 0x8002
[ 6028.787946] amdgpu: Finished evicting pasid 0x8002
[ 6028.960315] amdgpu: Started evicting pasid 0x8002
[ 6028.960330] amdgpu: Finished evicting pasid 0x8002
[ 6029.126650] amdgpu: Started evicting pasid 0x8002
[ 6029.126664] amdgpu: Finished evicting pasid 0x8002
[ 6029.291478] amdgpu: Started evicting pasid 0x8002
[ 6029.291492] amdgpu: Finished evicting pasid 0x8002
[ 6029.461998] amdgpu: Started evicting pasid 0x8002
[ 6029.462013] amdgpu: Finished evicting pasid 0x8002
[ 6029.626732] amdgpu: Started evicting pasid 0x8002
[ 6029.626746] amdgpu: Finished evicting pasid 0x8002
[ 6029.790655] amdgpu: Started evicting pasid 0x8002
[ 6029.790670] amdgpu: Finished evicting pasid 0x8002
[ 6029.959156] amdgpu: Started evicting pasid 0x8002
[ 6029.959171] amdgpu: Finished evicting pasid 0x8002
[ 6030.153003] amdgpu: Started evicting pasid 0x8002
[ 6030.153017] amdgpu: Finished evicting pasid 0x8002
[ 6030.315419] amdgpu: Started evicting pasid 0x8002
[ 6030.315434] amdgpu: Finished evicting pasid 0x8002
[ 6030.486340] amdgpu: Started evicting pasid 0x8002
[ 6030.486354] amdgpu: Finished evicting pasid 0x8002
[ 6030.647468] amdgpu: Started evicting pasid 0x8002
[ 6030.647481] amdgpu: Finished evicting pasid 0x8002
[ 6030.816949] amdgpu: Started evicting pasid 0x8002
[ 6030.816962] amdgpu: Finished evicting pasid 0x8002
[ 6030.982524] amdgpu: Started evicting pasid 0x8002
[ 6030.982538] amdgpu: Finished evicting pasid 0x8002
[ 6031.143319] amdgpu: Started evicting pasid 0x8002
[ 6031.143333] amdgpu: Finished evicting pasid 0x8002
[ 6031.306199] amdgpu: Started evicting pasid 0x8002
[ 6031.306212] amdgpu: Finished evicting pasid 0x8002
[ 6031.472575] amdgpu: Started evicting pasid 0x8002
[ 6031.472588] amdgpu: Finished evicting pasid 0x8002
[ 6031.640407] amdgpu: Started evicting pasid 0x8002
[ 6031.640424] amdgpu: Finished evicting pasid 0x8002
[ 6031.802304] amdgpu: Started evicting pasid 0x8002
[ 6031.802318] amdgpu: Finished evicting pasid 0x8002
[ 6031.962674] amdgpu: Started evicting pasid 0x8002
[ 6031.962688] amdgpu: Finished evicting pasid 0x8002
[ 6032.124884] amdgpu: Started evicting pasid 0x8002
[ 6032.124897] amdgpu: Finished evicting pasid 0x8002
[ 6032.287379] amdgpu: Started evicting pasid 0x8002
[ 6032.287393] amdgpu: Finished evicting pasid 0x8002
[ 6032.455665] amdgpu: Started evicting pasid 0x8002
[ 6032.455680] amdgpu: Finished evicting pasid 0x8002
[ 6032.645830] amdgpu: Started evicting pasid 0x8002
[ 6032.645845] amdgpu: Finished evicting pasid 0x8002
[ 6032.835524] amdgpu: Started evicting pasid 0x8002
[ 6032.835538] amdgpu: Finished evicting pasid 0x8002
[ 6033.005736] amdgpu: Started evicting pasid 0x8002
[ 6033.005749] amdgpu: Finished evicting pasid 0x8002
[ 6033.170010] amdgpu: Started evicting pasid 0x8002
[ 6033.170024] amdgpu: Finished evicting pasid 0x8002
[ 6033.331329] amdgpu: Started evicting pasid 0x8002
[ 6033.331343] amdgpu: Finished evicting pasid 0x8002
[ 6033.493281] amdgpu: Started evicting pasid 0x8002
[ 6033.493295] amdgpu: Finished evicting pasid 0x8002
[ 6033.654393] amdgpu: Started evicting pasid 0x8002
[ 6033.654407] amdgpu: Finished evicting pasid 0x8002
[ 6033.816705] amdgpu: Started evicting pasid 0x8002
[ 6033.816718] amdgpu: Finished evicting pasid 0x8002
[ 6033.978835] amdgpu: Started evicting pasid 0x8002
[ 6033.978850] amdgpu: Finished evicting pasid 0x8002
[ 6034.140441] amdgpu: Started evicting pasid 0x8002
[ 6034.140456] amdgpu: Finished evicting pasid 0x8002
[ 6034.306710] amdgpu: Started evicting pasid 0x8002
[ 6034.306724] amdgpu: Finished evicting pasid 0x8002
[ 6034.474951] amdgpu: Started evicting pasid 0x8002
[ 6034.474974] amdgpu: Finished evicting pasid 0x8002
[ 6034.645100] amdgpu: Started evicting pasid 0x8002
[ 6034.645114] amdgpu: Finished evicting pasid 0x8002
[ 6034.809092] amdgpu: Started evicting pasid 0x8002
[ 6034.809107] amdgpu: Finished evicting pasid 0x8002
[ 6034.971202] amdgpu: Started evicting pasid 0x8002
[ 6034.971216] amdgpu: Finished evicting pasid 0x8002
[ 6035.141564] amdgpu: Started evicting pasid 0x8002
[ 6035.141580] amdgpu: Finished evicting pasid 0x8002
[ 6035.304501] amdgpu: Started evicting pasid 0x8002
[ 6035.304514] amdgpu: Finished evicting pasid 0x8002
[ 6035.466171] amdgpu: Started evicting pasid 0x8002
[ 6035.466185] amdgpu: Finished evicting pasid 0x8002
[ 6036.002932] amdgpu: Started evicting pasid 0x8002
[ 6036.002947] amdgpu: Finished evicting pasid 0x8002
[ 6036.165021] amdgpu: Started evicting pasid 0x8002
[ 6036.165035] amdgpu: Finished evicting pasid 0x8002
[ 6036.331300] amdgpu: Started evicting pasid 0x8002
[ 6036.331314] amdgpu: Finished evicting pasid 0x8002
[ 6036.496617] amdgpu: Started evicting pasid 0x8002
[ 6036.496631] amdgpu: Finished evicting pasid 0x8002
[ 6036.657863] amdgpu: Started evicting pasid 0x8002
[ 6036.657878] amdgpu: Finished evicting pasid 0x8002
[ 6036.820818] amdgpu: Started evicting pasid 0x8002
[ 6036.820832] amdgpu: Finished evicting pasid 0x8002
[ 6036.981926] amdgpu: Started evicting pasid 0x8002
[ 6036.981940] amdgpu: Finished evicting pasid 0x8002
[ 6037.144758] amdgpu: Started evicting pasid 0x8002
[ 6037.144773] amdgpu: Finished evicting pasid 0x8002
[ 6037.305754] amdgpu: Started evicting pasid 0x8002
[ 6037.305768] amdgpu: Finished evicting pasid 0x8002
[ 6037.468998] amdgpu: Started evicting pasid 0x8002
[ 6037.469013] amdgpu: Finished evicting pasid 0x8002
[ 6037.636074] amdgpu: Started evicting pasid 0x8002
[ 6037.636087] amdgpu: Finished evicting pasid 0x8002
[ 6037.800865] amdgpu: Started evicting pasid 0x8002
[ 6037.800879] amdgpu: Finished evicting pasid 0x8002
[ 6037.967833] amdgpu: Started evicting pasid 0x8002
[ 6037.967847] amdgpu: Finished evicting pasid 0x8002
[ 6038.132139] amdgpu: Started evicting pasid 0x8002
[ 6038.132153] amdgpu: Finished evicting pasid 0x8002
[ 6038.297531] amdgpu: Started evicting pasid 0x8002
[ 6038.297544] amdgpu: Finished evicting pasid 0x8002
[ 6038.456626] amdgpu: Started evicting pasid 0x8002
[ 6038.456641] amdgpu: Finished evicting pasid 0x8002
[ 6038.618131] amdgpu: Started evicting pasid 0x8002
[ 6038.618146] amdgpu: Finished evicting pasid 0x8002
[ 6038.780363] amdgpu: Started evicting pasid 0x8002
[ 6038.780378] amdgpu: Finished evicting pasid 0x8002
[ 6038.941223] amdgpu: Started evicting pasid 0x8002
[ 6038.941237] amdgpu: Finished evicting pasid 0x8002
[ 6039.105476] amdgpu: Started evicting pasid 0x8002
[ 6039.105491] amdgpu: Finished evicting pasid 0x8002
[ 6039.272806] amdgpu: Started evicting pasid 0x8002
[ 6039.272820] amdgpu: Finished evicting pasid 0x8002
[ 6039.438809] amdgpu: Started evicting pasid 0x8002
[ 6039.438824] amdgpu: Finished evicting pasid 0x8002
[ 6039.601375] amdgpu: Started evicting pasid 0x8002
[ 6039.601388] amdgpu: Finished evicting pasid 0x8002
[ 6039.760399] amdgpu: Started evicting pasid 0x8002
[ 6039.760414] amdgpu: Finished evicting pasid 0x8002
[ 6039.921430] amdgpu: Started evicting pasid 0x8002
[ 6039.921445] amdgpu: Finished evicting pasid 0x8002
[ 6040.082787] amdgpu: Started evicting pasid 0x8002
[ 6040.082801] amdgpu: Finished evicting pasid 0x8002
[ 6040.244429] amdgpu: Started evicting pasid 0x8002
[ 6040.244443] amdgpu: Finished evicting pasid 0x8002
[ 6040.408443] amdgpu: Started evicting pasid 0x8002
[ 6040.408458] amdgpu: Finished evicting pasid 0x8002
[ 6040.569012] amdgpu: Started evicting pasid 0x8002
[ 6040.569026] amdgpu: Finished evicting pasid 0x8002
[ 6040.733409] amdgpu: Started evicting pasid 0x8002
[ 6040.733424] amdgpu: Finished evicting pasid 0x8002
[ 6040.892545] amdgpu: Started evicting pasid 0x8002
[ 6040.892560] amdgpu: Finished evicting pasid 0x8002
[ 6041.056408] amdgpu: Started evicting pasid 0x8002
[ 6041.056423] amdgpu: Finished evicting pasid 0x8002
[ 6041.216244] amdgpu: Started evicting pasid 0x8002
[ 6041.216257] amdgpu: Finished evicting pasid 0x8002
[ 6041.383924] amdgpu: Started evicting pasid 0x8002
[ 6041.383938] amdgpu: Finished evicting pasid 0x8002
[ 6041.547589] amdgpu: Started evicting pasid 0x8002
[ 6041.547602] amdgpu: Finished evicting pasid 0x8002
[ 6042.125359] amdgpu: Started evicting pasid 0x8002
[ 6042.125374] amdgpu: Finished evicting pasid 0x8002
[ 6043.033965] amdgpu: Started evicting pasid 0x8002
[ 6043.033979] amdgpu: Finished evicting pasid 0x8002
[ 6043.259839] amdgpu: Started evicting pasid 0x8002
[ 6043.259853] amdgpu: Finished evicting pasid 0x8002
[ 6043.420726] amdgpu: Started evicting pasid 0x8002
[ 6043.420741] amdgpu: Finished evicting pasid 0x8002
[ 6043.581094] amdgpu: Started evicting pasid 0x8002
[ 6043.581108] amdgpu: Finished evicting pasid 0x8002
[ 6043.744487] amdgpu: Started evicting pasid 0x8002
[ 6043.744501] amdgpu: Finished evicting pasid 0x8002
[ 6043.903882] amdgpu: Started evicting pasid 0x8002
[ 6043.903895] amdgpu: Finished evicting pasid 0x8002
[ 6044.426265] amdgpu: Started evicting pasid 0x8002
[ 6044.426280] amdgpu: Finished evicting pasid 0x8002
[ 6046.163923] amdgpu: Started evicting pasid 0x8002
[ 6046.163937] amdgpu: Finished evicting pasid 0x8002
[ 6046.323730] amdgpu: Started evicting pasid 0x8002
[ 6046.323744] amdgpu: Finished evicting pasid 0x8002
[ 6046.492201] amdgpu: Started evicting pasid 0x8002
[ 6046.492215] amdgpu: Finished evicting pasid 0x8002
[ 6046.655473] amdgpu: Started evicting pasid 0x8002
[ 6046.655487] amdgpu: Finished evicting pasid 0x8002
[ 6046.818221] amdgpu: Started evicting pasid 0x8002
[ 6046.818235] amdgpu: Finished evicting pasid 0x8002
[ 6047.566565] amdgpu: Started evicting pasid 0x8002
[ 6047.566578] amdgpu: Finished evicting pasid 0x8002
[ 6047.728334] amdgpu: Started evicting pasid 0x8002
[ 6047.728348] amdgpu: Finished evicting pasid 0x8002
[ 6047.888410] amdgpu: Started evicting pasid 0x8002
[ 6047.888424] amdgpu: Finished evicting pasid 0x8002
[ 6048.056162] amdgpu: Started evicting pasid 0x8002
[ 6048.056177] amdgpu: Finished evicting pasid 0x8002
[ 6048.066994] amdgpu: Started evicting pasid 0x8003
[ 6048.067008] amdgpu: Finished evicting pasid 0x8003
[ 6048.241924] amdgpu: Started evicting pasid 0x8002
[ 6048.241938] amdgpu: Finished evicting pasid 0x8002
[ 6048.393713] amdgpu: Started evicting pasid 0x8002
[ 6048.393726] amdgpu: Finished evicting pasid 0x8002
[ 6048.570483] amdgpu: Started evicting pasid 0x8002
[ 6048.570498] amdgpu: Finished evicting pasid 0x8002
[ 6048.720275] amdgpu: Started evicting pasid 0x8002
[ 6048.720288] amdgpu: Finished evicting pasid 0x8002
[ 6048.884825] amdgpu: Started evicting pasid 0x8002
[ 6048.884839] amdgpu: Finished evicting pasid 0x8002
[ 6049.044699] amdgpu: Started evicting pasid 0x8002
[ 6049.044712] amdgpu: Finished evicting pasid 0x8002
[ 6049.208840] amdgpu: Started evicting pasid 0x8002
[ 6049.208854] amdgpu: Finished evicting pasid 0x8002
[ 6049.376725] amdgpu: Started evicting pasid 0x8002
[ 6049.376739] amdgpu: Finished evicting pasid 0x8002
[ 6049.540328] amdgpu: Started evicting pasid 0x8002
[ 6049.540341] amdgpu: Finished evicting pasid 0x8002
[ 6049.701964] amdgpu: Started evicting pasid 0x8002
[ 6049.701977] amdgpu: Finished evicting pasid 0x8002
[ 6049.932453] amdgpu: Started evicting pasid 0x8002
[ 6049.932467] amdgpu: Finished evicting pasid 0x8002
[ 6050.097221] amdgpu: Started evicting pasid 0x8002
[ 6050.097235] amdgpu: Finished evicting pasid 0x8002
[ 6050.266439] amdgpu: Started evicting pasid 0x8002
[ 6050.266453] amdgpu: Finished evicting pasid 0x8002
[ 6050.431244] amdgpu: Started evicting pasid 0x8002
[ 6050.431258] amdgpu: Finished evicting pasid 0x8002
[ 6050.592571] amdgpu: Started evicting pasid 0x8002
[ 6050.592586] amdgpu: Finished evicting pasid 0x8002
[ 6051.100206] amdgpu: Started evicting pasid 0x8002
[ 6051.100220] amdgpu: Finished evicting pasid 0x8002
[ 6051.261124] amdgpu: Started evicting pasid 0x8002
[ 6051.261138] amdgpu: Finished evicting pasid 0x8002
[ 6051.424341] amdgpu: Started evicting pasid 0x8002
[ 6051.424360] amdgpu: Finished evicting pasid 0x8002
[ 6051.588523] amdgpu: Started evicting pasid 0x8002
[ 6051.588539] amdgpu: Finished evicting pasid 0x8002
[ 6051.756117] amdgpu: Started evicting pasid 0x8002
[ 6051.756130] amdgpu: Finished evicting pasid 0x8002
[ 6051.929007] amdgpu: Started evicting pasid 0x8002
[ 6051.929018] amdgpu: Finished evicting pasid 0x8002
[ 6052.091749] amdgpu: Started evicting pasid 0x8002
[ 6052.091764] amdgpu: Finished evicting pasid 0x8002
[ 6052.253079] amdgpu: Started evicting pasid 0x8002
[ 6052.253093] amdgpu: Finished evicting pasid 0x8002
[ 6052.641166] show_signal_msg: 27 callbacks suppressed
[ 6052.641168] hipMemset[24672]: segfault at 0 ip 00007fb84d477cf1 sp 00007ffea5978280 error 4 in libc-2.27.so[7fb84d3e0000+1e7000]
[ 6052.641173] Code: 0d dc 35 35 00 48 89 f0 48 f7 d8 f0 48 01 05 de 35 35 00 e8 d1 3b 08 00 e9 ac fe ff ff 0f 1f 40 00 4c 89 e8 48 25 00 00 00 fc <48> 8b 18 e9 aa fd ff ff 0f 1f 80 00 00 00 00 4c 3b 2d 29 5c 35 00
[ 6052.737901] amdgpu: Started evicting pasid 0x8002
[ 6052.737972] amdgpu: Finished evicting pasid 0x8002
[ 6054.312928] amdgpu: Started evicting pasid 0x8002
[ 6054.312993] amdgpu: Finished evicting pasid 0x8002
[ 6056.669584] amdgpu: Started evicting pasid 0x8002
[ 6056.669598] amdgpu: Finished evicting pasid 0x8002
[ 6057.161996] amdgpu: Started evicting pasid 0x8002
[ 6057.162009] amdgpu: Finished evicting pasid 0x8002
[ 6060.038056] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038060] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a01000 from client 18
[ 6060.038062] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6060.038064] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038066] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6060.038067] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038069] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6060.038070] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038072] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6060.038078] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038080] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a02000 from client 18
[ 6060.038081] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6060.038083] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038084] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6060.038085] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038087] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6060.038088] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038090] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6060.038094] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038096] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a03000 from client 18
[ 6060.038097] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6060.038099] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038100] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6060.038102] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038103] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6060.038104] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038106] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6060.038110] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038111] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a04000 from client 18
[ 6060.038113] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6060.038114] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038116] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6060.038117] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038118] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6060.038120] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038121] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6060.038125] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038127] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a05000 from client 18
[ 6060.038128] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038130] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038131] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038132] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038134] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038135] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038136] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.038142] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038144] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a06000 from client 18
[ 6060.038145] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038147] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038148] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038150] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038151] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038152] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038154] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.038159] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038161] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a07000 from client 18
[ 6060.038162] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038164] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038165] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038166] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038168] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038169] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038171] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.038176] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038177] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a08000 from client 18
[ 6060.038179] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038180] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038182] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038183] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038184] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038186] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038187] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.038192] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038193] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a09000 from client 18
[ 6060.038194] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038195] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038196] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038197] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038198] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038199] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038200] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.038205] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 24864 thread hipMemsetAsyncM pid 24864)
[ 6060.038206] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f31f5a01000 from client 18
[ 6060.038207] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6060.038209] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6060.038210] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6060.038211] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6060.038212] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6060.038213] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6060.038214] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6060.125741] amdgpu: Started evicting pasid 0x8002
[ 6060.125748] amdgpu: Finished evicting pasid 0x8002
[ 6060.656735] amdgpu: Started evicting pasid 0x8002
[ 6060.656754] amdgpu: Finished evicting pasid 0x8002
[ 6060.819504] amdgpu: Started evicting pasid 0x8002
[ 6060.819518] amdgpu: Finished evicting pasid 0x8002
[ 6061.628225] amdgpu: Started evicting pasid 0x8002
[ 6061.628239] amdgpu: Finished evicting pasid 0x8002
[ 6061.797852] amdgpu: Started evicting pasid 0x8002
[ 6061.797866] amdgpu: Finished evicting pasid 0x8002
[ 6061.961975] amdgpu: Started evicting pasid 0x8002
[ 6061.961989] amdgpu: Finished evicting pasid 0x8002
[ 6062.199835] amdgpu: Started evicting pasid 0x8002
[ 6062.199848] amdgpu: Finished evicting pasid 0x8002
[ 6062.596928] amdgpu: Started evicting pasid 0x8002

---

### 评论 #6 — dshm (2021-03-02T07:42:41Z)

[ 6062.596996] amdgpu: Finished evicting pasid 0x8002
[ 6063.005662] amdgpu: Started evicting pasid 0x8002
[ 6063.005717] amdgpu: Finished evicting pasid 0x8002
[ 6063.409382] amdgpu: Started evicting pasid 0x8002
[ 6063.409437] amdgpu: Finished evicting pasid 0x8002
[ 6063.828042] amdgpu: Started evicting pasid 0x8002
[ 6063.828099] amdgpu: Finished evicting pasid 0x8002
[ 6064.297588] amdgpu: Started evicting pasid 0x8002
[ 6064.297638] amdgpu: Finished evicting pasid 0x8002
[ 6064.763029] amdgpu: Started evicting pasid 0x8002
[ 6064.763084] amdgpu: Finished evicting pasid 0x8002
[ 6065.228331] amdgpu: Started evicting pasid 0x8002
[ 6065.228384] amdgpu: Finished evicting pasid 0x8002
[ 6065.405478] amdgpu: Started evicting pasid 0x8002
[ 6065.405499] amdgpu: Finished evicting pasid 0x8002
[ 6065.574319] amdgpu: Started evicting pasid 0x8002
[ 6065.574333] amdgpu: Finished evicting pasid 0x8002
[ 6065.735433] amdgpu: Started evicting pasid 0x8002
[ 6065.735447] amdgpu: Finished evicting pasid 0x8002
[ 6066.295448] amdgpu: Started evicting pasid 0x8002
[ 6066.295463] amdgpu: Finished evicting pasid 0x8002
[ 6066.460450] amdgpu: Started evicting pasid 0x8002
[ 6066.460464] amdgpu: Finished evicting pasid 0x8002
[ 6066.629307] amdgpu: Started evicting pasid 0x8002
[ 6066.629321] amdgpu: Finished evicting pasid 0x8002
[ 6066.795036] amdgpu: Started evicting pasid 0x8002
[ 6066.795050] amdgpu: Finished evicting pasid 0x8002
[ 6066.955563] amdgpu: Started evicting pasid 0x8002
[ 6066.955576] amdgpu: Finished evicting pasid 0x8002
[ 6067.118124] amdgpu: Started evicting pasid 0x8002
[ 6067.118138] amdgpu: Finished evicting pasid 0x8002
[ 6067.354777] amdgpu: Started evicting pasid 0x8002
[ 6067.354790] amdgpu: Finished evicting pasid 0x8002
[ 6067.512410] amdgpu: Started evicting pasid 0x8002
[ 6067.512424] amdgpu: Finished evicting pasid 0x8002
[ 6102.776745] amdgpu: Started evicting pasid 0x8002
[ 6102.776758] amdgpu: Finished evicting pasid 0x8002
[ 6102.946313] amdgpu: Started evicting pasid 0x8002
[ 6102.946326] amdgpu: Finished evicting pasid 0x8002
[ 6103.109419] amdgpu: Started evicting pasid 0x8002
[ 6103.109432] amdgpu: Finished evicting pasid 0x8002
[ 6103.271342] amdgpu: Started evicting pasid 0x8002
[ 6103.271356] amdgpu: Finished evicting pasid 0x8002
[ 6103.433039] amdgpu: Started evicting pasid 0x8002
[ 6103.433053] amdgpu: Finished evicting pasid 0x8002
[ 6103.594253] amdgpu: Started evicting pasid 0x8002
[ 6103.594268] amdgpu: Finished evicting pasid 0x8002
[ 6103.755421] amdgpu: Started evicting pasid 0x8002
[ 6103.755435] amdgpu: Finished evicting pasid 0x8002
[ 6103.918057] amdgpu: Started evicting pasid 0x8002
[ 6103.918071] amdgpu: Finished evicting pasid 0x8002
[ 6114.662451] amdgpu: Started evicting pasid 0x8002
[ 6114.662466] amdgpu: Finished evicting pasid 0x8002
[ 6114.823884] amdgpu: Started evicting pasid 0x8002
[ 6114.823898] amdgpu: Finished evicting pasid 0x8002
[ 6114.995813] amdgpu: Started evicting pasid 0x8002
[ 6114.995828] amdgpu: Finished evicting pasid 0x8002
[ 6115.162324] amdgpu: Started evicting pasid 0x8002
[ 6115.162340] amdgpu: Finished evicting pasid 0x8002
[ 6115.328431] amdgpu: Started evicting pasid 0x8002
[ 6115.328444] amdgpu: Finished evicting pasid 0x8002
[ 6115.491532] amdgpu: Started evicting pasid 0x8002
[ 6115.491546] amdgpu: Finished evicting pasid 0x8002
[ 6121.310845] amdgpu: Started evicting pasid 0x8002
[ 6121.310859] amdgpu: Finished evicting pasid 0x8002
[ 6122.976665] amdgpu: Started evicting pasid 0x8002
[ 6122.976679] amdgpu: Finished evicting pasid 0x8002
[ 6123.141387] amdgpu: Started evicting pasid 0x8002
[ 6123.141401] amdgpu: Finished evicting pasid 0x8002
[ 6123.300606] amdgpu: Started evicting pasid 0x8002
[ 6123.300620] amdgpu: Finished evicting pasid 0x8002
[ 6123.464697] amdgpu: Started evicting pasid 0x8002
[ 6123.464711] amdgpu: Finished evicting pasid 0x8002
[ 6123.928878] amdgpu: Started evicting pasid 0x8002
[ 6123.928891] amdgpu: Finished evicting pasid 0x8002
[ 6124.095988] amdgpu: Started evicting pasid 0x8002
[ 6124.096001] amdgpu: Finished evicting pasid 0x8002
[ 6195.677293] amdgpu: Started evicting pasid 0x8002
[ 6195.677305] amdgpu: Finished evicting pasid 0x8002
[ 6195.779611] amdgpu: Started restoring pasid 0x8002
[ 6195.779634] amdgpu: Finished restoring pasid 0x8002
[ 6195.824918] amdgpu: Started evicting pasid 0x8002
[ 6195.824931] amdgpu: Finished evicting pasid 0x8002
[ 6196.055711] amdgpu: Started evicting pasid 0x8002
[ 6196.055730] amdgpu: Finished evicting pasid 0x8002
[ 6197.754925] amdgpu: Started evicting pasid 0x8002
[ 6197.754939] amdgpu: Finished evicting pasid 0x8002
[ 6199.578105] amdgpu: Started evicting pasid 0x8002
[ 6199.578119] amdgpu: Finished evicting pasid 0x8002
[ 6199.747198] amdgpu: Started evicting pasid 0x8002
[ 6199.747214] amdgpu: Finished evicting pasid 0x8002
[ 6199.919800] amdgpu: Started evicting pasid 0x8002
[ 6199.919817] amdgpu: Finished evicting pasid 0x8002
[ 6200.090945] amdgpu: Started evicting pasid 0x8002
[ 6200.090960] amdgpu: Finished evicting pasid 0x8002
[ 6200.281741] amdgpu: Started evicting pasid 0x8002
[ 6200.281758] amdgpu: Finished evicting pasid 0x8002
[ 6200.449288] amdgpu: Started evicting pasid 0x8002
[ 6200.449303] amdgpu: Finished evicting pasid 0x8002
[ 6200.616535] amdgpu: Started evicting pasid 0x8002
[ 6200.616550] amdgpu: Finished evicting pasid 0x8002
[ 6200.784845] amdgpu: Started evicting pasid 0x8002
[ 6200.784860] amdgpu: Finished evicting pasid 0x8002
[ 6200.949445] amdgpu: Started evicting pasid 0x8002
[ 6200.949460] amdgpu: Finished evicting pasid 0x8002
[ 6201.113515] amdgpu: Started evicting pasid 0x8002
[ 6201.113530] amdgpu: Finished evicting pasid 0x8002
[ 6201.279989] amdgpu: Started evicting pasid 0x8002
[ 6201.280003] amdgpu: Finished evicting pasid 0x8002
[ 6201.444795] amdgpu: Started evicting pasid 0x8002
[ 6201.444809] amdgpu: Finished evicting pasid 0x8002
[ 6201.611590] amdgpu: Started evicting pasid 0x8002
[ 6201.611606] amdgpu: Finished evicting pasid 0x8002
[ 6201.804992] amdgpu: Started evicting pasid 0x8002
[ 6201.805007] amdgpu: Finished evicting pasid 0x8002
[ 6201.968251] amdgpu: Started evicting pasid 0x8002
[ 6201.968266] amdgpu: Finished evicting pasid 0x8002
[ 6202.132098] amdgpu: Started evicting pasid 0x8002
[ 6202.132113] amdgpu: Finished evicting pasid 0x8002
[ 6202.298838] amdgpu: Started evicting pasid 0x8002
[ 6202.298853] amdgpu: Finished evicting pasid 0x8002
[ 6202.463720] amdgpu: Started evicting pasid 0x8002
[ 6202.463735] amdgpu: Finished evicting pasid 0x8002
[ 6202.628600] amdgpu: Started evicting pasid 0x8002
[ 6202.628614] amdgpu: Finished evicting pasid 0x8002
[ 6202.794344] amdgpu: Started evicting pasid 0x8002
[ 6202.794359] amdgpu: Finished evicting pasid 0x8002
[ 6202.956824] amdgpu: Started evicting pasid 0x8002
[ 6202.956839] amdgpu: Finished evicting pasid 0x8002
[ 6203.119787] amdgpu: Started evicting pasid 0x8002
[ 6203.119802] amdgpu: Finished evicting pasid 0x8002
[ 6203.282485] amdgpu: Started evicting pasid 0x8002
[ 6203.282499] amdgpu: Finished evicting pasid 0x8002
[ 6203.443948] amdgpu: Started evicting pasid 0x8002
[ 6203.443961] amdgpu: Finished evicting pasid 0x8002
[ 6203.609379] amdgpu: Started evicting pasid 0x8002
[ 6203.609395] amdgpu: Finished evicting pasid 0x8002
[ 6203.773632] amdgpu: Started evicting pasid 0x8002
[ 6203.773646] amdgpu: Finished evicting pasid 0x8002
[ 6203.938952] amdgpu: Started evicting pasid 0x8002
[ 6203.938967] amdgpu: Finished evicting pasid 0x8002
[ 6204.103174] amdgpu: Started evicting pasid 0x8002
[ 6204.103188] amdgpu: Finished evicting pasid 0x8002
[ 6204.288289] amdgpu: Started evicting pasid 0x8002
[ 6204.288304] amdgpu: Finished evicting pasid 0x8002
[ 6204.480378] amdgpu: Started evicting pasid 0x8002
[ 6204.480393] amdgpu: Finished evicting pasid 0x8002
[ 6204.646733] amdgpu: Started evicting pasid 0x8002
[ 6204.646758] amdgpu: Finished evicting pasid 0x8002
[ 6204.811229] amdgpu: Started evicting pasid 0x8002
[ 6204.811245] amdgpu: Finished evicting pasid 0x8002
[ 6204.977209] amdgpu: Started evicting pasid 0x8002
[ 6204.977224] amdgpu: Finished evicting pasid 0x8002
[ 6205.141144] amdgpu: Started evicting pasid 0x8002
[ 6205.141159] amdgpu: Finished evicting pasid 0x8002
[ 6205.303112] amdgpu: Started evicting pasid 0x8002
[ 6205.303127] amdgpu: Finished evicting pasid 0x8002
[ 6205.466750] amdgpu: Started evicting pasid 0x8002
[ 6205.466766] amdgpu: Finished evicting pasid 0x8002
[ 6205.631978] amdgpu: Started evicting pasid 0x8002
[ 6205.631992] amdgpu: Finished evicting pasid 0x8002
[ 6205.799476] amdgpu: Started evicting pasid 0x8002
[ 6205.799493] amdgpu: Finished evicting pasid 0x8002
[ 6205.964575] amdgpu: Started evicting pasid 0x8002
[ 6205.964589] amdgpu: Finished evicting pasid 0x8002
[ 6206.130409] amdgpu: Started evicting pasid 0x8002
[ 6206.130422] amdgpu: Finished evicting pasid 0x8002
[ 6206.294677] amdgpu: Started evicting pasid 0x8002
[ 6206.294692] amdgpu: Finished evicting pasid 0x8002
[ 6206.460428] amdgpu: Started evicting pasid 0x8002
[ 6206.460443] amdgpu: Finished evicting pasid 0x8002
[ 6206.627210] amdgpu: Started evicting pasid 0x8002
[ 6206.627225] amdgpu: Finished evicting pasid 0x8002
[ 6206.792029] amdgpu: Started evicting pasid 0x8002
[ 6206.792043] amdgpu: Finished evicting pasid 0x8002
[ 6206.955916] amdgpu: Started evicting pasid 0x8002
[ 6206.955930] amdgpu: Finished evicting pasid 0x8002
[ 6207.121076] amdgpu: Started evicting pasid 0x8002
[ 6207.121090] amdgpu: Finished evicting pasid 0x8002
[ 6207.669750] amdgpu: Started evicting pasid 0x8002
[ 6207.669766] amdgpu: Finished evicting pasid 0x8002
[ 6207.834409] amdgpu: Started evicting pasid 0x8002
[ 6207.834451] amdgpu: Finished evicting pasid 0x8002
[ 6208.004657] amdgpu: Started evicting pasid 0x8002
[ 6208.004672] amdgpu: Finished evicting pasid 0x8002
[ 6208.168637] amdgpu: Started evicting pasid 0x8002
[ 6208.168652] amdgpu: Finished evicting pasid 0x8002
[ 6208.333197] amdgpu: Started evicting pasid 0x8002
[ 6208.333212] amdgpu: Finished evicting pasid 0x8002
[ 6208.500125] amdgpu: Started evicting pasid 0x8002
[ 6208.500140] amdgpu: Finished evicting pasid 0x8002
[ 6208.664642] amdgpu: Started evicting pasid 0x8002
[ 6208.664656] amdgpu: Finished evicting pasid 0x8002
[ 6208.830482] amdgpu: Started evicting pasid 0x8002
[ 6208.830497] amdgpu: Finished evicting pasid 0x8002
[ 6208.998503] amdgpu: Started evicting pasid 0x8002
[ 6208.998519] amdgpu: Finished evicting pasid 0x8002
[ 6209.170650] amdgpu: Started evicting pasid 0x8002
[ 6209.170665] amdgpu: Finished evicting pasid 0x8002
[ 6209.341422] amdgpu: Started evicting pasid 0x8002
[ 6209.341436] amdgpu: Finished evicting pasid 0x8002
[ 6209.505256] amdgpu: Started evicting pasid 0x8002
[ 6209.505272] amdgpu: Finished evicting pasid 0x8002
[ 6209.670691] amdgpu: Started evicting pasid 0x8002
[ 6209.670706] amdgpu: Finished evicting pasid 0x8002
[ 6209.839084] amdgpu: Started evicting pasid 0x8002
[ 6209.839099] amdgpu: Finished evicting pasid 0x8002
[ 6210.010155] amdgpu: Started evicting pasid 0x8002
[ 6210.010170] amdgpu: Finished evicting pasid 0x8002
[ 6210.182928] amdgpu: Started evicting pasid 0x8002
[ 6210.182945] amdgpu: Finished evicting pasid 0x8002
[ 6210.354019] amdgpu: Started evicting pasid 0x8002
[ 6210.354034] amdgpu: Finished evicting pasid 0x8002
[ 6210.518304] amdgpu: Started evicting pasid 0x8002
[ 6210.518319] amdgpu: Finished evicting pasid 0x8002
[ 6210.687389] amdgpu: Started evicting pasid 0x8002
[ 6210.687405] amdgpu: Finished evicting pasid 0x8002
[ 6210.853082] amdgpu: Started evicting pasid 0x8002
[ 6210.853097] amdgpu: Finished evicting pasid 0x8002
[ 6211.020943] amdgpu: Started evicting pasid 0x8002
[ 6211.020959] amdgpu: Finished evicting pasid 0x8002
[ 6211.186394] amdgpu: Started evicting pasid 0x8002
[ 6211.186409] amdgpu: Finished evicting pasid 0x8002
[ 6211.357477] amdgpu: Started evicting pasid 0x8002
[ 6211.357493] amdgpu: Finished evicting pasid 0x8002
[ 6211.524614] amdgpu: Started evicting pasid 0x8002
[ 6211.524628] amdgpu: Finished evicting pasid 0x8002
[ 6211.690565] amdgpu: Started evicting pasid 0x8002
[ 6211.690579] amdgpu: Finished evicting pasid 0x8002
[ 6211.861573] amdgpu: Started evicting pasid 0x8002
[ 6211.861589] amdgpu: Finished evicting pasid 0x8002
[ 6212.025844] amdgpu: Started evicting pasid 0x8002
[ 6212.025859] amdgpu: Finished evicting pasid 0x8002
[ 6212.193282] amdgpu: Started evicting pasid 0x8002
[ 6212.193296] amdgpu: Finished evicting pasid 0x8002
[ 6212.356853] amdgpu: Started evicting pasid 0x8002
[ 6212.356868] amdgpu: Finished evicting pasid 0x8002
[ 6212.518999] amdgpu: Started evicting pasid 0x8002
[ 6212.519013] amdgpu: Finished evicting pasid 0x8002
[ 6212.685811] amdgpu: Started evicting pasid 0x8002
[ 6212.685825] amdgpu: Finished evicting pasid 0x8002
[ 6212.852811] amdgpu: Started evicting pasid 0x8002
[ 6212.852827] amdgpu: Finished evicting pasid 0x8002
[ 6213.015882] amdgpu: Started evicting pasid 0x8002
[ 6213.015897] amdgpu: Finished evicting pasid 0x8002
[ 6213.181761] amdgpu: Started evicting pasid 0x8002
[ 6213.181776] amdgpu: Finished evicting pasid 0x8002
[ 6213.348380] amdgpu: Started evicting pasid 0x8002
[ 6213.348395] amdgpu: Finished evicting pasid 0x8002
[ 6213.930475] amdgpu: Started evicting pasid 0x8002
[ 6213.930491] amdgpu: Finished evicting pasid 0x8002
[ 6214.865337] amdgpu: Started evicting pasid 0x8002
[ 6214.865352] amdgpu: Finished evicting pasid 0x8002
[ 6215.087865] amdgpu: Started evicting pasid 0x8002
[ 6215.087880] amdgpu: Finished evicting pasid 0x8002
[ 6215.252695] amdgpu: Started evicting pasid 0x8002
[ 6215.252711] amdgpu: Finished evicting pasid 0x8002
[ 6215.421795] amdgpu: Started evicting pasid 0x8002
[ 6215.421810] amdgpu: Finished evicting pasid 0x8002
[ 6215.593852] amdgpu: Started evicting pasid 0x8002
[ 6215.593868] amdgpu: Finished evicting pasid 0x8002
[ 6215.764437] amdgpu: Started evicting pasid 0x8002
[ 6215.764452] amdgpu: Finished evicting pasid 0x8002
[ 6216.290276] amdgpu: Started evicting pasid 0x8002
[ 6216.290290] amdgpu: Finished evicting pasid 0x8002
[ 6218.015597] amdgpu: Started evicting pasid 0x8002
[ 6218.015610] amdgpu: Finished evicting pasid 0x8002
[ 6218.177525] amdgpu: Started evicting pasid 0x8002
[ 6218.177540] amdgpu: Finished evicting pasid 0x8002
[ 6218.341812] amdgpu: Started evicting pasid 0x8002
[ 6218.341826] amdgpu: Finished evicting pasid 0x8002
[ 6218.504954] amdgpu: Started evicting pasid 0x8002
[ 6218.504968] amdgpu: Finished evicting pasid 0x8002
[ 6218.667702] amdgpu: Started evicting pasid 0x8002
[ 6218.667715] amdgpu: Finished evicting pasid 0x8002
[ 6219.407653] amdgpu: Started evicting pasid 0x8002
[ 6219.407667] amdgpu: Finished evicting pasid 0x8002
[ 6219.569399] amdgpu: Started evicting pasid 0x8002
[ 6219.569412] amdgpu: Finished evicting pasid 0x8002
[ 6219.733837] amdgpu: Started evicting pasid 0x8002
[ 6219.733851] amdgpu: Finished evicting pasid 0x8002
[ 6219.904271] amdgpu: Started evicting pasid 0x8002
[ 6219.904285] amdgpu: Finished evicting pasid 0x8002
[ 6219.914090] amdgpu: Started evicting pasid 0x8003
[ 6219.914105] amdgpu: Finished evicting pasid 0x8003
[ 6220.086555] amdgpu: Started evicting pasid 0x8002
[ 6220.086569] amdgpu: Finished evicting pasid 0x8002
[ 6220.224689] amdgpu: Started evicting pasid 0x8002
[ 6220.224703] amdgpu: Finished evicting pasid 0x8002
[ 6220.395002] amdgpu: Started evicting pasid 0x8002
[ 6220.395016] amdgpu: Finished evicting pasid 0x8002
[ 6220.537377] amdgpu: Started evicting pasid 0x8002
[ 6220.537391] amdgpu: Finished evicting pasid 0x8002
[ 6220.699489] amdgpu: Started evicting pasid 0x8002
[ 6220.699503] amdgpu: Finished evicting pasid 0x8002
[ 6220.859968] amdgpu: Started evicting pasid 0x8002
[ 6220.859983] amdgpu: Finished evicting pasid 0x8002
[ 6221.021933] amdgpu: Started evicting pasid 0x8002
[ 6221.021948] amdgpu: Finished evicting pasid 0x8002
[ 6221.184203] amdgpu: Started evicting pasid 0x8002
[ 6221.184217] amdgpu: Finished evicting pasid 0x8002
[ 6221.345637] amdgpu: Started evicting pasid 0x8002
[ 6221.345652] amdgpu: Finished evicting pasid 0x8002
[ 6221.508308] amdgpu: Started evicting pasid 0x8002
[ 6221.508322] amdgpu: Finished evicting pasid 0x8002
[ 6221.737979] amdgpu: Started evicting pasid 0x8002
[ 6221.737994] amdgpu: Finished evicting pasid 0x8002
[ 6221.904331] amdgpu: Started evicting pasid 0x8002
[ 6221.904346] amdgpu: Finished evicting pasid 0x8002
[ 6222.065814] amdgpu: Started evicting pasid 0x8002
[ 6222.065828] amdgpu: Finished evicting pasid 0x8002
[ 6222.226465] amdgpu: Started evicting pasid 0x8002
[ 6222.226480] amdgpu: Finished evicting pasid 0x8002
[ 6222.387741] amdgpu: Started evicting pasid 0x8002
[ 6222.387755] amdgpu: Finished evicting pasid 0x8002
[ 6222.894520] amdgpu: Started evicting pasid 0x8002
[ 6222.894535] amdgpu: Finished evicting pasid 0x8002
[ 6223.056057] amdgpu: Started evicting pasid 0x8002
[ 6223.056071] amdgpu: Finished evicting pasid 0x8002
[ 6223.217331] amdgpu: Started evicting pasid 0x8002
[ 6223.217346] amdgpu: Finished evicting pasid 0x8002
[ 6223.380908] amdgpu: Started evicting pasid 0x8002
[ 6223.380923] amdgpu: Finished evicting pasid 0x8002
[ 6223.542786] amdgpu: Started evicting pasid 0x8002
[ 6223.542800] amdgpu: Finished evicting pasid 0x8002
[ 6223.715400] amdgpu: Started evicting pasid 0x8002
[ 6223.715412] amdgpu: Finished evicting pasid 0x8002
[ 6223.877062] amdgpu: Started evicting pasid 0x8002
[ 6223.877077] amdgpu: Finished evicting pasid 0x8002
[ 6224.038556] amdgpu: Started evicting pasid 0x8002
[ 6224.038570] amdgpu: Finished evicting pasid 0x8002
[ 6224.504740] amdgpu: Started evicting pasid 0x8002
[ 6224.504807] amdgpu: Finished evicting pasid 0x8002
[ 6226.079688] amdgpu: Started evicting pasid 0x8002
[ 6226.079755] amdgpu: Finished evicting pasid 0x8002
[ 6228.438768] amdgpu: Started evicting pasid 0x8002
[ 6228.438782] amdgpu: Finished evicting pasid 0x8002
[ 6228.929463] amdgpu: Started evicting pasid 0x8002
[ 6228.929491] amdgpu: Finished evicting pasid 0x8002
[ 6229.684463] gmc_v9_0_process_interrupt: 26 callbacks suppressed
[ 6229.684471] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684478] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0200000 from client 18
[ 6229.684481] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6229.684484] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684487] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6229.684489] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684492] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6229.684495] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684497] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6229.684507] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684511] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0201000 from client 18
[ 6229.684513] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6229.684516] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684518] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6229.684521] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684524] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6229.684526] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684528] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6229.684535] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684538] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0202000 from client 18
[ 6229.684541] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6229.684543] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684546] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6229.684548] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684551] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6229.684553] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684556] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6229.684562] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684565] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0203000 from client 18
[ 6229.684567] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6229.684570] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684572] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6229.684575] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684577] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6229.684580] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684582] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6229.684590] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684593] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0204000 from client 18
[ 6229.684595] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684597] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684600] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684602] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684604] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684606] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684609] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.684617] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684620] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0205000 from client 18
[ 6229.684623] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684625] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684627] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684629] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684631] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684633] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684635] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.684642] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684644] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0206000 from client 18
[ 6229.684646] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684648] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684649] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684651] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684653] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684655] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684657] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.684666] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684668] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0207000 from client 18
[ 6229.684670] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684672] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684674] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684676] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684678] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684679] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684681] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.684686] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684689] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0208000 from client 18
[ 6229.684692] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684694] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684696] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684699] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684701] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684703] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684705] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.684712] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 37168 thread hipMemsetAsyncM pid 37168)
[ 6229.684714] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe5d0200000 from client 18
[ 6229.684716] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6229.684718] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6229.684719] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6229.684721] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6229.684722] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6229.684723] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6229.684725] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6229.775947] amdgpu: Started evicting pasid 0x8002
[ 6229.775958] amdgpu: Finished evicting pasid 0x8002
[ 6230.262793] amdgpu: Started evicting pasid 0x8002
[ 6230.262806] amdgpu: Finished evicting pasid 0x8002
[ 6230.422721] amdgpu: Started evicting pasid 0x8002
[ 6230.422736] amdgpu: Finished evicting pasid 0x8002
[ 6231.237730] amdgpu: Started evicting pasid 0x8002
[ 6231.237744] amdgpu: Finished evicting pasid 0x8002
[ 6231.399213] amdgpu: Started evicting pasid 0x8002
[ 6231.399227] amdgpu: Finished evicting pasid 0x8002
[ 6231.557589] amdgpu: Started evicting pasid 0x8002
[ 6231.557603] amdgpu: Finished evicting pasid 0x8002
[ 6231.781512] amdgpu: Started evicting pasid 0x8002
[ 6231.781526] amdgpu: Finished evicting pasid 0x8002
[ 6232.179776] amdgpu: Started evicting pasid 0x8002
[ 6232.179833] amdgpu: Finished evicting pasid 0x8002
[ 6232.589046] amdgpu: Started evicting pasid 0x8002
[ 6232.589106] amdgpu: Finished evicting pasid 0x8002
[ 6232.997292] amdgpu: Started evicting pasid 0x8002
[ 6232.997354] amdgpu: Finished evicting pasid 0x8002
[ 6233.515346] amdgpu: Started evicting pasid 0x8002
[ 6233.515402] amdgpu: Finished evicting pasid 0x8002
[ 6233.985009] amdgpu: Started evicting pasid 0x8002
[ 6233.985062] amdgpu: Finished evicting pasid 0x8002
[ 6234.447291] amdgpu: Started evicting pasid 0x8002
[ 6234.447344] amdgpu: Finished evicting pasid 0x8002
[ 6234.906494] amdgpu: Started evicting pasid 0x8002
[ 6234.906546] amdgpu: Finished evicting pasid 0x8002
[ 6235.080661] amdgpu: Started evicting pasid 0x8002
[ 6235.080676] amdgpu: Finished evicting pasid 0x8002
[ 6235.241337] amdgpu: Started evicting pasid 0x8002
[ 6235.241351] amdgpu: Finished evicting pasid 0x8002
[ 6235.401607] amdgpu: Started evicting pasid 0x8002
[ 6235.401621] amdgpu: Finished evicting pasid 0x8002
[ 6235.956835] amdgpu: Started evicting pasid 0x8002
[ 6235.956850] amdgpu: Finished evicting pasid 0x8002
[ 6236.120241] amdgpu: Started evicting pasid 0x8002
[ 6236.120255] amdgpu: Finished evicting pasid 0x8002
[ 6236.283597] amdgpu: Started evicting pasid 0x8002
[ 6236.283611] amdgpu: Finished evicting pasid 0x8002
[ 6236.442402] amdgpu: Started evicting pasid 0x8002
[ 6236.442416] amdgpu: Finished evicting pasid 0x8002
[ 6236.601518] amdgpu: Started evicting pasid 0x8002
[ 6236.601533] amdgpu: Finished evicting pasid 0x8002
[ 6236.760258] amdgpu: Started evicting pasid 0x8002
[ 6236.760273] amdgpu: Finished evicting pasid 0x8002
[ 6236.985364] amdgpu: Started evicting pasid 0x8002
[ 6236.985379] amdgpu: Finished evicting pasid 0x8002
[ 6237.144778] amdgpu: Started evicting pasid 0x8002
[ 6237.144791] amdgpu: Finished evicting pasid 0x8002
[ 6272.248417] amdgpu: Started evicting pasid 0x8002
[ 6272.248432] amdgpu: Finished evicting pasid 0x8002
[ 6272.412421] amdgpu: Started evicting pasid 0x8002
[ 6272.412436] amdgpu: Finished evicting pasid 0x8002
[ 6272.577156] amdgpu: Started evicting pasid 0x8002
[ 6272.577171] amdgpu: Finished evicting pasid 0x8002
[ 6272.742151] amdgpu: Started evicting pasid 0x8002
[ 6272.742165] amdgpu: Finished evicting pasid 0x8002
[ 6272.906861] amdgpu: Started evicting pasid 0x8002
[ 6272.906882] amdgpu: Finished evicting pasid 0x8002
[ 6273.073235] amdgpu: Started evicting pasid 0x8002
[ 6273.073249] amdgpu: Finished evicting pasid 0x8002
[ 6273.236873] amdgpu: Started evicting pasid 0x8002
[ 6273.236888] amdgpu: Finished evicting pasid 0x8002
[ 6273.405067] amdgpu: Started evicting pasid 0x8002
[ 6273.405082] amdgpu: Finished evicting pasid 0x8002
[ 6284.166232] amdgpu: Started evicting pasid 0x8002
[ 6284.166246] amdgpu: Finished evicting pasid 0x8002
[ 6284.338301] amdgpu: Started evicting pasid 0x8002
[ 6284.338316] amdgpu: Finished evicting pasid 0x8002
[ 6284.508833] amdgpu: Started evicting pasid 0x8002
[ 6284.508848] amdgpu: Finished evicting pasid 0x8002
[ 6284.681328] amdgpu: Started evicting pasid 0x8002
[ 6284.681342] amdgpu: Finished evicting pasid 0x8002
[ 6284.856582] amdgpu: Started evicting pasid 0x8002
[ 6284.856598] amdgpu: Finished evicting pasid 0x8002
[ 6285.026499] amdgpu: Started evicting pasid 0x8002
[ 6285.026514] amdgpu: Finished evicting pasid 0x8002
[ 6290.853123] amdgpu: Started evicting pasid 0x8002
[ 6290.853136] amdgpu: Finished evicting pasid 0x8002
[ 6292.519293] amdgpu: Started evicting pasid 0x8002
[ 6292.519308] amdgpu: Finished evicting pasid 0x8002
[ 6292.693012] amdgpu: Started evicting pasid 0x8002
[ 6292.693027] amdgpu: Finished evicting pasid 0x8002
[ 6292.852410] amdgpu: Started evicting pasid 0x8002
[ 6292.852424] amdgpu: Finished evicting pasid 0x8002
[ 6293.013745] amdgpu: Started evicting pasid 0x8002
[ 6293.013759] amdgpu: Finished evicting pasid 0x8002
[ 6293.479837] amdgpu: Started evicting pasid 0x8002
[ 6293.479852] amdgpu: Finished evicting pasid 0x8002
[ 6293.640350] amdgpu: Started evicting pasid 0x8002
[ 6293.640364] amdgpu: Finished evicting pasid 0x8002
[ 6329.228501] amdgpu: Started evicting pasid 0x8002
[ 6329.228511] amdgpu: Finished evicting pasid 0x8002
[ 6329.331649] amdgpu: Started restoring pasid 0x8002
[ 6329.331663] amdgpu: Finished restoring pasid 0x8002
[ 6329.381013] amdgpu: Started evicting pasid 0x8002
[ 6329.381024] amdgpu: Finished evicting pasid 0x8002
[ 6329.606290] amdgpu: Started evicting pasid 0x8002
[ 6329.606303] amdgpu: Finished evicting pasid 0x8002
[ 6331.241493] amdgpu: Started evicting pasid 0x8002
[ 6331.241507] amdgpu: Finished evicting pasid 0x8002
[ 6333.013264] amdgpu: Started evicting pasid 0x8002
[ 6333.013278] amdgpu: Finished evicting pasid 0x8002
[ 6333.176866] amdgpu: Started evicting pasid 0x8002
[ 6333.176881] amdgpu: Finished evicting pasid 0x8002
[ 6333.341183] amdgpu: Started evicting pasid 0x8002
[ 6333.341197] amdgpu: Finished evicting pasid 0x8002
[ 6333.504983] amdgpu: Started evicting pasid 0x8002
[ 6333.504998] amdgpu: Finished evicting pasid 0x8002
[ 6333.698638] amdgpu: Started evicting pasid 0x8002
[ 6333.698652] amdgpu: Finished evicting pasid 0x8002
[ 6333.865748] amdgpu: Started evicting pasid 0x8002
[ 6333.865762] amdgpu: Finished evicting pasid 0x8002
[ 6334.028912] amdgpu: Started evicting pasid 0x8002
[ 6334.028925] amdgpu: Finished evicting pasid 0x8002
[ 6334.196461] amdgpu: Started evicting pasid 0x8002
[ 6334.196483] amdgpu: Finished evicting pasid 0x8002
[ 6334.360633] amdgpu: Started evicting pasid 0x8002
[ 6334.360648] amdgpu: Finished evicting pasid 0x8002
[ 6334.526698] amdgpu: Started evicting pasid 0x8002
[ 6334.526712] amdgpu: Finished evicting pasid 0x8002
[ 6334.684863] amdgpu: Started evicting pasid 0x8002
[ 6334.684878] amdgpu: Finished evicting pasid 0x8002
[ 6334.845931] amdgpu: Started evicting pasid 0x8002
[ 6334.845945] amdgpu: Finished evicting pasid 0x8002
[ 6335.011544] amdgpu: Started evicting pasid 0x8002
[ 6335.011556] amdgpu: Finished evicting pasid 0x8002
[ 6335.194153] amdgpu: Started evicting pasid 0x8002
[ 6335.194167] amdgpu: Finished evicting pasid 0x8002
[ 6335.361729] amdgpu: Started evicting pasid 0x8002
[ 6335.361742] amdgpu: Finished evicting pasid 0x8002
[ 6335.522904] amdgpu: Started evicting pasid 0x8002
[ 6335.522919] amdgpu: Finished evicting pasid 0x8002
[ 6335.685448] amdgpu: Started evicting pasid 0x8002
[ 6335.685461] amdgpu: Finished evicting pasid 0x8002
[ 6335.846001] amdgpu: Started evicting pasid 0x8002
[ 6335.846015] amdgpu: Finished evicting pasid 0x8002
[ 6336.008913] amdgpu: Started evicting pasid 0x8002
[ 6336.008928] amdgpu: Finished evicting pasid 0x8002
[ 6336.178242] amdgpu: Started evicting pasid 0x8002
[ 6336.178256] amdgpu: Finished evicting pasid 0x8002
[ 6336.341515] amdgpu: Started evicting pasid 0x8002
[ 6336.341529] amdgpu: Finished evicting pasid 0x8002
[ 6336.502065] amdgpu: Started evicting pasid 0x8002
[ 6336.502079] amdgpu: Finished evicting pasid 0x8002
[ 6336.665588] amdgpu: Started evicting pasid 0x8002
[ 6336.665601] amdgpu: Finished evicting pasid 0x8002
[ 6336.825415] amdgpu: Started evicting pasid 0x8002
[ 6336.825428] amdgpu: Finished evicting pasid 0x8002
[ 6336.990223] amdgpu: Started evicting pasid 0x8002
[ 6336.990236] amdgpu: Finished evicting pasid 0x8002
[ 6337.160245] amdgpu: Started evicting pasid 0x8002
[ 6337.160259] amdgpu: Finished evicting pasid 0x8002
[ 6337.328016] amdgpu: Started evicting pasid 0x8002
[ 6337.328029] amdgpu: Finished evicting pasid 0x8002
[ 6337.492565] amdgpu: Started evicting pasid 0x8002
[ 6337.492579] amdgpu: Finished evicting pasid 0x8002
[ 6337.683319] amdgpu: Started evicting pasid 0x8002
[ 6337.683333] amdgpu: Finished evicting pasid 0x8002
[ 6337.874865] amdgpu: Started evicting pasid 0x8002
[ 6337.874877] amdgpu: Finished evicting pasid 0x8002
[ 6338.042670] amdgpu: Started evicting pasid 0x8002
[ 6338.042683] amdgpu: Finished evicting pasid 0x8002
[ 6338.207190] amdgpu: Started evicting pasid 0x8002
[ 6338.207203] amdgpu: Finished evicting pasid 0x8002
[ 6338.371490] amdgpu: Started evicting pasid 0x8002
[ 6338.371504] amdgpu: Finished evicting pasid 0x8002
[ 6338.541175] amdgpu: Started evicting pasid 0x8002
[ 6338.541188] amdgpu: Finished evicting pasid 0x8002
[ 6338.705317] amdgpu: Started evicting pasid 0x8002
[ 6338.705330] amdgpu: Finished evicting pasid 0x8002
[ 6338.868157] amdgpu: Started evicting pasid 0x8002
[ 6338.868171] amdgpu: Finished evicting pasid 0x8002
[ 6339.027753] amdgpu: Started evicting pasid 0x8002
[ 6339.027767] amdgpu: Finished evicting pasid 0x8002
[ 6339.194219] amdgpu: Started evicting pasid 0x8002
[ 6339.194233] amdgpu: Finished evicting pasid 0x8002
[ 6339.360308] amdgpu: Started evicting pasid 0x8002
[ 6339.360322] amdgpu: Finished evicting pasid 0x8002
[ 6339.522091] amdgpu: Started evicting pasid 0x8002
[ 6339.522105] amdgpu: Finished evicting pasid 0x8002
[ 6339.687333] amdgpu: Started evicting pasid 0x8002
[ 6339.687347] amdgpu: Finished evicting pasid 0x8002
[ 6339.849105] amdgpu: Started evicting pasid 0x8002
[ 6339.849119] amdgpu: Finished evicting pasid 0x8002
[ 6340.017104] amdgpu: Started evicting pasid 0x8002
[ 6340.017119] amdgpu: Finished evicting pasid 0x8002
[ 6340.179552] amdgpu: Started evicting pasid 0x8002
[ 6340.179565] amdgpu: Finished evicting pasid 0x8002
[ 6340.346973] amdgpu: Started evicting pasid 0x8002
[ 6340.346986] amdgpu: Finished evicting pasid 0x8002
[ 6340.513044] amdgpu: Started evicting pasid 0x8002
[ 6340.513059] amdgpu: Finished evicting pasid 0x8002
[ 6341.048680] amdgpu: Started evicting pasid 0x8002
[ 6341.048693] amdgpu: Finished evicting pasid 0x8002
[ 6341.209998] amdgpu: Started evicting pasid 0x8002
[ 6341.210011] amdgpu: Finished evicting pasid 0x8002
[ 6341.372595] amdgpu: Started evicting pasid 0x8002
[ 6341.372610] amdgpu: Finished evicting pasid 0x8002
[ 6341.536389] amdgpu: Started evicting pasid 0x8002
[ 6341.536404] amdgpu: Finished evicting pasid 0x8002
[ 6341.699492] amdgpu: Started evicting pasid 0x8002
[ 6341.699506] amdgpu: Finished evicting pasid 0x8002
[ 6341.860444] amdgpu: Started evicting pasid 0x8002
[ 6341.860457] amdgpu: Finished evicting pasid 0x8002
[ 6342.020007] amdgpu: Started evicting pasid 0x8002
[ 6342.020022] amdgpu: Finished evicting pasid 0x8002
[ 6342.185826] amdgpu: Started evicting pasid 0x8002
[ 6342.185839] amdgpu: Finished evicting pasid 0x8002
[ 6342.355969] amdgpu: Started evicting pasid 0x8002
[ 6342.355983] amdgpu: Finished evicting pasid 0x8002
[ 6342.516609] amdgpu: Started evicting pasid 0x8002
[ 6342.516623] amdgpu: Finished evicting pasid 0x8002
[ 6342.684038] amdgpu: Started evicting pasid 0x8002
[ 6342.684057] amdgpu: Finished evicting pasid 0x8002
[ 6342.847542] amdgpu: Started evicting pasid 0x8002
[ 6342.847556] amdgpu: Finished evicting pasid 0x8002
[ 6343.014379] amdgpu: Started evicting pasid 0x8002
[ 6343.014393] amdgpu: Finished evicting pasid 0x8002
[ 6343.180369] amdgpu: Started evicting pasid 0x8002
[ 6343.180382] amdgpu: Finished evicting pasid 0x8002
[ 6343.341687] amdgpu: Started evicting pasid 0x8002
[ 6343.341700] amdgpu: Finished evicting pasid 0x8002
[ 6343.503480] amdgpu: Started evicting pasid 0x8002
[ 6343.503494] amdgpu: Finished evicting pasid 0x8002
[ 6343.669003] amdgpu: Started evicting pasid 0x8002
[ 6343.669023] amdgpu: Finished evicting pasid 0x8002
[ 6343.835952] amdgpu: Started evicting pasid 0x8002
[ 6343.835966] amdgpu: Finished evicting pasid 0x8002
[ 6343.999246] amdgpu: Started evicting pasid 0x8002
[ 6343.999260] amdgpu: Finished evicting pasid 0x8002
[ 6344.168471] amdgpu: Started evicting pasid 0x8002
[ 6344.168484] amdgpu: Finished evicting pasid 0x8002
[ 6344.330906] amdgpu: Started evicting pasid 0x8002
[ 6344.330921] amdgpu: Finished evicting pasid 0x8002
[ 6344.497259] amdgpu: Started evicting pasid 0x8002
[ 6344.497273] amdgpu: Finished evicting pasid 0x8002
[ 6344.655514] amdgpu: Started evicting pasid 0x8002
[ 6344.655527] amdgpu: Finished evicting pasid 0x8002
[ 6344.823342] amdgpu: Started evicting pasid 0x8002
[ 6344.823356] amdgpu: Finished evicting pasid 0x8002
[ 6344.991759] amdgpu: Started evicting pasid 0x8002
[ 6344.991773] amdgpu: Finished evicting pasid 0x8002
[ 6345.160857] amdgpu: Started evicting pasid 0x8002
[ 6345.160870] amdgpu: Finished evicting pasid 0x8002
[ 6345.321761] amdgpu: Started evicting pasid 0x8002
[ 6345.321775] amdgpu: Finished evicting pasid 0x8002
[ 6345.484829] amdgpu: Started evicting pasid 0x8002
[ 6345.484843] amdgpu: Finished evicting pasid 0x8002
[ 6345.646114] amdgpu: Started evicting pasid 0x8002
[ 6345.646128] amdgpu: Finished evicting pasid 0x8002
[ 6345.808351] amdgpu: Started evicting pasid 0x8002
[ 6345.808364] amdgpu: Finished evicting pasid 0x8002
[ 6345.968915] amdgpu: Started evicting pasid 0x8002
[ 6345.968929] amdgpu: Finished evicting pasid 0x8002
[ 6346.132790] amdgpu: Started evicting pasid 0x8002
[ 6346.132803] amdgpu: Finished evicting pasid 0x8002
[ 6346.292758] amdgpu: Started evicting pasid 0x8002
[ 6346.292773] amdgpu: Finished evicting pasid 0x8002
[ 6346.453348] amdgpu: Started evicting pasid 0x8002
[ 6346.453368] amdgpu: Finished evicting pasid 0x8002
[ 6346.614338] amdgpu: Started evicting pasid 0x8002
[ 6346.614351] amdgpu: Finished evicting pasid 0x8002
[ 6347.193747] amdgpu: Started evicting pasid 0x8002
[ 6347.193760] amdgpu: Finished evicting pasid 0x8002
[ 6348.117875] amdgpu: Started evicting pasid 0x8002
[ 6348.117889] amdgpu: Finished evicting pasid 0x8002
[ 6348.351850] amdgpu: Started evicting pasid 0x8002
[ 6348.351865] amdgpu: Finished evicting pasid 0x8002
[ 6348.518647] amdgpu: Started evicting pasid 0x8002
[ 6348.518660] amdgpu: Finished evicting pasid 0x8002
[ 6348.683735] amdgpu: Started evicting pasid 0x8002
[ 6348.683748] amdgpu: Finished evicting pasid 0x8002
[ 6348.846107] amdgpu: Started evicting pasid 0x8002
[ 6348.846121] amdgpu: Finished evicting pasid 0x8002
[ 6349.016079] amdgpu: Started evicting pasid 0x8002
[ 6349.016092] amdgpu: Finished evicting pasid 0x8002
[ 6349.534719] amdgpu: Started evicting pasid 0x8002
[ 6349.534734] amdgpu: Finished evicting pasid 0x8002
[ 6351.264123] amdgpu: Started evicting pasid 0x8002
[ 6351.264137] amdgpu: Finished evicting pasid 0x8002
[ 6351.430208] amdgpu: Started evicting pasid 0x8002
[ 6351.430222] amdgpu: Finished evicting pasid 0x8002
[ 6351.596688] amdgpu: Started evicting pasid 0x8002
[ 6351.596702] amdgpu: Finished evicting pasid 0x8002
[ 6351.758166] amdgpu: Started evicting pasid 0x8002
[ 6351.758180] amdgpu: Finished evicting pasid 0x8002
[ 6351.920432] amdgpu: Started evicting pasid 0x8002
[ 6351.920446] amdgpu: Finished evicting pasid 0x8002
[ 6352.658815] amdgpu: Started evicting pasid 0x8002
[ 6352.658829] amdgpu: Finished evicting pasid 0x8002
[ 6352.830563] amdgpu: Started evicting pasid 0x8002
[ 6352.830577] amdgpu: Finished evicting pasid 0x8002
[ 6352.991906] amdgpu: Started evicting pasid 0x8002
[ 6352.991920] amdgpu: Finished evicting pasid 0x8002
[ 6353.157199] amdgpu: Started evicting pasid 0x8002
[ 6353.157214] amdgpu: Finished evicting pasid 0x8002
[ 6353.164594] amdgpu: Started evicting pasid 0x8003
[ 6353.164608] amdgpu: Finished evicting pasid 0x8003
[ 6353.334775] amdgpu: Started evicting pasid 0x8002
[ 6353.334789] amdgpu: Finished evicting pasid 0x8002
[ 6353.484195] amdgpu: Started evicting pasid 0x8002
[ 6353.484210] amdgpu: Finished evicting pasid 0x8002
[ 6353.656903] amdgpu: Started evicting pasid 0x8002
[ 6353.656918] amdgpu: Finished evicting pasid 0x8002
[ 6353.798453] amdgpu: Started evicting pasid 0x8002
[ 6353.798472] amdgpu: Finished evicting pasid 0x8002
[ 6353.967901] amdgpu: Started evicting pasid 0x8002
[ 6353.967916] amdgpu: Finished evicting pasid 0x8002
[ 6354.131594] amdgpu: Started evicting pasid 0x8002
[ 6354.131608] amdgpu: Finished evicting pasid 0x8002
[ 6354.293260] amdgpu: Started evicting pasid 0x8002
[ 6354.293274] amdgpu: Finished evicting pasid 0x8002
[ 6354.455572] amdgpu: Started evicting pasid 0x8002
[ 6354.455585] amdgpu: Finished evicting pasid 0x8002
[ 6354.622997] amdgpu: Started evicting pasid 0x8002
[ 6354.623018] amdgpu: Finished evicting pasid 0x8002
[ 6354.787500] amdgpu: Started evicting pasid 0x8002
[ 6354.787514] amdgpu: Finished evicting pasid 0x8002
[ 6355.019890] amdgpu: Started evicting pasid 0x8002
[ 6355.019904] amdgpu: Finished evicting pasid 0x8002
[ 6355.184960] amdgpu: Started evicting pasid 0x8002
[ 6355.184975] amdgpu: Finished evicting pasid 0x8002
[ 6355.344329] amdgpu: Started evicting pasid 0x8002
[ 6355.344343] amdgpu: Finished evicting pasid 0x8002
[ 6355.505650] amdgpu: Started evicting pasid 0x8002
[ 6355.505664] amdgpu: Finished evicting pasid 0x8002
[ 6355.674521] amdgpu: Started evicting pasid 0x8002
[ 6355.674535] amdgpu: Finished evicting pasid 0x8002
[ 6356.191206] amdgpu: Started evicting pasid 0x8002
[ 6356.191221] amdgpu: Finished evicting pasid 0x8002
[ 6356.360792] amdgpu: Started evicting pasid 0x8002
[ 6356.360806] amdgpu: Finished evicting pasid 0x8002
[ 6356.522760] amdgpu: Started evicting pasid 0x8002
[ 6356.522775] amdgpu: Finished evicting pasid 0x8002
[ 6356.684054] amdgpu: Started evicting pasid 0x8002
[ 6356.684068] amdgpu: Finished evicting pasid 0x8002
[ 6356.847218] amdgpu: Started evicting pasid 0x8002
[ 6356.847232] amdgpu: Finished evicting pasid 0x8002
[ 6357.017465] amdgpu: Started evicting pasid 0x8002
[ 6357.017478] amdgpu: Finished evicting pasid 0x8002
[ 6357.179640] amdgpu: Started evicting pasid 0x8002
[ 6357.179654] amdgpu: Finished evicting pasid 0x8002
[ 6357.346359] amdgpu: Started evicting pasid 0x8002
[ 6357.346372] amdgpu: Finished evicting pasid 0x8002
[ 6357.832228] show_signal: 35 callbacks suppressed
[ 6357.832232] traps: Command Queue T[45134] general protection fault ip:7f4964825079 sp:7f4965e93b10 error:0 in libamdhip64.so.4.0.20496-4f163c68[7f4964627000+2f1000]
[ 6357.927366] amdgpu: Started evicting pasid 0x8002
[ 6357.927427] amdgpu: Finished evicting pasid 0x8002
[ 6359.513848] amdgpu: Started evicting pasid 0x8002
[ 6359.513919] amdgpu: Finished evicting pasid 0x8002
[ 6361.873937] amdgpu: Started evicting pasid 0x8002
[ 6361.873951] amdgpu: Finished evicting pasid 0x8002
[ 6362.357917] amdgpu: Started evicting pasid 0x8002
[ 6362.357930] amdgpu: Finished evicting pasid 0x8002
[ 6362.837501] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837505] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa00000 from client 18
[ 6362.837507] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6362.837509] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837510] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6362.837512] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837513] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6362.837515] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837516] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6362.837522] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837524] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa01000 from client 18
[ 6362.837526] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6362.837527] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837529] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6362.837530] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837532] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6362.837533] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837534] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6362.837539] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837540] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa02000 from client 18
[ 6362.837542] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6362.837543] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837545] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6362.837546] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837547] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6362.837549] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837550] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6362.837554] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837556] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa03000 from client 18
[ 6362.837557] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6362.837559] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837560] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6362.837562] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837563] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6362.837564] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837566] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6362.837570] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837571] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa04000 from client 18
[ 6362.837573] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837574] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837576] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837577] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837579] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837580] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837581] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.837587] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837588] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa05000 from client 18
[ 6362.837590] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837591] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837593] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837594] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837596] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837597] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837598] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.837604] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837606] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa06000 from client 18
[ 6362.837607] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837609] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837610] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837611] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837613] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837614] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837615] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.837621] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837622] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa08000 from client 18
[ 6362.837623] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837624] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837625] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837626] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837627] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837628] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837629] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.837634] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837635] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa07000 from client 18
[ 6362.837636] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837637] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837638] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837639] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837641] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837642] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837643] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.837648] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 45324 thread hipMemsetAsyncM pid 45324)
[ 6362.837649] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9aafa00000 from client 18
[ 6362.837650] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6362.837652] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6362.837653] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6362.837654] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6362.837655] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6362.837655] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6362.837656] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6362.926554] amdgpu: Started evicting pasid 0x8002
[ 6362.926564] amdgpu: Finished evicting pasid 0x8002
[ 6363.410982] amdgpu: Started evicting pasid 0x8002
[ 6363.410993] amdgpu: Finished evicting pasid 0x8002
[ 6363.571640] amdgpu: Started evicting pasid 0x8002
[ 6363.571654] amdgpu: Finished evicting pasid 0x8002
[ 6364.373543] amdgpu: Started evicting pasid 0x8002
[ 6364.373558] amdgpu: Finished evicting pasid 0x8002
[ 6364.540430] amdgpu: Started evicting pasid 0x8002
[ 6364.540444] amdgpu: Finished evicting pasid 0x8002
[ 6364.712872] amdgpu: Started evicting pasid 0x8002
[ 6364.712885] amdgpu: Finished evicting pasid 0x8002
[ 6364.946820] amdgpu: Started evicting pasid 0x8002
[ 6364.946834] amdgpu: Finished evicting pasid 0x8002
[ 6365.341191] amdgpu: Started evicting pasid 0x8002
[ 6365.341247] amdgpu: Finished evicting pasid 0x8002
[ 6365.750883] amdgpu: Started evicting pasid 0x8002
[ 6365.750939] amdgpu: Finished evicting pasid 0x8002
[ 6366.159269] amdgpu: Started evicting pasid 0x8002
[ 6366.159325] amdgpu: Finished evicting pasid 0x8002
[ 6366.595708] amdgpu: Started evicting pasid 0x8002
[ 6366.595762] amdgpu: Finished evicting pasid 0x8002
[ 6367.068688] amdgpu: Started evicting pasid 0x8002
[ 6367.068743] amdgpu: Finished evicting pasid 0x8002
[ 6367.534519] amdgpu: Started evicting pasid 0x8002
[ 6367.534577] amdgpu: Finished evicting pasid 0x8002
[ 6367.998015] amdgpu: Started evicting pasid 0x8002
[ 6367.998062] amdgpu: Finished evicting pasid 0x8002
[ 6368.171953] amdgpu: Started evicting pasid 0x8002
[ 6368.171967] amdgpu: Finished evicting pasid 0x8002
[ 6368.335572] amdgpu: Started evicting pasid 0x8002
[ 6368.335586] amdgpu: Finished evicting pasid 0x8002
[ 6368.496264] amdgpu: Started evicting pasid 0x8002
[ 6368.496278] amdgpu: Finished evicting pasid 0x8002
[ 6369.058255] amdgpu: Started evicting pasid 0x8002
[ 6369.058269] amdgpu: Finished evicting pasid 0x8002
[ 6369.220970] amdgpu: Started evicting pasid 0x8002
[ 6369.220985] amdgpu: Finished evicting pasid 0x8002
[ 6369.383288] amdgpu: Started evicting pasid 0x8002
[ 6369.383302] amdgpu: Finished evicting pasid 0x8002
[ 6369.545182] amdgpu: Started evicting pasid 0x8002
[ 6369.545197] amdgpu: Finished evicting pasid 0x8002
[ 6369.706935] amdgpu: Started evicting pasid 0x8002
[ 6369.706949] amdgpu: Finished evicting pasid 0x8002
[ 6369.868646] amdgpu: Started evicting pasid 0x8002
[ 6369.868660] amdgpu: Finished evicting pasid 0x8002
[ 6370.100820] amdgpu: Started evicting pasid 0x8002
[ 6370.100834] amdgpu: Finished evicting pasid 0x8002
[ 6370.268340] amdgpu: Started evicting pasid 0x8002
[ 6370.268354] amdgpu: Finished evicting pasid 0x8002
[ 6405.868663] amdgpu: Started evicting pasid 0x8002
[ 6405.868677] amdgpu: Finished evicting pasid 0x8002
[ 6406.030288] amdgpu: Started evicting pasid 0x8002
[ 6406.030302] amdgpu: Finished evicting pasid 0x8002
[ 6406.196122] amdgpu: Started evicting pasid 0x8002
[ 6406.196135] amdgpu: Finished evicting pasid 0x8002
[ 6406.369952] amdgpu: Started evicting pasid 0x8002
[ 6406.369965] amdgpu: Finished evicting pasid 0x8002
[ 6406.538491] amdgpu: Started evicting pasid 0x8002
[ 6406.538506] amdgpu: Finished evicting pasid 0x8002
[ 6406.711518] amdgpu: Started evicting pasid 0x8002
[ 6406.711531] amdgpu: Finished evicting pasid 0x8002
[ 6406.876288] amdgpu: Started evicting pasid 0x8002
[ 6406.876301] amdgpu: Finished evicting pasid 0x8002
[ 6407.039339] amdgpu: Started evicting pasid 0x8002
[ 6407.039353] amdgpu: Finished evicting pasid 0x8002
[ 6417.801118] amdgpu: Started evicting pasid 0x8002
[ 6417.801132] amdgpu: Finished evicting pasid 0x8002
[ 6417.971768] amdgpu: Started evicting pasid 0x8002
[ 6417.971782] amdgpu: Finished evicting pasid 0x8002
[ 6418.145107] amdgpu: Started evicting pasid 0x8002
[ 6418.145122] amdgpu: Finished evicting pasid 0x8002
[ 6418.312615] amdgpu: Started evicting pasid 0x8002
[ 6418.312629] amdgpu: Finished evicting pasid 0x8002
[ 6418.477818] amdgpu: Started evicting pasid 0x8002
[ 6418.477833] amdgpu: Finished evicting pasid 0x8002
[ 6418.649317] amdgpu: Started evicting pasid 0x8002
[ 6418.649332] amdgpu: Finished evicting pasid 0x8002
[ 6424.497549] amdgpu: Started evicting pasid 0x8002
[ 6424.497564] amdgpu: Finished evicting pasid 0x8002
[ 6426.194416] amdgpu: Started evicting pasid 0x8002
[ 6426.194430] amdgpu: Finished evicting pasid 0x8002
[ 6426.363108] amdgpu: Started evicting pasid 0x8002
[ 6426.363123] amdgpu: Finished evicting pasid 0x8002
[ 6426.525340] amdgpu: Started evicting pasid 0x8002
[ 6426.525353] amdgpu: Finished evicting pasid 0x8002
[ 6426.687589] amdgpu: Started evicting pasid 0x8002
[ 6426.687603] amdgpu: Finished evicting pasid 0x8002
[ 6427.153042] amdgpu: Started evicting pasid 0x8002
[ 6427.153056] amdgpu: Finished evicting pasid 0x8002
[ 6427.315582] amdgpu: Started evicting pasid 0x8002
[ 6427.315596] amdgpu: Finished evicting pasid 0x8002
[ 6490.478237] amdgpu: Started evicting pasid 0x8002
[ 6490.478248] amdgpu: Finished evicting pasid 0x8002
[ 6490.581523] amdgpu: Started restoring pasid 0x8002
[ 6490.581532] amdgpu: Finished restoring pasid 0x8002
[ 6490.630737] amdgpu: Started evicting pasid 0x8002
[ 6490.630748] amdgpu: Finished evicting pasid 0x8002
[ 6490.869534] amdgpu: Started evicting pasid 0x8002
[ 6490.869543] amdgpu: Finished evicting pasid 0x8002
[ 6492.582226] amdgpu: Started evicting pasid 0x8002
[ 6492.582242] amdgpu: Finished evicting pasid 0x8002
[ 6494.424632] amdgpu: Started evicting pasid 0x8002
[ 6494.424649] amdgpu: Finished evicting pasid 0x8002
[ 6494.592408] amdgpu: Started evicting pasid 0x8002
[ 6494.592423] amdgpu: Finished evicting pasid 0x8002
[ 6494.758887] amdgpu: Started evicting pasid 0x8002
[ 6494.758905] amdgpu: Finished evicting pasid 0x8002
[ 6494.930530] amdgpu: Started evicting pasid 0x8002
[ 6494.930546] amdgpu: Finished evicting pasid 0x8002
[ 6495.129751] amdgpu: Started evicting pasid 0x8002
[ 6495.129766] amdgpu: Finished evicting pasid 0x8002
[ 6495.301786] amdgpu: Started evicting pasid 0x8002
[ 6495.301802] amdgpu: Finished evicting pasid 0x8002
[ 6495.471339] amdgpu: Started evicting pasid 0x8002
[ 6495.471355] amdgpu: Finished evicting pasid 0x8002
[ 6495.639356] amdgpu: Started evicting pasid 0x8002
[ 6495.639373] amdgpu: Finished evicting pasid 0x8002
[ 6495.808271] amdgpu: Started evicting pasid 0x8002
[ 6495.808287] amdgpu: Finished evicting pasid 0x8002
[ 6495.976502] amdgpu: Started evicting pasid 0x8002
[ 6495.976519] amdgpu: Finished evicting pasid 0x8002
[ 6496.143032] amdgpu: Started evicting pasid 0x8002
[ 6496.143047] amdgpu: Finished evicting pasid 0x8002
[ 6496.313015] amdgpu: Started evicting pasid 0x8002
[ 6496.313030] amdgpu: Finished evicting pasid 0x8002
[ 6496.487323] amdgpu: Started evicting pasid 0x8002
[ 6496.487339] amdgpu: Finished evicting pasid 0x8002
[ 6496.685705] amdgpu: Started evicting pasid 0x8002
[ 6496.685720] amdgpu: Finished evicting pasid 0x8002
[ 6496.856423] amdgpu: Started evicting pasid 0x8002
[ 6496.856438] amdgpu: Finished evicting pasid 0x8002
[ 6497.020815] amdgpu: Started evicting pasid 0x8002
[ 6497.020832] amdgpu: Finished evicting pasid 0x8002
[ 6497.195712] amdgpu: Started evicting pasid 0x8002
[ 6497.195722] amdgpu: Finished evicting pasid 0x8002
[ 6497.363689] amdgpu: Started evicting pasid 0x8002
[ 6497.363704] amdgpu: Finished evicting pasid 0x8002
[ 6497.528224] amdgpu: Started evicting pasid 0x8002
[ 6497.528241] amdgpu: Finished evicting pasid 0x8002
[ 6497.694927] amdgpu: Started evicting pasid 0x8002
[ 6497.694944] amdgpu: Finished evicting pasid 0x8002
[ 6497.859100] amdgpu: Started evicting pasid 0x8002
[ 6497.859115] amdgpu: Finished evicting pasid 0x8002
[ 6498.027653] amdgpu: Started evicting pasid 0x8002
[ 6498.027670] amdgpu: Finished evicting pasid 0x8002
[ 6498.192226] amdgpu: Started evicting pasid 0x8002
[ 6498.192243] amdgpu: Finished evicting pasid 0x8002
[ 6498.357167] amdgpu: Started evicting pasid 0x8002
[ 6498.357182] amdgpu: Finished evicting pasid 0x8002
[ 6498.525663] amdgpu: Started evicting pasid 0x8002
[ 6498.525680] amdgpu: Finished evicting pasid 0x8002
[ 6498.693402] amdgpu: Started evicting pasid 0x8002
[ 6498.693418] amdgpu: Finished evicting pasid 0x8002
[ 6498.859431] amdgpu: Started evicting pasid 0x8002
[ 6498.859446] amdgpu: Finished evicting pasid 0x8002
[ 6499.027066] amdgpu: Started evicting pasid 0x8002
[ 6499.027083] amdgpu: Finished evicting pasid 0x8002
[ 6499.223693] amdgpu: Started evicting pasid 0x8002
[ 6499.223707] amdgpu: Finished evicting pasid 0x8002
[ 6499.417119] amdgpu: Started evicting pasid 0x8002
[ 6499.417134] amdgpu: Finished evicting pasid 0x8002
[ 6499.587194] amdgpu: Started evicting pasid 0x8002
[ 6499.587210] amdgpu: Finished evicting pasid 0x8002
[ 6499.752800] amdgpu: Started evicting pasid 0x8002
[ 6499.752814] amdgpu: Finished evicting pasid 0x8002
[ 6499.922719] amdgpu: Started evicting pasid 0x8002
[ 6499.922736] amdgpu: Finished evicting pasid 0x8002
[ 6500.090543] amdgpu: Started evicting pasid 0x8002
[ 6500.090558] amdgpu: Finished evicting pasid 0x8002
[ 6500.256264] amdgpu: Started evicting pasid 0x8002
[ 6500.256281] amdgpu: Finished evicting pasid 0x8002
[ 6500.421402] amdgpu: Started evicting pasid 0x8002
[ 6500.421417] amdgpu: Finished evicting pasid 0x8002
[ 6500.589038] amdgpu: Started evicting pasid 0x8002
[ 6500.589056] amdgpu: Finished evicting pasid 0x8002
[ 6500.760300] amdgpu: Started evicting pasid 0x8002
[ 6500.760316] amdgpu: Finished evicting pasid 0x8002
[ 6500.926735] amdgpu: Started evicting pasid 0x8002
[ 6500.926750] amdgpu: Finished evicting pasid 0x8002
[ 6501.092836] amdgpu: Started evicting pasid 0x8002
[ 6501.092851] amdgpu: Finished evicting pasid 0x8002
[ 6501.262461] amdgpu: Started evicting pasid 0x8002
[ 6501.262475] amdgpu: Finished evicting pasid 0x8002
[ 6501.427152] amdgpu: Started evicting pasid 0x8002
[ 6501.427167] amdgpu: Finished evicting pasid 0x8002
[ 6501.593676] amdgpu: Started evicting pasid 0x8002
[ 6501.593691] amdgpu: Finished evicting pasid 0x8002
[ 6501.759708] amdgpu: Started evicting pasid 0x8002
[ 6501.759722] amdgpu: Finished evicting pasid 0x8002
[ 6501.921339] amdgpu: Started evicting pasid 0x8002
[ 6501.921353] amdgpu: Finished evicting pasid 0x8002
[ 6502.086837] amdgpu: Started evicting pasid 0x8002
[ 6502.086852] amdgpu: Finished evicting pasid 0x8002
[ 6502.638843] amdgpu: Started evicting pasid 0x8002
[ 6502.638857] amdgpu: Finished evicting pasid 0x8002
[ 6502.799849] amdgpu: Started evicting pasid 0x8002
[ 6502.799864] amdgpu: Finished evicting pasid 0x8002
[ 6502.962056] amdgpu: Started evicting pasid 0x8002
[ 6502.962071] amdgpu: Finished evicting pasid 0x8002
[ 6503.125879] amdgpu: Started evicting pasid 0x8002
[ 6503.125894] amdgpu: Finished evicting pasid 0x8002
[ 6503.292875] amdgpu: Started evicting pasid 0x8002
[ 6503.292888] amdgpu: Finished evicting pasid 0x8002
[ 6503.456573] amdgpu: Started evicting pasid 0x8002
[ 6503.456587] amdgpu: Finished evicting pasid 0x8002
[ 6503.624478] amdgpu: Started evicting pasid 0x8002
[ 6503.624492] amdgpu: Finished evicting pasid 0x8002
[ 6503.789721] amdgpu: Started evicting pasid 0x8002
[ 6503.789734] amdgpu: Finished evicting pasid 0x8002
[ 6503.953905] amdgpu: Started evicting pasid 0x8002
[ 6503.953920] amdgpu: Finished evicting pasid 0x8002
[ 6504.121654] amdgpu: Started evicting pasid 0x8002
[ 6504.121668] amdgpu: Finished evicting pasid 0x8002
[ 6504.285708] amdgpu: Started evicting pasid 0x8002
[ 6504.285722] amdgpu: Finished evicting pasid 0x8002
[ 6504.450864] amdgpu: Started evicting pasid 0x8002
[ 6504.450877] amdgpu: Finished evicting pasid 0x8002
[ 6504.616603] amdgpu: Started evicting pasid 0x8002
[ 6504.616617] amdgpu: Finished evicting pasid 0x8002
[ 6504.780307] amdgpu: Started evicting pasid 0x8002
[ 6504.780322] amdgpu: Finished evicting pasid 0x8002
[ 6504.948231] amdgpu: Started evicting pasid 0x8002
[ 6504.948246] amdgpu: Finished evicting pasid 0x8002
[ 6505.115189] amdgpu: Started evicting pasid 0x8002
[ 6505.115204] amdgpu: Finished evicting pasid 0x8002
[ 6505.277884] amdgpu: Started evicting pasid 0x8002
[ 6505.277898] amdgpu: Finished evicting pasid 0x8002
[ 6505.444560] amdgpu: Started evicting pasid 0x8002
[ 6505.444575] amdgpu: Finished evicting pasid 0x8002
[ 6505.610669] amdgpu: Started evicting pasid 0x8002
[ 6505.610684] amdgpu: Finished evicting pasid 0x8002
[ 6505.774803] amdgpu: Started evicting pasid 0x8002
[ 6505.774817] amdgpu: Finished evicting pasid 0x8002
[ 6505.941048] amdgpu: Started evicting pasid 0x8002
[ 6505.941062] amdgpu: Finished evicting pasid 0x8002
[ 6506.105403] amdgpu: Started evicting pasid 0x8002
[ 6506.105417] amdgpu: Finished evicting pasid 0x8002
[ 6506.271602] amdgpu: Started evicting pasid 0x8002
[ 6506.271616] amdgpu: Finished evicting pasid 0x8002
[ 6506.432984] amdgpu: Started evicting pasid 0x8002
[ 6506.432998] amdgpu: Finished evicting pasid 0x8002
[ 6506.595058] amdgpu: Started evicting pasid 0x8002
[ 6506.595072] amdgpu: Finished evicting pasid 0x8002
[ 6506.757334] amdgpu: Started evicting pasid 0x8002
[ 6506.757353] amdgpu: Finished evicting pasid 0x8002
[ 6506.919034] amdgpu: Started evicting pasid 0x8002
[ 6506.919048] amdgpu: Finished evicting pasid 0x8002
[ 6507.079797] amdgpu: Started evicting pasid 0x8002
[ 6507.079810] amdgpu: Finished evicting pasid 0x8002
[ 6507.240926] amdgpu: Started evicting pasid 0x8002
[ 6507.240940] amdgpu: Finished evicting pasid 0x8002
[ 6507.403632] amdgpu: Started evicting pasid 0x8002
[ 6507.403646] amdgpu: Finished evicting pasid 0x8002
[ 6507.566584] amdgpu: Started evicting pasid 0x8002
[ 6507.566599] amdgpu: Finished evicting pasid 0x8002
[ 6507.731155] amdgpu: Started evicting pasid 0x8002
[ 6507.731169] amdgpu: Finished evicting pasid 0x8002
[ 6507.887936] amdgpu: Started evicting pasid 0x8002
[ 6507.887967] amdgpu: Finished evicting pasid 0x8002
[ 6508.049886] amdgpu: Started evicting pasid 0x8002
[ 6508.049899] amdgpu: Finished evicting pasid 0x8002
[ 6508.212169] amdgpu: Started evicting pasid 0x8002
[ 6508.212184] amdgpu: Finished evicting pasid 0x8002
[ 6508.786614] amdgpu: Started evicting pasid 0x8002
[ 6508.786629] amdgpu: Finished evicting pasid 0x8002
[ 6509.700774] amdgpu: Started evicting pasid 0x8002
[ 6509.700789] amdgpu: Finished evicting pasid 0x8002
[ 6509.921969] amdgpu: Started evicting pasid 0x8002
[ 6509.921983] amdgpu: Finished evicting pasid 0x8002
[ 6510.083110] amdgpu: Started evicting pasid 0x8002
[ 6510.083125] amdgpu: Finished evicting pasid 0x8002
[ 6510.245638] amdgpu: Started evicting pasid 0x8002
[ 6510.245653] amdgpu: Finished evicting pasid 0x8002
[ 6510.409692] amdgpu: Started evicting pasid 0x8002
[ 6510.409706] amdgpu: Finished evicting pasid 0x8002
[ 6510.571506] amdgpu: Started evicting pasid 0x8002
[ 6510.571521] amdgpu: Finished evicting pasid 0x8002
[ 6511.089459] amdgpu: Started evicting pasid 0x8002
[ 6511.089473] amdgpu: Finished evicting pasid 0x8002
[ 6512.777275] amdgpu: Started evicting pasid 0x8002
[ 6512.777289] amdgpu: Finished evicting pasid 0x8002
[ 6512.944615] amdgpu: Started evicting pasid 0x8002
[ 6512.944630] amdgpu: Finished evicting pasid 0x8002
[ 6513.105774] amdgpu: Started evicting pasid 0x8002
[ 6513.105787] amdgpu: Finished evicting pasid 0x8002
[ 6513.268000] amdgpu: Started evicting pasid 0x8002
[ 6513.268015] amdgpu: Finished evicting pasid 0x8002
[ 6513.432157] amdgpu: Started evicting pasid 0x8002
[ 6513.432171] amdgpu: Finished evicting pasid 0x8002
[ 6514.179353] amdgpu: Started evicting pasid 0x8002
[ 6514.179367] amdgpu: Finished evicting pasid 0x8002
[ 6514.343271] amdgpu: Started evicting pasid 0x8002
[ 6514.343286] amdgpu: Finished evicting pasid 0x8002
[ 6514.506647] amdgpu: Started evicting pasid 0x8002
[ 6514.506662] amdgpu: Finished evicting pasid 0x8002
[ 6514.673136] amdgpu: Started evicting pasid 0x8002
[ 6514.673150] amdgpu: Finished evicting pasid 0x8002
[ 6514.684943] amdgpu: Started evicting pasid 0x8003
[ 6514.684958] amdgpu: Finished evicting pasid 0x8003
[ 6514.856119] amdgpu: Started evicting pasid 0x8002
[ 6514.856133] amdgpu: Finished evicting pasid 0x8002
[ 6514.997245] amdgpu: Started evicting pasid 0x8002
[ 6514.997259] amdgpu: Finished evicting pasid 0x8002
[ 6515.169834] amdgpu: Started evicting pasid 0x8002
[ 6515.169847] amdgpu: Finished evicting pasid 0x8002
[ 6515.308167] amdgpu: Started evicting pasid 0x8002
[ 6515.308182] amdgpu: Finished evicting pasid 0x8002
[ 6515.474107] amdgpu: Started evicting pasid 0x8002
[ 6515.474121] amdgpu: Finished evicting pasid 0x8002
[ 6515.639086] amdgpu: Started evicting pasid 0x8002
[ 6515.639101] amdgpu: Finished evicting pasid 0x8002
[ 6515.800014] amdgpu: Started evicting pasid 0x8002
[ 6515.800028] amdgpu: Finished evicting pasid 0x8002
[ 6515.968071] amdgpu: Started evicting pasid 0x8002
[ 6515.968086] amdgpu: Finished evicting pasid 0x8002
[ 6516.129999] amdgpu: Started evicting pasid 0x8002
[ 6516.130013] amdgpu: Finished evicting pasid 0x8002
[ 6516.290683] amdgpu: Started evicting pasid 0x8002
[ 6516.290699] amdgpu: Finished evicting pasid 0x8002
[ 6516.515386] amdgpu: Started evicting pasid 0x8002
[ 6516.515400] amdgpu: Finished evicting pasid 0x8002
[ 6516.678696] amdgpu: Started evicting pasid 0x8002
[ 6516.678710] amdgpu: Finished evicting pasid 0x8002
[ 6516.838414] amdgpu: Started evicting pasid 0x8002
[ 6516.838428] amdgpu: Finished evicting pasid 0x8002
[ 6516.998253] amdgpu: Started evicting pasid 0x8002
[ 6516.998267] amdgpu: Finished evicting pasid 0x8002
[ 6517.159699] amdgpu: Started evicting pasid 0x8002
[ 6517.159714] amdgpu: Finished evicting pasid 0x8002
[ 6517.666179] amdgpu: Started evicting pasid 0x8002
[ 6517.666194] amdgpu: Finished evicting pasid 0x8002
[ 6517.827900] amdgpu: Started evicting pasid 0x8002
[ 6517.827914] amdgpu: Finished evicting pasid 0x8002
[ 6517.992668] amdgpu: Started evicting pasid 0x8002
[ 6517.992683] amdgpu: Finished evicting pasid 0x8002
[ 6518.157799] amdgpu: Started evicting pasid 0x8002
[ 6518.157813] amdgpu: Finished evicting pasid 0x8002
[ 6518.319996] amdgpu: Started evicting pasid 0x8002
[ 6518.320011] amdgpu: Finished evicting pasid 0x8002
[ 6518.491330] amdgpu: Started evicting pasid 0x8002
[ 6518.491350] amdgpu: Finished evicting pasid 0x8002
[ 6518.656528] amdgpu: Started evicting pasid 0x8002
[ 6518.656543] amdgpu: Finished evicting pasid 0x8002
[ 6518.818910] amdgpu: Started evicting pasid 0x8002
[ 6518.818924] amdgpu: Finished evicting pasid 0x8002
[ 6519.175146] gmc_v9_0_process_interrupt: 26 callbacks suppressed
[ 6519.175157] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175164] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5200000 from client 18
[ 6519.175168] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[ 6519.175171] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175173] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6519.175176] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175179] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[ 6519.175181] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175184] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175200] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175203] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5201000 from client 18
[ 6519.175206] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175209] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175211] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175214] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175216] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175219] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175221] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175228] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175232] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5202000 from client 18
[ 6519.175234] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175237] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175239] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175242] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175244] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175247] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175249] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175256] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175259] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5203000 from client 18
[ 6519.175262] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175265] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175267] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175270] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175272] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175275] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175277] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175284] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175287] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5204000 from client 18
[ 6519.175290] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175292] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175295] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175297] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175300] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175302] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175305] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175311] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175314] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5205000 from client 18
[ 6519.175317] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175319] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175322] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175324] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175327] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175329] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175332] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175338] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175341] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5206000 from client 18
[ 6519.175344] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175346] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175349] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175351] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175354] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175356] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175359] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175365] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175368] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5207000 from client 18
[ 6519.175371] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175374] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175376] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175378] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175381] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175383] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175386] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175393] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175396] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5208000 from client 18
[ 6519.175398] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175401] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175403] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175406] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175408] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175411] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175413] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.175420] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 55521 thread hipMemset pid 55521)
[ 6519.175423] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f04c5209000 from client 18
[ 6519.175425] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6519.175428] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6519.175430] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6519.175433] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6519.175435] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6519.175438] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6519.175440] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6519.276803] amdgpu: Started evicting pasid 0x8002
[ 6519.276817] amdgpu: Finished evicting pasid 0x8002
[ 6520.871470] amdgpu: Started evicting pasid 0x8002
[ 6520.871540] amdgpu: Finished evicting pasid 0x8002
[ 6523.217803] amdgpu: Started evicting pasid 0x8002
[ 6523.217818] amdgpu: Finished evicting pasid 0x8002
[ 6523.717311] amdgpu: Started evicting pasid 0x8002
[ 6523.717324] amdgpu: Finished evicting pasid 0x8002
[ 6526.687294] gmc_v9_0_process_interrupt: 77 callbacks suppressed
[ 6526.687303] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687310] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee00000 from client 18
[ 6526.687314] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6526.687317] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687320] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6526.687323] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687325] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6526.687328] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687330] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6526.687340] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687343] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee01000 from client 18
[ 6526.687346] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6526.687349] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687351] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6526.687354] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687356] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6526.687359] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687361] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6526.687368] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687371] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee02000 from client 18
[ 6526.687374] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6526.687376] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687379] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6526.687382] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687384] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6526.687387] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687389] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6526.687395] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687398] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee03000 from client 18
[ 6526.687401] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687404] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687406] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687409] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687411] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687414] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687416] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687424] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687427] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee04000 from client 18
[ 6526.687430] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687432] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687435] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687437] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687440] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687442] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687445] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687452] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687456] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee05000 from client 18
[ 6526.687458] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687461] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687463] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687466] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687468] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687471] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687473] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687490] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687493] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee06000 from client 18
[ 6526.687496] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687498] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687501] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687503] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687506] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687508] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687511] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687519] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687522] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee07000 from client 18
[ 6526.687525] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687527] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687530] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687532] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687535] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687537] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687540] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687548] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687551] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee08000 from client 18
[ 6526.687554] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687556] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687559] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687561] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687564] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687566] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687569] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.687578] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 55713 thread hipMemsetAsyncM pid 55713)
[ 6526.687581] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f81bee00000 from client 18
[ 6526.687584] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6526.687586] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6526.687589] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6526.687591] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6526.687594] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6526.687597] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6526.687599] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6526.776775] amdgpu: Started evicting pasid 0x8002
[ 6526.776793] amdgpu: Finished evicting pasid 0x8002
[ 6527.310856] amdgpu: Started evicting pasid 0x8002
[ 6527.310864] amdgpu: Finished evicting pasid 0x8002
[ 6527.472432] amdgpu: Started evicting pasid 0x8002
[ 6527.472445] amdgpu: Finished evicting pasid 0x8002
[ 6528.269850] amdgpu: Started evicting pasid 0x8002
[ 6528.269864] amdgpu: Finished evicting pasid 0x8002
[ 6528.429413] amdgpu: Started evicting pasid 0x8002
[ 6528.429426] amdgpu: Finished evicting pasid 0x8002
[ 6528.589580] amdgpu: Started evicting pasid 0x8002
[ 6528.589593] amdgpu: Finished evicting pasid 0x8002
[ 6528.818882] amdgpu: Started evicting pasid 0x8002
[ 6528.818896] amdgpu: Finished evicting pasid 0x8002
[ 6529.211800] amdgpu: Started evicting pasid 0x8002
[ 6529.211859] amdgpu: Finished evicting pasid 0x8002
[ 6529.615191] amdgpu: Started evicting pasid 0x8002
[ 6529.615253] amdgpu: Finished evicting pasid 0x8002
[ 6530.018649] amdgpu: Started evicting pasid 0x8002
[ 6530.018709] amdgpu: Finished evicting pasid 0x8002
[ 6530.441153] amdgpu: Started evicting pasid 0x8002
[ 6530.441214] amdgpu: Finished evicting pasid 0x8002
[ 6530.908110] amdgpu: Started evicting pasid 0x8002
[ 6530.908176] amdgpu: Finished evicting pasid 0x8002
[ 6531.372869] amdgpu: Started evicting pasid 0x8002
[ 6531.372918] amdgpu: Finished evicting pasid 0x8002
[ 6531.838303] amdgpu: Started evicting pasid 0x8002
[ 6531.838352] amdgpu: Finished evicting pasid 0x8002
[ 6532.013475] amdgpu: Started evicting pasid 0x8002
[ 6532.013489] amdgpu: Finished evicting pasid 0x8002
[ 6532.172051] amdgpu: Started evicting pasid 0x8002
[ 6532.172064] amdgpu: Finished evicting pasid 0x8002
[ 6532.334105] amdgpu: Started evicting pasid 0x8002
[ 6532.334119] amdgpu: Finished evicting pasid 0x8002
[ 6532.882379] amdgpu: Started evicting pasid 0x8002
[ 6532.882392] amdgpu: Finished evicting pasid 0x8002
[ 6533.045451] amdgpu: Started evicting pasid 0x8002
[ 6533.045463] amdgpu: Finished evicting pasid 0x8002
[ 6533.203978] amdgpu: Started evicting pasid 0x8002
[ 6533.203991] amdgpu: Finished evicting pasid 0x8002
[ 6533.365559] amdgpu: Started evicting pasid 0x8002
[ 6533.365573] amdgpu: Finished evicting pasid 0x8002
[ 6533.526226] amdgpu: Started evicting pasid 0x8002
[ 6533.526240] amdgpu: Finished evicting pasid 0x8002
[ 6533.688032] amdgpu: Started evicting pasid 0x8002
[ 6533.688045] amdgpu: Finished evicting pasid 0x8002
[ 6533.916843] amdgpu: Started evicting pasid 0x8002
[ 6533.916857] amdgpu: Finished evicting pasid 0x8002
[ 6534.079872] amdgpu: Started evicting pasid 0x8002
[ 6534.079886] amdgpu: Finished evicting pasid 0x8002
[ 6571.428644] amdgpu: Started evicting pasid 0x8002
[ 6571.428657] amdgpu: Finished evicting pasid 0x8002
[ 6571.588819] amdgpu: Started evicting pasid 0x8002
[ 6571.588833] amdgpu: Finished evicting pasid 0x8002
[ 6571.748001] amdgpu: Started evicting pasid 0x8002
[ 6571.748014] amdgpu: Finished evicting pasid 0x8002
[ 6571.908360] amdgpu: Started evicting pasid 0x8002
[ 6571.908375] amdgpu: Finished evicting pasid 0x8002
[ 6572.069807] amdgpu: Started evicting pasid 0x8002
[ 6572.069820] amdgpu: Finished evicting pasid 0x8002
[ 6572.230860] amdgpu: Started evicting pasid 0x8002
[ 6572.230874] amdgpu: Finished evicting pasid 0x8002
[ 6572.392840] amdgpu: Started evicting pasid 0x8002
[ 6572.392854] amdgpu: Finished evicting pasid 0x8002
[ 6572.554180] amdgpu: Started evicting pasid 0x8002
[ 6572.554194] amdgpu: Finished evicting pasid 0x8002
[ 6583.303526] amdgpu: Started evicting pasid 0x8002
[ 6583.303540] amdgpu: Finished evicting pasid 0x8002
[ 6583.465311] amdgpu: Started evicting pasid 0x8002
[ 6583.465324] amdgpu: Finished evicting pasid 0x8002
[ 6583.623930] amdgpu: Started evicting pasid 0x8002
[ 6583.623944] amdgpu: Finished evicting pasid 0x8002
[ 6583.784489] amdgpu: Started evicting pasid 0x8002
[ 6583.784503] amdgpu: Finished evicting pasid 0x8002
[ 6583.944942] amdgpu: Started evicting pasid 0x8002
[ 6583.944955] amdgpu: Finished evicting pasid 0x8002
[ 6584.104457] amdgpu: Started evicting pasid 0x8002
[ 6584.104471] amdgpu: Finished evicting pasid 0x8002
[ 6589.945826] amdgpu: Started evicting pasid 0x8002
[ 6589.945840] amdgpu: Finished evicting pasid 0x8002
[ 6591.623620] amdgpu: Started evicting pasid 0x8002
[ 6591.623634] amdgpu: Finished evicting pasid 0x8002
[ 6591.786846] amdgpu: Started evicting pasid 0x8002
[ 6591.786860] amdgpu: Finished evicting pasid 0x8002
[ 6591.952931] amdgpu: Started evicting pasid 0x8002
[ 6591.952947] amdgpu: Finished evicting pasid 0x8002
[ 6592.120335] amdgpu: Started evicting pasid 0x8002
[ 6592.120349] amdgpu: Finished evicting pasid 0x8002
[ 6592.592450] amdgpu: Started evicting pasid 0x8002
[ 6592.592464] amdgpu: Finished evicting pasid 0x8002
[ 6592.753774] amdgpu: Started evicting pasid 0x8002
[ 6592.753788] amdgpu: Finished evicting pasid 0x8002
[ 6600.049400] amdgpu: Started evicting pasid 0x8002
[ 6600.049411] amdgpu: Finished evicting pasid 0x8002
[ 6600.152208] amdgpu: Started restoring pasid 0x8002
[ 6600.152223] amdgpu: Finished restoring pasid 0x8002
[ 6600.201403] amdgpu: Started evicting pasid 0x8002
[ 6600.201414] amdgpu: Finished evicting pasid 0x8002
[ 6600.427124] amdgpu: Started evicting pasid 0x8002
[ 6600.427138] amdgpu: Finished evicting pasid 0x8002
[ 6602.072874] amdgpu: Started evicting pasid 0x8002
[ 6602.072888] amdgpu: Finished evicting pasid 0x8002
[ 6603.821766] amdgpu: Started evicting pasid 0x8002
[ 6603.821780] amdgpu: Finished evicting pasid 0x8002
[ 6603.981812] amdgpu: Started evicting pasid 0x8002
[ 6603.981825] amdgpu: Finished evicting pasid 0x8002
[ 6604.144289] amdgpu: Started evicting pasid 0x8002
[ 6604.144302] amdgpu: Finished evicting pasid 0x8002
[ 6604.305899] amdgpu: Started evicting pasid 0x8002
[ 6604.305912] amdgpu: Finished evicting pasid 0x8002
[ 6604.495641] amdgpu: Started evicting pasid 0x8002
[ 6604.495655] amdgpu: Finished evicting pasid 0x8002
[ 6604.659761] amdgpu: Started evicting pasid 0x8002
[ 6604.659775] amdgpu: Finished evicting pasid 0x8002
[ 6604.821498] amdgpu: Started evicting pasid 0x8002
[ 6604.821512] amdgpu: Finished evicting pasid 0x8002
[ 6604.983561] amdgpu: Started evicting pasid 0x8002
[ 6604.983576] amdgpu: Finished evicting pasid 0x8002
[ 6605.144658] amdgpu: Started evicting pasid 0x8002
[ 6605.144673] amdgpu: Finished evicting pasid 0x8002
[ 6605.307416] amdgpu: Started evicting pasid 0x8002
[ 6605.307431] amdgpu: Finished evicting pasid 0x8002
[ 6605.470767] amdgpu: Started evicting pasid 0x8002
[ 6605.470781] amdgpu: Finished evicting pasid 0x8002
[ 6605.629499] amdgpu: Started evicting pasid 0x8002
[ 6605.629515] amdgpu: Finished evicting pasid 0x8002
[ 6605.791425] amdgpu: Started evicting pasid 0x8002
[ 6605.791439] amdgpu: Finished evicting pasid 0x8002
[ 6605.976987] amdgpu: Started evicting pasid 0x8002
[ 6605.977001] amdgpu: Finished evicting pasid 0x8002
[ 6606.138043] amdgpu: Started evicting pasid 0x8002
[ 6606.138057] amdgpu: Finished evicting pasid 0x8002
[ 6606.296837] amdgpu: Started evicting pasid 0x8002
[ 6606.296851] amdgpu: Finished evicting pasid 0x8002
[ 6606.457986] amdgpu: Started evicting pasid 0x8002
[ 6606.458000] amdgpu: Finished evicting pasid 0x8002
[ 6606.619333] amdgpu: Started evicting pasid 0x8002
[ 6606.619347] amdgpu: Finished evicting pasid 0x8002
[ 6606.780485] amdgpu: Started evicting pasid 0x8002
[ 6606.780499] amdgpu: Finished evicting pasid 0x8002
[ 6606.944153] amdgpu: Started evicting pasid 0x8002
[ 6606.944167] amdgpu: Finished evicting pasid 0x8002
[ 6607.105153] amdgpu: Started evicting pasid 0x8002
[ 6607.105168] amdgpu: Finished evicting pasid 0x8002
[ 6607.266065] amdgpu: Started evicting pasid 0x8002
[ 6607.266079] amdgpu: Finished evicting pasid 0x8002
[ 6607.427560] amdgpu: Started evicting pasid 0x8002
[ 6607.427574] amdgpu: Finished evicting pasid 0x8002
[ 6607.589898] amdgpu: Started evicting pasid 0x8002
[ 6607.589912] amdgpu: Finished evicting pasid 0x8002
[ 6607.751233] amdgpu: Started evicting pasid 0x8002
[ 6607.751247] amdgpu: Finished evicting pasid 0x8002
[ 6607.912488] amdgpu: Started evicting pasid 0x8002
[ 6607.912501] amdgpu: Finished evicting pasid 0x8002
[ 6608.077826] amdgpu: Started evicting pasid 0x8002
[ 6608.077839] amdgpu: Finished evicting pasid 0x8002
[ 6608.240610] amdgpu: Started evicting pasid 0x8002
[ 6608.240629] amdgpu: Finished evicting pasid 0x8002
[ 6608.423171] amdgpu: Started evicting pasid 0x8002
[ 6608.423186] amdgpu: Finished evicting pasid 0x8002
[ 6608.610407] amdgpu: Started evicting pasid 0x8002
[ 6608.610422] amdgpu: Finished evicting pasid 0x8002
[ 6608.771495] amdgpu: Started evicting pasid 0x8002
[ 6608.771509] amdgpu: Finished evicting pasid 0x8002
[ 6608.933612] amdgpu: Started evicting pasid 0x8002
[ 6608.933626] amdgpu: Finished evicting pasid 0x8002
[ 6609.095397] amdgpu: Started evicting pasid 0x8002
[ 6609.095411] amdgpu: Finished evicting pasid 0x8002
[ 6609.257660] amdgpu: Started evicting pasid 0x8002
[ 6609.257673] amdgpu: Finished evicting pasid 0x8002
[ 6609.419637] amdgpu: Started evicting pasid 0x8002
[ 6609.419652] amdgpu: Finished evicting pasid 0x8002
[ 6609.581906] amdgpu: Started evicting pasid 0x8002
[ 6609.581921] amdgpu: Finished evicting pasid 0x8002
[ 6609.743540] amdgpu: Started evicting pasid 0x8002
[ 6609.743554] amdgpu: Finished evicting pasid 0x8002
[ 6609.905054] amdgpu: Started evicting pasid 0x8002
[ 6609.905067] amdgpu: Finished evicting pasid 0x8002
[ 6610.066930] amdgpu: Started evicting pasid 0x8002
[ 6610.066946] amdgpu: Finished evicting pasid 0x8002
[ 6610.228558] amdgpu: Started evicting pasid 0x8002
[ 6610.228572] amdgpu: Finished evicting pasid 0x8002
[ 6610.390110] amdgpu: Started evicting pasid 0x8002
[ 6610.390124] amdgpu: Finished evicting pasid 0x8002
[ 6610.551944] amdgpu: Started evicting pasid 0x8002
[ 6610.551957] amdgpu: Finished evicting pasid 0x8002
[ 6610.718610] amdgpu: Started evicting pasid 0x8002
[ 6610.718624] amdgpu: Finished evicting pasid 0x8002
[ 6610.876721] amdgpu: Started evicting pasid 0x8002
[ 6610.876735] amdgpu: Finished evicting pasid 0x8002
[ 6611.036730] amdgpu: Started evicting pasid 0x8002
[ 6611.036743] amdgpu: Finished evicting pasid 0x8002
[ 6611.199438] amdgpu: Started evicting pasid 0x8002
[ 6611.199452] amdgpu: Finished evicting pasid 0x8002
[ 6611.736874] amdgpu: Started evicting pasid 0x8002
[ 6611.736888] amdgpu: Finished evicting pasid 0x8002
[ 6611.897750] amdgpu: Started evicting pasid 0x8002
[ 6611.897763] amdgpu: Finished evicting pasid 0x8002
[ 6612.059388] amdgpu: Started evicting pasid 0x8002
[ 6612.059403] amdgpu: Finished evicting pasid 0x8002
[ 6612.221449] amdgpu: Started evicting pasid 0x8002
[ 6612.221462] amdgpu: Finished evicting pasid 0x8002
[ 6612.383653] amdgpu: Started evicting pasid 0x8002
[ 6612.383667] amdgpu: Finished evicting pasid 0x8002
[ 6612.545774] amdgpu: Started evicting pasid 0x8002
[ 6612.545787] amdgpu: Finished evicting pasid 0x8002
[ 6612.707075] amdgpu: Started evicting pasid 0x8002
[ 6612.707089] amdgpu: Finished evicting pasid 0x8002
[ 6612.870340] amdgpu: Started evicting pasid 0x8002
[ 6612.870354] amdgpu: Finished evicting pasid 0x8002
[ 6613.031582] amdgpu: Started evicting pasid 0x8002
[ 6613.031596] amdgpu: Finished evicting pasid 0x8002
[ 6613.194408] amdgpu: Started evicting pasid 0x8002
[ 6613.194421] amdgpu: Finished evicting pasid 0x8002
[ 6613.358690] amdgpu: Started evicting pasid 0x8002
[ 6613.358704] amdgpu: Finished evicting pasid 0x8002
[ 6613.517667] amdgpu: Started evicting pasid 0x8002
[ 6613.517681] amdgpu: Finished evicting pasid 0x8002
[ 6613.678947] amdgpu: Started evicting pasid 0x8002
[ 6613.678972] amdgpu: Finished evicting pasid 0x8002
[ 6613.840882] amdgpu: Started evicting pasid 0x8002
[ 6613.840896] amdgpu: Finished evicting pasid 0x8002
[ 6614.002776] amdgpu: Started evicting pasid 0x8002
[ 6614.002789] amdgpu: Finished evicting pasid 0x8002
[ 6614.163719] amdgpu: Started evicting pasid 0x8002
[ 6614.163732] amdgpu: Finished evicting pasid 0x8002
[ 6614.326489] amdgpu: Started evicting pasid 0x8002
[ 6614.326503] amdgpu: Finished evicting pasid 0x8002
[ 6614.487521] amdgpu: Started evicting pasid 0x8002
[ 6614.487535] amdgpu: Finished evicting pasid 0x8002
[ 6614.649670] amdgpu: Started evicting pasid 0x8002
[ 6614.649683] amdgpu: Finished evicting pasid 0x8002
[ 6614.810405] amdgpu: Started evicting pasid 0x8002
[ 6614.810418] amdgpu: Finished evicting pasid 0x8002
[ 6614.971242] amdgpu: Started evicting pasid 0x8002
[ 6614.971256] amdgpu: Finished evicting pasid 0x8002
[ 6615.135493] amdgpu: Started evicting pasid 0x8002
[ 6615.135506] amdgpu: Finished evicting pasid 0x8002
[ 6615.296480] amdgpu: Started evicting pasid 0x8002
[ 6615.296493] amdgpu: Finished evicting pasid 0x8002
[ 6615.458303] amdgpu: Started evicting pasid 0x8002
[ 6615.458316] amdgpu: Finished evicting pasid 0x8002
[ 6615.622700] amdgpu: Started evicting pasid 0x8002
[ 6615.622715] amdgpu: Finished evicting pasid 0x8002
[ 6615.783281] amdgpu: Started evicting pasid 0x8002
[ 6615.783295] amdgpu: Finished evicting pasid 0x8002
[ 6615.949804] amdgpu: Started evicting pasid 0x8002
[ 6615.949818] amdgpu: Finished evicting pasid 0x8002
[ 6616.107847] amdgpu: Started evicting pasid 0x8002
[ 6616.107868] amdgpu: Finished evicting pasid 0x8002
[ 6616.267253] amdgpu: Started evicting pasid 0x8002
[ 6616.267266] amdgpu: Finished evicting pasid 0x8002
[ 6616.429217] amdgpu: Started evicting pasid 0x8002
[ 6616.429231] amdgpu: Finished evicting pasid 0x8002
[ 6616.590535] amdgpu: Started evicting pasid 0x8002
[ 6616.590549] amdgpu: Finished evicting pasid 0x8002
[ 6616.751257] amdgpu: Started evicting pasid 0x8002
[ 6616.751271] amdgpu: Finished evicting pasid 0x8002
[ 6616.913873] amdgpu: Started evicting pasid 0x8002
[ 6616.913886] amdgpu: Finished evicting pasid 0x8002
[ 6617.076458] amdgpu: Started evicting pasid 0x8002
[ 6617.076472] amdgpu: Finished evicting pasid 0x8002
[ 6617.238755] amdgpu: Started evicting pasid 0x8002
[ 6617.238768] amdgpu: Finished evicting pasid 0x8002
[ 6617.806415] amdgpu: Started evicting pasid 0x8002
[ 6617.806429] amdgpu: Finished evicting pasid 0x8002
[ 6618.717325] amdgpu: Started evicting pasid 0x8002
[ 6618.717339] amdgpu: Finished evicting pasid 0x8002
[ 6618.937575] amdgpu: Started evicting pasid 0x8002
[ 6618.937588] amdgpu: Finished evicting pasid 0x8002
[ 6619.099107] amdgpu: Started evicting pasid 0x8002
[ 6619.099122] amdgpu: Finished evicting pasid 0x8002
[ 6619.260730] amdgpu: Started evicting pasid 0x8002
[ 6619.260743] amdgpu: Finished evicting pasid 0x8002
[ 6619.422823] amdgpu: Started evicting pasid 0x8002
[ 6619.422835] amdgpu: Finished evicting pasid 0x8002
[ 6619.585098] amdgpu: Started evicting pasid 0x8002
[ 6619.585112] amdgpu: Finished evicting pasid 0x8002
[ 6620.100063] amdgpu: Started evicting pasid 0x8002
[ 6620.100077] amdgpu: Finished evicting pasid 0x8002
[ 6621.805159] amdgpu: Started evicting pasid 0x8002
[ 6621.805173] amdgpu: Finished evicting pasid 0x8002
[ 6621.965345] amdgpu: Started evicting pasid 0x8002
[ 6621.965359] amdgpu: Finished evicting pasid 0x8002
[ 6622.123589] amdgpu: Started evicting pasid 0x8002
[ 6622.123603] amdgpu: Finished evicting pasid 0x8002
[ 6622.283849] amdgpu: Started evicting pasid 0x8002
[ 6622.283862] amdgpu: Finished evicting pasid 0x8002
[ 6622.444725] amdgpu: Started evicting pasid 0x8002
[ 6622.444739] amdgpu: Finished evicting pasid 0x8002
[ 6623.173440] amdgpu: Started evicting pasid 0x8002
[ 6623.173454] amdgpu: Finished evicting pasid 0x8002
[ 6623.335349] amdgpu: Started evicting pasid 0x8002
[ 6623.335362] amdgpu: Finished evicting pasid 0x8002
[ 6623.495860] amdgpu: Started evicting pasid 0x8002
[ 6623.495873] amdgpu: Finished evicting pasid 0x8002
[ 6623.661652] amdgpu: Started evicting pasid 0x8002
[ 6623.661666] amdgpu: Finished evicting pasid 0x8002
[ 6623.670615] amdgpu: Started evicting pasid 0x8003
[ 6623.670628] amdgpu: Finished evicting pasid 0x8003
[ 6623.846186] amdgpu: Started evicting pasid 0x8002
[ 6623.846201] amdgpu: Finished evicting pasid 0x8002
[ 6623.986949] amdgpu: Started evicting pasid 0x8002
[ 6623.986963] amdgpu: Finished evicting pasid 0x8002
[ 6624.157358] amdgpu: Started evicting pasid 0x8002
[ 6624.157372] amdgpu: Finished evicting pasid 0x8002
[ 6624.296441] amdgpu: Started evicting pasid 0x8002
[ 6624.296454] amdgpu: Finished evicting pasid 0x8002
[ 6624.458639] amdgpu: Started evicting pasid 0x8002
[ 6624.458653] amdgpu: Finished evicting pasid 0x8002
[ 6624.621515] amdgpu: Started evicting pasid 0x8002
[ 6624.621527] amdgpu: Finished evicting pasid 0x8002
[ 6624.783413] amdgpu: Started evicting pasid 0x8002
[ 6624.783427] amdgpu: Finished evicting pasid 0x8002
[ 6624.945557] amdgpu: Started evicting pasid 0x8002
[ 6624.945571] amdgpu: Finished evicting pasid 0x8002
[ 6625.107331] amdgpu: Started evicting pasid 0x8002
[ 6625.107345] amdgpu: Finished evicting pasid 0x8002
[ 6625.269558] amdgpu: Started evicting pasid 0x8002
[ 6625.269571] amdgpu: Finished evicting pasid 0x8002
[ 6625.497816] amdgpu: Started evicting pasid 0x8002
[ 6625.497829] amdgpu: Finished evicting pasid 0x8002
[ 6625.662990] amdgpu: Started evicting pasid 0x8002
[ 6625.663003] amdgpu: Finished evicting pasid 0x8002
[ 6625.824745] amdgpu: Started evicting pasid 0x8002
[ 6625.824758] amdgpu: Finished evicting pasid 0x8002
[ 6625.986783] amdgpu: Started evicting pasid 0x8002
[ 6625.986801] amdgpu: Finished evicting pasid 0x8002
[ 6626.148470] amdgpu: Started evicting pasid 0x8002
[ 6626.148484] amdgpu: Finished evicting pasid 0x8002
[ 6626.660502] amdgpu: Started evicting pasid 0x8002
[ 6626.660515] amdgpu: Finished evicting pasid 0x8002
[ 6626.821176] amdgpu: Started evicting pasid 0x8002
[ 6626.821190] amdgpu: Finished evicting pasid 0x8002
[ 6626.979745] amdgpu: Started evicting pasid 0x8002
[ 6626.979760] amdgpu: Finished evicting pasid 0x8002
[ 6627.139990] amdgpu: Started evicting pasid 0x8002
[ 6627.140004] amdgpu: Finished evicting pasid 0x8002
[ 6627.302718] amdgpu: Started evicting pasid 0x8002
[ 6627.302731] amdgpu: Finished evicting pasid 0x8002
[ 6627.472829] amdgpu: Started evicting pasid 0x8002
[ 6627.472849] amdgpu: Finished evicting pasid 0x8002
[ 6627.633949] amdgpu: Started evicting pasid 0x8002
[ 6627.633963] amdgpu: Finished evicting pasid 0x8002
[ 6627.797216] amdgpu: Started evicting pasid 0x8002
[ 6627.797229] amdgpu: Finished evicting pasid 0x8002
[ 6628.273761] amdgpu: Started evicting pasid 0x8002
[ 6628.273826] amdgpu: Finished evicting pasid 0x8002
[ 6629.846271] amdgpu: Started evicting pasid 0x8002
[ 6629.846337] amdgpu: Finished evicting pasid 0x8002
[ 6632.194235] amdgpu: Started evicting pasid 0x8002
[ 6632.194250] amdgpu: Finished evicting pasid 0x8002
[ 6632.685226] amdgpu: Started evicting pasid 0x8002
[ 6632.685239] amdgpu: Finished evicting pasid 0x8002
[ 6633.249315] gmc_v9_0_process_interrupt: 26 callbacks suppressed
[ 6633.249320] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249323] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282600000 from client 18
[ 6633.249324] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6633.249325] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249326] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6633.249327] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249328] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6633.249329] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249330] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6633.249342] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249343] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282601000 from client 18
[ 6633.249344] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6633.249345] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249346] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6633.249347] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249348] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6633.249349] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249349] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6633.249353] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249354] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282602000 from client 18
[ 6633.249355] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 6633.249356] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249357] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 6633.249358] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249358] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 6633.249359] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249360] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 6633.249363] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249364] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282603000 from client 18
[ 6633.249365] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249366] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249367] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249368] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249369] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249370] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249371] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249374] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249375] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282604000 from client 18
[ 6633.249376] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249377] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249377] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249378] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249379] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249380] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249381] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249384] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249385] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282605000 from client 18
[ 6633.249386] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249387] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249388] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249389] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249390] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249391] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249392] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249395] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249396] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282606000 from client 18
[ 6633.249397] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249398] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249399] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249399] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249400] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249401] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249402] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249407] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249408] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282607000 from client 18
[ 6633.249409] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249410] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249411] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249411] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249412] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249413] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249414] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249418] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249420] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282608000 from client 18
[ 6633.249420] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249421] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249422] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249423] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249424] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249425] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249426] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.249431] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 65404 thread hipMemsetAsyncM pid 65404)
[ 6633.249432] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2282600000 from client 18
[ 6633.249433] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 6633.249434] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 6633.249435] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 6633.249436] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 6633.249437] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 6633.249438] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 6633.249438] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 6633.334567] amdgpu: Started evicting pasid 0x8002
[ 6633.334573] amdgpu: Finished evicting pasid 0x8002
[ 6633.828425] amdgpu: Started evicting pasid 0x8002
[ 6633.828433] amdgpu: Finished evicting pasid 0x8002
[ 6633.988325] amdgpu: Started evicting pasid 0x8002
[ 6633.988338] amdgpu: Finished evicting pasid 0x8002
[ 6634.802179] amdgpu: Started evicting pasid 0x8002
[ 6634.802194] amdgpu: Finished evicting pasid 0x8002
[ 6634.969829] amdgpu: Started evicting pasid 0x8002
[ 6634.969843] amdgpu: Finished evicting pasid 0x8002
[ 6635.134497] amdgpu: Started evicting pasid 0x8002
[ 6635.134510] amdgpu: Finished evicting pasid 0x8002
[ 6635.364602] amdgpu: Started evicting pasid 0x8002
[ 6635.364615] amdgpu: Finished evicting pasid 0x8002
[ 6635.758684] amdgpu: Started evicting pasid 0x8002
[ 6635.758743] amdgpu: Finished evicting pasid 0x8002
[ 6636.163621] amdgpu: Started evicting pasid 0x8002
[ 6636.163676] amdgpu: Finished evicting pasid 0x8002
[ 6636.574801] amdgpu: Started evicting pasid 0x8002
[ 6636.574861] amdgpu: Finished evicting pasid 0x8002
[ 6637.013361] amdgpu: Started evicting pasid 0x8002
[ 6637.013419] amdgpu: Finished evicting pasid 0x8002
[ 6637.481280] amdgpu: Started evicting pasid 0x8002
[ 6637.481330] amdgpu: Finished evicting pasid 0x8002
[ 6637.954355] amdgpu: Started evicting pasid 0x8002
[ 6637.954410] amdgpu: Finished evicting pasid 0x8002
[ 6638.426867] amdgpu: Started evicting pasid 0x8002
[ 6638.426913] amdgpu: Finished evicting pasid 0x8002
[ 6638.603006] amdgpu: Started evicting pasid 0x8002
[ 6638.603020] amdgpu: Finished evicting pasid 0x8002
[ 6638.764156] amdgpu: Started evicting pasid 0x8002
[ 6638.764170] amdgpu: Finished evicting pasid 0x8002
[ 6638.925875] amdgpu: Started evicting pasid 0x8002
[ 6638.925888] amdgpu: Finished evicting pasid 0x8002
[ 6639.487022] amdgpu: Started evicting pasid 0x8002
[ 6639.487036] amdgpu: Finished evicting pasid 0x8002
[ 6639.657494] amdgpu: Started evicting pasid 0x8002
[ 6639.657508] amdgpu: Finished evicting pasid 0x8002
[ 6639.820809] amdgpu: Started evicting pasid 0x8002
[ 6639.820823] amdgpu: Finished evicting pasid 0x8002
[ 6639.985563] amdgpu: Started evicting pasid 0x8002
[ 6639.985577] amdgpu: Finished evicting pasid 0x8002
[ 6640.151076] amdgpu: Started evicting pasid 0x8002
[ 6640.151091] amdgpu: Finished evicting pasid 0x8002
[ 6640.310056] amdgpu: Started evicting pasid 0x8002
[ 6640.310070] amdgpu: Finished evicting pasid 0x8002
[ 6640.541513] amdgpu: Started evicting pasid 0x8002
[ 6640.541527] amdgpu: Finished evicting pasid 0x8002
[ 6640.702515] amdgpu: Started evicting pasid 0x8002
[ 6640.702529] amdgpu: Finished evicting pasid 0x8002
[ 6674.397619] amdgpu: Started evicting pasid 0x8002
[ 6674.397634] amdgpu: Finished evicting pasid 0x8002
[ 6674.559512] amdgpu: Started evicting pasid 0x8002
[ 6674.559526] amdgpu: Finished evicting pasid 0x8002
[ 6674.721678] amdgpu: Started evicting pasid 0x8002
[ 6674.721692] amdgpu: Finished evicting pasid 0x8002
[ 6674.882861] amdgpu: Started evicting pasid 0x8002
[ 6674.882875] amdgpu: Finished evicting pasid 0x8002
[ 6675.046730] amdgpu: Started evicting pasid 0x8002
[ 6675.046744] amdgpu: Finished evicting pasid 0x8002
[ 6675.214025] amdgpu: Started evicting pasid 0x8002
[ 6675.214039] amdgpu: Finished evicting pasid 0x8002
[ 6675.377608] amdgpu: Started evicting pasid 0x8002
[ 6675.377621] amdgpu: Finished evicting pasid 0x8002
[ 6675.540093] amdgpu: Started evicting pasid 0x8002
[ 6675.540107] amdgpu: Finished evicting pasid 0x8002
[ 6686.282409] amdgpu: Started evicting pasid 0x8002
[ 6686.282422] amdgpu: Finished evicting pasid 0x8002
[ 6686.442198] amdgpu: Started evicting pasid 0x8002
[ 6686.442212] amdgpu: Finished evicting pasid 0x8002
[ 6686.603250] amdgpu: Started evicting pasid 0x8002
[ 6686.603265] amdgpu: Finished evicting pasid 0x8002
[ 6686.764585] amdgpu: Started evicting pasid 0x8002
[ 6686.764599] amdgpu: Finished evicting pasid 0x8002
[ 6686.925187] amdgpu: Started evicting pasid 0x8002
[ 6686.925201] amdgpu: Finished evicting pasid 0x8002
[ 6687.091688] amdgpu: Started evicting pasid 0x8002
[ 6687.091702] amdgpu: Finished evicting pasid 0x8002
[ 6692.906885] amdgpu: Started evicting pasid 0x8002
[ 6692.906900] amdgpu: Finished evicting pasid 0x8002
[ 6694.555977] amdgpu: Started evicting pasid 0x8002
[ 6694.555991] amdgpu: Finished evicting pasid 0x8002
[ 6694.714775] amdgpu: Started evicting pasid 0x8002
[ 6694.714789] amdgpu: Finished evicting pasid 0x8002
[ 6694.875990] amdgpu: Started evicting pasid 0x8002
[ 6694.876004] amdgpu: Finished evicting pasid 0x8002
[ 6695.042043] amdgpu: Started evicting pasid 0x8002
[ 6695.042057] amdgpu: Finished evicting pasid 0x8002
[ 6695.509098] amdgpu: Started evicting pasid 0x8002
[ 6695.509112] amdgpu: Finished evicting pasid 0x8002
[ 6695.672717] amdgpu: Started evicting pasid 0x8002
[ 6695.672730] amdgpu: Finished evicting pasid 0x8002
[ 8082.585262] amdgpu: Started evicting pasid 0x8002
[ 8082.585272] amdgpu: Finished evicting pasid 0x8002
[ 8082.691101] amdgpu: Started restoring pasid 0x8002
[ 8082.691127] amdgpu: Finished restoring pasid 0x8002
[ 8082.732479] amdgpu: Started evicting pasid 0x8002
[ 8082.732490] amdgpu: Finished evicting pasid 0x8002
[ 8082.961796] amdgpu: Started evicting pasid 0x8002
[ 8082.961810] amdgpu: Finished evicting pasid 0x8002
[ 8084.616576] amdgpu: Started evicting pasid 0x8002
[ 8084.616590] amdgpu: Finished evicting pasid 0x8002
[ 8086.351384] amdgpu: Started evicting pasid 0x8002
[ 8086.351398] amdgpu: Finished evicting pasid 0x8002
[ 8086.515503] amdgpu: Started evicting pasid 0x8002
[ 8086.515527] amdgpu: Finished evicting pasid 0x8002
[ 8086.680421] amdgpu: Started evicting pasid 0x8002
[ 8086.680434] amdgpu: Finished evicting pasid 0x8002
[ 8086.839720] amdgpu: Started evicting pasid 0x8002
[ 8086.839735] amdgpu: Finished evicting pasid 0x8002
[ 8087.034649] amdgpu: Started evicting pasid 0x8002
[ 8087.034662] amdgpu: Finished evicting pasid 0x8002
[ 8087.204488] amdgpu: Started evicting pasid 0x8002
[ 8087.204503] amdgpu: Finished evicting pasid 0x8002
[ 8087.367123] amdgpu: Started evicting pasid 0x8002
[ 8087.367137] amdgpu: Finished evicting pasid 0x8002
[ 8087.527875] amdgpu: Started evicting pasid 0x8002
[ 8087.527888] amdgpu: Finished evicting pasid 0x8002
[ 8087.689644] amdgpu: Started evicting pasid 0x8002
[ 8087.689657] amdgpu: Finished evicting pasid 0x8002
[ 8087.850222] amdgpu: Started evicting pasid 0x8002
[ 8087.850237] amdgpu: Finished evicting pasid 0x8002
[ 8088.012783] amdgpu: Started evicting pasid 0x8002
[ 8088.012797] amdgpu: Finished evicting pasid 0x8002
[ 8088.173710] amdgpu: Started evicting pasid 0x8002
[ 8088.173724] amdgpu: Finished evicting pasid 0x8002
[ 8088.333452] amdgpu: Started evicting pasid 0x8002
[ 8088.333465] amdgpu: Finished evicting pasid 0x8002
[ 8088.511686] amdgpu: Started evicting pasid 0x8002
[ 8088.511700] amdgpu: Finished evicting pasid 0x8002
[ 8088.679463] amdgpu: Started evicting pasid 0x8002
[ 8088.679477] amdgpu: Finished evicting pasid 0x8002
[ 8088.841962] amdgpu: Started evicting pasid 0x8002
[ 8088.841976] amdgpu: Finished evicting pasid 0x8002
[ 8089.002355] amdgpu: Started evicting pasid 0x8002
[ 8089.002369] amdgpu: Finished evicting pasid 0x8002
[ 8089.163211] amdgpu: Started evicting pasid 0x8002
[ 8089.163225] amdgpu: Finished evicting pasid 0x8002
[ 8089.327858] amdgpu: Started evicting pasid 0x8002
[ 8089.327872] amdgpu: Finished evicting pasid 0x8002
[ 8089.498736] amdgpu: Started evicting pasid 0x8002
[ 8089.498750] amdgpu: Finished evicting pasid 0x8002
[ 8089.666642] amdgpu: Started evicting pasid 0x8002

---

### 评论 #7 — dshm (2021-03-02T07:44:16Z)

[ 8089.666657] amdgpu: Finished evicting pasid 0x8002
[ 8089.831543] amdgpu: Started evicting pasid 0x8002
[ 8089.831558] amdgpu: Finished evicting pasid 0x8002
[ 8089.994775] amdgpu: Started evicting pasid 0x8002
[ 8089.994790] amdgpu: Finished evicting pasid 0x8002
[ 8090.158452] amdgpu: Started evicting pasid 0x8002
[ 8090.158466] amdgpu: Finished evicting pasid 0x8002
[ 8090.327760] amdgpu: Started evicting pasid 0x8002
[ 8090.327774] amdgpu: Finished evicting pasid 0x8002
[ 8090.491021] amdgpu: Started evicting pasid 0x8002
[ 8090.491036] amdgpu: Finished evicting pasid 0x8002
[ 8090.657542] amdgpu: Started evicting pasid 0x8002
[ 8090.657555] amdgpu: Finished evicting pasid 0x8002
[ 8090.816211] amdgpu: Started evicting pasid 0x8002
[ 8090.816232] amdgpu: Finished evicting pasid 0x8002
[ 8091.008617] amdgpu: Started evicting pasid 0x8002
[ 8091.008632] amdgpu: Finished evicting pasid 0x8002
[ 8091.197615] amdgpu: Started evicting pasid 0x8002
[ 8091.197628] amdgpu: Finished evicting pasid 0x8002
[ 8091.358878] amdgpu: Started evicting pasid 0x8002
[ 8091.358892] amdgpu: Finished evicting pasid 0x8002
[ 8091.520163] amdgpu: Started evicting pasid 0x8002
[ 8091.520177] amdgpu: Finished evicting pasid 0x8002
[ 8091.682174] amdgpu: Started evicting pasid 0x8002
[ 8091.682188] amdgpu: Finished evicting pasid 0x8002
[ 8091.843575] amdgpu: Started evicting pasid 0x8002
[ 8091.843588] amdgpu: Finished evicting pasid 0x8002
[ 8092.005586] amdgpu: Started evicting pasid 0x8002
[ 8092.005601] amdgpu: Finished evicting pasid 0x8002
[ 8092.167631] amdgpu: Started evicting pasid 0x8002
[ 8092.167645] amdgpu: Finished evicting pasid 0x8002
[ 8092.331978] amdgpu: Started evicting pasid 0x8002
[ 8092.331993] amdgpu: Finished evicting pasid 0x8002
[ 8092.490908] amdgpu: Started evicting pasid 0x8002
[ 8092.490922] amdgpu: Finished evicting pasid 0x8002
[ 8092.652110] amdgpu: Started evicting pasid 0x8002
[ 8092.652124] amdgpu: Finished evicting pasid 0x8002
[ 8092.812828] amdgpu: Started evicting pasid 0x8002
[ 8092.812843] amdgpu: Finished evicting pasid 0x8002
[ 8092.974351] amdgpu: Started evicting pasid 0x8002
[ 8092.974364] amdgpu: Finished evicting pasid 0x8002
[ 8093.135015] amdgpu: Started evicting pasid 0x8002
[ 8093.135029] amdgpu: Finished evicting pasid 0x8002
[ 8093.297573] amdgpu: Started evicting pasid 0x8002
[ 8093.297588] amdgpu: Finished evicting pasid 0x8002
[ 8093.459760] amdgpu: Started evicting pasid 0x8002
[ 8093.459774] amdgpu: Finished evicting pasid 0x8002
[ 8093.621960] amdgpu: Started evicting pasid 0x8002
[ 8093.621974] amdgpu: Finished evicting pasid 0x8002
[ 8093.782750] amdgpu: Started evicting pasid 0x8002
[ 8093.782771] amdgpu: Finished evicting pasid 0x8002
[ 8094.329323] amdgpu: Started evicting pasid 0x8002
[ 8094.329336] amdgpu: Finished evicting pasid 0x8002
[ 8094.492794] amdgpu: Started evicting pasid 0x8002
[ 8094.492807] amdgpu: Finished evicting pasid 0x8002
[ 8094.654648] amdgpu: Started evicting pasid 0x8002
[ 8094.654663] amdgpu: Finished evicting pasid 0x8002
[ 8094.818638] amdgpu: Started evicting pasid 0x8002
[ 8094.818651] amdgpu: Finished evicting pasid 0x8002
[ 8094.990461] amdgpu: Started evicting pasid 0x8002
[ 8094.990475] amdgpu: Finished evicting pasid 0x8002
[ 8095.157526] amdgpu: Started evicting pasid 0x8002
[ 8095.157540] amdgpu: Finished evicting pasid 0x8002
[ 8095.320209] amdgpu: Started evicting pasid 0x8002
[ 8095.320223] amdgpu: Finished evicting pasid 0x8002
[ 8095.480229] amdgpu: Started evicting pasid 0x8002
[ 8095.480243] amdgpu: Finished evicting pasid 0x8002
[ 8095.641150] amdgpu: Started evicting pasid 0x8002
[ 8095.641164] amdgpu: Finished evicting pasid 0x8002
[ 8095.800811] amdgpu: Started evicting pasid 0x8002
[ 8095.800825] amdgpu: Finished evicting pasid 0x8002
[ 8095.961870] amdgpu: Started evicting pasid 0x8002
[ 8095.961895] amdgpu: Finished evicting pasid 0x8002
[ 8096.127259] amdgpu: Started evicting pasid 0x8002
[ 8096.127272] amdgpu: Finished evicting pasid 0x8002
[ 8098.113172] amdgpu: Started evicting pasid 0x8002
[ 8098.113183] amdgpu: Finished evicting pasid 0x8002
[ 8098.213757] amdgpu: Started restoring pasid 0x8002
[ 8098.213772] amdgpu: Finished restoring pasid 0x8002
[ 8098.266946] amdgpu: Started evicting pasid 0x8002
[ 8098.266957] amdgpu: Finished evicting pasid 0x8002
[ 8098.494504] amdgpu: Started evicting pasid 0x8002
[ 8098.494518] amdgpu: Finished evicting pasid 0x8002
[ 8100.134253] amdgpu: Started evicting pasid 0x8002
[ 8100.134268] amdgpu: Finished evicting pasid 0x8002
[ 8101.889448] amdgpu: Started evicting pasid 0x8002
[ 8101.889462] amdgpu: Finished evicting pasid 0x8002
[ 8102.053208] amdgpu: Started evicting pasid 0x8002
[ 8102.053223] amdgpu: Finished evicting pasid 0x8002
[ 8102.214466] amdgpu: Started evicting pasid 0x8002
[ 8102.214481] amdgpu: Finished evicting pasid 0x8002
[ 8102.376670] amdgpu: Started evicting pasid 0x8002
[ 8102.376684] amdgpu: Finished evicting pasid 0x8002
[ 8102.568104] amdgpu: Started evicting pasid 0x8002
[ 8102.568119] amdgpu: Finished evicting pasid 0x8002
[ 8102.728575] amdgpu: Started evicting pasid 0x8002
[ 8102.728589] amdgpu: Finished evicting pasid 0x8002
[ 8102.894646] amdgpu: Started evicting pasid 0x8002
[ 8102.894661] amdgpu: Finished evicting pasid 0x8002
[ 8103.053333] amdgpu: Started evicting pasid 0x8002
[ 8103.053347] amdgpu: Finished evicting pasid 0x8002
[ 8103.214879] amdgpu: Started evicting pasid 0x8002
[ 8103.214894] amdgpu: Finished evicting pasid 0x8002
[ 8103.376138] amdgpu: Started evicting pasid 0x8002
[ 8103.376151] amdgpu: Finished evicting pasid 0x8002
[ 8103.538581] amdgpu: Started evicting pasid 0x8002
[ 8103.538595] amdgpu: Finished evicting pasid 0x8002
[ 8103.702247] amdgpu: Started evicting pasid 0x8002
[ 8103.702261] amdgpu: Finished evicting pasid 0x8002
[ 8103.869382] amdgpu: Started evicting pasid 0x8002
[ 8103.869396] amdgpu: Finished evicting pasid 0x8002
[ 8104.064120] amdgpu: Started evicting pasid 0x8002
[ 8104.064134] amdgpu: Finished evicting pasid 0x8002
[ 8104.226113] amdgpu: Started evicting pasid 0x8002
[ 8104.226127] amdgpu: Finished evicting pasid 0x8002
[ 8104.390458] amdgpu: Started evicting pasid 0x8002
[ 8104.390472] amdgpu: Finished evicting pasid 0x8002
[ 8104.558699] amdgpu: Started evicting pasid 0x8002
[ 8104.558713] amdgpu: Finished evicting pasid 0x8002
[ 8104.722097] amdgpu: Started evicting pasid 0x8002
[ 8104.722112] amdgpu: Finished evicting pasid 0x8002
[ 8104.886211] amdgpu: Started evicting pasid 0x8002
[ 8104.886225] amdgpu: Finished evicting pasid 0x8002
[ 8105.045838] amdgpu: Started evicting pasid 0x8002
[ 8105.045851] amdgpu: Finished evicting pasid 0x8002
[ 8105.206215] amdgpu: Started evicting pasid 0x8002
[ 8105.206229] amdgpu: Finished evicting pasid 0x8002
[ 8105.370362] amdgpu: Started evicting pasid 0x8002
[ 8105.370376] amdgpu: Finished evicting pasid 0x8002
[ 8105.534711] amdgpu: Started evicting pasid 0x8002
[ 8105.534733] amdgpu: Finished evicting pasid 0x8002
[ 8105.702373] amdgpu: Started evicting pasid 0x8002
[ 8105.702388] amdgpu: Finished evicting pasid 0x8002
[ 8105.863008] amdgpu: Started evicting pasid 0x8002
[ 8105.863022] amdgpu: Finished evicting pasid 0x8002
[ 8106.023284] amdgpu: Started evicting pasid 0x8002
[ 8106.023298] amdgpu: Finished evicting pasid 0x8002
[ 8106.186579] amdgpu: Started evicting pasid 0x8002
[ 8106.186593] amdgpu: Finished evicting pasid 0x8002
[ 8106.348620] amdgpu: Started evicting pasid 0x8002
[ 8106.348635] amdgpu: Finished evicting pasid 0x8002
[ 8106.539675] amdgpu: Started evicting pasid 0x8002
[ 8106.539689] amdgpu: Finished evicting pasid 0x8002
[ 8106.733020] amdgpu: Started evicting pasid 0x8002
[ 8106.733034] amdgpu: Finished evicting pasid 0x8002
[ 8106.895098] amdgpu: Started evicting pasid 0x8002
[ 8106.895112] amdgpu: Finished evicting pasid 0x8002
[ 8107.055997] amdgpu: Started evicting pasid 0x8002
[ 8107.056011] amdgpu: Finished evicting pasid 0x8002
[ 8107.216327] amdgpu: Started evicting pasid 0x8002
[ 8107.216341] amdgpu: Finished evicting pasid 0x8002
[ 8107.377553] amdgpu: Started evicting pasid 0x8002
[ 8107.377566] amdgpu: Finished evicting pasid 0x8002
[ 8107.540440] amdgpu: Started evicting pasid 0x8002
[ 8107.540454] amdgpu: Finished evicting pasid 0x8002
[ 8107.702672] amdgpu: Started evicting pasid 0x8002
[ 8107.702686] amdgpu: Finished evicting pasid 0x8002
[ 8107.873706] amdgpu: Started evicting pasid 0x8002
[ 8107.873720] amdgpu: Finished evicting pasid 0x8002
[ 8108.036084] amdgpu: Started evicting pasid 0x8002
[ 8108.036099] amdgpu: Finished evicting pasid 0x8002
[ 8108.200164] amdgpu: Started evicting pasid 0x8002
[ 8108.200178] amdgpu: Finished evicting pasid 0x8002
[ 8108.359231] amdgpu: Started evicting pasid 0x8002
[ 8108.359245] amdgpu: Finished evicting pasid 0x8002
[ 8108.522234] amdgpu: Started evicting pasid 0x8002
[ 8108.522256] amdgpu: Finished evicting pasid 0x8002
[ 8108.683061] amdgpu: Started evicting pasid 0x8002
[ 8108.683075] amdgpu: Finished evicting pasid 0x8002
[ 8108.843356] amdgpu: Started evicting pasid 0x8002
[ 8108.843370] amdgpu: Finished evicting pasid 0x8002
[ 8109.005753] amdgpu: Started evicting pasid 0x8002
[ 8109.005766] amdgpu: Finished evicting pasid 0x8002
[ 8109.170535] amdgpu: Started evicting pasid 0x8002
[ 8109.170549] amdgpu: Finished evicting pasid 0x8002
[ 8109.337540] amdgpu: Started evicting pasid 0x8002
[ 8109.337554] amdgpu: Finished evicting pasid 0x8002
[ 8109.876026] amdgpu: Started evicting pasid 0x8002
[ 8109.876040] amdgpu: Finished evicting pasid 0x8002
[ 8110.036459] amdgpu: Started evicting pasid 0x8002
[ 8110.036473] amdgpu: Finished evicting pasid 0x8002
[ 8110.199091] amdgpu: Started evicting pasid 0x8002
[ 8110.199106] amdgpu: Finished evicting pasid 0x8002
[ 8110.360657] amdgpu: Started evicting pasid 0x8002
[ 8110.360671] amdgpu: Finished evicting pasid 0x8002
[ 8110.529459] amdgpu: Started evicting pasid 0x8002
[ 8110.529474] amdgpu: Finished evicting pasid 0x8002
[ 8110.696125] amdgpu: Started evicting pasid 0x8002
[ 8110.696140] amdgpu: Finished evicting pasid 0x8002
[ 8110.856349] amdgpu: Started evicting pasid 0x8002
[ 8110.856362] amdgpu: Finished evicting pasid 0x8002
[ 8111.017070] amdgpu: Started evicting pasid 0x8002
[ 8111.017084] amdgpu: Finished evicting pasid 0x8002
[ 8111.181274] amdgpu: Started evicting pasid 0x8002
[ 8111.181287] amdgpu: Finished evicting pasid 0x8002
[ 8111.340103] amdgpu: Started evicting pasid 0x8002
[ 8111.340116] amdgpu: Finished evicting pasid 0x8002
[ 8111.501989] amdgpu: Started evicting pasid 0x8002
[ 8111.502004] amdgpu: Finished evicting pasid 0x8002
[ 8111.662873] amdgpu: Started evicting pasid 0x8002
[ 8111.662887] amdgpu: Finished evicting pasid 0x8002
[ 8111.824013] amdgpu: Started evicting pasid 0x8002
[ 8111.824032] amdgpu: Finished evicting pasid 0x8002
[ 8111.986765] amdgpu: Started evicting pasid 0x8002
[ 8111.986778] amdgpu: Finished evicting pasid 0x8002
[ 8112.148403] amdgpu: Started evicting pasid 0x8002
[ 8112.148418] amdgpu: Finished evicting pasid 0x8002
[ 8112.310014] amdgpu: Started evicting pasid 0x8002
[ 8112.310029] amdgpu: Finished evicting pasid 0x8002
[ 8112.470799] amdgpu: Started evicting pasid 0x8002
[ 8112.470813] amdgpu: Finished evicting pasid 0x8002
[ 8112.633086] amdgpu: Started evicting pasid 0x8002
[ 8112.633100] amdgpu: Finished evicting pasid 0x8002
[ 8112.794250] amdgpu: Started evicting pasid 0x8002
[ 8112.794265] amdgpu: Finished evicting pasid 0x8002
[ 8112.957634] amdgpu: Started evicting pasid 0x8002
[ 8112.957648] amdgpu: Finished evicting pasid 0x8002
[ 8113.120957] amdgpu: Started evicting pasid 0x8002
[ 8113.120971] amdgpu: Finished evicting pasid 0x8002
[ 8113.281887] amdgpu: Started evicting pasid 0x8002
[ 8113.281901] amdgpu: Finished evicting pasid 0x8002
[ 8113.454356] amdgpu: Started evicting pasid 0x8002
[ 8113.454370] amdgpu: Finished evicting pasid 0x8002
[ 8113.620777] amdgpu: Started evicting pasid 0x8002
[ 8113.620791] amdgpu: Finished evicting pasid 0x8002
[ 8113.784178] amdgpu: Started evicting pasid 0x8002
[ 8113.784220] amdgpu: Finished evicting pasid 0x8002
[ 8113.949430] amdgpu: Started evicting pasid 0x8002
[ 8113.949444] amdgpu: Finished evicting pasid 0x8002
[ 8114.110311] amdgpu: Started evicting pasid 0x8002
[ 8114.110326] amdgpu: Finished evicting pasid 0x8002
[ 8114.270756] amdgpu: Started evicting pasid 0x8002
[ 8114.270770] amdgpu: Finished evicting pasid 0x8002
[ 8114.431915] amdgpu: Started evicting pasid 0x8002
[ 8114.431929] amdgpu: Finished evicting pasid 0x8002
[ 8114.595191] amdgpu: Started evicting pasid 0x8002
[ 8114.595205] amdgpu: Finished evicting pasid 0x8002
[ 8114.755778] amdgpu: Started evicting pasid 0x8002
[ 8114.755792] amdgpu: Finished evicting pasid 0x8002
[ 8114.918591] amdgpu: Started evicting pasid 0x8002
[ 8114.918605] amdgpu: Finished evicting pasid 0x8002
[ 8115.080939] amdgpu: Started evicting pasid 0x8002
[ 8115.080953] amdgpu: Finished evicting pasid 0x8002
[ 8115.241582] amdgpu: Started evicting pasid 0x8002
[ 8115.241596] amdgpu: Finished evicting pasid 0x8002
[ 8115.406141] amdgpu: Started evicting pasid 0x8002
[ 8115.406155] amdgpu: Finished evicting pasid 0x8002
[ 8115.973705] amdgpu: Started evicting pasid 0x8002
[ 8115.973720] amdgpu: Finished evicting pasid 0x8002
[ 8116.880977] amdgpu: Started evicting pasid 0x8002
[ 8116.880992] amdgpu: Finished evicting pasid 0x8002
[ 8117.105190] amdgpu: Started evicting pasid 0x8002
[ 8117.105205] amdgpu: Finished evicting pasid 0x8002
[ 8117.273317] amdgpu: Started evicting pasid 0x8002
[ 8117.273331] amdgpu: Finished evicting pasid 0x8002
[ 8117.436242] amdgpu: Started evicting pasid 0x8002
[ 8117.436256] amdgpu: Finished evicting pasid 0x8002
[ 8117.598781] amdgpu: Started evicting pasid 0x8002
[ 8117.598795] amdgpu: Finished evicting pasid 0x8002
[ 8117.761023] amdgpu: Started evicting pasid 0x8002
[ 8117.761037] amdgpu: Finished evicting pasid 0x8002
[ 8118.283958] amdgpu: Started evicting pasid 0x8002
[ 8118.283972] amdgpu: Finished evicting pasid 0x8002
[ 8119.997183] amdgpu: Started evicting pasid 0x8002
[ 8119.997197] amdgpu: Finished evicting pasid 0x8002
[ 8120.159708] amdgpu: Started evicting pasid 0x8002
[ 8120.159722] amdgpu: Finished evicting pasid 0x8002
[ 8120.324636] amdgpu: Started evicting pasid 0x8002
[ 8120.324650] amdgpu: Finished evicting pasid 0x8002
[ 8120.488087] amdgpu: Started evicting pasid 0x8002
[ 8120.488101] amdgpu: Finished evicting pasid 0x8002
[ 8120.654505] amdgpu: Started evicting pasid 0x8002
[ 8120.654519] amdgpu: Finished evicting pasid 0x8002
[ 8121.381179] amdgpu: Started evicting pasid 0x8002
[ 8121.381194] amdgpu: Finished evicting pasid 0x8002
[ 8121.548458] amdgpu: Started evicting pasid 0x8002
[ 8121.548472] amdgpu: Finished evicting pasid 0x8002
[ 8121.711945] amdgpu: Started evicting pasid 0x8002
[ 8121.711959] amdgpu: Finished evicting pasid 0x8002
[ 8121.886020] amdgpu: Started evicting pasid 0x8002
[ 8121.886035] amdgpu: Finished evicting pasid 0x8002
[ 8121.895196] amdgpu: Started evicting pasid 0x8003
[ 8121.895210] amdgpu: Finished evicting pasid 0x8003
[ 8122.065534] amdgpu: Started evicting pasid 0x8002
[ 8122.065549] amdgpu: Finished evicting pasid 0x8002
[ 8122.205716] amdgpu: Started evicting pasid 0x8002
[ 8122.205730] amdgpu: Finished evicting pasid 0x8002
[ 8122.376880] amdgpu: Started evicting pasid 0x8002
[ 8122.376894] amdgpu: Finished evicting pasid 0x8002
[ 8122.519451] amdgpu: Started evicting pasid 0x8002
[ 8122.519465] amdgpu: Finished evicting pasid 0x8002
[ 8122.688043] amdgpu: Started evicting pasid 0x8002
[ 8122.688058] amdgpu: Finished evicting pasid 0x8002
[ 8122.853221] amdgpu: Started evicting pasid 0x8002
[ 8122.853235] amdgpu: Finished evicting pasid 0x8002
[ 8123.013645] amdgpu: Started evicting pasid 0x8002
[ 8123.013660] amdgpu: Finished evicting pasid 0x8002
[ 8123.176135] amdgpu: Started evicting pasid 0x8002
[ 8123.176149] amdgpu: Finished evicting pasid 0x8002
[ 8123.341589] amdgpu: Started evicting pasid 0x8002
[ 8123.341603] amdgpu: Finished evicting pasid 0x8002
[ 8123.500648] amdgpu: Started evicting pasid 0x8002
[ 8123.500661] amdgpu: Finished evicting pasid 0x8002
[ 8123.738767] amdgpu: Started evicting pasid 0x8002
[ 8123.738781] amdgpu: Finished evicting pasid 0x8002
[ 8123.901125] amdgpu: Started evicting pasid 0x8002
[ 8123.901134] amdgpu: Finished evicting pasid 0x8002
[ 8124.072627] amdgpu: Started evicting pasid 0x8002
[ 8124.072641] amdgpu: Finished evicting pasid 0x8002
[ 8124.236252] amdgpu: Started evicting pasid 0x8002
[ 8124.236265] amdgpu: Finished evicting pasid 0x8002
[ 8124.399969] amdgpu: Started evicting pasid 0x8002
[ 8124.399983] amdgpu: Finished evicting pasid 0x8002
[ 8124.914089] amdgpu: Started evicting pasid 0x8002
[ 8124.914103] amdgpu: Finished evicting pasid 0x8002
[ 8125.076031] amdgpu: Started evicting pasid 0x8002
[ 8125.076045] amdgpu: Finished evicting pasid 0x8002
[ 8125.240210] amdgpu: Started evicting pasid 0x8002
[ 8125.240225] amdgpu: Finished evicting pasid 0x8002
[ 8125.407200] amdgpu: Started evicting pasid 0x8002
[ 8125.407214] amdgpu: Finished evicting pasid 0x8002
[ 8125.570348] amdgpu: Started evicting pasid 0x8002
[ 8125.570363] amdgpu: Finished evicting pasid 0x8002
[ 8125.738712] amdgpu: Started evicting pasid 0x8002
[ 8125.738727] amdgpu: Finished evicting pasid 0x8002
[ 8125.903022] amdgpu: Started evicting pasid 0x8002
[ 8125.903035] amdgpu: Finished evicting pasid 0x8002
[ 8126.065267] amdgpu: Started evicting pasid 0x8002
[ 8126.065282] amdgpu: Finished evicting pasid 0x8002
[ 8126.530799] amdgpu: Started evicting pasid 0x8002
[ 8126.530864] amdgpu: Finished evicting pasid 0x8002
[ 8128.100755] amdgpu: Started evicting pasid 0x8002
[ 8128.100821] amdgpu: Finished evicting pasid 0x8002
[ 8130.451482] amdgpu: Started evicting pasid 0x8002
[ 8130.451496] amdgpu: Finished evicting pasid 0x8002
[ 8130.940368] amdgpu: Started evicting pasid 0x8002
[ 8130.940383] amdgpu: Finished evicting pasid 0x8002
[ 8131.346177] gmc_v9_0_process_interrupt: 17 callbacks suppressed
[ 8131.346184] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346191] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4201000 from client 18
[ 8131.346194] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 8131.346197] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346199] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 8131.346202] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346204] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 8131.346207] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346209] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 8131.346218] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346221] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4202000 from client 18
[ 8131.346224] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 8131.346227] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346229] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 8131.346231] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346234] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 8131.346236] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346239] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 8131.346245] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346248] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4203000 from client 18
[ 8131.346251] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 8131.346254] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346256] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 8131.346258] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346261] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 8131.346263] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346266] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 8131.346272] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346275] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4204000 from client 18
[ 8131.346277] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[ 8131.346280] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346282] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[ 8131.346285] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346287] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[ 8131.346290] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346292] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[ 8131.346300] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346303] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4205000 from client 18
[ 8131.346306] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346308] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346311] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346313] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346316] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346318] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346321] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.346329] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346332] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4206000 from client 18
[ 8131.346334] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346337] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346339] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346341] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346343] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346345] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346347] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.346354] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346356] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4208000 from client 18
[ 8131.346358] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346359] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346361] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346363] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346365] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346366] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346368] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.346375] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346377] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4207000 from client 18
[ 8131.346379] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346382] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346384] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346386] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346389] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346391] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346393] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.346402] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346404] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4209000 from client 18
[ 8131.346407] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346408] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346410] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346411] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346413] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346414] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346415] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.346422] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 22295 thread hipMemsetAsyncM pid 22295)
[ 8131.346423] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f72d4201000 from client 18
[ 8131.346425] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[ 8131.346426] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[ 8131.346428] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[ 8131.346429] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[ 8131.346430] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[ 8131.346432] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[ 8131.346433] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[ 8131.439088] amdgpu: Started evicting pasid 0x8002
[ 8131.439099] amdgpu: Finished evicting pasid 0x8002
[ 8131.931690] amdgpu: Started evicting pasid 0x8002
[ 8131.931704] amdgpu: Finished evicting pasid 0x8002
[ 8132.092412] amdgpu: Started evicting pasid 0x8002
[ 8132.092427] amdgpu: Finished evicting pasid 0x8002
[ 8132.890967] amdgpu: Started evicting pasid 0x8002
[ 8132.890981] amdgpu: Finished evicting pasid 0x8002
[ 8133.055772] amdgpu: Started evicting pasid 0x8002
[ 8133.055785] amdgpu: Finished evicting pasid 0x8002
[ 8133.215558] amdgpu: Started evicting pasid 0x8002
[ 8133.215571] amdgpu: Finished evicting pasid 0x8002
[ 8133.439432] amdgpu: Started evicting pasid 0x8002
[ 8133.439446] amdgpu: Finished evicting pasid 0x8002
[ 8133.831170] amdgpu: Started evicting pasid 0x8002
[ 8133.831226] amdgpu: Finished evicting pasid 0x8002
[ 8134.235165] amdgpu: Started evicting pasid 0x8002
[ 8134.235225] amdgpu: Finished evicting pasid 0x8002
[ 8134.652511] amdgpu: Started evicting pasid 0x8002
[ 8134.652572] amdgpu: Finished evicting pasid 0x8002
[ 8135.072818] amdgpu: Started evicting pasid 0x8002
[ 8135.072876] amdgpu: Finished evicting pasid 0x8002
[ 8135.540612] amdgpu: Started evicting pasid 0x8002
[ 8135.540659] amdgpu: Finished evicting pasid 0x8002
[ 8136.004422] amdgpu: Started evicting pasid 0x8002
[ 8136.004473] amdgpu: Finished evicting pasid 0x8002
[ 8136.468761] amdgpu: Started evicting pasid 0x8002
[ 8136.468811] amdgpu: Finished evicting pasid 0x8002
[ 8136.641704] amdgpu: Started evicting pasid 0x8002
[ 8136.641718] amdgpu: Finished evicting pasid 0x8002
[ 8136.803234] amdgpu: Started evicting pasid 0x8002
[ 8136.803249] amdgpu: Finished evicting pasid 0x8002
[ 8136.964097] amdgpu: Started evicting pasid 0x8002
[ 8136.964111] amdgpu: Finished evicting pasid 0x8002
[ 8137.548387] amdgpu: Started evicting pasid 0x8002
[ 8137.548401] amdgpu: Finished evicting pasid 0x8002
[ 8137.712592] amdgpu: Started evicting pasid 0x8002
[ 8137.712606] amdgpu: Finished evicting pasid 0x8002
[ 8137.874510] amdgpu: Started evicting pasid 0x8002
[ 8137.874524] amdgpu: Finished evicting pasid 0x8002
[ 8138.036519] amdgpu: Started evicting pasid 0x8002
[ 8138.036532] amdgpu: Finished evicting pasid 0x8002
[ 8138.197784] amdgpu: Started evicting pasid 0x8002
[ 8138.197798] amdgpu: Finished evicting pasid 0x8002
[ 8138.359870] amdgpu: Started evicting pasid 0x8002
[ 8138.359885] amdgpu: Finished evicting pasid 0x8002
[ 8138.592998] amdgpu: Started evicting pasid 0x8002
[ 8138.593012] amdgpu: Finished evicting pasid 0x8002
[ 8138.753517] amdgpu: Started evicting pasid 0x8002
[ 8138.753532] amdgpu: Finished evicting pasid 0x8002
[ 8174.072211] amdgpu: Started evicting pasid 0x8002
[ 8174.072224] amdgpu: Finished evicting pasid 0x8002
[ 8174.240127] amdgpu: Started evicting pasid 0x8002
[ 8174.240141] amdgpu: Finished evicting pasid 0x8002
[ 8174.402198] amdgpu: Started evicting pasid 0x8002
[ 8174.402212] amdgpu: Finished evicting pasid 0x8002
[ 8174.562537] amdgpu: Started evicting pasid 0x8002
[ 8174.562551] amdgpu: Finished evicting pasid 0x8002
[ 8174.724673] amdgpu: Started evicting pasid 0x8002
[ 8174.724688] amdgpu: Finished evicting pasid 0x8002
[ 8174.886003] amdgpu: Started evicting pasid 0x8002
[ 8174.886018] amdgpu: Finished evicting pasid 0x8002
[ 8175.047749] amdgpu: Started evicting pasid 0x8002
[ 8175.047763] amdgpu: Finished evicting pasid 0x8002
[ 8175.212026] amdgpu: Started evicting pasid 0x8002
[ 8175.212040] amdgpu: Finished evicting pasid 0x8002
[ 8185.962462] amdgpu: Started evicting pasid 0x8002
[ 8185.962475] amdgpu: Finished evicting pasid 0x8002
[ 8186.130402] amdgpu: Started evicting pasid 0x8002
[ 8186.130416] amdgpu: Finished evicting pasid 0x8002
[ 8186.294106] amdgpu: Started evicting pasid 0x8002
[ 8186.294120] amdgpu: Finished evicting pasid 0x8002
[ 8186.459815] amdgpu: Started evicting pasid 0x8002
[ 8186.459829] amdgpu: Finished evicting pasid 0x8002
[ 8186.618745] amdgpu: Started evicting pasid 0x8002
[ 8186.618760] amdgpu: Finished evicting pasid 0x8002
[ 8186.780174] amdgpu: Started evicting pasid 0x8002
[ 8186.780188] amdgpu: Finished evicting pasid 0x8002
[ 8192.624424] amdgpu: Started evicting pasid 0x8002
[ 8192.624438] amdgpu: Finished evicting pasid 0x8002
[ 8194.286060] amdgpu: Started evicting pasid 0x8002
[ 8194.286074] amdgpu: Finished evicting pasid 0x8002
[ 8194.452454] amdgpu: Started evicting pasid 0x8002
[ 8194.452467] amdgpu: Finished evicting pasid 0x8002
[ 8194.612859] amdgpu: Started evicting pasid 0x8002
[ 8194.612873] amdgpu: Finished evicting pasid 0x8002
[ 8194.784493] amdgpu: Started evicting pasid 0x8002
[ 8194.784506] amdgpu: Finished evicting pasid 0x8002
[ 8195.269326] amdgpu: Started evicting pasid 0x8002
[ 8195.269340] amdgpu: Finished evicting pasid 0x8002
[ 8195.434279] amdgpu: Started evicting pasid 0x8002
[ 8195.434293] amdgpu: Finished evicting pasid 0x8002
[11890.708225] amdgpu: Started evicting pasid 0x8002
[11890.708294] amdgpu: Finished evicting pasid 0x8002
[11892.082540] amdgpu: Started evicting pasid 0x8002
[11892.082611] amdgpu: Finished evicting pasid 0x8002
[11893.024851] amdgpu: Started evicting pasid 0x8002
[11893.024920] amdgpu: Finished evicting pasid 0x8002
[11893.926192] amdgpu: Started evicting pasid 0x8002
[11893.926262] amdgpu: Finished evicting pasid 0x8002
[11906.903584] amdgpu: Started evicting pasid 0x8002
[11906.903595] amdgpu: Finished evicting pasid 0x8002
[11907.767075] amdgpu: Started evicting pasid 0x8002
[11907.767086] amdgpu: Finished evicting pasid 0x8002
[11908.110155] amdgpu: Started evicting pasid 0x8002
[11908.110166] amdgpu: Finished evicting pasid 0x8002
[11908.439017] amdgpu: Started evicting pasid 0x8002
[11908.439028] amdgpu: Finished evicting pasid 0x8002
[11949.881899] amdgpu: Started evicting pasid 0x8002
[11949.881964] amdgpu: Finished evicting pasid 0x8002
[11964.967743] amdgpu: Started evicting pasid 0x8002
[11964.967754] amdgpu: Finished evicting pasid 0x8002
[12014.827439] amdgpu: Started evicting pasid 0x8002
[12014.827450] amdgpu: Finished evicting pasid 0x8002
[12014.930935] amdgpu: Started restoring pasid 0x8002
[12014.930973] amdgpu: Finished restoring pasid 0x8002
[12015.418055] amdgpu: Started evicting pasid 0x8002
[12015.418066] amdgpu: Finished evicting pasid 0x8002
[12015.971201] amdgpu: Started evicting pasid 0x8002
[12015.971213] amdgpu: Finished evicting pasid 0x8002
[12016.074830] amdgpu: Started restoring pasid 0x8002
[12016.074867] amdgpu: Finished restoring pasid 0x8002
[12017.438065] amdgpu: Started evicting pasid 0x8002
[12017.438076] amdgpu: Finished evicting pasid 0x8002
[12017.538701] amdgpu: Started restoring pasid 0x8002
[12017.538738] amdgpu: Finished restoring pasid 0x8002
[13683.158018] amdgpu: Started evicting pasid 0x8002
[13683.158030] amdgpu: Finished evicting pasid 0x8002
[13683.259605] amdgpu: Started restoring pasid 0x8002
[13683.259624] amdgpu: Finished restoring pasid 0x8002
[13683.309007] amdgpu: Started evicting pasid 0x8002
[13683.309020] amdgpu: Finished evicting pasid 0x8002
[13683.542329] amdgpu: Started evicting pasid 0x8002
[13683.542344] amdgpu: Finished evicting pasid 0x8002
[13685.191697] amdgpu: Started evicting pasid 0x8002
[13685.191711] amdgpu: Finished evicting pasid 0x8002
[13686.925245] amdgpu: Started evicting pasid 0x8002
[13686.925259] amdgpu: Finished evicting pasid 0x8002
[13687.084863] amdgpu: Started evicting pasid 0x8002
[13687.084876] amdgpu: Finished evicting pasid 0x8002
[13687.245796] amdgpu: Started evicting pasid 0x8002
[13687.245810] amdgpu: Finished evicting pasid 0x8002
[13687.405008] amdgpu: Started evicting pasid 0x8002
[13687.405023] amdgpu: Finished evicting pasid 0x8002
[13687.593582] amdgpu: Started evicting pasid 0x8002
[13687.593596] amdgpu: Finished evicting pasid 0x8002
[13687.752059] amdgpu: Started evicting pasid 0x8002
[13687.752073] amdgpu: Finished evicting pasid 0x8002
[13687.911466] amdgpu: Started evicting pasid 0x8002
[13687.911480] amdgpu: Finished evicting pasid 0x8002
[13688.073526] amdgpu: Started evicting pasid 0x8002
[13688.073540] amdgpu: Finished evicting pasid 0x8002
[13688.234994] amdgpu: Started evicting pasid 0x8002
[13688.235012] amdgpu: Finished evicting pasid 0x8002
[13688.396429] amdgpu: Started evicting pasid 0x8002
[13688.396443] amdgpu: Finished evicting pasid 0x8002
[13688.559837] amdgpu: Started evicting pasid 0x8002
[13688.559851] amdgpu: Finished evicting pasid 0x8002
[13688.720637] amdgpu: Started evicting pasid 0x8002
[13688.720651] amdgpu: Finished evicting pasid 0x8002
[13688.883595] amdgpu: Started evicting pasid 0x8002
[13688.883614] amdgpu: Finished evicting pasid 0x8002
[13689.073231] amdgpu: Started evicting pasid 0x8002
[13689.073245] amdgpu: Finished evicting pasid 0x8002
[13689.236813] amdgpu: Started evicting pasid 0x8002
[13689.236826] amdgpu: Finished evicting pasid 0x8002
[13689.402883] amdgpu: Started evicting pasid 0x8002
[13689.402897] amdgpu: Finished evicting pasid 0x8002
[13689.565295] amdgpu: Started evicting pasid 0x8002
[13689.565309] amdgpu: Finished evicting pasid 0x8002
[13689.860992] amdgpu: Started evicting pasid 0x8002
[13689.861006] amdgpu: Finished evicting pasid 0x8002
[13690.021865] amdgpu: Started evicting pasid 0x8002
[13690.021878] amdgpu: Finished evicting pasid 0x8002
[13690.180502] amdgpu: Started evicting pasid 0x8002
[13690.180516] amdgpu: Finished evicting pasid 0x8002
[13690.340545] amdgpu: Started evicting pasid 0x8002
[13690.340558] amdgpu: Finished evicting pasid 0x8002
[13690.501140] amdgpu: Started evicting pasid 0x8002
[13690.501154] amdgpu: Finished evicting pasid 0x8002
[13690.663530] amdgpu: Started evicting pasid 0x8002
[13690.663544] amdgpu: Finished evicting pasid 0x8002
[13690.825113] amdgpu: Started evicting pasid 0x8002
[13690.825128] amdgpu: Finished evicting pasid 0x8002
[13690.988048] amdgpu: Started evicting pasid 0x8002
[13690.988062] amdgpu: Finished evicting pasid 0x8002
[13691.148869] amdgpu: Started evicting pasid 0x8002
[13691.148882] amdgpu: Finished evicting pasid 0x8002
[13691.311353] amdgpu: Started evicting pasid 0x8002
[13691.311368] amdgpu: Finished evicting pasid 0x8002
[13691.474701] amdgpu: Started evicting pasid 0x8002
[13691.474715] amdgpu: Finished evicting pasid 0x8002
[13691.660694] amdgpu: Started evicting pasid 0x8002
[13691.660709] amdgpu: Finished evicting pasid 0x8002
[13691.849366] amdgpu: Started evicting pasid 0x8002
[13691.849380] amdgpu: Finished evicting pasid 0x8002
[13692.004487] amdgpu: Started evicting pasid 0x8002
[13692.004502] amdgpu: Finished evicting pasid 0x8002
[13692.166884] amdgpu: Started evicting pasid 0x8002
[13692.166898] amdgpu: Finished evicting pasid 0x8002
[13692.332499] amdgpu: Started evicting pasid 0x8002
[13692.332514] amdgpu: Finished evicting pasid 0x8002
[13692.490892] amdgpu: Started evicting pasid 0x8002
[13692.490906] amdgpu: Finished evicting pasid 0x8002
[13692.654491] amdgpu: Started evicting pasid 0x8002
[13692.654504] amdgpu: Finished evicting pasid 0x8002
[13692.812960] amdgpu: Started evicting pasid 0x8002
[13692.812974] amdgpu: Finished evicting pasid 0x8002
[13692.974314] amdgpu: Started evicting pasid 0x8002
[13692.974327] amdgpu: Finished evicting pasid 0x8002
[13693.133098] amdgpu: Started evicting pasid 0x8002
[13693.133112] amdgpu: Finished evicting pasid 0x8002
[13693.292497] amdgpu: Started evicting pasid 0x8002
[13693.292511] amdgpu: Finished evicting pasid 0x8002
[13693.454494] amdgpu: Started evicting pasid 0x8002
[13693.454507] amdgpu: Finished evicting pasid 0x8002
[13693.616040] amdgpu: Started evicting pasid 0x8002
[13693.616054] amdgpu: Finished evicting pasid 0x8002
[13693.778185] amdgpu: Started evicting pasid 0x8002
[13693.778198] amdgpu: Finished evicting pasid 0x8002
[13693.938669] amdgpu: Started evicting pasid 0x8002
[13693.938683] amdgpu: Finished evicting pasid 0x8002
[13694.102273] amdgpu: Started evicting pasid 0x8002
[13694.102287] amdgpu: Finished evicting pasid 0x8002
[13694.260016] amdgpu: Started evicting pasid 0x8002
[13694.260030] amdgpu: Finished evicting pasid 0x8002
[13694.422581] amdgpu: Started evicting pasid 0x8002
[13694.422595] amdgpu: Finished evicting pasid 0x8002
[13694.953379] amdgpu: Started evicting pasid 0x8002
[13694.953393] amdgpu: Finished evicting pasid 0x8002
[13695.113251] amdgpu: Started evicting pasid 0x8002
[13695.113264] amdgpu: Finished evicting pasid 0x8002
[13695.274136] amdgpu: Started evicting pasid 0x8002
[13695.274150] amdgpu: Finished evicting pasid 0x8002
[13695.433691] amdgpu: Started evicting pasid 0x8002
[13695.433705] amdgpu: Finished evicting pasid 0x8002
[13695.594509] amdgpu: Started evicting pasid 0x8002
[13695.594522] amdgpu: Finished evicting pasid 0x8002
[13695.759370] amdgpu: Started evicting pasid 0x8002
[13695.759384] amdgpu: Finished evicting pasid 0x8002
[13695.920758] amdgpu: Started evicting pasid 0x8002
[13695.920772] amdgpu: Finished evicting pasid 0x8002
[13696.082590] amdgpu: Started evicting pasid 0x8002
[13696.082604] amdgpu: Finished evicting pasid 0x8002
[13696.247360] amdgpu: Started evicting pasid 0x8002
[13696.247375] amdgpu: Finished evicting pasid 0x8002
[13696.412903] amdgpu: Started evicting pasid 0x8002
[13696.412917] amdgpu: Finished evicting pasid 0x8002
[13696.574927] amdgpu: Started evicting pasid 0x8002
[13696.574941] amdgpu: Finished evicting pasid 0x8002
[13696.738978] amdgpu: Started evicting pasid 0x8002
[13696.738993] amdgpu: Finished evicting pasid 0x8002
[13696.903109] amdgpu: Started evicting pasid 0x8002
[13696.903124] amdgpu: Finished evicting pasid 0x8002
[13697.067534] amdgpu: Started evicting pasid 0x8002
[13697.067549] amdgpu: Finished evicting pasid 0x8002
[13697.227229] amdgpu: Started evicting pasid 0x8002
[13697.227243] amdgpu: Finished evicting pasid 0x8002
[13697.388485] amdgpu: Started evicting pasid 0x8002
[13697.388499] amdgpu: Finished evicting pasid 0x8002
[13697.551203] amdgpu: Started evicting pasid 0x8002
[13697.551217] amdgpu: Finished evicting pasid 0x8002
[13697.714099] amdgpu: Started evicting pasid 0x8002
[13697.714113] amdgpu: Finished evicting pasid 0x8002
[13697.874869] amdgpu: Started evicting pasid 0x8002
[13697.874884] amdgpu: Finished evicting pasid 0x8002
[13698.036532] amdgpu: Started evicting pasid 0x8002
[13698.036546] amdgpu: Finished evicting pasid 0x8002
[13698.199071] amdgpu: Started evicting pasid 0x8002
[13698.199085] amdgpu: Finished evicting pasid 0x8002
[13698.359910] amdgpu: Started evicting pasid 0x8002
[13698.359925] amdgpu: Finished evicting pasid 0x8002
[13698.520602] amdgpu: Started evicting pasid 0x8002
[13698.520616] amdgpu: Finished evicting pasid 0x8002
[13698.682899] amdgpu: Started evicting pasid 0x8002
[13698.682914] amdgpu: Finished evicting pasid 0x8002
[13698.843134] amdgpu: Started evicting pasid 0x8002
[13698.843149] amdgpu: Finished evicting pasid 0x8002
[13699.005309] amdgpu: Started evicting pasid 0x8002
[13699.005323] amdgpu: Finished evicting pasid 0x8002
[13699.166309] amdgpu: Started evicting pasid 0x8002
[13699.166324] amdgpu: Finished evicting pasid 0x8002
[13699.332481] amdgpu: Started evicting pasid 0x8002
[13699.332495] amdgpu: Finished evicting pasid 0x8002
[13699.491360] amdgpu: Started evicting pasid 0x8002
[13699.491378] amdgpu: Finished evicting pasid 0x8002
[13699.655869] amdgpu: Started evicting pasid 0x8002
[13699.655884] amdgpu: Finished evicting pasid 0x8002
[13699.815788] amdgpu: Started evicting pasid 0x8002
[13699.815802] amdgpu: Finished evicting pasid 0x8002
[13699.976457] amdgpu: Started evicting pasid 0x8002
[13699.976471] amdgpu: Finished evicting pasid 0x8002
[13700.138099] amdgpu: Started evicting pasid 0x8002
[13700.138112] amdgpu: Finished evicting pasid 0x8002
[13700.299414] amdgpu: Started evicting pasid 0x8002
[13700.299428] amdgpu: Finished evicting pasid 0x8002
[13700.460156] amdgpu: Started evicting pasid 0x8002
[13700.460170] amdgpu: Finished evicting pasid 0x8002
[13701.021060] amdgpu: Started evicting pasid 0x8002
[13701.021074] amdgpu: Finished evicting pasid 0x8002
[13701.914129] amdgpu: Started evicting pasid 0x8002
[13701.914144] amdgpu: Finished evicting pasid 0x8002
[13702.128949] amdgpu: Started evicting pasid 0x8002
[13702.128964] amdgpu: Finished evicting pasid 0x8002
[13702.295532] amdgpu: Started evicting pasid 0x8002
[13702.295547] amdgpu: Finished evicting pasid 0x8002
[13702.458230] amdgpu: Started evicting pasid 0x8002
[13702.458244] amdgpu: Finished evicting pasid 0x8002
[13702.622205] amdgpu: Started evicting pasid 0x8002
[13702.622219] amdgpu: Finished evicting pasid 0x8002
[13702.784896] amdgpu: Started evicting pasid 0x8002
[13702.784909] amdgpu: Finished evicting pasid 0x8002
[13703.297305] amdgpu: Started evicting pasid 0x8002
[13703.297319] amdgpu: Finished evicting pasid 0x8002
[13704.984204] amdgpu: Started evicting pasid 0x8002
[13704.984218] amdgpu: Finished evicting pasid 0x8002
[13705.142357] amdgpu: Started evicting pasid 0x8002
[13705.142372] amdgpu: Finished evicting pasid 0x8002
[13705.304766] amdgpu: Started evicting pasid 0x8002
[13705.304780] amdgpu: Finished evicting pasid 0x8002
[13705.467492] amdgpu: Started evicting pasid 0x8002
[13705.467506] amdgpu: Finished evicting pasid 0x8002
[13705.628061] amdgpu: Started evicting pasid 0x8002
[13705.628074] amdgpu: Finished evicting pasid 0x8002
[13706.355937] amdgpu: Started evicting pasid 0x8002
[13706.355952] amdgpu: Finished evicting pasid 0x8002
[13706.518230] amdgpu: Started evicting pasid 0x8002
[13706.518244] amdgpu: Finished evicting pasid 0x8002
[13706.680254] amdgpu: Started evicting pasid 0x8002
[13706.680268] amdgpu: Finished evicting pasid 0x8002
[13706.843563] amdgpu: Started evicting pasid 0x8002
[13706.843578] amdgpu: Finished evicting pasid 0x8002
[13706.854111] amdgpu: Started evicting pasid 0x8003
[13706.854124] amdgpu: Finished evicting pasid 0x8003
[13707.026197] amdgpu: Started evicting pasid 0x8002
[13707.026210] amdgpu: Finished evicting pasid 0x8002
[13707.166075] amdgpu: Started evicting pasid 0x8003
[13707.166089] amdgpu: Finished evicting pasid 0x8003
[13707.338218] amdgpu: Started evicting pasid 0x8002
[13707.338233] amdgpu: Finished evicting pasid 0x8002
[13707.483689] amdgpu: Started evicting pasid 0x8002
[13707.483704] amdgpu: Finished evicting pasid 0x8002
[13707.643054] amdgpu: Started evicting pasid 0x8002
[13707.643068] amdgpu: Finished evicting pasid 0x8002
[13707.802161] amdgpu: Started evicting pasid 0x8002
[13707.802175] amdgpu: Finished evicting pasid 0x8002
[13707.963407] amdgpu: Started evicting pasid 0x8002
[13707.963421] amdgpu: Finished evicting pasid 0x8002
[13708.124844] amdgpu: Started evicting pasid 0x8002
[13708.124858] amdgpu: Finished evicting pasid 0x8002
[13708.285805] amdgpu: Started evicting pasid 0x8002
[13708.285819] amdgpu: Finished evicting pasid 0x8002
[13708.449122] amdgpu: Started evicting pasid 0x8002
[13708.449137] amdgpu: Finished evicting pasid 0x8002
[13708.676864] amdgpu: Started evicting pasid 0x8002
[13708.676879] amdgpu: Finished evicting pasid 0x8002
[13708.834507] amdgpu: Started evicting pasid 0x8002
[13708.834521] amdgpu: Finished evicting pasid 0x8002
[13708.995735] amdgpu: Started evicting pasid 0x8002
[13708.995750] amdgpu: Finished evicting pasid 0x8002
[13709.157649] amdgpu: Started evicting pasid 0x8002
[13709.157663] amdgpu: Finished evicting pasid 0x8002
[13709.319285] amdgpu: Started evicting pasid 0x8002
[13709.319299] amdgpu: Finished evicting pasid 0x8002
[13709.826582] amdgpu: Started evicting pasid 0x8002
[13709.826596] amdgpu: Finished evicting pasid 0x8002
[13709.992470] amdgpu: Started evicting pasid 0x8002
[13709.992485] amdgpu: Finished evicting pasid 0x8002
[13710.153399] amdgpu: Started evicting pasid 0x8002
[13710.153413] amdgpu: Finished evicting pasid 0x8002
[13710.313989] amdgpu: Started evicting pasid 0x8002
[13710.314004] amdgpu: Finished evicting pasid 0x8002
[13710.477483] amdgpu: Started evicting pasid 0x8002
[13710.477497] amdgpu: Finished evicting pasid 0x8002
[13710.653089] amdgpu: Started evicting pasid 0x8002
[13710.653100] amdgpu: Finished evicting pasid 0x8002
[13710.810833] amdgpu: Started evicting pasid 0x8002
[13710.810846] amdgpu: Finished evicting pasid 0x8002
[13710.969782] amdgpu: Started evicting pasid 0x8002
[13710.969795] amdgpu: Finished evicting pasid 0x8002
[13711.313220] gmc_v9_0_process_interrupt: 35 callbacks suppressed
[13711.313231] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313238] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45200000 from client 18
[13711.313242] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[13711.313245] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313248] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13711.313250] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313253] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[13711.313255] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313258] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313273] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313277] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45201000 from client 18
[13711.313280] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313283] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313285] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313288] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313290] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313293] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313295] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313302] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313305] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45202000 from client 18
[13711.313308] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313311] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313313] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313316] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313318] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313321] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313323] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313331] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313334] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45203000 from client 18
[13711.313337] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313339] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313342] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313344] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313347] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313349] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313352] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313359] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313362] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45204000 from client 18
[13711.313365] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313367] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313370] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313372] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313375] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313378] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313380] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313387] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313390] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45205000 from client 18
[13711.313392] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313395] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313397] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313400] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313402] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313405] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313407] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313414] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313417] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45206000 from client 18
[13711.313419] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313422] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313424] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313427] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313429] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313432] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313434] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313441] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313444] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45208000 from client 18
[13711.313446] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313449] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313451] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313454] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313456] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313459] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313461] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313468] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313471] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45207000 from client 18
[13711.313473] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313476] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313478] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313481] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313483] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313486] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313488] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.313495] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipMemset pid 65841 thread hipMemset pid 65841)
[13711.313498] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fde45209000 from client 18
[13711.313500] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13711.313503] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13711.313505] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13711.313508] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13711.313510] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13711.313513] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13711.313515] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13711.408485] amdgpu: Started evicting pasid 0x8002
[13711.408498] amdgpu: Finished evicting pasid 0x8002
[13712.979972] amdgpu: Started evicting pasid 0x8002
[13712.980037] amdgpu: Finished evicting pasid 0x8002
[13715.328738] amdgpu: Started evicting pasid 0x8002
[13715.328752] amdgpu: Finished evicting pasid 0x8002
[13715.824283] amdgpu: Started evicting pasid 0x8002
[13715.824297] amdgpu: Finished evicting pasid 0x8002
[13716.376912] gmc_v9_0_process_interrupt: 79 callbacks suppressed
[13716.376918] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.376923] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4200000 from client 18
[13716.376926] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13716.376928] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.376930] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13716.376932] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.376934] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13716.376935] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.376937] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13716.376945] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.376948] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4201000 from client 18
[13716.376950] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13716.376952] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.376954] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13716.376955] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.376957] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13716.376959] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.376961] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13716.376966] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.376969] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4202000 from client 18
[13716.376971] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13716.376972] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.376974] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13716.376976] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.376978] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13716.376980] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.376982] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13716.376986] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.376989] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4203000 from client 18
[13716.376991] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.376992] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.376994] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.376996] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.376998] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377000] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377002] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377009] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377011] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4204000 from client 18
[13716.377013] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377015] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377017] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377018] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377020] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377022] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377024] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377030] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377033] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4205000 from client 18
[13716.377035] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377036] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377038] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377040] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377042] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377044] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377046] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377052] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377054] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4206000 from client 18
[13716.377056] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377058] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377060] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377062] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377064] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377065] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377067] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377072] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377074] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4207000 from client 18
[13716.377075] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377077] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377078] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377079] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377081] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377082] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377083] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377089] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377090] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4208000 from client 18
[13716.377092] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377093] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377094] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377096] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377097] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377099] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377100] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.377106] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 66048 thread hipMemsetAsyncM pid 66048)
[13716.377108] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdad4200000 from client 18
[13716.377110] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13716.377112] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13716.377113] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13716.377115] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13716.377117] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13716.377118] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13716.377120] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13716.466554] amdgpu: Started evicting pasid 0x8002
[13716.466566] amdgpu: Finished evicting pasid 0x8002
[13716.956305] amdgpu: Started evicting pasid 0x8002
[13716.956319] amdgpu: Finished evicting pasid 0x8002
[13717.116851] amdgpu: Started evicting pasid 0x8002
[13717.116865] amdgpu: Finished evicting pasid 0x8002
[13717.927956] amdgpu: Started evicting pasid 0x8002
[13717.927970] amdgpu: Finished evicting pasid 0x8002
[13718.087771] amdgpu: Started evicting pasid 0x8002
[13718.087785] amdgpu: Finished evicting pasid 0x8002
[13718.247619] amdgpu: Started evicting pasid 0x8002
[13718.247633] amdgpu: Finished evicting pasid 0x8002
[13718.472169] amdgpu: Started evicting pasid 0x8002
[13718.472184] amdgpu: Finished evicting pasid 0x8002
[13718.868374] amdgpu: Started evicting pasid 0x8002
[13718.868434] amdgpu: Finished evicting pasid 0x8002
[13719.269918] amdgpu: Started evicting pasid 0x8002
[13719.269977] amdgpu: Finished evicting pasid 0x8002
[13719.673539] amdgpu: Started evicting pasid 0x8002
[13719.673602] amdgpu: Finished evicting pasid 0x8002
[13720.100101] amdgpu: Started evicting pasid 0x8002
[13720.100158] amdgpu: Finished evicting pasid 0x8002
[13720.578638] amdgpu: Started evicting pasid 0x8002
[13720.578694] amdgpu: Finished evicting pasid 0x8002
[13721.045409] amdgpu: Started evicting pasid 0x8002
[13721.045462] amdgpu: Finished evicting pasid 0x8002
[13721.519512] amdgpu: Started evicting pasid 0x8002
[13721.519564] amdgpu: Finished evicting pasid 0x8002
[13721.691495] amdgpu: Started evicting pasid 0x8002
[13721.691509] amdgpu: Finished evicting pasid 0x8002
[13721.853433] amdgpu: Started evicting pasid 0x8002
[13721.853448] amdgpu: Finished evicting pasid 0x8002
[13722.021328] amdgpu: Started evicting pasid 0x8002
[13722.021342] amdgpu: Finished evicting pasid 0x8002
[13722.580007] amdgpu: Started evicting pasid 0x8002
[13722.580023] amdgpu: Finished evicting pasid 0x8002
[13722.741594] amdgpu: Started evicting pasid 0x8002
[13722.741609] amdgpu: Finished evicting pasid 0x8002
[13722.907109] amdgpu: Started evicting pasid 0x8002
[13722.907124] amdgpu: Finished evicting pasid 0x8002
[13723.077481] amdgpu: Started evicting pasid 0x8002
[13723.077494] amdgpu: Finished evicting pasid 0x8002
[13723.244945] amdgpu: Started evicting pasid 0x8002
[13723.244960] amdgpu: Finished evicting pasid 0x8002
[13723.410480] amdgpu: Started evicting pasid 0x8002
[13723.410495] amdgpu: Finished evicting pasid 0x8002
[13723.641935] amdgpu: Started evicting pasid 0x8002
[13723.641950] amdgpu: Finished evicting pasid 0x8002
[13723.809818] amdgpu: Started evicting pasid 0x8002
[13723.809832] amdgpu: Finished evicting pasid 0x8002
[13758.236303] amdgpu: Started evicting pasid 0x8002
[13758.236319] amdgpu: Finished evicting pasid 0x8002
[13758.398311] amdgpu: Started evicting pasid 0x8002
[13758.398326] amdgpu: Finished evicting pasid 0x8002
[13758.565267] amdgpu: Started evicting pasid 0x8002
[13758.565281] amdgpu: Finished evicting pasid 0x8002
[13758.731735] amdgpu: Started evicting pasid 0x8002
[13758.731750] amdgpu: Finished evicting pasid 0x8002
[13758.891839] amdgpu: Started evicting pasid 0x8002
[13758.891853] amdgpu: Finished evicting pasid 0x8002
[13759.053264] amdgpu: Started evicting pasid 0x8002
[13759.053278] amdgpu: Finished evicting pasid 0x8002
[13759.220994] amdgpu: Started evicting pasid 0x8002
[13759.221009] amdgpu: Finished evicting pasid 0x8002
[13759.385995] amdgpu: Started evicting pasid 0x8002
[13759.386010] amdgpu: Finished evicting pasid 0x8002
[13770.148187] amdgpu: Started evicting pasid 0x8002
[13770.148201] amdgpu: Finished evicting pasid 0x8002
[13770.312491] amdgpu: Started evicting pasid 0x8002
[13770.312507] amdgpu: Finished evicting pasid 0x8002
[13770.475204] amdgpu: Started evicting pasid 0x8002
[13770.475219] amdgpu: Finished evicting pasid 0x8002
[13770.634008] amdgpu: Started evicting pasid 0x8002
[13770.634023] amdgpu: Finished evicting pasid 0x8002
[13770.796088] amdgpu: Started evicting pasid 0x8002
[13770.796137] amdgpu: Finished evicting pasid 0x8002
[13770.958681] amdgpu: Started evicting pasid 0x8002
[13770.958696] amdgpu: Finished evicting pasid 0x8002
[13776.771674] amdgpu: Started evicting pasid 0x8002
[13776.771689] amdgpu: Finished evicting pasid 0x8002
[13778.446968] amdgpu: Started evicting pasid 0x8002
[13778.446981] amdgpu: Finished evicting pasid 0x8002
[13778.608662] amdgpu: Started evicting pasid 0x8002
[13778.608676] amdgpu: Finished evicting pasid 0x8002
[13778.770793] amdgpu: Started evicting pasid 0x8002
[13778.770807] amdgpu: Finished evicting pasid 0x8002
[13778.931836] amdgpu: Started evicting pasid 0x8002
[13778.931850] amdgpu: Finished evicting pasid 0x8002
[13779.397254] amdgpu: Started evicting pasid 0x8002
[13779.397268] amdgpu: Finished evicting pasid 0x8002
[13779.560389] amdgpu: Started evicting pasid 0x8002
[13779.560403] amdgpu: Finished evicting pasid 0x8002
[13906.829501] show_signal_msg: 26 callbacks suppressed
[13906.829503] hipMemset[74498]: segfault at 0 ip 00007fba6d0f0cf1 sp 00007ffdd9ccd6e0 error 4 in libc-2.27.so[7fba6d059000+1e7000]
[13906.829509] Code: 0d dc 35 35 00 48 89 f0 48 f7 d8 f0 48 01 05 de 35 35 00 e8 d1 3b 08 00 e9 ac fe ff ff 0f 1f 40 00 4c 89 e8 48 25 00 00 00 fc <48> 8b 18 e9 aa fd ff ff 0f 1f 80 00 00 00 00 4c 3b 2d 29 5c 35 00
[13906.926838] amdgpu: Started evicting pasid 0x8002
[13906.926905] amdgpu: Finished evicting pasid 0x8002
[13910.205786] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205794] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04400000 from client 18
[13910.205798] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13910.205801] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205804] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13910.205806] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205809] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13910.205812] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205814] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13910.205824] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205828] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04401000 from client 18
[13910.205831] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205833] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205836] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205839] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205841] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205844] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205846] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.205853] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205856] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04402000 from client 18
[13910.205859] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205862] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205864] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205867] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205870] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205872] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205875] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.205881] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205884] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04403000 from client 18
[13910.205886] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205889] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205892] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205894] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205897] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205899] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205902] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.205910] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205913] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04404000 from client 18
[13910.205916] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205918] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205921] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205923] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205926] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205928] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205931] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.205939] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205942] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04405000 from client 18
[13910.205945] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205947] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205950] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205952] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205955] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205957] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205960] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.205967] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemset pid 74577 thread hipMemset pid 74577)
[13910.205970] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fab04406000 from client 18
[13910.205973] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13910.205976] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13910.205978] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13910.205981] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13910.205983] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13910.205986] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13910.205988] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13910.300679] amdgpu: Started evicting pasid 0x8002
[13910.300692] amdgpu: Finished evicting pasid 0x8002
[13921.290681] amdgpu: Started evicting pasid 0x8002
[13921.290696] amdgpu: Finished evicting pasid 0x8002
[13921.450889] amdgpu: Started evicting pasid 0x8002
[13921.450902] amdgpu: Finished evicting pasid 0x8002
[13921.610727] amdgpu: Started evicting pasid 0x8002
[13921.610742] amdgpu: Finished evicting pasid 0x8002
[13921.771826] amdgpu: Started evicting pasid 0x8002
[13921.771839] amdgpu: Finished evicting pasid 0x8002
[13921.934745] amdgpu: Started evicting pasid 0x8002
[13921.934760] amdgpu: Finished evicting pasid 0x8002
[13922.096026] amdgpu: Started evicting pasid 0x8002
[13922.096041] amdgpu: Finished evicting pasid 0x8002
[13922.611409] amdgpu: Started evicting pasid 0x8002
[13922.611424] amdgpu: Finished evicting pasid 0x8002
[13922.773370] amdgpu: Started evicting pasid 0x8002
[13922.773385] amdgpu: Finished evicting pasid 0x8002
[13922.937386] amdgpu: Started evicting pasid 0x8002
[13922.937400] amdgpu: Finished evicting pasid 0x8002
[13923.097951] amdgpu: Started evicting pasid 0x8002
[13923.097965] amdgpu: Finished evicting pasid 0x8002
[13923.264401] amdgpu: Started evicting pasid 0x8002
[13923.264415] amdgpu: Finished evicting pasid 0x8002
[13923.439466] amdgpu: Started evicting pasid 0x8002
[13923.439478] amdgpu: Finished evicting pasid 0x8002
[13923.603310] amdgpu: Started evicting pasid 0x8002
[13923.603325] amdgpu: Finished evicting pasid 0x8002
[13923.766033] amdgpu: Started evicting pasid 0x8002
[13923.766047] amdgpu: Finished evicting pasid 0x8002
[13923.934753] amdgpu: Started evicting pasid 0x8002
[13923.934765] amdgpu: Finished evicting pasid 0x8002
[13924.100266] amdgpu: Started evicting pasid 0x8002
[13924.100281] amdgpu: Finished evicting pasid 0x8002
[13944.044337] amdgpu: Started evicting pasid 0x8002
[13944.044350] amdgpu: Finished evicting pasid 0x8002
[13944.203585] amdgpu: Started evicting pasid 0x8002
[13944.203600] amdgpu: Finished evicting pasid 0x8002
[13944.366710] amdgpu: Started evicting pasid 0x8002
[13944.366724] amdgpu: Finished evicting pasid 0x8002
[13945.114895] amdgpu: Started evicting pasid 0x8002
[13945.114910] amdgpu: Finished evicting pasid 0x8002
[13945.279861] amdgpu: Started evicting pasid 0x8002
[13945.279877] amdgpu: Finished evicting pasid 0x8002
[13945.440095] amdgpu: Started evicting pasid 0x8002
[13945.440109] amdgpu: Finished evicting pasid 0x8002
[13945.607187] amdgpu: Started evicting pasid 0x8002
[13945.607202] amdgpu: Finished evicting pasid 0x8002
[13945.615922] amdgpu: Started evicting pasid 0x8003
[13945.615936] amdgpu: Finished evicting pasid 0x8003
[13945.792160] amdgpu: Started evicting pasid 0x8002
[13945.792175] amdgpu: Finished evicting pasid 0x8002
[13945.931686] amdgpu: Started evicting pasid 0x8002
[13945.931700] amdgpu: Finished evicting pasid 0x8002
[13946.104176] amdgpu: Started evicting pasid 0x8002
[13946.104190] amdgpu: Finished evicting pasid 0x8002
[13946.246565] amdgpu: Started evicting pasid 0x8002
[13946.246579] amdgpu: Finished evicting pasid 0x8002
[13946.413523] amdgpu: Started evicting pasid 0x8002
[13946.413538] amdgpu: Finished evicting pasid 0x8002
[13946.582169] amdgpu: Started evicting pasid 0x8002
[13946.582184] amdgpu: Finished evicting pasid 0x8002
[13946.746341] amdgpu: Started evicting pasid 0x8002
[13946.746355] amdgpu: Finished evicting pasid 0x8002
[13946.914668] amdgpu: Started evicting pasid 0x8002
[13946.914684] amdgpu: Finished evicting pasid 0x8002
[13947.086657] amdgpu: Started evicting pasid 0x8002
[13947.086672] amdgpu: Finished evicting pasid 0x8002
[13947.248431] amdgpu: Started evicting pasid 0x8002
[13947.248445] amdgpu: Finished evicting pasid 0x8002
[13947.479878] amdgpu: Started evicting pasid 0x8002
[13947.479892] amdgpu: Finished evicting pasid 0x8002
[13947.642615] amdgpu: Started evicting pasid 0x8002
[13947.642630] amdgpu: Finished evicting pasid 0x8002
[13947.805687] amdgpu: Started evicting pasid 0x8002
[13947.805702] amdgpu: Finished evicting pasid 0x8002
[13947.978206] amdgpu: Started evicting pasid 0x8002
[13947.978221] amdgpu: Finished evicting pasid 0x8002
[13948.146683] amdgpu: Started evicting pasid 0x8002
[13948.146699] amdgpu: Finished evicting pasid 0x8002
[13948.662022] amdgpu: Started evicting pasid 0x8002
[13948.662037] amdgpu: Finished evicting pasid 0x8002
[13948.825718] amdgpu: Started evicting pasid 0x8002
[13948.825734] amdgpu: Finished evicting pasid 0x8002
[13948.986914] amdgpu: Started evicting pasid 0x8002
[13948.986929] amdgpu: Finished evicting pasid 0x8002
[13949.147441] amdgpu: Started evicting pasid 0x8002
[13949.147455] amdgpu: Finished evicting pasid 0x8002
[13949.308572] amdgpu: Started evicting pasid 0x8002
[13949.308586] amdgpu: Finished evicting pasid 0x8002
[13949.480637] amdgpu: Started evicting pasid 0x8002
[13949.480649] amdgpu: Finished evicting pasid 0x8002
[13949.643369] amdgpu: Started evicting pasid 0x8002
[13949.643384] amdgpu: Finished evicting pasid 0x8002
[13949.804757] amdgpu: Started evicting pasid 0x8002
[13949.804772] amdgpu: Finished evicting pasid 0x8002
[13950.191487] hipMemset[75808]: segfault at 0 ip 00007f5a5fcf6cf1 sp 00007fff04357700 error 4 in libc-2.27.so[7f5a5fc5f000+1e7000]
[13950.191493] Code: 0d dc 35 35 00 48 89 f0 48 f7 d8 f0 48 01 05 de 35 35 00 e8 d1 3b 08 00 e9 ac fe ff ff 0f 1f 40 00 4c 89 e8 48 25 00 00 00 fc <48> 8b 18 e9 aa fd ff ff 0f 1f 80 00 00 00 00 4c 3b 2d 29 5c 35 00
[13950.289077] amdgpu: Started evicting pasid 0x8002
[13950.289144] amdgpu: Finished evicting pasid 0x8002
[13951.881455] amdgpu: Started evicting pasid 0x8002
[13951.881522] amdgpu: Finished evicting pasid 0x8002
[13954.265460] amdgpu: Started evicting pasid 0x8002
[13954.265475] amdgpu: Finished evicting pasid 0x8002
[13954.749441] amdgpu: Started evicting pasid 0x8002
[13954.749455] amdgpu: Finished evicting pasid 0x8002
[13955.155910] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155915] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0200000 from client 18
[13955.155916] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13955.155918] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155919] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13955.155920] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.155921] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13955.155923] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.155924] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13955.155931] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155933] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0201000 from client 18
[13955.155934] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13955.155936] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155937] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13955.155938] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.155940] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13955.155941] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.155942] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13955.155947] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155948] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0202000 from client 18
[13955.155949] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13955.155951] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155952] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13955.155953] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.155955] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13955.155956] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.155957] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13955.155962] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155963] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0203000 from client 18
[13955.155965] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[13955.155966] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155968] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[13955.155969] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.155970] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[13955.155972] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.155973] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[13955.155977] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155978] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0204000 from client 18
[13955.155980] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13955.155981] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155982] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13955.155984] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.155985] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13955.155986] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.155988] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13955.155992] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.155994] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0205000 from client 18
[13955.155995] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13955.155996] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.155997] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13955.155999] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.156000] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13955.156001] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.156002] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13955.156008] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.156010] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0206000 from client 18
[13955.156011] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13955.156012] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.156013] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13955.156015] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.156016] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13955.156017] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.156018] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13955.156024] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.156026] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0207000 from client 18
[13955.156027] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13955.156028] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.156030] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13955.156031] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.156032] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13955.156034] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.156035] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13955.156041] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process hipMemsetAsyncM pid 76003 thread hipMemsetAsyncM pid 76003)
[13955.156042] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0ec0208000 from client 18
[13955.156044] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[13955.156045] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[13955.156047] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[13955.156048] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[13955.156049] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[13955.156051] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[13955.156052] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[13955.245749] amdgpu: Started evicting pasid 0x8002
[13955.245757] amdgpu: Finished evicting pasid 0x8002
[13955.739011] amdgpu: Started evicting pasid 0x8002
[13955.739027] amdgpu: Finished evicting pasid 0x8002
[13955.903057] amdgpu: Started evicting pasid 0x8002
[13955.903072] amdgpu: Finished evicting pasid 0x8002
[14320.182905] gmc_v9_0_process_interrupt: 27 callbacks suppressed
[14320.182915] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.182922] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a00000 from client 18
[14320.182926] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14320.182929] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.182932] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14320.182934] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.182937] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14320.182940] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.182942] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.182951] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.182955] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a01000 from client 18
[14320.182958] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14320.182961] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.182963] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14320.182966] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.182968] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14320.182971] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.182973] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.182980] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.182983] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a02000 from client 18
[14320.182986] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14320.182988] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.182991] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14320.182994] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.182996] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14320.182998] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183001] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183007] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183010] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a03000 from client 18
[14320.183013] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183016] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183018] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183020] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183023] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183026] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183028] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183036] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183039] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a04000 from client 18
[14320.183041] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183044] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183046] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183049] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183052] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183054] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183057] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183064] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183067] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a05000 from client 18
[14320.183070] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183073] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183075] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183078] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183080] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183083] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183085] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183094] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183097] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a00000 from client 18
[14320.183100] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183102] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183105] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183107] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183110] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183112] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183115] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183122] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183125] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a01000 from client 18
[14320.183128] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183130] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183133] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183135] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183138] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183140] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183143] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183151] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183154] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a02000 from client 18
[14320.183156] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183159] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183161] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183164] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183167] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183169] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183172] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.183179] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfBufferCo pid 9174 thread hipPerfBufferCo pid 9174)
[14320.183182] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff536a03000 from client 18
[14320.183185] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14320.183188] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14320.183190] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14320.183192] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14320.183195] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14320.183197] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14320.183200] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14320.280453] amdgpu: Started evicting pasid 0x8002
[14320.280466] amdgpu: Finished evicting pasid 0x8002
[14324.162434] amdgpu: Started evicting pasid 0x8002
[14324.162447] amdgpu: Finished evicting pasid 0x8002
[14326.808641] gmc_v9_0_process_interrupt: 30 callbacks suppressed
[14326.808650] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808658] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511501000 from client 18
[14326.808661] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14326.808664] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808667] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14326.808669] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808672] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14326.808674] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808677] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808692] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808695] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511502000 from client 18
[14326.808698] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14326.808700] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808703] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14326.808706] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808708] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14326.808711] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808713] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808721] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808725] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511501000 from client 18
[14326.808727] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14326.808730] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808732] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14326.808735] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808737] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14326.808740] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808742] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808749] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808752] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511502000 from client 18
[14326.808755] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14326.808757] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808760] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14326.808762] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808765] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14326.808767] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808770] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808776] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808779] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511503000 from client 18
[14326.808781] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14326.808784] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808787] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14326.808789] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808792] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14326.808794] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808796] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808803] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808807] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511501000 from client 18
[14326.808809] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
[14326.808812] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808814] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[14326.808817] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808819] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[14326.808822] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808824] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808831] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808834] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511502000 from client 18
[14326.808836] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14326.808839] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808842] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14326.808844] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808847] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14326.808849] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808852] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.808858] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process hipPerfSharedMe pid 12119 thread hipPerfSharedMe pid 12119)
[14326.808861] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fc511503000 from client 18
[14326.808863] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[14326.808866] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[14326.808868] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[14326.808871] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[14326.808873] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[14326.808876] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[14326.808878] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[14326.905200] amdgpu: Started evicting pasid 0x8002
[14326.905211] amdgpu: Finished evicting pasid 0x8002
[17680.680847] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.680854] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b01000 from client 18
[17680.680858] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17680.680861] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.680864] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17680.680867] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.680869] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17680.680872] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.680874] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17680.680886] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.680889] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b02000 from client 18
[17680.680892] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.680895] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.680897] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.680900] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.680903] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.680905] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.680908] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.680915] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.680918] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b03000 from client 18
[17680.680920] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.680923] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.680925] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.680928] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.680931] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.680933] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.680936] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.680942] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.680945] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b04000 from client 18
[17680.680947] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.680950] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.680953] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.680955] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.680958] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.680960] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.680963] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.681192] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.681195] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b01000 from client 18
[17680.681198] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17680.681201] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.681203] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17680.681206] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.681208] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17680.681211] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.681213] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17680.681220] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.681223] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b02000 from client 18
[17680.681225] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.681228] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.681230] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.681233] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.681235] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.681238] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.681240] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.681248] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.681251] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b03000 from client 18
[17680.681254] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.681256] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.681259] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.681261] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.681264] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.681266] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.681269] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.681276] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13084 thread python pid 13084)
[17680.681279] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007ff6e9b04000 from client 18
[17680.681282] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17680.681284] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17680.681287] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17680.681289] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17680.681292] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17680.681294] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17680.681297] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17680.783186] amdgpu: Started evicting pasid 0x8002
[17680.783195] amdgpu: Finished evicting pasid 0x8002
[17695.016805] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13454 thread python pid 13454)
[17695.016810] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7d4f01000 from client 18
[17695.016811] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17695.016813] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17695.016814] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17695.016815] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17695.016816] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17695.016817] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17695.016818] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17695.016826] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13454 thread python pid 13454)
[17695.016828] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7d4f02000 from client 18
[17695.016829] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17695.016830] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17695.016831] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17695.016833] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17695.016834] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17695.016835] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17695.016836] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17695.017176] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13454 thread python pid 13454)
[17695.017178] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7d4f01000 from client 18
[17695.017179] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17695.017180] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17695.017181] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17695.017183] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17695.017184] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17695.017185] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17695.017186] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17695.017190] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13454 thread python pid 13454)
[17695.017191] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7d4f02000 from client 18
[17695.017192] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17695.017193] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17695.017194] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17695.017195] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17695.017196] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17695.017197] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17695.017199] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17695.017205] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 13454 thread python pid 13454)
[17695.017206] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7d4f03000 from client 18
[17695.017208] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17695.017209] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17695.017210] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17695.017211] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17695.017212] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17695.017213] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17695.017214] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17695.118324] amdgpu: Started evicting pasid 0x8002
[17695.118337] amdgpu: Finished evicting pasid 0x8002
[17821.176133] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 16400 thread python pid 16400)
[17821.176139] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd3c7701000 from client 18
[17821.176142] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17821.176144] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17821.176146] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17821.176148] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17821.176150] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17821.176151] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17821.176153] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17821.176164] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 16400 thread python pid 16400)
[17821.176166] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd3c7702000 from client 18
[17821.176168] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17821.176170] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17821.176172] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17821.176173] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17821.176175] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17821.176177] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17821.176179] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17821.176355] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 16400 thread python pid 16400)
[17821.176358] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd3c7701000 from client 18
[17821.176360] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[17821.176361] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17821.176363] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[17821.176365] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17821.176367] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[17821.176368] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17821.176370] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[17821.176376] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 16400 thread python pid 16400)
[17821.176378] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd3c7702000 from client 18
[17821.176380] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[17821.176381] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[17821.176383] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[17821.176385] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[17821.176386] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[17821.176388] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[17821.176390] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[17821.271347] amdgpu: Started evicting pasid 0x8003
[17821.271357] amdgpu: Finished evicting pasid 0x8003
[18351.718477] perf: interrupt took too long (2503 > 2500), lowering kernel.perf_event_max_sample_rate to 79750
[18504.798488] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798496] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9b06400000 from client 27
[18504.798500] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00901031
[18504.798503] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[18504.798505] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[18504.798508] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798511] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[18504.798513] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798516] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798526] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798529] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9c38983000 from client 27
[18504.798532] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00901031
[18504.798535] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[18504.798537] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[18504.798540] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798542] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[18504.798545] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798547] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798556] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798559] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9c27793000 from client 27
[18504.798562] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798564] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798567] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798569] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798572] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798574] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798577] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798584] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798587] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9affeca000 from client 27
[18504.798590] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798592] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798595] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798597] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798600] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798602] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798605] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798612] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798615] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9af546b000 from client 27
[18504.798618] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798620] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798623] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798625] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798628] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798630] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798633] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798640] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798643] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9c2b91a000 from client 27
[18504.798645] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798648] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798650] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798653] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798655] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798658] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798660] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798668] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798671] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9e3da5d000 from client 27
[18504.798673] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798676] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798678] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798681] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798683] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798686] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798688] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798695] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798698] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9c27793000 from client 27
[18504.798701] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798703] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798706] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798708] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798711] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798713] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798716] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798723] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798726] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9c2b91a000 from client 27
[18504.798729] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798731] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798734] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798736] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798739] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798741] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798744] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.798751] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:9 pasid:32770, for process python pid 15494 thread python pid 15494)
[18504.798754] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f9e3da5d000 from client 27
[18504.798757] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18504.798759] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18504.798762] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18504.798764] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18504.798767] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18504.798769] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18504.798772] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18504.897150] amdgpu: Started evicting pasid 0x8002
[18504.897159] amdgpu: Finished evicting pasid 0x8002
[18574.035196] gmc_v9_0_process_interrupt: 18 callbacks suppressed
[18574.035200] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035203] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f001fecb000 from client 27
[18574.035204] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[18574.035205] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[18574.035206] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[18574.035207] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035208] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[18574.035209] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035209] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035214] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035215] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0015461000 from client 27
[18574.035216] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[18574.035217] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[18574.035217] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[18574.035218] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035219] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[18574.035220] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035220] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035225] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035225] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f03aa400000 from client 27
[18574.035226] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[18574.035227] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[18574.035228] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[18574.035228] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035229] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[18574.035230] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035230] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035234] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035235] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f004bbb2000 from client 27
[18574.035235] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035236] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035237] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035238] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035238] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035239] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035240] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035243] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035244] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f01a4e39000 from client 27
[18574.035244] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035245] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035246] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035247] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035247] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035248] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035249] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035252] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035253] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0199737000 from client 27
[18574.035253] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035254] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035255] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035255] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035256] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035257] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035258] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035261] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035262] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0142363000 from client 27
[18574.035262] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035263] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035264] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035264] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035265] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035266] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035267] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035270] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035271] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f0015461000 from client 27
[18574.035272] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035272] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035273] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035274] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035274] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035275] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035276] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035279] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035280] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f03aa400000 from client 27
[18574.035281] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035281] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035282] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035283] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035283] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035284] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035285] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.035288] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32771, for process python pid 18606 thread python pid 18606)
[18574.035289] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f01a4e39000 from client 27
[18574.035290] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[18574.035290] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[18574.035291] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[18574.035292] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[18574.035292] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[18574.035293] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[18574.035294] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[18574.131565] amdgpu: Started evicting pasid 0x8003
[18574.131574] amdgpu: Finished evicting pasid 0x8003
[18708.764839] amdgpu: Started evicting pasid 0x8002
[18708.764851] amdgpu: Finished evicting pasid 0x8002
[18708.865568] amdgpu: Started restoring pasid 0x8002
[18708.865587] amdgpu: Finished restoring pasid 0x8002
[18709.120078] amdgpu: Started evicting pasid 0x8002
[18709.120089] amdgpu: Finished evicting pasid 0x8002
[18709.221559] amdgpu: Started restoring pasid 0x8002
[18709.221580] amdgpu: Finished restoring pasid 0x8002
[18727.832497] amdgpu: Started evicting pasid 0x8002
[18727.832509] amdgpu: Finished evicting pasid 0x8002
[18727.935808] amdgpu: Started restoring pasid 0x8002
[18727.935832] amdgpu: Finished restoring pasid 0x8002
[18731.536477] amdgpu: Started evicting pasid 0x8002
[18731.536484] amdgpu: Finished evicting pasid 0x8002
[18731.639487] amdgpu: Started restoring pasid 0x8002
[18731.639510] amdgpu: Finished restoring pasid 0x8002
[18736.505265] amdgpu: Started evicting pasid 0x8002
[18736.505275] amdgpu: Finished evicting pasid 0x8002
[18736.607070] amdgpu: Started restoring pasid 0x8002
[18736.607094] amdgpu: Finished restoring pasid 0x8002
[18740.958221] amdgpu: Started evicting pasid 0x8003
[18740.958233] amdgpu: Finished evicting pasid 0x8003
[18741.058673] amdgpu: Started restoring pasid 0x8003
[18741.058696] amdgpu: Finished restoring pasid 0x8003
[18741.090255] amdgpu: Started evicting pasid 0x8003
[18741.090266] amdgpu: Finished evicting pasid 0x8003
[18741.190657] amdgpu: Started restoring pasid 0x8003
[18741.190679] amdgpu: Finished restoring pasid 0x8003
[18741.275150] amdgpu: Started evicting pasid 0x8002
[18741.275162] amdgpu: Finished evicting pasid 0x8002
[18741.378612] amdgpu: Started restoring pasid 0x8002
[18741.378637] amdgpu: Finished restoring pasid 0x8002
[18755.300310] amdgpu: Started evicting pasid 0x8002
[18755.300316] amdgpu: Finished evicting pasid 0x8002
[18755.401364] amdgpu: Started restoring pasid 0x8002
[18755.401386] amdgpu: Finished restoring pasid 0x8002
[18759.378120] amdgpu: Started evicting pasid 0x8003
[18759.378132] amdgpu: Finished evicting pasid 0x8003
[18759.381556] amdgpu: Started evicting pasid 0x8002
[18759.381564] amdgpu: Finished evicting pasid 0x8002
[18759.481036] amdgpu: Started restoring pasid 0x8003
[18759.481057] amdgpu: Finished restoring pasid 0x8003
[18759.485029] amdgpu: Started restoring pasid 0x8002
[18759.485046] amdgpu: Finished restoring pasid 0x8002
[18763.118514] amdgpu: Started evicting pasid 0x8003
[18763.118527] amdgpu: Finished evicting pasid 0x8003
[18763.220672] amdgpu: Started restoring pasid 0x8003
[18763.220694] amdgpu: Finished restoring pasid 0x8003
[18768.204975] amdgpu: Started evicting pasid 0x8003
[18768.204989] amdgpu: Finished evicting pasid 0x8003
[18768.308197] amdgpu: Started restoring pasid 0x8003
[18768.308221] amdgpu: Finished restoring pasid 0x8003
[18773.035990] amdgpu: Started evicting pasid 0x8003
[18773.036001] amdgpu: Finished evicting pasid 0x8003
[18773.139785] amdgpu: Started restoring pasid 0x8003
[18773.139807] amdgpu: Finished restoring pasid 0x8003
[18774.602860] amdgpu: Started evicting pasid 0x8002
[18774.602873] amdgpu: Finished evicting pasid 0x8002
[18774.703641] amdgpu: Started restoring pasid 0x8002
[18774.703663] amdgpu: Finished restoring pasid 0x8002
[18787.619369] amdgpu: Started evicting pasid 0x8003
[18787.619382] amdgpu: Finished evicting pasid 0x8003
[18787.722476] amdgpu: Started restoring pasid 0x8003
[18787.722496] amdgpu: Finished restoring pasid 0x8003
[18791.584518] amdgpu: Started evicting pasid 0x8003
[18791.584530] amdgpu: Finished evicting pasid 0x8003
[18791.686128] amdgpu: Started restoring pasid 0x8003
[18791.686150] amdgpu: Finished restoring pasid 0x8003
[18794.736983] amdgpu: Started evicting pasid 0x8002
[18794.736996] amdgpu: Finished evicting pasid 0x8002
[18794.837833] amdgpu: Started restoring pasid 0x8002
[18794.837849] amdgpu: Finished restoring pasid 0x8002
[18806.375860] amdgpu: Started evicting pasid 0x8003
[18806.375865] amdgpu: Finished evicting pasid 0x8003
[18806.476792] amdgpu: Started restoring pasid 0x8003
[18806.476813] amdgpu: Finished restoring pasid 0x8003
[18808.679747] amdgpu: Started evicting pasid 0x8002
[18808.679759] amdgpu: Finished evicting pasid 0x8002
[18808.780583] amdgpu: Started restoring pasid 0x8002
[18808.780604] amdgpu: Finished restoring pasid 0x8002
[18824.923933] amdgpu: Started evicting pasid 0x8002
[18824.923946] amdgpu: Finished evicting pasid 0x8002
[18825.027139] amdgpu: Started restoring pasid 0x8002
[18825.027155] amdgpu: Finished restoring pasid 0x8002
[18829.636183] amdgpu: Started evicting pasid 0x8003
[18829.636195] amdgpu: Finished evicting pasid 0x8003
[18829.738762] amdgpu: Started restoring pasid 0x8003
[18829.738783] amdgpu: Finished restoring pasid 0x8003
[18840.658331] amdgpu: Started evicting pasid 0x8002
[18840.658343] amdgpu: Finished evicting pasid 0x8002
[18840.761730] amdgpu: Started restoring pasid 0x8002
[18840.761746] amdgpu: Finished restoring pasid 0x8002
[18849.062630] amdgpu: Started evicting pasid 0x8003
[18849.062642] amdgpu: Finished evicting pasid 0x8003
[18849.164969] amdgpu: Started restoring pasid 0x8003
[18849.164993] amdgpu: Finished restoring pasid 0x8003
[18856.251365] amdgpu: Started evicting pasid 0x8002
[18856.251378] amdgpu: Finished evicting pasid 0x8002
[18856.352395] amdgpu: Started restoring pasid 0x8002
[18856.352414] amdgpu: Finished restoring pasid 0x8002
[18869.566681] amdgpu: Started evicting pasid 0x8003
[18869.566692] amdgpu: Finished evicting pasid 0x8003
[18869.667198] amdgpu: Started restoring pasid 0x8003
[18869.667221] amdgpu: Finished restoring pasid 0x8003
[18872.005154] amdgpu: Started evicting pasid 0x8002
[18872.005167] amdgpu: Finished evicting pasid 0x8002
[18872.106952] amdgpu: Started restoring pasid 0x8002
[18872.106978] amdgpu: Finished restoring pasid 0x8002
[18872.587916] amdgpu: Started evicting pasid 0x8002
[18872.587922] amdgpu: Finished evicting pasid 0x8002
[18872.694889] amdgpu: Started restoring pasid 0x8002
[18872.694914] amdgpu: Finished restoring pasid 0x8002
[18872.785142] amdgpu: Started evicting pasid 0x8002
[18872.785152] amdgpu: Finished evicting pasid 0x8002
[18872.886849] amdgpu: Started restoring pasid 0x8002
[18872.886875] amdgpu: Finished restoring pasid 0x8002
[18887.376691] amdgpu: Started evicting pasid 0x8002
[18887.376696] amdgpu: Finished evicting pasid 0x8002
[18887.477561] amdgpu: Started restoring pasid 0x8002
[18887.477582] amdgpu: Finished restoring pasid 0x8002
[18890.293084] amdgpu: Started evicting pasid 0x8003
[18890.293096] amdgpu: Finished evicting pasid 0x8003
[18890.393300] amdgpu: Started restoring pasid 0x8003
[18890.393323] amdgpu: Finished restoring pasid 0x8003
[18901.146480] amdgpu: Started evicting pasid 0x8002
[18901.146493] amdgpu: Finished evicting pasid 0x8002
[18901.248410] amdgpu: Started restoring pasid 0x8002
[18901.248432] amdgpu: Finished restoring pasid 0x8002
[18911.456314] amdgpu: Started evicting pasid 0x8003
[18911.456321] amdgpu: Finished evicting pasid 0x8003
[18911.559454] amdgpu: Started restoring pasid 0x8003
[18911.559476] amdgpu: Finished restoring pasid 0x8003
[18913.789845] amdgpu: Started evicting pasid 0x8002
[18913.789855] amdgpu: Finished evicting pasid 0x8002

---

### 评论 #8 — dshm (2021-03-02T07:45:14Z)

[18913.891239] amdgpu: Started restoring pasid 0x8002
[18913.891260] amdgpu: Finished restoring pasid 0x8002
[18927.485867] amdgpu: Started evicting pasid 0x8002
[18927.485880] amdgpu: Finished evicting pasid 0x8002
[18927.585916] amdgpu: Started restoring pasid 0x8002
[18927.585937] amdgpu: Finished restoring pasid 0x8002
[18932.902527] amdgpu: Started evicting pasid 0x8003
[18932.902538] amdgpu: Finished evicting pasid 0x8003
[18933.005529] amdgpu: Started restoring pasid 0x8003
[18933.005551] amdgpu: Finished restoring pasid 0x8003
[18933.294835] amdgpu: Started evicting pasid 0x8003
[18933.294841] amdgpu: Finished evicting pasid 0x8003
[18933.397446] amdgpu: Started restoring pasid 0x8003
[18933.397468] amdgpu: Finished restoring pasid 0x8003
[18933.435340] amdgpu: Started evicting pasid 0x8003
[18933.435352] amdgpu: Finished evicting pasid 0x8003
[18933.537476] amdgpu: Started restoring pasid 0x8003
[18933.537497] amdgpu: Finished restoring pasid 0x8003
[18941.533720] amdgpu: Started evicting pasid 0x8002
[18941.533733] amdgpu: Finished evicting pasid 0x8002
[18941.636704] amdgpu: Started restoring pasid 0x8002
[18941.636726] amdgpu: Finished restoring pasid 0x8002
[18947.198656] amdgpu: Started evicting pasid 0x8003
[18947.198663] amdgpu: Finished evicting pasid 0x8003
[18947.300202] amdgpu: Started restoring pasid 0x8003
[18947.300224] amdgpu: Finished restoring pasid 0x8003
[18954.628592] amdgpu: Started evicting pasid 0x8002
[18954.628597] amdgpu: Finished evicting pasid 0x8002
[18954.731540] amdgpu: Started restoring pasid 0x8002
[18954.731562] amdgpu: Finished restoring pasid 0x8002
[18961.574346] amdgpu: Started evicting pasid 0x8003
[18961.574359] amdgpu: Finished evicting pasid 0x8003
[18961.674908] amdgpu: Started restoring pasid 0x8003
[18961.674931] amdgpu: Finished restoring pasid 0x8003
[18964.457429] amdgpu: Started evicting pasid 0x8002
[18964.457434] amdgpu: Finished evicting pasid 0x8002
[18964.558725] amdgpu: Started restoring pasid 0x8002
[18964.558748] amdgpu: Finished restoring pasid 0x8002
[18974.592179] amdgpu: Started evicting pasid 0x8003
[18974.592186] amdgpu: Finished evicting pasid 0x8003
[18974.693730] amdgpu: Started restoring pasid 0x8003
[18974.693750] amdgpu: Finished restoring pasid 0x8003
[18987.275053] amdgpu: Started evicting pasid 0x8003
[18987.275065] amdgpu: Finished evicting pasid 0x8003
[18987.376612] amdgpu: Started restoring pasid 0x8003
[18987.376636] amdgpu: Finished restoring pasid 0x8003
[18999.973076] amdgpu: Started evicting pasid 0x8003
[18999.973082] amdgpu: Finished evicting pasid 0x8003
[19000.075520] amdgpu: Started restoring pasid 0x8003
[19000.075544] amdgpu: Finished restoring pasid 0x8003
[19012.746062] amdgpu: Started evicting pasid 0x8003
[19012.746075] amdgpu: Finished evicting pasid 0x8003
[19012.846274] amdgpu: Started restoring pasid 0x8003
[19012.846308] amdgpu: Finished restoring pasid 0x8003
[19022.732687] amdgpu: Started evicting pasid 0x8003
[19022.732700] amdgpu: Finished evicting pasid 0x8003
[19022.833453] amdgpu: Started restoring pasid 0x8003
[19022.833471] amdgpu: Finished restoring pasid 0x8003
[19127.027168] gmc_v9_0_process_interrupt: 22 callbacks suppressed
[19127.027175] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 56653 thread python pid 56653)
[19127.027179] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdfc1301000 from client 18
[19127.027181] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19127.027183] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19127.027184] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19127.027186] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19127.027187] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19127.027188] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19127.027190] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19127.027199] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 56653 thread python pid 56653)
[19127.027200] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdfc1302000 from client 18
[19127.027202] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19127.027203] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19127.027204] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19127.027206] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19127.027207] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19127.027208] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19127.027210] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19127.027499] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 56653 thread python pid 56653)
[19127.027502] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdfc1301000 from client 18
[19127.027503] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19127.027504] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19127.027506] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19127.027507] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19127.027508] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19127.027510] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19127.027511] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19127.027515] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 56653 thread python pid 56653)
[19127.027517] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdfc1302000 from client 18
[19127.027518] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19127.027519] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19127.027521] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19127.027522] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19127.027523] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19127.027525] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19127.027526] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19127.027529] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 56653 thread python pid 56653)
[19127.027531] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fdfc1303000 from client 18
[19127.027532] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19127.027534] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19127.027535] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19127.027536] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19127.027537] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19127.027539] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19127.027540] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19127.116201] amdgpu: Started evicting pasid 0x8002
[19127.116208] amdgpu: Finished evicting pasid 0x8002
[19301.806185] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 60598 thread python pid 60598)
[19301.806190] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2ae4701000 from client 18
[19301.806192] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19301.806194] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19301.806195] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19301.806197] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19301.806198] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19301.806200] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19301.806201] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19301.806210] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 60598 thread python pid 60598)
[19301.806212] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2ae4702000 from client 18
[19301.806213] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19301.806215] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19301.806216] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19301.806217] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19301.806218] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19301.806220] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19301.806221] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19301.806511] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 60598 thread python pid 60598)
[19301.806513] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2ae4701000 from client 18
[19301.806515] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19301.806516] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19301.806517] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19301.806519] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19301.806520] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19301.806521] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19301.806522] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19301.806527] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 60598 thread python pid 60598)
[19301.806528] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2ae4702000 from client 18
[19301.806530] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19301.806531] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19301.806532] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19301.806534] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19301.806535] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19301.806536] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19301.806537] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19301.899670] amdgpu: Started evicting pasid 0x8002
[19301.899680] amdgpu: Finished evicting pasid 0x8002
[19441.099146] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 63792 thread python pid 63792)
[19441.099152] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2021901000 from client 18
[19441.099155] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19441.099158] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19441.099160] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19441.099162] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19441.099164] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19441.099166] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19441.099169] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19441.099181] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 63792 thread python pid 63792)
[19441.099184] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2021902000 from client 18
[19441.099186] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19441.099189] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19441.099191] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19441.099193] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19441.099195] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19441.099197] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19441.099199] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19441.099450] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 63792 thread python pid 63792)
[19441.099453] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2021901000 from client 18
[19441.099455] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19441.099457] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19441.099459] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19441.099462] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19441.099464] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19441.099466] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19441.099468] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19441.099473] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 63792 thread python pid 63792)
[19441.099476] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f2021902000 from client 18
[19441.099478] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19441.099480] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19441.099482] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19441.099484] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19441.099486] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19441.099489] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19441.099491] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19441.199105] amdgpu: Started evicting pasid 0x8002
[19441.199116] amdgpu: Finished evicting pasid 0x8002
[19459.490006] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 64225 thread python pid 64225)
[19459.490012] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd645b01000 from client 18
[19459.490014] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19459.490016] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19459.490017] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19459.490019] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19459.490020] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19459.490022] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19459.490023] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19459.490033] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 64225 thread python pid 64225)
[19459.490035] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd645b02000 from client 18
[19459.490037] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19459.490038] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19459.490040] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19459.490041] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19459.490043] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19459.490044] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19459.490045] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19459.490050] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 64225 thread python pid 64225)
[19459.490052] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd645b03000 from client 18
[19459.490054] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19459.490055] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19459.490056] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19459.490058] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19459.490059] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19459.490061] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19459.490062] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19459.490331] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 64225 thread python pid 64225)
[19459.490333] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd645b01000 from client 18
[19459.490334] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[19459.490335] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19459.490336] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[19459.490337] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19459.490338] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[19459.490339] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19459.490340] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[19459.490344] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 64225 thread python pid 64225)
[19459.490345] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fd645b02000 from client 18
[19459.490346] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[19459.490347] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[19459.490348] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[19459.490349] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[19459.490350] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[19459.490353] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[19459.490363] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[19459.578299] amdgpu: Started evicting pasid 0x8002
[19459.578307] amdgpu: Finished evicting pasid 0x8002
[31335.181888] perf: interrupt took too long (3159 > 3128), lowering kernel.perf_event_max_sample_rate to 63250
[76282.692519] perf: interrupt took too long (3950 > 3948), lowering kernel.perf_event_max_sample_rate to 50500
[86284.940658] IPv6: eno4: IPv6 duplicate address 2400:dd01:1034:800:d518:b7af:3949:fd82 used by 94:e4:ba:ed:c5:86 detected!
[86285.580493] IPv6: eno4: IPv6 duplicate address 2400:dd01:1034:800:b0a6:67e8:be5:8a08 used by 94:e4:ba:ed:c5:86 detected!
[86285.824559] IPv6: eno4: IPv6 duplicate address 2400:dd01:1034:800:642d:ca49:7435:a858 used by 94:e4:ba:ed:c5:86 detected!
[86285.824579] IPv6: ipv6_create_tempaddr: regeneration time exceeded - disabled temporary address support
[100760.089768] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.089776] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959301000 from client 18
[100760.089780] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[100760.089783] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.089786] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[100760.089788] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.089791] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[100760.089794] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.089796] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[100760.089822] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.089825] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959302000 from client 18
[100760.089827] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100760.089829] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.089831] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100760.089833] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.089835] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100760.089837] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.089839] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100760.089845] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.089847] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959303000 from client 18
[100760.089849] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100760.089851] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.089853] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100760.089855] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.089857] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100760.089859] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.089861] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100760.090082] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.090085] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959301000 from client 18
[100760.090088] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[100760.090090] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.090092] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[100760.090094] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.090096] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[100760.090098] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.090100] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[100760.090105] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.090107] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959302000 from client 18
[100760.090109] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100760.090111] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.090113] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100760.090115] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.090117] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100760.090119] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.090121] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100760.090131] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36706 thread python pid 36706)
[100760.090133] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f7959303000 from client 18
[100760.090135] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100760.090137] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100760.090139] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100760.090141] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100760.090143] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100760.090145] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100760.090147] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100760.179464] amdgpu: Started evicting pasid 0x8002
[100760.179473] amdgpu: Finished evicting pasid 0x8002
[100774.533037] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533042] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568301000 from client 18
[100774.533044] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[100774.533046] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533048] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[100774.533049] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533051] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[100774.533052] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533054] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[100774.533062] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533064] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568302000 from client 18
[100774.533066] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533067] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533069] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533070] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533072] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533073] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533074] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.533079] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533081] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568303000 from client 18
[100774.533082] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533083] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533085] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533086] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533088] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533089] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533091] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.533095] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533096] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568304000 from client 18
[100774.533098] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533099] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533101] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533102] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533104] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533105] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533106] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.533345] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533348] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568301000 from client 18
[100774.533350] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[100774.533352] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533354] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[100774.533356] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533358] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[100774.533360] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533362] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[100774.533367] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533369] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568302000 from client 18
[100774.533371] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533373] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533375] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533377] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533379] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533381] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533383] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.533388] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533390] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568303000 from client 18
[100774.533393] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533395] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533397] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533398] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533400] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533402] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533404] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.533414] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 36848 thread python pid 36848)
[100774.533424] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f3568304000 from client 18
[100774.533434] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[100774.533443] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[100774.533453] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[100774.533462] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[100774.533471] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[100774.533480] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[100774.533490] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[100774.626607] amdgpu: Started evicting pasid 0x8002
[100774.626622] amdgpu: Finished evicting pasid 0x8002
[101431.765746] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 29400 thread python pid 29400)
[101431.765750] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe55fb01000 from client 18
[101431.765752] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[101431.765754] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101431.765755] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[101431.765757] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101431.765758] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[101431.765759] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101431.765761] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[101431.765770] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 29400 thread python pid 29400)
[101431.765771] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe55fb02000 from client 18
[101431.765773] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101431.765774] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101431.765775] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101431.765777] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101431.765778] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101431.765779] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101431.765781] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101431.765958] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 29400 thread python pid 29400)
[101431.765960] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe55fb01000 from client 18
[101431.765961] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[101431.765963] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101431.765964] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[101431.765965] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101431.765967] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[101431.765968] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101431.765969] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[101431.765973] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 29400 thread python pid 29400)
[101431.765975] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe55fb02000 from client 18
[101431.765976] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101431.765977] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101431.765979] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101431.765980] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101431.765981] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101431.765982] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101431.765984] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101431.765987] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32771, for process python pid 29400 thread python pid 29400)
[101431.765989] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe55fb03000 from client 18
[101431.765990] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101431.765992] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101431.765993] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101431.765994] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101431.765995] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101431.765997] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101431.765998] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101431.866409] amdgpu: Started evicting pasid 0x8003
[101431.866420] amdgpu: Finished evicting pasid 0x8003
[101441.675127] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675130] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f63d3359000 from client 27
[101441.675131] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[101441.675132] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[101441.675133] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[101441.675134] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675135] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[101441.675136] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675136] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675142] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675143] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f62a7eca000 from client 27
[101441.675144] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[101441.675145] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[101441.675145] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[101441.675146] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675147] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[101441.675148] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675148] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675152] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675153] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f632e400000 from client 27
[101441.675154] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[101441.675154] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[101441.675155] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[101441.675156] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675156] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[101441.675157] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675158] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675161] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675162] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f633d01b000 from client 27
[101441.675163] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675164] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675164] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675165] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675166] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675166] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675167] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675171] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675171] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f62d010d000 from client 27
[101441.675172] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675173] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675174] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675175] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675176] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675176] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675177] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675180] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675181] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f629d461000 from client 27
[101441.675182] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675183] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675183] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675184] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675185] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675185] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675186] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675189] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675190] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f62a7ecb000 from client 27
[101441.675191] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675192] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675192] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675193] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675194] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675194] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675195] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675198] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675199] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f63d335e000 from client 27
[101441.675200] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675201] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675202] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675202] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675203] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675204] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675204] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675208] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675209] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f63d335e000 from client 27
[101441.675209] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675210] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675211] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675212] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675212] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675213] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675214] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.675218] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 37784 thread python pid 37784)
[101441.675219] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f631fe4c000 from client 27
[101441.675219] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[101441.675220] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[101441.675221] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[101441.675221] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[101441.675222] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[101441.675223] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[101441.675224] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[101441.773475] amdgpu: Started evicting pasid 0x8002
[101441.773485] amdgpu: Finished evicting pasid 0x8002
[102969.330436] amdgpu: Started evicting pasid 0x8002
[102969.330477] amdgpu: Finished evicting pasid 0x8002
[102969.433770] amdgpu: Started restoring pasid 0x8002
[102969.433832] amdgpu: Finished restoring pasid 0x8002
[102969.850605] amdgpu: Started evicting pasid 0x8002
[102969.850647] amdgpu: Finished evicting pasid 0x8002
[102969.953703] amdgpu: Started restoring pasid 0x8002
[102969.953771] amdgpu: Finished restoring pasid 0x8002
[102970.463330] amdgpu: Started evicting pasid 0x8002
[102970.463373] amdgpu: Finished evicting pasid 0x8002
[102970.565648] amdgpu: Started restoring pasid 0x8002
[102970.565721] amdgpu: Finished restoring pasid 0x8002
[102970.855797] amdgpu: Started evicting pasid 0x8002
[102970.855839] amdgpu: Finished evicting pasid 0x8002
[102970.957659] amdgpu: Started restoring pasid 0x8002
[102970.957737] amdgpu: Finished restoring pasid 0x8002
[102971.682277] amdgpu: Started evicting pasid 0x8002
[102971.682316] amdgpu: Finished evicting pasid 0x8002
[102971.785514] amdgpu: Started restoring pasid 0x8002
[102971.785594] amdgpu: Finished restoring pasid 0x8002
[102974.768054] amdgpu: Started evicting pasid 0x8002
[102974.768091] amdgpu: Finished evicting pasid 0x8002
[102974.869292] amdgpu: Started restoring pasid 0x8002
[102974.869360] amdgpu: Finished restoring pasid 0x8002
[102974.901490] amdgpu: Started evicting pasid 0x8002
[102974.901575] amdgpu: Finished evicting pasid 0x8002
[102975.005275] amdgpu: Started restoring pasid 0x8002
[102975.005353] amdgpu: Finished restoring pasid 0x8002
[102975.667261] amdgpu: Started evicting pasid 0x8002
[102975.667298] amdgpu: Finished evicting pasid 0x8002
[102975.769222] amdgpu: Started restoring pasid 0x8002
[102975.769301] amdgpu: Finished restoring pasid 0x8002
[102979.217913] amdgpu: Started evicting pasid 0x8002
[102979.217953] amdgpu: Finished evicting pasid 0x8002
[102979.320867] amdgpu: Started restoring pasid 0x8002
[102979.320949] amdgpu: Finished restoring pasid 0x8002
[102979.525184] amdgpu: Started evicting pasid 0x8002
[102979.525223] amdgpu: Finished evicting pasid 0x8002
[102979.628877] amdgpu: Started restoring pasid 0x8002
[102979.628955] amdgpu: Finished restoring pasid 0x8002
[102982.813859] amdgpu: Started evicting pasid 0x8002
[102982.813898] amdgpu: Finished evicting pasid 0x8002
[102982.916545] amdgpu: Started restoring pasid 0x8002
[102982.916623] amdgpu: Finished restoring pasid 0x8002
[102982.941835] amdgpu: Started evicting pasid 0x8002
[102982.941882] amdgpu: Finished evicting pasid 0x8002
[102983.044435] amdgpu: Started restoring pasid 0x8002
[102983.044509] amdgpu: Finished restoring pasid 0x8002
[102986.836624] amdgpu: Started evicting pasid 0x8002
[102986.836677] amdgpu: Finished evicting pasid 0x8002
[102986.940202] amdgpu: Started restoring pasid 0x8002
[102986.940299] amdgpu: Finished restoring pasid 0x8002
[102987.829630] amdgpu: Started evicting pasid 0x8002
[102987.829680] amdgpu: Finished evicting pasid 0x8002
[102987.932090] amdgpu: Started restoring pasid 0x8002
[102987.932188] amdgpu: Finished restoring pasid 0x8002
[102990.129367] amdgpu: Started evicting pasid 0x8002
[102990.129417] amdgpu: Finished evicting pasid 0x8002
[102990.231870] amdgpu: Started restoring pasid 0x8002
[102990.231968] amdgpu: Finished restoring pasid 0x8002
[102990.281061] amdgpu: Started evicting pasid 0x8002
[102990.281113] amdgpu: Finished evicting pasid 0x8002
[102990.383897] amdgpu: Started restoring pasid 0x8002
[102990.383993] amdgpu: Finished restoring pasid 0x8002
[102991.250120] amdgpu: Started evicting pasid 0x8002
[102991.250171] amdgpu: Finished evicting pasid 0x8002
[102991.351809] amdgpu: Started restoring pasid 0x8002
[102991.351906] amdgpu: Finished restoring pasid 0x8002
[102992.140224] amdgpu: Started evicting pasid 0x8002
[102992.140276] amdgpu: Finished evicting pasid 0x8002
[102992.243758] amdgpu: Started restoring pasid 0x8002
[102992.243855] amdgpu: Finished restoring pasid 0x8002
[102992.692233] amdgpu: Started evicting pasid 0x8002
[102992.693201] amdgpu: Finished evicting pasid 0x8002
[102992.795857] amdgpu: Started restoring pasid 0x8002
[102992.795947] amdgpu: Finished restoring pasid 0x8002
[104658.807196] amdgpu: Started evicting pasid 0x8002
[104658.807270] amdgpu: Finished evicting pasid 0x8002
[104658.910458] amdgpu: Started restoring pasid 0x8002
[104658.910573] amdgpu: Finished restoring pasid 0x8002
[104793.153221] amdgpu: Started evicting pasid 0x8002
[104793.153278] amdgpu: Finished evicting pasid 0x8002
[104808.287237] amdgpu: Started evicting pasid 0x8002
[104808.287279] amdgpu: Finished evicting pasid 0x8002
[104808.389022] amdgpu: Started restoring pasid 0x8002
[104808.389087] amdgpu: Finished restoring pasid 0x8002
[104808.810588] amdgpu: Started evicting pasid 0x8002
[104808.810630] amdgpu: Finished evicting pasid 0x8002
[104808.912978] amdgpu: Started restoring pasid 0x8002
[104808.913046] amdgpu: Finished restoring pasid 0x8002
[104809.406722] amdgpu: Started evicting pasid 0x8002
[104809.406760] amdgpu: Finished evicting pasid 0x8002
[104809.508943] amdgpu: Started restoring pasid 0x8002
[104809.509009] amdgpu: Finished restoring pasid 0x8002
[104809.810123] amdgpu: Started evicting pasid 0x8002
[104809.810164] amdgpu: Finished evicting pasid 0x8002
[104809.912930] amdgpu: Started restoring pasid 0x8002
[104809.913006] amdgpu: Finished restoring pasid 0x8002
[104810.619593] amdgpu: Started evicting pasid 0x8002
[104810.619636] amdgpu: Finished evicting pasid 0x8002
[104810.720860] amdgpu: Started restoring pasid 0x8002
[104810.720936] amdgpu: Finished restoring pasid 0x8002
[104813.693439] amdgpu: Started evicting pasid 0x8002
[104813.693477] amdgpu: Finished evicting pasid 0x8002
[104813.796449] amdgpu: Started restoring pasid 0x8002
[104813.796507] amdgpu: Finished restoring pasid 0x8002
[104813.824563] amdgpu: Started evicting pasid 0x8002
[104813.824653] amdgpu: Finished evicting pasid 0x8002
[104813.928567] amdgpu: Started restoring pasid 0x8002
[104813.928646] amdgpu: Finished restoring pasid 0x8002
[104814.598595] amdgpu: Started evicting pasid 0x8002
[104814.598635] amdgpu: Finished evicting pasid 0x8002
[104814.700481] amdgpu: Started restoring pasid 0x8002
[104814.700567] amdgpu: Finished restoring pasid 0x8002
[104818.009220] amdgpu: Started evicting pasid 0x8002
[104818.009262] amdgpu: Finished evicting pasid 0x8002
[104818.112173] amdgpu: Started restoring pasid 0x8002
[104818.112253] amdgpu: Finished restoring pasid 0x8002
[104818.326541] amdgpu: Started evicting pasid 0x8002
[104818.326582] amdgpu: Finished evicting pasid 0x8002
[104818.428097] amdgpu: Started restoring pasid 0x8002
[104818.428185] amdgpu: Finished restoring pasid 0x8002
[104821.580867] amdgpu: Started evicting pasid 0x8002
[104821.580909] amdgpu: Finished evicting pasid 0x8002
[104821.683865] amdgpu: Started restoring pasid 0x8002
[104821.683947] amdgpu: Finished restoring pasid 0x8002
[104821.710663] amdgpu: Started evicting pasid 0x8002
[104821.710709] amdgpu: Finished evicting pasid 0x8002
[104821.811864] amdgpu: Started restoring pasid 0x8002
[104821.811941] amdgpu: Finished restoring pasid 0x8002
[104825.565227] amdgpu: Started evicting pasid 0x8002
[104825.565278] amdgpu: Finished evicting pasid 0x8002
[104825.667482] amdgpu: Started restoring pasid 0x8002
[104825.667585] amdgpu: Finished restoring pasid 0x8002
[104826.571486] amdgpu: Started evicting pasid 0x8002
[104826.571540] amdgpu: Finished evicting pasid 0x8002
[104826.675428] amdgpu: Started restoring pasid 0x8002
[104826.675531] amdgpu: Finished restoring pasid 0x8002
[104828.874437] amdgpu: Started evicting pasid 0x8002
[104828.874487] amdgpu: Finished evicting pasid 0x8002
[104828.975101] amdgpu: Started restoring pasid 0x8002
[104828.975207] amdgpu: Finished restoring pasid 0x8002
[104829.023715] amdgpu: Started evicting pasid 0x8002
[104829.023768] amdgpu: Finished evicting pasid 0x8002
[104829.127230] amdgpu: Started restoring pasid 0x8002
[104829.127331] amdgpu: Finished restoring pasid 0x8002
[104830.007258] amdgpu: Started evicting pasid 0x8002
[104830.007313] amdgpu: Finished evicting pasid 0x8002
[104830.111082] amdgpu: Started restoring pasid 0x8002
[104830.111186] amdgpu: Finished restoring pasid 0x8002
[104830.910820] amdgpu: Started evicting pasid 0x8002
[104830.910873] amdgpu: Finished evicting pasid 0x8002
[104831.010998] amdgpu: Started restoring pasid 0x8002
[104831.011117] amdgpu: Finished restoring pasid 0x8002
[104831.469321] amdgpu: Started evicting pasid 0x8002
[104831.469441] amdgpu: Finished evicting pasid 0x8002
[104831.570947] amdgpu: Started restoring pasid 0x8002
[104831.571062] amdgpu: Finished restoring pasid 0x8002
[105347.268849] perf: interrupt took too long (4940 > 4937), lowering kernel.perf_event_max_sample_rate to 40250
[112195.537430] show_signal_msg: 22 callbacks suppressed
[112195.537435] mytest[29781]: segfault at 0 ip 0000559ad41cd916 sp 00007ffef77f2280 error 6 in mytest[559ad41cd000+1000]
[112195.537446] Code: 20 00 01 5d c3 0f 1f 80 00 00 00 00 f3 c3 66 0f 1f 44 00 00 55 48 89 e5 5d e9 66 ff ff ff 55 48 89 e5 48 83 ec 10 48 8b 45 f8 <c7> 00 01 00 00 00 48 8d 35 62 01 00 00 48 8d 3d f6 06 20 00 e8 81
[112383.986833] mytest[34228]: segfault at 0 ip 0000556d07263916 sp 00007fff6add47f0 error 6 in mytest[556d07263000+1000]
[112383.986844] Code: 20 00 01 5d c3 0f 1f 80 00 00 00 00 f3 c3 66 0f 1f 44 00 00 55 48 89 e5 5d e9 66 ff ff ff 55 48 89 e5 48 83 ec 10 48 8b 45 f8 <c7> 00 01 00 00 00 48 8d 35 62 01 00 00 48 8d 3d f6 06 20 00 e8 81
[117005.849546] amdgpu: Started evicting pasid 0x8002
[117005.849598] amdgpu: Finished evicting pasid 0x8002
[117005.952843] amdgpu: Started restoring pasid 0x8002
[117005.953039] amdgpu: Finished restoring pasid 0x8002
[117006.352626] amdgpu: Started evicting pasid 0x8002
[117006.352676] amdgpu: Finished evicting pasid 0x8002
[117006.452849] amdgpu: Started restoring pasid 0x8002
[117006.452963] amdgpu: Finished restoring pasid 0x8002
[117006.561225] amdgpu: Started evicting pasid 0x8002
[117006.561296] amdgpu: Finished evicting pasid 0x8002
[117006.664851] amdgpu: Started restoring pasid 0x8002
[117006.664968] amdgpu: Finished restoring pasid 0x8002
[117007.929318] amdgpu: Started evicting pasid 0x8002
[117007.929377] amdgpu: Finished evicting pasid 0x8002
[117008.032711] amdgpu: Started restoring pasid 0x8002
[117008.032800] amdgpu: Finished restoring pasid 0x8002
[117008.377150] amdgpu: Started evicting pasid 0x8002
[117008.377202] amdgpu: Finished evicting pasid 0x8002
[117008.480660] amdgpu: Started restoring pasid 0x8002
[117008.480751] amdgpu: Finished restoring pasid 0x8002
[117008.807035] amdgpu: Started evicting pasid 0x8002
[117008.807088] amdgpu: Finished evicting pasid 0x8002
[117008.908633] amdgpu: Started restoring pasid 0x8002
[117008.908730] amdgpu: Finished restoring pasid 0x8002
[117009.474388] amdgpu: Started evicting pasid 0x8002
[117009.474441] amdgpu: Finished evicting pasid 0x8002
[117009.576655] amdgpu: Started restoring pasid 0x8002
[117009.576754] amdgpu: Finished restoring pasid 0x8002
[117009.936388] amdgpu: Started evicting pasid 0x8002
[117009.936440] amdgpu: Finished evicting pasid 0x8002
[117010.036500] amdgpu: Started restoring pasid 0x8002
[117010.036617] amdgpu: Finished restoring pasid 0x8002
[117010.319090] amdgpu: Started evicting pasid 0x8002
[117010.319143] amdgpu: Finished evicting pasid 0x8002
[117010.420399] amdgpu: Started restoring pasid 0x8002
[117010.420498] amdgpu: Finished restoring pasid 0x8002
[117010.736777] amdgpu: Started evicting pasid 0x8002
[117010.736831] amdgpu: Finished evicting pasid 0x8002
[117010.840450] amdgpu: Started restoring pasid 0x8002
[117010.840548] amdgpu: Finished restoring pasid 0x8002
[117011.619193] amdgpu: Started evicting pasid 0x8002
[117011.619254] amdgpu: Finished evicting pasid 0x8002
[117011.720405] amdgpu: Started restoring pasid 0x8002
[117011.720502] amdgpu: Finished restoring pasid 0x8002
[117012.308275] amdgpu: Started evicting pasid 0x8002
[117012.308330] amdgpu: Finished evicting pasid 0x8002
[117012.412277] amdgpu: Started restoring pasid 0x8002
[117012.412363] amdgpu: Finished restoring pasid 0x8002
[117012.726364] amdgpu: Started evicting pasid 0x8002
[117012.726415] amdgpu: Finished evicting pasid 0x8002
[117012.828291] amdgpu: Started restoring pasid 0x8002
[117012.828391] amdgpu: Finished restoring pasid 0x8002
[117013.126888] amdgpu: Started evicting pasid 0x8002
[117013.126941] amdgpu: Finished evicting pasid 0x8002
[117013.228288] amdgpu: Started restoring pasid 0x8002
[117013.228390] amdgpu: Finished restoring pasid 0x8002
[117013.528905] amdgpu: Started evicting pasid 0x8002
[117013.528910] amdgpu: Finished evicting pasid 0x8002
[117013.632247] amdgpu: Started restoring pasid 0x8002
[117013.632348] amdgpu: Finished restoring pasid 0x8002
[117014.267772] amdgpu: Started evicting pasid 0x8002
[117014.267822] amdgpu: Finished evicting pasid 0x8002
[117014.368189] amdgpu: Started restoring pasid 0x8002
[117014.368290] amdgpu: Finished restoring pasid 0x8002
[117014.973801] amdgpu: Started evicting pasid 0x8002
[117014.973855] amdgpu: Finished evicting pasid 0x8002
[117015.076102] amdgpu: Started restoring pasid 0x8002
[117015.076205] amdgpu: Finished restoring pasid 0x8002
[117015.402934] amdgpu: Started evicting pasid 0x8002
[117015.402985] amdgpu: Finished evicting pasid 0x8002
[117015.504072] amdgpu: Started restoring pasid 0x8002
[117015.504174] amdgpu: Finished restoring pasid 0x8002
[117015.784831] amdgpu: Started evicting pasid 0x8002
[117015.784886] amdgpu: Finished evicting pasid 0x8002
[117015.887983] amdgpu: Started restoring pasid 0x8002
[117015.888086] amdgpu: Finished restoring pasid 0x8002
[117016.192244] amdgpu: Started evicting pasid 0x8002
[117016.192252] amdgpu: Finished evicting pasid 0x8002
[117016.295942] amdgpu: Started restoring pasid 0x8002
[117016.296039] amdgpu: Finished restoring pasid 0x8002
[117017.027174] amdgpu: Started evicting pasid 0x8002
[117017.027224] amdgpu: Finished evicting pasid 0x8002
[117017.127945] amdgpu: Started restoring pasid 0x8002
[117017.128052] amdgpu: Finished restoring pasid 0x8002
[117017.457193] amdgpu: Started evicting pasid 0x8002
[117017.457243] amdgpu: Finished evicting pasid 0x8002
[117017.559905] amdgpu: Started restoring pasid 0x8002
[117017.560008] amdgpu: Finished restoring pasid 0x8002
[117017.891766] amdgpu: Started evicting pasid 0x8002
[117017.891817] amdgpu: Finished evicting pasid 0x8002
[117017.995812] amdgpu: Started restoring pasid 0x8002
[117017.995919] amdgpu: Finished restoring pasid 0x8002
[117018.048755] amdgpu: Started evicting pasid 0x8002
[117018.048809] amdgpu: Finished evicting pasid 0x8002
[117018.151885] amdgpu: Started restoring pasid 0x8002
[117018.151997] amdgpu: Finished restoring pasid 0x8002
[117018.713843] amdgpu: Started evicting pasid 0x8002
[117018.713895] amdgpu: Finished evicting pasid 0x8002
[117018.815805] amdgpu: Started restoring pasid 0x8002
[117018.815909] amdgpu: Finished restoring pasid 0x8002
[117019.431480] amdgpu: Started evicting pasid 0x8002
[117019.431531] amdgpu: Finished evicting pasid 0x8002
[117019.531729] amdgpu: Started restoring pasid 0x8002
[117019.531830] amdgpu: Finished restoring pasid 0x8002
[117020.174328] amdgpu: Started evicting pasid 0x8002
[117020.174379] amdgpu: Finished evicting pasid 0x8002
[117020.275620] amdgpu: Started restoring pasid 0x8002
[117020.275721] amdgpu: Finished restoring pasid 0x8002
[117020.555164] amdgpu: Started evicting pasid 0x8002
[117020.555215] amdgpu: Finished evicting pasid 0x8002
[117020.655518] amdgpu: Started restoring pasid 0x8002
[117020.655623] amdgpu: Finished restoring pasid 0x8002
[117020.954233] amdgpu: Started evicting pasid 0x8002
[117020.954285] amdgpu: Finished evicting pasid 0x8002
[117021.055544] amdgpu: Started restoring pasid 0x8002
[117021.055646] amdgpu: Finished restoring pasid 0x8002
[117021.120250] amdgpu: Started evicting pasid 0x8002
[117021.120302] amdgpu: Finished evicting pasid 0x8002
[117021.223576] amdgpu: Started restoring pasid 0x8002
[117021.223683] amdgpu: Finished restoring pasid 0x8002
[117022.203904] amdgpu: Started evicting pasid 0x8002
[117022.203981] amdgpu: Finished evicting pasid 0x8002
[117022.307429] amdgpu: Started restoring pasid 0x8002
[117022.307534] amdgpu: Finished restoring pasid 0x8002
[117022.362143] amdgpu: Started evicting pasid 0x8002
[117022.362197] amdgpu: Finished evicting pasid 0x8002
[117022.463362] amdgpu: Started restoring pasid 0x8002
[117022.463466] amdgpu: Finished restoring pasid 0x8002
[117023.150823] amdgpu: Started evicting pasid 0x8002
[117023.150899] amdgpu: Finished evicting pasid 0x8002
[117023.251438] amdgpu: Started restoring pasid 0x8002
[117023.251542] amdgpu: Finished restoring pasid 0x8002
[117023.846737] amdgpu: Started evicting pasid 0x8002
[117023.846790] amdgpu: Finished evicting pasid 0x8002
[117023.947329] amdgpu: Started restoring pasid 0x8002
[117023.947434] amdgpu: Finished restoring pasid 0x8002
[117024.268834] amdgpu: Started evicting pasid 0x8002
[117024.268888] amdgpu: Finished evicting pasid 0x8002
[117024.371271] amdgpu: Started restoring pasid 0x8002
[117024.371350] amdgpu: Finished restoring pasid 0x8002
[117024.431253] amdgpu: Started evicting pasid 0x8002
[117024.431307] amdgpu: Finished evicting pasid 0x8002
[117024.535270] amdgpu: Started restoring pasid 0x8002
[117024.535376] amdgpu: Finished restoring pasid 0x8002
[117025.151449] amdgpu: Started evicting pasid 0x8002
[117025.151502] amdgpu: Finished evicting pasid 0x8002
[117025.255213] amdgpu: Started restoring pasid 0x8002
[117025.255318] amdgpu: Finished restoring pasid 0x8002
[117025.956704] amdgpu: Started evicting pasid 0x8002
[117025.956758] amdgpu: Finished evicting pasid 0x8002
[117026.059084] amdgpu: Started restoring pasid 0x8002
[117026.059189] amdgpu: Finished restoring pasid 0x8002
[117028.554898] amdgpu: Started evicting pasid 0x8002
[117028.554947] amdgpu: Finished evicting pasid 0x8002
[117028.658939] amdgpu: Started restoring pasid 0x8002
[117028.659033] amdgpu: Finished restoring pasid 0x8002
[117028.739553] amdgpu: Started evicting pasid 0x8002
[117028.739561] amdgpu: Finished evicting pasid 0x8002
[117028.842913] amdgpu: Started restoring pasid 0x8002
[117028.843009] amdgpu: Finished restoring pasid 0x8002
[117029.683067] amdgpu: Started evicting pasid 0x8002
[117029.683121] amdgpu: Finished evicting pasid 0x8002
[117029.790813] amdgpu: Started restoring pasid 0x8002
[117029.790914] amdgpu: Finished restoring pasid 0x8002
[117030.056073] amdgpu: Started evicting pasid 0x8002
[117030.056127] amdgpu: Finished evicting pasid 0x8002
[117030.158806] amdgpu: Started restoring pasid 0x8002
[117030.158906] amdgpu: Finished restoring pasid 0x8002
[117030.455187] amdgpu: Started evicting pasid 0x8002
[117030.455239] amdgpu: Finished evicting pasid 0x8002
[117030.562758] amdgpu: Started restoring pasid 0x8002
[117030.562855] amdgpu: Finished restoring pasid 0x8002
[117030.630426] amdgpu: Started evicting pasid 0x8002
[117030.630476] amdgpu: Finished evicting pasid 0x8002
[117030.734926] amdgpu: Started restoring pasid 0x8002
[117030.735009] amdgpu: Finished restoring pasid 0x8002
[117032.284068] amdgpu: Started evicting pasid 0x8002
[117032.284120] amdgpu: Finished evicting pasid 0x8002
[117032.386493] amdgpu: Started restoring pasid 0x8002
[117032.386593] amdgpu: Finished restoring pasid 0x8002
[117034.521089] amdgpu: Started evicting pasid 0x8002
[117034.521137] amdgpu: Finished evicting pasid 0x8002
[117034.622406] amdgpu: Started restoring pasid 0x8002
[117034.622509] amdgpu: Finished restoring pasid 0x8002
[117034.686485] amdgpu: Started evicting pasid 0x8002
[117034.686543] amdgpu: Finished evicting pasid 0x8002
[117034.790403] amdgpu: Started restoring pasid 0x8002
[117034.790507] amdgpu: Finished restoring pasid 0x8002
[117035.477880] amdgpu: Started evicting pasid 0x8002
[117035.477933] amdgpu: Finished evicting pasid 0x8002
[117035.578294] amdgpu: Started restoring pasid 0x8002
[117035.578384] amdgpu: Finished restoring pasid 0x8002
[117036.237651] amdgpu: Started evicting pasid 0x8002
[117036.237701] amdgpu: Finished evicting pasid 0x8002
[117036.338250] amdgpu: Started restoring pasid 0x8002
[117036.338351] amdgpu: Finished restoring pasid 0x8002
[117038.466952] amdgpu: Started evicting pasid 0x8002
[117038.467003] amdgpu: Finished evicting pasid 0x8002
[117038.570060] amdgpu: Started restoring pasid 0x8002
[117038.570165] amdgpu: Finished restoring pasid 0x8002
[117038.627684] amdgpu: Started evicting pasid 0x8002
[117038.627735] amdgpu: Finished evicting pasid 0x8002
[117038.730022] amdgpu: Started restoring pasid 0x8002
[117038.730140] amdgpu: Finished restoring pasid 0x8002
[117039.086062] amdgpu: Started evicting pasid 0x8002
[117039.086123] amdgpu: Finished evicting pasid 0x8002
[117039.189954] amdgpu: Started restoring pasid 0x8002
[117039.190032] amdgpu: Finished restoring pasid 0x8002
[117039.261314] amdgpu: Started evicting pasid 0x8002
[117039.261375] amdgpu: Finished evicting pasid 0x8002
[117039.361948] amdgpu: Started restoring pasid 0x8002
[117039.362053] amdgpu: Finished restoring pasid 0x8002
[117039.896706] amdgpu: Started evicting pasid 0x8002
[117039.896755] amdgpu: Finished evicting pasid 0x8002
[117039.997963] amdgpu: Started restoring pasid 0x8002
[117039.998063] amdgpu: Finished restoring pasid 0x8002
[117040.768246] amdgpu: Started evicting pasid 0x8002
[117040.768301] amdgpu: Finished evicting pasid 0x8002
[117040.869814] amdgpu: Started restoring pasid 0x8002
[117040.869911] amdgpu: Finished restoring pasid 0x8002
[117043.877799] amdgpu: Started evicting pasid 0x8002
[117043.877849] amdgpu: Finished evicting pasid 0x8002
[117043.981584] amdgpu: Started restoring pasid 0x8002
[117043.981680] amdgpu: Finished restoring pasid 0x8002
[117044.055422] amdgpu: Started evicting pasid 0x8002
[117044.055473] amdgpu: Finished evicting pasid 0x8002
[117044.157534] amdgpu: Started restoring pasid 0x8002
[117044.157625] amdgpu: Finished restoring pasid 0x8002
[117045.001988] amdgpu: Started evicting pasid 0x8002
[117045.002040] amdgpu: Finished evicting pasid 0x8002
[117045.105512] amdgpu: Started restoring pasid 0x8002
[117045.105610] amdgpu: Finished restoring pasid 0x8002
[117045.373118] amdgpu: Started evicting pasid 0x8002
[117045.373173] amdgpu: Finished evicting pasid 0x8002
[117045.473475] amdgpu: Started restoring pasid 0x8002
[117045.473573] amdgpu: Finished restoring pasid 0x8002
[117045.770904] amdgpu: Started evicting pasid 0x8002
[117045.770955] amdgpu: Finished evicting pasid 0x8002
[117045.873446] amdgpu: Started restoring pasid 0x8002
[117045.873530] amdgpu: Finished restoring pasid 0x8002
[117045.933620] amdgpu: Started evicting pasid 0x8002
[117045.933675] amdgpu: Finished evicting pasid 0x8002
[117046.037430] amdgpu: Started restoring pasid 0x8002
[117046.037535] amdgpu: Finished restoring pasid 0x8002
[117047.335327] amdgpu: Started evicting pasid 0x8002
[117047.335380] amdgpu: Finished evicting pasid 0x8002
[117047.437306] amdgpu: Started restoring pasid 0x8002
[117047.437401] amdgpu: Finished restoring pasid 0x8002
[117050.562580] amdgpu: Started evicting pasid 0x8002
[117050.562629] amdgpu: Finished evicting pasid 0x8002
[117050.665030] amdgpu: Started restoring pasid 0x8002
[117050.665118] amdgpu: Finished restoring pasid 0x8002
[117050.731447] amdgpu: Started evicting pasid 0x8002
[117050.731499] amdgpu: Finished evicting pasid 0x8002
[117050.832986] amdgpu: Started restoring pasid 0x8002
[117050.833078] amdgpu: Finished restoring pasid 0x8002
[117051.520997] amdgpu: Started evicting pasid 0x8002
[117051.521052] amdgpu: Finished evicting pasid 0x8002
[117051.624949] amdgpu: Started restoring pasid 0x8002
[117051.625047] amdgpu: Finished restoring pasid 0x8002
[117052.267975] amdgpu: Started evicting pasid 0x8002
[117052.268027] amdgpu: Finished evicting pasid 0x8002
[117052.368889] amdgpu: Started restoring pasid 0x8002
[117052.368980] amdgpu: Finished restoring pasid 0x8002
[117055.546641] amdgpu: Started evicting pasid 0x8002
[117055.546691] amdgpu: Finished evicting pasid 0x8002
[117055.648596] amdgpu: Started restoring pasid 0x8002
[117055.648692] amdgpu: Finished restoring pasid 0x8002
[117055.705361] amdgpu: Started evicting pasid 0x8002
[117055.705413] amdgpu: Finished evicting pasid 0x8002
[117055.808458] amdgpu: Started restoring pasid 0x8002
[117055.808545] amdgpu: Finished restoring pasid 0x8002
[117056.147720] amdgpu: Started evicting pasid 0x8002
[117056.147771] amdgpu: Finished evicting pasid 0x8002
[117056.248551] amdgpu: Started restoring pasid 0x8002
[117056.248636] amdgpu: Finished restoring pasid 0x8002
[117056.558656] amdgpu: Started evicting pasid 0x8002
[117056.558710] amdgpu: Finished evicting pasid 0x8002
[117056.660446] amdgpu: Started restoring pasid 0x8002
[117056.660528] amdgpu: Finished restoring pasid 0x8002
[117056.753369] amdgpu: Started evicting pasid 0x8002
[117056.753419] amdgpu: Finished evicting pasid 0x8002
[117056.856370] amdgpu: Started restoring pasid 0x8002
[117056.856464] amdgpu: Finished restoring pasid 0x8002
[117057.417492] amdgpu: Started evicting pasid 0x8002
[117057.417562] amdgpu: Finished evicting pasid 0x8002
[117057.520429] amdgpu: Started restoring pasid 0x8002
[117057.520529] amdgpu: Finished restoring pasid 0x8002
[117058.139085] amdgpu: Started evicting pasid 0x8002
[117058.139136] amdgpu: Finished evicting pasid 0x8002
[117058.240334] amdgpu: Started restoring pasid 0x8002
[117058.240425] amdgpu: Finished restoring pasid 0x8002
[117061.522970] amdgpu: Started evicting pasid 0x8002
[117061.523020] amdgpu: Finished evicting pasid 0x8002
[117061.624091] amdgpu: Started restoring pasid 0x8002
[117061.624184] amdgpu: Finished restoring pasid 0x8002
[117061.759750] amdgpu: Started evicting pasid 0x8002
[117061.759801] amdgpu: Finished evicting pasid 0x8002
[117061.860060] amdgpu: Started restoring pasid 0x8002
[117061.860156] amdgpu: Finished restoring pasid 0x8002
[117062.191645] amdgpu: Started evicting pasid 0x8002
[117062.191695] amdgpu: Finished evicting pasid 0x8002
[117062.292036] amdgpu: Started restoring pasid 0x8002
[117062.292136] amdgpu: Finished restoring pasid 0x8002
[117063.010495] amdgpu: Started evicting pasid 0x8002
[117063.010548] amdgpu: Finished evicting pasid 0x8002
[117063.112093] amdgpu: Started restoring pasid 0x8002
[117063.112186] amdgpu: Finished restoring pasid 0x8002
[117063.821233] amdgpu: Started evicting pasid 0x8002
[117063.821286] amdgpu: Finished evicting pasid 0x8002
[117063.923872] amdgpu: Started restoring pasid 0x8002
[117063.923970] amdgpu: Finished restoring pasid 0x8002
[117064.639518] amdgpu: Started evicting pasid 0x8002
[117064.639570] amdgpu: Finished evicting pasid 0x8002
[117064.739824] amdgpu: Started restoring pasid 0x8002
[117064.739924] amdgpu: Finished restoring pasid 0x8002
[117065.458008] amdgpu: Started evicting pasid 0x8002
[117065.458096] amdgpu: Finished evicting pasid 0x8002
[117065.559738] amdgpu: Started restoring pasid 0x8002
[117065.559820] amdgpu: Finished restoring pasid 0x8002
[117066.110985] amdgpu: Started evicting pasid 0x8002
[117066.111037] amdgpu: Finished evicting pasid 0x8002
[117066.211699] amdgpu: Started restoring pasid 0x8002
[117066.211793] amdgpu: Finished restoring pasid 0x8002
[117222.652000] amdgpu: Started evicting pasid 0x8002
[117222.652054] amdgpu: Finished evicting pasid 0x8002
[117222.754064] amdgpu: Started restoring pasid 0x8002
[117222.754147] amdgpu: Finished restoring pasid 0x8002
[117226.717286] amdgpu: Started evicting pasid 0x8002
[117226.717334] amdgpu: Finished evicting pasid 0x8002
[117226.817647] amdgpu: Started restoring pasid 0x8002
[117226.817730] amdgpu: Finished restoring pasid 0x8002
[117227.058141] amdgpu: Started evicting pasid 0x8002
[117227.058193] amdgpu: Finished evicting pasid 0x8002
[117227.161621] amdgpu: Started restoring pasid 0x8002
[117227.161709] amdgpu: Finished restoring pasid 0x8002
[117229.944132] amdgpu: Started evicting pasid 0x8002
[117229.944188] amdgpu: Finished evicting pasid 0x8002
[117230.045394] amdgpu: Started restoring pasid 0x8002
[117230.045475] amdgpu: Finished restoring pasid 0x8002
[117230.439796] amdgpu: Started evicting pasid 0x8002
[117230.439848] amdgpu: Finished evicting pasid 0x8002
[117230.541334] amdgpu: Started restoring pasid 0x8002
[117230.541417] amdgpu: Finished restoring pasid 0x8002
[117233.311748] amdgpu: Started evicting pasid 0x8002
[117233.311797] amdgpu: Finished evicting pasid 0x8002
[117233.413095] amdgpu: Started restoring pasid 0x8002
[117233.413175] amdgpu: Finished restoring pasid 0x8002
[117234.033362] amdgpu: Started evicting pasid 0x8002
[117234.033438] amdgpu: Finished evicting pasid 0x8002
[117234.136977] amdgpu: Started restoring pasid 0x8002
[117234.137065] amdgpu: Finished restoring pasid 0x8002
[117234.225710] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.225720] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba00000 from client 18
[117234.225723] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[117234.225726] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.225729] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[117234.225732] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.225735] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[117234.225738] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.225741] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[117234.225752] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.225756] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba01000 from client 18
[117234.225759] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[117234.225762] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.225765] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[117234.225767] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.225770] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[117234.225772] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.225775] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[117234.225782] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.225785] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba02000 from client 18
[117234.225788] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[117234.225791] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.225793] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[117234.225796] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.225798] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[117234.225801] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.225803] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[117234.226177] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.226180] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba00000 from client 18
[117234.226182] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[117234.226185] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.226187] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[117234.226190] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.226192] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[117234.226195] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.226197] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[117234.226204] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.226207] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba01000 from client 18
[117234.226209] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[117234.226212] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.226215] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[117234.226218] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.226220] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[117234.226223] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.226226] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[117234.226234] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 11888 thread python pid 11888)
[117234.226238] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f4a4ba02000 from client 18
[117234.226240] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[117234.226243] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[117234.226246] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[117234.226248] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[117234.226251] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[117234.226253] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[117234.226256] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[117234.323121] amdgpu: Started evicting pasid 0x8002
[117234.323129] amdgpu: Finished evicting pasid 0x8002
[150653.992946] SGI XFS with ACLs, security attributes, realtime, no debug enabled
[150654.021880] JFS: nTxBlock = 8192, nTxLock = 65536
[150654.071473] ntfs: driver 2.1.32 [Flags: R/O MODULE].
[150654.151694] QNX4 filesystem 0.2.3 registered.
[423765.380239] amdgpu: Started evicting pasid 0x8002
[423765.380249] amdgpu: Finished evicting pasid 0x8002
[423765.485767] amdgpu: Started restoring pasid 0x8002
[423765.485786] amdgpu: Finished restoring pasid 0x8002
[423787.066877] amdgpu: Started evicting pasid 0x8002
[423787.066888] amdgpu: Finished evicting pasid 0x8002
[423787.167773] amdgpu: Started restoring pasid 0x8002
[423787.167797] amdgpu: Finished restoring pasid 0x8002
[423819.709435] amdgpu: Started evicting pasid 0x8003
[423819.709467] amdgpu: Finished evicting pasid 0x8003
[423819.812716] amdgpu: Started restoring pasid 0x8003
[423819.812760] amdgpu: Finished restoring pasid 0x8003
[423979.565886] amdgpu: Started evicting pasid 0x8002
[423979.565898] amdgpu: Finished evicting pasid 0x8002
[423979.669830] amdgpu: Started restoring pasid 0x8002
[423979.669855] amdgpu: Finished restoring pasid 0x8002
[423982.013374] amdgpu: Started evicting pasid 0x8002
[423982.013385] amdgpu: Finished evicting pasid 0x8002
[423982.113610] amdgpu: Started restoring pasid 0x8002
[423982.113633] amdgpu: Finished restoring pasid 0x8002
[423982.961876] amdgpu: Started evicting pasid 0x8003
[423982.961887] amdgpu: Finished evicting pasid 0x8003
[423983.065525] amdgpu: Started restoring pasid 0x8003
[423983.065570] amdgpu: Finished restoring pasid 0x8003
[423985.317982] amdgpu: Started evicting pasid 0x8002
[423985.317994] amdgpu: Finished evicting pasid 0x8002
[423985.421306] amdgpu: Started restoring pasid 0x8002
[423985.421326] amdgpu: Finished restoring pasid 0x8002
[423986.209338] amdgpu: Started evicting pasid 0x8003
[423986.209350] amdgpu: Finished evicting pasid 0x8003
[423986.313266] amdgpu: Started restoring pasid 0x8003
[423986.313308] amdgpu: Finished restoring pasid 0x8003
[423986.582513] amdgpu: Started evicting pasid 0x8003
[423986.582524] amdgpu: Finished evicting pasid 0x8003
[423986.685224] amdgpu: Started restoring pasid 0x8003
[423986.685262] amdgpu: Finished restoring pasid 0x8003
[423987.127440] amdgpu: Started evicting pasid 0x8003
[423987.127451] amdgpu: Finished evicting pasid 0x8003
[423987.229123] amdgpu: Started restoring pasid 0x8003
[423987.229167] amdgpu: Finished restoring pasid 0x8003
[428158.895953] docker0: port 1(vethe249af1) entered blocking state
[428158.895958] docker0: port 1(vethe249af1) entered disabled state
[428158.896121] device vethe249af1 entered promiscuous mode
[428159.206987] eth0: renamed from veth173912b
[428159.236444] IPv6: ADDRCONF(NETDEV_CHANGE): vethe249af1: link becomes ready
[428159.236557] docker0: port 1(vethe249af1) entered blocking state
[428159.236561] docker0: port 1(vethe249af1) entered forwarding state
[428159.236870] IPv6: ADDRCONF(NETDEV_CHANGE): docker0: link becomes ready
[428621.642629] docker0: port 1(vethe249af1) entered disabled state
[428621.642754] veth173912b: renamed from eth0
[428621.700578] docker0: port 1(vethe249af1) entered disabled state
[428621.705282] device vethe249af1 left promiscuous mode
[428621.705290] docker0: port 1(vethe249af1) entered disabled state
[428625.460364] docker0: port 1(veth89c13f9) entered blocking state
[428625.460368] docker0: port 1(veth89c13f9) entered disabled state
[428625.460780] device veth89c13f9 entered promiscuous mode
[428625.742961] eth0: renamed from vethefc1ab0
[428625.774815] IPv6: ADDRCONF(NETDEV_CHANGE): veth89c13f9: link becomes ready
[428625.774940] docker0: port 1(veth89c13f9) entered blocking state
[428625.774944] docker0: port 1(veth89c13f9) entered forwarding state
[430713.003515] vethefc1ab0: renamed from eth0
[430713.061345] docker0: port 1(veth89c13f9) entered disabled state
[430713.062831] docker0: port 1(veth89c13f9) entered disabled state
[430713.068611] device veth89c13f9 left promiscuous mode
[430713.068616] docker0: port 1(veth89c13f9) entered disabled state
[430716.767278] docker0: port 1(veth51acb5d) entered blocking state
[430716.767283] docker0: port 1(veth51acb5d) entered disabled state
[430716.767634] device veth51acb5d entered promiscuous mode
[430717.040777] eth0: renamed from veth4c76f27
[430717.072694] IPv6: ADDRCONF(NETDEV_CHANGE): veth51acb5d: link becomes ready
[430717.072823] docker0: port 1(veth51acb5d) entered blocking state
[430717.072826] docker0: port 1(veth51acb5d) entered forwarding state
[438075.183812] veth4c76f27: renamed from eth0
[438075.250773] docker0: port 1(veth51acb5d) entered disabled state
[438075.252634] docker0: port 1(veth51acb5d) entered disabled state
[438075.256981] device veth51acb5d left promiscuous mode
[438075.256986] docker0: port 1(veth51acb5d) entered disabled state
[438174.024522] docker0: port 1(vethfc742c2) entered blocking state
[438174.024526] docker0: port 1(vethfc742c2) entered disabled state
[438174.024848] device vethfc742c2 entered promiscuous mode
[438174.294988] eth0: renamed from veth9bf34da
[438174.339117] IPv6: ADDRCONF(NETDEV_CHANGE): vethfc742c2: link becomes ready
[438174.339233] docker0: port 1(vethfc742c2) entered blocking state
[438174.339236] docker0: port 1(vethfc742c2) entered forwarding state
[438555.638828] veth9bf34da: renamed from eth0
[438555.703950] docker0: port 1(vethfc742c2) entered disabled state
[438555.705482] docker0: port 1(vethfc742c2) entered disabled state
[438555.709860] device vethfc742c2 left promiscuous mode
[438555.709865] docker0: port 1(vethfc742c2) entered disabled state
[438723.936833] docker0: port 1(vethe8e696c) entered blocking state
[438723.936838] docker0: port 1(vethe8e696c) entered disabled state
[438723.937157] device vethe8e696c entered promiscuous mode
[438724.241917] eth0: renamed from veth7417dcc
[438724.273734] IPv6: ADDRCONF(NETDEV_CHANGE): vethe8e696c: link becomes ready
[438724.273858] docker0: port 1(vethe8e696c) entered blocking state
[438724.273860] docker0: port 1(vethe8e696c) entered forwarding state
[439193.482496] veth7417dcc: renamed from eth0
[439193.550437] docker0: port 1(vethe8e696c) entered disabled state
[439193.552299] docker0: port 1(vethe8e696c) entered disabled state
[439193.556395] device vethe8e696c left promiscuous mode
[439193.556399] docker0: port 1(vethe8e696c) entered disabled state
[439718.687585] docker0: port 1(veth97aaea8) entered blocking state
[439718.687588] docker0: port 1(veth97aaea8) entered disabled state
[439718.687849] device veth97aaea8 entered promiscuous mode
[439718.969128] eth0: renamed from veth7bfab19
[439718.994204] IPv6: ADDRCONF(NETDEV_CHANGE): veth97aaea8: link becomes ready
[439718.994360] docker0: port 1(veth97aaea8) entered blocking state
[439718.994365] docker0: port 1(veth97aaea8) entered forwarding state
[439719.136786] docker0: port 1(veth97aaea8) entered disabled state
[439719.136902] veth7bfab19: renamed from eth0
[439719.211796] docker0: port 1(veth97aaea8) entered disabled state
[439719.217532] device veth97aaea8 left promiscuous mode
[439719.217539] docker0: port 1(veth97aaea8) entered disabled state
[439719.899160] docker0: port 1(veth3a6fb1a) entered blocking state
[439719.899165] docker0: port 1(veth3a6fb1a) entered disabled state
[439719.899641] device veth3a6fb1a entered promiscuous mode
[439719.899917] docker0: port 1(veth3a6fb1a) entered blocking state
[439719.899920] docker0: port 1(veth3a6fb1a) entered forwarding state
[439719.900373] docker0: port 1(veth3a6fb1a) entered disabled state
[439720.160914] eth0: renamed from vethd116197
[439720.192763] IPv6: ADDRCONF(NETDEV_CHANGE): veth3a6fb1a: link becomes ready
[439720.192900] docker0: port 1(veth3a6fb1a) entered blocking state
[439720.192903] docker0: port 1(veth3a6fb1a) entered forwarding state
[440045.047324] vethd116197: renamed from eth0
[440045.110666] docker0: port 1(veth3a6fb1a) entered disabled state
[440045.113431] docker0: port 1(veth3a6fb1a) entered disabled state
[440045.118323] device veth3a6fb1a left promiscuous mode
[440045.118328] docker0: port 1(veth3a6fb1a) entered disabled state
[440059.246492] docker0: port 1(vethca94e25) entered blocking state
[440059.246496] docker0: port 1(vethca94e25) entered disabled state
[440059.246868] device vethca94e25 entered promiscuous mode
[440059.526441] eth0: renamed from veth077c903
[440059.558521] IPv6: ADDRCONF(NETDEV_CHANGE): vethca94e25: link becomes ready
[440059.558638] docker0: port 1(vethca94e25) entered blocking state
[440059.558641] docker0: port 1(vethca94e25) entered forwarding state
[440217.393245] docker0: port 1(vethca94e25) entered disabled state
[440217.393433] veth077c903: renamed from eth0
[440217.445077] docker0: port 1(vethca94e25) entered disabled state
[440217.451551] device vethca94e25 left promiscuous mode
[440217.451561] docker0: port 1(vethca94e25) entered disabled state
[440441.591641] docker0: port 1(veth24c83d3) entered blocking state
[440441.591645] docker0: port 1(veth24c83d3) entered disabled state
[440441.591952] device veth24c83d3 entered promiscuous mode
[440441.844920] eth0: renamed from veth3c4b377
[440441.870390] IPv6: ADDRCONF(NETDEV_CHANGE): veth24c83d3: link becomes ready
[440441.870530] docker0: port 1(veth24c83d3) entered blocking state
[440441.870532] docker0: port 1(veth24c83d3) entered forwarding state
[440558.947049] veth3c4b377: renamed from eth0
[440559.033630] docker0: port 1(veth24c83d3) entered disabled state
[440559.035526] docker0: port 1(veth24c83d3) entered disabled state
[440559.039987] device veth24c83d3 left promiscuous mode
[440559.039992] docker0: port 1(veth24c83d3) entered disabled state
[440673.873917] docker0: port 1(veth775cbc9) entered blocking state
[440673.873922] docker0: port 1(veth775cbc9) entered disabled state
[440673.874299] device veth775cbc9 entered promiscuous mode
[440674.272226] eth0: renamed from vethd8712c9
[440674.332168] IPv6: ADDRCONF(NETDEV_CHANGE): veth775cbc9: link becomes ready
[440674.332302] docker0: port 1(veth775cbc9) entered blocking state
[440674.332305] docker0: port 1(veth775cbc9) entered forwarding state
[440897.132669] vethd8712c9: renamed from eth0
[440897.208542] docker0: port 1(veth775cbc9) entered disabled state
[440897.210045] docker0: port 1(veth775cbc9) entered disabled state
[440897.214640] device veth775cbc9 left promiscuous mode
[440897.214645] docker0: port 1(veth775cbc9) entered disabled state
[440925.791591] docker0: port 1(vethf13efd8) entered blocking state
[440925.791596] docker0: port 1(vethf13efd8) entered disabled state
[440925.791908] device vethf13efd8 entered promiscuous mode
[440926.069985] eth0: renamed from veth95518de
[440926.111321] IPv6: ADDRCONF(NETDEV_CHANGE): vethf13efd8: link becomes ready
[440926.111451] docker0: port 1(vethf13efd8) entered blocking state
[440926.111454] docker0: port 1(vethf13efd8) entered forwarding state
[441252.476884] veth95518de: renamed from eth0
[441252.531864] docker0: port 1(vethf13efd8) entered disabled state
[441252.533448] docker0: port 1(vethf13efd8) entered disabled state
[441252.537077] device vethf13efd8 left promiscuous mode
[441252.537083] docker0: port 1(vethf13efd8) entered disabled state
[441267.947206] docker0: port 1(vethfdf2efc) entered blocking state
[441267.947210] docker0: port 1(vethfdf2efc) entered disabled state
[441267.947571] device vethfdf2efc entered promiscuous mode
[441268.239712] eth0: renamed from veth4a4eacf
[441268.271607] IPv6: ADDRCONF(NETDEV_CHANGE): vethfdf2efc: link becomes ready
[441268.271738] docker0: port 1(vethfdf2efc) entered blocking state
[441268.271741] docker0: port 1(vethfdf2efc) entered forwarding state
[441297.157143] docker0: port 1(vethfdf2efc) entered disabled state
[441297.157319] veth4a4eacf: renamed from eth0
[441297.219298] docker0: port 1(vethfdf2efc) entered disabled state
[441297.223866] device vethfdf2efc left promiscuous mode
[441297.223871] docker0: port 1(vethfdf2efc) entered disabled state
[441400.030611] docker0: port 1(veth994b253) entered blocking state
[441400.030615] docker0: port 1(veth994b253) entered disabled state
[441400.030942] device veth994b253 entered promiscuous mode
[441400.347954] eth0: renamed from vethf600c53
[441400.395681] IPv6: ADDRCONF(NETDEV_CHANGE): veth994b253: link becomes ready
[441400.395843] docker0: port 1(veth994b253) entered blocking state
[441400.395848] docker0: port 1(veth994b253) entered forwarding state
[441400.648753] docker0: port 1(veth994b253) entered disabled state
[441400.648916] vethf600c53: renamed from eth0
[441400.702694] docker0: port 1(veth994b253) entered disabled state
[441400.708550] device veth994b253 left promiscuous mode
[441400.708558] docker0: port 1(veth994b253) entered disabled state
[441401.461152] docker0: port 1(veth272e535) entered blocking state
[441401.461156] docker0: port 1(veth272e535) entered disabled state
[441401.461438] device veth272e535 entered promiscuous mode
[441401.461743] docker0: port 1(veth272e535) entered blocking state
[441401.461746] docker0: port 1(veth272e535) entered forwarding state
[441401.462361] docker0: port 1(veth272e535) entered disabled state
[441401.735884] eth0: renamed from veth63dce81
[441401.767617] IPv6: ADDRCONF(NETDEV_CHANGE): veth272e535: link becomes ready
[441401.767747] docker0: port 1(veth272e535) entered blocking state
[441401.767751] docker0: port 1(veth272e535) entered forwarding state
[441661.929232] veth63dce81: renamed from eth0
[441661.988392] docker0: port 1(veth272e535) entered disabled state
[441661.991437] docker0: port 1(veth272e535) entered disabled state
[441661.996282] device veth272e535 left promiscuous mode
[441661.996287] docker0: port 1(veth272e535) entered disabled state
[441673.273435] docker0: port 1(vethe7ab64d) entered blocking state
[441673.273439] docker0: port 1(vethe7ab64d) entered disabled state
[441673.273709] device vethe7ab64d entered promiscuous mode
[441673.551410] eth0: renamed from veth1d04a2a
[441673.583361] IPv6: ADDRCONF(NETDEV_CHANGE): vethe7ab64d: link becomes ready
[441673.583487] docker0: port 1(vethe7ab64d) entered blocking state
[441673.583490] docker0: port 1(vethe7ab64d) entered forwarding state
[441942.551838] veth1d04a2a: renamed from eth0
[441942.619619] docker0: port 1(vethe7ab64d) entered disabled state
[441942.621203] docker0: port 1(vethe7ab64d) entered disabled state
[441942.626280] device vethe7ab64d left promiscuous mode
[441942.626285] docker0: port 1(vethe7ab64d) entered disabled state
[443449.267615] docker0: port 1(veth15aa7c2) entered blocking state
[443449.267619] docker0: port 1(veth15aa7c2) entered disabled state
[443449.267993] device veth15aa7c2 entered promiscuous mode
[443449.566250] eth0: renamed from veth0d64843
[443449.594007] IPv6: ADDRCONF(NETDEV_CHANGE): veth15aa7c2: link becomes ready
[443449.594174] docker0: port 1(veth15aa7c2) entered blocking state
[443449.594178] docker0: port 1(veth15aa7c2) entered forwarding state
[443675.107418] docker0: port 2(vethc410a54) entered blocking state
[443675.107422] docker0: port 2(vethc410a54) entered disabled state
[443675.107757] device vethc410a54 entered promiscuous mode
[443675.413825] eth0: renamed from vethdc5e3c6
[443675.445693] IPv6: ADDRCONF(NETDEV_CHANGE): vethc410a54: link becomes ready
[443675.445814] docker0: port 2(vethc410a54) entered blocking state
[443675.445817] docker0: port 2(vethc410a54) entered forwarding state
[443677.814194] docker0: port 1(veth15aa7c2) entered disabled state
[443677.814473] veth0d64843: renamed from eth0
[443677.864344] docker0: port 1(veth15aa7c2) entered disabled state
[443677.868752] device veth15aa7c2 left promiscuous mode
[443677.868760] docker0: port 1(veth15aa7c2) entered disabled state
[443688.820829] docker0: port 1(vethf6e9766) entered blocking state
[443688.820832] docker0: port 1(vethf6e9766) entered disabled state
[443688.821142] device vethf6e9766 entered promiscuous mode
[443689.084669] eth0: renamed from veth03b6c96
[443689.104427] IPv6: ADDRCONF(NETDEV_CHANGE): vethf6e9766: link becomes ready
[443689.104570] docker0: port 1(vethf6e9766) entered blocking state
[443689.104573] docker0: port 1(vethf6e9766) entered forwarding state
[443711.794475] docker0: port 1(vethf6e9766) entered disabled state
[443711.794712] veth03b6c96: renamed from eth0
[443711.887639] docker0: port 1(vethf6e9766) entered disabled state
[443711.892828] device vethf6e9766 left promiscuous mode
[443711.892833] docker0: port 1(vethf6e9766) entered disabled state
[443756.836093] docker0: port 1(vethfa089d7) entered blocking state
[443756.836097] docker0: port 1(vethfa089d7) entered disabled state
[443756.836401] device vethfa089d7 entered promiscuous mode
[443757.110359] eth0: renamed from vethefbcd09
[443757.144431] IPv6: ADDRCONF(NETDEV_CHANGE): vethfa089d7: link becomes ready
[443757.144562] docker0: port 1(vethfa089d7) entered blocking state
[443757.144565] docker0: port 1(vethfa089d7) entered forwarding state
[443872.200671] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200680] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc301000 from client 18
[443872.200684] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[443872.200687] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.200690] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[443872.200693] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.200695] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[443872.200698] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.200700] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[443872.200715] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200719] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc302000 from client 18
[443872.200722] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.200724] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.200727] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.200729] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.200732] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.200735] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.200738] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.200745] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200748] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc303000 from client 18
[443872.200751] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.200754] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.200756] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.200759] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.200761] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.200764] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.200766] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.200773] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200776] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc304000 from client 18
[443872.200779] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.200781] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.200784] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.200786] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.200789] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.200791] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.200794] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.200966] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200970] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc301000 from client 18
[443872.200973] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[443872.200975] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.200978] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[443872.200981] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.200983] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[443872.200986] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.200989] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[443872.200995] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.200998] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc302000 from client 18
[443872.201001] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.201003] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.201006] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.201009] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.201012] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.201019] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.201027] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.201041] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.201044] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc303000 from client 18
[443872.201047] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.201050] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.201052] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.201055] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.201057] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.201060] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.201063] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.201070] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54841 thread python pid 54841)
[443872.201074] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe7bc304000 from client 18
[443872.201082] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443872.201090] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443872.201097] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443872.201099] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443872.201102] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443872.201105] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443872.201109] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443872.330890] amdgpu: Started evicting pasid 0x8002
[443872.330909] amdgpu: Finished evicting pasid 0x8002
[443877.140803] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54970 thread python pid 54970)
[443877.140810] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe6e9701000 from client 18
[443877.140813] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
[443877.140815] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443877.140817] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[443877.140819] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443877.140821] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x5
[443877.140823] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443877.140825] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x1
[443877.140838] amdgpu 0000:3d:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:40 vmid:8 pasid:32770, for process python pid 54970 thread python pid 54970)
[443877.140841] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007fe6e9702000 from client 18
[443877.140843] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[443877.140845] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[443877.140848] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[443877.140850] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[443877.140852] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[443877.140854] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[443877.140856] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[443877.236865] amdgpu: Started evicting pasid 0x8002
[443877.236874] amdgpu: Finished evicting pasid 0x8002
[443922.571546] docker0: port 1(vethfa089d7) entered disabled state
[443922.571734] vethefbcd09: renamed from eth0
[443922.653227] docker0: port 1(vethfa089d7) entered disabled state
[443922.659448] device vethfa089d7 left promiscuous mode
[443922.659455] docker0: port 1(vethfa089d7) entered disabled state
[444086.722230] gmc_v9_0_process_interrupt: 6 callbacks suppressed
[444086.722241] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722248] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5d967ce000 from client 27
[444086.722252] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[444086.722255] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[444086.722258] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[444086.722261] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722263] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[444086.722266] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722268] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722278] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722281] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5e50514000 from client 27
[444086.722284] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00801031
[444086.722287] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x8
[444086.722289] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x1
[444086.722292] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722294] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[444086.722297] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722300] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722307] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722310] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5f124fe000 from client 27
[444086.722313] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722316] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722319] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722321] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722324] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722327] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722329] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722336] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722339] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5dee8f6000 from client 27
[444086.722342] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722344] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722347] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722350] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722352] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722355] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722357] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722365] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722368] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5e8f283000 from client 27
[444086.722371] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722373] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722376] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722378] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722381] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722384] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722386] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722394] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722397] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5e507e9000 from client 27
[444086.722400] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722402] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722405] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722407] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722410] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722413] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722415] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722423] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722426] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5fd63ff000 from client 27
[444086.722429] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722432] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722435] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722438] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722440] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722443] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722445] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722454] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722457] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5fcc497000 from client 27
[444086.722460] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722462] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722465] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722467] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722470] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722472] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722475] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722483] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722486] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5f12513000 from client 27
[444086.722489] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722491] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722494] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722496] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722499] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722501] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722504] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.722512] amdgpu 0000:3d:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:24 vmid:8 pasid:32770, for process python pid 56726 thread python pid 56726)
[444086.722515] amdgpu 0000:3d:00.0: amdgpu:   in page starting at address 0x00007f5d967ce000 from client 27
[444086.722517] amdgpu 0000:3d:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
[444086.722520] amdgpu 0000:3d:00.0: amdgpu: 	 Faulty UTCL2 client ID: 0x0
[444086.722522] amdgpu 0000:3d:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[444086.722525] amdgpu 0000:3d:00.0: amdgpu: 	 WALKER_ERROR: 0x0
[444086.722527] amdgpu 0000:3d:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x0
[444086.722530] amdgpu 0000:3d:00.0: amdgpu: 	 MAPPING_ERROR: 0x0
[444086.722532] amdgpu 0000:3d:00.0: amdgpu: 	 RW: 0x0
[444086.822932] amdgpu: Started evicting pasid 0x8002
[444086.822944] amdgpu: Finished evicting pasid 0x8002
[444319.192908] docker0: port 1(veth2a34a86) entered blocking state
[444319.192912] docker0: port 1(veth2a34a86) entered disabled state
[444319.193192] device veth2a34a86 entered promiscuous mode
[444319.483698] eth0: renamed from veth5a4ed29
[444319.516985] IPv6: ADDRCONF(NETDEV_CHANGE): veth2a34a86: link becomes ready
[444319.517133] docker0: port 1(veth2a34a86) entered blocking state
[444319.517136] docker0: port 1(veth2a34a86) entered forwarding state
[444549.273190] docker0: port 1(veth2a34a86) entered disabled state
[444549.273446] veth5a4ed29: renamed from eth0
[444549.349804] docker0: port 1(veth2a34a86) entered disabled state
[444549.354914] device veth2a34a86 left promiscuous mode
[444549.354923] docker0: port 1(veth2a34a86) entered disabled state
[444559.586397] docker0: port 1(vethc00ce1f) entered blocking state
[444559.586402] docker0: port 1(vethc00ce1f) entered disabled state
[444559.586726] device vethc00ce1f entered promiscuous mode
[444559.866458] eth0: renamed from vetha96fdb4
[444559.919013] IPv6: ADDRCONF(NETDEV_CHANGE): vethc00ce1f: link becomes ready
[444559.919159] docker0: port 1(vethc00ce1f) entered blocking state
[444559.919163] docker0: port 1(vethc00ce1f) entered forwarding state
[444739.769215] vetha96fdb4: renamed from eth0
[444739.840394] docker0: port 1(vethc00ce1f) entered disabled state
[444739.842253] docker0: port 1(vethc00ce1f) entered disabled state
[444739.846608] device vethc00ce1f left promiscuous mode
[444739.846611] docker0: port 1(vethc00ce1f) entered disabled state
[444949.669362] docker0: port 1(veth7b0e681) entered blocking state
[444949.669365] docker0: port 1(veth7b0e681) entered disabled state
[444949.669631] device veth7b0e681 entered promiscuous mode
[444949.946036] eth0: renamed from veth9273b35
[444949.979414] IPv6: ADDRCONF(NETDEV_CHANGE): veth7b0e681: link becomes ready
[444949.979567] docker0: port 1(veth7b0e681) entered blocking state
[444949.979570] docker0: port 1(veth7b0e681) entered forwarding state
[445146.069911] veth9273b35: renamed from eth0
[445146.135521] docker0: port 1(veth7b0e681) entered disabled state
[445146.137189] docker0: port 1(veth7b0e681) entered disabled state
[445146.140984] device veth7b0e681 left promiscuous mode
[445146.140990] docker0: port 1(veth7b0e681) entered disabled state
[445606.292588] docker0: port 1(vethb4f6d8c) entered blocking state
[445606.292593] docker0: port 1(vethb4f6d8c) entered disabled state
[445606.292964] device vethb4f6d8c entered promiscuous mode
[445606.562604] eth0: renamed from vethebc4ad6
[445606.603944] IPv6: ADDRCONF(NETDEV_CHANGE): vethb4f6d8c: link becomes ready
[445606.604108] docker0: port 1(vethb4f6d8c) entered blocking state
[445606.604110] docker0: port 1(vethb4f6d8c) entered forwarding state
[445807.093943] docker0: port 1(vethb4f6d8c) entered disabled state
[445807.094210] vethebc4ad6: renamed from eth0
[445807.198672] docker0: port 1(vethb4f6d8c) entered disabled state
[445807.205286] device vethb4f6d8c left promiscuous mode
[445807.205294] docker0: port 1(vethb4f6d8c) entered disabled state
[445819.616379] docker0: port 1(vethd794e20) entered blocking state
[445819.616381] docker0: port 1(vethd794e20) entered disabled state
[445819.616640] device vethd794e20 entered promiscuous mode
[445819.923215] eth0: renamed from veth17bec9e
[445819.956658] IPv6: ADDRCONF(NETDEV_CHANGE): vethd794e20: link becomes ready
[445819.956831] docker0: port 1(vethd794e20) entered blocking state
[445819.956836] docker0: port 1(vethd794e20) entered forwarding state
[445820.119891] docker0: port 1(vethd794e20) entered disabled state
[445820.120026] veth17bec9e: renamed from eth0
[445820.161440] docker0: port 1(vethd794e20) entered disabled state
[445820.167679] device vethd794e20 left promiscuous mode
[445820.167688] docker0: port 1(vethd794e20) entered disabled state
[445820.627261] docker0: port 1(veth54227f3) entered blocking state
[445820.627265] docker0: port 1(veth54227f3) entered disabled state
[445820.627572] device veth54227f3 entered promiscuous mode
[445820.627760] docker0: port 1(veth54227f3) entered blocking state
[445820.627762] docker0: port 1(veth54227f3) entered forwarding state
[445820.642510] docker0: port 1(veth54227f3) entered disabled state
[445820.890798] eth0: renamed from veth7c50af6
[445820.932476] IPv6: ADDRCONF(NETDEV_CHANGE): veth54227f3: link becomes ready
[445820.932592] docker0: port 1(veth54227f3) entered blocking state
[445820.932595] docker0: port 1(veth54227f3) entered forwarding state
[445821.092743] veth7c50af6: renamed from eth0
[445821.151035] docker0: port 1(veth54227f3) entered disabled state
[445821.153677] docker0: port 1(veth54227f3) entered disabled state
[445821.157732] device veth54227f3 left promiscuous mode
[445821.157741] docker0: port 1(veth54227f3) entered disabled state
[445821.344643] docker0: port 1(veth9c5388f) entered blocking state
[445821.344647] docker0: port 1(veth9c5388f) entered disabled state
[445821.344965] device veth9c5388f entered promiscuous mode
[445821.346701] docker0: port 1(veth9c5388f) entered blocking state
[445821.346705] docker0: port 1(veth9c5388f) entered forwarding state
[445821.614946] eth0: renamed from vethd2af3ea
[445821.662682] docker0: port 1(veth9c5388f) entered disabled state
[445821.664587] IPv6: ADDRCONF(NETDEV_CHANGE): veth9c5388f: link becomes ready
[445821.664724] docker0: port 1(veth9c5388f) entered blocking state
[445821.664727] docker0: port 1(veth9c5388f) entered forwarding state
[445821.818024] docker0: port 1(veth9c5388f) entered disabled state
[445821.818153] vethd2af3ea: renamed from eth0
[445821.885803] docker0: port 1(veth9c5388f) entered disabled state
[445821.891312] device veth9c5388f left promiscuous mode
[445821.891320] docker0: port 1(veth9c5388f) entered disabled state
[445822.377841] docker0: port 1(veth8daed26) entered blocking state
[445822.377845] docker0: port 1(veth8daed26) entered disabled state
[445822.378226] device veth8daed26 entered promiscuous mode
[445822.378410] docker0: port 1(veth8daed26) entered blocking state
[445822.378412] docker0: port 1(veth8daed26) entered forwarding state
[445822.646768] eth0: renamed from veth8af1d5e
[445822.676284] IPv6: ADDRCONF(NETDEV_CHANGE): veth8daed26: link becomes ready
[445822.827829] docker0: port 1(veth8daed26) entered disabled state
[445822.828000] veth8af1d5e: renamed from eth0
[445822.894246] docker0: port 1(veth8daed26) entered disabled state
[445822.899682] device veth8daed26 left promiscuous mode
[445822.899690] docker0: port 1(veth8daed26) entered disabled state
[445823.152025] docker0: port 1(veth7bea3cb) entered blocking state
[445823.152028] docker0: port 1(veth7bea3cb) entered disabled state
[445823.152407] device veth7bea3cb entered promiscuous mode
[445823.153781] docker0: port 1(veth7bea3cb) entered blocking state
[445823.153783] docker0: port 1(veth7bea3cb) entered forwarding state
[445823.398782] eth0: renamed from veth49e9ab9
[445823.436289] IPv6: ADDRCONF(NETDEV_CHANGE): veth7bea3cb: link becomes ready
[445823.587181] docker0: port 1(veth7bea3cb) entered disabled state
[445823.587335] veth49e9ab9: renamed from eth0
[445823.665299] docker0: port 1(veth7bea3cb) entered disabled state
[445823.670467] device veth7bea3cb left promiscuous mode
[445823.670473] docker0: port 1(veth7bea3cb) entered disabled state
[445824.141726] docker0: port 1(vethf9c8ee7) entered blocking state
[445824.141730] docker0: port 1(vethf9c8ee7) entered disabled state
[445824.142092] device vethf9c8ee7 entered promiscuous mode
[445824.143630] docker0: port 1(vethf9c8ee7) entered blocking state
[445824.143634] docker0: port 1(vethf9c8ee7) entered forwarding state
[445824.406978] eth0: renamed from veth9a8d105
[445824.444401] IPv6: ADDRCONF(NETDEV_CHANGE): vethf9c8ee7: link becomes ready
[445824.589707] docker0: port 1(vethf9c8ee7) entered disabled state
[445824.589911] veth9a8d105: renamed from eth0
[445824.672823] docker0: port 1(vethf9c8ee7) entered disabled state
[445824.677006] device vethf9c8ee7 left promiscuous mode
[445824.677013] docker0: port 1(vethf9c8ee7) entered disabled state
[445824.872205] docker0: port 1(veth5b932c3) entered blocking state
[445824.872210] docker0: port 1(veth5b932c3) entered disabled state
[445824.872507] device veth5b932c3 entered promiscuous mode
[445824.873968] docker0: port 1(veth5b932c3) entered blocking state
[445824.873972] docker0: port 1(veth5b932c3) entered forwarding state
[445825.158730] eth0: renamed from veth0867d24
[445825.182699] IPv6: ADDRCONF(NETDEV_CHANGE): veth5b932c3: link becomes ready
[445825.343046] docker0: port 1(veth5b932c3) entered disabled state
[445825.343259] veth0867d24: renamed from eth0
[445825.410234] docker0: port 1(veth5b932c3) entered disabled state
[445825.414821] device veth5b932c3 left promiscuous mode
[445825.414831] docker0: port 1(veth5b932c3) entered disabled state
[445825.856128] docker0: port 1(vethff473f8) entered blocking state
[445825.856131] docker0: port 1(vethff473f8) entered disabled state
[445825.856350] device vethff473f8 entered promiscuous mode
[445825.856474] docker0: port 1(vethff473f8) entered blocking state
[445825.856476] docker0: port 1(vethff473f8) entered forwarding state
[445826.114645] eth0: renamed from vethb9d482b
[445826.136122] IPv6: ADDRCONF(NETDEV_CHANGE): vethff473f8: link becomes ready
[445826.284932] docker0: port 1(vethff473f8) entered disabled state
[445826.285109] vethb9d482b: renamed from eth0
[445826.352482] docker0: port 1(vethff473f8) entered disabled state
[445826.357780] device vethff473f8 left promiscuous mode
[445826.357802] docker0: port 1(vethff473f8) entered disabled state
[445826.577351] docker0: port 1(vethe26a357) entered blocking state
[445826.577355] docker0: port 1(vethe26a357) entered disabled state
[445826.577665] device vethe26a357 entered promiscuous mode
[445826.577920] docker0: port 1(vethe26a357) entered blocking state
[445826.577923] docker0: port 1(vethe26a357) entered forwarding state
[445826.749937] docker0: port 1(vethe26a357) entered disabled state
[445826.834646] eth0: renamed from veth28a7df8
[445826.867995] IPv6: ADDRCONF(NETDEV_CHANGE): vethe26a357: link becomes ready
[445826.868113] docker0: port 1(vethe26a357) entered blocking state
[445826.868116] docker0: port 1(vethe26a357) entered forwarding state
[445827.034342] docker0: port 1(vethe26a357) entered disabled state
[445827.034452] veth28a7df8: renamed from eth0
[445827.100332] docker0: port 1(vethe26a357) entered disabled state
[445827.107775] device vethe26a357 left promiscuous mode
[445827.107780] docker0: port 1(vethe26a357) entered disabled state
[445827.620245] docker0: port 1(veth079a89a) entered blocking state
[445827.620249] docker0: port 1(veth079a89a) entered disabled state
[445827.620588] device veth079a89a entered promiscuous mode
[445827.620797] docker0: port 1(veth079a89a) entered blocking state
[445827.620800] docker0: port 1(veth079a89a) entered forwarding state
[445827.773894] docker0: port 1(veth079a89a) entered disabled state
[445827.862531] eth0: renamed from veth257f98e
[445827.883824] IPv6: ADDRCONF(NETDEV_CHANGE): veth079a89a: link becomes ready
[445827.883952] docker0: port 1(veth079a89a) entered blocking state
[445827.883956] docker0: port 1(veth079a89a) entered forwarding state
[445884.363765] docker0: port 1(veth079a89a) entered disabled state
[445884.363996] veth257f98e: renamed from eth0
[445884.459146] docker0: port 1(veth079a89a) entered disabled state
[445884.465045] device veth079a89a left promiscuous mode
[445884.465050] docker0: port 1(veth079a89a) entered disabled state
[445887.160859] docker0: port 1(veth787e422) entered blocking state
[445887.160863] docker0: port 1(veth787e422) entered disabled state
[445887.161152] device veth787e422 entered promiscuous mode
[445887.444952] eth0: renamed from vethace2c69
[445887.485732] IPv6: ADDRCONF(NETDEV_CHANGE): veth787e422: link becomes ready
[445887.485822] docker0: port 1(veth787e422) entered blocking state
[445887.485824] docker0: port 1(veth787e422) entered forwarding state
[445887.650551] docker0: port 1(veth787e422) entered disabled state
[445887.650732] vethace2c69: renamed from eth0
[445887.722103] docker0: port 1(veth787e422) entered disabled state
[445887.728094] device veth787e422 left promiscuous mode
[445887.728101] docker0: port 1(veth787e422) entered disabled state
[445888.187296] docker0: port 1(veth02a66d0) entered blocking state
[445888.187300] docker0: port 1(veth02a66d0) entered disabled state
[445888.187581] device veth02a66d0 entered promiscuous mode
[445888.189105] docker0: port 1(veth02a66d0) entered blocking state
[445888.189110] docker0: port 1(veth02a66d0) entered forwarding state
[445888.468910] eth0: renamed from veth7cbeb55
[445888.502100] IPv6: ADDRCONF(NETDEV_CHANGE): veth02a66d0: link becomes ready
[445904.150271] docker0: port 1(veth02a66d0) entered disabled state
[445904.150512] veth7cbeb55: renamed from eth0
[445904.218734] docker0: port 1(veth02a66d0) entered disabled state
[445904.224177] device veth02a66d0 left promiscuous mode
[445904.224184] docker0: port 1(veth02a66d0) entered disabled state
[445906.132394] docker0: port 1(veth1c9efb4) entered blocking state
[445906.132397] docker0: port 1(veth1c9efb4) entered disabled state
[445906.132593] device veth1c9efb4 entered promiscuous mode
[445906.411400] eth0: renamed from vethc8ca158
[445906.452701] IPv6: ADDRCONF(NETDEV_CHANGE): veth1c9efb4: link becomes ready
[445906.452863] docker0: port 1(veth1c9efb4) entered blocking state
[445906.452866] docker0: port 1(veth1c9efb4) entered forwarding state
[447218.910237] vethc8ca158: renamed from eth0
[447218.969103] docker0: port 1(veth1c9efb4) entered disabled state
[447218.971630] docker0: port 1(veth1c9efb4) entered disabled state
[447218.976920] device veth1c9efb4 left promiscuous mode
[447218.976925] docker0: port 1(veth1c9efb4) entered disabled state
[447271.294533] docker0: port 1(vethe07461f) entered blocking state
[447271.294537] docker0: port 1(vethe07461f) entered disabled state
[447271.294929] device vethe07461f entered promiscuous mode
[447271.585015] eth0: renamed from veth6d59b47
[447271.610080] IPv6: ADDRCONF(NETDEV_CHANGE): vethe07461f: link becomes ready
[447271.610208] docker0: port 1(vethe07461f) entered blocking state
[447271.610211] docker0: port 1(vethe07461f) entered forwarding state
[447271.754255] docker0: port 1(vethe07461f) entered disabled state
[447271.754429] veth6d59b47: renamed from eth0
[447271.815156] docker0: port 1(vethe07461f) entered disabled state
[447271.820312] device vethe07461f left promiscuous mode
[447271.820320] docker0: port 1(vethe07461f) entered disabled state
[447273.023921] docker0: port 1(vethbbd1ddb) entered blocking state
[447273.023925] docker0: port 1(vethbbd1ddb) entered disabled state
[447273.024214] device vethbbd1ddb entered promiscuous mode
[447273.024449] docker0: port 1(vethbbd1ddb) entered blocking state
[447273.024452] docker0: port 1(vethbbd1ddb) entered forwarding state
[447273.288548] eth0: renamed from veth254f2fc
[447273.332400] IPv6: ADDRCONF(NETDEV_CHANGE): vethbbd1ddb: link becomes ready
[447292.816983] docker0: port 1(vethbbd1ddb) entered disabled state
[447292.817269] veth254f2fc: renamed from eth0
[447292.872373] docker0: port 1(vethbbd1ddb) entered disabled state
[447292.877868] device vethbbd1ddb left promiscuous mode
[447292.877877] docker0: port 1(vethbbd1ddb) entered disabled state
[447293.701787] docker0: port 1(veth63259b9) entered blocking state
[447293.701791] docker0: port 1(veth63259b9) entered disabled state
[447293.702098] device veth63259b9 entered promiscuous mode
[447293.702324] docker0: port 1(veth63259b9) entered blocking state
[447293.702327] docker0: port 1(veth63259b9) entered forwarding state
[447293.822425] docker0: port 1(veth63259b9) entered disabled state
[447293.950931] eth0: renamed from veth70757f3
[447293.984381] IPv6: ADDRCONF(NETDEV_CHANGE): veth63259b9: link becomes ready
[447293.984549] docker0: port 1(veth63259b9) entered blocking state
[447293.984554] docker0: port 1(veth63259b9) entered forwarding state
[447294.139802] docker0: port 1(veth63259b9) entered disabled state
[447294.139937] veth70757f3: renamed from eth0
[447294.196753] docker0: port 1(veth63259b9) entered disabled state
[447294.203076] device veth63259b9 left promiscuous mode
[447294.203085] docker0: port 1(veth63259b9) entered disabled state
[447294.415038] docker0: port 1(veth9fcccce) entered blocking state
[447294.415042] docker0: port 1(veth9fcccce) entered disabled state
[447294.415371] device veth9fcccce entered promiscuous mode
[447294.415729] docker0: port 1(veth9fcccce) entered blocking state
[447294.415732] docker0: port 1(veth9fcccce) entered forwarding state
[447294.666902] eth0: renamed from veth3b32dae
[447294.690793] IPv6: ADDRCONF(NETDEV_CHANGE): veth9fcccce: link becomes ready
[447294.842500] docker0: port 1(veth9fcccce) entered disabled state
[447294.842668] veth3b32dae: renamed from eth0
[447294.904589] docker0: port 1(veth9fcccce) entered disabled state
[447294.911298] device veth9fcccce left promiscuous mode
[447294.911307] docker0: port 1(veth9fcccce) entered disabled state
[447398.725556] docker0: port 1(vethec7e9f0) entered blocking state
[447398.725560] docker0: port 1(vethec7e9f0) entered disabled state
[447398.725890] device vethec7e9f0 entered promiscuous mode
[447399.057484] eth0: renamed from vethd17c139
[447399.089525] IPv6: ADDRCONF(NETDEV_CHANGE): vethec7e9f0: link becomes ready
[447399.089672] docker0: port 1(vethec7e9f0) entered blocking state
[447399.089675] docker0: port 1(vethec7e9f0) entered forwarding state
[449536.696128] docker0: port 3(veth491a417) entered blocking state
[449536.696131] docker0: port 3(veth491a417) entered disabled state
[449536.696440] device veth491a417 entered promiscuous mode
[449536.989646] eth0: renamed from vetha4181fd
[449537.013525] IPv6: ADDRCONF(NETDEV_CHANGE): veth491a417: link becomes ready
[449537.013675] docker0: port 3(veth491a417) entered blocking state
[449537.013679] docker0: port 3(veth491a417) entered forwarding state
[449703.979378] docker0: port 3(veth491a417) entered disabled state
[449703.979602] vetha4181fd: renamed from eth0
[449704.028286] docker0: port 3(veth491a417) entered disabled state
[449704.034501] device veth491a417 left promiscuous mode
[449704.034507] docker0: port 3(veth491a417) entered disabled state
[450148.733189] docker0: port 1(vethec7e9f0) entered disabled state
[450148.733391] vethd17c139: renamed from eth0
[450148.820417] docker0: port 1(vethec7e9f0) entered disabled state
[450148.825076] device vethec7e9f0 left promiscuous mode
[450148.825081] docker0: port 1(vethec7e9f0) entered disabled state
[450215.686962] docker0: port 1(veth42d6e67) entered blocking state
[450215.686966] docker0: port 1(veth42d6e67) entered disabled state
[450215.687271] device veth42d6e67 entered promiscuous mode
[450215.988911] eth0: renamed from veth4575d4b
[450216.016631] IPv6: ADDRCONF(NETDEV_CHANGE): veth42d6e67: link becomes ready
[450216.016769] docker0: port 1(veth42d6e67) entered blocking state
[450216.016772] docker0: port 1(veth42d6e67) entered forwarding state
[450225.781753] docker0: port 1(veth42d6e67) entered disabled state
[450225.781955] veth4575d4b: renamed from eth0
[450225.853311] docker0: port 1(veth42d6e67) entered disabled state
[450225.859640] device veth42d6e67 left promiscuous mode
[450225.859649] docker0: port 1(veth42d6e67) entered disabled state
[450247.294145] docker0: port 1(vetha96ff0d) entered blocking state
[450247.294150] docker0: port 1(vetha96ff0d) entered disabled state
[450247.294581] device vetha96ff0d entered promiscuous mode
[450247.601972] eth0: renamed from veth46f4d8b
[450247.635218] IPv6: ADDRCONF(NETDEV_CHANGE): vetha96ff0d: link becomes ready
[450247.635363] docker0: port 1(vetha96ff0d) entered blocking state
[450247.635366] docker0: port 1(vetha96ff0d) entered forwarding state
[451668.976127] veth46f4d8b: renamed from eth0
[451669.028557] docker0: port 1(vetha96ff0d) entered disabled state
[451669.032225] docker0: port 1(vetha96ff0d) entered disabled state
[451669.038335] device vetha96ff0d left promiscuous mode
[451669.038338] docker0: port 1(vetha96ff0d) entered disabled state
[451684.345643] docker0: port 1(vethbbc73dc) entered blocking state
[451684.345647] docker0: port 1(vethbbc73dc) entered disabled state
[451684.345921] device vethbbc73dc entered promiscuous mode
[451684.651289] eth0: renamed from vethfc076d1
[451684.675098] IPv6: ADDRCONF(NETDEV_CHANGE): vethbbc73dc: link becomes ready
[451684.675251] docker0: port 1(vethbbc73dc) entered blocking state
[451684.675254] docker0: port 1(vethbbc73dc) entered forwarding state
[463999.878694] vethdc5e3c6: renamed from eth0
[463999.945377] docker0: port 2(vethc410a54) entered disabled state
[463999.946963] docker0: port 2(vethc410a54) entered disabled state
[463999.951396] device vethc410a54 left promiscuous mode
[463999.951400] docker0: port 2(vethc410a54) entered disabled state
[510060.146088] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[510060.146098] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[510060.146114] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[510207.569078] amdgpu: Started evicting pasid 0x8002
[510207.569146] amdgpu: Finished evicting pasid 0x8002
[510208.952127] amdgpu: Started evicting pasid 0x8002
[510208.952211] amdgpu: Finished evicting pasid 0x8002
[510209.930126] amdgpu: Started evicting pasid 0x8002
[510209.930195] amdgpu: Finished evicting pasid 0x8002
[510210.839709] amdgpu: Started evicting pasid 0x8002
[510210.839779] amdgpu: Finished evicting pasid 0x8002
[512673.612722] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[512673.612737] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[512673.612751] amdgpu: update_invalid_user_pages: Failed to get user pages: -14
[512757.108405] amdgpu: Started evicting pasid 0x8002
[512757.108478] amdgpu: Finished evicting pasid 0x8002
[512758.542207] amdgpu: Started evicting pasid 0x8002
[512758.542277] amdgpu: Finished evicting pasid 0x8002
[512759.523636] amdgpu: Started evicting pasid 0x8002
[512759.523705] amdgpu: Finished evicting pasid 0x8002
[512761.040997] amdgpu: Started evicting pasid 0x8002
[512761.041063] amdgpu: Finished evicting pasid 0x8002
[527875.516641] amdgpu: Started evicting pasid 0x8002
[527875.516713] amdgpu: Finished evicting pasid 0x8002
[527876.937165] amdgpu: Started evicting pasid 0x8002
[527876.937238] amdgpu: Finished evicting pasid 0x8002
[527877.904923] amdgpu: Started evicting pasid 0x8002
[527877.904993] amdgpu: Finished evicting pasid 0x8002
[527878.831989] amdgpu: Started evicting pasid 0x8002
[527878.832059] amdgpu: Finished evicting pasid 0x8002
[528040.138170] amdgpu: Started evicting pasid 0x8002
[528040.138240] amdgpu: Finished evicting pasid 0x8002
[528041.554280] amdgpu: Started evicting pasid 0x8002
[528041.554350] amdgpu: Finished evicting pasid 0x8002
[528042.529731] amdgpu: Started evicting pasid 0x8002
[528042.529802] amdgpu: Finished evicting pasid 0x8002
[528043.452229] amdgpu: Started evicting pasid 0x8002
[528043.452299] amdgpu: Finished evicting pasid 0x8002


---

### 评论 #9 — dshm (2021-03-02T07:46:02Z)

the dmesg log is too long, I separate it into several comments, thanks a lot!

---

### 评论 #10 — ROCmSupport (2021-03-02T09:08:53Z)

Thanks @dshm 
Instead of pasting it here, better to attach as a text file for readability.

---

### 评论 #11 — dshm (2021-03-02T09:35:35Z)

> Thanks @dshm
> Instead of pasting it here, better to attach as a text file for readability.

I upload the log to my github, and you can get the log file in https://github.com/dshm/HIP-Examples-errors/blob/main/dmesgnewlog     Thanks a lot!

---

### 评论 #12 — scottkosty (2021-03-05T15:00:56Z)

@dshm note for the future that you can attach files to GitHub issues. When you are responding to a comment, you should see txt that says "Attach files by dragging & dropping, selecting or pasting them". Or if you prefer, just click on that text and it should open a file browser window for you to select the log.

By the way, thanks for reporting this issue. As a future ROCm user, I appreciate your time in reporting the issue.

---

### 评论 #13 — ROCmSupport (2021-03-09T10:11:07Z)

Thanks @dshm for the logs.
I tried it on my Vega10 machine and not able to reproduce this issue.
I am not able to reproduce it on Vega20 also.

_My card:_
43:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XL/XT [Radeon RX Vega 56/64] [1002:687f] (rev c1)


root@taccuser-X399-DESIGNARE-EX:/var/lib/jenkins/pytorch/HIP-Examples# ./test_all.sh

==== vectorAdd ====
rm -f ./vectoradd_hip.exe
rm -f vectoradd_hip.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
/opt/rocm/hip/bin/hipcc vectoradd_hip.o -o vectoradd_hip.exe
./vectoradd_hip.exe
 System minor 0
 System major 9
 agent prop name Device 687f
hip Device prop succeeded
PASSED!

==== gpu-burn ====
rm -rf build
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/BurnKernel.o BurnKernel.cpp
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/common.o common.cpp
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/AmdGpuMonitor.o AmdGpuMonitor.cpp
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/gpuburn.o gpuburn.cpp
/opt/rocm/hip/bin/hipcc -lm -lpthread -o build/gpuburn-hip build/BurnKernel.o build/common.o build/AmdGpuMonitor.o build/gpuburn.o
Total no. of GPUs found: 1
Init Burn Thread for device (0)
Temps: [GPU0: 34 C] 5s
Burn Thread using device (0)
Temps: [GPU0: 39 C] 4s
Temps: [GPU0: 40 C] 3s
Temps: [GPU0: 40 C] 2s
Temps: [GPU0: 41 C] 1s
Stopping burn thread on device (0)

==== strided-access ====
rm -f strided-access *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o strided-access benchmark-hip.cpp
# Using device: Device 687f
# stride     time       GB/sec
   0        0.000572        419.58
   1        0.003649        65.7714
   2        0.007097        33.8171
   3        0.005024        47.7707
   4        0.004909        48.8898
   5        0.005881        40.8094
   6        0.005121        46.8658
   7        0.00603        39.801
   8        0.006535        36.7253
   9        0.007657        31.3439
   10        0.008243        29.1156
   11        0.00874        27.46
   12        0.008843        27.1401
   13        0.009742        24.6356
   14        0.010324        23.2468
   15        0.011099        21.6236
   16        0.011513        20.846
   17        0.012132        19.7824
   18        0.012364        19.4112
   19        0.01255        19.1235
   20        0.012629        19.0039
   21        0.012954        18.5271
   22        0.012902        18.6018
   23        0.013123        18.2885
   24        0.013135        18.2718
   25        0.013172        18.2205
   26        0.013002        18.4587
   27        0.012911        18.5888
   28        0.012796        18.7559
   29        0.01265        18.9723
   30        0.012496        19.2061
   31        0.012511        19.1831
   32        0.011337        21.1696

==== rtm8 ====
Using HIP_PATH=/opt/rocm/hip
hipcc -std=c++11 -O3 -o rtm8_hip rtm8.cpp
memory (MB) = 984.096000
pts (billions) = 1.122751
Tflops = 0.075224
dt = 0.680694
pt_rate (millions/sec) = 1649.420371
flop_rate (Gflops) = 110.511165
speedup = 0.404182

==== reduction ====
rm -f reduction *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o reduction reduction.cpp
./reduction 1024*1024*4
ARRAYSIZE: 1024
Array size: 0.00390625 MB
The average performance of reduction is 0.0293178 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 8388608
ARRAYSIZE: 8388608
Array size: 32 MB
The average performance of reduction is 32.9265 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 16777216
ARRAYSIZE: 16777216
Array size: 64 MB
The average performance of reduction is 52.9247 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 33554432
ARRAYSIZE: 33554432
Array size: 128 MB
The average performance of reduction is 76.0442 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 67108864
ARRAYSIZE: 67108864
Array size: 256 MB
The average performance of reduction is 113.107 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 134217728
ARRAYSIZE: 134217728
Array size: 512 MB
The average performance of reduction is 154.815 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 268435456
ARRAYSIZE: 268435456
Array size: 1024 MB
The average performance of reduction is 224.649 GBytes/sec
VERIFICATION: result is CORRECT

./reduction 536870912
ARRAYSIZE: 536870912
Array size: 2048 MB
The average performance of reduction is 282.746 GBytes/sec
VERIFICATION: result is CORRECT


==== mini-nbody ====
hipcc -I../ -DSHMOO nbody-orig.cpp -o nbody-orig
./nbody-orig 1024
1024, 1.706
./nbody-orig 2048
2048, 3.383
./nbody-orig 4096
4096, 7.786
./nbody-orig 8192
8192, 17.390
./nbody-orig 16384
16384, 39.165
./nbody-orig 32768
32768, 73.177
./nbody-orig 65536
65536, 93.762
./nbody-orig 131072
131072, 97.108
./nbody-orig 262144
262144, 99.304
./nbody-orig 524288
524288, 100.546
hipcc -I../ -DSHMOO nbody-soa.cpp -o nbody-soa
./nbody-soa 1024
1024, 1.740
./nbody-soa 2048
2048, 3.863
./nbody-soa 4096
4096, 8.072
./nbody-soa 8192
8192, 18.658
./nbody-soa 16384
16384, 40.629
./nbody-soa 32768
32768, 73.747
./nbody-soa 65536
65536, 94.576
./nbody-soa 131072
131072, 97.391
hipcc -I../ -DSHMOO nbody-block.cpp -o nbody-block
./nbody-block 1024
1024, 2.025
./nbody-block 2048
2048, 4.665
./nbody-block 4096
4096, 9.586
./nbody-block 8192
8192, 20.975
./nbody-block 16384
16384, 46.853
./nbody-block 32768
32768, 77.429
./nbody-block 65536
65536, 96.900
./nbody-block 131072
131072, 97.142

==== add4 ====
rm -f   gpu-stream-hip *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -c hip-stream.cpp -o hip-stream.o
g++ -std=c++11 -O3   -c -o common.o common.cpp
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 common.o hip-stream.o -lm -o gpu-stream-hip
./gpu-stream-hip
GPU-STREAM
Version: 1.0
Implementation: HIP
GridSize: 26214400 work-items
GroupSize: 1024 work-items
Operations/Work-item: 1
Precision: double

Running kernels 10 times
Array size: 200.0 MB (=0.2 GB) 0 bytes padding
Total size: 1000.0 MB (=1.0 GB)
Using HIP device Device 687f (compute_units=64)
Driver: 321200
d_a=0x7fb944e00000
d_b=0x7fb938400000
d_c=0x7fb92ba00000
d_d=0x7fb91f000000
d_e=0x7fb912600000
Function    MBytes/sec  Min (sec)   Max         Average
Copy        384548.399  0.00109     0.00197     0.00135
Mul         377532.588  0.00111     0.00197     0.00133
Add4        341155.315  0.00307     0.00388     0.00334
Triad       349327.187  0.00180     0.00227     0.00202
GEOMEAN     362679.072
./gpu-stream-hip --groups 256 --groupSize 256
GPU-STREAM
Version: 1.0
Implementation: HIP
GridSize: 65536 work-items
GroupSize: 256 work-items
Operations/Work-item: 400
Using looper kernels:
Precision: double

Running kernels 10 times
Array size: 200.0 MB (=0.2 GB) 0 bytes padding
Total size: 1000.0 MB (=1.0 GB)
Using HIP device Device 687f (compute_units=64)
Driver: 321200
d_a=0x7f3b14e00000
d_b=0x7f3b08400000
d_c=0x7f3afba00000
d_d=0x7f3aef000000
d_e=0x7f3ae2600000
Function    MBytes/sec  Min (sec)   Max         Average
Copy        363562.481  0.00115     0.00198     0.00135
Mul         365754.150  0.00115     0.00202     0.00134
Add4        336539.076  0.00312     0.00394     0.00341
Triad       340161.077  0.00185     0.00213     0.00200
GEOMEAN     351254.672
./gpu-stream-hip --float
GPU-STREAM
Version: 1.0
Implementation: HIP
Warning: If number of iterations set >= 8, expect rounding errors with single precision
GridSize: 26214400 work-items
GroupSize: 1024 work-items
Operations/Work-item: 1
Precision: float

Running kernels 10 times
Array size: 100.0 MB (=0.1 GB) 0 bytes padding
Total size: 500.0 MB (=0.5 GB)
Using HIP device Device 687f (compute_units=64)
Driver: 321200
d_a=0x7ff416600000
d_b=0x7ff410000000
d_c=0x7ff409a00000
d_d=0x7ff403400000
d_e=0x7ff3fce00000
Function    MBytes/sec  Min (sec)   Max         Average
Copy        299079.154  0.00070     0.00112     0.00083
Mul         308430.560  0.00068     0.00116     0.00080
Add4        299994.450  0.00175     0.00261     0.00197
Triad       288726.840  0.00109     0.00165     0.00122
GEOMEAN     298975.761
./gpu-stream-hip --float --groups 256 --groupSize 256
GPU-STREAM
Version: 1.0
Implementation: HIP
Warning: If number of iterations set >= 8, expect rounding errors with single precision
GridSize: 65536 work-items
GroupSize: 256 work-items
Operations/Work-item: 400
Using looper kernels:
Precision: float

Running kernels 10 times
Array size: 100.0 MB (=0.1 GB) 0 bytes padding
Total size: 500.0 MB (=0.5 GB)
Using HIP device Device 687f (compute_units=64)
Driver: 321200
d_a=0x7f889a600000
d_b=0x7f8894000000
d_c=0x7f888da00000
d_d=0x7f8887400000
d_e=0x7f8880e00000
Function    MBytes/sec  Min (sec)   Max         Average
Copy        299485.328  0.00070     0.00106     0.00078
Mul         315111.957  0.00067     0.00107     0.00077
Add4        296871.426  0.00177     0.00263     0.00199
Triad       284166.681  0.00111     0.00164     0.00123
GEOMEAN     298707.066

==== cuda-stream ====
rm -f stream *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o stream stream.cpp
 STREAM Benchmark implementation in HIP
 Array size (double precision) = 536.87 MB
 using 192 threads per block, 349526 blocks
 output in IEC units (KiB = 1024 B)

Function      Rate (GiB/s)  Avg time(s)  Min time(s)  Max time(s)
-----------------------------------------------------------------
Copy:         354.8481      0.00290536   0.00281811   0.00336909
Scale:        351.3700      0.00292871   0.00284600   0.00332189
Add:          326.6592      0.00468678   0.00459194   0.00524712
Triad:        327.4412      0.00465951   0.00458097   0.00521207


---

### 评论 #14 — scottkosty (2021-03-09T15:42:22Z)

@ROCmSupport @dshm it will be easier to follow GitHub issues if you either attach files, or do something like the following:

    <details>
    long text
    </details>

The above produces the following:

<details>
long text
</details>

I promise I will not make any other pedantic formatting comment now :)

---

### 评论 #15 — dshm (2021-03-10T09:33:56Z)

> @ROCmSupport @dshm it will be easier to follow GitHub issues if you either attach files, or do something like the following:
> 
> ```
> <details>
> long text
> </details>
> ```
> 
> The above produces the following:
> 
> I promise I will not make any other pedantic formatting comment now :)

Got it, Thanks a lot!

---

### 评论 #16 — dshm (2021-03-11T02:12:37Z)

> Thanks @dshm for the logs.
> I tried it on my Vega10 machine and not able to reproduce this issue.
> I am not able to reproduce it on Vega20 also.
> 
> _My card:_
> 43:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XL/XT [Radeon RX Vega 56/64] [1002:687f] (rev c1)
> 
> root@taccuser-X399-DESIGNARE-EX:/var/lib/jenkins/pytorch/HIP-Examples# ./test_all.sh
> 
> ==== vectorAdd ====
> rm -f ./vectoradd_hip.exe
> rm -f vectoradd_hip.o
> rm -f /opt/rocm/hip/src/*.o
> /opt/rocm/hip/bin/hipcc -g -c -o vectoradd_hip.o vectoradd_hip.cpp
> /opt/rocm/hip/bin/hipcc vectoradd_hip.o -o vectoradd_hip.exe
> ./vectoradd_hip.exe
> System minor 0
> System major 9
> agent prop name Device 687f
> hip Device prop succeeded
> PASSED!
> 
> ==== gpu-burn ====
> rm -rf build
> mkdir -p build
> /opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/BurnKernel.o BurnKernel.cpp
> mkdir -p build
> /opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/common.o common.cpp
> mkdir -p build
> /opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/AmdGpuMonitor.o AmdGpuMonitor.cpp
> mkdir -p build
> /opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include -O3 -c -o build/gpuburn.o gpuburn.cpp
> /opt/rocm/hip/bin/hipcc -lm -lpthread -o build/gpuburn-hip build/BurnKernel.o build/common.o build/AmdGpuMonitor.o build/gpuburn.o
> Total no. of GPUs found: 1
> Init Burn Thread for device (0)
> Temps: [GPU0: 34 C] 5s
> Burn Thread using device (0)
> Temps: [GPU0: 39 C] 4s
> Temps: [GPU0: 40 C] 3s
> Temps: [GPU0: 40 C] 2s
> Temps: [GPU0: 41 C] 1s
> Stopping burn thread on device (0)
> 
> ==== strided-access ====
> rm -f strided-access *.o
> /opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o strided-access benchmark-hip.cpp
> 
> # Using device: Device 687f
> # stride time GB/sec
> 0 0.000572 419.58
> 1 0.003649 65.7714
> 2 0.007097 33.8171
> 3 0.005024 47.7707
> 4 0.004909 48.8898
> 5 0.005881 40.8094
> 6 0.005121 46.8658
> 7 0.00603 39.801
> 8 0.006535 36.7253
> 9 0.007657 31.3439
> 10 0.008243 29.1156
> 11 0.00874 27.46
> 12 0.008843 27.1401
> 13 0.009742 24.6356
> 14 0.010324 23.2468
> 15 0.011099 21.6236
> 16 0.011513 20.846
> 17 0.012132 19.7824
> 18 0.012364 19.4112
> 19 0.01255 19.1235
> 20 0.012629 19.0039
> 21 0.012954 18.5271
> 22 0.012902 18.6018
> 23 0.013123 18.2885
> 24 0.013135 18.2718
> 25 0.013172 18.2205
> 26 0.013002 18.4587
> 27 0.012911 18.5888
> 28 0.012796 18.7559
> 29 0.01265 18.9723
> 30 0.012496 19.2061
> 31 0.012511 19.1831
> 32 0.011337 21.1696
> 
> ==== rtm8 ====
> Using HIP_PATH=/opt/rocm/hip
> hipcc -std=c++11 -O3 -o rtm8_hip rtm8.cpp
> memory (MB) = 984.096000
> pts (billions) = 1.122751
> Tflops = 0.075224
> dt = 0.680694
> pt_rate (millions/sec) = 1649.420371
> flop_rate (Gflops) = 110.511165
> speedup = 0.404182
> 
> ==== reduction ====
> rm -f reduction _.o /opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o reduction reduction.cpp ./reduction 1024_1024*4
> ARRAYSIZE: 1024
> Array size: 0.00390625 MB
> The average performance of reduction is 0.0293178 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 8388608
> ARRAYSIZE: 8388608
> Array size: 32 MB
> The average performance of reduction is 32.9265 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 16777216
> ARRAYSIZE: 16777216
> Array size: 64 MB
> The average performance of reduction is 52.9247 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 33554432
> ARRAYSIZE: 33554432
> Array size: 128 MB
> The average performance of reduction is 76.0442 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 67108864
> ARRAYSIZE: 67108864
> Array size: 256 MB
> The average performance of reduction is 113.107 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 134217728
> ARRAYSIZE: 134217728
> Array size: 512 MB
> The average performance of reduction is 154.815 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 268435456
> ARRAYSIZE: 268435456
> Array size: 1024 MB
> The average performance of reduction is 224.649 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ./reduction 536870912
> ARRAYSIZE: 536870912
> Array size: 2048 MB
> The average performance of reduction is 282.746 GBytes/sec
> VERIFICATION: result is CORRECT
> 
> ==== mini-nbody ====
> hipcc -I../ -DSHMOO nbody-orig.cpp -o nbody-orig
> ./nbody-orig 1024
> 1024, 1.706
> ./nbody-orig 2048
> 2048, 3.383
> ./nbody-orig 4096
> 4096, 7.786
> ./nbody-orig 8192
> 8192, 17.390
> ./nbody-orig 16384
> 16384, 39.165
> ./nbody-orig 32768
> 32768, 73.177
> ./nbody-orig 65536
> 65536, 93.762
> ./nbody-orig 131072
> 131072, 97.108
> ./nbody-orig 262144
> 262144, 99.304
> ./nbody-orig 524288
> 524288, 100.546
> hipcc -I../ -DSHMOO nbody-soa.cpp -o nbody-soa
> ./nbody-soa 1024
> 1024, 1.740
> ./nbody-soa 2048
> 2048, 3.863
> ./nbody-soa 4096
> 4096, 8.072
> ./nbody-soa 8192
> 8192, 18.658
> ./nbody-soa 16384
> 16384, 40.629
> ./nbody-soa 32768
> 32768, 73.747
> ./nbody-soa 65536
> 65536, 94.576
> ./nbody-soa 131072
> 131072, 97.391
> hipcc -I../ -DSHMOO nbody-block.cpp -o nbody-block
> ./nbody-block 1024
> 1024, 2.025
> ./nbody-block 2048
> 2048, 4.665
> ./nbody-block 4096
> 4096, 9.586
> ./nbody-block 8192
> 8192, 20.975
> ./nbody-block 16384
> 16384, 46.853
> ./nbody-block 32768
> 32768, 77.429
> ./nbody-block 65536
> 65536, 96.900
> ./nbody-block 131072
> 131072, 97.142
> 
> ==== add4 ====
> rm -f gpu-stream-hip *.o
> /opt/rocm/hip/bin/hipcc -std=c++11 -O3 -c hip-stream.cpp -o hip-stream.o
> g++ -std=c++11 -O3 -c -o common.o common.cpp
> /opt/rocm/hip/bin/hipcc -std=c++11 -O3 common.o hip-stream.o -lm -o gpu-stream-hip
> ./gpu-stream-hip
> GPU-STREAM
> Version: 1.0
> Implementation: HIP
> GridSize: 26214400 work-items
> GroupSize: 1024 work-items
> Operations/Work-item: 1
> Precision: double
> 
> Running kernels 10 times
> Array size: 200.0 MB (=0.2 GB) 0 bytes padding
> Total size: 1000.0 MB (=1.0 GB)
> Using HIP device Device 687f (compute_units=64)
> Driver: 321200
> d_a=0x7fb944e00000
> d_b=0x7fb938400000
> d_c=0x7fb92ba00000
> d_d=0x7fb91f000000
> d_e=0x7fb912600000
> Function MBytes/sec Min (sec) Max Average
> Copy 384548.399 0.00109 0.00197 0.00135
> Mul 377532.588 0.00111 0.00197 0.00133
> Add4 341155.315 0.00307 0.00388 0.00334
> Triad 349327.187 0.00180 0.00227 0.00202
> GEOMEAN 362679.072
> ./gpu-stream-hip --groups 256 --groupSize 256
> GPU-STREAM
> Version: 1.0
> Implementation: HIP
> GridSize: 65536 work-items
> GroupSize: 256 work-items
> Operations/Work-item: 400
> Using looper kernels:
> Precision: double
> 
> Running kernels 10 times
> Array size: 200.0 MB (=0.2 GB) 0 bytes padding
> Total size: 1000.0 MB (=1.0 GB)
> Using HIP device Device 687f (compute_units=64)
> Driver: 321200
> d_a=0x7f3b14e00000
> d_b=0x7f3b08400000
> d_c=0x7f3afba00000
> d_d=0x7f3aef000000
> d_e=0x7f3ae2600000
> Function MBytes/sec Min (sec) Max Average
> Copy 363562.481 0.00115 0.00198 0.00135
> Mul 365754.150 0.00115 0.00202 0.00134
> Add4 336539.076 0.00312 0.00394 0.00341
> Triad 340161.077 0.00185 0.00213 0.00200
> GEOMEAN 351254.672
> ./gpu-stream-hip --float
> GPU-STREAM
> Version: 1.0
> Implementation: HIP
> Warning: If number of iterations set >= 8, expect rounding errors with single precision
> GridSize: 26214400 work-items
> GroupSize: 1024 work-items
> Operations/Work-item: 1
> Precision: float
> 
> Running kernels 10 times
> Array size: 100.0 MB (=0.1 GB) 0 bytes padding
> Total size: 500.0 MB (=0.5 GB)
> Using HIP device Device 687f (compute_units=64)
> Driver: 321200
> d_a=0x7ff416600000
> d_b=0x7ff410000000
> d_c=0x7ff409a00000
> d_d=0x7ff403400000
> d_e=0x7ff3fce00000
> Function MBytes/sec Min (sec) Max Average
> Copy 299079.154 0.00070 0.00112 0.00083
> Mul 308430.560 0.00068 0.00116 0.00080
> Add4 299994.450 0.00175 0.00261 0.00197
> Triad 288726.840 0.00109 0.00165 0.00122
> GEOMEAN 298975.761
> ./gpu-stream-hip --float --groups 256 --groupSize 256
> GPU-STREAM
> Version: 1.0
> Implementation: HIP
> Warning: If number of iterations set >= 8, expect rounding errors with single precision
> GridSize: 65536 work-items
> GroupSize: 256 work-items
> Operations/Work-item: 400
> Using looper kernels:
> Precision: float
> 
> Running kernels 10 times
> Array size: 100.0 MB (=0.1 GB) 0 bytes padding
> Total size: 500.0 MB (=0.5 GB)
> Using HIP device Device 687f (compute_units=64)
> Driver: 321200
> d_a=0x7f889a600000
> d_b=0x7f8894000000
> d_c=0x7f888da00000
> d_d=0x7f8887400000
> d_e=0x7f8880e00000
> Function MBytes/sec Min (sec) Max Average
> Copy 299485.328 0.00070 0.00106 0.00078
> Mul 315111.957 0.00067 0.00107 0.00077
> Add4 296871.426 0.00177 0.00263 0.00199
> Triad 284166.681 0.00111 0.00164 0.00123
> GEOMEAN 298707.066
> 
> ==== cuda-stream ====
> rm -f stream *.o
> /opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o stream stream.cpp
> STREAM Benchmark implementation in HIP
> Array size (double precision) = 536.87 MB
> using 192 threads per block, 349526 blocks
> output in IEC units (KiB = 1024 B)
> 
> ## Function Rate (GiB/s) Avg time(s) Min time(s) Max time(s)
> Copy: 354.8481 0.00290536 0.00281811 0.00336909
> Scale: 351.3700 0.00292871 0.00284600 0.00332189
> Add: 326.6592 0.00468678 0.00459194 0.00524712
> Triad: 327.4412 0.00465951 0.00458097 0.00521207

@ROCmSupport Thank you a lot for reply! What are the steps of operation you tried? Could you please give the commands and environment you use in detail? Could it be possible that the problem is graph card related? Though it is vega10, we don’t have Radeon RX Vega 56/64. Did you test the code on Radeon PRO WX 8100?


---

### 评论 #17 — ROCmSupport (2021-03-12T05:39:49Z)

Hi @dshm 
I don't have Radeon Pro WX8100 with us. It is most likely due to problem with the card, i.e, ROCm on specific card(your card).
Recommend you to try with any other ROCm supported card and let me know.




---

### 评论 #18 — dshm (2021-03-12T08:34:47Z)

> Hi @dshm
> I don't have Radeon Pro WX8100 with us. It is most likely due to problem with the card, i.e, ROCm on specific card(your card).
> Recommend you to try with any other ROCm supported card and let me know.

@ROCmSupport 
1. Could you please give the steps of command you use to test in your machine in detail? 
2. And could you please give the test environment in your machine in detail?  
3. I have tried another machine with 6900xt card but fails for other errors. The link to the new issue is https://github.com/RadeonOpenCompute/ROCm/issues/1404
Could you please give me some adivice? Thank you a lot for your time!


---

### 评论 #19 — ROCmSupport (2021-03-12T11:26:20Z)

I followed the below steps(given by you) on My Vega10-64 card.
Base OS is Ubuntu 18.04 with 5.4 kernel + ROCm 4.0 installed in it.

Launched docker: rocm/pytorch:rocm4.0_ubuntu18.04_py3.6_pytorch_1.7.0.
I run the test using the following command
git clone https://github.com/ROCm-Developer-Tools/HIP-Examples.git
cd HIP-Examples
git submodule init
git submodule update
./test_all.sh 2>&1 | tee testlog

---

### 评论 #20 — ROCmSupport (2021-05-07T13:07:27Z)

Hi @dshm 
Can you please share an update. Else request to close this issue as its open for more than 14 days.
Thanks for understanding.

---

### 评论 #21 — ROCmSupport (2021-05-11T04:51:52Z)

Thanks @dshm for the closure of this issue Hope this issue is fixed.
Feel free to open a new issue for quick & fast resolution.
Thank you.

---
