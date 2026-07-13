# ROCm does not work after installation [AsusTUF505DY]

- **Issue #:** 1398
- **State:** closed
- **Created:** 2021-03-01T20:37:41Z
- **Updated:** 2021-03-02T10:25:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1398

My issue is pretty much the same as @JoseVSeb had in #1204. I'm trying to get PyTorch working for my Master, but haven't been able to. Reading I think my problem may also be related with what @Djip007 mentions in #750 but my Linux knowledge is rather basic so I don't know.

I also have an Asus TUF 505DY.
CPU: AMD Ryzen 5 3550H (With Vega/Raven GPU)
GPU: Radeon RX560X
Ubuntu: 20.04.2 LTS
Kernel: 5.6.0-1042-oem

I managed to follow the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) but the final verification fails.

I'll attach the output of the commands I've seen used during debugging on the similar issue and if any other log is necessary I'll be glad to provide it.

Thanks in advance!

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064316/rocminfo.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064318/clinfo.txt)
[rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064324/rocm-smi.txt)
[lspci-vvv.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064326/lspci-vvv.txt)
[lspci-tv.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064327/lspci-tv.txt)






