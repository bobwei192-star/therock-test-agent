# clinfo  gives terminate called after throwing an instance of 'cl::Error'

> **Issue #511**
> **状态**: closed
> **创建时间**: 2018-08-23T22:31:05Z
> **更新时间**: 2018-08-25T06:33:02Z
> **关闭时间**: 2018-08-24T00:17:32Z
> **作者**: CatspersCoffee
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/511

## 描述

Hi All, 
im having some issues getting Vega 56/64 GPUs to show up in platforms

Ubuntu 16.04 with kerenl 4.13
mainboard/ CPU are all PCIE 3.0 compatible.


**i can sun "/opt/rocm/bin/rocminfo " successfully and lists all the GPUs. however when running "/opt/rocm/opencl/bin/x86_64/clinfo" i get:**

:~$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)


**running "/opt/rocm/bin/rocm-smi -hw" gives:**

 GPU  DID    ECC        VBIOS
  5   687f   N/A   113-D0500100-103
  3   687f   N/A   113-D0500300-102
  1   687f   N/A   113-D0500100-104
  6   687f   N/A   113-D0500100-102
  4   687f   N/A   113-D0500350-102
  2   687f   N/A   113-D0500100-104
  0   1902   N/A   None





**i can verify the installation of ROCm:**

:~$ apt show rocm-libs -a
Package: rocm-libs
Version: 1.8.192
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 13.3 kB
Depends: rocfft, rocrand, hipblas, rocblas
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 772 B
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack



:~$ dmesg | grep kfd
[    1.618386] kfd kfd: Initialized module
[    3.753602] kfd kfd: Allocated 3969056 bytes on gart
[    3.753739] kfd kfd: added device 1002:687f
[    5.742944] kfd kfd: Allocated 3969056 bytes on gart
[    5.743203] kfd kfd: added device 1002:687f
[    7.775265] kfd kfd: Allocated 3969056 bytes on gart
[    7.775648] kfd kfd: added device 1002:687f
[    9.754696] kfd kfd: Allocated 3969056 bytes on gart
[    9.755192] kfd kfd: added device 1002:687f
[   11.800216] kfd kfd: Allocated 3969056 bytes on gart
[   11.800847] kfd kfd: added device 1002:687f
[   13.807090] kfd kfd: Allocated 3969056 bytes on gart
[   13.807851] kfd kfd: added device 1002:687f


any help would be much appreciated

---

## 评论 (28 条)

### 评论 #1 — jlgreathouse (2018-08-23T22:32:48Z)

Just to test the simple stuff first: is your user in the 'video' group?

---

### 评论 #2 — CatspersCoffee (2018-08-23T22:36:35Z)

Yes. my user is in video group.

---

### 评论 #3 — CatspersCoffee (2018-08-23T22:47:07Z)

if i run as sudo i get:

:~$ sudo clinfo
Number of platforms                               0


---

### 评论 #4 — jlgreathouse (2018-08-23T22:55:52Z)

OK, let's run some tests then to see where things are breaking. :)

Could I get you to run the following sets of commands and show me their output?
```shell
cp -R /opt/rocm/hip/samples/1_Utils/hipInfo/ ~
cd ~/hipInfo
make hipInfo
./hipInfo
```

```shell
cp -R /opt/rocm/hip/samples/0_Intro/square/ ~
cd ~/square/
make
./square.out
```

```shell
cd ~
git clone https://github.com/ROCm-Developer-Tools/clARMOR.git -b develop
cd ~/clARMOR
export OCL_INCLUDE_DIR=/opt/rocm/opencl/include/
export OCL_LIB_DIR=/opt/rocm/opencl/lib/x86_64/
make info_check
./bin/clarmor-info -g -b
```
This one relies on having done the one above:
```shell
cd ~/clARMOR/tests/good_cl_mem
make build_test
./good_cl_mem.exe
```

---

### 评论 #5 — CatspersCoffee (2018-08-23T23:05:54Z)

**First:**

