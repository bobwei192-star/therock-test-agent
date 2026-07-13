# [Issue]: ROCM5.7.3, RCCL2.19.4 GPU kernel can't printf。 Hash value collision detected

- **Issue #:** 3001
- **State:** closed
- **Created:** 2024-04-09T05:07:47Z
- **Updated:** 2024-10-01T20:02:30Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 5.7.0
- **URL:** https://github.com/ROCm/ROCm/issues/3001

### Problem Description
In the rccl file prims_simple.h，I have added a section of printf in this kernel function， such as :

> __device__ __forceinline__ void genericOp(
>       intptr_t srcIx, intptr_t dstIx, int nelem, bool postOp
>     ) {
>     constexpr int DirectRecv = /*1 &&*/ Direct && DirectRecv1;
>     constexpr int DirectSend = /*1 &&*/ Direct && DirectSend1;
>     constexpr int Src = SrcBuf != -1;
>     constexpr int Dst = DstBuf != -1;
>     nelem = nelem < 0 ? 0 : nelem;
>     int sliceSize = stepSize*StepPerSlice;
>     sliceSize = max(divUp(nelem, 16*SlicePerChunk)*16, sliceSize/32);
>     int slice = 0;
>     int offset = 0;
>     if(tid == 0) {
>         printf("in genericOp \n");
>     }
> 


**when i run rccl test,  Use this command ./build/sendrecv_perf -b 8 -e 128M -f 2 -t 1 -g 2，will report this error：** 


> enquence.cc Current function: ncclLaunchKernel line 1090
> :1:rocvirtual.cpp           :2945: 74877529363 us: [pid:44406 tid:0x7f26f4922c00] Pcie atomics not enabled, hostcall not supported
> :1:rocvirtual.cpp           :3280: 74877529375 us: [pid:44406 tid:0x7f26f4922c00] AQL dispatch failed!
> yz-adm3: Test NCCL failure /home/yang.yang/yy/work/test-rccl/build/src/hipify/common.cu.cpp:451 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '


After seeing the explanation here  https://rocm.docs.amd.com/en/latest/about/CHANGELOG.html#non-hostcall-hip-printf, I have added the following settings in the RCCL CMakelists.txt file : 

target_compile_options(rccl PRIVATE -mprintf-kind=buffered)

makefiles/common.mk: 
CXXFLAGS   := -DCUDA_MAJOR=$(CUDA_MAJOR) -DCUDA_MINOR=$(CUDA_MINOR) -fPIC -fvisibility=hidden \
              -Wall -mprintf-kind=buffered -g -Wno-unused-function -Wno-sign-compare -std=c++11 -Wvla \
              -I $(CUDA_INC) \
              $(CXXFLAGS)

**After compiling RCCL, reported this error :**

> enquence.cc Current function: ncclLaunchKernel line 1090
> :1:devhcprintf.cpp          :265 : 81559524344 us: [pid:65800 tid:0x7f0d2c53d440] Hash value collision detected, printf buffer ill formed
> :1:rocvirtual.cpp           :3188: 81559524353 us: [pid:65800 tid:0x7f0d2c53d440]
> Could not print data from the printf buffer!
> :1:rocvirtual.cpp           :3280: 81559524355 us: [pid:65800 tid:0x7f0d2c53d440] AQL dispatch failed!
> :1:devhcprintf.cpp          :265 : 81559524402 us: [pid:65799 tid:0x7ff8fd860440] Hash value collision detected, printf buffer ill formed
> :1:rocvirtual.cpp           :3188: 81559524410 us: [pid:65799 tid:0x7ff8fd860440]
> Could not print data from the printf buffer!
> :1:rocvirtual.cpp           :3280: 81559524416 us: [pid:65799 tid:0x7ff8fd860440] AQL dispatch failed!
> [rank0]: RuntimeError: NCCL Error 1: unhandled cuda error (run with NCCL_DEBUG=INFO for details)
> [rank1]: RuntimeError: NCCL Error 1: unhandled cuda error (run with NCCL_DEBUG=INFO for details)

I have set these environment variables
export HIP_KERNEL_PRINTF=1
export HIP_ENABLE_PRINTF=1
export HCC_ENABLE_PRINTF=1
export AMD_LOG_LEVEL=1

Using a Linux server with two GPU cards,  **without printf, the program executes normally**, How should I solve this problem?




### Operating System

22.04.1 LTS (Jammy Jellyfish)

### CPU

12th Gen Intel(R) Core(TM) i7-12700

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 5.7.0

### ROCm Component

HIP, HIPCC, rccl