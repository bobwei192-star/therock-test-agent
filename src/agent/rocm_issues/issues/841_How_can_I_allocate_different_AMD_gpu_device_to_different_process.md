# How can I allocate different AMD gpu device to different process?

> **Issue #841**
> **状态**: closed
> **创建时间**: 2019-07-11T06:34:03Z
> **更新时间**: 2022-11-05T13:26:02Z
> **关闭时间**: 2019-07-19T15:06:38Z
> **作者**: nanguanqi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/841

## 描述

Suppose, on the machine, there are 2 AMD gpu devices. How can I make process 1 use device0, process2 use device1?  Is there an environment variable like "CUDA_VISIABLE_DEVICES" to set visible AMD GPU devices for processes?

Dy default, are AMD GPU devices shared by all processes?

---

## 评论 (7 条)

### 评论 #1 — nanguanqi (2019-07-11T08:29:17Z)

If it is OpenCL application, set the GPU_DEVICE_ORDINAL environment parameter could help.  If it is HC or HIP application, does this GPU_DEVICE_ORDINAL  take effect to allocate gpu device to application?

---

### 评论 #2 — sunway513 (2019-07-11T20:36:04Z)

There're a couple of methods to expose only selected GPUs to the user process for hip/hcc path:
1. Use HIP_VISIBLE_DEVICES environment variable to select the target GPUs for the process from the HIP level. e.g. use the following to select the first GPU:

- export HIP_VISIBLE_DEVICES=0

2. Use ROCR_VISIBLE_DEVICES environment variable to select the target GPUs from the ROCr (ROCm user-bit driver) level. e.g. the following to select the first GPU:
- export ROCR_VISIBLE_DEVICES=0
3. Pass selected GPU driver interfaces (/dev/dri/render#) )to Docker container. e.g. use the following docker run command option to select the first GPU:
- `sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --group-add video `
Note you should see the following four interfaces if you have a 4xGPU system:
`$ ls /dev/dri/render* `
`/dev/dri/renderD128  /dev/dri/renderD129  /dev/dri/renderD130  /dev/dri/renderD131`


---

### 评论 #3 — nanguanqi (2019-07-12T04:03:23Z)

@sunway513  many thanks for your response. It is real helpful to me.  I am new for AMD GPU world, and I have no real environment for testing and experiment. Could I know more about ROCR_VISIBLE_DEVICES?

For ROCR_VISIBLE_DEVICES environment variable, does it work for both HCC, HIP and openCL applications?

Is there any environment pre-condition to use the ROCR_VISIBLE_DEVICES environment variable for exposing selected devices? What is difference between ROCm user-bit driver and driver installed from rocm-dkms primary meta-package?

If I install rocm platform via rocm-dkms primary meta-package way,  then I could leverage this variable to expose selected gpu devices for different application process?

---

### 评论 #4 — sunway513 (2019-07-13T15:51:40Z)

Hi @nanguanqi , you are welcome :-)
ROCR_VISIBLE_DEVICES operates on the ROCm ROCr runtime, that's under the layer below hip/hcc/math-libs etc; therefore, I'd assume it'll work equally for OCL path in ROCm stack. 

ROCm user bit drivers include [ROCr ](https://github.com/RadeonOpenCompute/ROCR-Runtime)and [THUNK](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface). 
If you use docker as an example, those two user bit drivers shall be included inside docker container. 
Rock-dkms, on the other hand, includes kernel driver (amdgpu) and device firmware, those must be installed on the bare metal. 
THUNK and amdgpu kernel driver talks via `/dev/dri` and `/dev/kfd` interfaces, you can consult with the following docker run command for ROCm containers:
`docker run -it --network=host --device=/dev/kfd --device=/dev/dri --group-add video`

And to your last question, yes, that would work. 


---

### 评论 #5 — Necktwi (2022-10-28T16:22:17Z)

@sunway513 but how do i confirm that my process is using the right device?

---

### 评论 #6 — sunway513 (2022-10-28T16:38:20Z)

> 

Hi, you can open another terminal and watch for the GPU activities using the following command:
`watch -n 0.1 rocm-smi`

---

### 评论 #7 — Necktwi (2022-11-05T13:26:02Z)

@sunway513, I got Radeon WX4100(node 1) and MI100(node 2), I've set `export HIP_VISIBLE_DEVICES=2; export ROCR_VISIBLE_DEVICES=2` and did `rocminfo` which show only node 1(wx4100) while I'm expecting node 2((MI100). I tried all the combinations 0,1,2 and "0,1,2" but the MI100 card will never be active except for "0,1,2".

---