```
:~/hipInfo$ ./hipInfo

compiler: hcc version=1.2.18272-47899bc-86791fc-c1f9263, workweek (YYWWD) = 18272
--------------------------------------------------------------------------------
device#                           0
Name:                             Device 687f
pciBusID:                         5
pciDeviceID:                      0
multiProcessorCount:              64
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1630 Mhz
memoryClockRate:                  945 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:                            device#1 device#2 device#3 device#4 device#5
non-peers:                        device#0

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
--------------------------------------------------------------------------------
device#                           1
Name:                             Device 687f
pciBusID:                         14
pciDeviceID:                      0
multiProcessorCount:              64
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1630 Mhz
memoryClockRate:                  945 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:                            device#0 device#2 device#3 device#4 device#5
non-peers:                        device#1

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
--------------------------------------------------------------------------------
device#                           2
Name:                             Device 687f
pciBusID:                         17
pciDeviceID:                      0
multiProcessorCount:              56
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1590 Mhz
memoryClockRate:                  800 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:                            device#0 device#1 device#3 device#4 device#5
non-peers:                        device#2

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
--------------------------------------------------------------------------------
device#                           3
Name:                             Device 687f
pciBusID:                         20
pciDeviceID:                      0
multiProcessorCount:              56
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1590 Mhz
memoryClockRate:                  800 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:                            device#0 device#1 device#2 device#4 device#5
non-peers:                        device#3

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
--------------------------------------------------------------------------------
device#                           4
Name:                             Device 687f
pciBusID:                         23
pciDeviceID:                      0
multiProcessorCount:              64
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1630 Mhz
memoryClockRate:                  945 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:                            device#0 device#1 device#2 device#3 device#5
non-peers:                        device#4

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
--------------------------------------------------------------------------------
device#                           5
Name:                             Device 687f
pciBusID:                         26
pciDeviceID:                      0
multiProcessorCount:              64
maxThreadsPerMultiProcessor:      2560
isMultiGpuBoard:                  1
clockRate:                        1630 Mhz
memoryClockRate:                  945 Mhz
memoryBusWidth:                   2048
clockInstructionRate:             1000 Mhz
totalGlobalMem:                   7.98 GB
maxSharedMemoryPerMultiProcessor: 7.98 GB
totalConstMem:                    16384
sharedMemPerBlock:                64.00 KB
regsPerBlock:                     0
warpSize:                         64
l2CacheSize:                      0
computeMode:                      0
maxThreadsPerBlock:               1024
maxThreadsDim.x:                  1024
maxThreadsDim.y:                  1024
maxThreadsDim.z:                  1024
maxGridSize.x:                    2147483647
maxGridSize.y:                    2147483647
maxGridSize.z:                    2147483647
major:                            3
minor:                            0
concurrentKernels:                1
arch.hasGlobalInt32Atomics:       1
arch.hasGlobalFloatAtomicExch:    1
arch.hasSharedInt32Atomics:       1
arch.hasSharedFloatAtomicExch:    1
arch.hasFloatAtomicAdd:           1
arch.hasGlobalInt64Atomics:       1
arch.hasSharedInt64Atomics:       1
arch.hasDoubles:                  1
arch.hasWarpVote:                 1
arch.hasWarpBallot:               1
arch.hasWarpShuffle:              1
arch.hasFunnelShift:              0
arch.hasThreadFenceSystem:        1
arch.hasSyncThreadsExt:           0
arch.hasSurfaceFuncs:             0
arch.has3dGrid:                   1
arch.hasDynamicParallelism:       0
gcnArch:                          900
peers:
non-peers:                        device#0 device#1 device#2 device#3 device#4 device#5

memInfo.total:                    7.98 GB
memInfo.free:                     7.73 GB (97%)
```

**Second:**
```
:~/square$ ./square.out
info: running on device Device 687f
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
info: check result
PASSED!
```
**3rd (all output):**

