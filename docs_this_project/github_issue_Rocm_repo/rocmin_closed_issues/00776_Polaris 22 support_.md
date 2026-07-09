# Polaris 22 support?

- **Issue #:** 776
- **State:** closed
- **Created:** 2019-04-18T19:02:30Z
- **Updated:** 2020-10-28T23:15:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/776

https://www.techpowerup.com/gpu-specs/amd-polaris-22.g821 says ROCm isn't supported on Polaris 22.  Is that accurate and not going to change?

I am running Ubuntu 18.10 with Linux 4.18 and the ROCm stack appears to be completely broken, include HCC and OpenCL.

```
$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```

```
$ lsmod | grep amd
amdgpu               3518464  11
amdttm                102400  1 amdgpu
amd_sched              28672  1 amdgpu
amdkcl                 24576  3 amd_sched,amdttm,amdgpu
amd_iommu_v2           20480  1 amdgpu
drm_kms_helper        172032  2 amdgpu,i915
drm                   458752  10 drm_kms_helper,amd_sched,amdttm,amdgpu,i915,amdkcl
i2c_algo_bit           16384  3 igb,amdgpu,i915
```