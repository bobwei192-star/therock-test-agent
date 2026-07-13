# Performance issue with JCulpit Opencl-experiments Application on 1950X and 2 x Vega64.  - Wrong Wave Size Set in App.

- **Issue #:** 265
- **State:** closed
- **Created:** 2017-11-27T10:12:06Z
- **Updated:** 2017-12-01T23:29:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/265

So I thought when going for ROCm, investing in top-end AMD hardware would be a good idea...

So far, the only bright spot is the 1950X performance. The OpenCL performance of the two Vega64 cards can only be classified as nonexistant.

After two-man-weeks worth of hassle setting things up on a Ubuntu 17.10 to the point where clinfo at least doesn't crash, I'm trying to let some OpenCL programs run. And there are the results:

```
root@amd:~/tools-master# ./cl-demo 10 1000000
Choose platform:
[0] Advanced Micro Devices, Inc.
Enter choice: 0
Choose device:
[0] gfx900
[1] gfx900
Enter choice: 0
---------------------------------------------------------------------
NAME: gfx900
VENDOR: Advanced Micro Devices, Inc.
PROFILE: FULL_PROFILE
VERSION: OpenCL 1.2 
... yadda yadda ...
*** Set CL_HELPER_NO_COMPILER_OUTPUT_NAG=1 to disable this message.
0.000006 s
0.019669 GB/s
GOOD
```
0.019669 GB/s - wow. A 1080Ti does 170 GB/s there.

Trying another benchmark program, gives me warnings right away:

```
benchmarking... /tmp/AMD_4742_41/t_4742_43.cl:140:2: warning: null character ignored [-Wnull-character]
}<U+0000>
 ^
/tmp/AMD_4802_41/t_4802_43.cl:140:2: warning: null character ignored [-Wnull-character]
}<U+0000>
 ^
1 warning generated.
o*** Error in `./opencl-bench': corrupted double-linked list: 0x0000559cb21948b0 ***
```

Of course both programs work on everything from WX4100 over all the 1050/1060/1070/1080 and Quadro and Tesla cards.

So how am I going to improve things from here?

For starters, I'd like to know why https://github.com/jcupitt/opencl-experiments/tree/master/tools-master

gives me 8500 times worse benchmark results on a Vega64 than on a 1080Ti. Maybe from there on things will get better.

Some system info

```
root@amd:~/tools-master# lspci -v | grep -i vga
0a:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] (rev c1) (prog-if 00 [VGA controller])
43:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] (rev c1) (prog-if 00 [VGA controller])

root@amd:~/tools-master# uname -a
Linux amd 4.11.0-kfd-compute-rocm-rel-1.6-180 #1 SMP Tue Oct 10 08:15:38 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux

cat /opt/rocm/.info/version -> 1.6.180
```