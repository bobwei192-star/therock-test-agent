# problem running tensorflow after installing rocm 1.9

> **Issue #536**
> **状态**: closed
> **创建时间**: 2018-09-15T10:57:32Z
> **更新时间**: 2018-09-16T17:26:44Z
> **关闭时间**: 2018-09-16T17:26:44Z
> **作者**: witeko
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/536

## 描述

After installing rocm 1.9 my "Python 3: http://repo.radeon.com/rocm/misc/tensorflow/tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl" (from: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) doesn't work for training models using my GPU. It used to work on rocm 1.8.3. 

When I run cifar training from (git clone https://github.com/tensorflow/models.git) I get the following:
```
(gpu_ts18) witold@witold-r7:~/models-master/tutorials/image/cifar10$ python cifar10_train.py 
/home/witold/anaconda3/envs/gpu_ts18/lib/python3.5/site-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
>> Downloading cifar-10-binary.tar.gz 100.0%
Successfully downloaded cifar-10-binary.tar.gz 170052171 bytes.
Filling queue with 20000 CIFAR images before starting to train. This will take a few minutes.
2018-09-15 12:40:39.887189: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-15 12:40:39.892631: W tensorflow/stream_executor/rocm/rocm_driver.cc:404] creating context when one is currently active; existing: 0x55912a2d3a90
2018-09-15 12:40:39.893133: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1451] Found device 0 with properties: 
name: Ellesmere [Radeon RX 470/480]
AMDGPU ISA: gfx803
memoryClockRate (GHz) 1.34
pciBusID 0000:42:00.0
Total memory: 8.00GiB
Free memory: 7.75GiB
2018-09-15 12:40:39.893147: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1562] Adding visible gpu devices: 0
2018-09-15 12:40:39.893167: I tensorflow/core/common_runtime/gpu/gpu_device.cc:989] Device interconnect StreamExecutor with strength 1 edge matrix:
2018-09-15 12:40:39.893174: I tensorflow/core/common_runtime/gpu/gpu_device.cc:995]      0 
2018-09-15 12:40:39.893179: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1008] 0:   N 
2018-09-15 12:40:39.893671: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1124] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7539 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480], pci bus id: 0000:42:00.0)
clang (LLVM option parsing): Unknown command line argument '-enable-si-insert-waitcnts'.  Try: 'clang (LLVM option parsing) -help'
clang (LLVM option parsing): Did you mean '-enable-post-misched'?
MIOpen Error: /data/repo/MIOpen/src/tmp_dir.cpp:18: Can't execute cd /tmp/miopen-MIOpenUtilKernels.cl-404f-de5f-4a8e-6657; /opt/rocm/bin/clang-ocl  -DNUM_CH_PER_WG=1 -DNUM_IM_BLKS_X=1 -DNUM_IM_BLKS=3 -DLOCAL_MEM_SIZE=432 -DSTRIDE_GT_1=0 -DTILE_SZ_X=32 -DTILE_SZ_Y=8 -DUSE_IM_OFF_GUARD=1 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -mcpu=gfx803 -Wno-everything MIOpenUtilKernels.cl -o /tmp/miopen-MIOpenUtilKernels.cl-404f-de5f-4a8e-6657/MIOpenUtilKernels.cl.o
2018-09-15 12:40:51.352749: F tensorflow/stream_executor/rocm/rocm_dnn.cc:1803] Check failed: status == miopenStatusSuccess (7 vs. 0)Unable to find a suitable algorithm for doing forward convolution
Aborted (core dumped)
```
```
(gpu_ts18) witold@witold-r7:~/models-master/tutorials/image/cifar10$ python cifar10_train.py 
/home/witold/anaconda3/envs/gpu_ts18/lib/python3.5/site-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
Filling queue with 20000 CIFAR images before starting to train. This will take a few minutes.
2018-09-15 12:41:27.375043: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2018-09-15 12:41:27.379509: W tensorflow/stream_executor/rocm/rocm_driver.cc:404] creating context when one is currently active; existing: 0x555b47134ba0
2018-09-15 12:41:27.379650: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1451] Found device 0 with properties: 
name: Ellesmere [Radeon RX 470/480]
AMDGPU ISA: gfx803
memoryClockRate (GHz) 1.34
pciBusID 0000:42:00.0
Total memory: 8.00GiB
Free memory: 7.75GiB
2018-09-15 12:41:27.379663: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1562] Adding visible gpu devices: 0
2018-09-15 12:41:27.379684: I tensorflow/core/common_runtime/gpu/gpu_device.cc:989] Device interconnect StreamExecutor with strength 1 edge matrix:
2018-09-15 12:41:27.379692: I tensorflow/core/common_runtime/gpu/gpu_device.cc:995]      0 
2018-09-15 12:41:27.379699: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1008] 0:   N 
2018-09-15 12:41:27.379726: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1124] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7539 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480], pci bus id: 0000:42:00.0)
clang (LLVM option parsing): Unknown command line argument '-enable-si-insert-waitcnts'.  Try: 'clang (LLVM option parsing) -help'
clang (LLVM option parsing): Did you mean '-enable-post-misched'?
MIOpen Error: /data/repo/MIOpen/src/tmp_dir.cpp:18: Can't execute cd /tmp/miopen-MIOpenUtilKernels.cl-6a7e-dd91-177f-7c59; /opt/rocm/bin/clang-ocl  -DNUM_CH_PER_WG=1 -DNUM_IM_BLKS_X=1 -DNUM_IM_BLKS=3 -DLOCAL_MEM_SIZE=432 -DSTRIDE_GT_1=0 -DTILE_SZ_X=32 -DTILE_SZ_Y=8 -DUSE_IM_OFF_GUARD=1 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -mcpu=gfx803 -Wno-everything MIOpenUtilKernels.cl -o /tmp/miopen-MIOpenUtilKernels.cl-6a7e-dd91-177f-7c59/MIOpenUtilKernels.cl.o
2018-09-15 12:41:30.804919: F tensorflow/stream_executor/rocm/rocm_dnn.cc:1803] Check failed: status == miopenStatusSuccess (7 vs. 0)Unable to find a suitable algorithm for doing forward convolution
Aborted (core dumped)
```
```
witold@witold-r7:~$ uname -a
Linux witold-r7 4.15.0-34-generic #37-Ubuntu SMP Mon Aug 27 15:21:48 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
```
apt list --installed | grep -i roc

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

amd64-microcode/bionic-updates,now 3.20180524.1~ubuntu0.18.04.2 amd64 [installed,automatic]
hsa-ext-rocr-dev/Ubuntu 16.04,now 1.1.9-8-g51c00c2 amd64 [installed]
hsa-rocr-dev/Ubuntu 16.04,now 1.1.9-8-g51c00c2 amd64 [installed]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-8-g238782c amd64 [installed,automatic]
hsakmt-roct-dev/Ubuntu 16.04,now 1.0.9-8-g238782c amd64 [installed]
intel-microcode/bionic-updates,bionic-security,now 3.20180807a.0ubuntu0.18.04.1 amd64 [installed,automatic]
libcroco3/bionic,now 0.6.12-2 amd64 [installed]
libpostproc54/bionic-updates,bionic-security,now 7:3.4.4-0ubuntu0.18.04.1 amd64 [installed,automatic]
libprocps6/bionic-updates,bionic-security,now 2:3.3.12-3ubuntu1.1 amd64 [installed,automatic]
libwebrtc-audio-processing1/bionic,now 0.3-1 amd64 [installed,automatic]
procps/bionic-updates,bionic-security,now 2:3.3.12-3ubuntu1.1 amd64 [installed]
python3-ptyprocess/bionic,bionic,now 0.5.2-1 all [installed]
rocblas/Ubuntu 16.04,now 0.14.2.4 amd64 [installed,automatic]
rocfft/Ubuntu 16.04,now 0.8.6.0 amd64 [installed,automatic]
rock-dkms/Ubuntu 16.04,now 1.9-211 all [installed,automatic]
rocm-clang-ocl/now 0.3.0-c1b678e amd64 [installed,local]
rocm-dev/Ubuntu 16.04,now 1.9.211 amd64 [installed]
rocm-device-libs/Ubuntu 16.04,now 0.0.1 amd64 [installed]
rocm-dkms/Ubuntu 16.04,now 1.9.211 amd64 [installed]
rocm-libs/Ubuntu 16.04,now 1.9.211 amd64 [installed]
rocm-opencl/Ubuntu 16.04,now 1.2.0-2018090737 amd64 [installed]
rocm-opencl-dev/Ubuntu 16.04,now 1.2.0-2018090737 amd64 [installed]
rocm-profiler/Ubuntu 16.04,now 5.4.6878 amd64 [installed]
rocm-smi/Ubuntu 16.04,now 1.0.0-72-gec1da05 amd64 [installed,automatic]
rocm-utils/Ubuntu 16.04,now 1.9.211 amd64 [installed]
rocminfo/Ubuntu 16.04,now 1.0.0 amd64 [installed,automatic]
rocr_debug_agent/Ubuntu 16.04,now 1.0.0 amd64 [installed,automatic]
rocrand/Ubuntu 16.04,now 1.8.1 amd64 [installed,automatic]
```

---

## 评论 (7 条)

### 评论 #1 — dagamayank (2018-09-16T02:51:19Z)

@sunway513 

---

### 评论 #2 — dagamayank (2018-09-16T02:52:17Z)

/cc @jlgreathouse to confirm if this GPU is supported. `name: Ellesmere [Radeon RX 470/480]`

---

### 评论 #3 — jlgreathouse (2018-09-16T02:53:19Z)

Ellesmere is Polaris 10, so it's on our support list.

---

### 评论 #4 — sunway513 (2018-09-16T02:58:24Z)

@witeko The ROCm1.9.0 compatible TF1.8 whl file has not been refreshed yet, it should be ready soon.
CC @parallelo  

In the meanwhile, you can use our published docker images to run TF on ROCm1.9:
https://hub.docker.com/r/rocm/tensorflow/tags/

---

### 评论 #5 — sunway513 (2018-09-16T03:11:01Z)

@witeko I've just confirmed the `cifar10_train.py` can work correctly inside the `rocm/tensorflow:rocm1.9.0-tf1.8-python3`, some logs below:
```
/root/models/tutorials/image/cifar10# python3 ./cifar10_train.py                                            
>> Downloading cifar-10-binary.tar.gz 100.0%
Successfully downloaded cifar-10-binary.tar.gz 170052171 bytes.
Filling queue with 20000 CIFAR images before starting to train. This will take a few minutes.
2018-09-16 03:08:01.964458: W tensorflow/stream_executor/rocm/rocm_driver.cc:404] creating context when one is currently acti
ve; existing: 0x7fb8537a1860
2018-09-16 03:08:01.964646: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1451] Found device 0 with properties: 
name: Device 6860
AMDGPU ISA: gfx900
memoryClockRate (GHz) 1.5
pciBusID 0000:07:00.0
Total memory: 15.98GiB
Free memory: 15.73GiB
2018-09-16 03:08:01.964677: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1562] Adding visible gpu devices: 0
2018-09-16 03:08:01.964712: I tensorflow/core/common_runtime/gpu/gpu_device.cc:989] Device interconnect StreamExecutor with s
trength 1 edge matrix:
2018-09-16 03:08:01.964729: I tensorflow/core/common_runtime/gpu/gpu_device.cc:995]      0 
2018-09-16 03:08:01.964743: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1008] 0:   N 
2018-09-16 03:08:01.964786: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1124] Created TensorFlow device (/job:localhos
t/replica:0/task:0/device:GPU:0 with 15306 MB memory) -> physical GPU (device: 0, name: Device 6860, pci bus id: 0000:07:00.0
)
2018-09-16 03:08:25.113552: I tensorflow/core/kernels/conv_grad_input_ops.cc:1007] running auto-tune for Backward-Data
2018-09-16 03:08:28.086031: I tensorflow/core/kernels/conv_grad_filter_ops.cc:959] running auto-tune for Backward-Filter
2018-09-16 03:08:31.626393: I tensorflow/core/kernels/conv_grad_filter_ops.cc:959] running auto-tune for Backward-Filter
2018-09-16 03:08:34.939534: step 0, loss = 4.67 (38.7 examples/sec; 3.309 sec/batch)
2018-09-16 03:08:35.314975: step 10, loss = 4.62 (3408.5 examples/sec; 0.038 sec/batch)
2018-09-16 03:08:35.560467: step 20, loss = 4.55 (5214.1 examples/sec; 0.025 sec/batch)
2018-09-16 03:08:35.688392: step 30, loss = 4.42 (10005.6 examples/sec; 0.013 sec/batch)
2018-09-16 03:08:35.928513: step 40, loss = 4.40 (5330.6 examples/sec; 0.024 sec/batch)
2018-09-16 03:08:36.152942: step 50, loss = 4.37 (5703.5 examples/sec; 0.022 sec/batch)
2018-09-16 03:08:36.275191: step 60, loss = 4.41 (10469.9 examples/sec; 0.012 sec/batch)
2018-09-16 03:08:36.502439: step 70, loss = 4.22 (5632.7 examples/sec; 0.023 sec/batch)
2018-09-16 03:08:36.618470: step 80, loss = 4.10 (11031.0 examples/sec; 0.012 sec/batch)
2018-09-16 03:08:36.853146: step 90, loss = 4.13 (5454.4 examples/sec; 0.023 sec/batch)
```

---

### 评论 #6 — witeko (2018-09-16T10:32:35Z)

Thank You all :)
The problem started when I used "ubuntu system update" to update the rocm.
The problem ended when I just reinstalled all. 

This guy here seems to have a similar problem (or maybe not): https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/142

On the side: my gfx803 with clock 1.34 and 8GB seems to be faster than Your gfx900 :)
2018-09-16 12:30:55.558282: step 600, loss = 3.06 (4891.1 examples/sec; 0.026 sec/batch)
2018-09-16 12:30:55.715084: step 610, loss = 3.10 (8163.2 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:55.871621: step 620, loss = 3.01 (8176.9 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.028245: step 630, loss = 3.19 (8172.4 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.184747: step 640, loss = 3.02 (8178.8 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.340392: step 650, loss = 2.82 (8223.8 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.506263: step 660, loss = 2.86 (7716.8 examples/sec; 0.017 sec/batch)
2018-09-16 12:30:56.662123: step 670, loss = 2.73 (8212.5 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.818286: step 680, loss = 2.81 (8196.6 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:56.974245: step 690, loss = 2.76 (8207.3 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:57.234423: step 700, loss = 2.76 (4919.7 examples/sec; 0.026 sec/batch)
2018-09-16 12:30:57.390278: step 710, loss = 2.76 (8212.8 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:57.546052: step 720, loss = 2.79 (8217.0 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:57.701955: step 730, loss = 2.67 (8210.3 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:57.857821: step 740, loss = 2.66 (8212.2 examples/sec; 0.016 sec/batch)
2018-09-16 12:30:58.013449: step 750, loss = 2.72 (8224.8 examples/sec; 0.016 sec/batch)

---

### 评论 #7 — sunway513 (2018-09-16T17:26:44Z)

@witeko , thanks for confirming the issue is resolved on your end, I'll close the ticket.
Besides, please find the logs on my gfx900 card at step 600:
`2018-09-16 17:17:33.927281: step 600, loss = 2.92 (5021.8 examples/sec; 0.025 sec/batch)
2018-09-16 17:17:34.026046: step 610, loss = 3.13 (12958.5 examples/sec; 0.010 sec/batch)
2018-09-16 17:17:34.117120: step 620, loss = 2.94 (14053.7 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.207950: step 630, loss = 2.93 (14092.2 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.311038: step 640, loss = 3.24 (12416.7 examples/sec; 0.010 sec/batch)
2018-09-16 17:17:34.402318: step 650, loss = 2.95 (14022.6 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.493105: step 660, loss = 2.79 (14098.9 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.581978: step 670, loss = 2.94 (14402.6 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.677013: step 680, loss = 2.85 (13468.7 examples/sec; 0.010 sec/batch)
2018-09-16 17:17:34.766933: step 690, loss = 2.74 (14234.9 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:34.989854: step 700, loss = 2.74 (5741.9 examples/sec; 0.022 sec/batch)
2018-09-16 17:17:35.085954: step 710, loss = 2.68 (13320.0 examples/sec; 0.010 sec/batch)
2018-09-16 17:17:35.176742: step 720, loss = 2.67 (14098.3 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:35.267900: step 730, loss = 2.88 (14041.5 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:35.360048: step 740, loss = 2.92 (13890.7 examples/sec; 0.009 sec/batch)
2018-09-16 17:17:35.459550: step 750, loss = 2.73 (12864.2 examples/sec; 0.010 sec/batch)`


---
