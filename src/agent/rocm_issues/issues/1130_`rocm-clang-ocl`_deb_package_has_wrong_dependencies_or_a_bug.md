# `rocm-clang-ocl` deb package has wrong dependencies or a bug

> **Issue #1130**
> **状态**: closed
> **创建时间**: 2020-06-04T14:08:42Z
> **更新时间**: 2020-12-09T07:21:47Z
> **关闭时间**: 2020-12-09T07:21:47Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1130

## 描述

```
$ /opt/rocm-3.5.0/bin/clang-ocl
/opt/rocm-3.5.0/bin/clang-ocl: line 37: /opt/rocm-3.5.0/llvm/bin/clang: No such file or directory
$
```

```
$ apt show rocm-clang-ocl
Package: rocm-clang-ocl
Version: 0.5.0.51-rocm-rel-3.5-30-74b3b81
Priority: optional
Section: devel
Maintainer: Paul Fultz II <paul.fultz@amd.com>
Installed-Size: 15.4 kB
Depends: rocm-opencl-dev
Download-Size: 1,616 B
APT-Manual-Installed: no
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: OpenCL compilation with clang compiler.
```

I don't know where, but no package provide `/opt/rocm-3.5.0/llvm/bin/clang` file.


---

## 评论 (11 条)

### 评论 #1 — Hurricane31337 (2020-06-11T01:41:11Z)

