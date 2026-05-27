# monitor turn off after start tensorflow training

> **Issue #1270**
> **状态**: closed
> **创建时间**: 2020-10-29T04:39:35Z
> **更新时间**: 2020-12-11T05:32:12Z
> **关闭时间**: 2020-12-11T05:32:12Z
> **作者**: mrmoein
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1270

## 描述

hello 
when i try train my model , screen turn off and get no signal and monitor go to sleep mode

ryzen 5 2600
rx 580
ubuntu 20.04
kernel 5.4

Is there a log file?
idk what to do!

---

## 评论 (9 条)

### 评论 #1 — xuhuisheng (2020-10-29T05:08:10Z)

ROCm-3.7.0+ may halt the gfx803 gpu. Could you have a try with ROCm-3.5.1?
Please refer: https://github.com/RadeonOpenCompute/ROCm/issues/1265

---

### 评论 #2 — mrmoein (2020-10-29T15:38:35Z)

> ROCm-3.7.0+ may halt the gfx803 gpu. Could you have a try with ROCm-3.5.1?
> Please refer: #1265

i downgrade to 3.5.1 (reinstall os and fresh install everything) but problem still exist :(

---

### 评论 #3 — rkothako (2020-11-02T07:49:27Z)

Hi @mrmoein 
Thanks for the issue. Looks like its an environmental issue.
Can you please share detailed steps to reproduce the issue.
Thank you.

---

### 评论 #4 — mrmoein (2020-11-04T15:17:25Z)

@rkothako 
i am new in linux (one year experince) and machine learning (just started), Maybe I am installing wrong

### my installing steps:

this is my fresh install:
> System:    Host: moein-pc Kernel: 5.4.0-52-generic x86_64 bits: 64 Desktop: Cinnamon 4.6.7 Distro: Linux Mint 20 Ulyana 
Machine:   Type: Desktop Mobo: ASUSTeK model: PRIME B450M-A v: Rev X.0x serial: <superuser/root required> 
           UEFI: American Megatrends v: 2203 date: 07/28/2020 
CPU:       Topology: 6-Core model: AMD Ryzen 5 2600 bits: 64 type: MT MCP L2 cache: 3072 KiB 
           Speed: 1555 MHz min/max: 1550/3400 MHz Core speeds (MHz): 1: 1546 2: 1558 3: 1543 4: 1540 5: 1546 6: 1566 7: 1547 
           8: 1558 9: 1541 10: 1544 11: 1543 12: 1545 
Graphics:  Device-1: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] driver: amdgpu 
           v: 5.6.0 
           Display: x11 server: X.Org 1.20.8 driver: amdgpu,ati unloaded: fbdev,modesetting,vesa resolution: 1920x1080~60Hz 
           OpenGL: renderer: Radeon RX 580 Series (POLARIS10 DRM 3.37.0 5.4.0-52-generic LLVM 10.0.0) v: 4.6 Mesa 20.0.8 
Audio:     Device-1: AMD Ellesmere HDMI Audio [Radeon RX 470/480 / 570/580/590] driver: snd_hda_intel 
           Device-2: Advanced Micro Devices [AMD] Family 17h HD Audio driver: snd_hda_intel 
           Sound Server: ALSA v: k5.4.0-52-generic 
Network:   Device-1: Realtek RTL8111/8168/8411 PCI Express Gigabit Ethernet driver: r8169 
           IF: enp7s0 state: up speed: 100 Mbps duplex: full mac: 0c:9d:92:c7:30:53 
Drives:    Local Storage: total: 2.05 TiB used: 277.70 GiB (13.2%) 
           ID-1: /dev/sda vendor: Western Digital model: WD20EZRZ-22Z5HB0 size: 1.82 TiB 
           ID-2: /dev/sdb vendor: Silicon Power model: SPCC Solid State Disk size: 238.47 GiB 
Partition: ID-1: / size: 58.04 GiB used: 20.63 GiB (35.5%) fs: ext4 dev: /dev/sdb5 
           ID-2: /home size: 537.81 GiB used: 257.03 GiB (47.8%) fs: ext4 dev: /dev/sda4 
Sensors:   System Temperatures: cpu: 32.8 C mobo: N/A gpu: amdgpu temp: 36 C 
           Fan Speeds (RPM): N/A gpu: amdgpu fan: 1278 
Info:      Processes: 334 Uptime: 24m Memory: 15.63 GiB used: 1.61 GiB (10.3%) Shell: bash inxi: 3.0.38 


