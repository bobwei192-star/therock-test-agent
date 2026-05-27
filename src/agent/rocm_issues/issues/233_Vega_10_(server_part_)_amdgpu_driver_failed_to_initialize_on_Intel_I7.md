# Vega 10 (server part ) amdgpu driver failed to initialize on Intel I7

> **Issue #233**
> **状态**: closed
> **创建时间**: 2017-10-23T12:51:53Z
> **更新时间**: 2017-10-23T14:17:05Z
> **关闭时间**: 2017-10-23T14:17:05Z
> **作者**: FalconBsp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/233

## 描述

Trying to run ROCm on Vega10 server part and facing below issues.  

dmesg logs: 
```
[   11.406987] Doesn't get msg:1 from pf.
[   11.406989] Doesn't get READY_TO_ACCESS_GPU from pf, give up
[   11.406992] amdgpu 0000:04:00.0: Fatal error during GPU init
[   21.329721] Doesn't get msg:1 from pf.
[   21.329722] Doesn't get READY_TO_ACCESS_GPU from pf, give up
[   21.329729] [drm] amdgpu: finishing device.
[   21.329730] [TTM] Memory type 2 has not been initialized
[   21.329817] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x31fb1a47d84, max_idle_ns: 440795381027 ns
[   21.329904] amdgpu: probe of 0000:04:00.0 failed with error -62
```

cpuinfo:
```
processor       : 7
vendor_id       : GenuineIntel
cpu family      : 6
model           : 58
model name      : Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz
stepping        : 9
microcode       : 0x15
cpu MHz         : 1599.975
cache size      : 8192 KB
physical id     : 0
siblings        : 8
core id         : 3
cpu cores       : 4
apicid          : 7
initial apicid  : 7
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm epb tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm ida arat pln pts
bugs            :
bogomips        : 6936.03
clflush size    : 64
cache_alignment : 64
address sizes   : 36 bits physical, 48 bits virtual
power management:
```


---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-10-23T14:04:39Z)

For Intel CPU we need Haswell or new which support Atomic Completers/PCIe Atomics  correctly,  This is not supported CPU. 





---

### 评论 #2 — FalconBsp (2017-10-23T14:08:22Z)

WX9100 works fine on this Intel system . Problem with Vega10 card.  If it is a PCIe Atomic issue , it should not work on WX9100 . 

---

### 评论 #3 — gstoner (2017-10-23T14:16:23Z)

Is this MI25 GPU your are testing, if so it the same core in WX9100,  it should not have an issue. 

---

### 评论 #4 — gstoner (2017-10-23T14:17:05Z)

Ivybridge is still not officially supported 

---
