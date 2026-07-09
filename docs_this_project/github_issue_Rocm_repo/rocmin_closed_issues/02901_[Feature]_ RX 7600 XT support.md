# [Feature]: RX 7600 XT support

- **Issue #:** 2901
- **State:** closed
- **Created:** 2024-02-16T23:56:36Z
- **Updated:** 2025-06-01T18:01:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/2901

### Suggestion Description

I recently bought an RX 7600 XT for primarily GPGPU purposes. I did unfortunately however not check the compatibility list before purchase and was sad to learn that my graphics card is currently not working with ROCm.

---

I have the latest ROCm packages installed (6.0.0).

`rocminfo` gives me the following:
```
$ /opt/rocm/bin/rocminfo --support
ROCk module is loaded
hsa api call failure at: /usr/src/debug/rocminfo/rocminfo-rocm-6.0.0/rocminfo.cc:1219
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

`rocm-smi` lists the GPU as such:
```
0       [0x0518 : 0xc0]       N/A     N/A    N/A, N/A        None  None  0%   unknown  Unsupported    0%   0%    
        Navi 33 [Radeon RX 7                                                                                     
```

---

I first found the page listing [supported GPUs on Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html). There is very few GPUs listed here.

The [supported GPUs on Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html) page does list quite a few more GPUs, also the ones that AFAIK work well on Linux. I do not however see the RX 7600 XT listed here at all, so this gives me some hope that the GPU might be supported at some point.

I hope you can consider adding support for the RX 7600 XT, since it seems like a fantastic choice for ML and GPGPU in this budget range.

### Operating System

Arch Linux (Linux 6.7.4-arch1-1 x86_64)

### GPU

AMD Radeon RX 7600 XT

### ROCm Component

_No response_