I also have the same problem and a fix or at least a temporary solution like providing the binaries here would be highly appreciated. Without clang-ocl, not even the simple TensorFlow benchmark (https://github.com/tensorflow/benchmarks) can be run:
```
INFO:tensorflow:Running local_init_op.
I0611 02:46:32.544585 139791440680768 session_manager.py:505] Running local_init_op.
INFO:tensorflow:Done running local_init_op.
I0611 02:46:32.645938 139791440680768 session_manager.py:508] Done running local_init_op.
Running warm up
2020-06-11 02:46:33.707456: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-06-11 02:46:33.918845: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
MIOpen(HIP): Error [ValidateGcnAssemblerImpl] Wrong path to assembler: '/opt/rocm/llvm/bin/clang'. Expect performance degradation.
/opt/rocm-3.5.0/bin/clang-ocl: Zeile 37: /opt/rocm-3.5.0/llvm/bin/clang: Datei oder Verzeichnis nicht gefunden
MIOpen Error: /root/driver/MLOpen/src/tmp_dir.cpp:47: Can't execute cd /tmp/miopen-MIOpenConvDirUni.cl-6338-a1df-125f-3c5a; /opt/rocm-3.5.0/bin/clang-ocl  -DMLO_HW_WAVE_SZ=64 -DMLO_DIR_FORWARD=1 -DMLO_FILTER_SIZE0=7 -DMLO_FILTER_SIZE1=7 -DMLO_FILTER_PAD0=0 -DMLO_FILTER_PAD1=0 -DMLO_FILTER_STRIDE0=2 -DMLO_FILTER_STRIDE1=2 -DMLO_N_OUTPUTS=64 -DMLO_N_INPUTS=3 -DMLO_BATCH_SZ=128 -DMLO_OUT_WIDTH=112 -DMLO_OUT_HEIGHT=112 -DMLO_OUT_BATCH_STRIDE=802816 -DMLO_OUT_CHANNEL_STRIDE=12544 -DMLO_OUT_STRIDE=112 -DMLO_IN_WIDTH=230 -DMLO_IN_HEIGHT=230 -DMLO_IN_BATCH_STRIDE=158700 -DMLO_IN_CHANNEL_STRIDE=52900 -DMLO_IN_STRIDE=230 -DMLO_IN_TILE0=16 -DMLO_IN_TILE1=16 -DMLO_GRP_TILE0=8 -DMLO_GRP_TILE1=16 -DMLO_OUT_TILE0=2 -DMLO_OUT_TILE1=1 -DMLO_N_STACKS=1 -DMLO_N_OUT_TILES=8 -DMLO_N_OUT_TILES_PERSTACK=8 -DMLO_N_IN_TILES_PERSTACK=1 -DMLO_N_READ_PROCS=128 -DMLO_ALU_VTILE0=8 -DMLO_ALU_VTILE1=16 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_INT8=0 -DMIOPEN_USE_INT8x4=0 -DMIOPEN_USE_BFP16=0 -DMIOPEN_USE_INT32=0 -DMIOPEN_USE_RNE_BFLOAT16=1 -DMLO_CONV_BIAS=0 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_INT8=0 -DMIOPEN_USE_INT8x4=0 -DMIOPEN_USE_BFP16=0 -DMIOPEN_USE_INT32=0 -DMIOPEN_USE_RNE_BFLOAT16=1 -mcpu=gfx906 -Wno-everything  MIOpenConvDirUni.cl -o /tmp/miopen-MIOpenConvDirUni.cl-6338-a1df-125f-3c5a/MIOpenConvDirUni.cl.o
2020-06-11 02:46:34.102884: F tensorflow/stream_executor/rocm/rocm_dnn.cc:3248] call to miopenConvolutionForwardCompileSolution failed: miopenStatusUnknownError
Fatal Python error: Aborted
```

It could also explain why Blender (optimized Linux version from the website) crashes when trying to render using the GPU (needs to compile a render kernel), but I haven't validated this in the logs.

---

### 评论 #2 — Laggger164 (2020-07-22T13:06:43Z)

The problem seems to be that clang was not installed at all or was incorrectly installed for some reason.

I managed to solve that problem following the official installation guide here: 
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

By following the build HIP-clang manually section:

git clone -b rocm-3.5.x https://github.com/RadeonOpenCompute/llvm-project.git
cd llvm-project
mkdir -p build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/llvm -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=1 -DLLVM_TARGETS_TO_BUILD="AMDGPU;X86" -DLLVM_ENABLE_PROJECTS="clang;lld;compiler-rt" ../llvm
make -j
sudo make install

Look out for the make -j, when I let it run on my server it chewed up all the 16GB of memory like it was nothing and the OS started to kill the compiler's processes.
I found that the best workaround was to set it to -j4 (or -j8 if you have a CPU with 8 threads, or -jn with n threads, you get the idea)

It took a little long to compile but that might be because of the weak CPU.


This revealed another problem when I tried testing ROCm through the tf_cnn_benchmarks.py from the official TensorFlow github page (it's an old one)

I came to have the same error as Mathieu Poliquin at the end of his video: https://www.youtube.com/watch?v=9a47-nCZ1MA

Others seem to have the same problem too and it seems to be a recurring problem throughout many versions

#869 

<details>
  <summary>My console error output</summary>
~/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks$ sudo python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50 --variable_update=parameter
WARNING:tensorflow:From /home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/compat/v2_compat.py:96: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
FATAL Flags parsing error: flag --variable_update=parameter: value should be one of <parameter_server|replicated|distributed_replicated|independent|distributed_all_reduce|collective_all_reduce|horovod>
Pass --helpshort or --helpfull to see help on flags.
uniteq@uniteq-franks:~/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks$ sudo python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50
WARNING:tensorflow:From /home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/compat/v2_compat.py:96: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
2020-07-22 14:48:29.146386: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2
2020-07-22 14:48:29.170899: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3499910000 Hz
2020-07-22 14:48:29.170995: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x46ff2a0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-07-22 14:48:29.171009: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-07-22 14:48:29.172214: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-07-22 14:48:30.268666: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x4708df0 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-07-22 14:48:30.268689: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 10 XT [Radeon RX Vega 64], AMDGPU ISA version: gfx900
2020-07-22 14:48:30.268694: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (1): Vega 10 XT [Radeon RX Vega 64], AMDGPU ISA version: gfx900
2020-07-22 14:48:30.268822: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties:
pciBusID: 0000:03:00.0 name: Vega 10 XT [Radeon RX Vega 64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.63GHz coreCount: 64 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-07-22 14:48:30.268864: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 1 with properties:
pciBusID: 0000:0a:00.0 name: Vega 10 XT [Radeon RX Vega 64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.63GHz coreCount: 64 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-07-22 14:48:30.587772: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-07-22 14:48:30.588692: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-07-22 14:48:31.021245: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-07-22 14:48:31.023162: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-07-22 14:48:31.023321: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0, 1
2020-07-22 14:48:31.023345: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-07-22 14:48:31.023354: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 1
2020-07-22 14:48:31.023362: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N Y
2020-07-22 14:48:31.023369: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 1:   Y N
2020-07-22 14:48:31.023505: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7384 MB memory) -> physical GPU (device: 0, name: Vega 10 XT [Radeon RX Vega 64], pci bus id: 0000:03:00.0)
2020-07-22 14:48:31.317782: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:1 with 7384 MB memory) -> physical GPU (device: 1, name: Vega 10 XT [Radeon RX Vega 64], pci bus id: 0000:0a:00.0)
TensorFlow:  2.2
Model:       resnet50
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
WARNING:tensorflow:From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:134: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
W0722 14:48:31.623008 140710254581568 deprecation.py:323] From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:134: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
WARNING:tensorflow:From /home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer_v1) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
W0722 14:48:31.627437 140710254581568 deprecation.py:323] From /home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer_v1) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
WARNING:tensorflow:From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:266: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
W0722 14:48:31.654390 140710254581568 deprecation.py:323] From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:266: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
Initializing graph
WARNING:tensorflow:From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2268: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
W0722 14:48:33.651320 140710254581568 deprecation.py:323] From /home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2268: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
2020-07-22 14:48:33.897377: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties:
pciBusID: 0000:03:00.0 name: Vega 10 XT [Radeon RX Vega 64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.63GHz coreCount: 64 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-07-22 14:48:33.897448: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 1 with properties:
pciBusID: 0000:0a:00.0 name: Vega 10 XT [Radeon RX Vega 64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.63GHz coreCount: 64 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-07-22 14:48:33.897484: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-07-22 14:48:33.897501: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-07-22 14:48:33.897516: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-07-22 14:48:33.897550: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-07-22 14:48:33.897696: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0, 1
2020-07-22 14:48:33.897713: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-07-22 14:48:33.897718: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 1
2020-07-22 14:48:33.897722: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N Y
2020-07-22 14:48:33.897726: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 1:   Y N
2020-07-22 14:48:33.897844: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7384 MB memory) -> physical GPU (device: 0, name: Vega 10 XT [Radeon RX Vega 64], pci bus id: 0000:03:00.0)
2020-07-22 14:48:33.897963: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:1 with 7384 MB memory) -> physical GPU (device: 1, name: Vega 10 XT [Radeon RX Vega 64], pci bus id: 0000:0a:00.0)
INFO:tensorflow:Running local_init_op.
I0722 14:48:34.541863 140710254581568 session_manager.py:505] Running local_init_op.
INFO:tensorflow:Done running local_init_op.
I0722 14:48:34.595754 140710254581568 session_manager.py:508] Done running local_init_op.
Running warm up
2020-07-22 14:48:35.584903: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-07-22 14:48:35.718963: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
LLVM ERROR: Attempting to emit BUFFER_ATOMIC_ADD_F32_OFFEN_vi instruction but the Feature_HasAtomicFaddInsts predicate(s) are not met
PLEASE submit a bug report to https://bugs.llvm.org/ and include the crash backtrace.
Stack dump:
0.      Program arguments: /opt/rocm-3.5.0/llvm/bin/llc /tmp/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw-c69f18-gfx900-optimized-848c5f.bc -O3 -mtriple=amdgcn-amd-amdhsa -mcpu=gfx900 -filetype=obj -amdgpu-early-inline-all=true -amdgpu-function-calls=false -amdgpu-enable-global-sgpr-addr --amdgpu-spill-vgpr-to-agpr=0 -o /tmp/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw-c69f18-gfx900-6d1de7.o
1.      Running pass 'CallGraph Pass Manager' on module '/tmp/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw-c69f18-gfx900-optimized-848c5f.bc'.
2.      Running pass 'AMDGPU Assembly Printer' on function '@_ZN2ck31amd_intrinsic_buffer_atomic_addIfLi1EEEvPKT_PS1_ii'
 #0 0x000055b1db98dbaa llvm::sys::PrintStackTrace(llvm::raw_ostream&) (/opt/rocm-3.5.0/llvm/bin/llc+0x1a37baa)
 #1 0x000055b1db98b724 llvm::sys::RunSignalHandlers() (/opt/rocm-3.5.0/llvm/bin/llc+0x1a35724)
 #2 0x000055b1db98b873 SignalHandler(int) (/opt/rocm-3.5.0/llvm/bin/llc+0x1a35873)
 #3 0x00007f3b1ea9c8a0 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x128a0)
 #4 0x00007f3b1d74df47 raise /build/glibc-2ORdQG/glibc-2.27/signal/../sysdeps/unix/sysv/linux/raise.c:51:0
 #5 0x00007f3b1d74f8b1 abort /build/glibc-2ORdQG/glibc-2.27/stdlib/abort.c:81:0
 #6 0x000055b1db906bbe llvm::report_fatal_error(llvm::Twine const&, bool) (/opt/rocm-3.5.0/llvm/bin/llc+0x19b0bbe)
 #7 0x000055b1db906d1e (/opt/rocm-3.5.0/llvm/bin/llc+0x19b0d1e)
 #8 0x000055b1daa55046 llvm::AMDGPUMCCodeEmitter::verifyInstructionPredicates(llvm::MCInst const&, llvm::FeatureBitset const&) const (/opt/rocm-3.5.0/llvm/bin/llc+0xaff046)
 #9 0x000055b1daa5512b (anonymous namespace)::SIMCCodeEmitter::encodeInstruction(llvm::MCInst const&, llvm::raw_ostream&, llvm::SmallVectorImpl<llvm::MCFixup>&, llvm::MCSubtargetInfo const&) const (/opt/rocm-3.5.0/llvm/bin/llc+0xaff12b)
