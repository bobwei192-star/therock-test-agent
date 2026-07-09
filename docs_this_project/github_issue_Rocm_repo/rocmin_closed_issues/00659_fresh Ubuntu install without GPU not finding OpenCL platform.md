# fresh Ubuntu install without GPU not finding OpenCL platform

- **Issue #:** 659
- **State:** closed
- **Created:** 2019-01-03T15:05:21Z
- **Updated:** 2019-01-03T18:48:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/659

I tried to do a basic setup to test ROCm for OpenCL for CPU-only (initially).  clGetPlatformIDs is returning -1001.  Can anyone confirm these steps?


**Test setup:**
Fresh install of Ubuntu 18.04 **in a virtual machine**, running on Intel i7 v4 CPU with 4 cores, no discrete GPU.


**Steps:**

```
$ sudo apt update
$ sudo apt install rocm-dkms
```
 Succes. Reboot.

```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call retured 4104
```

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```

`$ strace /opt/rocm/opencl/bin/x86_64/clinfo`
Shows that **libamdoclcl64.so** is not found in a couple dozen paths right before exit 1.


Did I miss something?  Other packages are mentioned on the install guide.

`$ sudo apt install rock-dkms`
"already the newest version" 0 upgraded, 0 newly installed.

`$ sudo apt install rocm-opencl-dev`
"already the newest version" 0 upgraded, 0 newly installed.

`$ sudo apt-get install dkms rock-dkms rocm-opencl`
for each ... "already the newest version" 0 upgraded, 0 newly installed.


I'm not sure what else to try.  Where should libamdoclcl64.so be located?   Would it be installed if I don't have a supported GPU?