```
:~$ cd ~/clARMOR
catsper@vegarig:~/clARMOR$ export OCL_INCLUDE_DIR=/opt/rocm/opencl/include/
catsper@vegarig:~/clARMOR$ export OCL_LIB_DIR=/opt/rocm/opencl/lib/x86_64/
catsper@vegarig:~/clARMOR$ make info_check
make --directory=make/../src/info_check
make[1]: Entering directory '/home/catsper/clARMOR/src/info_check'
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"get_cl_info.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem /op                                                                  t/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -fPIC -c -MMD -o                                                                   ../../make/../src/info_check/get_cl_info.o ../../make/../src/info_check/get_cl_info.c
gcc -o ../../make/../bin/clarmor-info ../../make/../src/info_check/get_cl_info.o -Wl,--as-needed -lstdc++ -L/opt/rocm/opencl/lib/x86_64/ -lOpenCL -L/opt/rocm/opencl/lib/x86_                                                                  64/ -lOpenCL
make[1]: Leaving directory '/home/catsper/clARMOR/src/info_check'
catsper@vegarig:~/clARMOR$ ./bin/clarmor-info -g -b
catsper@vegarig:~/clARMOR$ cd ~/clARMOR/tests/good_cl_mem
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ make build_test
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"cl_utils.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem /opt/r                                                                  ocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/catsper/clA                                                                  RMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -MMD -o ..                                                                  /../make/../src/utils/cl_utils.o ../../make/../src/utils/cl_utils.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"universal_event.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem                                                                   /opt/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/cats                                                                  per/clARMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -MM                                                                  D -o ../../make/../src/utils/universal_event.o ../../make/../src/utils/universal_event.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"util_functions.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem                                                                   /opt/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/catsp                                                                  er/clARMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -MMD                                                                   -o ../../make/../src/utils/util_functions.o ../../make/../src/utils/util_functions.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"cl_err.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem /opt/roc                                                                  m/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/catsper/clARM                                                                  OR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -MMD -o ../.                                                                  ./make/../src/utils/cl_err.o ../../make/../src/utils/cl_err.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"check_app_sdk.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isystem /                                                                  opt/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/catspe                                                                  r/clARMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -MMD                                                                   -o ../../make/../src/utils/check_app_sdk.o ../../make/../src/utils/check_app_sdk.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"test_good_cl_mem.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -isyste                                                                  m /opt/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/home/cat                                                                  sper/clARMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC -c -M                                                                  MD -o test_good_cl_mem.o test_good_cl_mem.c
gcc -g3 -ggdb -pthread -fPIC -DBASE_FILE_NAME=\"common_test_functions.c\" -DCLARMOR_VERSION=\"18.08-2-gfc2f480\" -DLINUX -Werror -Wall -Wextra -Wpedantic -pedantic-errors -i                                                                  system /opt/rocm/opencl/include/ -Wpacked -Wundef -I/opt/rocm/opencl/include/ -I../../make/../src/include -O3 -march=native -DNDEBUG -std=gnu11 -Wold-style-definition -I/hom                                                                  e/catsper/clARMOR/tests/good_cl_mem/../common_include/ -DOUTPUT_FILE_NAME='"/home/catsper/clARMOR/tests/good_cl_mem/buffer_overflow_detector.out"' -DEXPECTED_ERRORS=0 -fPIC                                                                   -c -MMD -o /home/catsper/clARMOR/tests/good_cl_mem/../common_include/common_test_functions.o /home/catsper/clARMOR/tests/good_cl_mem/../common_include/common_test_functions.                                                                  c
gcc ../../make/../src/utils/cl_utils.o ../../make/../src/utils/universal_event.o ../../make/../src/utils/util_functions.o ../../make/../src/utils/cl_err.o ../../make/../src/                                                                  utils/check_app_sdk.o test_good_cl_mem.o /home/catsper/clARMOR/tests/good_cl_mem/../common_include/common_test_functions.o -Wl,--as-needed -lstdc++ -L/opt/rocm/opencl/lib/x8                                                                  6_64/ -lOpenCL -lm -ldl -o good_cl_mem.exe
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ ./good_cl_mem.exe
Searching for platforms...
OpenCL error, exiting application.
/home/catsper/clARMOR/tests/good_cl_mem/../common_include/common_test_functions.c:179: error: UNKNOWN CL ERROR CODE (-1001)
catsper@vegarig:~/clARMOR/tests/good_cl_mem$
```

---

### 评论 #6 — jlgreathouse (2018-08-23T23:22:19Z)

I edited your message to enclose the outputs in code blocks. This should help formatting. :)