#10 0x000055b1db349a13 llvm::MCELFStreamer::EmitInstToData(llvm::MCInst const&, llvm::MCSubtargetInfo const&) (/opt/rocm-3.5.0/llvm/bin/llc+0x13f3a13)
#11 0x000055b1db361eae llvm::MCObjectStreamer::emitInstructionImpl(llvm::MCInst const&, llvm::MCSubtargetInfo const&) (/opt/rocm-3.5.0/llvm/bin/llc+0x140beae)
#12 0x000055b1db361f19 llvm::MCObjectStreamer::emitInstruction(llvm::MCInst const&, llvm::MCSubtargetInfo const&) (/opt/rocm-3.5.0/llvm/bin/llc+0x140bf19)
#13 0x000055b1da53d26f llvm::AMDGPUAsmPrinter::emitInstruction(llvm::MachineInstr const*) (/opt/rocm-3.5.0/llvm/bin/llc+0x5e726f)
#14 0x000055b1dac942af llvm::AsmPrinter::emitFunctionBody() (/opt/rocm-3.5.0/llvm/bin/llc+0xd3e2af)
#15 0x000055b1da52a05c llvm::AMDGPUAsmPrinter::runOnMachineFunction(llvm::MachineFunction&) (/opt/rocm-3.5.0/llvm/bin/llc+0x5d405c)
#16 0x000055b1dae99d3e llvm::MachineFunctionPass::runOnFunction(llvm::Function&) (/opt/rocm-3.5.0/llvm/bin/llc+0xf43d3e)
#17 0x000055b1db295311 llvm::FPPassManager::runOnFunction(llvm::Function&) (/opt/rocm-3.5.0/llvm/bin/llc+0x133f311)
#18 0x000055b1daaea16a (anonymous namespace)::CGPassManager::runOnModule(llvm::Module&) (/opt/rocm-3.5.0/llvm/bin/llc+0xb9416a)
#19 0x000055b1db2961a1 llvm::legacy::PassManagerImpl::run(llvm::Module&) (/opt/rocm-3.5.0/llvm/bin/llc+0x13401a1)
#20 0x000055b1da4e16ec compileModule(char**, llvm::LLVMContext&) (/opt/rocm-3.5.0/llvm/bin/llc+0x58b6ec)
#21 0x000055b1da474126 main (/opt/rocm-3.5.0/llvm/bin/llc+0x51e126)
#22 0x00007f3b1d730b97 __libc_start_main /build/glibc-2ORdQG/glibc-2.27/csu/../csu/libc-start.c:344:0
#23 0x000055b1da4daf9a _start (/opt/rocm-3.5.0/llvm/bin/llc+0x584f9a)
clang-11: error: unable to execute command: Aborted (core dumped)
clang-11: error: amdgcn-link command failed due to signal (use -v to see invocation)
clang version 11.0.0 (https://github.com/RadeonOpenCompute/llvm-project.git 0383ad1cfb0a8e05b0a020e8632400194628b243)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-3.5.0/llvm/bin
clang-11: note: diagnostic msg:
********************

PLEASE ATTACH THE FOLLOWING FILES TO THE BUG REPORT:
Preprocessed source(s) and associated run script(s) are located at:
clang-11: note: diagnostic msg: /tmp/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw-4add9e.cu
clang-11: note: diagnostic msg: /tmp/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw-4add9e.sh
clang-11: note: diagnostic msg:

********************
MIOpen Error: /root/driver/MLOpen/src/tmp_dir.cpp:47: Can't execute cd /tmp/miopen-gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw.cpp-2732-dac2-050e-fffe;  /opt/rocm-3.5.0/llvm/bin/clang++  -std=c++14  -DCK_PARAM_PROBLEM_N=32 -DCK_PARAM_PROBLEM_K=256 -DCK_PARAM_PROBLEM_C=64 -DCK_PARAM_PROBLEM_HI=56 -DCK_PARAM_PROBLEM_WI=56 -DCK_PARAM_PROBLEM_HO=56 -DCK_PARAM_PROBLEM_WO=56 -DCK_PARAM_PROBLEM_Y=1 -DCK_PARAM_PROBLEM_X=1 -DCK_PARAM_PROBLEM_CONV_STRIDE_H=1 -DCK_PARAM_PROBLEM_CONV_STRIDE_W=1 -DCK_PARAM_PROBLEM_CONV_DILATION_H=1 -DCK_PARAM_PROBLEM_CONV_DILATION_W=1 -DCK_PARAM_PROBLEM_IN_LEFT_PAD_H=0 -DCK_PARAM_PROBLEM_IN_LEFT_PAD_W=0 -DCK_PARAM_PROBLEM_IN_RIGHT_PAD_H=0 -DCK_PARAM_PROBLEM_IN_RIGHT_PAD_W=0 -DCK_PARAM_PROBLEM_CONV_DIRECTION_FORWARD=1 -DCK_PARAM_PROBLEM_CONV_DIRECTION_BACKWARD_DATA=0 -DCK_PARAM_PROBLEM_CONV_DIRECTION_BACKWARD_WEIGHT=0 -DCK_PARAM_TUNABLE_BLOCK_SIZE=256 -DCK_PARAM_TUNABLE_GEMM_M_PER_BLOCK=128 -DCK_PARAM_TUNABLE_GEMM_N_PER_BLOCK=128 -DCK_PARAM_TUNABLE_GEMM_K_PER_BLOCK=16 -DCK_PARAM_TUNABLE_GEMM_M_PER_THREAD=4 -DCK_PARAM_TUNABLE_GEMM_N_PER_THREAD=4 -DCK_PARAM_TUNABLE_GEMM_M_LEVEL0_CLUSTER=4 -DCK_PARAM_TUNABLE_GEMM_N_LEVEL0_CLUSTER=4 -DCK_PARAM_TUNABLE_GEMM_M_LEVEL1_CLUSTER=4 -DCK_PARAM_TUNABLE_GEMM_N_LEVEL1_CLUSTER=4 -DCK_PARAM_TUNABLE_GEMM_A_BLOCK_COPY_CLUSTER_LENGTHS_GEMM_K=4 -DCK_PARAM_TUNABLE_GEMM_A_BLOCK_COPY_CLUSTER_LENGTHS_GEMM_M=64 -DCK_PARAM_TUNABLE_GEMM_A_BLOCK_COPY_SRC_DATA_PER_READ_GEMM_K=4 -DCK_PARAM_TUNABLE_GEMM_A_BLOCK_COPY_DST_DATA_PER_WRITE_GEMM_M=2 -DCK_PARAM_TUNABLE_GEMM_B_BLOCK_COPY_CLUSTER_LENGTHS_GEMM_K=8 -DCK_PARAM_TUNABLE_GEMM_B_BLOCK_COPY_CLUSTER_LENGTHS_GEMM_N=32 -DCK_PARAM_TUNABLE_GEMM_B_BLOCK_COPY_SRC_DATA_PER_READ_GEMM_N=4 -DCK_PARAM_TUNABLE_GEMM_B_BLOCK_COPY_DST_DATA_PER_WRITE_GEMM_N=4 -DCK_PARAM_TUNABLE_GEMM_C_THREAD_COPY_DST_DATA_PER_WRITE_GEMM_N1=4 -DCK_PARAM_DEPENDENT_GRID_SIZE=1568 -DCK_THREADWISE_GEMM_USE_AMD_INLINE_ASM=1 -DCK_USE_AMD_INLINE_ASM=1 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_INT8=0 -DMIOPEN_USE_INT8x4=0 -DMIOPEN_USE_BFP16=0 -DMIOPEN_USE_INT32=0 -DMIOPEN_USE_RNE_BFLOAT16=1 -mcpu=gfx900 -Wno-everything --cuda-gpu-arch=gfx900 --cuda-device-only -c -O3  -Wno-unused-command-line-argument -I. -x hip --hip-device-lib-path=/opt/rocm/lib -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -D__HIP_ROCclr__=1 -isystem /opt/rocm-3.5.0/hip/../include -isystem /opt/rocm-3.5.0/llvm/lib/clang/11.0.0/include/.. -D__HIP_PLATFORM_HCC__=1 -D__HIP_ROCclr__=1 -isystem /opt/rocm-3.5.0/hip/include -isystem /opt/rocm/include --hip-device-lib-path=/opt/rocm/lib --hip-link -mllvm -amdgpu-enable-global-sgpr-addr -mllvm --amdgpu-spill-vgpr-to-agpr=0 gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw.cpp -o /tmp/miopen-gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw.cpp-2732-dac2-050e-fffe/gridwise_convolution_implicit_gemm_v4r4_nchw_kcyx_nkhw.cpp.o
2020-07-22 14:48:42.371011: F tensorflow/stream_executor/rocm/rocm_dnn.cc:3248] call to miopenConvolutionForwardCompileSolution failed: miopenStatusUnknownError
Fatal Python error: Aborted

