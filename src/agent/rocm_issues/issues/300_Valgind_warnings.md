# Valgind warnings

> **Issue #300**
> **状态**: closed
> **创建时间**: 2018-01-17T00:44:02Z
> **更新时间**: 2018-05-05T14:48:58Z
> **关闭时间**: 2018-05-05T14:48:58Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/300

## 描述

I ran my opencl program against valgrind, and I get a number of 
`== Conditional jump or move depends on uninitialised value(s)`
warnings triggered  by `clEnqueueNDRangeKernel` and `clEnqueueWriteBuffer`




---

## 评论 (4 条)

### 评论 #1 — gstoner (2018-02-16T17:10:41Z)

We. are fixing this it was false positives 

---

### 评论 #2 — gstoner (2018-03-02T23:08:15Z)

@boxerab  Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It support 4.13 Linux kernel   We fixed issue for Valgrind to fix the false positives in this release 

---

### 评论 #3 — boxerab (2018-05-05T03:05:08Z)

Still getting valgrind warnings with 1.7.2


==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE819E3: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE84C85: hsaKmtMapMemoryToGPU (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE877D3: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE7E185: hsaKmtCreateEvent (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAA00002: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA0A1C7: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA0B8A9: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EEDA4: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EEE03: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA093AD: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EFD29: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355== 
==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE83887: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE84DC4: hsaKmtMapMemoryToGPUNodes (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xA9EB7DB: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA077F2: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA000C1: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA0A1EC: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA0B8A9: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EEDA4: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EEE03: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA093AD: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EFD29: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355== 
==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE819E3: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE84C85: hsaKmtMapMemoryToGPU (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE87526: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE87AD6: hsaKmtCreateQueue (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xA9E6559: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9DFED9: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9E3F35: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA09448: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EFD29: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0x70E6ACC: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70B2B12: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355== 
==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE819E3: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE87E6E: hsaKmtCreateQueue (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xA9E6559: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9DFED9: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9E3F35: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA09448: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EFD29: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0x70E6ACC: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70B2B12: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70BF306: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x708FB7D: clGetPlatformIDs (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355== 
==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE83887: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE84DC4: hsaKmtMapMemoryToGPUNodes (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xA9E9878: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EDE2B: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9EBC03: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA076AB: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9F28A1: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9E7779: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9E7A78: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA17334: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xAA17A4D: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355== 
==19355== Conditional jump or move depends on uninitialised value(s)
==19355==    at 0xAE7F74F: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE83887: ??? (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xAE84DC4: hsaKmtMapMemoryToGPUNodes (in /opt/rocm/libhsakmt/lib/libhsakmt.so.1.0.7)
==19355==    by 0xA9E9282: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0xA9FC880: ??? (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.7)
==19355==    by 0x70E3C81: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70F192C: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70E691A: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70E7443: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70B2B12: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x70BF306: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355==    by 0x708FB7D: clGetPlatformIDs (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==19355== 
Platform found : Advanced Micro Devices, Inc.


---

### 评论 #4 — gstoner (2018-05-05T14:48:57Z)

Your getting a false positive 

---
