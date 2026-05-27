# ROCm docker doesn't work with some MI100 GPUs sets

> **Issue #1482**
> **状态**: closed
> **创建时间**: 2021-05-27T07:12:52Z
> **更新时间**: 2021-09-30T16:56:36Z
> **关闭时间**: 2021-09-29T14:59:55Z
> **作者**: simonschuang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1482

## 负责人

- ROCmSupport

## 描述

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



---

## 评论 (13 条)

### 评论 #1 — ROCmSupport (2021-06-01T10:19:35Z)

Thanks @simonschuang for reaching out.
We have seen this issue locally and ready with the fix.
Fix will be available in next release.
Thank you.

---

### 评论 #2 — jammm (2021-08-02T06:20:19Z)

@ROCmSupport when can we expect the next release?

---

### 评论 #3 — ROCmSupport (2021-08-03T05:14:35Z)

ROCm 4.3 is released couple of hours ago.
You can try and update the results.

---

### 评论 #4 — jammm (2021-08-04T11:40:20Z)

Thanks @ROCmSupport !
BTW, what if I want to use a different driver version instead of the one packaged with rock-dkms? For example, 21.20?
I've added a separate issue to discuss this here https://github.com/RadeonOpenCompute/ROCm/issues/1545

---

### 评论 #5 — jammm (2021-08-05T05:24:18Z)

Hello @ROCmSupport ,

Coming back to this issue, I'm still unable to setup a single GPU on a docker container with ROCm 4.3. It's the same issue as outlined above.
What's the proper way to select a single gpu from /dev/dri/.. ?

---

### 评论 #6 — ROCmSupport (2021-08-05T05:48:10Z)

Hi @jammm 
To run the docker container a specific device, run the command like this:

**To run on a first GPU alone:**
sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 seccomp=unconfined --group-add video -v $HOME/dockerx:/dockerx <docker-image>

**To run on first 2 GPUs:**
sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --device=/dev/dri/renderD129 seccomp=unconfined --group-add video -v $HOME/dockerx:/dockerx <docker-image>

Likewise you keep adding render devices like renderD128, 129, 130 etc.,.

---

### 评论 #7 — jammm (2021-08-05T06:48:43Z)

@ROCmSupport The above commands don't work (you missed the --security-opt flag, I think)
After adding that flag, I still can't seem to use a specific GPU. For example, in a 4 GPU machine, if I want to use the 2nd GPU alone (/dev/dri/renderD129), I instead get 3 GPU's in rocm-smi:
![image](https://user-images.githubusercontent.com/2500920/128304349-f2059b37-aec7-46dd-a26f-f48b715dc1b2.png)


---

### 评论 #8 — ROCmSupport (2021-08-05T09:44:04Z)

Hi @jammm 
The above command is a generic one. You can add many flags as per your requirement as per docker documentation.
I casually use this way:
sudo docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=64G -v $HOME/dockerx:/dockerx <docker_image>

Let me validate this issue with ROCm 4.3 now.

---

### 评论 #9 — ROCmSupport (2021-08-05T10:17:16Z)

Looks like issue is resolved with 4.3
I tried on 4.3 host + 4.3 docker on a 2*MI50 machine and here are the results.

taccuser@taccuser-SYS-4028GR-TR2:~$ sudo docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri/renderD129 --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=64G -v $HOME/dockerx:/dockerx rocm/dev-ubuntu-18.04:4.3-complete
root@taccuser-SYS-4028GR-TR2:/# /opt/rocm/bin/rocm-smi

======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%
0    29.0c  15.0W   930Mhz  350Mhz  255%  auto  225.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
root@taccuser-SYS-4028GR-TR2:/# exit
logout
taccuser@taccuser-SYS-4028GR-TR2:~$ sudo docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=64G -v $HOME/dockerx:/dockerx rocm/dev-ubuntu-18.04:4.3-complete
root@taccuser-SYS-4028GR-TR2:/# /opt/rocm/bin/rocm-smi

 


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%
0    29.0c  15.0W   930Mhz  350Mhz  255%  auto  225.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
root@taccuser-SYS-4028GR-TR2:/# exit
logout
taccuser@taccuser-SYS-4028GR-TR2:~$ sudo docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=64G -v $HOME/dockerx:/dockerx rocm/dev-ubuntu-18.04:4.3-complete
root@taccuser-SYS-4028GR-TR2:/# /opt/rocm/bin/rocm-smi

 


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%
0    29.0c  15.0W   930Mhz  350Mhz  255%  auto  225.0W    0%   0%
1    30.0c  15.0W   930Mhz  350Mhz  255%  auto  225.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log

---

### 评论 #10 — jammm (2021-08-05T10:30:42Z)

Seems like my host machine ubuntu 18.04 didn't have kernel 5.4 on it (it's 4.15)
I'll upgrade the kernel to 5.4 and report back my findings. Thanks!

