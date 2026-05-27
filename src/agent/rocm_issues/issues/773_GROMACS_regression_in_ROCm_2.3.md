# GROMACS regression in ROCm 2.3

> **Issue #773**
> **状态**: closed
> **创建时间**: 2019-04-16T15:17:22Z
> **更新时间**: 2023-12-12T20:11:56Z
> **关闭时间**: 2023-12-12T20:10:05Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/773

## 描述

The major GROMACS kernel flavors regressed by ~30% on both Fiji and Vega from 2.2 to 2.3.

---

## 评论 (13 条)

### 评论 #1 — sunway513 (2019-04-16T15:23:55Z)

Hi @pszi1ard , could you provide the samples/steps to reproduce the performance regression? 

---

### 评论 #2 — pszi1ard (2019-04-16T15:27:07Z)

The wall-time of the top (time-wise) kernel should indicate where the issue is. I believe AMD has internal pref regression testing of GROMACS, so I'm hoping I don't need to write line-by-line instructions here as perf-testing GROMACS should be a known thing.



---

### 评论 #3 — gowthamcr (2019-04-23T12:11:31Z)

Hi @pszi1ard 
Can you provide us the version of the Gromacs you are observing issue with?

---

### 评论 #4 — pszi1ard (2019-04-23T18:50:35Z)

I did the performance measurements with the 2019.2 code but I doubt it is very dependent on the GROMACS version.

I observe major regressions in multiple kernels; for the a 192k sized input (e.g. inputs inside this tarball 0192/ -- generate input tpr with gmx grompp -f pme.mdp)(http://ftp.gromacs.org/benchmarks/water_GMX50_bare.tar.gz):
nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl: -32%
pmeGatherKernel: -350%
pmeSolveXYZKernel: -26%
clFFT kernels: ballpark 2x slower


---

### 评论 #5 — pszi1ard (2019-04-23T18:52:24Z)

> pmeGatherKernel: -350%

This one issues a warning about failing to unroll a loop, so that is probably (part?) of the reason. Can I force unroll? 


---

### 评论 #6 — pszi1ard (2019-04-26T13:10:11Z)

Wrestled through the pain of running the profiler, the most likely main reasons for the nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl regression is VGPR/SGPR usage that went from 77/62 to 95/66 dropping occupancy to 0.2; already the original VGPR use is higher than what I believe it should be (I think this should be able to run at 0.5 occupancy).

I hope this helps. Please let me know if there is any progress and what the ETA for the fix to land in a release is -- the current 2.3 is just unusable even for development.

---

### 评论 #7 — pszi1ard (2019-06-10T15:39:40Z)

Still no fix after the 2.5 release.

---

### 评论 #8 — pszi1ard (2019-09-30T09:40:15Z)

FYI: The 2.8 release is still severely regressed (so was the 2.7).

---

### 评论 #9 — pszi1ard (2019-10-08T12:20:00Z)

FYI: no change in 2.9 either.

---

### 评论 #10 — pszi1ard (2020-10-22T18:00:18Z)

This bug is still not fixed in 3.8.

I've identified it to be related to a missed optimization of float3 register array allocation which was introduced sometime after ROCm 2.2 (at least based on my historic performance data).

---

### 评论 #11 — tasso (2023-12-12T19:56:55Z)

Is this issue reproducible with the latest ROCM?  If not, can we please close it?  Thanks!

---

### 评论 #12 — pszi1ard (2023-12-12T20:10:05Z)

This is all about the GROMACS OpenCL backend, I don't think this was ever addressed, but this backend is deprecated in favor of the SYCL backed. 

---

### 评论 #13 — tasso (2023-12-12T20:11:55Z)

Thanks for the reply!

---
