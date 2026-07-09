# Radeon RX 7900 XTX ROCm 5.4.3 - HSA_STATUS_OUT_OF_RESOURCES

- **Issue #:** 2191
- **State:** closed
- **Created:** 2023-05-30T07:14:34Z
- **Updated:** 2023-05-30T11:24:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/2191

On an Ubuntu 22.04 system with an AMD Radeon RX 7900 XTX with ROCm 5.4.3 installed via apt, I see the errors below while running basic utilities/tests:

```
apt list --installed | grep rocm

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

rocm-bandwidth-test/jammy,now 1.4.0.50403-121~22.04 amd64 [installed]
rocm-clang-ocl/jammy,now 0.5.0.50403-121~22.04 amd64 [installed,automatic]
rocm-cmake/jammy,now 0.8.0.50403-121~22.04 amd64 [installed,automatic]
rocm-core/jammy,now 5.4.3.50403-121~22.04 amd64 [installed,automatic]
rocm-dbgapi/jammy,now 0.68.0.50403-121~22.04 amd64 [installed,automatic]
rocm-debug-agent/jammy,now 2.0.3.50403-121~22.04 amd64 [installed,automatic]
rocm-dev/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-developer-tools/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-device-libs/jammy,now 1.0.0.50403-121~22.04 amd64 [installed,automatic]
rocm-dkms/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-gdb/jammy,now 12.1.50403-121~22.04 amd64 [installed,automatic]
rocm-hip-libraries/jammy,now 5.4.3.50403-121~22.04 amd64 [installed,automatic]
rocm-hip-runtime-dev/jammy,now 5.4.3.50403-121~22.04 amd64 [installed,automatic]
rocm-hip-runtime/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-hip-sdk/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-language-runtime/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-llvm/jammy,now 15.0.0.23045.50403-121~22.04 amd64 [installed,automatic]
rocm-ml-libraries/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-ml-sdk/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-ocl-icd/jammy,now 2.0.0.50403-121~22.04 amd64 [installed,automatic]
rocm-opencl-dev/jammy,now 2.0.0.50403-121~22.04 amd64 [installed]
rocm-opencl-runtime/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-opencl-sdk/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocm-opencl/jammy,now 2.0.0.50403-121~22.04 amd64 [installed]
rocm-smi-lib/jammy,now 5.0.0.50403-121~22.04 amd64 [installed,automatic]
rocm-utils/jammy,now 5.4.3.50403-121~22.04 amd64 [installed]
rocminfo/jammy,now 1.0.0.50403-121~22.04 amd64 [installed,automatic]
rocmtools-dev/jammy,now 1.5.0.50403-121~22.04 amd64 [installed]
```

```
$ rocminfo 
ROCk module is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1148
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

```
/opt/rocm/bin/rocm-bandwidth-test 
HSA Error Found!  In file: /long_pathname_so_that_rpms_can_package_the_debug_info/src/tests/rocm_bandwidth_test/rocm_bandwidth_test_parse.cpp;   At line: 519
Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

``` 
$ lshw -class video
*-display
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:83:00.0
       version: c8
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: iomemory:2c00-2bff iomemory:2c80-2c7f irq:199 memory:2c000000000-2c7ffffffff memory:2c800000000-2c8001fffff ioport:9000(size=256) memory:d0d00000-d0dfffff memory:d0e00000-d0e1ffff
```

`clinfo` lists the NVIDIA GPU card that I have in one of the slots but does not list the Radeon card.

The user here is added to both the `video` and `render` groups.