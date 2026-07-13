# clinfo freezes in ROCm 5.1 for gfx906 AMD Radeon VII GPU

- **Issue #:** 1744
- **State:** closed
- **Created:** 2022-05-24T08:06:14Z
- **Updated:** 2022-05-30T15:10:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1744

Hi,

`clinfo` freezes for ROCm 5.1 in a gfx906 AMD Radeon VII GPU

Any suggestions on how to overcome this?

Output of `dmesg` after freezing

```
[  431.635174] amdgpu: HIQ MQD's queue_doorbell_id0 is not 0, Queue preemption time out
[  433.675364] amdgpu: HIQ MQD's queue_doorbell_id0 is not 0, Queue preemption time out
[  433.675388] amdgpu: Failed to evict process queues
[  433.675402] amdgpu: Failed to quiesce KFD
[  433.675434] amdgpu: HIQ MQD's queue_doorbell_id0 is not 0, Queue preemption time out
[  433.675454] amdgpu: Resetting wave fronts (cpsch) on dev 00000000cbdd3dcd
```

In the initial parts of the `dmesg` an I2C error is also present

```
[    2.012494] [drm] VCE initialized successfully.
[    2.013685] [drm] TX was terminated, IC_TX_ABRT_SOURCE val is:1000001
[    2.013690] [drm:smu_v11_0_i2c_xfer.cold.4 [amdgpu]] *ERROR* Received I2C_NAK_7B_ADDR_NOACK !!!
[    2.013863] [drm:smu_v11_0_i2c_xfer [amdgpu]] *ERROR* WriteI2CData() - I2C error occurred :1
[    2.013998] fbcon: Taking over console
[    2.014061] Console: switching to colour frame buffer device 100x37
[    2.014725] [drm:amdgpu_ras_eeprom_init [amdgpu]] *ERROR* Failed to read EEPROM table header, res:-5
[    2.014888] amdgpu 0000:25:00.0: amdgpu: Failed to initialize ras recovery! (-5)
```

**System Information**

```
x86_64
AlmaLinux release 8.6 (Sky Tiger)
AlmaLinux release 8.6 (Sky Tiger)
NAME="AlmaLinux"
VERSION="8.6 (Sky Tiger)"
ID="almalinux"
ID_LIKE="rhel centos fedora"
VERSION_ID="8.6"
PLATFORM_ID="platform:el8"
PRETTY_NAME="AlmaLinux 8.6 (Sky Tiger)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:almalinux:almalinux:8::baseos"
HOME_URL="https://almalinux.org/"
DOCUMENTATION_URL="https://wiki.almalinux.org/"
BUG_REPORT_URL="https://bugs.almalinux.org/"

ALMALINUX_MANTISBT_PROJECT="AlmaLinux-8"
ALMALINUX_MANTISBT_PROJECT_VERSION="8.6"

AlmaLinux release 8.6 (Sky Tiger)
AlmaLinux release 8.6 (Sky Tiger)
```

**Kernel Information**

```
Linux 4.18.0-372.9.1.el8.x86_64 #1 SMP Tue May 10 08:57:35 EDT 2022 x86_64
```

**Additional Info**

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/8760694/rocminfo.txt)
[hipconfig.txt](https://github.com/RadeonOpenCompute/ROCm/files/8760690/hipconfig.txt)
