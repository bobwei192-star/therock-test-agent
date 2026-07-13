# Unable to open /dev/kfd read-write: Cannot allocate memory (DID 7340)

- **Issue #:** 1318
- **State:** closed
- **Created:** 2020-12-03T15:54:47Z
- **Updated:** 2021-01-04T06:46:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/1318

When running:
```
$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
Failed to get user name to check for render group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
When i looked to dmesg:
```
$ sudo dmesg | grep kfd
[    2.244241] kfd kfd: DID 7340 is missing in supported_devices
[    2.244243] kfd kfd: kgd2kfd_probe failed
```

Info:
```
$ uname -a
Linux ... 5.4.0-54-generic #60-Ubuntu SMP Fri Nov 6 10:37:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```
On 5.4.0-56 kmod compilation gives me error. (didn't record that error and rebooted. :-1:  )

```
$ lspci | grep VGA
2f:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (rev c5)
```
I found in /usr/src/amdgpu-3.10-27/amd/amdkfd/kfd_device.c#447
```
...
static const struct kfd_device_info navi14_device_info = {
	.asic_family = CHIP_NAVI14,
	.asic_name = "navi14",
        ....
```
Maybe ID of this card is not listed?

Thanks for help.