Thread 0x00007ff9a8bd9740 (most recent call first):
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1443 in _call_tf_sessionrun
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1350 in _run_fn
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1365 in _do_call
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1359 in _do_run
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1181 in _run
  File "/home/uniteq/.local/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 958 in run
  File "/home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 870 in benchmark_one_step
  File "/home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 2433 in benchmark_with_session
  File "/home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 2295 in _benchmark_graph
  File "/home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 2088 in _benchmark_train
  File "/home/uniteq/Projects/tutorials/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 1883 in run
  File "tf_cnn_benchmarks.py", line 68 in main
  File "/home/uniteq/.local/lib/python3.6/site-packages/absl/app.py", line 250 in _run_main
  File "/home/uniteq/.local/lib/python3.6/site-packages/absl/app.py", line 299 in run
  File "tf_cnn_benchmarks.py", line 73 in <module>
Aborted
</details>

I am really running out of ideas but I am hoping I helped you at least a little.

---

### 评论 #3 — baryluk (2020-07-22T14:04:53Z)

@Laggger164 Sure, but it is not a fix to the problem in reported this issue.

The problem here is the package has incorrect dependencies. No amount of work or workarounds by me will fix that.

---

### 评论 #4 — Hurricane31337 (2020-07-22T14:26:25Z)

