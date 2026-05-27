# RPM packages: Not all header files are symlinked into /opt/rocm/include

> **Issue #1558**
> **状态**: closed
> **创建时间**: 2021-08-18T10:16:06Z
> **更新时间**: 2024-01-17T23:18:44Z
> **关闭时间**: 2024-01-17T23:18:44Z
> **作者**: Sturmflut
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1558

## 描述

The following official RPM packages symlink their header files into `/opt/rocm/include/`:

hipblas-0.46.0.40300-52.el7.x86_64
hipcub-2.10.9.40300-52.el7.x86_64
hipfft-1.0.3.40300-52.el7.x86_64
hipsparse-1.10.7.40300-52.el7.x86_64
hsakmt-roct-devel-20210520.3.071986.40300-52.el7.x86_64
hsa-rocr-dev-1.3.0.40300-52.el7.x86_64
miopen-hip-2.12.0.40300-52.el7.x86_64
rccl-2.8.4.40300-52.el7.x86_64
rocalution-1.12.1.40300-52.el7.x86_64
rocblas-2.39.0.40300-52.el7.x86_64
rocfft-1.0.12.40300-52.el7.x86_64
rocm-dbgapi-0.48.0.40300-52.el7.x86_64
rocprim-2.10.9.40300-52.el7.x86_64
rocprofiler-dev-1.0.0.40300-52.el7.x86_64
rocsolver-3.13.0.40300-52.el7.x86_64
rocsparse-1.20.2.40300-52.el7.x86_64
rocthrust-2.10.9.40300-52.el7.x86_64
roctracer-dev-1.0.0.40300-52.el7.x86_64

At least the following don't:

rocm-opencl-devel-2.0.0.40300-52.el7.x86_64
hip-base-4.3.21300.5994.40300-52.el7.x86_64

This makes it hard for us as an HPC provider to provide documentation and environment module files for our HPC users since we have to document multiple paths and cannot simply communicate `/opt/rocm/include/`.

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-08-18T11:39:11Z)

Thanks @Sturmflut for reaching out.
I certainly understood the problem.
I will talk to packaging team on this and will share an update.
Thank you.

---

### 评论 #2 — abhimeda (2024-01-02T15:49:50Z)

Is this still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #3 — nartmada (2024-01-17T23:18:44Z)

Closing this ticket as it has become stale.  @Sturmflut, please re-open this ticket if you still see the issue with latest ROCm 6.0.0.  Thanks.

---
