# Fedora Distribution support

> **Issue #567**
> **状态**: closed
> **创建时间**: 2018-10-03T16:07:31Z
> **更新时间**: 2021-10-19T22:29:45Z
> **关闭时间**: 2021-01-07T08:40:10Z
> **作者**: akostadinov
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/567

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hello, [Fedora](http://fedoraproject.org/) is a linux distribution that strives to stay very close to upstream and has a 6 month update cycle so one can find pretty much the latest dev tools on it. It will be very useful to have RPM repo for installing on Fedora linux. Useful for the ROCm project - to see how things work with latest available kernels and tools as well for Fedora users.
Presently only Ubuntu and RHEL repos are available.

---

## 评论 (50 条)

### 评论 #1 — gstoner (2018-10-07T18:22:30Z)


One thing Rehat guys were looking at supporting this via COPR https://copr.fedorainfracloud.org/coprs/tstellar/rocm-amd/ 

---

### 评论 #2 — akostadinov (2018-10-07T19:08:38Z)

 Presently not useful but good to know. Fun quote:

> Instructions not filled in by author. Author knows what to do. Everybody else should avoid this repo.

---

### 评论 #3 — gstoner (2018-10-07T19:14:23Z)

One thing we have been working on is getting the core kernel driver upstream so it will be easier to support other Distros.  

WIth 1.9.1 with the current upstream Linux kernel, it should be possible to get Fedora working again.   let me talk to the team about getting build instruction out for this 

---

### 评论 #4 — tomkv (2018-10-15T12:59:45Z)

It does work on Fedora 28 and current kernel.

However, the pain points for building from source are:

- Not a obvious relation between existing binary packages and which repo they come from. The packages that compose the system change between releases, so the game starts again with each release.
- If you find the repo, it may not have the version or checkout that was used to build the binary release yet;
- Binary-only artefacts in binary packages, that are not in any repo;
- Certain stubborness wrt paths; some packages do not like being outside /opt/rocm + /opt/rocm/packagename, so patching is required. Distributions will insist on other path;
- Build system for some packages may not like ninja-build (cmake -GNinja; ROCm-Device-Libs/opencl won't build), but when building with gnu make, you will either run out of memory when using all your cores, or you have to limit the number of cores, which makes it build for eternity. Makes it not a fun debugging why the build failed.

So these are those points that I remember since I did the build the last time.


---

### 评论 #5 — yaxxie (2018-10-16T21:17:27Z)

How about having the binary distribution working? I only had two roadblocks, one of them serious:

1) The hcc package requires pth which seems to have been renamed in latest fedora

2) The rocm-dkms fails to compile...

```  CC [M]  /var/lib/dkms/amdgpu/1.9-224.el7/build/amd/amdkfd/kfd_device.o
/var/lib/dkms/amdgpu/1.9-224.el7/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
/var/lib/dkms/amdgpu/1.9-224.el7/build/amd/amdgpu/amdgpu_drv.c:768:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’? [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  vga_switcheroo_process_delayed_switch
  CC [M]  /var/lib/dkms/amdgpu/1.9-224.el7/build/amd/amdkcl/main.o
cc1: some warnings being treated as errors
make[2]: *** [scripts/Makefile.build:317: /var/lib/dkms/amdgpu/1.9-224.el7/build/amd/amdgpu/amdgpu_drv.o] Error 1
```

If we could get these sorted Fedora users should be able to use the binary distribution (which some of us would prefer to building from source)

---

### 评论 #6 — chriselrod (2018-10-17T06:03:26Z)

> How about having the binary distribution working? I only had two roadblocks, one of them serious:
> 
>     1. The hcc package requires pth which seems to have been renamed in latest fedora

> nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

https://fedora.pkgs.org/27/fedora-x86_64/npth-1.5-3.fc27.x86_64.rpm.html

> 2. The rocm-dkms fails to compile...

For kernels 4.18+, I believe you aren't supposed to use rocm-dkms. Eg, [this comment](https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/open-source-amd-linux/1047471-amd-rocm-1-9-available-with-vega-20-support-plus-upstream-kernel-compatibility/page2#post1047548).


---

### 评论 #7 — yaxxie (2018-10-17T08:20:13Z)

Thanks, will re-evaulate later on (I did install npth and forced the hcc rpm to install without deps). Will try to understand why clinfo isn't showing the GPU device despite the dkms module failing to compile. Maybe I missed a step. In any case, I could contribute a "for fedora users" installation guide if I get it running.

---

### 评论 #8 — tomkv (2018-10-17T08:44:22Z)

> Will try to understand why clinfo isn't showing the GPU device despite the dkms module failing to compile. 

Check if you have amdkfd loaded and /dev/kfd has the correct permissions.

Amdkfd needs to be loaded when amdgpu loads, it cannot be modprobed later. In Fedora, amdgpu is being loaded from initramfs, and initramfs is missing the amdkfd module, so you must add it manually and rebuild initramfs.

How to handle permissions is in the ROCm readme, add the udev rule.

Also try running `rocm-smi`, `rocminfo` and `dmesg|grep kfd`, what they do say. `clinfo` is OpenCL-specific info tool.

---

### 评论 #9 — chriselrod (2018-10-17T16:35:45Z)

> Thanks, will re-evaulate later on (I did install npth and forced the hcc rpm to install without deps). Will try to understand why clinfo isn't showing the GPU device despite the dkms module failing to compile. Maybe I missed a step. In any case, I could contribute a "for fedora users" installation guide if I get it running.

Hopefully tomkv's suggestions help. If you do get it running and write the guide, I'll definitely swap my Debian installation (that has ROCm) to Fedora.

---

### 评论 #10 — yaxxie (2018-10-17T19:44:35Z)

rocm-dkms was red herring, it looks like I got close but not quite there:

```# /opt/rocm/bin/rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  0   66c     47.9W    1330Mhz  2000Mhz  33.73%   auto      0%         0%       
================================================================================
====================           End of ROCm SMI Log          ====================

```

```# /opt/rocm/bin/rocminfo  | grep 'Device Type:'
  Device Type:             CPU                                
  Device Type:             GPU 
```

```# dmesg|grep kfd
[    1.663581] kfd kfd: Initialized module
[    1.917791] kfd kfd: Allocated 3969056 bytes on gart
[    1.917912] kfd kfd: added device 1002:67df
```

```# /opt/rocm/opencl/bin/x86_64/clinfo  | grep 'Device Type:'
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
  Device Type:					 CL_DEVICE_TYPE_CPU
  Device Type:					 CL_DEVICE_TYPE_GPU
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
ERROR: clGetDeviceIDs(-1)

```

(Sorry for wall of debugging stuff)....

And finally....

```[root@future-yaxxie ocltest]# g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL
./HelloWorld.cpp: In function ‘_cl_command_queue* CreateCommandQueue(cl_context, _cl_device_id**)’:
./HelloWorld.cpp:116:69: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
     commandQueue = clCreateCommandQueue(context, devices[0], 0, NULL);
                                                                     ^
In file included from ./HelloWorld.cpp:23:
/opt/rocm/opencl/include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
./HelloWorld.cpp:116:69: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
     commandQueue = clCreateCommandQueue(context, devices[0], 0, NULL);
                                                                     ^
In file included from ./HelloWorld.cpp:23:
/opt/rocm/opencl/include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
[root@future-yaxxie ocltest]# ./HelloWorld 
DRM_IOCTL_I915_GEM_APERTURE failed: Invalid argument
Assuming 131072kB available aperture size.
May lead to reduced performance or incorrect rendering.
get chip id failed: -1 [2]
param: 4, val: 0
Could not create GPU context, trying CPU...
0 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99 102 105 108 111 114 117 120 123 126 129 132 135 138 141 144 147 150 153 156 159 162 165 168 171 174 177 180 183 186 189 192 195 198 201 204 207 210 213 216 219 222 225 228 231 234 237 240 243 246 249 252 255 258 261 264 267 270 273 276 279 282 285 288 291 294 297 300 303 306 309 312 315 318 321 324 327 330 333 336 339 342 345 348 351 354 357 360 363 366 369 372 375 378 381 384 387 390 393 396 399 402 405 408 411 414 417 420 423 426 429 432 435 438 441 444 447 450 453 456 459 462 465 468 471 474 477 480 483 486 489 492 495 498 501 504 507 510 513 516 519 522 525 528 531 534 537 540 543 546 549 552 555 558 561 564 567 570 573 576 579 582 585 588 591 594 597 600 603 606 609 612 615 618 621 624 627 630 633 636 639 642 645 648 651 654 657 660 663 666 669 672 675 678 681 684 687 690 693 696 699 702 705 708 711 714 717 720 723 726 729 732 735 738 741 744 747 750 753 756 759 762 765 768 771 774 777 780 783 786 789 792 795 798 801 804 807 810 813 816 819 822 825 828 831 834 837 840 843 846 849 852 855 858 861 864 867 870 873 876 879 882 885 888 891 894 897 900 903 906 909 912 915 918 921 924 927 930 933 936 939 942 945 948 951 954 957 960 963 966 969 972 975 978 981 984 987 990 993 996 999 1002 1005 1008 1011 1014 1017 1020 1023 1026 1029 1032 1035 1038 1041 1044 1047 1050 1053 1056 1059 1062 1065 1068 1071 1074 1077 1080 1083 1086 1089 1092 1095 1098 1101 1104 1107 1110 1113 1116 1119 1122 1125 1128 1131 1134 1137 1140 1143 1146 1149 1152 1155 1158 1161 1164 1167 1170 1173 1176 1179 1182 1185 1188 1191 1194 1197 1200 1203 1206 1209 1212 1215 1218 1221 1224 1227 1230 1233 1236 1239 1242 1245 1248 1251 1254 1257 1260 1263 1266 1269 1272 1275 1278 1281 1284 1287 1290 1293 1296 1299 1302 1305 1308 1311 1314 1317 1320 1323 1326 1329 1332 1335 1338 1341 1344 1347 1350 1353 1356 1359 1362 1365 1368 1371 1374 1377 1380 1383 1386 1389 1392 1395 1398 1401 1404 1407 1410 1413 1416 1419 1422 1425 1428 1431 1434 1437 1440 1443 1446 1449 1452 1455 1458 1461 1464 1467 1470 1473 1476 1479 1482 1485 1488 1491 1494 1497 1500 1503 1506 1509 1512 1515 1518 1521 1524 1527 1530 1533 1536 1539 1542 1545 1548 1551 1554 1557 1560 1563 1566 1569 1572 1575 1578 1581 1584 1587 1590 1593 1596 1599 1602 1605 1608 1611 1614 1617 1620 1623 1626 1629 1632 1635 1638 1641 1644 1647 1650 1653 1656 1659 1662 1665 1668 1671 1674 1677 1680 1683 1686 1689 1692 1695 1698 1701 1704 1707 1710 1713 1716 1719 1722 1725 1728 1731 1734 1737 1740 1743 1746 1749 1752 1755 1758 1761 1764 1767 1770 1773 1776 1779 1782 1785 1788 1791 1794 1797 1800 1803 1806 1809 1812 1815 1818 1821 1824 1827 1830 1833 1836 1839 1842 1845 1848 1851 1854 1857 1860 1863 1866 1869 1872 1875 1878 1881 1884 1887 1890 1893 1896 1899 1902 1905 1908 1911 1914 1917 1920 1923 1926 1929 1932 1935 1938 1941 1944 1947 1950 1953 1956 1959 1962 1965 1968 1971 1974 1977 1980 1983 1986 1989 1992 1995 1998 2001 2004 2007 2010 2013 2016 2019 2022 2025 2028 2031 2034 2037 2040 2043 2046 2049 2052 2055 2058 2061 2064 2067 2070 2073 2076 2079 2082 2085 2088 2091 2094 2097 2100 2103 2106 2109 2112 2115 2118 2121 2124 2127 2130 2133 2136 2139 2142 2145 2148 2151 2154 2157 2160 2163 2166 2169 2172 2175 2178 2181 2184 2187 2190 2193 2196 2199 2202 2205 2208 2211 2214 2217 2220 2223 2226 2229 2232 2235 2238 2241 2244 2247 2250 2253 2256 2259 2262 2265 2268 2271 2274 2277 2280 2283 2286 2289 2292 2295 2298 2301 2304 2307 2310 2313 2316 2319 2322 2325 2328 2331 2334 2337 2340 2343 2346 2349 2352 2355 2358 2361 2364 2367 2370 2373 2376 2379 2382 2385 2388 2391 2394 2397 2400 2403 2406 2409 2412 2415 2418 2421 2424 2427 2430 2433 2436 2439 2442 2445 2448 2451 2454 2457 2460 2463 2466 2469 2472 2475 2478 2481 2484 2487 2490 2493 2496 2499 2502 2505 2508 2511 2514 2517 2520 2523 2526 2529 2532 2535 2538 2541 2544 2547 2550 2553 2556 2559 2562 2565 2568 2571 2574 2577 2580 2583 2586 2589 2592 2595 2598 2601 2604 2607 2610 2613 2616 2619 2622 2625 2628 2631 2634 2637 2640 2643 2646 2649 2652 2655 2658 2661 2664 2667 2670 2673 2676 2679 2682 2685 2688 2691 2694 2697 2700 2703 2706 2709 2712 2715 2718 2721 2724 2727 2730 2733 2736 2739 2742 2745 2748 2751 2754 2757 2760 2763 2766 2769 2772 2775 2778 2781 2784 2787 2790 2793 2796 2799 2802 2805 2808 2811 2814 2817 2820 2823 2826 2829 2832 2835 2838 2841 2844 2847 2850 2853 2856 2859 2862 2865 2868 2871 2874 2877 2880 2883 2886 2889 2892 2895 2898 2901 2904 2907 2910 2913 2916 2919 2922 2925 2928 2931 2934 2937 2940 2943 2946 2949 2952 2955 2958 2961 2964 2967 2970 2973 2976 2979 2982 2985 2988 2991 2994 2997 
Executed program succesfully.
```

