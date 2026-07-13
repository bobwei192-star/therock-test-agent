# "kfd2kgd: amdgpu: failed to validate PT BOs"

- **Issue #:** 365
- **State:** closed
- **Created:** 2018-03-18T20:22:44Z
- **Updated:** 2018-06-03T13:20:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/365

I am unable to run `rocminfo`, let alone anything else related to this ecosystem, as this issue happens during initialization. I built all the packages from source and narrowed down the specific syscall to [this line]( https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/1f08bc194197107eb09b9af0bf37078b6bee67b2/src/fmm.c#L1491).

[dmesg](https://gist.github.com/DiamondLovesYou/3394875f3db5f5a9a5d1b8a32e0fb56c#file-dmesg)
[Linux .config](https://gist.github.com/DiamondLovesYou/3394875f3db5f5a9a5d1b8a32e0fb56c#file-config)

I'm using @fxkamd's branches of `ROCK-Kernel-Driver` and `ROCT-Thunk-Interface`, built from source.

My hardware is a Amd Ryzen 1950X on an ASUS ROG ZENITH EXTREME board. 64Gb RAM ECC, spread over 4 dimms, overclocked to 2933Mhz from 2400Mhz. MSI Radeon 580 8Gb, and an nvidia 1070Ti (this is blacklisted on the linux side, I use it exclusively for passthrough). No PCIe switches/bridges/etc.

The odd thing about my issue is that I have had ROCm working in the past, on older kernel versions.

Btw, what on Earth is a "BO"? I'm not finding any documentation on what exactly that is.