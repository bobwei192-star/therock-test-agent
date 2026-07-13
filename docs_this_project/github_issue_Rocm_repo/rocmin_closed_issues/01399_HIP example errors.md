# HIP example errors

- **Issue #:** 1399
- **State:** closed
- **Created:** 2021-03-02T06:45:37Z
- **Updated:** 2021-05-11T04:51:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1399

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