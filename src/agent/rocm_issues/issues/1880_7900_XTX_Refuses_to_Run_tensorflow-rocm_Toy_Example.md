# 7900 XTX Refuses to Run tensorflow-rocm Toy Example

> **Issue #1880**
> **状态**: closed
> **创建时间**: 2022-12-24T10:58:17Z
> **更新时间**: 2024-08-22T15:35:15Z
> **关闭时间**: 2024-08-22T15:35:14Z
> **作者**: Mushoz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1880

## 描述

### Issue Type

Bug

### Tensorflow Version

Tensorflow-rocm v2.11.0-3797-gfe65ef3bbcf 2.11.0

### rocm Version

5.4.1

### Custom Code

Yes

### OS Platform and Distribution

Archlinux: Kernel 6.1.1

### Python version

3.10

### GPU model and memory

7900 XTX 24GB

### Current Behaviour?

I am not entirely sure whether this is an upstream (ROCM) issue, or with Tensorflow-rocm specifically, so I am reporting it to both repo's. A toy example refuses to run and dumps core. I would have expected it to train successfully.


### Standalone code to reproduce the issue

```
import tensorflow as tf
import numpy as np

features = np.random.randn(10000,25)
targets = np.random.randn(10000)

model = tf.keras.Sequential([
     tf.keras.layers.Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.MeanSquaredError())

model.fit(x=features, y=targets)
```


### Relevant log output

```
[jaap@Jaap-Desktop code]$ pipenv run python testNN.py
2022-12-24 11:18:37.178811: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
python: /build/hsa-rocr/src/ROCR-Runtime-rocm-5.4.1/src/core/runtime/amd_gpu_agent.cpp:339: void rocr::AMD::GpuAgent::AssembleShader(const char*, AssembleTarget, void*&, size_t&) const: Assertion `code_buf != NULL && "Code buffer allocation failed"' failed.
```


---

## 评论 (100 条)

### 评论 #1 — sofiageo (2022-12-24T11:27:00Z)

It's probably a packaging issue for Arch, try with `opencl-amd` and `opencl-amd-dev` from AUR and see if it makes a difference.

p.s damn that GPU must be a beast 💯 

---

### 评论 #2 — Mushoz (2022-12-24T12:03:54Z)

Unfortunately that doesn't seem to work. First it tries to remove the conflicting packages:

```
:: opencl-amd and rocm-opencl-runtime are in conflict. Remove rocm-opencl-runtime? [y/N] y
:: opencl-amd and hip-runtime-amd are in conflict (hip). Remove hip-runtime-amd? [y/N] y
```

However, answering Y to both question still results in a failure to install:

```
error: failed to commit transaction (conflicting files)
opencl-amd: /opt/rocm exists in filesystem
Errors occurred, no packages were upgraded.
 -> exit status 1
```

Are you sure these packages are even required though? From what I understand, tensorflow-rocm does NOT use opencl at all. As a matter of fact, I upgraded from a 6900XT which was able to run tensorflow-rocm with the exact same packages I have currently installed just fine.

---

### 评论 #3 — sofiageo (2022-12-24T12:34:08Z)

The package name is just that for historical reasons, nothing to do with OpenCL. The reason you get these conflicts errors is because it's not properly handling the conflicts. It's something I will try to fix soon but it's not there yet. So you have to manually remove any rocm-arch package yourself if you want to try `opencl-amd`.

p.s I don't want to spam the rocm issue tracker with arch packaging comments, so if you are still interested to try it feel free to comment on the AUR page and we can continue the discussion there.

---

### 评论 #4 — Mushoz (2022-12-24T14:23:16Z)

I just uninstalled all previous `rocm` packages and went with the `opencl-amd` + `opencl-amd-dev`, but that's just making the example run on the CPU rather than the GPU. So unfortunately it does not fix the issue at hand. Any ideas? :)

---

### 评论 #5 — sofiageo (2022-12-24T15:44:44Z)

I guess it's because your GPU is not supported yet in ROCm. I ran your example with my 5700 XT and it's working fine (although it didn't complete in 10 minutes and I had to cancel it). Maybe you can try to `HSA_OVERRIDE_GFX_VERSION=10.3.0 python sample.py` or something similar.

---

### 评论 #6 — Mushoz (2022-12-25T19:51:06Z)

That just makes it crash with an out of memory error, which is bogus for such a small example with 24GB memory:

```
[jaap@Jaap-Desktop code]$ HSA_OVERRIDE_GFX_VERSION=10.3.0 pipenv run python testNN.py
2022-12-25 20:49:47.446031: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-25 20:49:48.428818: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.466946: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.466999: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.467209: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-25 20:49:48.468937: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469011: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469044: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469138: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469176: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469209: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-25 20:49:48.469229: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1613] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 24060 MB memory:  -> device: 0, name: AMD Radeon Graphics, pci bus id: 0000:2d:00.0
2022-12-25 20:49:48.492206: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:573] could not allocate ROCM stream for device 0: HIP_ERROR_OutOfMemory
2022-12-25 20:49:48.492218: I tensorflow/compiler/xla/stream_executor/stream_executor_pimpl.cc:791] failed to allocate stream; live stream count: 1
2022-12-25 20:49:48.492221: E tensorflow/compiler/xla/stream_executor/stream.cc:297] failed to allocate stream during initialization
2022-12-25 20:49:48.512792: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:573] could not allocate ROCM stream for device 0: HIP_ERROR_OutOfMemory
2022-12-25 20:49:48.512801: I tensorflow/compiler/xla/stream_executor/stream_executor_pimpl.cc:791] failed to allocate stream; live stream count: 1
2022-12-25 20:49:48.512804: E tensorflow/compiler/xla/stream_executor/stream.cc:297] failed to allocate stream during initialization
2022-12-25 20:49:48.512811: I tensorflow/compiler/xla/stream_executor/stream.cc:1038] [stream=0x55edc5775fb0,impl=0x55edc5775770] did not wait for [stream=0x55edc5794720,impl=0x55edc5775e20]
2022-12-25 20:49:48.512815: I tensorflow/compiler/xla/stream_executor/stream.cc:1038] [stream=0x55edc5794720,impl=0x55edc5775e20] did not wait for [stream=0x55edc5775fb0,impl=0x55edc5775770]
2022-12-25 20:49:48.533248: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:573] could not allocate ROCM stream for device 0: HIP_ERROR_OutOfMemory
2022-12-25 20:49:48.533265: I tensorflow/compiler/xla/stream_executor/stream_executor_pimpl.cc:791] failed to allocate stream; live stream count: 1
2022-12-25 20:49:48.533270: E tensorflow/compiler/xla/stream_executor/stream.cc:297] failed to allocate stream during initialization
2022-12-25 20:49:48.553530: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:573] could not allocate ROCM stream for device 0: HIP_ERROR_OutOfMemory
2022-12-25 20:49:48.553539: I tensorflow/compiler/xla/stream_executor/stream_executor_pimpl.cc:791] failed to allocate stream; live stream count: 1
2022-12-25 20:49:48.553543: E tensorflow/compiler/xla/stream_executor/stream.cc:297] failed to allocate stream during initialization
2022-12-25 20:49:48.573939: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:573] could not allocate ROCM stream for device 0: HIP_ERROR_OutOfMemory
2022-12-25 20:49:48.573949: I tensorflow/compiler/xla/stream_executor/stream_executor_pimpl.cc:791] failed to allocate stream; live stream count: 1
2022-12-25 20:49:48.573953: E tensorflow/compiler/xla/stream_executor/stream.cc:297] failed to allocate stream during initialization
2022-12-25 20:49:48.582885: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-25 20:49:48.668485: I tensorflow/compiler/xla/stream_executor/stream.cc:1038] [stream=0x55edc57947d0,impl=0x55edc5794920] did not wait for [stream=0x55edc5775fb0,impl=0x55edc5775770]
```

---

### 评论 #7 — Syntax3rror404 (2022-12-29T16:00:51Z)

7900xtx with rocm would be awsome!!!! @Mushoz do you get it working now? I have the same usecase

---

### 评论 #8 — jannesklee (2022-12-29T16:21:38Z)

The problem also occurs with 7900xt. Also with arch linux rocm packages from aur. Is there anything that can be done in order to make it run? 

Edit: I reproduced the same output with the samples/0_Intro/bit_extract in https://github.com/ROCm-Developer-Tools/HIP.git as an easier minimal example.

---

### 评论 #9 — Syntax3rror404 (2022-12-29T16:23:05Z)

So this means this problem are only exits on arch linux? And not on ubuntu or debian?

---

### 评论 #10 — jannesklee (2022-12-29T16:52:48Z)

Installing opencl-amd and opencl-amd-dev seems to work for me.

 @Mushoz Did you install llvm with version >= 15 (arch still has 14)

You can also have a look at:
https://www.phoronix.com/review/rx7900xt-rx7900xtx-linux
https://www.reddit.com/r/linux_gaming/comments/zk0462/amd_radeon_rx_7900_xtx_rx_7900_xt_linux_support/

There it states what is needed:
- llvm >= 15 
- new mesa version compiled against llvm >= 15
- the firmware needed to be added manually, but I think it is now already included (at least in arch)


---

### 评论 #11 — Mushoz (2022-12-29T17:36:49Z)

@jannesklee I am running llvm-minimal-git. Everything is working as it should game-wise. It's just that rocm is broken. Are you able to run the example in my first post just fine? And you are certain it's running on the GPU and not the CPU? Could you run the following python script and show the output?

```
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

