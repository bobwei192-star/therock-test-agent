# [Issue]:  brocken cp-command in half post-build script

- **Issue #:** 3743
- **State:** closed
- **Created:** 2024-09-18T02:31:39Z
- **Updated:** 2024-09-30T13:56:06Z
- **Labels:** Under Investigation, AMD Radeon Pro W7900, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3743

### Problem Description

While trying to move package files, after building half, the cp command brakes in cause of incomplete filename-pattern.
I can't locate where the cp call takes place to fix it.

### Operating System

Debian 12 Bookworm with Backports

### CPU

 AMD Ryzen 5 5600G with Radeon Graphics

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.2.0

### ROCm Component

half

### Steps to Reproduce

Like described in README.md in ROCm.git 
local settings: export GPU_ARCHS="gfx803;gfx90c"

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

[all fine until …]
-- Install configuration: "Release"
-- Installing: /opt/rocm-6.2.0/include/half/half.hpp
-- Installing: /opt/rocm-6.2.0/share/doc/half/LICENSE.txt
gmake[1]: Leaving directory '/home/builder/devel/amd/rocm-6.2/out/debian-12/12/build/half'
+ rm -rf _CPack_Packages/
+ find -name '*.o' -delete
+ mkdir -p /home/builder/devel/amd/rocm-6.2/out/debian-12/12//half
+ cp '/home/builder/devel/amd/rocm-6.2/out/debian-12/12/build/half/*.' /home/builder/devel/amd/rocm-6.2/out/debian-12/12//half
cp: cannot stat '/home/builder/devel/amd/rocm-6.2/out/debian-12/12/build/half/*.': No such file or directory

real	0m2.276s
user	0m0.713s
sys	0m0.290s
+ mv /home/builder/devel/amd/rocm-6.2/out/debian-12/12/logs/half.inprogress /home/builder/devel/amd/rocm-6.2/out/debian-12/12/logs/half.errors
+ echo Error in half
Error in half
+ exit 1