OK, looks like ROCm and HSA stuff works, but OpenCL is broken. It's not `clinfo`, per say; it looks like the OpenCL runtime isn't properly finding any platforms. That's especially odd, because that's even before seeing any GPU devices. The fact that you get a different answer when running with sudo is weird, too.

I seem to remember that "-1001" is a non-standard OpenCL error code frequently returned by the Nvidia OpenCL runtime as a generic "failed but we don't specify why" marker. Did your system previously have Nvidia GPUs in it, and/or do you have the CUDA SDK installed?

Could you run the following commands and show me the output?

- `ldd ~/clARMOR/tests/good_cl_mem/good_cl_mem.exe`
- `ls -alh /etc/OpenCL/vendors`
- ```for i in `ls -1 /etc/OpenCL/vendors`; do echo -n "$i : "; cat /etc/OpenCL/vendors/$i; done```
- `echo $OPENCL_VENDOR_PATH`

---

### 评论 #7 — CatspersCoffee (2018-08-23T23:32:25Z)

thankyou, apologies.. im formatting Git noob :-)

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ ldd ~/clARMOR/tests/good_cl_mem/good_cl_mem.exe
        linux-vdso.so.1 =>  (0x00007ffeb3dbe000)
        libOpenCL.so.1 => /usr/lib/x86_64-linux-gnu/libOpenCL.so.1 (0x00007fae5e758000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fae5e38e000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fae5e18a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fae5e963000)
```

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ ls -alh /etc/OpenCL/vendors
ls: cannot access '/etc/OpenCL/vendors': No such file or directory
```

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ for i inls -1 /etc/OpenCL/vendors; do echo -n "$i : "; cat /etc/OpenCL/vendors/$i; done
-bash: syntax error near unexpected token `inls'
```
i assume it cant find dir or there is error in the loop here? 

---

### 评论 #8 — jlgreathouse (2018-08-23T23:43:21Z)

Oops, speaking of GitHub formatting noob, looks like I forgot that putting backticks in a bash command is going to make things throw up. The third command should have been:
```shell
for i in `ls -1 /etc/OpenCL/vendors`; do echo -n "$i : "; cat /etc/OpenCL/vendors/$i; done
```

That said, it's a bit weird that you don't have anything in /etc/OpenCL/vendors. This should be set up by default when installing ROCm, I believe. What steps did you go through to install ROCm and OpenCL? Did you just install the `rocm-dkms` package?

Try this:
```shell
sudo mkdir -p /etc/OpenCL/vendors/
echo 'libamdocl64.so' | sudo tee /etc/OpenCL/vendors/amdocl64.icd
/opt/rocm/opencl/bin/x86_64/clinfo
```

If the final line doesn't work, perhaps try it with `LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:$LD_LIBRARY_PATH /opt/rocm/opencl/bin/x86_64/clinfo`

---

### 评论 #9 — CatspersCoffee (2018-08-23T23:44:32Z)

Oh and no this was a clean install of 16.04 Desktop LTS, no other Nvidia cards were installed in this unit period. its only ever seen the 6x Vegas and no other AMD cards.

---

### 评论 #10 — CatspersCoffee (2018-08-23T23:45:32Z)

i followed this guide:
https://github.com/RadeonOpenCompute/ROCm


---

### 评论 #11 — jlgreathouse (2018-08-23T23:48:12Z)

I was able to reproduce the "-1001" value using the standard libOpenCL.so ICD loader that ships with Ubuntu 16.04 LTS. I see that error if I remove the AMD vendor ICD from /etc/OpenCL/vendors/, so I suspect that's part of the problem here.

To make sure I haven't messed up any of the directions on that page, could you also run:
`echo $LD_LIBRARY_PATH` and `echo $PATH` ?

---

### 评论 #12 — CatspersCoffee (2018-08-23T23:51:03Z)

```
sudo mkdir -p /opt/OpenCL/vendors/
[sudo] password for catsper:
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo 'libamdocl64.so' | sudo tee /etc/OpenCL/vendors/amdocl64.icd
tee: /etc/OpenCL/vendors/amdocl64.icd: No such file or directory
libamdocl64.so
```

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```
```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:$LD_LIBRARY_PATH /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