---

### 评论 #12 — jannesklee (2022-12-29T17:47:30Z)

I got the same error when testing the minimal example shown above, and other samples and it vanished when I used the other packages. When I check the usage with nvtop it shows me that the dedicated graphic card is in use. 

Maybe the llvm-minimal-git version is not enough. At https://aur.archlinux.org/pkgbase/llvm-git Lone_Wolf states that llvm-minimal-git *focuses on providing stuff needed for AUR mesa-git. Doesn't support cross-compiling or any bindings for external stuff like ocaml & python*.

Unfortunately I am currently not capable to install tensorflow, because I get compilation errors, but this is something else I guess. I try to make it run but without success.

---

### 评论 #13 — Mushoz (2022-12-29T17:53:29Z)

@jannesklee no need to compile tensorflow. You can install `tensorflow-rocm` via pip or pipenv if you want to keep it contained within its own virtual environment. Would you mind running my previously mentioned script?

---

### 评论 #14 — jannesklee (2022-12-29T18:22:50Z)

My output is. I do not completely understand it to be honest.. 

```
python samply.py 
2022-12-29 19:22:12.450100: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F AVX512_VNNI AVX512_BF16 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-29 19:22:12.510354: I tensorflow/core/util/port.cc:104] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2022-12-29 19:22:13.488612: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.488649: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.521375: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.521408: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.521421: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.521438: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1990] Ignoring visible gpu device (device: 0, name: AMD Radeon Graphics, pci bus id: 0000:16:00.0) with AMDGPU version : gfx1100. The supported AMDGPU versions are gfx1030, gfx900, gfx906, gfx908, gfx90a.
2022-12-29 19:22:13.521448: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-29 19:22:13.521454: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1990] Ignoring visible gpu device (device: 1, name: AMD Radeon Graphics, pci bus id: 0000:38:00.0) with AMDGPU version : gfx1036. The supported AMDGPU versions are gfx1030, gfx900, gfx906, gfx908, gfx90a.
2022-12-29 19:22:13.521638: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F AVX512_VNNI AVX512_BF16 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-29 19:22:13.531205: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.531933: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.532580: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.534466: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.534728: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.535002: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.537283: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.538129: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.540706: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.541347: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.546382: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.546865: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.551241: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.551819: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.552166: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.552624: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.555412: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.555920: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.556342: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.556773: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.557366: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.558349: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.558775: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.559037: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.562307: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.565317: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.567121: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.579977: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.580617: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.581283: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.581875: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.583109: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.583446: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.583800: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.584342: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.584655: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.683227: E tensorflow/core/framework/node_def_util.cc:675] NodeDef mentions attribute grad_a which is not in the op definition: Op<name=_MklMatMul; signature=a:T, b:T -> product:T; attr=transpose_a:bool,default=false; attr=transpose_b:bool,default=false; attr=T:type,allowed=[DT_BFLOAT16, DT_FLOAT]> This may be expected if your graph generating binary is newer  than this binary. Unknown attributes will be ignored. NodeDef: {{node gradient_tape/sequential/dense/MatMul/MatMul}}
2022-12-29 19:22:13.684957: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
190/313 [=================>............] - ETA: 0s - loss: 2.4990 2022-12-29 19:22:13.768593: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.768931: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-12-29 19:22:13.769222: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
313/313 [==============================] - 0s 257us/step - loss: 2.1766
```

---

### 评论 #15 — saadrahim (2022-12-29T18:24:39Z)

Support for this GPU is not enabled on ROCm 5.4.1. Please await the 5.5.0 release announcement to check for support.

---

### 评论 #16 — Syntax3rror404 (2022-12-29T18:34:38Z)

When we can expect a release of 5.5.0 are there any date scheduled?  

---

### 评论 #17 — Mushoz (2022-12-29T20:10:26Z)

@jannesklee I have the same output. Unfortunately it specifically states that it is ignoring the GPU because it is unsupported.

@saadrahim when can we expect 5.5.0 to release? CUDA is so much easier in this regard. It just works. In order for ROCM to be able to compete with CUDA it really has to step up in terms of communication so that users can rely on ROCM as they can on CUDA

---

### 评论 #18 — cgmb (2023-01-03T22:41:55Z)