then finally ... additional info:

```[root@future-yaxxie ocltest]# dnf list installed | grep ROCm
comgr.x86_64                           0.0.0-1                         @ROCm    
hip_base.x86_64                        1.5.18353-1                     @ROCm    
hip_doc.x86_64                         1.5.18353-1                     @ROCm    
hip_hcc.x86_64                         1.5.18353-1                     @ROCm    
hip_samples.x86_64                     1.5.18353-1                     @ROCm    
hipblas.x86_64                         0.10.3.1-1                      @ROCm    
hsa-amd-aqlprofile.x86_64              1.0.0-1                         @ROCm    
hsa-ext-rocr-dev.x86_64                1.1.9_9_ge4ab040-1              @ROCm    
hsa-rocr-dev.x86_64                    1.1.9_9_ge4ab040-1              @ROCm    
hsakmt-roct.x86_64                     1.0.9_8_g238782c-1              @ROCm    
hsakmt-roct-dev.x86_64                 1.0.9_8_g238782c-1              @ROCm    
rocblas.x86_64                         0.14.2.4-1                      @ROCm    
rocfft.x86_64                          0.8.6.0-1                       @ROCm    
rocm-clang-ocl.x86_64                  0.3.0_7997136-1                 @ROCm    
rocm-cmake.x86_64                      0.2.0_5e74c90-1                 @ROCm    
rocm-dev.x86_64                        1.9.211-1                       @ROCm    
rocm-device-libs.x86_64                0.0.1-1                         @ROCm    
rocm-libs.x86_64                       1.9.211-1                       @ROCm    
rocm-opencl.x86_64                     1.2.0-2018090742                @ROCm    
rocm-opencl-devel.x86_64               1.2.0-2018090742                @ROCm    
rocm-profiler.x86_64                   5.4.6878-g15f6673               @ROCm    
rocm-smi.x86_64                        1.0.0_72_gec1da05-1             @ROCm    
rocm-utils.x86_64                      1.9.211-1                       @ROCm    
rocminfo.x86_64                        1.0.0-1                         @ROCm    
rocr_debug_agent.x86_64                1.0.0-1                         @ROCm    
rocrand.x86_64                         1.8.1-1                         @ROCm    
[root@future-yaxxie ocltest]# uname -a
Linux future-yaxxie 4.18.12-200.fc28.x86_64 #1 SMP Thu Oct 4 15:46:35 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
[root@future-yaxxie ocltest]# which clang
/opt/rocm/opencl/bin/x86_64/clang
[root@future-yaxxie ocltest]# 
```

I'd write it up if it were working, but it isn't...

---

### 评论 #11 — yaxxie (2018-10-17T19:51:11Z)

You know what ignore all that, I had loads of OpenCL trash laying around on my system from previous attempts to make it work -- once I binned them it worked like a charm.

---

### 评论 #12 — yaxxie (2018-10-17T20:11:50Z)

After going through my shell history I distilled it down to this (which means it actually wasn't too difficult)
Fedora 28

```# Do the business of setting up the rocm repo
vi /etc/yum.repos.d/rocm.repo

# Install prereqs for hcc
dnf install npth-devel hsa-ext-rocr-dev rocm-utils
# force hcc installation
dnf download hcc
rpm -ifvh  hcc-1.2.18354-Linux.rpm --nodeps

dnf install hsa-rocr-dev rocm-profiler rocm-opencl-devel rocm-cmake rocminfo rocm-dev  rocm-libs rocm-utils rocm-clang-ocl clang-devel cxlactivitylogger miopengemm miopen-hip 

# These probably gave me some trouble
dnf erase libclc pocl
# dunno if we need to get rid of this but I did, but it should be providing the intel CPU openCL
dnf erase  beignet
```

you might notice the miopen stuff, I was trying to run tensorflow-rocm, but it segfaults...
I'm going to play around some more and see if this is actually functioning (I'm going to try arrayfire next)

I should emphasise:
I didn't need to add udev rules
I didn't need to rebuild initramfs to load amdkfd
I didn't need to add users to video group


---

### 评论 #13 — chriselrod (2018-10-18T00:21:46Z)

Brilliant!
Just installed Fedora 29, followed your steps. Didn't realize I also had `libclc`, `pocl`, and `beignet` installed by default. I removed them.

