# [Issue]: OpenCL Vendor detection in Multi ROCm broken

- **Issue #:** 5977
- **State:** open
- **Created:** 2026-02-18T08:20:06Z
- **Updated:** 2026-03-04T15:15:53Z
- **Labels:** ROCm 6.2.4, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5977

### Problem Description

Hi, it seems that something in the way OpenCL is handled changed at some point. We have a dual ROCm installation with 7.2.0 and 6.2.4 but detection of GPU devices is not consistent.

I would expect:
a) both versions to handle the same
b) Especially not showing up or showing up as two platforms seems broken

### Operating System

Alma 9.7

### CPU

Irelevant

### GPU

Irelevant

### ROCm Version

7.2.0, 6.2.4

### ROCm Component

_No response_

### Steps to Reproduce

Create a multi ROCm (6.2.4 and 7.2.0 in our case) installation.

Run
```
module purge
module load rocm/6.2.4
clinfo
```
All GPUs show up 8+2.
This behaviour, although correct, is very strange to me because the /etc/ld.so.conf.d that tells the system where to look for the libamdocl is not there. So it shouldn't know where to look at all, or is it looking according to some ROCM_PATH variable?

Run
```
module purge
module load rocm/7.2.0
clinfo
```

No GPU devices show up only CPUs 2.

I have a couple of thoughts on the reason for this.
- The order of installation might have an impact
- Package dependencies between the two versions might have changed so we are missing a "important package" in the 7.2.0 installation.
- **The `rocm-opencl-icd-loader`doesn't exist for 7.2.0 and sounds to me like it could do what is not happening for 7.2.0** 
- In the past there used to be a rocm file in /etc/ld.so.conf.d which defined the path to look for the libamdocl...so (It is not present in our installation)
- When exporting LD_LIBRARY_PATH to include /opt/rocm-<version>/lib in the modulefile for 7.2.0 the GPUs are detected twice. Which I believe might have to do with both rocm versions being in /etc/OpenCL/vendors

```
ls -l /etc/OpenCL/vendors/
total 12
-rw-r--r--. 1 root root 15 Feb 17 11:50 amdocl64_60204_139.icd
-rw-r--r--. 1 root root 15 Jan 10 01:36 amdocl64_70200_43.icd
-rw-r--r--  1 root root 18 Feb 17 18:11 pocl.icd


module load rocm/7.2.0
LD_LIBRARY_PATH=/opt/rocm-7.2.0 clinfo
Number of platforms:                             3
...
```
Which, by the way, doesn't happen in 6.2.4 (maybe due to some version check or because it simply works differently).

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_