its strange because it looks like there is nothing inside the dir?
```
catsper@vegarig:/opt/OpenCL/vendors$ ls
catsper@vegarig:/opt/OpenCL/vendors$ pwd
/opt/OpenCL/vendors
catsper@vegarig:/opt/OpenCL/vendors$
```

results of PATH:
```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo $LD_LIBRARY_PATH

catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo $PATH
/home/catsper/bin:/home/catsper/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
catsper@vegarig:~/clARMOR/tests/good_cl_mem$

```

---

### 评论 #13 — jlgreathouse (2018-08-23T23:52:51Z)

Erk, sorry. I had a typo in a line. The first line should've been `sudo mkdir -p /etc/OpenCL/vendors`. If you could run that chunk of code again that sets the ICD, I'd appreciate it.

---

### 评论 #14 — CatspersCoffee (2018-08-23T23:56:49Z)

ok cool, here you go:

all the sets just to be sure ;-) 

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ sudo mkdir -p /etc/OpenCL/vendors
```
```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo 'libamdocl64.so' | sudo tee /etc/OpenCL/vendors/amdocl64.icd
libamdocl64.so
```

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP.internal (2574.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_object_metadata cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               6
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#5, D#0, F#0 ]
  Max compute units:                             64
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
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#14, D#0, F#0 ]
  Max compute units:                             64
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
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#17, D#0, F#0 ]
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
  Max clock frequency:                           1590Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#20, D#0, F#0 ]
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
  Max clock frequency:                           1590Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#23, D#0, F#0 ]
  Max compute units:                             64
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
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program


  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 687f
  Device Topology:                               PCI[ B#26, D#0, F#0 ]
  Max compute units:                             64
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
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
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
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
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
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7f877757b270
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                2574.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

```


---

### 评论 #15 — jlgreathouse (2018-08-23T23:59:57Z)

Great, looks like things are working as expected now. You may want to go try the 'good_cl_mem.exe" test again just to be sure a real application runs, but if clinfo works, you're probably good to go.

I am unsure why your ICD was not installed correctly by default; I've done a dozen (or more) ROCm installed since the last time we updated the ROCm repo, and it's worked every time on my systems. Odd.

By the way, you may want to run these commands so that in the future your ROCm-focused applications we all the right binaries and library directories:
```shell
echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$LD_LIBRARY_PATH' | sudo tee -a /etc/profile.d/rocm.sh
echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | sudo tee -a /etc/profile.d/rocm.sh
```

This is totally optional, though.

---

### 评论 #16 — CatspersCoffee (2018-08-24T00:06:40Z)

Great, thankyou, the result from 'good_cl_mem.exe" is:

```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ ./good_cl_mem.exe
Searching for platforms...
    Using platform: AMD Accelerated Parallel Processing
Searching for devices...
    Using device: gfx900


Running Good cl_mem Test...
    Using buffer size: 1048576
Launching 262144 work items to write up to 262144 entries.
This will write 1048576 out of 1048576 bytes in the buffer.
Done Running Good cl_mem Test.

```

and i have run the commands you suggest.. 
```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$LD_LIBRARY_PATH' | sudo tee -a /etc/profile.d/rocm.sh
[sudo] password for catsper:
export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$LD_LIBRARY_PATH
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | sudo tee -a /etc/profile.d/rocm.sh
export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64


```

let see what the miner program says on launch.. ( standby...  )


---

### 评论 #17 — CatspersCoffee (2018-08-24T00:11:53Z)

excellent! thankyou very much for the help!

what was the issue at the end of the day? ROCm and ICD not installign correctly? what is ICD ? 

