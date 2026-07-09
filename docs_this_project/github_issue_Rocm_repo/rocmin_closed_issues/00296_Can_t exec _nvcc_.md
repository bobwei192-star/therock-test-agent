# Can't exec "nvcc"

- **Issue #:** 296
- **State:** closed
- **Created:** 2018-01-04T09:53:49Z
- **Updated:** 2018-01-22T16:47:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/296

I installed rocm1.7  and run hipconfig ,get this error info:
HIP version  : 1.4.17494

== hipconfig
HIP_PATH     : /opt/rocm/hip
HIP_PLATFORM : nvcc
CPP_CONFIG   :  -D__HIP_PLATFORM_NVCC__=  -I/opt/rocm/hip/include -I/usr/local/cuda/include

== nvcc
Can't exec "nvcc": 没有那个文件或目录 at /opt/rocm/hip/bin/hipconfig line 144.

=== Environment Variables
PATH=/opt/rocm/hcc/bin:/opt/rocm/hip/bin:/home/ken/bin:/home/ken/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/rocm/bin/
HIP_PATH=/opt/rocm/hip
HCC_HOME=/opt/rocm/hcc

== Linux Kernel
Hostname     : ken-B250M-D3H
Linux ken-B250M-D3H 4.13.0-21-generic #24~16.04.1-Ubuntu SMP Mon Dec 18 19:39:31 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial


this error  look is line  70 of hipconfig  programe:
if (not defined $HIP_PLATFORM) {
     70     $NAMDGPUNODES=`cat /sys/class/kfd/kfd/topology/nodes/*/properties 2>/dev/null | grep -c 'simd_count [1-9]'`;
     71 
     72     if ($NAMDGPUNODES > 0) {
     73         $HIP_PLATFORM = "hcc"
     74     } else {
     75         $HIP_PLATFORM = "nvcc";
     76     }
     77 }
cat /sys/class/kfd/kfd/topology/nodes/*/properties 2>/dev/null | grep -c 'simd_count [1-9]'
$NAMDGPUNODES =0


lspci info:
lspci |grep VGA
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)

my GPU is a xfx vega64 gpu.