I'm a bit surprised that you're having trouble with ROCm 5.4.1 on the 7900 XTX, as that architecture is gfx1100 and most of the AMD-provided binaries for ROCm 5.4.1 contain gfx1100 code objects. It's not listed as officially supported in [the GPU support table for ROCm 5.4](https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4/page/About_This_Document.html#d2e131), but I would have expected it would mostly work anyway. Is this problem specific to Tensorflow? e.g., do other libraries packaged by Arch work? A quick check might be to build and run Arch's [`test.cpp` for rocrand](https://github.com/rocm-arch/rocm-arch/tree/79fc2a8a4a37dee67c9ff17d4dae5015f0827a00/rocrand).

> I guess it's because your GPU is not supported yet in ROCm. I ran your example with my 5700 XT and it's working fine (although it didn't complete in 10 minutes and I had to cancel it). Maybe you can try to `HSA_OVERRIDE_GFX_VERSION=10.3.0 python sample.py` or something similar.

When you set `HSA_OVERRIDE_GFX_VERSION=10.3.0`, you're telling libhsakmt to pretend that your GPU is Navi 21 (gfx1030). To my knowledge, that works just fine for all the RDNA 2 GPUs, since they all use the same instruction set.

The RDNA 1 instruction sets are similar enough to the RDNA 2 instruction set that sometimes you can successfully run code that was compiled for RDNA 2 on an RDNA 1 GPU (as you are doing with your 5700 XT), however, this is not guaranteed to work. The instruction sets are not identical and if the code you're running happens to use an RDNA 2 instruction that worked differently in RDNA 1 (or doesn't exist at all in RDNA 1), then your program may not function correctly.

Similarly, the RDNA 3 instruction sets are different from the RDNA 2 instruction set. If you try to run code compiled for RDNA 2 on an RDNA 3 GPU using `HSA_OVERRIDE_GFX_VERSION`, the result may not work correctly.

---

### 评论 #19 — jannesklee (2023-01-04T11:25:04Z)

My assumption is also that it is a problem from tensorflow side. I tested above the samples from https://github.com/ROCm-Developer-Tools/HIP

Example [bit_extract](https://github.com/ROCm-Developer-Tools/HIP/tree/develop/samples/0_Intro/bit_extract):
```
    make
    ./bit_extract
```

gives me

```
    info: running on device #0 AMD Radeon Graphics
    info: allocate host mem (  7.63 MB)
    info: allocate device mem (  7.63 MB)
    info: copy Host2Device
    info: launch 'bit_extract_kernel' 
    info: copy Device2Host
    info: check result
    PASSED!
```
I can also see some activity with nvtop, but unfortunately I do not know exactly how to give more details here.

Regarding your example I unfortunately get a core dump, when running ./test.sh:

```
In file included from test.cpp:1:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand.hpp:35:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand_kernel.h:54:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand_kernel_hcc.h:37:
In file included from /opt/rocm-5.4.1/include/rocrand/rocrand_kernel.h:28:
/opt/rocm-5.4.1/include/rocrand/rocrand_common.h:74:6: warning: "Disabled inline asm, because the build target does not support it." [-W#warnings]
    #warning "Disabled inline asm, because the build target does not support it."
     ^
1 warning generated when compiling for gfx1036.
In file included from test.cpp:1:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand.hpp:35:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand_kernel.h:54:
In file included from /opt/rocm-5.4.1/include/hiprand/hiprand_kernel_hcc.h:37:
In file included from /opt/rocm-5.4.1/include/rocrand/rocrand_kernel.h:28:
/opt/rocm-5.4.1/include/rocrand/rocrand_common.h:74:6: warning: "Disabled inline asm, because the build target does not support it." [-W#warnings]
    #warning "Disabled inline asm, because the build target does not support it."
     ^
1 warning generated when compiling for gfx1100.
./test.sh: line 5:  7225 Segmentation fault      (core dumped) "$OUT"/test

```


---

### 评论 #20 — Mushoz (2023-01-04T11:33:03Z)

@jannesklee I am not so sure. @saadrahim Specifically stated that ROCM 5.5.0 is required for these cards to run tensorflow. I am also not surprised you are able to run that HIP example. There is some preliminary support for the 7900 series, given that Blender can also use the HIP backend just fine: https://www.phoronix.com/review/rx7900-blender-opencl

That has me thinking though. It would be interesting to see if pytorch-rocm is able to run. I can see that there are docker images available, and some tags are using rocm 5.4.1. That would take packaging issues AND tensorflow out of the equation, and would allow us to see if these cards are able to do any machine learning with the current rocm stack. I might try this out tonight.

Docker images in case you want to give it a shot: https://hub.docker.com/r/rocm/pytorch/tags

---

### 评论 #21 — AndersStendevad (2023-01-09T17:25:14Z)

@jannesklee did it work ?

---

### 评论 #22 — wsippel (2023-01-11T12:54:26Z)

@Mushoz pytorch-rocm doesn't appear to work, either. Can't find the GPU at all by default and segfaults with HSA_OVERRIDE_GFX_VERSION set.

---

### 评论 #23 — Mushoz (2023-01-19T15:53:10Z)

@wsippel Ah, I just replied to you on the AUR but only just now realized you are active here as well. A week ago changes for RDNA3 were merged for MIOpen: https://github.com/ROCmSoftwarePlatform/MIOpen/commits/develop

See the 11th of January. Do you reckon we could get it to work by compiling MIOpen from source?

---

### 评论 #24 — Kardi5 (2023-01-23T01:57:58Z)

@wsippel @Mushoz I can confirm that with some effort a build of pytorch 1.13.1 against AMD RX 7900 XTX with ROCm 5.4.2 works and is functional for my use case of running models. 

Rough outline for build is the usage of an Ubuntu (20.04/22.04) Docker image as AMD provides ROCm repos for it and installing all required deps without kernel module. See https://github.com/ROCmSoftwarePlatform/MIOpen/blob/develop/Dockerfile#L67 basically edit 5.3 to 5.4.2 and run all commands till line 67. I also adapted the amdgpu install command to `amdgpu-install -y --usecase=graphics,rocm,lrt,hip,hiplibsdk --no-dkms` as some libs were missing for the torch build.

Maybe you can build tensorflow via instructions from https://www.tensorflow.org/install/source and adapting the build command to (in venv):
TF_NEED_ROCM=1 python configure.py 


---

### 评论 #25 — Mushoz (2023-01-23T07:56:13Z)

@Kardi5 Would you mind sharing the final dockerfile that you used? I would love to try and replicate that for Tensorflow. Please leave in all the pytorch specific things as well. I will try to do something similar for Tensorflow.

---

### 评论 #26 — Kardi5 (2023-01-23T13:47:20Z)

@Mushoz Sure, but I don't have a complete one myself right now. It was more of an interactive trial and error until all builds worked out. I hope to create a complete dockerfile tonight/tomorrow based on the notes I took. 

---

### 评论 #27 — aaronmondal (2023-01-24T15:56:31Z)

This issue also affects Gentoo when installing ROCm via portage. Installing `dev-libs/rocm-opencl-runtime`, which currently defaults to the older 5.3.3 will cause `clinfo` to raise the OPs error:

```cpp
clinfo: /var/tmp/portage/dev-libs/rocr-runtime-5.3.3/work/ROCR-Runtime-rocm-5.3.3/src/core/runtime/amd_gpu_agent.cpp:339: void rocr::AMD::GpuAgent::AssembleShader(const char 
*, rocr::AMD::GpuAgent::AssembleTarget, void *&, size_t &) const: Assertion `code_buf != NULL && "Code buffer allocation failed"' failed.
Aborted (core dumped)
```

Im rather certain that this particular error is not related to TensorFlow or MIOpen, as I was able to repro the error above with only a basic installation of the Rocm OpenCL runtime and friends.

The changes from ROCR 5.4.1 to 5.4.2 have not been downstreamed to GitHub yet, making it tricky to reproduce the workaround @Kardi5 proposed for other distros. I guess I'll try with 5.4.1 for now.

---

### 评论 #28 — Kardi5 (2023-01-25T00:20:55Z)

@Mushoz So far I could only create a rough draft of a complete Dockerfile. Maybe you will find it useful nonetheless. 
Current main problem is that my compilation of Magma shows a lot of error'd calls to ROCm as during `docker build` I can not attach any device like I can during `docker build`. 

Over at https://github.com/pytorch/pytorch/blob/master/.circleci/docker/ubuntu-rocm/Dockerfile there is a more complete example even though much more complex. Their Magma build script (https://github.com/pytorch/pytorch/blob/master/.circleci/docker/common/install_rocm_magma.sh) might be the solution to my troubles but I did not have time to look through it in more detail.

There might still be errors besides Magma building after line `WORKDIR /build/magma/build` 

Draft Torch + Torchvision Dockerfile
```
FROM ubuntu:22.04

### START SECTION AMD ROCm install
# based on https://github.com/ROCmSoftwarePlatform/MIOpen/blob/develop/Dockerfile
ARG DEBIAN_FRONTEND=noninteractive
ARG USE_MLIR="OFF"

# Support multiarch
RUN dpkg --add-architecture i386

# Install preliminary dependencies
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated \
    apt-utils \
    ca-certificates \
    curl \
    libnuma-dev \
    gnupg2 \
    wget

#Add gpg keys
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 9386B48A1A693C5C && \
    wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | apt-key add -

# Check the AMD repo for exact package name
RUN wget https://repo.radeon.com/amdgpu-install/5.4.2/ubuntu/jammy/amdgpu-install_5.4.50402-1_all.deb --no-check-certificate
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated \
    ./amdgpu-install_5.4.50402-1_all.deb

# Add rocm repository
# Note: The ROCm version with $USE_MLIR should keep in sync with default ROCm version
# unless MLIR library is incompatible with current ROCm.
RUN export ROCM_APT_VER=5.4.2;\
echo $ROCM_APT_VER &&\
sh -c 'echo deb [arch=amd64 trusted=yes] http://repo.radeon.com/rocm/apt/$ROCM_APT_VER/ ubuntu main > /etc/apt/sources.list.d/rocm.list'
RUN sh -c "echo deb http://mirrors.kernel.org/ubuntu jammy main universe | tee -a /etc/apt/sources.list"

RUN amdgpu-install -y --usecase=rocm,graphics,rocmdev,rocmdevtools,lrt,hip,hiplibsdk,mllib,mlsdk --no-dkms

# Install dependencies
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated \
    build-essential \
    cmake \
    clang-format-12 \
    doxygen \
    gdb \
    git \
    lcov \
    libncurses5-dev \
    llvm-amdgpu \
    miopengemm \
    pkg-config \
    python3-dev \
    python3-pip \
    python3-venv \
    rocblas \
    rpm \
    software-properties-common

# Setup ubsan environment to printstacktrace
ENV UBSAN_OPTIONS=print_stacktrace=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

### START SECTION install Magma (torch dep) and PyTorch deps
# For Magma
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated \
    libmkl-core libmkl-def libmkl-dev libmkl-full-dev libmkl-intel-thread libmkl-gnu-thread gfortran

# For PyTorch
RUN apt-get update && \ 
DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends --allow-unauthenticated \
    build-essential ca-certificates ccache cmake curl git libjpeg-dev libpng-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

### START SECTION Magma and Torch build
RUN useradd -m -G video -U --shell /bin/bash roc && \
    mkdir /build && \
    chown roc:roc /build
USER roc
WORKDIR /build

# Download latest Magma version: http://icl.utk.edu/projectsfiles/magma/downloads/
# Install steps found here: https://salsa.debian.org/science-team/magma/-/tree/master/
RUN wget -qnc "https://icl.utk.edu/projectsfiles/magma/downloads/magma-2.7.0.tar.gz" -O "magma.tar.gz" && \
    tar -xzf magma.tar.gz && \
    rm magma.tar.gz && \
    mv magma* magma && \
    mkdir magma/build

WORKDIR /build/magma/build

# ERRORS START HERE, RUN THE REST OF THIS INTERACTIVELY

# You may want to adopt gfx1100 to something else: https://llvm.org/docs/AMDGPUUsage.html#processors search gfx11
RUN cmake -DMAGMA_ENABLE_HIP=ON -DCMAKE_CXX_COMPILER=hipcc -DGPU_TARGET='gfx1100' .. && \
    make -j $(nproc)

USER root
RUN make install
USER roc
WORKDIR /build
CMD git clone -j 4 --recursive https://github.com/pytorch/pytorch --depth 1 --branch v1.13.1

# Build of Torch based on: https://github.com/pytorch/pytorch/blob/master/Dockerfile
# Miniconda is experimental here, maybe use Anaconda if run interactively
RUN curl -fsSL -v -o ~/miniconda.sh -O  "https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-x86_64.sh" && \
    RUN chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda install -y python=3.9 cmake conda-build pyyaml numpy ipython && \
    /opt/conda/bin/python -mpip install -r /build/pytorch/requirements.txt && \
    /opt/conda/bin/conda install -y ninja cffi dataclasses && \
    /opt/conda/bin/conda install -y mkl mkl-include && \
    /opt/conda/bin/conda clean -ya

WORKDIR /build/pytorch
RUN python tools/amd_build/build_amd.py

RUN --mount=type=cache,target=/opt/ccache \
    export CMAKE_PREFIX_PATH="$(dirname $(which conda))/../",/usr/local/magma/ \
    PYTORCH_ROCM_ARCH=gfx1100 USE_MAGMA=1 USE_ROCM=1 USE_NVCC=0 USE_CUDA=0 python setup.py install

# Test build of Torch
# Should print: True Radeon RX 7900 XTX
RUN python3 -c 'import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(torch.cuda.current_device()))'

# Torchvision build
WORKDIR /build
RUN git clone --recursive https://github.com/pytorch/vision --depth 1 --branch v0.14.1
WORKDIR /build/vision
RUN python setup.py install
WORKDIR /build
RUN rm -rf pytorch && rm -rf vision
```

Build with `docker build . -t rocmbuild:1`

Run interactively with:
```docker run -d --network=host --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size 8G rocmbuild:1 sleep 400000``` 
(hacky, but works+some volumes might be wanted)

---

### 评论 #29 — aaronmondal (2023-01-25T16:10:04Z)

Can confirm that with `HSA_OVERRIDE_GFX_VERSION=10.3.0` the issue seems to go away on Gentoo when unmasking the currently still pre-experimental Clang/LLVM 16 toolchain and adjusting the 5.3.3 ebuilds for the following package versions:
```bash
rocr-runtime-5.4.1  # 5.4.2 not yet available.
roct-thunk-interface-5.4.2
rocm-opencl-runtime-5.4.2
rocm-comgr-5.4.2
rocm-device-libs-5.4.2
```
So this issue should originate from one of these libraries.

The downside is that the gentoo Clang 16 toolchain is not able to build mesa due to rtti flag mismatch, so current usability may be limited. That's either a gentoo or mesa bug though.

---

### 评论 #30 — fruitpudding (2023-01-26T07:52:34Z)

@Kardi5 I can confirm this works. Thank you!

There are some mysterious bugs though (e.g. randomly popped up NaN tensors) I'll look further into them when I have time

---

### 评论 #31 — cgmb (2023-01-26T08:04:38Z)

> Can confirm that with `HSA_OVERRIDE_GFX_VERSION=10.3.0` the issue seems to go away

GFX version 10.3.0 and 11.0.0 are not generally compatible. Using this setting on an RDNA3 GPU is only going to cause you headaches.

> rocr-runtime-5.4.1  # 5.4.2 not yet available.

I'm not sure why it doesn't show up in the releases tab, but it has been tagged:
https://github.com/RadeonOpenCompute/ROCR-Runtime/releases/tag/rocm-5.4.2

---

### 评论 #32 — wsippel (2023-01-26T10:23:17Z)

I might be overly optimistic, but some bits and bops of ROCm have been tagged for 5.5 already, milestones are nearing completion, and documentation is getting updated, so official support should be pretty close? If it's just a matter of days, I'm not sure trying to get 5.4 working is worth the effort. 

---

### 评论 #33 — aaronmondal (2023-01-26T10:45:32Z)

@cgmb Thanks for the link! The download link for the 5.4.2 release is in the same format as the others and it seems to work fine for the existing ebuilds.

> GFX version 10.3.0 and 11.0.0 are not generally compatible. Using this setting on an RDNA3 GPU is only going to cause you headaches.

Sorry, I was unclear there. The `HSA_OVERRIDE...` makes the particular error go away but the GPU is still unusable.

With my current builds code like [this](https://github.com/eomii/rules_ll/blob/main/examples/hip_example/example.cpp), (built with hipcc from the 5.4.2 gentoo toolchain, not the toolchain in the linked repo) and `clinfo` fail with

```
HSA exception: Queue create failed at hsaKmtCreateQueue
```

If I understand correctly this means that the ROCt-Thunk-Interface can't even communicate with the driver (kernel 6.1.8-gentoo), so I'm surprised that the Dockerfile @Kardi5 posted works at all.

@wsippel Yeah tbh I don't expect 5.4 to be overly useful. From a toolchain perspective though there most likely won't be too many differences between 5.4 and 5.5. The ROCm "stable" releases are about as unstable as regular commits and the patches to get things working won't change too much between versions. Seeing that issues like [this](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/155) apparently have been unnoticed despite breaking all upstream builds for almost 2 months I'd not be too optimistic that 5.5 will just build out of the box.

---

### 评论 #34 — fruitpudding (2023-01-27T10:23:40Z)

> There are some mysterious bugs though (e.g. randomly popped up NaN tensors) I'll look further into them when I have time

These random crashes were gone after I compiled 6.2rc5 kernel w/ `drm-fixes-2023-01-27`. I believe at least part of the stability problem is caused by kernel-side bugs. Try `drm-fixes` (or the more risky `drm-next`) if you encountered mysterious bugs.

The performance is still quite low anyway (<5it/s stable diffusion txt2img generation) I hope it could become better after ROCm 5.5 is released.

---

### 评论 #35 — wsippel (2023-01-28T08:49:56Z)

@fruitpudding For Stable Diffusion, you could check out [SHARK](https://github.com/nod-ai/SHARK) for the time being. It uses Vulkan Compute and provides RDNA3 optimised kernels. The feature set is still quite limited though, especially compared to Auto1111's implementation. 

---

### 评论 #36 — fruitpudding (2023-01-30T01:51:53Z)

@wsippel [Shark.sd](shark.sd) is fast. However it got a completely concrete/fixed data shape (you can't even change the resolution of generated images) and I don't think this could change easily.
If your use case is providing a fixed-size image generation web service, shark.sd might be good. Otherwise I may try and see if something like [AITemplate](https://github.com/facebookincubator/AITemplate) works, which still requires a solid ROCm software stack.

---

### 评论 #37 — Mushoz (2023-01-31T14:22:36Z)

> I might be overly optimistic, but some bits and bops of ROCm have been tagged for 5.5 already, milestones are nearing completion, and documentation is getting updated, so official support should be pretty close? If it's just a matter of days, I'm not sure trying to get 5.4 working is worth the effort.

@wsippel Any pointers where you are seeing stuff getting tagged for 5.5.0 and where I can find the documentation updates? Curious to look around so I hopefully can get a better understanding of how far off we currently are. Thanks!

---

### 评论 #38 — MoritzMaxeiner (2023-01-31T19:06:25Z)

FWIW, I have a 7900 XT running (on Funtoo Linux) under kernel 6.2rc6 (which includes drm-fixes-2023-01-27) with ROCm 5.4.2 compiled using LLVM 16 snapshot 20230127: I also receive the `Assertion 'code_buf != NULL && "Code buffer allocation failed"' failed` error when running `clinfo` or `rocminfo`, unless using `HSA_OVERRIDE_GFX_VERSION=10.3.0` (which I gather shouldn't be used).

My question would be this: Is ROCm 5.5 going to officially support the 7900 XT?

---

### 评论 #39 — wsippel (2023-02-01T10:18:11Z)

@Mushoz I just noticed it rummaging through random AMD repos (eg rocMLIR, MIOpen, rocWMMA). The due date for the 5.5 milestone in MIOpen is today for example. Doesn't necessarily mean it'll release today or tomorrow of course, there are still some urgent issues open, but it seems to be getting close.

@MoritzMaxeiner `rocminfo` and `clinfo` work just fine for me on a 7900XTX, running the official ROCm 5.4.2 packages on Arch (llvm 15, kernel 6.1.8-xanmod). OpenCL in general and Blender's HIP backend also work, I think it's mostly stuff relying on MIOpen that doesn't. RDNA3 has since been at least partially enabled in MIOpen, so I think - or hope - that it'll work in ROCm 5.5.

---

### 评论 #40 — MoritzMaxeiner (2023-02-01T15:59:00Z)

> @MoritzMaxeiner `rocminfo` and `clinfo` work just fine for me on a 7900XTX, running the official ROCm 5.4.2 packages on Arch (llvm 15, kernel 6.1.8-xanmod). OpenCL in general and Blender's HIP backend also work, I think it's mostly stuff relying on MIOpen that doesn't. RDNA3 has since been at least partially enabled in MIOpen, so I think - or hope - that it'll work in ROCm 5.5.

Huh, that's interesting. When I try to compile [rocm-device-libs](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/) with llvm(+clang) 15 I receive the following error ([full build log](https://github.com/RadeonOpenCompute/ROCm/files/10558935/build_rocm-device-libs-5.4.2-llvm-15.log)):

```
[...]/ockl/src/mtime.cl:20:12: error: use of undeclared identifier '__builtin_amdgcn_s_sendmsg_rtnl'
    return __builtin_amdgcn_s_sendmsg_rtnl(0x83);
```

I assumed this is some new thing only avaible in llvm 16, which is why I used the latest snapshot.

---

### 评论 #41 — aaronmondal (2023-02-02T13:30:14Z)

@MoritzMaxeiner In upstream Clang the symbol was added after the 15 release cut. I believe @wsippel used the AMD llvm-15 fork which had this symbol added in their customized variant for ROCm 5.4.2. Upstream Clang (16/17) also has it.

Original:
https://github.com/llvm/llvm-project/blob/llvmorg-15.0.7/clang/include/clang/Basic/BuiltinsAMDGPU.def

AMD variant:
https://github.com/RadeonOpenCompute/llvm-project/blob/rocm-5.4.2/clang/include/clang/Basic/BuiltinsAMDGPU.def

---

### 评论 #42 — MoritzMaxeiner (2023-02-02T20:30:23Z)

@aaronmondal Thanks, I've now tried both with "normal" llvm/clang 15 with that change as a patch, as well as with [llvm-roc](https://github.com/RadeonOpenCompute/llvm-project/tree/rocm-5.4.2) (5.4.2). Neither makes any difference, I still receive the `Code buffer allocation failed` error on my 7900 XT (not XTX) with both clinfo and rocminfo.

---

### 评论 #43 — aaronmondal (2023-02-02T21:57:37Z)

@MoritzMaxeiner Ok cool then this is at least reproducible and was likely also encountered by AMD. That makes me optimistic that our issue will be fixed in the 5.5 release.

I still find it unsettling that a similar setup already seems to work for some other users, but I'm not sure that it's worth the effort to force things to work with 5.4.2

@saadrahim It'd be really nice if there could be a discussion with AMD to conduct ROCm development more in an open-source fashion and not just downstreaming releases to GitHub when everything is "perfect" (for instance a [GitHub discussion](https://docs.github.com/de/discussions)). The number of people working at HEAD without regard for stable releases is continuously increasing. Having to wait for stable releases causes delays in the development of downstream tooling and projects and ultimately harms end user experience.

At least regarding tooling I can say that I'd much rather have a completely buggy ROCm trunk branch that maybe crashes every 5 seconds than not being able to integrate AMD support all :sweat_smile: 

---

### 评论 #44 — MoritzMaxeiner (2023-02-04T14:00:20Z)

@aaronmondal Well, it turned out the fix is simple: Funtoo (copied from Gentoo, so possibly same issue there) sets `CMAKE_CXX_FLAGS_RELEASE` to empty by default, which causes [rocr-runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime) to be compiled with debug settings in release mode. The solution is to explicitly define `NDEBUG` in the rocr-runtime ebuild like so `-DCMAKE_CXX_FLAGS_RELEASE="${CXXFLAGS} -DNDEBUG"`. With that set, I can successfully run rocminfo, clinfo, and the rocm bandwith test.

Imho rocr-runtime's CMakeLists.txt should not depend on `CMAKE_CXX_FLAGS_RELEASE`, which can be set from the outside, to contain `-DNDEBUG`. It should ensure internally that it's added as needed based on the caller setting `CMAKE_BUILD_TYPE`.


---

### 评论 #45 — Mushoz (2023-02-07T13:31:30Z)

@MoritzMaxeiner Are you able to run tensorflow now? Or is that still not possible?

The lack of communication is getting really frustrating. Especially reading back topics such as these: https://github.com/RadeonOpenCompute/ROCm/issues/1776

That last comment in particular really aged like milk unfortunately :(

---

### 评论 #46 — CorvetteCole (2023-02-07T16:24:34Z)

I still cannot on my 7900 XTX. Hoping 5.5 fixes this.

---

### 评论 #47 — Blackanubis (2023-02-07T17:40:04Z)

I have the impression that a lot of us are looking forward to this update...

---

### 评论 #48 — MoritzMaxeiner (2023-02-07T18:07:28Z)

@Mushoz Nope, unfortunately not. tensorflow-rocm requires rccl to be installed in the system, and rccl 5.4.2 simply will not compile for me (see [rccl_build_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/10678090/rccl_build_log.txt)). It complains about shared variables not being allowed to be extern when in invoking hipcc 5.4.2, despite the latter supposedly having support for that for [quite a while](https://rocmdocs.amd.com/en/latest/Programming_Guides/HIP-FAQ.html#does-the-hip-clang-compiler-support-extern-shared-declarations). Since I don't know if this is an upstream issue or a packaging issue, I'm currently deliberating how to proceed. I've tried compiling hip manually, but that was a wholly unpleasant experience I'd like to avoid repeating.

Also, despite rocminfo and clinfo running fine, Blender 3.4.1 is not able to find my 7900 XT as a HIP device without any error messages. Simply "no device found".

I've also tried out the binary wheel for pytorch rocm (5.2), but that similarly just says "no device found".

---

### 评论 #49 — wsippel (2023-02-07T18:34:15Z)

@MoritzMaxeiner Blender's HIP backend should totally work. It works for me, on a 7900XTX. And it's quite fast, too. I expect HIP-RT to be faster, but let's say it performs as expected right now (comparable to a 3090Ti with CUDA). From what I can tell, HIP works, MIOpen doesn't. And MIOpen is what's needed for Torch and Tensorflow. 

---

### 评论 #50 — MoritzMaxeiner (2023-02-07T18:52:41Z)

@wsippel Hm, it seems you're right. I had removed the hip package (since it didn't seem to work properly to compile rccl), but it is required to run blender. So after reinstalling the dedicated hip, Blender can find the the gpu and the cpu. It seems Blender does not ship with the required runtime libraries for hip, you need to have them available in the system.

---

### 评论 #51 — aaronmondal (2023-02-07T18:55:15Z)

@MoritzMaxeiner So far I couldn't get things to work with the NDEBUG workaround, but It's highly likely i just messed something up in the process. I'll try again but at the moment I'm still getting this error somewhere in the `clinfo` output and when executing HIP code:
```
HSA exception: Queue create failed at hsaKmtCreateQueue
```
I think this points to driver issues, but I may be wrong. The 6.2 kernel release is around the corner, so maybe we can hope for some kind of progress then.

---

### 评论 #52 — littlewu2508 (2023-02-08T04:17:10Z)

@MoritzMaxeiner @aaronmondal I'm the maintainer of Gentoo ROCm packages. I've pushed some 9999 ebuilds at https://github.com/littlewu2508/gentoo/tree/rocm-9999, and they built in my environment. Seems that it already has good support for RDNA3 (turn on `amdgpu_targets_gfx1100` use flag), but I don't have RDNA3 cards. Are you interested in trying them out? You can turn on `FEATURES=test` for rocBLAS and miopen to test the GPU (alert: rocBLAS src_test is very time & power consuming)

I'm also very curious about the AI instruction of RDNA3. From code rocBLAS-5.5 seems to support using these instructions. `USE=benchmark` turns on installing `rocblas-bench` for sci-libs/rocBLAS

---

### 评论 #53 — Mushoz (2023-02-08T10:50:47Z)

I can see that ROCm 5.4.3 has just been released, so that pretty much means a 5.5.0 release is not yet near :(

@littlewu2508 that looks very interesting, thank you! What exactly do you mean with 9999 ebuilds? Is that similar to Arch's -git packages in the AUR? If so, I will happily see if I can figure out how the Gentoo build system works and try to install your packages in a Gentoo docker container. My hope is that if this works, I can just share the docker buildfile for others to use. 

---

### 评论 #54 — littlewu2508 (2023-02-08T11:04:51Z)

> that looks very interesting, thank you! What exactly do you mean with 9999 ebuilds? Is that similar to Arch's -git packages in the AUR?

Exactly, 9999 ebuilds tracks the git repo as its source, not release tarballs. However in order to install according to FHS and other Gentoo policies, many packages are heavily patched, and 9999 ebuilds can be broken very easily.

> If so, I will happily see if I can figure out how the Gentoo build system works and try to install your packages in a Gentoo docker container. My hope is that if this works, I can just share the docker buildfile for others to use.

That would be nice. I also use a gentoo docker to develop these 9999 ebuilds, I can manage to share them.

---

### 评论 #55 — Mushoz (2023-02-08T11:08:24Z)

If you can share those dockerfiles that would be lovely! I have no experience whatsoever with Gentoo, so it's going to be a bit of a learning curve for me. A good starting point would be much appreciated :)

---

### 评论 #56 — aaronmondal (2023-02-08T15:00:48Z)

@littlewu2508 Which Clang/LLVM version should I use with that? The `pre20230107` was missing symbols for the device libs and building `rc1` gives me the error below. Could there be a patch missing or something? This looks to me like a patch was incompletely applied, either on my end or in your repo:
```cpp
FAILED: bin/amdgpu-arch 
: && /usr/lib/llvm/16/bin/clang++-16 -O2 -pipe -fPIC -fno-semantic-interposition -fvisibility-inlines-hidden -Werror=date-time -Werror=unguarded-availability-new -Wall -Wextra -Wno-unused-parameter -Wwrite-strings -Wcast-qual -Wmissing-field-initializers -Wimplicit-fallthrough -Wcovered-switch-default -Wno-noexcept-type -Wnon-virtual-dtor -Wdelete-non-virtual-dtor -Wsuggest-override -Wstring-conversion -Wmisleading-indentation -Wctad-maybe-unsupported -fdiagnostics-color -ffunction-sections -fdata-sections -fno-common -Woverloaded-virtual -pedantic -Wno-long-long -Wno-nested-anon-types -Wl,-O2 -Wl,--as-needed -Wl,--color-diagnostics    -Wl,--gc-sections tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o -o bin/amdgpu-arch -L/usr/lib/llvm/16/lib64 -Wl,-rpath,"\$ORIGIN/../lib64:/usr/lib/llvm/16/lib64"  lib64/libclang-cpp.so.16+libcxx  /usr/lib/llvm/16/lib64/libLLVM-16+libcxx.so && :
ld.lld: error: undefined symbol: hsa_init
>>> referenced by AMDGPUArch.cpp
>>>               tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o:(main)

ld.lld: error: undefined symbol: hsa_iterate_agents
>>> referenced by AMDGPUArch.cpp
>>>               tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o:(main)

ld.lld: error: undefined symbol: hsa_shut_down
>>> referenced by AMDGPUArch.cpp
>>>               tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o:(main)

ld.lld: error: undefined symbol: hsa_agent_get_info
>>> referenced by AMDGPUArch.cpp
>>>               tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o:(iterateAgentsCallback(hsa_agent_s, void*))
>>> referenced by AMDGPUArch.cpp
>>>               tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o:(iterateAgentsCallback(hsa_agent_s, void*))
```
**Edit**: I think I need need to try `20230127` which contains changes that are not in `rc1`.

---

### 评论 #57 — littlewu2508 (2023-02-08T16:15:13Z)

> Which Clang/LLVM version should I use with that?

I just picked dafebd5b5a08dde25f5f52f65cac54bd6ec0ecde which is the HEAD of llvm-project at that time. llvm, clang, lld is building fine

---

### 评论 #58 — aaronmondal (2023-02-08T17:07:34Z)

The `rocm-device-libs` gentoo ebuild fails to build because of [this](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be). That is a dependency for the `rocr-runtime` which defines the missing symbols.

Upstreamed changes to `AMDGPUArch.cpp` from the amd llvm fork to llvm main break at least the pinned `16*` gentoo ebuilds when hsa is detected on the system (which is part of rocr-runtime). So we have a circular dependency between `AMDGPUArch.cpp` and rocr-runtime (which depends on rocm-device-libs).

I'll try to remove the old `rocr-runtime` and rebuild without any amd libs on the system.

---

### 评论 #59 — littlewu2508 (2023-02-09T02:49:54Z)

> The `rocm-device-libs` gentoo ebuild fails to build because of [this](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be). That is a dependency for the `rocr-runtime` which defines the missing symbols.
> 

Thanks. Last time I tested rocm-device-libs was half a month ago, seems that this commit last week broke the existing gentoo rocm packaging. 

> Upstreamed changes to `AMDGPUArch.cpp` from the amd llvm fork to llvm main break at least the pinned `16*` gentoo ebuilds when hsa is detected on the system (which is part of rocr-runtime). So we have a circular dependency between `AMDGPUArch.cpp` and rocr-runtime (which depends on rocm-device-libs).

I'll try to remove the dependency of rocm-device-libs (and the whole llvm stack) of rocr-runtime as a workaround. But does that mean the llvm-16 will have to explicitly depend on rocr-runtime? That sounds a bit strange.

---

### 评论 #60 — littlewu2508 (2023-02-10T10:53:22Z)

> The rocm-device-libs gentoo ebuild fails to build because of [this](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be). That is a dependency for the `rocr-runtime`, which defines the missing symbols.
> 

What you want is [this llvm change](https://github.com/llvm/llvm-project/commit/df0488369d32a8cb1604a85d008e602e4de24d05), it's in main branch, not in llvm-16 release candidates. Perhaps we need either need to let llvm upstream backport to 16, or revert [this](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be).

> Upstreamed changes to `AMDGPUArch.cpp` from the amd llvm fork to llvm main break at least the pinned `16*` gentoo ebuilds when hsa is detected on the system. I think there is a circular dependency between the file in the previous error and rocr-runtime (which depends on rocm-device-libs).
> 

I'll try to figure that out. I guess it's essentially a packaging issue.


---

### 评论 #61 — littlewu2508 (2023-02-10T14:16:43Z)

> 



> ```c++
> FAILED: bin/amdgpu-arch 
> : && /usr/lib/llvm/16/bin/clang++-16 -O2 -pipe -fPIC -fno-semantic-interposition -fvisibility-inlines-hidden -Werror=date-time -Werror=unguarded-availability-new -Wall -Wextra -Wno-unused-parameter -Wwrite-strings -Wcast-qual -Wmissing-field-initializers -Wimplicit-fallthrough -Wcovered-switch-default -Wno-noexcept-type -Wnon-virtual-dtor -Wdelete-non-virtual-dtor -Wsuggest-override -Wstring-conversion -Wmisleading-indentation -Wctad-maybe-unsupported -fdiagnostics-color -ffunction-sections -fdata-sections -fno-common -Woverloaded-virtual -pedantic -Wno-long-long -Wno-nested-anon-types -Wl,-O2 -Wl,--as-needed -Wl,--color-diagnostics    -Wl,--gc-sections tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o -o bin/amdgpu-arch -L/usr/lib/llvm/16/lib64 -Wl,-rpath,"\$ORIGIN/../lib64:/usr/lib/llvm/16/lib64"  lib64/libclang-cpp.so.16+libcxx  /usr/lib/llvm/16/lib64/libLLVM-16+libcxx.so && :
> ld.lld: error: undefined symbol: hsa_init
> ```

Can you try adding a `-lhsa-runtime64` in compile command?

I suspect the linking error is not ABI breakage, just missed this lib from command line.

---

### 评论 #62 — jhuber6 (2023-02-10T14:22:18Z)

> > 
> 
> > ```c++
> > FAILED: bin/amdgpu-arch 
> > : && /usr/lib/llvm/16/bin/clang++-16 -O2 -pipe -fPIC -fno-semantic-interposition -fvisibility-inlines-hidden -Werror=date-time -Werror=unguarded-availability-new -Wall -Wextra -Wno-unused-parameter -Wwrite-strings -Wcast-qual -Wmissing-field-initializers -Wimplicit-fallthrough -Wcovered-switch-default -Wno-noexcept-type -Wnon-virtual-dtor -Wdelete-non-virtual-dtor -Wsuggest-override -Wstring-conversion -Wmisleading-indentation -Wctad-maybe-unsupported -fdiagnostics-color -ffunction-sections -fdata-sections -fno-common -Woverloaded-virtual -pedantic -Wno-long-long -Wno-nested-anon-types -Wl,-O2 -Wl,--as-needed -Wl,--color-diagnostics    -Wl,--gc-sections tools/amdgpu-arch/CMakeFiles/amdgpu-arch.dir/AMDGPUArch.cpp.o -o bin/amdgpu-arch -L/usr/lib/llvm/16/lib64 -Wl,-rpath,"\$ORIGIN/../lib64:/usr/lib/llvm/16/lib64"  lib64/libclang-cpp.so.16+libcxx  /usr/lib/llvm/16/lib64/libLLVM-16+libcxx.so && :
> > ld.lld: error: undefined symbol: hsa_init
> > ```
> 
> Can you try adding a `-lhsa-runtime64` in compile command?
> 
> I suspect the linking error is not ABI breakage, just missed this lib from command line.

I was about to suggest this, because I'm unsure why it seems to be missing. This code path should only be taken if CMake found the `hsa-runtime64` package. Which indicates that the library should've been linked in.

---

### 评论 #63 — littlewu2508 (2023-02-10T14:33:00Z)

> I was about to suggest this, because I'm unsure why it seems to be missing. This code path should only be taken if CMake found the hsa-runtime64 package. Which indicates that the library should've been linked in.

Some cmake issue, I believe. I wrote a standard `CMakeLists.txt` using ` target_link_libraries(foo  hsa-runtime64::hsa-runtime64)` and the libhsa-runtime64.so appeared in `build.ninja` I suspect there's strange thing going on with the `clang_target_link_libraries`

---

### 评论 #64 — jhuber6 (2023-02-10T14:34:56Z)

> > I was about to suggest this, because I'm unsure why it seems to be missing. This code path should only be taken if CMake found the hsa-runtime64 package. Which indicates that the library should've been linked in.
> 
> Some cmake issue, I believe. I wrote a standard `CMakeLists.txt` using ` target_link_libraries(foo hsa-runtime64::hsa-runtime64)` and the libhsa-runtime64.so appeared in `build.ninja` I suspect there's strange thing going on with the `clang_target_link_libraries`

I noticed that and made https://github.com/llvm/llvm-project/commit/067a5c68845c13d45e85ec9eaa11d2b2d829bab4 a few minutes ago. Maybe it will fix the problems.

---

### 评论 #65 — MoritzMaxeiner (2023-02-10T17:36:27Z)

@littlewu2508 Hey, thanks for the info. Well, the main problem I ran into simply happened because I forgot to to add `AMDGPU_TARGETS` use expand to my profile, so that's why rccl wasn't compiling. After fixing that, I now have (some parts of) rocm 5.4.3 compiled with llvm 15.0.7, up to and including rccl (with gfx1100). Since my current goal is to compile pytorch, I also had to add an additional package `dev-libs/rocm-core` (pytorch won't compile without the contained headers), that you may want to adapt for Gentoo: [rocm-core.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/10709854/rocm-core.tar.gz). Also, dev-util/hip should probably distribute hipify-perl, since future versions of rccl are going to require it at some point: https://github.com/ROCmSoftwarePlatform/rccl/commit/562dd870368db437541c8460c367009abaf579b0


---

### 评论 #66 — MoritzMaxeiner (2023-02-10T23:43:43Z)

For anyone interested, I was able to build miopen 5.4.3 with gfx1100 offloading enabled (afaict anyway). However, running the test suite yielded only about 87% of tests passing on my 7900 XT, see the full log here: [miopen_build_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/10711991/miopen_build_log.txt)

Also of note for anyone reproducing: My CPU load (ryzen 9 7900) was being fully loaded during the test runs, while rocm-smi showed only between 6% and 10% load.

---

### 评论 #67 — littlewu2508 (2023-02-11T02:21:55Z)

> @littlewu2508 Hey, thanks for the info. Well, the main problem I ran into simply happened because I forgot to to add `AMDGPU_TARGETS` use expand to my profile, so that's why rccl wasn't compiling. After fixing that, I now have (some parts of) rocm 5.4.3 compiled with llvm 15.0.7, up to and including rccl (with gfx1100). 

Sounds nice.

Since my current goal is to compile pytorch, I also had to add an additional package `dev-libs/rocm-core` (pytorch won't compile without the contained headers), that you may want to adapt for Gentoo: [rocm-core.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/10709854/rocm-core.tar.gz). Also, dev-util/hip should probably distribute hipify-perl, since future versions of rccl are going to require it at some point: [ROCmSoftwarePlatform/rccl@562dd87](https://github.com/ROCmSoftwarePlatform/rccl/commit/562dd870368db437541c8460c367009abaf579b0)

I'll take a look at hipify-perl package

---

### 评论 #68 — littlewu2508 (2023-02-11T02:25:25Z)

> For anyone interested, I was able to build miopen 5.4.3 with gfx1100 offloading enabled (afaict anyway). However, running the test suite yielded only about 87% of tests passing on my 7900 XT, see the full log here: [miopen_build_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/10711991/miopen_build_log.txt)
> 

Interesting. I browsed miopen-5.4.3 source an there's not a single word mentioning gfx1100.

> Also of note for anyone reproducing: My CPU load (ryzen 9 7900) was being fully loaded during the test runs, while rocm-smi showed only between 6% and 10% load.

Normal. The test is basically comparing convolution results between CPU and GPU, and your GPU surely beats ryzen 9 7900. This is also true for other rocm math libraries.

I still suggest not using rocm-5.4 for RDNA3 because the support for rocBLAS is very initial. I guess you won't get the ideal performance (try rocblas-bench)

---

### 评论 #69 — littlewu2508 (2023-02-11T06:23:33Z)

@Mushoz @MoritzMaxeiner I pushed my Gentoo rocBLAS-9999 nightly built docker at https://hub.docker.com/r/littlewu2508/clang-16_rc2-rocblas-9999-5.5-gfx1100. It has llvm-16.0.0_rc2 and the latest rocBLAS. You can enter it by ` docker run -it --device=/dev/kfd --device=/dev/dri`, and execute `rocblas-test` to verify using openblas. You can also use `rocblas-bench` to do benchmarks

---

### 评论 #70 — Displacer (2023-02-11T07:53:04Z)

docker image with rocblas-test basically works for me (some rare failures still exists). 

---

### 评论 #71 — Displacer (2023-02-11T08:01:03Z)

test is still in progess, current log: http://0x0.st/HrNE.txt

---

### 评论 #72 — littlewu2508 (2023-02-11T08:21:42Z)

> test is still in progess, current log: http://0x0.st/HrNE.txt

The test is extreeeemely long and electric power demanding.

There are existing issues like https://github.com/ROCmSoftwarePlatform/rocBLAS/issues/1287

The segfault may have relations with openblas issue https://github.com/xianyi/OpenBLAS/issues/3740. You can install other CPU blas implementations to see if the issue is gone

---

### 评论 #73 — Displacer (2023-02-11T10:19:43Z)

full log: http://0x0.st/HrqN.txt

unfortunately docker image seems lack OpenCL and some other stuff like hipblas to test with lc0 or lc0-hip



---

### 评论 #74 — littlewu2508 (2023-02-12T14:39:04Z)

I pushed some more 9999 ebuilds (tracking ROCm git developing branch) at https://github.com/littlewu2508/gentoo/tree/rocm-9999, including most math libraries (should be enough for pytorch/tensorflow I guess). I'll compile them for gfx1100 in docker.

---

### 评论 #75 — littlewu2508 (2023-02-12T16:58:51Z)

> I'll compile them for gfx1100 in docker.

Now start pushing to https://hub.docker.com/r/littlewu2508/clang-16_rc2-rocm-math-libs-9999-5.5-gfx1100

---

### 评论 #76 — MoritzMaxeiner (2023-02-12T18:53:29Z)

@littlewu2508 Thanks for your work. Strangely enough, when setting up rocm 9999 deps (with lllvm 16 rc2), and then trying to compile rocFFT I always get

```
cd /home/mm/Workshop/rocm/rocFFT/build/library/src && /home/mm/Workshop/rocm/rocFFT/build/library/src/rocfft_aot_helper "" /home/mm/Workshop/rocm/rocFFT/build/library/src/rocfft_kernel_cache.db /home/mm/Workshop/rocm/rocFFT/build/library/src/rocfft_rtc_helper gfx1100
terminate called after throwing an instance of 'std::runtime_error'
  what():  compile failed without log
```

(The above is when trying to compile it manually, after receiving an empty what in the 9999 ebuild. Trying out a different architecture yields the same error).

---

### 评论 #77 — littlewu2508 (2023-02-13T15:46:41Z)

I managed to compile pytorch and torchvision based on Gentoo's rocm stack, with a bit bug fixing on existing 9999 rocm ebuilds. The rocm-enabled caffe2 ebuild and torchvision (copied from science overlay) are pushed to https://github.com/littlewu2508/gentoo/tree/rocm-9999.

Meanwhile the docker containing pytorch and  torchvision for 7900XT is https://hub.docker.com/r/littlewu2508/clang-16_rc2-pytorch-1.12-rocm-9999-5.5-gfx1100. Since I don't have RDNA3 GPU I can't test it, but the gfx1031-pytorch can train a simple mnist now.

I know this is a tensorflow issue, but debugging with tensorflow compilation is far more difficult for me, and currently I have no plan for using it yet, so I'm not going to try compile tensorflow recently, but I'm open to questions if anyone want to give a try.

---

### 评论 #78 — aaronmondal (2023-02-13T17:55:45Z)

@littlewu2508 I just tried getting your `rocm-9999` ebuilds to work again. I set `LLVM_MAX_SLOT=17` in the ROCm 9999 ebuilds and used the `17.0.0_pre20230211` Clang/LLVM packages. I'm incredibly excited to say that your ebuilds seem to work and hipcc compiles and runs the [code I orignally posted](https://github.com/eomii/rules_ll/blob/main/examples/hip_example/example.cpp). Thanks a lot for your efforts! :tada:
```
Number of devices is 1
System major: 11
System minor: 0
Device name : AMD Radeon Graphics
Vector calculation passed.
```
The `clinfo` command also works without setting the `HSA_*` flag.

---

### 评论 #79 — littlewu2508 (2023-02-14T03:32:55Z)

> @littlewu2508 I just tried getting your `rocm-9999` ebuilds to work again. I set `LLVM_MAX_SLOT=17` in the ROCm 9999 ebuilds and used the `17.0.0_pre20230211` Clang/LLVM packages. I'm incredibly excited to say that your ebuilds seem to work and hipcc compiles and runs the [code I orignally posted](https://github.com/eomii/rules_ll/blob/main/examples/hip_example/example.cpp). Thanks a lot for your efforts! tada
> 
> ```
> Number of devices is 1
> System major: 11
> System minor: 0
> Device name : AMD Radeon Graphics
> Vector calculation passed.
> ```
> 
> The `clinfo` command also works without setting the `HSA_*` flag.

Have you tried using the llvm-16_rc2 with rocm-device-libs reverting https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be ? It would be great if the whole ROCm would work on RDNA3 with the upcoming llvm-16 releases.

---

### 评论 #80 — aaronmondal (2023-02-14T14:31:51Z)

Maybe it's better to try to backport https://github.com/llvm/llvm-project/commit/df0488369d32a8cb1604a85d008e602e4de24d05 into Clang 16 instead.

I'll try to get feedback on this at https://reviews.llvm.org/D142507.

---

### 评论 #81 — Displacer (2023-02-14T16:56:52Z)

> > @littlewu2508 I just tried getting your `rocm-9999` ebuilds to work again. I set `LLVM_MAX_SLOT=17` in the ROCm 9999 ebuilds and used the `17.0.0_pre20230211` Clang/LLVM packages. I'm incredibly excited to say that your ebuilds seem to work and hipcc compiles and runs the [code I orignally posted](https://github.com/eomii/rules_ll/blob/main/examples/hip_example/example.cpp). Thanks a lot for your efforts! tada
> > ```
> > Number of devices is 1
> > System major: 11
> > System minor: 0
> > Device name : AMD Radeon Graphics
> > Vector calculation passed.
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > The `clinfo` command also works without setting the `HSA_*` flag.
> 
> Have you tried using the llvm-16_rc2 with rocm-device-libs reverting [RadeonOpenCompute/ROCm-Device-Libs@8dc779e](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/8dc779e19cbf2ccfd3307b60f7db57cf4203a5be) ? It would be great if the whole ROCm would work on RDNA3 with the upcoming llvm-16 releases.

I have forgotten to mention this isue in gentoo https://bugs.gentoo.org/891499

temporary fixed with fetch specific commit in ebuild:
EGIT_COMMIT="4d8e283e8ff17e89b7502649a78ac58d6523f4a3"

backporting changes to llvm-16 looks like a correct solution to this issue


---

### 评论 #82 — cromefire (2023-02-15T22:55:15Z)

> Meanwhile the docker containing pytorch and torchvision for 7900XT is https://hub.docker.com/r/littlewu2508/clang-16_rc2-pytorch-1.12-rocm-9999-5.5-gfx1100. Since I don't have RDNA3 GPU I can't test it, but the gfx1031-pytorch can train a simple mnist now.

Still fails with some weird memory paging issues, I have a feeling the current ROCm has issues with memory allocation on RDNA3 (did a simple resnet test, although it fails before it even reaches the model).

---

### 评论 #83 — Kardi5 (2023-02-16T13:15:05Z)

@cromefire If you are experiencing GPU page faults, hangs or resets maybe this will help you (atleast it helped me):
`echo "high" > /sys/class/drm/card0/device/power_dpm_force_performance_level` (you might need to change the card number)
There seems to be some kind of (power state/frequency scaling?) bug. See https://gitlab.freedesktop.org/mesa/mesa/-/issues/7939
If you want to do this more granular checkout https://gitlab.freedesktop.org/drm/amd/-/issues/2337#note_1732289

---

### 评论 #84 — cromefire (2023-02-17T21:26:03Z)

@Kardi5 Well that sadly only partially worked:
```
Memory access fault by GPU node-1 (Agent handle: 0x5612741e3b90) on address 0x7f60502bc000. Reason: Page not present or supervisor privilege.
```
It's not crashing like immediately anymore, but there's probably something else that's wrong (Used Pytorch).

---

### 评论 #85 — littlewu2508 (2023-02-20T04:24:11Z)

I'm afraid memory issues are related to low level runtimes (amdgpu kernel driver, roct-thunk-interface, rocr-runtime). roct-thunk-interface and rocr-runtime does not have a clear development branch on github. They update codes in a bunch at every release. So we have to wait for ROCm-5.5

---

### 评论 #86 — Blackanubis (2023-02-27T16:35:15Z)

The wait is long, I regret having invested in a 7900xtx. I foolishly believed that it would work directly.

---

### 评论 #87 — wsippel (2023-02-27T19:48:57Z)

> The wait is long, I regret having invested in a 7900xtx. I foolishly believed that it would work directly.

HIP worked day 1. But yeah, I'm in the same boat - I thought we were close four weeks ago, but here we are. The cards launched three months ago. I'm sure it's not the devs' fault, but this is just embarrassing. Is it too much to ask for full support on release day? Clearly not, Nvidia can do it. AMD isn't the underdog anymore, so that excuse no longer works, either. They have a lot of catching up to do, and I see very little effort. I'm incredibly disappointed, both as a customer and as a shareholder.

---

### 评论 #88 — CorvetteCole (2023-02-27T20:26:02Z)

Same exact boat. Purchased AMD for the Linux support, figured 7900 XTX would be good enough for my ML needs compared to the 4090. However, right now it is nothing. I can live with bad performance, but this kind of support is why CUDA remains uncontested

---

### 评论 #89 — stylerw (2023-03-01T02:41:24Z)

I also am sad that I went AMD this round, largely on the strength of their (historical) better Linux support.    I never thought I'd be sacrificing Linux compatibility by going AMD, particularly when I had such a positive experience with ROCm with my prior late-cycle RDNA2 card (which just didn't have enough VRAM).

It's understandable to have to wait for upstreamed code (e.g. Mesa, Linux Kernel) to reach the Distro for full GPU support, but this is code coming directly from AMD, and thus, there's little excuse for this long of a lag before enabling core functionalities of these cards.

I hope that we can get some nightlies for ROCm 5.5, or at least between-release updates to the repo so we can compile ourselves.  Or at the very least, a timeline update, so we know if we're days, weeks, or months away from a working ROCm build, and thus, working Torch/Tensorflow.  

---

### 评论 #90 — CorvetteCole (2023-03-01T05:53:43Z)

Yes the most frustrating part is the total lack of transparency. I'm sure the devs are not to blame here for that, but it is hard to get a finger on where we are on the priority list. I have been thinking about selling and moving to a 4080 or 4090, just hate to leave the well-supported Linux land of AMD.

---

### 评论 #91 — Mushoz (2023-03-01T12:49:16Z)

Well, @saadrahim specifically promised he would ask his higher-ups what they can do in terms of a forward looking statement for a (rough) timeline, but we haven't heard back from him. Of course the decision is ultimately with his higher-ups, meaning we cannot blame him whatever decision is made. However, suffice to say I am extremely disappointed with the fact he never got back to us with news about this decision, even if the decision itself could be bad news.

Post I am talking about: https://github.com/RadeonOpenCompute/ROCm/discussions/1836#discussioncomment-4586574

Anyway, I paid a premium for being an early adopter, but I have actually been using my old 6900XT more than my 7900 XTX due to the fact I cannot use my 7900 XTX for half of my usecases at all. In the future, I will definitely pick Nvidia over AMD as an early adopter (which I usually am) for a next release. It saddens me, since I WANT to support AMD. But they are really making it hard.

Early adopters like us are what's required for the ROCm ecosystem to grow, since we will share our experiences with other potential users. It's very unfortunate I am forced to share a negative experience. I KNOW it shouldn't have to be negative experiences, because in general my experience with my 6900 XT was extremely positive. But alas.

---

### 评论 #92 — ilisparrow (2023-03-02T20:06:48Z)

Thank you for your feedback. 
I was looking into AMD and ROCm for an Nvidia alternative. But it seems like the software is still not ready, and the support seems lacking, even more when you look at other issues. :/

---

### 评论 #93 — Kademo15 (2023-03-16T06:37:44Z)

Is there still no info or did I miss something

---

### 评论 #94 — Mushoz (2023-03-16T06:57:49Z)

@Kademo15 Still no news unfortunately. It seems that it's simply not worth to support AMD as an early adopter if you care about ML in any way, shape or form. I think I speak for a lot of us if I say that I am thoroughly disappointed.

---

### 评论 #95 — MoritzMaxeiner (2023-03-16T11:02:01Z)

> Is there still no info or did I miss something

You can just check the [release page](https://github.com/RadeonOpenCompute/ROCm/releases) every couple of days, it's what I do :sweat_smile:. I'll reserve my judgement for until 5.5.0 is released, though I'm not happy about how long it's taking, either. But good software development takes time, so for now I'll continue to be patient.

---

### 评论 #96 — Kademo15 (2023-03-16T14:14:16Z)

@Mushoz Yea i bought the gpu and right then ai image creation and chat gpt and all that stuff kicked in. And i took interest in ai image generation becaue i saw how good it had become and now i am sitting here running directml version of stablediffusion at 20+s/it if i want to go above 512x512. Its frustrating i have a for me 1300€ card and i am waiting 5+ months for drivers. 

---

### 评论 #97 — Kademo15 (2023-03-16T14:20:57Z)

@MoritzMaxeiner Yea thank you for the suggestion I will check that everyday from now on.   

---

### 评论 #98 — Syntax3rror404 (2023-03-16T17:29:52Z)

> @Mushoz Yea i bought the gpu and right then ai image creation and chat gpt and all that stuff kicked in. And i took interest in ai image generation becaue i saw how good it had become and now i am sitting here running directml version of stablediffusion at 20+s/it if i want to go above 512x512. Its frustrating i have a for me 1300€ card and i am waiting 5+ months for drivers.

If amd sleeps through this, no one will buy amd graphics cards for machine learning in 1 to 2 years. Then they will lose the rest of the ml market to nvidia. 

With nvidia I buy a gpu and I do not care cuda always runs!!! 

So it is absolutely incomprehensible to me why amd is acting like this! Documentation totally unclear you have to search for hours just to see which graphics cards supports rocm and the latest graphics cards do not even get a driver after 5 months. 

---

### 评论 #99 — Kademo15 (2023-03-16T19:20:24Z)

@Syntax3rror404 its like that and then add to it that its only linux so all of windows user need to use vms or a different op

---

### 评论 #100 — Hamblok0 (2023-03-16T19:21:07Z)

> now i am sitting here running directml version of stablediffusion at 20+s/it if i want to go above 512x512

I recently starting using the directML version of AUTOMATIC's stable diffusion web ui and I'm only able to get 1.5 it/s at best using a 7900XT. What arguments/settings are you using to achieve this? 

---
