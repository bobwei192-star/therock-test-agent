# Pytorch Docker build complete but error running my code

> **Issue #972**
> **状态**: closed
> **创建时间**: 2019-12-18T10:46:41Z
> **更新时间**: 2020-01-14T02:34:40Z
> **关闭时间**: 2020-01-14T02:34:40Z
> **作者**: se11en
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/972

## 描述

```
Stack dump:
0.	Program arguments: /opt/rocm/hcc/bin/llc -mtriple amdgcn-amd-amdhsa -mcpu=gfx906 -mattr=-code-object-v3 -O3 -mattr=+enable-ds128 -mattr=+sram-ecc -amdgpu-function-calls=0 -filetype=obj -o /tmp/tmp.Hs1ZTry9XT/kernel-gfx906.hsaco.isabin /tmp/tmp.Hs1ZTry9XT/kernel-gfx906.hsaco.opt.bc 
1.	Running pass 'CallGraph Pass Manager' on module '/tmp/tmp.Hs1ZTry9XT/kernel-gfx906.hsaco.opt.bc'.
2.	Running pass 'Greedy Register Allocator' on function '@gridwise_convolution_implicit_gemm_v4_nchw_kcyx_nkhw_lds_double_buffer'
 #0 0x000000000183867a llvm::sys::PrintStackTrace(llvm::raw_ostream&) (/opt/rocm/hcc/bin/llc+0x183867a)
 #1 0x00000000018364fc llvm::sys::RunSignalHandlers() (/opt/rocm/hcc/bin/llc+0x18364fc)
 #2 0x0000000001836669 SignalHandler(int) (/opt/rocm/hcc/bin/llc+0x1836669)
 #3 0x00007f60effc7890 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x12890)
 #4 0x00000000010fc10a llvm::VirtRegAuxInfo::weightCalcHelper(llvm::LiveInterval&, llvm::SlotIndex*, llvm::SlotIndex*) (/opt/rocm/hcc/bin/llc+0x10fc10a)
 #5 0x00000000010fd17d llvm::VirtRegAuxInfo::calculateSpillWeightAndHint(llvm::LiveInterval&) (/opt/rocm/hcc/bin/llc+0x10fd17d)
 #6 0x00000000010fd267 llvm::calculateSpillWeightsAndHints(llvm::LiveIntervals&, llvm::MachineFunction&, llvm::VirtRegMap*, llvm::MachineLoopInfo const&, llvm::MachineBlockFrequencyInfo const&, float (*)(float, unsigned int, unsigned int)) (/opt/rocm/hcc/bin/llc+0x10fd267)
 #7 0x0000000000ff44a8 (anonymous namespace)::RAGreedy::runOnMachineFunction(llvm::MachineFunction&) (/opt/rocm/hcc/bin/llc+0xff44a8)
 #8 0x0000000000f0e47a llvm::MachineFunctionPass::runOnFunction(llvm::Function&) (.part.38.constprop.39) (/opt/rocm/hcc/bin/llc+0xf0e47a)
 #9 0x00000000012359cf llvm::FPPassManager::runOnFunction(llvm::Function&) (/opt/rocm/hcc/bin/llc+0x12359cf)
#10 0x0000000000bf8aa7 (anonymous namespace)::CGPassManager::runOnModule(llvm::Module&) (/opt/rocm/hcc/bin/llc+0xbf8aa7)
#11 0x000000000123699b llvm::legacy::PassManagerImpl::run(llvm::Module&) (/opt/rocm/hcc/bin/llc+0x123699b)
#12 0x0000000000709883 compileModule(char**, llvm::LLVMContext&) (.constprop.440) (/opt/rocm/hcc/bin/llc+0x709883)
#13 0x00000000006a0cf5 main (/opt/rocm/hcc/bin/llc+0x6a0cf5)
#14 0x00007f60eec5bb97 __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b97)
#15 0x00000000006fbdf9 _start (/opt/rocm/hcc/bin/llc+0x6fbdf9)
/opt/rocm/hcc/bin/clamp-device: line 259:  1955 Segmentation fault      (core dumped) $LLC -mtriple amdgcn-amd-amdhsa -mcpu=$AMDGPU_TARGET $CODE_OBJECT_FORMAT $HCC_OPT $KMOPTLLC -amdgpu-function-calls=$AMDGPU_FUNC_CALLS -filetype=obj -o $2.isabin $2.opt.bc
Generating AMD GCN kernel failed in llc for target: gfx906
clang-10: error: linker command failed with exit code 139 (use -v to see invocation)
MIOpen Error: /root/driver/MLOpen/src/tmp_dir.cpp:18: Can't execute cd /tmp/miopen-gridwise_convolution_implicit_gemm_v4_nchw_kcyx_nkhw_lds_double_buffer.cpp-bf53-b7c6-99dc-f6d8; KMOPTLLC=-mattr=+enable-ds128 /opt/rocm/hcc/bin/hcc  -std=c++14 -DCK_PARAM_PROBLEM_N=8 -DCK_PARAM_PROBLEM_K=16 -DCK_PARAM_PROBLEM_C=128 -DCK_PARAM_PROBLEM_HI=64 -DCK_PARAM_PROBLEM_WI=64 -DCK_PARAM_PROBLEM_HO=64 -DCK_PARAM_PROBLEM_WO=64 -DCK_PARAM_PROBLEM_Y=1 -DCK_PARAM_PROBLEM_X=1 -DCK_PARAM_PROBLEM_CONV_STRIDE_H=1 -DCK_PARAM_PROBLEM_CONV_STRIDE_W=1 -DCK_PARAM_PROBLEM_CONV_DILATION_H=1 -DCK_PARAM_PROBLEM_CONV_DILATION_W=1 -DCK_PARAM_TUNABLE_BLOCK_SIZE=64 -DCK_PARAM_TUNABLE_B_PER_BLOCK=16 -DCK_PARAM_TUNABLE_K_PER_BLOCK=16 -DCK_PARAM_TUNABLE_E_PER_BLOCK=4 -DCK_PARAM_DEPENDENT_GRID_SIZE=512 -DCK_PARAM_GEMM_N_REPEAT=2 -DCK_PARAM_GEMM_M_PER_THREAD_SUB_C=2 -DCK_PARAM_GEMM_N_PER_THREAD_SUB_C=2 -DCK_PARAM_GEMM_M_LEVEL0_CLUSTER=2 -DCK_PARAM_GEMM_N_LEVEL0_CLUSTER=4 -DCK_PARAM_GEMM_M_LEVEL1_CLUSTER=2 -DCK_PARAM_GEMM_N_LEVEL1_CLUSTER=4 -DCK_PARAM_IN_BLOCK_COPY_CLUSTER_LENGTHS_E=4 -DCK_PARAM_IN_BLOCK_COPY_CLUSTER_LENGTHS_N1=1 -DCK_PARAM_IN_BLOCK_COPY_CLUSTER_LENGTHS_B=16 -DCK_PARAM_IN_BLOCK_COPY_CLUSTER_LENGTHS_N2=1 -DCK_PARAM_IN_BLOCK_COPY_SRC_DATA_PER_READ_B=1 -DCK_PARAM_IN_BLOCK_COPY_DST_DATA_PER_WRITE_N2=2 -DCK_PARAM_WEI_BLOCK_COPY_CLUSTER_LENGTHS_E=4 -DCK_PARAM_WEI_BLOCK_COPY_CLUSTER_LENGTHS_K=16 -DCK_PARAM_WEI_BLOCK_COPY_SRC_DATE_PER_READ_E=1 -DCK_PARAM_WEI_BLOCK_COPY_DST_DATE_PER_WRITE_K=1 -DCK_BLOCKWISE_GEMM_USE_AMD_INLINE_ASM=1 -D__HIP_PLATFORM_HCC__=1 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_INT8=0 -DMIOPEN_USE_INT8x4=0 -DMIOPEN_USE_BFP16=0 -DMIOPEN_USE_INT32=0 -DMIOPEN_USE_RNE_BFLOAT16=1 -mcpu=gfx906 -Wno-everything -amdgpu-target=gfx906 -Wno-unused-command-line-argument -I. -isystem /opt/rocm/hip/include -isystem /opt/rocm/hsa/include -hc -hc -L /opt/rocm/lib -Wl,-rpath /opt/rocm/lib -Wl,--whole-archive -hc -fPIC -isystem /opt/rocm/include -isystem /opt/rocm/include -ldl -Wl,--no-whole-archive -ldl -lm -hc -fPIC -isystem /opt/rocm/include -isystem /opt/rocm/include gridwise_convolution_implicit_gemm_v4_nchw_kcyx_nkhw_lds_double_buffer.cpp -o /tmp/miopen-gridwise_convolution_implicit_gemm_v4_nchw_kcyx_nkhw_lds_double_buffer.cpp-bf53-b7c6-99dc-f6d8/gridwise_convolution_implicit_gemm_v4_nchw_kcyx_nkhw_lds_double_buffer.cpp.o
Traceback (most recent call last):
  File "main.py", line 136, in <module>
    train(epoch)
  File "main.py", line 68, in train
    prediction = model(input, neigbor)
  File "/root/.local/lib/python3.6/site-packages/torch/nn/modules/module.py", line 539, in __call__
    result = self.forward(*input, **kwargs)
  File "/data/12thDec_lowfusion_modified/rbpn.py", line 146, in forward
    output = self.conv2(output)
  File "/root/.local/lib/python3.6/site-packages/torch/nn/modules/module.py", line 539, in __call__
    result = self.forward(*input, **kwargs)
  File "/root/.local/lib/python3.6/site-packages/torch/nn/modules/conv.py", line 345, in forward
    return self._conv_forward(input, self.weight)
  File "/root/.local/lib/python3.6/site-packages/torch/nn/modules/conv.py", line 342, in _conv_forward
    self.padding, self.dilation, self.groups)
RuntimeError: miopenStatusUnknownError
```
the host is Ubuntu18.04 with a RADEON VII GPU, after docker installation(pulled rocm2.10_ubuntu18.04_py3.6_pytorch_profiling) and builded successfully, when I ran my code, error occured, I cannot figure out why.

---

## 评论 (4 条)

### 评论 #1 — IceFlowerLi (2019-12-23T01:47:39Z)

Please check your physical memory fistly. This error will happen if the memory is not enough for your program. Try insert more memory-chips in your machine.

---

### 评论 #2 — se11en (2019-12-23T02:58:29Z)

> Please check your physical memory fistly. This error will happen if the memory is not enough for your program. Try insert more memory-chips in your machine.

I have 64GB ram which is limited by the motherboard.
After I changed the batch size of training, strange things happened: batch = 4 or = 12 is OK,but crashed when batch=8

---

### 评论 #3 — searlmc1 (2020-01-13T23:10:18Z)

Hi,

Could you please let me know if this is reproducible with ROCm 3.0 ?

Thanks


---

### 评论 #4 — se11en (2020-01-14T02:32:11Z)

> Hi,
> 
> Could you please let me know if this is reproducible with ROCm 3.0 ?
> 
> Thanks

Ever since I updated to ROCM3.0 the problem never happened again.
Thank you for your attention.

---