The HelloWorld program runs successfully (and I don't see the line about it switching to the CPU).
However, when I try the [HIP examples](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/roc-1.9.x):
```
$ ./test_all.sh 

==== vectorAdd ====
rm -f ./vectoradd_hip.exe
rm -f vectoradd_hip.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
/opt/rocm/hip/bin/hipcc vectoradd_hip.o -o vectoradd_hip.exe
./vectoradd_hip.exe
make: *** [Makefile:30: test] Segmentation fault (core dumped)

==== gpu-burn ====
rm -rf build
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include  -c -o build/BurnKernel.o BurnKernel.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include  -c -o build/common.o common.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include  -c -o build/AmdGpuMonitor.o AmdGpuMonitor.cpp  
mkdir -p build
/opt/rocm/hip/bin/hipcc -I/opt/rocm/hip/include -I/opt/rocm/hcc/include  -c -o build/gpuburn.o gpuburn.cpp  
/opt/rocm/hip/bin/hipcc -lm -o build/gpuburn-hip build/BurnKernel.o build/common.o build/AmdGpuMonitor.o build/gpuburn.o
./test_all.sh: line 19:  5698 Segmentation fault      (core dumped) ./build/gpuburn-hip -t 5

==== strided-access ====
rm -f strided-access *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o strided-access benchmark-hip.cpp 
./test_all.sh: line 28:  6316 Segmentation fault      (core dumped) ./strided-access

==== rtm8 ====
Using HIP_PATH=/opt/rocm/hip
hipcc -std=c++11 -O3 -o rtm8_hip rtm8.cpp
./test_all.sh: line 37:  6885 Segmentation fault      (core dumped) ./rtm8_hip

==== reduction ====
rm -f reduction *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o reduction reduction.cpp 
./reduction 1024*1024*4
./run.sh: line 4:  7470 Segmentation fault      (core dumped) ./$EXE $K
./reduction 8388608
./run.sh: line 4:  7474 Segmentation fault      (core dumped) ./$EXE $K
./reduction 16777216
./run.sh: line 4:  7489 Segmentation fault      (core dumped) ./$EXE $K
./reduction 33554432
./run.sh: line 4:  7505 Segmentation fault      (core dumped) ./$EXE $K
./reduction 67108864
./run.sh: line 4:  7518 Segmentation fault      (core dumped) ./$EXE $K
./reduction 134217728
./run.sh: line 4:  7527 Segmentation fault      (core dumped) ./$EXE $K
./reduction 268435456
./run.sh: line 4:  7543 Segmentation fault      (core dumped) ./$EXE $K
./reduction 536870912
./run.sh: line 4:  7556 Segmentation fault      (core dumped) ./$EXE $K

==== mini-nbody ====
hipcc -I../ -DSHMOO nbody-orig.cpp -o nbody-orig
./nbody-orig 1024
./HIP-nbody-orig.sh: line 32:  8156 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 2048
./HIP-nbody-orig.sh: line 32:  8160 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 4096
./HIP-nbody-orig.sh: line 32:  8173 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 8192
./HIP-nbody-orig.sh: line 32:  8202 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 16384
./HIP-nbody-orig.sh: line 32:  8215 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 32768
./HIP-nbody-orig.sh: line 32:  8228 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 65536
./HIP-nbody-orig.sh: line 32:  8254 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 131072
./HIP-nbody-orig.sh: line 32:  8267 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 262144
./HIP-nbody-orig.sh: line 32:  8288 Segmentation fault      (core dumped) ./$EXE $K
./nbody-orig 524288
./HIP-nbody-orig.sh: line 32:  8304 Segmentation fault      (core dumped) ./$EXE $K
hipcc -I../ -DSHMOO nbody-soa.cpp -o nbody-soa
./nbody-soa 1024
./HIP-nbody-soa.sh: line 34:  8880 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 2048
./HIP-nbody-soa.sh: line 34:  8884 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 4096
./HIP-nbody-soa.sh: line 34:  8898 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 8192
./HIP-nbody-soa.sh: line 34:  8912 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 16384
./HIP-nbody-soa.sh: line 34:  8925 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 32768
./HIP-nbody-soa.sh: line 34:  8938 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 65536
./HIP-nbody-soa.sh: line 34:  8960 Segmentation fault      (core dumped) ./$EXE $K
./nbody-soa 131072
./HIP-nbody-soa.sh: line 34:  8972 Segmentation fault      (core dumped) ./$EXE $K
hipcc -I../ -DSHMOO nbody-block.cpp -o nbody-block
./nbody-block 1024
./HIP-nbody-block.sh: line 34:  9558 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 2048
./HIP-nbody-block.sh: line 34:  9563 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 4096
./HIP-nbody-block.sh: line 34:  9576 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 8192
./HIP-nbody-block.sh: line 34:  9589 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 16384
./HIP-nbody-block.sh: line 34:  9598 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 32768
./HIP-nbody-block.sh: line 34:  9610 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 65536
./HIP-nbody-block.sh: line 34:  9619 Segmentation fault      (core dumped) ./$EXE $K
./nbody-block 131072
./HIP-nbody-block.sh: line 34:  9641 Segmentation fault      (core dumped) ./$EXE $K

==== add4 ====
rm -f   gpu-stream-hip *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -c hip-stream.cpp -o hip-stream.o
g++ -std=c++11 -O3   -c -o common.o common.cpp
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 common.o hip-stream.o -lm -o gpu-stream-hip
./gpu-stream-hip
./runhip.sh: line 2: 10276 Segmentation fault      (core dumped) ./gpu-stream-hip
./gpu-stream-hip --groups 256 --groupSize 256
./runhip.sh: line 4: 10280 Segmentation fault      (core dumped) ./gpu-stream-hip --groups 256 --groupSize 256
./gpu-stream-hip --float
./runhip.sh: line 6: 10293 Segmentation fault      (core dumped) ./gpu-stream-hip --float
./gpu-stream-hip --float --groups 256 --groupSize 256
./runhip.sh: line 8: 10306 Segmentation fault      (core dumped) ./gpu-stream-hip --float --groups 256 --groupSize 256

==== cuda-stream ====
rm -f stream *.o
/opt/rocm/hip/bin/hipcc -std=c++11 -O3 -o stream stream.cpp 
./test_all.sh: line 72: 10878 Segmentation fault      (core dumped) ./stream

==== Rodinia ====
\033[0;35m--CLEAN: nw\033[0m
\033[0;35m--CLEAN: gaussian\033[0m
\033[0;35m--CLEAN: myocyte\033[0m
\033[0;35m--CLEAN: hybridsort\033[0m
\033[0;35m--CLEAN: hotspot\033[0m
\033[0;35m--CLEAN: nn\033[0m
\033[0;35m--CLEAN: pathfinder\033[0m
\033[0;35m--CLEAN: streamcluster\033[0m
\033[0;35m--CLEAN: kmeans\033[0m
\033[0;35m--CLEAN: heartwall\033[0m
\033[0;35m--CLEAN: b+tree\033[0m
\033[0;35m--CLEAN: dwt2d\033[0m
\033[0;35m--CLEAN: lud\033[0m
\033[0;35m--CLEAN: srad\033[0m
\033[0;35m--CLEAN: bfs\033[0m
\033[0;35m--CLEAN: lavaMD\033[0m
\033[0;35m--CLEAN: backprop\033[0m
\033[0;35m--CLEAN: cfd\033[0m
\033[0;35m--TESTING: nw\033[0m
executing: ../../test/nw/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: gaussian\033[0m
executing: ../../test/gaussian/run3.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/gaussian/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/gaussian/run4.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/gaussian/run1.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/gaussian/run2.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: myocyte\033[0m
executing: ../../test/myocyte/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: hybridsort\033[0m
executing: ../../test/hybridsort/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: hotspot\033[0m
executing: ../../test/hotspot/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: nn\033[0m
executing: ../../test/nn/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: pathfinder\033[0m
executing: ../../test/pathfinder/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: streamcluster\033[0m
executing: ../../test/streamcluster/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: kmeans\033[0m
executing: ../../test/kmeans/run3.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/kmeans/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/kmeans/run1.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/kmeans/run2.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: heartwall\033[0m
executing: ../../test/heartwall/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: b+tree\033[0m
executing: ../../test/b+tree/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: dwt2d\033[0m
executing: ../../test/dwt2d/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/dwt2d/run1.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: lud\033[0m
executing: ../../test/lud/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: srad\033[0m
executing: ../../test/srad/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: bfs\033[0m
executing: ../../test/bfs/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/bfs/run1.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: lavaMD\033[0m
executing: ../../test/lavaMD/run3.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/lavaMD/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/lavaMD/run4.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/lavaMD/run1.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/lavaMD/run2.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: backprop\033[0m
executing: ../../test/backprop/run0.cmd...      \033[0;31mFAILED!\033[0m
\033[0;35m--TESTING: cfd\033[0m
executing: ../../test/cfd/run0.cmd...      \033[0;31mFAILED!\033[0m
executing: ../../test/cfd/run1.cmd...      \033[0;31mFAILED!\033[0m
```

A wall of segmentation faults. Also a little funny to see a `.exe` executable in `vectorAdd`.


I replaced my Debian install with this Fedora. With Debian, I couldn't/didn't bother to get a normal TensorFlow install to work; lots of missing dependencies, like openssl 1.0.0, while only 1.0.2 was available from libraries.
Docker worked fine though, so I went that route.

I'm not optimistic now though, given the failure of all the HIP examples.
```
Thread 1 "vectoradd_hip.e" received signal SIGSEGV, Segmentation fault.
__memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:376
376		VMOVU	-VEC_SIZE(%rsi, %rdx), %VEC(5)
(gdb) backtrace
#0  __memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:376
#1  0x00007ffff7f47495 in std::char_traits<char>::copy (__n=4273264, __s2=<optimized out>, __s1=<optimized out>)
    at /usr/src/debug/gcc-8.2.1-4.fc29.x86_64/obj-x86_64-redhat-linux/x86_64-redhat-linux/libstdc++-v3/include/bits/char_traits.h:350
#2  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_S_copy (__n=4273264, __s=<optimized out>, 
    __d=<optimized out>)
    at /usr/src/debug/gcc-8.2.1-4.fc29.x86_64/obj-x86_64-redhat-linux/x86_64-redhat-linux/libstdc++-v3/include/bits/basic_string.h:340
```

---

### 评论 #14 — yaxxie (2018-10-18T09:07:02Z)

> I'm not optimistic now though, given the failure of all the HIP examples.

Its not that it won't work (I'm going to try source build tonight), it just seems like the RPM distribution won't work (Which is a shame) -- although actually if you're only looking for OpenCL (unlikely at this point) it does look like it works (I tried the arrayfire openCL examples, seemed to work fine)

---

### 评论 #15 — chriselrod (2018-10-18T21:45:13Z)

Hmm, how is that going?

I wish I'd tried a few more examples on Debian before switching to Fedora, so I'd have more reference points.
Before uninstalling hcc and trying to compile it from source, I figured I'd try the [saxpy hcc example](https://github.com/RadeonOpenCompute/hcc/wiki#how-to-use-hcc).
```
$ hcc -hc saxpy.cpp -o saxpy
ld: /tmp/saxpy-a33022.o: in function `hc::completion_future hc::parallel_for_each<main::$_2>(hc::accelerator_view const&, hc::extent<1> const&, main::$_2 const&)':
saxpy.cpp:(.text+0xcf5c): undefined reference to `Kalmar::CLAMP::CreateKernel(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, Kalmar::KalmarQueue*)'
clang-7: error: linker command failed with exit code 1 (use -v to see invocation)

$ hcc -hc -I/opt/rocm/hcc/include saxpy.cpp -o saxpy
ld: /tmp/saxpy-0b561d.o: in function `hc::completion_future hc::parallel_for_each<main::$_2>(hc::accelerator_view const&, hc::extent<1> const&, main::$_2 const&)':
saxpy.cpp:(.text+0xcf5c): undefined reference to `Kalmar::CLAMP::CreateKernel(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, Kalmar::KalmarQueue*)'
clang-7: error: linker command failed with exit code 1 (use -v to see invocation)
```
I don't know C++ very well, so I was expecting including the directory that contains [kalmar_launch.h](https://github.com/RadeonOpenCompute/hcc/blob/4c23c46c418ef2cbbc2d57a23665383856ebee44/include/kalmar_launch.h) and company to solve this undefined reference.

