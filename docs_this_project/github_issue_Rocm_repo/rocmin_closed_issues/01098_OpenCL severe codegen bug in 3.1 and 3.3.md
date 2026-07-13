# OpenCL severe codegen bug in 3.1 and 3.3

- **Issue #:** 1098
- **State:** closed
- **Created:** 2020-05-06T09:01:12Z
- **Updated:** 2020-05-30T09:10:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1098

(compiling for Radeon VII, gfx906)

This report is about an insidious bug affecting OpenCL in ROCm 3.1 and 3.3. The bug is really subtle, hard to pin-point, that's why it took so long to report it. At the same time, the bug is maddening for us developers, I would call it severe for sure. The bug seems to be absent in ROCm 2.10.

In order to facilitate the debugging, in a recent commit https://github.com/preda/gpuowl/commit/90b9fc33b10ff7acf649f2248c3ffbed7397e845 I disabled -cl-fast-relaxed-math to take it out of the suspects list (it seems -cl-fast-relaxed-math is not related to the bug).

Please have a look at [the workaround](https://github.com/preda/gpuowl/blob/90b9fc33b10ff7acf649f2248c3ffbed7397e845/gpuowl.cl#L1510-L1514) we have in gpuowl, which consists in adding an artificial branch that is never taken. This workaround is not a solution because the underlying bug can surface in a different place; and secondarilly the workaround also has a slight performance impact. In brief we'd like the bug fixed and the workaround removed.

The workaround is controlled by the define NO_KCOS_ROCM_BUG which allows to compare the ISA and the behavior with the workaround ON/OFF (by default it's ON, and when running with *-use NO_KCOS_ROCM_BUG* it's OFF).

The way to detect the presence of the bug is: at least one of these fails (error, EE reported):
```
gpuowl -prp 95576851 -fft 5.5M -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -use NO_KCOS_ROCM_BUG
```

OTOH when the bug is absent, all these run correctly (OK reported):
```
gpuowl -prp 95576851 -fft 5.5M -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -fft 5.5M
gpuowl -prp 95576851
```

The ISA generated in both cases (with/without the workaround) can be saved using -dump <folder> and compared.

Using the above detector, I did a bisect on the LLVM history (starting from around ROCm 2.10), and it pointed to this change as the point where the bug is introduced:
https://reviews.llvm.org/rG555d8f4ef5ebb2cdce2636af5102ff944da5fef8
https://github.com/llvm/llvm-project/commit/555d8f4ef5ebb2cdce2636af5102ff944da5fef8

I attach the ISA before/after the above change, both with the workaround disabled ("after" is broken by the change):
[ISA-FFT5.5-before.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585695/ISA-FFT5.5-before.txt)
[ISA-FFT5.5-after.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585696/ISA-FFT5.5-after.txt)

Also I attach the ISA, after the change, fixed by applying the workaround (-use NO_KCOS_ROCM_BUG)
[ISA-FFT5.5-after-workaround.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585713/ISA-FFT5.5-after-workaround.txt)

@rampitec I would appreciate help with understanding the bug precisely and fixing it. It would be a great relief for me when this is fixed.
