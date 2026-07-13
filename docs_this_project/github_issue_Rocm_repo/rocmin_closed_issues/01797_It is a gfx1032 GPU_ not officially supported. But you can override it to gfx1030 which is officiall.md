# It is a gfx1032 GPU, not officially supported. But you can override it to gfx1030 which is officially supported. That actually works.

- **Issue #:** 1797
- **State:** closed
- **Created:** 2022-08-24T08:03:58Z
- **Updated:** 2022-08-24T08:07:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1797

It is a gfx1032 GPU, not officially supported. But you can override it to gfx1030 which is officially supported. That actually works.
https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html

I have tested that on a gfx1032 GPU with pytorch mnist example.

Make sure amdgpu kernel mode driver is installed.
If you use a generic kernel on Ubuntu 20.04, install amdgpu kernel mode driver as following 
```
sudo apt-get update
wget https://repo.radeon.com/amdgpu-install/22.10.3/ubuntu/focal/amdgpu-install_22.10.3.50103-1_all.deb 
sudo apt-get install ./amdgpu-install_22.10.3.50103-1_all.deb

amdgpu-install --usecase=dkms
```
Pull and run pytorch docker image.
```
sudo docker pull rocm/pytorch:latest

sudo docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latest

root@cdd69b58e233:/var/lib/jenkins# python3
Python 3.7.13 (default, Mar 29 2022, 02:18:16)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
Aborted (core dumped)
root@cdd69b58e233:/var/lib/jenkins#

root@cdd69b58e233:/var/lib/jenkins# HSA_OVERRIDE_GFX_VERSION=10.3.0 python3
Python 3.7.13 (default, Mar 29 2022, 02:18:16)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>>

```

