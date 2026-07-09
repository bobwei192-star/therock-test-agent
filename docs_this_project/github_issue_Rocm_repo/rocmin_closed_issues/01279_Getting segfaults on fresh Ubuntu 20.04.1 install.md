# Getting segfaults on fresh Ubuntu 20.04.1 install

- **Issue #:** 1279
- **State:** closed
- **Created:** 2020-11-06T22:28:53Z
- **Updated:** 2020-11-14T16:18:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/1279

Hello! I'm pretty new to ROCm, so I'm sorry if I've missed anything obvious, but...

I've been trying to get ROCm set up on a laptop which happens to have an AMD card. It _might_ be too old, but I'm not totally sure yet. After the segfaults I've been getting, I'm not too hopeful, but I thought I'd ask.

For some background, this is a fresh install of Ubuntu 20.04.1, which I set up using [wubiuefi](https://github.com/hakuna-m/wubiuefi). I have done almost nothing to the system except follow the instructions for [installing ROCm](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu).

[This is the output I'm getting from the rocminfo and clinfo.](https://gist.github.com/Autofire/0dfd012710b9029fa869553009dce2d3) At the end, I also have the results of trying to build and run [this ROCm program](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/master/vectorAdd):

```
daniel@ubuntu:~/HIP-Examples/vectorAdd$ make
/opt/rocm/hip/bin/hipcc -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
/opt/rocm/hip/bin/hipcc vectoradd_hip.o -o vectoradd_hip.exe
./vectoradd_hip.exe
 System minor 0
 System major 4238752
 agent prop name 
hip Device prop succeeded 
make: *** [Makefile:30: test] Segmentation fault (core dumped)
```

It's not just this program; all of the examples in that repo are also throwing segfaults. Am I missing some driver (this wouldn't surprise me)? Or is my hardware incompatible?

If it helps, [here is the info on the graphics card that the AMD Radeon Pro Settings comes up with.](https://gist.github.com/Autofire/168aacfdfc6bf7a2449b112a913445c9)