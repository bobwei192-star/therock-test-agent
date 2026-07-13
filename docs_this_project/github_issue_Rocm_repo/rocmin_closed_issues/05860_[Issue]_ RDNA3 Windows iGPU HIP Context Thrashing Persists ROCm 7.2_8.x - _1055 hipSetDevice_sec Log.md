# [Issue]: RDNA3 Windows iGPU HIP Context Thrashing Persists ROCm 7.2/8.x - ~1055 hipSetDevice/sec Logs

- **Issue #:** 5860
- **State:** closed
- **Created:** 2026-01-16T13:23:42Z
- **Updated:** 2026-04-14T16:24:12Z
- **Labels:** status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5860

### Problem Description

gfx1103 iGPU Windows ROCm: hipSetDevice 1055x/sec kills 60% performance - HIP logs proof.

1055 hipSetDevice calls/second. Healthy HIP: 1 call total at init.

Unlike discrete RX 9070XT (performance issues but stable context), iGPUs thrash HIP context 1000x more due to shared memory. Here's HIP_LOG_LEVEL=3 proof: 1055 hipSetDevice/sec vs healthy 1-2/min

7742 lines like these before step 1—that's your smoking gun right there. Healthy startup = 100-300 lines total. I'm at 25x+ excessive during init alone.

I'll just copy & paste below a small chunk of those 7742 lines, that clearly shows the pattern, 7 loops.

The repeating loop is like this:
memcpy (3.2MB tile) → hipSetDevice → 4x hipGetDevice → ctx state → stream checks → memcpy (2.5KB meta) → hipSetDevice → repeat

Each memcpy triggers 15-20 device context calls

The pattern shows 4 complete thrash cycles in ~0.0027 seconds:
Cycle 1: 1223391421us → hipSetDevice(0) → 15 lines device/ctx checks → 1223391746us memcpy
Cycle 2: 1223391959us → hipSetDevice(0) → repeat → 1223392258us  
Cycle 3: 1223393312us → hipSetDevice(0) → repeat → 1223393689us
Cycle 4: 1223393873us → hipSetDevice(0) → repeat → 1223394190us

7 hipSetDevice calls in 6,632 microseconds (0.0066 seconds) during ComfyUI - Healthy HIP: 1x total at init.

Every single memcpy triggers a full device context re-initialization. This explains the 7742+ HIP lines before step 1.

HIP documentation and best practices are clear: hipSetDevice should be called ONCE at application startup to select the target GPU, then HIP maintains that context automatically in thread-local storage.

My logs prove the thrashing alone eats more cycles than actual GPU compute.

As for performance cost, look at the timestamps:
hipLaunchKernel takes 22–40 microseconds.
The hipSetDevice / hipGetDevice chatter surrounding it takes about 150–200 microseconds.

The "Guardrails" are taking 5x longer than the actual math. The CPU is spending 80% of its time talking to the driver and only 20% actually launching math.

Some more data before the log example, my iGPU usage is at around 90% during KSampler, GPU temperature is around 40 C, idle temperature 27 C. I have 32 GB RAM in total and I set 16 GB VRAM in BIOS dedicated to iGPU.

There is plenty of headroom in memory, so the thrashing isn't caused by "Out of Memory" swapping. During KSampler, iGPU VRAM (16 GB) in use is around 16000 MB but system memory (16 GB) is only at around 29%.

I'll share my log and environment variables, flags in the .bat file below.

### Operating System

Windows 11 (10.0.26200)

### CPU

AMD Ryzen 5 8600G w/ Radeon 760M Graphics

### GPU

AMD Radeon 760M Graphics

### ROCm Version

7.2.53150

### ROCm Component

_No response_

### Steps to Reproduce

1. set AMD_LOG_LEVEL=3 in run_amd_gpu.bat
3. Run this file to start ComfyUI
4. Run KSampler workflow
5.  Observe Thrashing even before 1st step 
6. Expected: hipSetDevice(0) 1x at startup [HIP docs]Reality:  7x hipSetDevice(0) in 0.0066s chunk during steady-state memcpy
→ 1055 calls/second, 15+ device/ctx checks per memcpy cycle
6. 7742+ HIP lines before step 1 (vs expected ~200), rocminfo confirms gfx1103 detection works, iGPU is being used but not optimized

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I'm using a portable ComfyUI build, my environment variables and flags in the .bat file:

set HSA_OVERRIDE_GFX_VERSION=11.0.3

set PYTORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
set PYTORCH_ALLOC_CONF=expandable_segments:True
set PYTORCH_HIP_ALLOC_CONF=expandable_segments:True
set PYTORCH_ALLOC_CONF=max_split_size_mb:128
set PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:128
set HIP_FORCE_DEV_KFD=1