EDIT:
Verbose version
```
$ hcc -hc saxpy.cpp -c -o saxpy.cpp.o
$ hcc -hc -v saxpy.cpp.o -o saxpy
HCC clang version 7.0.0 (ssh://gerritgit/compute/ec/hcc-tot/clang e2b51bfd063e4ccd426b64290bdc1587f2bf855a) (ssh://gerritgit/compute/ec/hcc-tot/llvm 009cb63e6e67f60303e7b11642113db848619871) (based on HCC 1.2.18354-ec91fed-e2b51bf-009cb63 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/bin
Found candidate GCC installation: /usr/lib/gcc/x86_64-redhat-linux/8
Selected GCC installation: /usr/lib/gcc/x86_64-redhat-linux/8
Candidate multilib: .;@m64
Candidate multilib: 32;@m32
Selected multilib: .;@m64
Found HCC installation: /opt/rocm/bin/..
 "/opt/rocm/hcc/bin/clamp-link" --verbose -lstdc++ -L/opt/rocm/bin/../lib --rpath=/opt/rocm/bin/../lib -ldl -lm -lpthread -lhc_am -lmcwamp --amdgpu-target=gfx900 --hash-style=gnu --no-add-needed --eh-frame-hdr -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o saxpy /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crt1.o /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crti.o /usr/lib/gcc/x86_64-redhat-linux/8/crtbegin.o -L/usr/lib/gcc/x86_64-redhat-linux/8 -L/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64 -L/lib/../lib64 -L/usr/lib/../lib64 -L/usr/lib/gcc/x86_64-redhat-linux/8/../../.. -L/opt/rocm/hcc/bin/../lib -L/lib -L/usr/lib saxpy.cpp.o -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-redhat-linux/8/crtend.o /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crtn.o -lclang_rt.builtins-x86_64
AMDGPU target array: gfx900

new kernel args: /tmp/tmp.g8tKVcQ5Oj/mcwamp.cpp.kernel.bc /tmp/tmp.g8tKVcQ5Oj/saxpy.cpp.kernel.bc

new host args: /tmp/tmp.g8tKVcQ5Oj/mcwamp.cpp.host.o /tmp/tmp.g8tKVcQ5Oj/saxpy.cpp.host.o

new other args: --verbose -lstdc++ -L/opt/rocm/bin/../lib --rpath=/opt/rocm/bin/../lib -ldl -lm -lpthread -lhc_am --hash-style=gnu --no-add-needed --eh-frame-hdr -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o saxpy /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crt1.o /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crti.o /usr/lib/gcc/x86_64-redhat-linux/8/crtbegin.o -L/usr/lib/gcc/x86_64-redhat-linux/8 -L/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64 -L/lib/../lib64 -L/usr/lib/../lib64 -L/usr/lib/gcc/x86_64-redhat-linux/8/../../.. -L/opt/rocm/hcc/bin/../lib -L/lib -L/usr/lib -lstdc++ -lm -lgcc_s -lgcc -lc -lgcc_s -lgcc /usr/lib/gcc/x86_64-redhat-linux/8/crtend.o /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crtn.o -lclang_rt.builtins-x86_64

Generating AMD GCN kernel
Finished generation of AMD GCN kernels
GNU ld version 2.31.1-13.fc29
  Supported emulations:
   elf_x86_64
   elf32_x86_64
   elf_i386
   elf_iamcu
   elf_l1om
   elf_k1om
   i386pep
   i386pe
using internal linker script:
==================================================
/* Script for -z combreloc -z separate-code: combine and sort reloc sections with separate code segment */
/* Copyright (C) 2014-2018 Free Software Foundation, Inc.
   Copying and distribution of this script, with or without modification,
   are permitted in any medium without royalty provided the copyright
   notice and this notice are preserved.  */
OUTPUT_FORMAT("elf64-x86-64", "elf64-x86-64",
	      "elf64-x86-64")
OUTPUT_ARCH(i386:x86-64)
ENTRY(_start)
SEARCH_DIR("=/usr/x86_64-redhat-linux/lib64"); SEARCH_DIR("=/usr/lib64"); SEARCH_DIR("=/usr/local/lib64"); SEARCH_DIR("=/lib64"); SEARCH_DIR("=/usr/x86_64-redhat-linux/lib"); SEARCH_DIR("=/usr/local/lib"); SEARCH_DIR("=/lib"); SEARCH_DIR("=/usr/lib");
SECTIONS
{
  /* Read-only sections, merged into text segment: */
  PROVIDE (__executable_start = SEGMENT_START("text-segment", 0x400000)); . = SEGMENT_START("text-segment", 0x400000) + SIZEOF_HEADERS;
  .interp         : { *(.interp) }
  .note.gnu.build-id : { *(.note.gnu.build-id) }
  .hash           : { *(.hash) }
  .gnu.hash       : { *(.gnu.hash) }
  .dynsym         : { *(.dynsym) }
  .dynstr         : { *(.dynstr) }
  .gnu.version    : { *(.gnu.version) }
  .gnu.version_d  : { *(.gnu.version_d) }
  .gnu.version_r  : { *(.gnu.version_r) }
  .rela.dyn       :
    {
      *(.rela.init)
      *(.rela.text .rela.text.* .rela.gnu.linkonce.t.*)
      *(.rela.fini)
      *(.rela.rodata .rela.rodata.* .rela.gnu.linkonce.r.*)
      *(.rela.data .rela.data.* .rela.gnu.linkonce.d.*)
      *(.rela.tdata .rela.tdata.* .rela.gnu.linkonce.td.*)
      *(.rela.tbss .rela.tbss.* .rela.gnu.linkonce.tb.*)
      *(.rela.ctors)
      *(.rela.dtors)
      *(.rela.got)
      *(.rela.bss .rela.bss.* .rela.gnu.linkonce.b.*)
      *(.rela.ldata .rela.ldata.* .rela.gnu.linkonce.l.*)
      *(.rela.lbss .rela.lbss.* .rela.gnu.linkonce.lb.*)
      *(.rela.lrodata .rela.lrodata.* .rela.gnu.linkonce.lr.*)
      *(.rela.ifunc)
    }
  .rela.plt       :
    {
      *(.rela.plt)
      PROVIDE_HIDDEN (__rela_iplt_start = .);
      *(.rela.iplt)
      PROVIDE_HIDDEN (__rela_iplt_end = .);
    }
  . = ALIGN(CONSTANT (MAXPAGESIZE));
  .init           :
  {
    KEEP (*(SORT_NONE(.init)))
  }
  .plt            : { *(.plt) *(.iplt) }
.plt.got        : { *(.plt.got) }
.plt.sec        : { *(.plt.sec) }
  .text           :
  {
    *(.text.unlikely .text.*_unlikely .text.unlikely.*)
    *(.text.exit .text.exit.*)
    *(.text.startup .text.startup.*)
    *(.text.hot .text.hot.*)
    *(.text .stub .text.* .gnu.linkonce.t.*)
    /* .gnu.warning sections are handled specially by elf32.em.  */
    *(.gnu.warning)
  }
  .fini           :
  {
    KEEP (*(SORT_NONE(.fini)))
  }
  PROVIDE (__etext = .);
  PROVIDE (_etext = .);
  PROVIDE (etext = .);
  . = ALIGN(CONSTANT (MAXPAGESIZE));
  /* Adjust the address for the rodata segment.  We want to adjust up to
     the same address within the page on the next page up.  */
  . = SEGMENT_START("rodata-segment", ALIGN(CONSTANT (MAXPAGESIZE)) + (. & (CONSTANT (MAXPAGESIZE) - 1)));
  .rodata         : { *(.rodata .rodata.* .gnu.linkonce.r.*) }
  .rodata1        : { *(.rodata1) }
  .eh_frame_hdr : { *(.eh_frame_hdr) *(.eh_frame_entry .eh_frame_entry.*) }
  .eh_frame       : ONLY_IF_RO { KEEP (*(.eh_frame)) *(.eh_frame.*) }
  .gcc_except_table   : ONLY_IF_RO { *(.gcc_except_table
  .gcc_except_table.*) }
  .gnu_extab   : ONLY_IF_RO { *(.gnu_extab*) }
  /* These sections are generated by the Sun/Oracle C++ compiler.  */
  .exception_ranges   : ONLY_IF_RO { *(.exception_ranges
  .exception_ranges*) }
  /* Adjust the address for the data segment.  We want to adjust up to
     the same address within the page on the next page up.  */
  . = DATA_SEGMENT_ALIGN (CONSTANT (MAXPAGESIZE), CONSTANT (COMMONPAGESIZE));
  /* Exception handling  */
  .eh_frame       : ONLY_IF_RW { KEEP (*(.eh_frame)) *(.eh_frame.*) }
  .gnu_extab      : ONLY_IF_RW { *(.gnu_extab) }
  .gcc_except_table   : ONLY_IF_RW { *(.gcc_except_table .gcc_except_table.*) }
  .exception_ranges   : ONLY_IF_RW { *(.exception_ranges .exception_ranges*) }
  /* Thread Local Storage sections  */
  .tdata	  :
   {
     PROVIDE_HIDDEN (__tdata_start = .);
     *(.tdata .tdata.* .gnu.linkonce.td.*)
   }
  .tbss		  : { *(.tbss .tbss.* .gnu.linkonce.tb.*) *(.tcommon) }
  .preinit_array     :
  {
    PROVIDE_HIDDEN (__preinit_array_start = .);
    KEEP (*(.preinit_array))
    PROVIDE_HIDDEN (__preinit_array_end = .);
  }
  .init_array     :
  {
    PROVIDE_HIDDEN (__init_array_start = .);
    KEEP (*(SORT_BY_INIT_PRIORITY(.init_array.*) SORT_BY_INIT_PRIORITY(.ctors.*)))
    KEEP (*(.init_array EXCLUDE_FILE (*crtbegin.o *crtbegin?.o *crtend.o *crtend?.o ) .ctors))
    PROVIDE_HIDDEN (__init_array_end = .);
  }
  .fini_array     :
  {
    PROVIDE_HIDDEN (__fini_array_start = .);
    KEEP (*(SORT_BY_INIT_PRIORITY(.fini_array.*) SORT_BY_INIT_PRIORITY(.dtors.*)))
    KEEP (*(.fini_array EXCLUDE_FILE (*crtbegin.o *crtbegin?.o *crtend.o *crtend?.o ) .dtors))
    PROVIDE_HIDDEN (__fini_array_end = .);
  }
  .ctors          :
  {
    /* gcc uses crtbegin.o to find the start of
       the constructors, so we make sure it is
       first.  Because this is a wildcard, it
       doesn't matter if the user does not
       actually link against crtbegin.o; the
       linker won't look for a file to match a
       wildcard.  The wildcard also means that it
       doesn't matter which directory crtbegin.o
       is in.  */
    KEEP (*crtbegin.o(.ctors))
    KEEP (*crtbegin?.o(.ctors))
    /* We don't want to include the .ctor section from
       the crtend.o file until after the sorted ctors.
       The .ctor section from the crtend file contains the
       end of ctors marker and it must be last */
    KEEP (*(EXCLUDE_FILE (*crtend.o *crtend?.o ) .ctors))
    KEEP (*(SORT(.ctors.*)))
    KEEP (*(.ctors))
  }
  .dtors          :
  {
    KEEP (*crtbegin.o(.dtors))
    KEEP (*crtbegin?.o(.dtors))
    KEEP (*(EXCLUDE_FILE (*crtend.o *crtend?.o ) .dtors))
    KEEP (*(SORT(.dtors.*)))
    KEEP (*(.dtors))
  }
  .jcr            : { KEEP (*(.jcr)) }
  .data.rel.ro : { *(.data.rel.ro.local* .gnu.linkonce.d.rel.ro.local.*) *(.data.rel.ro .data.rel.ro.* .gnu.linkonce.d.rel.ro.*) }
  .dynamic        : { *(.dynamic) }
  .got            : { *(.got) *(.igot) }
  . = DATA_SEGMENT_RELRO_END (SIZEOF (.got.plt) >= 24 ? 24 : 0, .);
  .got.plt        : { *(.got.plt)  *(.igot.plt) }
  .data           :
  {
    *(.data .data.* .gnu.linkonce.d.*)
    SORT(CONSTRUCTORS)
  }
  .data1          : { *(.data1) }
  _edata = .; PROVIDE (edata = .);
  . = .;
  __bss_start = .;
  .bss            :
  {
   *(.dynbss)
   *(.bss .bss.* .gnu.linkonce.b.*)
   *(COMMON)
   /* Align here to ensure that the .bss section occupies space up to
      _end.  Align after .bss to ensure correct alignment even if the
      .bss section disappears because there are no input sections.
      FIXME: Why do we need it? When there is no .bss section, we don't
      pad the .data section.  */
   . = ALIGN(. != 0 ? 64 / 8 : 1);
  }
  .lbss   :
  {
    *(.dynlbss)
    *(.lbss .lbss.* .gnu.linkonce.lb.*)
    *(LARGE_COMMON)
  }
  . = ALIGN(64 / 8);
  . = SEGMENT_START("ldata-segment", .);
  .lrodata   ALIGN(CONSTANT (MAXPAGESIZE)) + (. & (CONSTANT (MAXPAGESIZE) - 1)) :
  {
    *(.lrodata .lrodata.* .gnu.linkonce.lr.*)
  }
  .ldata   ALIGN(CONSTANT (MAXPAGESIZE)) + (. & (CONSTANT (MAXPAGESIZE) - 1)) :
  {
    *(.ldata .ldata.* .gnu.linkonce.l.*)
    . = ALIGN(. != 0 ? 64 / 8 : 1);
  }
  . = ALIGN(64 / 8);
  _end = .; PROVIDE (end = .);
  . = DATA_SEGMENT_END (.);
  /* Stabs debugging sections.  */
  .stab          0 : { *(.stab) }
  .stabstr       0 : { *(.stabstr) }
  .stab.excl     0 : { *(.stab.excl) }
  .stab.exclstr  0 : { *(.stab.exclstr) }
  .stab.index    0 : { *(.stab.index) }
  .stab.indexstr 0 : { *(.stab.indexstr) }
  .comment       0 : { *(.comment) }
  .gnu.build.attributes : { *(.gnu.build.attributes .gnu.build.attributes.*) }
  /* DWARF debug sections.
     Symbols in the DWARF debugging sections are relative to the beginning
     of the section so we begin them at 0.  */
  /* DWARF 1 */
  .debug          0 : { *(.debug) }
  .line           0 : { *(.line) }
  /* GNU DWARF 1 extensions */
  .debug_srcinfo  0 : { *(.debug_srcinfo) }
  .debug_sfnames  0 : { *(.debug_sfnames) }
  /* DWARF 1.1 and DWARF 2 */
  .debug_aranges  0 : { *(.debug_aranges) }
  .debug_pubnames 0 : { *(.debug_pubnames) }
  /* DWARF 2 */
  .debug_info     0 : { *(.debug_info .gnu.linkonce.wi.*) }
  .debug_abbrev   0 : { *(.debug_abbrev) }
  .debug_line     0 : { *(.debug_line .debug_line.* .debug_line_end ) }
  .debug_frame    0 : { *(.debug_frame) }
  .debug_str      0 : { *(.debug_str) }
  .debug_loc      0 : { *(.debug_loc) }
  .debug_macinfo  0 : { *(.debug_macinfo) }
  /* SGI/MIPS DWARF 2 extensions */
  .debug_weaknames 0 : { *(.debug_weaknames) }
  .debug_funcnames 0 : { *(.debug_funcnames) }
  .debug_typenames 0 : { *(.debug_typenames) }
  .debug_varnames  0 : { *(.debug_varnames) }
  /* DWARF 3 */
  .debug_pubtypes 0 : { *(.debug_pubtypes) }
  .debug_ranges   0 : { *(.debug_ranges) }
  /* DWARF Extension.  */
  .debug_macro    0 : { *(.debug_macro) }
  .debug_addr     0 : { *(.debug_addr) }
  .gnu.attributes 0 : { KEEP (*(.gnu.attributes)) }
  /DISCARD/ : { *(.note.GNU-stack) *(.gnu_debuglink) *(.gnu.lto_*) }
}


==================================================
attempt to open /tmp/tmp.g8tKVcQ5Oj/kernel_hsa.o succeeded
/tmp/tmp.g8tKVcQ5Oj/kernel_hsa.o
attempt to open /tmp/tmp.g8tKVcQ5Oj/mcwamp.cpp.host.o succeeded
/tmp/tmp.g8tKVcQ5Oj/mcwamp.cpp.host.o
attempt to open /tmp/tmp.g8tKVcQ5Oj/saxpy.cpp.host.o succeeded
/tmp/tmp.g8tKVcQ5Oj/saxpy.cpp.host.o
attempt to open /opt/rocm/bin/../lib/libstdc++.so failed
attempt to open /opt/rocm/bin/../lib/libstdc++.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libstdc++.so succeeded
-lstdc++ (/usr/lib/gcc/x86_64-redhat-linux/8/libstdc++.so)
attempt to open /opt/rocm/bin/../lib/libdl.so failed
attempt to open /opt/rocm/bin/../lib/libdl.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libdl.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libdl.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libdl.so succeeded
-ldl (/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libdl.so)
attempt to open /opt/rocm/bin/../lib/libm.so failed
attempt to open /opt/rocm/bin/../lib/libm.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libm.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libm.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so succeeded
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so
attempt to open //lib64/libm.so.6 succeeded
/lib64/libm.so.6 (//lib64/libm.so.6)
attempt to open //usr/lib64/libmvec_nonshared.a succeeded
attempt to open //lib64/libmvec.so.1 succeeded
/lib64/libmvec.so.1 (//lib64/libmvec.so.1)
/lib64/libmvec.so.1 (//lib64/libmvec.so.1)
attempt to open /opt/rocm/bin/../lib/libpthread.so failed
attempt to open /opt/rocm/bin/../lib/libpthread.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libpthread.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libpthread.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libpthread.so succeeded
-lpthread (/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libpthread.so)
attempt to open /opt/rocm/bin/../lib/libhc_am.so succeeded
-lhc_am (/opt/rocm/bin/../lib/libhc_am.so)
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crt1.o succeeded
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crt1.o
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crti.o succeeded
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crti.o
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/crtbegin.o succeeded
/usr/lib/gcc/x86_64-redhat-linux/8/crtbegin.o
attempt to open /opt/rocm/bin/../lib/libstdc++.so failed
attempt to open /opt/rocm/bin/../lib/libstdc++.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libstdc++.so succeeded
-lstdc++ (/usr/lib/gcc/x86_64-redhat-linux/8/libstdc++.so)
attempt to open /opt/rocm/bin/../lib/libm.so failed
attempt to open /opt/rocm/bin/../lib/libm.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libm.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libm.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so succeeded
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libm.so
attempt to open //lib64/libm.so.6 succeeded
/lib64/libm.so.6 (//lib64/libm.so.6)
attempt to open //usr/lib64/libmvec_nonshared.a succeeded
attempt to open //lib64/libmvec.so.1 succeeded
/lib64/libmvec.so.1 (//lib64/libmvec.so.1)
attempt to open /opt/rocm/bin/../lib/libgcc_s.so failed
attempt to open /opt/rocm/bin/../lib/libgcc_s.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc_s.so succeeded
-lgcc_s (/usr/lib/gcc/x86_64-redhat-linux/8/libgcc_s.so)
attempt to open /opt/rocm/bin/../lib/libgcc.so failed
attempt to open /opt/rocm/bin/../lib/libgcc.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc.a succeeded
attempt to open /opt/rocm/bin/../lib/libc.so failed
attempt to open /opt/rocm/bin/../lib/libc.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libc.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libc.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libc.so succeeded
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libc.so
opened script file /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libc.so
attempt to open //lib64/libc.so.6 succeeded
/lib64/libc.so.6 (//lib64/libc.so.6)
attempt to open //usr/lib64/libc_nonshared.a succeeded
(//usr/lib64/libc_nonshared.a)elf-init.oS
attempt to open //lib64/ld-linux-x86-64.so.2 succeeded
/lib64/ld-linux-x86-64.so.2 (//lib64/ld-linux-x86-64.so.2)
/lib64/ld-linux-x86-64.so.2 (//lib64/ld-linux-x86-64.so.2)
attempt to open /opt/rocm/bin/../lib/libgcc_s.so failed
attempt to open /opt/rocm/bin/../lib/libgcc_s.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc_s.so succeeded
-lgcc_s (/usr/lib/gcc/x86_64-redhat-linux/8/libgcc_s.so)
attempt to open /opt/rocm/bin/../lib/libgcc.so failed
attempt to open /opt/rocm/bin/../lib/libgcc.a failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc.so failed
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/libgcc.a succeeded
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/crtend.o succeeded
/usr/lib/gcc/x86_64-redhat-linux/8/crtend.o
attempt to open /usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crtn.o succeeded
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/crtn.o
attempt to open /opt/rocm/bin/../lib/libclang_rt.builtins-x86_64.so failed
attempt to open /opt/rocm/bin/../lib/libclang_rt.builtins-x86_64.a succeeded
ld-linux-x86-64.so.2 needed by /usr/lib/gcc/x86_64-redhat-linux/8/libstdc++.so
found ld-linux-x86-64.so.2 at //lib64/ld-linux-x86-64.so.2
libhsa-runtime64.so.1 needed by /opt/rocm/bin/../lib/libhc_am.so
attempt to open //opt/rocm/bin/../lib/libhsa-runtime64.so.1 failed
attempt to open /opt/rocm/lib/libhsa-runtime64.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/libhsa-runtime64.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/libhsa-runtime64.so.1 failed
attempt to open //opt/rocm/lib64/libhsa-runtime64.so.1 failed
attempt to open //usr/lib64//bind9-export/libhsa-runtime64.so.1 failed
attempt to open //opt/rocm/lib64/libhsa-runtime64.so.1 failed
attempt to open //opt/rocm/hiprand/lib/libhsa-runtime64.so.1 failed
found libhsa-runtime64.so.1 at //opt/rocm/hsa/lib/libhsa-runtime64.so.1
libhsakmt.so.1 needed by //opt/rocm/hsa/lib/libhsa-runtime64.so.1
attempt to open //opt/rocm/bin/../lib/libhsakmt.so.1 failed
attempt to open /opt/rocm/lib/libhsakmt.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/libhsakmt.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/libhsakmt.so.1 failed
found libhsakmt.so.1 at //opt/rocm/lib64/libhsakmt.so.1
libz.so.1 needed by //opt/rocm/hsa/lib/libhsa-runtime64.so.1
attempt to open //opt/rocm/bin/../lib/libz.so.1 failed
attempt to open /opt/rocm/lib/libz.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/libz.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/libz.so.1 failed
attempt to open //opt/rocm/lib64/libz.so.1 failed
attempt to open //usr/lib64//bind9-export/libz.so.1 failed
attempt to open //opt/rocm/lib64/libz.so.1 failed
attempt to open //opt/rocm/hiprand/lib/libz.so.1 failed
attempt to open //opt/rocm/hsa/lib/libz.so.1 failed
attempt to open //opt/rocm/hsa/lib/libz.so.1 failed
attempt to open //opt/rocm/hsa-amd-aqlprofile/lib/libz.so.1 failed
attempt to open //usr/lib64/iscsi/libz.so.1 failed
attempt to open //opt/rocm/lib64/libz.so.1 failed
attempt to open //usr/lib64/qt-3.3/lib/libz.so.1 failed
attempt to open //opt/rocm/lib/libz.so.1 failed
attempt to open //opt/rocm/lib/libz.so.1 failed
attempt to open //opt/rocm/rocrand/lib/libz.so.1 failed
attempt to open //opt/rocm/lib/libz.so.1 failed
attempt to open //opt/rocm/lib64/libz.so.1 failed
attempt to open //opt/rocm/opencl/lib/x86_64/libz.so.1 failed
attempt to open //usr/x86_64-redhat-linux/lib64/libz.so.1 failed
found libz.so.1 at //usr/lib64/libz.so.1
librt.so.1 needed by //opt/rocm/hsa/lib/libhsa-runtime64.so.1
attempt to open //opt/rocm/bin/../lib/librt.so.1 failed
attempt to open /opt/rocm/lib/librt.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/librt.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/librt.so.1 failed
attempt to open //opt/rocm/lib64/librt.so.1 failed
attempt to open //usr/lib64//bind9-export/librt.so.1 failed
attempt to open //opt/rocm/lib64/librt.so.1 failed
attempt to open //opt/rocm/hiprand/lib/librt.so.1 failed
attempt to open //opt/rocm/hsa/lib/librt.so.1 failed
attempt to open //opt/rocm/hsa/lib/librt.so.1 failed
attempt to open //opt/rocm/hsa-amd-aqlprofile/lib/librt.so.1 failed
attempt to open //usr/lib64/iscsi/librt.so.1 failed
attempt to open //opt/rocm/lib64/librt.so.1 failed
attempt to open //usr/lib64/qt-3.3/lib/librt.so.1 failed
attempt to open //opt/rocm/lib/librt.so.1 failed
attempt to open //opt/rocm/lib/librt.so.1 failed
attempt to open //opt/rocm/rocrand/lib/librt.so.1 failed
attempt to open //opt/rocm/lib/librt.so.1 failed
attempt to open //opt/rocm/lib64/librt.so.1 failed
attempt to open //opt/rocm/opencl/lib/x86_64/librt.so.1 failed
attempt to open //usr/x86_64-redhat-linux/lib64/librt.so.1 failed
found librt.so.1 at //usr/lib64/librt.so.1
libnuma.so.1 needed by //opt/rocm/lib64/libhsakmt.so.1
attempt to open //opt/rocm/bin/../lib/libnuma.so.1 failed
attempt to open /opt/rocm/lib/libnuma.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/libnuma.so.1 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/libnuma.so.1 failed
attempt to open //opt/rocm/lib64/libnuma.so.1 failed
attempt to open //usr/lib64//bind9-export/libnuma.so.1 failed
attempt to open //opt/rocm/lib64/libnuma.so.1 failed
attempt to open //opt/rocm/hiprand/lib/libnuma.so.1 failed
attempt to open //opt/rocm/hsa/lib/libnuma.so.1 failed
attempt to open //opt/rocm/hsa/lib/libnuma.so.1 failed
attempt to open //opt/rocm/hsa-amd-aqlprofile/lib/libnuma.so.1 failed
attempt to open //usr/lib64/iscsi/libnuma.so.1 failed
attempt to open //opt/rocm/lib64/libnuma.so.1 failed
attempt to open //usr/lib64/qt-3.3/lib/libnuma.so.1 failed
attempt to open //opt/rocm/lib/libnuma.so.1 failed
attempt to open //opt/rocm/lib/libnuma.so.1 failed
attempt to open //opt/rocm/rocrand/lib/libnuma.so.1 failed
attempt to open //opt/rocm/lib/libnuma.so.1 failed
attempt to open //opt/rocm/lib64/libnuma.so.1 failed
attempt to open //opt/rocm/opencl/lib/x86_64/libnuma.so.1 failed
attempt to open //usr/x86_64-redhat-linux/lib64/libnuma.so.1 failed
found libnuma.so.1 at //usr/lib64/libnuma.so.1
libpci.so.3 needed by //opt/rocm/lib64/libhsakmt.so.1
attempt to open //opt/rocm/bin/../lib/libpci.so.3 failed
attempt to open /opt/rocm/lib/libpci.so.3 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib64/libpci.so.3 failed
attempt to open //opt/rh/devtoolset-7/root/usr/lib/libpci.so.3 failed
attempt to open //opt/rocm/lib64/libpci.so.3 failed
attempt to open //usr/lib64//bind9-export/libpci.so.3 failed
attempt to open //opt/rocm/lib64/libpci.so.3 failed
attempt to open //opt/rocm/hiprand/lib/libpci.so.3 failed
attempt to open //opt/rocm/hsa/lib/libpci.so.3 failed
attempt to open //opt/rocm/hsa/lib/libpci.so.3 failed
attempt to open //opt/rocm/hsa-amd-aqlprofile/lib/libpci.so.3 failed
attempt to open //usr/lib64/iscsi/libpci.so.3 failed
attempt to open //opt/rocm/lib64/libpci.so.3 failed
attempt to open //usr/lib64/qt-3.3/lib/libpci.so.3 failed
attempt to open //opt/rocm/lib/libpci.so.3 failed
attempt to open //opt/rocm/lib/libpci.so.3 failed
attempt to open //opt/rocm/rocrand/lib/libpci.so.3 failed
attempt to open //opt/rocm/lib/libpci.so.3 failed
attempt to open //opt/rocm/lib64/libpci.so.3 failed
attempt to open //opt/rocm/opencl/lib/x86_64/libpci.so.3 failed
attempt to open //usr/x86_64-redhat-linux/lib64/libpci.so.3 failed
found libpci.so.3 at //usr/lib64/libpci.so.3
libresolv.so.2 needed by //usr/lib64/libpci.so.3
attempt to open //opt/rocm/bin/../lib/libresolv.so.2 failed
attempt to open /opt/rocm/lib/libresolv.so.2 failed
attempt to open //opt/rocm/lib64/libresolv.so.2 failed
attempt to open //usr/lib64//bind9-export/libresolv.so.2 failed
attempt to open //opt/rocm/lib64/libresolv.so.2 failed
attempt to open //opt/rocm/hiprand/lib/libresolv.so.2 failed
attempt to open //opt/rocm/hsa/lib/libresolv.so.2 failed
attempt to open //opt/rocm/hsa/lib/libresolv.so.2 failed
attempt to open //opt/rocm/hsa-amd-aqlprofile/lib/libresolv.so.2 failed
attempt to open //usr/lib64/iscsi/libresolv.so.2 failed
attempt to open //opt/rocm/lib64/libresolv.so.2 failed
attempt to open //usr/lib64/qt-3.3/lib/libresolv.so.2 failed
attempt to open //opt/rocm/lib/libresolv.so.2 failed
attempt to open //opt/rocm/lib/libresolv.so.2 failed
attempt to open //opt/rocm/rocrand/lib/libresolv.so.2 failed
attempt to open //opt/rocm/lib/libresolv.so.2 failed
attempt to open //opt/rocm/lib64/libresolv.so.2 failed
attempt to open //opt/rocm/opencl/lib/x86_64/libresolv.so.2 failed
attempt to open //usr/x86_64-redhat-linux/lib64/libresolv.so.2 failed
found libresolv.so.2 at //usr/lib64/libresolv.so.2
ld: /tmp/tmp.g8tKVcQ5Oj/saxpy.cpp.host.o: in function `hc::completion_future hc::parallel_for_each<main::$_2>(hc::accelerator_view const&, hc::extent<1> const&, main::$_2 const&)':
saxpy.cpp:(.text+0xcf5c): undefined reference to `Kalmar::CLAMP::CreateKernel(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, Kalmar::KalmarQueue*)'
clang-7: error: linker command failed with exit code 1 (use -v to see invocation)
```