---

### 评论 #11 — simonschuang (2021-09-29T14:59:55Z)

Hi guys, we have verified the issue has been fixed at latest release of ROCm 4.3.
There is no problem to me to launch docker with selected MI100 GPUs. I will close this issue, thank you!

# Try GPU 1, 3
```
giga4@g492:~$ sudo docker run -it --rm --network=host --device=/dev/kfd --device=/dev/dri/renderD131 --device=/dev/dri/renderD133 --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=64G -v $HOME/dockerx:/dockerx --entrypoint=/bin/bash rocm/tensorflow:rocm4.3.1-tf2.6-dev
root@g492:/root# rocm-smi --showbus


======================= ROCm System Management Interface =======================
================================== PCI Bus ID ==================================
GPU[0]          : PCI Bus: 0000:D7:00.0
GPU[1]          : PCI Bus: 0000:E2:00.0
================================================================================
============================= End of ROCm SMI Log ==============================
root@g492:/root# python3.6 ~/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow/python/compat/v2_compat.py:101: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
2021-09-06 09:50:19.869948: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-09-06 09:50:19.870542: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 31740 MB memory:  -> device: 0, name: Device 738c, pci bus id: 0000:d7:00.0
2021-09-06 09:50:20.199962: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:1 with 31740 MB memory:  -> device: 1, name: Device 738c, pci bus id: 0000:e2:00.0
TensorFlow:  2.6
Model:       trivial
Dataset:     imagenet (synthetic)
Mode:        training
SingleSess:  False
Batch size:  32 global
             32 per device
Num batches: 100
Num epochs:  0.00
Devices:     ['/gpu:0']
NUMA bind:   False
Data format: NCHW
Optimizer:   sgd
Variables:   parameter_server
==========
Generating training model
Initializing graph
WARNING:tensorflow:From /root/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2268: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
W0906 09:50:20.617376 140163200104256 deprecation.py:345] From /root/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2268: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
2021-09-06 09:50:20.638027: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 31740 MB memory:  -> device: 0, name: Device 738c, pci bus id: 0000:d7:00.0
2021-09-06 09:50:20.638253: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1510] Created device /job:localhost/replica:0/task:0/device:GPU:1 with 31740 MB memory:  -> device: 1, name: Device 738c, pci bus id: 0000:e2:00.0
2021-09-06 09:50:20.660838: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
INFO:tensorflow:Running local_init_op.
I0906 09:50:20.947933 140163200104256 session_manager.py:531] Running local_init_op.
2021-09-06 09:50:20.956659: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
INFO:tensorflow:Done running local_init_op.
I0906 09:50:20.982545 140163200104256 session_manager.py:534] Done running local_init_op.
2021-09-06 09:50:20.992772: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2021-09-06 09:50:20.995656: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2021-09-06 09:50:20.997336: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
Running warm up
2021-09-06 09:50:21.019260: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
Done warm up
Step    Img/sec total_loss
1       images/sec: 18686.6 +/- 0.0 (jitter = 0.0)      9.330
10      images/sec: 17603.5 +/- 211.0 (jitter = 833.2)  9.330
20      images/sec: 18464.3 +/- 249.9 (jitter = 1454.3) 9.330
30      images/sec: 18968.1 +/- 215.9 (jitter = 1157.4) 9.330
40      images/sec: 19219.4 +/- 176.8 (jitter = 945.0)  9.330
50      images/sec: 19380.9 +/- 149.2 (jitter = 691.9)  9.330
60      images/sec: 19445.9 +/- 128.4 (jitter = 658.6)  9.330
70      images/sec: 19492.8 +/- 112.3 (jitter = 597.0)  9.330
80      images/sec: 19532.3 +/- 100.2 (jitter = 544.1)  9.330
90      images/sec: 19577.8 +/- 91.2 (jitter = 553.3)   9.330
100     images/sec: 19544.5 +/- 92.7 (jitter = 545.2)   9.330
----------------------------------------------------------------
total images/sec: 18902.21
----------------------------------------------------------------

```

---

### 评论 #12 — jammm (2021-09-29T15:01:02Z)

@simonschuang can you also try only GPU 3 or only GPU 2?

---

### 评论 #13 — simonschuang (2021-09-30T16:56:36Z)

@jammm I have tried three cases: using GPU 0+1+2,  using GPU 0+1 and using GPU 1+3. All works.
Sorry I have returned all borrowed GPUs, I can't try only GPU 3 or 2.. :( 

---