set HIP_VISIBLE_DEVICES=0
set HSA_ENABLE_SDMA=0
set ROCR_FORCE_DISABLE_CUASM=1
set AMD_LOG_LEVEL=3

set TORCH_CUDNN_ENABLED=0

.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --highvram --use-pytorch-cross-attention --disable-smart-memory

My logs prove the thrashing alone eats more cycles than actual GPU compute.

A smaller example from the full log of 7742+ similar lines I got before step 1, that shows 7 of the repeating loops:

:3:hip_graph.cpp            :2062: 1223390479 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223390500 us:   hipMemcpyWithStream ( 00000253C9B10000, 000000054F120000, 3276800, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223391398 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 898 us
:3:hip_device_runtime.cpp   :776 : 1223391421 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223391444 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223391511 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223391531 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223391552 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223391579 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223391598 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223391613 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223391627 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223391642 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223391657 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223391671 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223391685 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223391700 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223391715 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223391729 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223391746 us:   hipMemcpyWithStream ( 000002538FFFC000, 00000003002A6E00, 2560, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223391936 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 190 us
:3:hip_device_runtime.cpp   :776 : 1223391959 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223391982 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223392025 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223392041 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223392058 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223392074 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223392093 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223392108 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223392124 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223392140 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223392157 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223392173 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223392189 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223392205 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223392222 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223392238 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223392258 us:   hipMemcpyWithStream ( 00000253CAD10000, 000000054F760000, 3276800, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223393277 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 1019 us
:3:hip_device_runtime.cpp   :776 : 1223393312 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223393336 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223393400 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223393417 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223393445 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223393486 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223393517 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223393543 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223393567 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223393583 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223393599 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223393614 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223393628 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223393642 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223393658 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223393672 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223393689 us:   hipMemcpyWithStream ( 000002538FFFCA00, 00000003002A5000, 2560, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223393853 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 164 us
:3:hip_device_runtime.cpp   :776 : 1223393873 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223393889 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223393957 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223393973 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223393990 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223394006 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223394025 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223394040 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223394056 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223394072 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223394089 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223394104 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223394121 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223394137 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223394154 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223394170 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223394190 us:   hipMemcpyWithStream ( 00000253CB090000, 000000054EE00000, 3276800, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223395105 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 915 us
:3:hip_device_runtime.cpp   :776 : 1223395126 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223395142 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395193 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223395209 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223395225 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223395241 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223395259 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223395274 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395300 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223395316 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223395333 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223395348 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395365 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223395381 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223395398 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223395413 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223395434 us:   hipMemcpyWithStream ( 000002538FFFD400, 00000003002A6400, 2560, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223395581 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 147 us
:3:hip_device_runtime.cpp   :776 : 1223395602 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223395618 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395660 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223395675 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223395689 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223395704 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223395719 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223395735 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395765 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223395794 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :1082: 1223395830 us:   hipStreamIsCapturing ( char array:<null>, 000000611B73DD50 )
:3:hip_graph.cpp            :1083: 1223395848 us:  hipStreamIsCapturing: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223395865 us:   hipGetDevice ( 000000611B73DBCC )
:3:hip_device_runtime.cpp   :702 : 1223395881 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_graph.cpp            :2061: 1223395899 us:   hipStreamGetCaptureInfo ( char array:<null>, 000000611B73DC54, char array:<null> )
:3:hip_graph.cpp            :2062: 1223395914 us:  hipStreamGetCaptureInfo: Returned hipSuccess :
:3:hip_memory.cpp           :827 : 1223395934 us:   hipMemcpyWithStream ( 00000253CB410000, 000000054F440000, 3276800, hipMemcpyDeviceToHost, char array:<null> )
:3:hip_memory.cpp           :844 : 1223396933 us:  hipMemcpyWithStream: Returned hipSuccess : : duration: 999 us
:3:hip_device_runtime.cpp   :776 : 1223396957 us:   hipSetDevice ( 0 )
:3:hip_device_runtime.cpp   :782 : 1223396973 us:  hipSetDevice: Returned hipSuccess :
:3:hip_device_runtime.cpp   :690 : 1223397028 us:   hipGetDevice ( 000000611B73DC14 )
:3:hip_device_runtime.cpp   :702 : 1223397045 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_device_runtime.cpp   :690 : 1223397062 us:   hipGetDevice ( 000000611B73DC6C )
:3:hip_device_runtime.cpp   :702 : 1223397078 us:  hipGetDevice: Returned hipSuccess : 0
:3:hip_context.cpp          :368 : 1223397096 us:   hipDevicePrimaryCtxGetState ( 0, 000000611B73DC64, 000000611B73DC60 )
:3:hip_context.cpp          :382 : 1223397111 us:  hipDevicePrimaryCtxGetState: Returned hipSuccess :