```

catsper@vegarig:~/tdxminer-v0.2.2.2$ ./miner.sh
             tdxminer version 0.2.2.2
  This is a beta release and may be unstable on some hardware.
[2018-08-24 12:07:40] Successfully initialized GPU 0: Vega with 64 CU
[2018-08-24 12:07:40] Successfully initialized GPU 1: Vega with 64 CU
[2018-08-24 12:07:40] Successfully initialized GPU 2: Vega with 56 CU
[2018-08-24 12:07:40] Successfully initialized GPU 3: Vega with 56 CU
[2018-08-24 12:07:40] Successfully initialized GPU 4: Vega with 64 CU
[2018-08-24 12:07:40] Successfully initialized GPU 5: Vega with 64 CU
[2018-08-24 12:07:41] Pool xxx successfully subscribed.
[2018-08-24 12:07:41] Dev pool connected and ready.
[2018-08-24 12:07:41] Pool xxx authorization succeeded.
[2018-08-24 12:07:42] Pool xxx set difficulty to 1.000000
[2018-08-24 12:07:42] Pool xxx extranonce subscribe succeeded.
[2018-08-24 12:07:44] Pool xxx received new job. (job_id: b7ab)
[2018-08-24 12:07:46] Pool xxx share accepted.
[2018-08-24 12:07:46] Pool xxx share accepted.
[2018-08-24 12:07:46] Pool xxx share accepted.
```

---

### 评论 #18 — jlgreathouse (2018-08-24T00:17:32Z)

All OpenCL programs (or at least well-formed ones) will link against libOpenCL.so. However, it's possible that you might have multiple OpenCL runtime installations from multiple vendors. Imagine, for instance, if you wanted to use Intel's OpenCL runtime for CPUs (I think this still exists?) and AMD's OpenCL runtime for GPUs at the same time. You wouldn't want to write your program to try to load libOpenCL.intel.so and libOpenCL.amd.so (what if 20 more OpenCL implementations appeared overnight?)

