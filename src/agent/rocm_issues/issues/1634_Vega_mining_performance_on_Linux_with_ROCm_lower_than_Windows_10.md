# Vega mining performance on Linux with ROCm lower than Windows 10

> **Issue #1634**
> **状态**: closed
> **创建时间**: 2021-12-10T09:09:48Z
> **更新时间**: 2021-12-27T01:08:07Z
> **关闭时间**: 2021-12-20T09:02:05Z
> **作者**: falcon35180
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1634

## 描述

Running teamredminer (https://github.com/todxx/teamredminer) on Linux with ROCm 4.5, hashrates are noticeably lower than on Windows 10 on the same hardware. The cards are a reference Vega 56 with Samsung memory and an Asus ROG Strix Vega 64.

With undervolting, memory overclocking and tweaked memory timings (same settings on both OSs), I can get over 48MH/s on DaggerHashimoto (Ethereum) from each GPU on Windows, whereas Linux only manages 33-36MH/s. The lower performance is accompanied by reduced power usage and temperatures.

The differences are similar using stock clocks and voltages, can't remember the exact figures, though.

Linux system is Linux Mint 20 with kernel 5.13, using upstream amdgpu driver. Windows is running the 21.12.1 driver.

I have run clpeak (https://github.com/krrishnarraj/clpeak) on both OSs - results pasted below.

The discrepancies in the transfer bandwidth test results are particularly interesting.

I have tried changing several amdgpu module parameters, such as vm_fragment_size, vm_update_mode and aspm - none of these changes resulted in improvements. Any ideas as to what to look into next would be much appreciated.

Windows:
```
Platform: AMD Accelerated Parallel Processing
  Device: gfx900
    Driver version  : 3354.13 (PAL,HSAIL) (Win64)
    Compute units   : 64
    Clock frequency : 1630 MHz

    Global memory bandwidth (GBPS)
      float   : 364.59
      float2  : 379.73
      float4  : 385.51
      float8  : 383.24
      float16 : 325.42

    Single-precision compute (GFLOPS)
      float   : 13089.21
      float2  : 13056.11
      float4  : 12934.32
      float8  : 12867.45
      float16 : 12529.31

    Half-precision compute (GFLOPS)
      half   : 12982.25
      half2  : 25354.93
      half4  : 24860.46
      half8  : 23939.06
      half16 : 22331.70

    Double-precision compute (GFLOPS)
      double   : 825.91
      double2  : 823.98
      double4  : 823.00
      double8  : 821.03
      double16 : 817.52

    Integer compute (GIOPS)
      int   : 2495.30
      int2  : 2481.64
      int4  : 2488.13
      int8  : 2484.30
      int16 : 2487.74

    Transfer bandwidth (GBPS)
      enqueueWriteBuffer         : 2.91
      enqueueReadBuffer          : 2.39
      enqueueMapBuffer(for read) : 75882.81
        memcpy from mapped ptr   : 2.38
      enqueueUnmap(after write)  : 181990.14
        memcpy to mapped ptr     : 2.95

    Kernel launch latency : 59.50 us

  Device: gfx900
    Driver version  : 3354.13 (PAL,HSAIL) (Win64)
    Compute units   : 56
    Clock frequency : 1590 MHz

    Global memory bandwidth (GBPS)
      float   : 320.61
      float2  : 332.34
      float4  : 340.35
      float8  : 344.50
      float16 : 305.04

    Single-precision compute (GFLOPS)
      float   : 10733.66
      float2  : 10613.94
      float4  : 10314.71
      float8  : 10212.31
      float16 : 9855.57

    Half-precision compute (GFLOPS)
      half   : 10436.38
      half2  : 20421.78
      half4  : 19752.11
      half8  : 18967.41
      half16 : 17752.78

    Double-precision compute (GFLOPS)
      double   : 694.07
      double2  : 690.22
      double4  : 688.07
      double8  : 687.52
      double16 : 685.72

    Integer compute (GIOPS)
      int   : 1898.99
      int2  : 1880.71
      int4  : 1889.94
      int8  : 1887.28
      int16 : 1896.17

    Transfer bandwidth (GBPS)
      enqueueWriteBuffer         : 2.94
      enqueueReadBuffer          : 2.37
      enqueueMapBuffer(for read) : 95021.40
        memcpy from mapped ptr   : 2.29
      enqueueUnmap(after write)  : 181222.23
        memcpy to mapped ptr     : 2.94

    Kernel launch latency : 59.80 us
```

Linux:
```
Platform: AMD Accelerated Parallel Processing
  Device: gfx900:xnack-
    Driver version  : 3361.0 (HSA1.1,LC) (Linux x64)
    Compute units   : 56
    Clock frequency : 1590 MHz

    Global memory bandwidth (GBPS)
      float   : 312.46
      float2  : 322.03
      float4  : 326.64
      float8  : 329.15
      float16 : 321.54

    Single-precision compute (GFLOPS)
      float   : 10593.58
      float2  : 10215.07
      float4  : 10026.24
      float8  : 9855.66
      float16 : 9713.92

    Half-precision compute (GFLOPS)
      half   : 10267.45
      half2  : 20182.21
      half4  : 19756.11
      half8  : 19284.08
      half16 : 18863.68

    Double-precision compute (GFLOPS)
      double   : 689.39
      double2  : 685.22
      double4  : 684.34
      double8  : 685.17
      double16 : 681.57

    Integer compute (GIOPS)
      int   : 1890.58
      int2  : 1871.43
      int4  : 1870.61
      int8  : 1869.36
      int16 : 1879.31

    Transfer bandwidth (GBPS)
      enqueueWriteBuffer         : 4.27
      enqueueReadBuffer          : 4.32
      enqueueMapBuffer(for read) : 59322.75
        memcpy from mapped ptr   : 4.32
      enqueueUnmap(after write)  : 102750.41
        memcpy to mapped ptr     : 4.27

    Kernel launch latency : 15.27 us

  Device: gfx900:xnack-
    Driver version  : 3361.0 (HSA1.1,LC) (Linux x64)
    Compute units   : 64
    Clock frequency : 1630 MHz

    Global memory bandwidth (GBPS)
      float   : 349.93
      float2  : 353.29
      float4  : 354.18
      float8  : 356.31
      float16 : 340.10

    Single-precision compute (GFLOPS)
      float   : 13176.29
      float2  : 13072.32
      float4  : 12906.65
      float8  : 12737.35
      float16 : 12527.88

    Half-precision compute (GFLOPS)
      half   : 13049.59
      half2  : 25511.26
      half4  : 25244.17
      half8  : 24785.29
      half16 : 24175.22

    Double-precision compute (GFLOPS)
      double   : 835.39
      double2  : 832.95
      double4  : 831.27
      double8  : 829.59
      double16 : 825.01

    Integer compute (GIOPS)
      int   : 2517.39
      int2  : 2502.12
      int4  : 2498.14
      int8  : 2492.57
      int16 : 2488.88

    Transfer bandwidth (GBPS)
      enqueueWriteBuffer         : 4.33
      enqueueReadBuffer          : 4.39
      enqueueMapBuffer(for read) : 58996.80
        memcpy from mapped ptr   : 4.39
      enqueueUnmap(after write)  : 102996.81
        memcpy to mapped ptr     : 4.34

    Kernel launch latency : 16.97 us
```

---

## 评论 (6 条)

### 评论 #1 — Nostromo-KM (2021-12-13T22:38:07Z)

To get the same performance as windows you would need to downgrade your kernel to 5.4 series. 
Anything above that i tested resulted in performance regression.
No idea where the regression comes from, kernel or rocm.

---

### 评论 #2 — falcon35180 (2021-12-14T04:29:08Z)

Thanks, Nostromo-KM. Can't remember if I ever tried it with 5.4, but will give it a go.

---

### 评论 #3 — falcon35180 (2021-12-14T16:50:43Z)

Update: performance is indeed higher with 5.4 kernel. ROCm libraries/packages are still 4.5, firmware is the same as before (latest version in repos).

My guess would be that the amdgpu module is responsible for the regression - this could be checked by installing the DKMS module, providing it actually builds with 5.4.

---

### 评论 #4 — ROCmSupport (2021-12-20T09:02:05Z)

Hi @falcon35180 
Thanks for reaching out.
I certainly understood the situation.
I do not think its an ideal comparison as we are comparing between Linux/ROCm and Windows10/non-ROCm.
So I can not comment more on this as the comparison is not ideal.
I recommend to try with older kernels like 5.4 as suggested above. 
This way you might find perf drops by comparing 2 different linux kernels, I recommend to file the issues in those cases.
Thank you.

---

### 评论 #5 — Atemu (2021-12-24T17:25:48Z)

@falcon35180 FYI you can run the AMDGPU-pro stack in a docker container. You can get a Docker image with AMDGPU-pro and teamredminer here: https://hub.docker.com/r/wesparish/teamredminer.

Works just fine without any special kernel modules or similar and you can keep using your regular desktop with Mesa at the same time.

---

### 评论 #6 — falcon35180 (2021-12-27T01:08:07Z)

@Atemu I'm now running the two Vegas on a Tiny Core Linux setup with kernel 5.4, upstream driver and amdgpu-pro OpenCL libraries. As mentioned earlier, 5.4 performs well - amdgpu-pro (version 20.40) and ROCm give the same results in this regard.

---