note: same problem in ubuntu 20.04 with kernel 5.4
note: Python 3.8.5
note: tensorflow-rocm version 2.3.2
note: Rocm 3.5.1

step 1: i install rocm from this guid => [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu)

> /opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo

seems fine and work
also `rocm-smi` work but some python errors display befor results

> /opt/rocm/bin/rocm-smi:816: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if clocktype is 'freq':
/opt/rocm/bin/rocm-smi:901: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if component is 'driver':
/opt/rocm/bin/rocm-smi:923: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if (retiredType is 'all' or \
/opt/rocm/bin/rocm-smi:924: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'retired' and pgType is 'R' or \
/opt/rocm/bin/rocm-smi:924: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'retired' and pgType is 'R' or \
/opt/rocm/bin/rocm-smi:925: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'pending' and pgType is 'P' or \
/opt/rocm/bin/rocm-smi:925: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'pending' and pgType is 'P' or \
/opt/rocm/bin/rocm-smi:926: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'unreservable' and pgType is 'F'):
/opt/rocm/bin/rocm-smi:926: SyntaxWarning: "is" with a literal. Did you mean "=="?
  retiredType is 'unreservable' and pgType is 'F'):
/opt/rocm/bin/rocm-smi:1501: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if component is 'driver':
/opt/rocm/bin/rocm-smi:1938: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if ptype is 'R':
/opt/rocm/bin/rocm-smi:1940: SyntaxWarning: "is" with a literal. Did you mean "=="?
  elif ptype is 'P':
/opt/rocm/bin/rocm-smi:2395: SyntaxWarning: "is" with a literal. Did you mean "=="?
  if clkType is 'sclk':
/opt/rocm/bin/rocm-smi:2397: SyntaxWarning: "is" with a literal. Did you mean "=="?
  elif clkType is 'mclk':
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr   SCLK    MCLK     Fan    Perf  PwrCap  VRAM%  GPU%  
0    32.0c  31.251W  600Mhz  2000Mhz  29.8%  auto  165.0W    2%   0%    
================================================================================


step 2:  i make a virtual environment with pycharm and follow this 3 steps from this link:
[https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#amd-rocm-tensorflow-v2-2-0-beta1-release](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#amd-rocm-tensorflow-v2-2-0-beta1-release)
also i cant install `cxlactivitylogger` and get this error `E: Unable to locate package cxlactivitylogger`

step 3: after install tensorflow i run this script:

> import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

and the result is
> 2020-11-04 21:20:22.721520: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-11-04 21:20:23.384511: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:08:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.38GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-11-04 21:20:23.592651: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-11-04 21:20:23.593659: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-11-04 21:20:23.834415: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-11-04 21:20:23.835650: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-11-04 21:20:23.835772: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
Num GPUs Available:  1


step 4: after that i run this commend:
`cd ~ && git clone -b cnn_tf_v1.15_compatible https://github.com/tensorflow/benchmarks.git && 
python ~/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=resnet50`
and after few seconds (when training start) the screen turns off
same problem when i train my model

i try ssh to my pc from another one and run again the script:
> import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

but this time i receive => Num GPUs Available:  0


---

### 评论 #5 — rkothako (2020-11-05T08:38:00Z)

Thanks @mrmoein 
Issue is not reproducible with gfx9 devices. Looks like specific to gfx8 devices.

---

### 评论 #6 — mrmoein (2020-11-20T19:34:31Z)

i still can't fix the problem! where is the log file? is it exist?

---

### 评论 #7 — ROCmSupport (2020-11-23T04:58:50Z)

Hi @mrmoein 
Is the issue observed only with ROCm? 
For me, looks like, issue is specific to your config.
Because with and without ROCm, we are not able to reproduce this issue here.

---

### 评论 #8 — mrmoein (2020-11-23T05:45:42Z)

> Hi @mrmoein
> Is the issue observed only with ROCm?
> For me, looks like, issue is specific to your config.
> Because with and without ROCm, we are not able to reproduce this issue here.

hello, two time when i play "Left for dead" in middle of game this problem happend too. i think when turn vsinc off the game use 100% of my gpu and this happened!

but when i start tensorflow it happens all time.

i check my gpu temperature but it is ok.

---

### 评论 #9 — ROCmSupport (2020-11-23T05:58:46Z)

Thanks @mrmoein for additional information.
So it means, its not ROCm issue.

---
