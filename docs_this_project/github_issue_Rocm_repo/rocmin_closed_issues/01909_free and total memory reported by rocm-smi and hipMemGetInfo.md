# free and total memory reported by rocm-smi and hipMemGetInfo

- **Issue #:** 1909
- **State:** closed
- **Created:** 2023-02-16T14:33:41Z
- **Updated:** 2024-02-05T17:53:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1909

The free value reported by rocm-smi is different from that reported by the HIP API. Thanks.


$ rocm-smi --showmeminfo vram

```
======================= ROCm System Management Interface =======================
============================= Memory Usage (Bytes) =============================
GPU[0]          : VRAM Total Memory (B): 4278190080
GPU[0]          : VRAM Total Used Memory (B): 108814336
================================================================================
============================= End of ROCm SMI Log ==============================
```

However, hipMemGetInfo(&free, &total) also returns 4278190080 for both