EDIT:
On Ubuntu...
```
$ hcc -hc saxpy.cpp -o saxpy
objdump: /usr/lib/x86_64-linux-gnu/libm.a: file format not recognized
$ ls
saxpy  saxpy.cpp
$ ./saxpy 
0 errors
```

---

### 评论 #16 — chriselrod (2018-10-31T06:17:41Z)

I built hcc from source. Now:
```
$ /home/chriselrod/Documents/languages/hcc/build/bin/hcc -hc saxpy.cpp -o saxpy
objdump: /usr/lib64/libm.a: file format not recognized

$ ./saxpy 
0 errors
```
(For reference, the file format not recognized objdump has already been reported [here](https://github.com/RadeonOpenCompute/hcc/issues/874).)

---

### 评论 #17 — yaxxie (2018-10-31T18:44:32Z)

So did you compile hcc or whole runtime? Because this would indicate the runtime worked but I had segfaults with tensorflow-rocm and when I get time I need to figure out if I need to build the whole runtime and tensorflow or what 

---

### 评论 #18 — chriselrod (2018-10-31T19:26:44Z)

Just `hcc`. If you're only compiling hcc, be sure to checkout `roc-1.9.x` instead of "clang_tot_upgrade" like in the README, because the latest hcc is no longer compatible with the roc-1.9.x components you installed via
```
dnf install npth-devel hsa-ext-rocr-dev rocm-utils
```

Does [the OpenCL test](https://github.com/RadeonOpenCompute/ROCm#upon-restart-to-test-your-opencl-instance) work for you? It did for me, which is why I decided to start with just building hcc.

I have not yet tested tensorflow-rocm, but I will try at some point over the next week.
It's also worth trying if the tensorflow-rocm docker works.
Unfortunately docker-ce isn't available in the docker Fedora 29 repos yet. I'll go ahead and use one one of the workarounds (eg, using the F28 repo, or installing docker without dnf) if I run into some free time in the next week.

---

### 评论 #19 — yaxxie (2018-11-02T22:17:07Z)

Once I built hcc from source the saxypy example worked. OpenCL was already working before that (I built arrayfire and clinfo showed good outputs)

`tensorflow-rocm` still failed though, with a segfault when downloaded from pip. I can believe its due to `tensorflow-rocm` being compiled on different system but I couldn't build it myself, bazel is too fiddly. 

---

### 评论 #20 — acowley (2018-11-03T00:09:21Z)

I am able to run the `tensorflow-rocm` wheel on NixOS by setting its constituent libraries’ `rpath`s to pick up our built from source ROCm libraries, and then `LD_PRELOAD` to force our `libstdc++.so`. One or both of those may be needed on other distros, too.

---

### 评论 #21 — yaxxie (2018-11-04T22:47:21Z)

Thanks for the tip. It good to know it does actually work!
NixOS will be one of my targets once I manage this, but RPATH patching and LD_PRELOAD sounds way too hacky for my tastes, so I'd probably fight a bit more with bazel and see over in ROCmSoftwarePlatform/tensorflow-upstream what tricks I'm missing for building.

---

### 评论 #22 — yaxxie (2018-11-04T22:51:30Z)

Also In response to:

> It's also worth trying if the tensorflow-rocm docker works.

This worked for me, I was able to launch the container on a system with the runtime and the kernel drivers installed (although I' pretty sure one only needs the kernel drivers for passing through devices to the docker container)

---

### 评论 #23 — acowley (2018-11-04T23:22:03Z)

I also have a from-source build with bazel on NixOS, but haven’t pushed it to `nixos-rocm` as it’s worse, imho. The `fetch` phase [doesn’t reliably work](https://github.com/tensorflow/tensorflow/issues/22665#issuecomment-434133894) on the tensorflow source, and the rocm port includes many hard coded tool paths that need patching on NixOS, and then tensorflow tries very hard to statically link `libstdc++` which causes issues when it calls into your rocm libs.

I’ll still try to push the from-source derivation to the public repo, but it’s a remarkably slow build (~6 hours for me) and wasn’t ultimately more satisfying to me than making the wheel work. Hopefully the `fetch` issue will be resolved to reduce the ugly a bit.

---

### 评论 #24 — jlgreathouse (2018-12-25T00:23:03Z)

Hi @akostadinov 

While we do not yet have a binary repo that completely works with Fedora, we *do* now have tools in our [Experimental ROC project](https://github.com/RadeonOpenCompute/Experimental_ROC) that will install all of the open source ROCm user-land software on Fedora 28 and Fedora 29. This uses the upstream kernel driver, since the `rock-dkms` package does not currently build on the kernel versions that are in Fedora. However, ROCm should work on any the GPUs [described in this section of our README](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-support-in-upstream-linux-kernels).

Note that the Fedora install scripts give you two options:

1. Install mostly from RPM packages, except for HCC and HIP, which must be rebuilt from source. The scripts will do this automatically.
2. Install fully from source by pulling the ROCm 2.0 commits from our GitHub repositories.
  * Note that this lets you choose to install directly from the build or to build your own RPM packages

The project also has a few other scripts to help things like setting the proper permissions on `/dev/kfd` and putting users in the correct `video` groups, etc.

@yaxxie and @chriselrod -- I have to thank both of you, as your tests getting Fedora working were helped me hammer out the bugs in these scripts. :) You may want to try them out as well

In addition, you both may be interested in the following new documentation we put together that I put together to help describe the ROCm software stack, the programs it has in it, and what packages correspond to that software:

- [The ROCm platform and its software](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#the-latest-rocm-platform---rocm-20)
- [The binary packages in the ROCm platform](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-binary-package-structure)
- [Information about using the upstream driver](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-support-in-upstream-linux-kernels) vs `rock-dkms`
- [Updated manifest of the software commits that go into ROCm](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#getting-rocm-source-code)

---

### 评论 #25 — yaxxie (2019-01-02T22:31:05Z)

@jlgreathouse Thanks for sharing this!

Running it as I type (saves me the effort of rebuilding HIP and HCC for the failed upgrades).

One comment, I notice it did a `dnf install dkms` but we don't need that because we are using upstream and dont need the ROCK kernel drivers (as per docs)?

---

### 评论 #26 — jlgreathouse (2019-01-02T22:45:56Z)

Good catch. I'll admit that there was some copy & paste between Fedora and CentOS/RHEL to save myself a bunch of typing. Feel free to submit a PR to the Experimental_ROC repo. It's developed in the open, so we won't need to do any "AMD-internal vs. GitHub-hosted" repo juggling. :)

---

### 评论 #27 — yaxxie (2019-01-02T23:00:10Z)

PR submitted -- Do you have any comments about whether with rocm2 tensorflow-rocm wil lwork out of box or not? (I'm about to find out the hardway in an hour or two anyway) :)

---

### 评论 #28 — jlgreathouse (2019-01-02T23:02:55Z)

I'll admit that I haven't tested that. I would hope that it does, or our "build MIOpen etc. from source" isn't working properly. However, my goal for the distro install scripts was to recreate what we ship at repo.radeon.com, except from GitHub source. Our TF implementation isn't shipped that way, so it wasn't on my (overly full) TODO list. I also didn't go out of my way to test anything major except for batches of OpenCL, HCC, and HIP test apps to verify functionality.

---

### 评论 #29 — yaxxie (2019-01-02T23:12:22Z)

Not a problem, I'll just update when I know. Last time I tried it segfaulted and it looked like I needed to build from source (which I wasn't able to get going).

Thanks for your input though!

---

### 评论 #30 — buraksarac (2019-09-27T09:26:34Z)

Hi All,
 I was able to install 2.7.2 on Fedora30 (yum_2.7.2.tar.bz2  ) using Experimental Fedora 29 rpm install scripts as a guide and run most of commands manually. Overall things worked out out of box. I did not run any opencl app yet but looking forward to:) Problems I had faced during installation:

- extracting and installation of core rocm rpms went smoothly, I had to just track down missing deps

**hcc manual installation:**(https://github.com/RadeonOpenCompute/Experimental_ROC/blob/master/distro_install_scripts/Fedora/common/component_scripts/01_09_hcc.sh)
  

- I had to hardcode **MAX_THREADS**, script wasnt very generous by default , 32 thread took 20G of memory otherwise I stuck with 5 thread
-  _I believe only this issue critical_: during packaging phase CPack aggressively complained about python shebangs conflict for some files (i.e. rpt, hmaptool,run-find-all-symbols, ) and terminated process (https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error)

**rocm libs installation:**
 

- I have just removed trusth

**HIP examples:**

-  rocm agent enumerator was not in opt/rocm/bin but in /bin i had to create symlink

**After test:**
 Out of topic but I have a feeling my results are a bit low for comparing to GPU device gflop values on wikipedia, I do not know which device is used but do you think those numbers are normal for TR1950x,FuryX and Vega pair, logs attached (no dmesg error present)

   

- Using HIP_PATH=/opt/rocm/hip
-    hipcc -std=c++11 -O3 -o rtm8_hip rtm8.cpp
-    memory (MB) = 984.096000
-    pts (billions) = 1.122751
-    Tflops = 0.075224
-    dt = 0.213201
-    pt_rate (millions/sec) = 5266.159529
-    flop_rate (Gflops) = 352.832688
-    speedup = 0.126594



**kernel&amdgpu latest**: vanilla with fedora config, 5.3 release
build on commit cbafe18c71028d5e0ee1626b4776fea5d5824a78
**glxinfo**: https://pastebin.com/QvGvxCBQ
**rocminfo**: https://pastebin.com/5vmbSJa5
**clinfo**: https://pastebin.com/kfar2KLE
**hip_examples_log**: https://pastebin.com/jvdFw3gk

---

### 评论 #31 — buraksarac (2019-09-27T16:04:50Z)

here is the update script I have used for hcc probably you might want to add some conditions like env python or bin/python:
`find /tmp/tmp.z8puzdEA2K/ -type f -and \( -name 'rpt' -or -name 'scan-view' -or -name '*.py' -or -name 'hmaptool' -or -name 'git-clang-format' \) -exec sed -i "s/python/python3/g" {} \;`

---

### 评论 #32 — DeathTBO (2020-04-29T19:13:52Z)

I'm actually surprised how painless it was to setup. Almost nothing works on the first try. I'm running Fedora 32 and Kernel 5.6.7-300. I also have 5700 XT and a Ryzen 2700.

This post caught my eye: https://www.reddit.com/r/Fedora/comments/er8odt/davinci_resolve_on_fedora_31_with_amd_gpu/

I decided to use version 3.3 instead (which does works with Resolve).

```[ROCm]
name=ROCm
baseurl=https://repo.radeon.com/rocm/yum/3.3/
enabled=1
gpgcheck=0
```

I then began the installation and forcing hcc to install. Unfortunately I did not check if hcc actually needed to be forced.

```
sudo dnf install npth-devel hsa-ext-rocr-dev rocm-utils rocm-runtime
sudo dnf download hcc
sudo rpm -ifvh hcc-3.1.20114-Linux.rpm --nodeps
```

~~At this point it wasn't quite working, but it sounded like it needed dkms (and maybe the runtime)~~

~~sudo dnf install rocm-runtime rocm-dkms~~

I then added myself to the video group, and voila. It was immediately recognized in Blender and Resolve.

Now performance is a different story. While rendering in Blender I have two cores maxed, and the gpu will bounce from ~3% to 99%. It renders blocks very slowly because of this. Each spike does carry a lot of samples, so if this could could consistently use 100% I'm sure it would be very fast.

In a blender render race my CPU blazes past the GPU.

Edit: Added rocm-runtime to the initial instruction, and crossed out the dkms bit.

---

### 评论 #33 — andrewschott (2020-05-03T01:08:36Z)

@DeathTBO I followed your instructions but I had nothing but crashes when trying to use the any render device, and the kernel-core update installs but fails on the amdgpu driver build.  Rebooting into the new 5.6.8 kernel that just dropped yielded a broken kernel.  Simple fix for me was to remove all this and reinstall kernel-core.  Now all seems fine.  You run into this?  

---

### 评论 #34 — DeathTBO (2020-05-03T22:19:28Z)

@andrewschott Yes I had the same issue when upgrading to 5.6.8, but I think it's a dkms issue rather than a rocm issue. I have an openrazer dkms package that also fails and breaks the kernel install. I had to remove both rocm and openrazer dkms for it to work.

---

### 评论 #35 — yaxxie (2020-05-04T08:53:08Z)

> but I think it's a dkms issue rather than a rocm issue

> sudo dnf install rocm-runtime rocm-dkms

When I was testing a while back, I didn't need to add the rocm-dkms module. Somewhere in the docs I think it was saying this was to load a version of `amdkfd` kernel module but I believe this has been mainlined for a long time now

---

### 评论 #36 — Goddard (2020-05-14T22:05:24Z)

So what is the easy button for fedora 32?

---

### 评论 #37 — JLTastet (2020-06-07T16:38:54Z)

ROCm 3.5 works fine with my Vega M GPU on Fedora 32. See my comment here: https://github.com/RadeonOpenCompute/ROCm/issues/651#issuecomment-640245153. I mostly followed [@DeathTBO's instructions above](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-621408488).

---

### 评论 #38 — ptitjes (2020-11-30T10:41:46Z)

@DeathTBO For the record, I was able to have a fully functional DR 16.2.7 with Fedora 33 using the in-kernel amdgpu driver and OpenCL part of ROCm provided in AMDGPU-PRO 20.45 (seems to be something like ROCm 3.8).

The main ingredients are the re-wrapped RPM package of Ubuntu binaries https://github.com/ptitjes/opencl-amd and the OpenCL fix of https://github.com/h33p/resolve-amdocl-fix.

---

### 评论 #39 — ROCmSupport (2021-01-07T08:40:10Z)

Thanks @JLTastet and @ptitjes for the latest update on Fedora.
Request everyone, who is looking for Fedore support, to go with tweaks and install ROCm as mentioned above.
Thank you.

---

### 评论 #40 — JLTastet (2021-01-07T11:04:56Z)

@ROCmSupport This fix is outdated. My ROCm install eventually broke, and I did not succeed in reinstalling it (neither on Fedora 32 nor 33).

---

### 评论 #41 — KevinWhalen (2021-01-07T15:18:22Z)

@JLTastet, with Fedora 32 and ROCm 4.0.0, I had to put the fullpath for the ICD (Installable Client Driver) in and did it in a new file. My focus is on OpenCL though, so I do not know if this helps with everything.

    echo /opt/rocm/opencl/lib/libamdocl64.so | sudo tee /etc/OpenCL/vendors/amdocl64_rocm_custom.icd

~~Previously...~~ *[edit 2021-02-03]* Looks like shebang (runtime specification) conflicts continue abound. Options are: **1.** force install from `dnf` and manually update the files; **2.** download with `dnf` and install from `rpm` CLI with nodeps as below; or **3.** create a fake rpm that "provides" the needed program as a symlink ([example](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-771870262) by @yaxxie).

Otherwise, I followed past suggestions from in this ticket (and have been doing so since, I think, Fedora 28, except am now not using `rocm-dkms`). To condense and summarize again:

*__FYI:__ the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html) recommends a fresh ROCm install for v4.0, so it is best to remove all old version of ROCm before moving forward (`sudo dnf list --installed | grep "@ROCm"`).*

```bash
sudo dnf remove libclc pocl beignet hsakmt mesa-libOpenCL
sudo dnf install npth-devel kmod
sudo dnf install --setopt=install_weak_deps=False hsa-ext-rocr-dev rocm-utils
# May require similar rpm forcing for rocminfo and rocm-smi-lib64.
sudo rpm -ifvh --nodeps --replacepkgs --replacefiles $(sudo dnf repoquery --quiet --location hcc)
sudo dnf install rocm-dev rocm-opencl rocm-opencl-devel opencl-headers
# Some said they did not need udev stuff, but it is in the v4.0 documentation.
sudo mkdir -p /etc/udev/rules.d
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules
# The documentation also has some user group stuff. Like the udev stuff, I am
# unsure of its need, but here it is for completeness.
echo -e '\nADD_EXTRA_GROUPS=1\nEXTRA_GROUPS=video\n' | sudo tee -a /etc/adduser.conf
sudo usermod -a -G video $(whoami)
```

I have not tested much on the host. I run it in a container with the below. Inside there, I have every `bin` under `/opt/rocm` and `/opt/rocm-${ROCM_VERSION}` in `/etc/profile.d/rocm-custom.sh`. Then every `lib` and `lib64` nested under those same directories into `/etc/ld.so.conf.d/rocm-custom.conf`. That is followed by calling `ldconfig`.

    docker build --tag opencl:rocm-fedora - < Dockerfile
    docker run --rm -i -t --privileged --device /dev/dri:/dev/dri opencl:rocm-fedora

**References**

Not everything from these was needed for me because I was already following comments from this ticket.

* <https://rigtorp.se/notes/rocm/>
* <https://linuxreviews.org/Radeon_Open_Compute#Fedora_32.2F33.2C_OpenCL_only>
* <https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel>


---

### 评论 #42 — DaveWK (2021-02-02T15:45:17Z)

@ROCmSupport  It would be nice if ROCM could package the rocminfo and rocm-smi-lib64 so I didn't need to fiddle with the python shebang to make it work.. just re-iterating from: https://rigtorp.se/notes/rocm/ but you have to find the packages, force an "ignore deps" install and then sed the rocm_agent_enumerator:
```
 dnf repoquery --location rocminfo
rpm -Uvh --nodeps http://repo.radeon.com/rocm/centos8/rpm/rocminfo-1.4.0.1.rocm-rel-4.0-23-605b3a5.rpm
 sed -i 's/^#!.*/#!\/usr\/bin\/python/' /opt/rocm-4.0.0/bin/rocm_agent_enumerator 
dnf repoquery --location rocm-smi-lib64
rpm -Uvh --nodeps http://repo.radeon.com/rocm/centos8/rpm/rocm-smi-lib64-2.9.0.9-rocm-rel-4.0-23-4b49d2d.x86_64.rpm
```
then you can proceed w/ installing rocm-dev:
```
 dnf install rocm-dev rocm-opencl rocm-opencl-devel opencl-headers
```

This is kind of a pain to keep doing when there's a known fix..



---

### 评论 #43 — yaxxie (2021-02-02T18:30:25Z)

Something which would ease this pain which I use:

This is an RPM spec file
```

Name:       rocm-python-dummy
Version:    1.0.0
Release:    2%{?dist}
Summary:    Makes ROCm be quiet about missing "platform-python"
License:    MIT
Source0:    yapyap.tar
BuildArch:  noarch

Provides: /usr/libexec/platform-python

%description
Makes ROCm be quiet about missing "platform-python" 

%files

%changelog
```

then build it using `rpmbuild -bb dummy.spec` and then install the generated RPM.
Then if you do `ln -s /usr/bin/python /usr/libexec/platform-python`  you don't have to force nodeps to install packages and you don't have to replace the interpreter in any files. It's not great, it just makes it less unbearable.

---

### 评论 #44 — DeathTBO (2021-03-01T23:14:13Z)

So it's been close to a year, and I decided to check out ROCm once again. The process seemed... Easier? Keep in mind this is not a fresh install, but I did remove (all of?) the ROCm files last year.

I added my repo file, this time using version 4.0.1.

```
[ROCm]
name=ROCm
baseurl=https://repo.radeon.com/rocm/yum/4.0.1/
enabled=1
gpgcheck=0
```

I noticed the ``hcc`` package was missing, a package I had to force on version 3. @DaveWK mentioned needing to fiddle around with python sed and nodep installs, but the ``rocm_agent_enumerator`` package wasn't in the 4.0.1 repo.

I figured I could skip that step, so I decided to go ahead and run his install command.

`` dnf install rocm-dev rocm-opencl rocm-opencl-devel opencl-headers``

And voila. After a reboot it was immediately recognized as a device, and I am currently rendering in Blender.

Performance is far better than last time. However, my 8/16 Ryzen cpu still renders overall faster, but each individual square now renders at a constant rate. I noticed in #887 that the 5700xt isn't fully supported... A shame since that is probably the only thing holding me back now.

I would love for @ROCmSupport to officially support Fedora, especially since CentOS is moving to a rolling release. It feels like Fedora would be a more stable ground.

Edit: DaVinci Resolve 17 also installed and launched no problem.

---

### 评论 #45 — ROCmSupport (2021-03-02T06:21:55Z)

Hi @DeathTBO 
Thanks for your kind response.
We do not have plans to support Fedora right now.
Please stay tuned for the updates via our Documentation.
Thank you.

---

### 评论 #46 — akostadinov (2021-03-02T08:14:51Z)

Because of open drivers performance and installation issues, I decided to sell my card and do whatever I want in the cloud for the time being. I guess this is not possible for everybody but for those that can do that, you can sell your cards now prices are huge to return some of your investment. When prices of new cards become low or after a few years I may try again.

---

### 评论 #47 — darkbasic (2021-03-02T13:30:34Z)

> I would love for @ROCmSupport to officially support Fedora

Me either, but I also wonder why ROCm isn't yet in the official repos. Is it still a packaging hell?
Most users believe clover will become usable before ROCm does, which is funny considering how long clover has been taking.

---

### 评论 #48 — buraksarac (2021-03-02T16:43:56Z)

I gave up long time ago but reading follow ups it is impressive what AMD has achieved with linux contributions, built a great team with lot of knowledge and failed to provide a proper,high performance,backward compatible low level SDK/language to its own hardware... If I am not getting most of it from your software where I should look, I had a feeling even your old AMD opencl sdks had better performance ratio by percentage, not even mentioning distro supports... So gpus waiting in my storage fury-x, vega 64, sapphire toxic... Would there be a next generation? I doubt it, I turn to CPUs with threadrippers,still a AMD supporter and I hope you will do better on FPGA

---

### 评论 #49 — d1saster (2021-04-25T15:49:26Z)

Not sure whether it is still useful for anybody here, but I am also an owner of a 5700XT card and a while ago I thought I'll give it a try and self-compile ROCm for Fedora 33, not knowing what obstacles would wait for me. However, I managed to compile a huge part and packaged it for COPR. It is available [here](https://copr.fedorainfracloud.org/coprs/knechtges/rocm-hip/). It is just Fedora 33 and ROCm 3.9 IIRC, and I am not sure yet whether I really want to go again through the daunting task of patching things for the newer releases, but lets see. Unfortunately, the COPR repository is missing the higher level libraries like BLAS etc., which from my understanding are those libraries that miss support for my 5700XT.

---

### 评论 #50 — mbana (2021-10-19T22:29:45Z)

I've written a blog post on how to get version `v4.3.1` running on Fedora 34, please see <https://bana.io/blog/fedora-34-rocm-install/>. If I've left you out from the list of references, please let me know.

---
