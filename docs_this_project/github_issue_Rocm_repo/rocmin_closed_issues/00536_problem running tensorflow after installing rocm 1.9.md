# problem running tensorflow after installing rocm 1.9

- **Issue #:** 536
- **State:** closed
- **Created:** 2018-09-15T10:57:32Z
- **Updated:** 2018-09-16T17:26:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/536

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