```
root@cdd69b58e233:/var/lib/jenkins# rocminfo
*******
Agent 2
*******
  Name:                    gfx1032
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon PRO W6600
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      2048(0x800) KB
    L3:                      32768(0x8000) KB
  Chip ID:                 29667(0x73e3)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2910
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            28
  SIMDs per CU:            2
  Shader Engines:          4
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
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
      Name:                    amdgcn-amd-amdhsa--gfx1032
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
```
```
root@cdd69b58e233:/var/lib/jenkins/pytorch/examples/mnist# HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 main.py
...
Train Epoch: 14 [0/60000 (0%)]  Loss: 0.029361
Train Epoch: 14 [640/60000 (1%)]        Loss: 0.020166
Train Epoch: 14 [1280/60000 (2%)]       Loss: 0.008040
Train Epoch: 14 [1920/60000 (3%)]       Loss: 0.051216
Train Epoch: 14 [2560/60000 (4%)]       Loss: 0.001075
Train Epoch: 14 [3200/60000 (5%)]       Loss: 0.057989
Train Epoch: 14 [3840/60000 (6%)]       Loss: 0.039574
Train Epoch: 14 [4480/60000 (7%)]       Loss: 0.005929
Train Epoch: 14 [5120/60000 (9%)]       Loss: 0.090919
Train Epoch: 14 [5760/60000 (10%)]      Loss: 0.070765
Train Epoch: 14 [6400/60000 (11%)]      Loss: 0.005689
Train Epoch: 14 [7040/60000 (12%)]      Loss: 0.022842
Train Epoch: 14 [7680/60000 (13%)]      Loss: 0.025918
Train Epoch: 14 [8320/60000 (14%)]      Loss: 0.011779
Train Epoch: 14 [8960/60000 (15%)]      Loss: 0.009255
Train Epoch: 14 [9600/60000 (16%)]      Loss: 0.012456
Train Epoch: 14 [10240/60000 (17%)]     Loss: 0.015307
Train Epoch: 14 [10880/60000 (18%)]     Loss: 0.001581
Train Epoch: 14 [11520/60000 (19%)]     Loss: 0.007551
Train Epoch: 14 [12160/60000 (20%)]     Loss: 0.007114
Train Epoch: 14 [12800/60000 (21%)]     Loss: 0.006242
Train Epoch: 14 [13440/60000 (22%)]     Loss: 0.003852
Train Epoch: 14 [14080/60000 (23%)]     Loss: 0.025893
Train Epoch: 14 [14720/60000 (25%)]     Loss: 0.024052
Train Epoch: 14 [15360/60000 (26%)]     Loss: 0.007025
Train Epoch: 14 [16000/60000 (27%)]     Loss: 0.005092
Train Epoch: 14 [16640/60000 (28%)]     Loss: 0.001427
Train Epoch: 14 [17280/60000 (29%)]     Loss: 0.003324
Train Epoch: 14 [17920/60000 (30%)]     Loss: 0.001264
Train Epoch: 14 [18560/60000 (31%)]     Loss: 0.002595
Train Epoch: 14 [19200/60000 (32%)]     Loss: 0.003115
Train Epoch: 14 [19840/60000 (33%)]     Loss: 0.019476
Train Epoch: 14 [20480/60000 (34%)]     Loss: 0.005185
Train Epoch: 14 [21120/60000 (35%)]     Loss: 0.032551
Train Epoch: 14 [21760/60000 (36%)]     Loss: 0.013329
Train Epoch: 14 [22400/60000 (37%)]     Loss: 0.088533
Train Epoch: 14 [23040/60000 (38%)]     Loss: 0.083046
Train Epoch: 14 [23680/60000 (39%)]     Loss: 0.014655
Train Epoch: 14 [24320/60000 (41%)]     Loss: 0.062322
Train Epoch: 14 [24960/60000 (42%)]     Loss: 0.030058
Train Epoch: 14 [25600/60000 (43%)]     Loss: 0.028837
Train Epoch: 14 [26240/60000 (44%)]     Loss: 0.016934
Train Epoch: 14 [26880/60000 (45%)]     Loss: 0.001474
Train Epoch: 14 [27520/60000 (46%)]     Loss: 0.046969
Train Epoch: 14 [28160/60000 (47%)]     Loss: 0.011573
Train Epoch: 14 [28800/60000 (48%)]     Loss: 0.029901
Train Epoch: 14 [29440/60000 (49%)]     Loss: 0.002406
Train Epoch: 14 [30080/60000 (50%)]     Loss: 0.035965
Train Epoch: 14 [30720/60000 (51%)]     Loss: 0.022652
Train Epoch: 14 [31360/60000 (52%)]     Loss: 0.017276
Train Epoch: 14 [32000/60000 (53%)]     Loss: 0.006537
Train Epoch: 14 [32640/60000 (54%)]     Loss: 0.017766
Train Epoch: 14 [33280/60000 (55%)]     Loss: 0.016734
Train Epoch: 14 [33920/60000 (57%)]     Loss: 0.014395
Train Epoch: 14 [34560/60000 (58%)]     Loss: 0.044845
Train Epoch: 14 [35200/60000 (59%)]     Loss: 0.009965
Train Epoch: 14 [35840/60000 (60%)]     Loss: 0.001743
Train Epoch: 14 [36480/60000 (61%)]     Loss: 0.148522
Train Epoch: 14 [37120/60000 (62%)]     Loss: 0.028784
Train Epoch: 14 [37760/60000 (63%)]     Loss: 0.001296
Train Epoch: 14 [38400/60000 (64%)]     Loss: 0.088509
Train Epoch: 14 [39040/60000 (65%)]     Loss: 0.011910
Train Epoch: 14 [39680/60000 (66%)]     Loss: 0.022110
Train Epoch: 14 [40320/60000 (67%)]     Loss: 0.002538
Train Epoch: 14 [40960/60000 (68%)]     Loss: 0.033725
Train Epoch: 14 [41600/60000 (69%)]     Loss: 0.025057
Train Epoch: 14 [42240/60000 (70%)]     Loss: 0.022314
Train Epoch: 14 [42880/60000 (71%)]     Loss: 0.006667
Train Epoch: 14 [43520/60000 (72%)]     Loss: 0.008564
Train Epoch: 14 [44160/60000 (74%)]     Loss: 0.066551
Train Epoch: 14 [44800/60000 (75%)]     Loss: 0.003902
Train Epoch: 14 [45440/60000 (76%)]     Loss: 0.017624
Train Epoch: 14 [46080/60000 (77%)]     Loss: 0.069699
Train Epoch: 14 [46720/60000 (78%)]     Loss: 0.060984
Train Epoch: 14 [47360/60000 (79%)]     Loss: 0.009416
Train Epoch: 14 [48000/60000 (80%)]     Loss: 0.028712
Train Epoch: 14 [48640/60000 (81%)]     Loss: 0.010477
Train Epoch: 14 [49280/60000 (82%)]     Loss: 0.027884
Train Epoch: 14 [49920/60000 (83%)]     Loss: 0.003463
Train Epoch: 14 [50560/60000 (84%)]     Loss: 0.005643
Train Epoch: 14 [51200/60000 (85%)]     Loss: 0.094961
Train Epoch: 14 [51840/60000 (86%)]     Loss: 0.011150
Train Epoch: 14 [52480/60000 (87%)]     Loss: 0.025268
Train Epoch: 14 [53120/60000 (88%)]     Loss: 0.001729
Train Epoch: 14 [53760/60000 (90%)]     Loss: 0.039884
Train Epoch: 14 [54400/60000 (91%)]     Loss: 0.011366
Train Epoch: 14 [55040/60000 (92%)]     Loss: 0.004681
Train Epoch: 14 [55680/60000 (93%)]     Loss: 0.001321
Train Epoch: 14 [56320/60000 (94%)]     Loss: 0.092475
Train Epoch: 14 [56960/60000 (95%)]     Loss: 0.032426
Train Epoch: 14 [57600/60000 (96%)]     Loss: 0.011749
Train Epoch: 14 [58240/60000 (97%)]     Loss: 0.017789
Train Epoch: 14 [58880/60000 (98%)]     Loss: 0.015819
Train Epoch: 14 [59520/60000 (99%)]     Loss: 0.014150

Test set: Average loss: 0.0283, Accuracy: 9909/10000 (99%)
```

_Originally posted by @xfyucg in https://github.com/RadeonOpenCompute/ROCm/issues/1756#issuecomment-1159603527_