@Laggger164 Yes, I also fixed it by manually compiling any missing dependencies and copying them into their respective paths. But just a day later, another apt update damaged the installation again... That's why we decided to just sell all of our Radeon VIIs and instead switch to Nvidia GPUs to be productive again.

Personally, I really hope that AMD will put more effort into its ML-related releases (e.g. by just running them on a new Ubuntu VM before release, writing better guides, and carefully monitoring the performance impact for each release).
I will continue to monitor the ROCm issue situation and would be happy to initiate a switch back if AMD GPUs can be used for ML without any major problems.

---

### 评论 #5 — Laggger164 (2020-07-22T14:35:49Z)

> @Laggger164 Sure, but it is not a fix to the problem in reported this issue.
> 
> The problem here is the package has incorrect dependencies. No amount of work or workarounds by me will fix that.

It is indeed more like a temporary patch to just get on with it for a while rather than a fix.
I am just throwing it here since it might help someone for a little bit.

AMD really does need to work on this a lot more, this ROCm system is really underwhelming, nothing but problems.

---

### 评论 #6 — baryluk (2020-09-22T20:01:12Z)

Still broken in rocm 3.8.0.



---

### 评论 #7 — Laggger164 (2020-09-22T20:25:38Z)

> Still broken in rocm 3.8.0.

What OS do you have and what drivers are you using?

---

### 评论 #8 — baryluk (2020-09-22T21:00:44Z)

> > Still broken in rocm 3.8.0.
> 
> What OS do you have and what drivers are you using?

It doesn't matter. The control file in the package is incorrect.

---

### 评论 #9 — pfultz2 (2020-09-22T22:48:16Z)

Clang-ocl package depends on rocm-opencl, but as opencl now uses comgr to compile instead of the compiler, the compiler is no longer provided as a dependency of opencl. Here is PR to fix that: 

https://github.com/RadeonOpenCompute/clang-ocl/pull/32

---

### 评论 #10 — baryluk (2020-09-22T22:53:14Z)

@pfultz2 Thank you.


---

### 评论 #11 — baryluk (2020-12-09T07:21:47Z)

The fix was merged. Closing.

---
