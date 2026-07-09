# [Issue]: Installing rocm

- **Issue #:** 2847
- **State:** closed
- **Created:** 2024-01-27T06:20:05Z
- **Updated:** 2024-01-29T08:06:24Z
- **Labels:** AMD Instinct MI300X, ROCm 6.0.0
- **URL:** https://github.com/ROCm/ROCm/issues/2847

### Problem Description

I have been trying to install rocm on my machine without success for quite some time, and haven't been having much success. 

In reporting this issue, I was ran 
```
 echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
```

and had the following output:

```
GPU:
```

Which is was concerning, however, I do see that the GPU is discoverable via:

```
sudo lshw -numeric -C display
  *-display UNCLAIMED
       description: VGA compatible controller
       product: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] [1002:67DF]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI] [1002]
       physical id: 0
       bus info: pci@0000:09:00.0
       version: c7
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list
       configuration: latency=0
       resources: memory:e0000000-efffffff memory:f0000000-f01fffff ioport:2000(size=256) memory:f0a00000-f0a3ffff memory:f0a60000-f0a7ffff
```

My kernel verison is:

```
uname -srmv
Linux 5.15.0-91-generic #101~20.04.1-Ubuntu SMP Thu Nov 16 14:22:28 UTC 2023 x86_64
```
Which seems to satisfy the supported OS requirements listed [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions).



### Operating System

Ubuntu 20.04.6 LTS (Focal Fossa)"

### CPU

AMD Ryzen 7 2700X Eight-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is NOT loaded, possibly no GPU devices

### Additional Information

Looking into it, it looks like rocm6.0 may not be supported for my device, however, I'm unable to determine what version of rocm I need. A pointer to the right version installation docs would be helpful here, thanks!

Also, the issue dialogue made me select a GPU, but didn't list my GPU, so I chose MI300X.