# make rocm work with "ASUS TUF505DY"

- **Issue #:** 750
- **State:** closed
- **Created:** 2019-03-20T23:59:33Z
- **Updated:** 2023-12-18T18:52:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/750

I am the happy owner of the new "ASUS TUF505DY" notebook. it have the new "AMD Ryzen 5 3550H" (With Vega/Raven GPU) CPU and a "Radeon RX560X" GPU

I manage to instal Fedora29 (no success with Centos7...) I know it is not et suported OS... but i like to help
I will update all firmware ( picasso firmware) for Ryzen APU from the linux-firmware repo.
I build the last kernel (5.0.3) patching kfd_device.c with the id of the Raven:

```
diff --git a/drivers/gpu/drm/amd/amdkfd/kfd_device.c b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
index 8be9677c0c07..73e722cc6ae2 100644
--- a/drivers/gpu/drm/amd/amdkfd/kfd_device.c
+++ b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
@@ -319,6 +319,7 @@ static const struct kfd_deviceid supported_devices[] = {
        { 0x9875, &carrizo_device_info },       /* Carrizo */
        { 0x9876, &carrizo_device_info },       /* Carrizo */
        { 0x9877, &carrizo_device_info },       /* Carrizo */
+       { 0x15D8, &raven_device_info },         /* Raven */
        { 0x15DD, &raven_device_info },         /* Raven */
 #endif
        { 0x67A0, &hawaii_device_info },        /* Hawaii */
```

after that the dmesg look good: (I am not sure it have to be done like this...)
```
> dmesg | grep kfd
[    2.492929] kfd kfd: Allocated 3969056 bytes on gart
[    2.494745] kfd kfd: added device 1002:67ef
[    2.653922] kfd kfd: Allocated 3969056 bytes on gart
[    2.654235] kfd kfd: added device 1002:15d8
```

after some install of centos rpm (rocm2.2) rocminfo report:
```
hsa api call failure at line 952, file: /home/philou/tmp/rocm/rocminfo/rocminfo.cc. Call returned 4104
```

after read some issus report I uninstall all rocm rpm and clone rocm repo (master branche):
```
> ROCT-Thunk-Interface
> ROCR-Runtime
> rocminfo
```

all are build with DEBUG for use with gdb.

I Path ROCT-Thunk-Interface to add device 1002:15d8 (Raven...)

```
#> ROCT-Thunk-Interface
diff --git a/src/topology.c b/src/topology.c
index c7f8a28..c4b9e98 100644
--- a/src/topology.c
+++ b/src/topology.c
@@ -200,6 +200,7 @@ static struct hsa_gfxip_table {
        { 0x69A3, 9, 0, 4, 1, "Vega12", CHIP_VEGA12 },
        { 0x69Af, 9, 0, 4, 1, "Vega12", CHIP_VEGA12 },
        /* Raven */
+       { 0x15D8, 9, 0, 2, 0, "Raven", CHIP_RAVEN },
        { 0x15DD, 9, 0, 2, 0, "Raven", CHIP_RAVEN },
        /* Vega20 */
        { 0x66A0, 9, 0, 6, 1, "Vega20", CHIP_VEGA20 },
```

and track rocminfo with gdb.
I finish in 'ROCT-Thunk-Interface'/src/openclose.c
```
HSAKMT_STATUS HSAKMTAPI hsaKmtOpenKFD(void)
{
	HSAKMT_STATUS result;
	int fd;
	HsaSystemProperties sys_props;

	pthread_mutex_lock(&hsakmt_mutex);

	/* If the process has forked, the child process must re-initialize
	 * it's connection to KFD. Any references tracked by kfd_open_count
	 * belong to the parent
	 */
	if (is_forked_child())
		clear_after_fork();

	if (kfd_open_count == 0) {
		init_vars_from_env();

		fd = open(kfd_device_name, O_RDWR | O_CLOEXEC);

// > fd = -1...
// > errno = EAGAIN
```

I find in 'drivers/gpu/drm/amd/amdkfd/kfd_device.c' it can be probleme with reset...

I don't know how to debug inside kfd kernel module (i need more time with google ;))

With dmesg I have many reset...
```
[   14.164505] amdgpu 0000:01:00.0: GPU pci config reset
[   29.774100] amdgpu 0000:01:00.0: GPU pci config reset
[   36.345021] amdgpu 0000:01:00.0: GPU pci config reset
```

[dmesg-5.0.3.txt](https://github.com/RadeonOpenCompute/ROCm/files/2990489/dmesg-5.0.3.txt)