So instead, libOpenCL.so is actually an [Installable Client Driver loader](https://www.khronos.org/news/permalink/opencl-installable-client-driver-icd-loader). It goes off into system-standard locations (like /etc/OpenCL/vendors/) and finds all of the OpenCL "platforms" in the system by looking into the .icd files to say "which file is the actual OpenCL platform runtime". Then it can enumerate all of these platforms, and your application can choose which one it wants.

For some reason, your ROCm installation put AMD's OpenCL runtime in the correct place (/opt/rocm/opencl/lib/x86_64/libamdocl64.so), but it did not install the proper .icd files. As such, your libOpenCL.so didn't see any platforms, because there were no .icd files to load. Again, I'm not sure why that happened, and I've been unable to repeat this issue when doing a fresh ROCm installation.

Glad we were able to get this working!

---

### 评论 #19 — CatspersCoffee (2018-08-24T00:27:20Z)

Hmm interesting. i will try do another fresh install on another PC with a Vega and let you know the results.

i wonder if it would be wise to post a script to check and install the correct .icd files while doing or after the ROCm install ?  or do you think this issue was concentrated to this particular install, i may have screwed something up along the way when installing ROCm in the first place.. so it could be as simple as a user (me) error.

---

### 评论 #20 — jlgreathouse (2018-08-24T00:34:45Z)

Installing this .icd file is done as part of installing the `rocmrocm-opencl` package. Specifically, these lines in the postinst commands of the .deb:
```shell
do_ldconfig() {
    echo /opt/rocm/opencl/lib/x86_64 > /etc/ld.so.conf.d/x86_64-rocm-opencl.conf && ldconfig
    mkdir -p /etc/OpenCL/vendors && (echo libamdocl64.so > /etc/OpenCL/vendors/amdocl64.icd)
}
```

As such, I'm not sure how it's possible to get that package installed and yet not have the ICD correctly installed. It's a mystery to me. :)

If this turns out to be a common problem, I'll look into a way to detect that this happened. As it stands, I'm not sure if this isn't just a fluke.

---

### 评论 #21 — CatspersCoffee (2018-08-24T07:21:29Z)

any idea after shutting down the rig and then restarting why tdx miner runs but GPU load is 0% and the miner does not do any hashing the miner can see all 6 GPU's and it connects to pool and receives jobs but there is no hashing going on? i dont understand what would have changed? 'clinfo' reports correctly and Running Good cl_mem Test is fine.

---

### 评论 #22 — CatspersCoffee (2018-08-24T07:28:21Z)

```
             tdxminer version 0.2.2.2
  This is a beta release and may be unstable on some hardware.
[2018-08-24 19:25:06] Successfully initialized GPU 0: Vega with 64 CU
[2018-08-24 19:25:06] Successfully initialized GPU 1: Vega with 64 CU
[2018-08-24 19:25:06] Successfully initialized GPU 2: Vega with 56 CU
[2018-08-24 19:25:06] Successfully initialized GPU 3: Vega with 56 CU
[2018-08-24 19:25:06] Successfully initialized GPU 4: Vega with 64 CU
[2018-08-24 19:25:06] Successfully initialized GPU 5: Vega with 64 CU
[2018-08-24 19:25:07] Dev pool connected and ready.
[2018-08-24 19:25:07] Pool xxx successfully subscribed.
[2018-08-24 19:25:07] Pool xxx authorization succeeded.
[2018-08-24 19:25:07] Pool xxx set difficulty to 1.000000
[2018-08-24 19:25:07] Pool xxx received new job. (job_id: ba45)
[2018-08-24 19:25:07] Pool xxx extranonce subscribe succeeded.
[2018-08-24 19:25:47] Pool xxx received new job. (job_id: ba46)
[2018-08-24 19:26:06] Stats GPU 0 -
[2018-08-24 19:26:06] Stats GPU 1 -
[2018-08-24 19:26:06] Stats GPU 2 -
[2018-08-24 19:26:06] Stats GPU 3 -
[2018-08-24 19:26:06] Stats GPU 4 -
[2018-08-24 19:26:06] Stats GPU 5 -
[2018-08-24 19:26:06] Stats Total -
```

---

### 评论 #23 — CatspersCoffee (2018-08-24T07:32:14Z)

ok,
so 'export HSA_ENABLE_SDMA=0' has to be run.
evidently this has to be done on startup

---

### 评论 #24 — CatspersCoffee (2018-08-25T05:35:04Z)

Ok im back to square one on this. rig was running find, then anotehr reboot and no devices found.
i have tried what we have gone through but no luck:
```
catsper@vegarig:~/clARMOR/tests/good_cl_mem$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```


---

### 评论 #25 — jlgreathouse (2018-08-25T05:43:31Z)

Please show the outputs of the non-OpenCL tests (rocminfo, hipinfo, the square example).

---

### 评论 #26 — CatspersCoffee (2018-08-25T05:51:26Z)

**for "dmesg | grep kfd":**
```
catsper@vegarig:~$ dmesg | grep kfd
[    1.570460] kfd kfd: Initialized module
[    3.746305] amdgpu 0000:05:00.0: kfd not supported on this ASIC
[    5.882866] amdgpu 0000:0b:00.0: kfd not supported on this ASIC
[    7.862110] amdgpu 0000:10:00.0: kfd not supported on this ASIC
[    9.855555] amdgpu 0000:13:00.0: kfd not supported on this ASIC
[   11.830535] amdgpu 0000:16:00.0: kfd not supported on this ASIC
[   14.038485] amdgpu 0000:19:00.0: kfd not supported on this ASIC
```

**for "rocminfo" :**

```
catsper@vegarig:~$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
```
for hipinfo:
```
catsper@vegarig:~/hipInfo$ ./hipInfo

compiler: hcc version=1.2.18272-47899bc-86791fc-c1f9263, workweek (YYWWD) = 18272
terminate called after throwing an instance of 'ihipException'
  what():  std::exception
Aborted (core dumped)
```
**for "square":**
```
catsper@vegarig:~/square$ ./square.out
terminate called after throwing an instance of 'ihipException'
  what():  std::exception
Aborted (core dumped)
```

**also checking kernel version:**
```
catsper@vegarig:~/square$ uname -a
Linux vegarig 4.15.0-33-generic #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```


---

### 评论 #27 — jlgreathouse (2018-08-25T05:57:17Z)

Oh, yeah, I see the problem. At the moment (#510), ROCm 1.8.2 is broken on Ubuntu kernel 4.15.0-33. It looks like between upgrades your system updated its kernel and you're falling back to a non-working KFD.

As mentioned in #510, we are working on solving this issue with a hotfix or point release. For now, I would recommend downgrading your kernel to 4.15.0-32.

---

### 评论 #28 — CatspersCoffee (2018-08-25T06:33:02Z)

ok cool, selecting kernel 4.15.0-32 on startup, everything is fine now. Thankyou for the quick reply, much appreciated :-) 

---
