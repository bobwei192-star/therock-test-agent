# ROCm docker doesn't work with some MI100 GPUs sets

- **Issue #:** 1482
- **State:** closed
- **Created:** 2021-05-27T07:12:52Z
- **Updated:** 2021-09-30T16:56:36Z
- **Assignees:** ROCmSupport
- **URL:** https://github.com/ROCm/ROCm/issues/1482

Problems description:
--------------------------
Follow the rocm-docker [guide](https://rocmdocs.amd.com/en/latest/ROCm_Virtualization_Containers/ROCm-Virtualization-&-Containers.html#rocm-docker) to pass through GPUs into containers
It works well with all four GPUs passthrough into a docker container, but it doesn't works when specify some sets of GPUs into a conatiner. rocm-smi shows GPUs, but rocminfo shows no GPU. In consequence, Tensorflow shows HIP_ERROR_NoDevice


Environment:
---------------
OS: Ubuntu 20.04.2 LTS (Focal Fossa)
GPU model : AMD 4*MI100 gpus, gfx908 arch. Connected with an AMD Infinity Fabric 
ROCm version: 4.2.0
Linux Kernel:  5.4.0-58-generic

Reproduces Steps:
---------------------
1. There are four MI100 GPUs on server

AMD GPU devices see in the OS: /dev/dri/renderD128 , renderD129, renderD130, renderD131
```
xxx@xxx:~/$ rocm-smi --showbus


======================= ROCm System Management Interface =======================
================================== PCI Bus ID ==================================
GPU[0]          : PCI Bus: 0000:41:00.0
GPU[1]          : PCI Bus: 0000:D7:00.0
GPU[2]          : PCI Bus: 0000:DC:00.0
GPU[3]          : PCI Bus: 0000:E2:00.0
================================================================================
============================= End of ROCm SMI Log ==============================
xxx@xxx:~/$ ls -al /dev/dri/by-path/ | grep renderD
lrwxrwxrwx 1 root root  13 May 12 06:52 pci-0000:41:00.0-render -> ../renderD128
lrwxrwxrwx 1 root root  13 May 12 06:52 pci-0000:d7:00.0-render -> ../renderD129
lrwxrwxrwx 1 root root  13 May 12 06:52 pci-0000:dc:00.0-render -> ../renderD130
lrwxrwxrwx 1 root root  13 May 12 06:52 pci-0000:e2:00.0-render -> ../renderD131

```
2. Launch docker container with first AMD GPUs, and it works normally
```
docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --device=/dev/dri/renderD129 seccomp=unconfined --group-add video rocm/rocm-terminal bash
```
```
rocm-user@d96d5240c68e:~$ rocm-smi


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK     Fan   Perf  PwrCap  VRAM%  GPU%
0    34.0c  37.0W   300Mhz  1200Mhz  0.0%  auto  290.0W    0%   0%
1    33.0c  39.0W   300Mhz  1200Mhz  0.0%  auto  290.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
rocm-user@d96d5240c68e:~$ sudo rocminfo
ROCk module is loaded
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
(skip)
*******
Agent 3
*******
  Name:                    gfx908
  Uuid:                    GPU-93855a2eb929ce13
  Marketing Name:          Arcturus GL-XL [AMD Instinct MI100]
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
(skip)
*** Done ***

```

3. Launch docker container with first and third GPUs, it doesn't works
For example, we specify renderD128, renderD130 to a container, rocm-smi will grab two GPUs, but rocminfo shows empty section in "HSA Agent"
```
docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --device=/dev/dri/renderD130 seccomp=unconfined --group-add video rocm/rocm-terminal bash

```

```
rocm-user@c6d0207a8a35:~$ rocm-smi


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK     Fan   Perf  PwrCap  VRAM%  GPU%
0    32.0c  37.0W   300Mhz  1200Mhz  0.0%  auto  290.0W    0%   0%
1    31.0c  38.0W   300Mhz  1200Mhz  0.0%  auto  290.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
rocm-user@c6d0207a8a35:~$ sudo rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  12884.901889MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*** Done ***
```
Run Tensorflow example code shows "HIP_ERROR_NoDevice"
```
python mnist_test.py
...
could not retrieve ROCM device count: HIP_ERROR_NoDevice
...
{RUN in CPU mode}
```

4. Following GPU set combinations work normally:
* /dev/dri/renderD128
* /dev/dri/renderD129
* /dev/dri/renderD128 + /dev/dri/renderD129
* /dev/dri/renderD128 + /dev/dri/renderD129 + /dev/dri/renderD130
* /dev/dri/renderD128 + /dev/dri/renderD129 + /dev/dri/renderD130 + /dev/dri/renderD131

5. But the issue happens with other GPUs combinations:
* /dev/dri/renderD128 + /dev/dri/renderD130
* /dev/dri/renderD128 + /dev/dri/renderD131
* /dev/dri/renderD130 + /dev/dri/renderD131
...

