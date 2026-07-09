# new rocm-smi reports an error when trying to find fan of QXL video device (libvirt-qemu/kvm)

- **Issue #:** 282
- **State:** closed
- **Created:** 2017-12-21T23:05:11Z
- **Updated:** 2018-06-03T15:28:18Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/282

Hi,

I have been using rocm for a while now inside a qemu/kvm VM using PCI-passthrough for the AMD GPUs.  There is also a QXL video device for the VM (GPU 0).

After a recent update, `rocm-smi` now has a messy error when it tries to get info about the QXL device fans on GPU 0.

`rocm-smi` version: `1.0.0-34-g23012d0`
kernel:  `Linux 4.11.0-kfd-compute-rocm-rel-1.6-180`
error:
```
root@ubuntu:/home/tux# rocm-smi 
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  5   47.0c   120.210W 1000Mhz  500Mhz   71.76%   auto      0%       
  3   44.0c   81.170W  1266Mhz  2088Mhz  100.0%   auto      0%       
  1   43.0c   76.33W   1185Mhz  2088Mhz  100.0%   manual    2%       
  4   42.0c   73.255W  1185Mhz  2088Mhz  100.0%   manual    2%       
  2   41.0c   81.253W  1266Mhz  2088Mhz  100.0%   manual    0%       
Traceback (most recent call last):
  File "/usr/bin/rocm-smi", line 1058, in <module>
    showAllConcise(deviceList)
  File "/usr/bin/rocm-smi", line 728, in showAllConcise
    fan = str(getFanSpeed(device))
  File "/usr/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
root@ubuntu:/home/tux# 
```
it seems to normally detect no powerplay on `GPU 0` with the rest of the fields when invoking `roc-smi -a`, but has the same messy error with the fans:

```
root@ubuntu:/home/tux# rocm-smi -a
====================    ROCm System Management Interface    ====================
================================================================================
GPU[5] 		: GPU ID: 0x7300
GPU[3] 		: GPU ID: 0x67df
GPU[1] 		: GPU ID: 0x67df
GPU[4] 		: GPU ID: 0x67df
GPU[2] 		: GPU ID: 0x67df
GPU[0] 		: GPU ID: 0x0100
================================================================================
================================================================================
GPU[5] 		: Temperature: 53.0c
GPU[3] 		: Temperature: 48.0c
GPU[1] 		: Temperature: 48.0c
GPU[4] 		: Temperature: 47.0c
GPU[2] 		: Temperature: 46.0c
GPU[0] 		: Unable to display temperature
================================================================================
================================================================================
GPU[5] 		: GPU Clock Level: 7 (1000Mhz)
GPU[5] 		: GPU Memory Clock Level: 0 (500Mhz)
GPU[3] 		: GPU Clock Level: 4 (1266Mhz)
GPU[3] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[1] 		: GPU Clock Level: 3 (1185Mhz)
GPU[1] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[4] 		: GPU Clock Level: 3 (1185Mhz)
GPU[4] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[2] 		: GPU Clock Level: 4 (1266Mhz)
GPU[2] 		: GPU Memory Clock Level: 2 (2088Mhz)
GPU[0] 		: PowerPlay not enabled - Cannot display clocks
================================================================================
================================================================================
GPU[5] 		: Fan Level: 183 (71.76)%
GPU[3] 		: Fan Level: 255 (100.0)%
GPU[1] 		: Fan Level: 255 (100.0)%
GPU[4] 		: Fan Level: 255 (100.0)%
GPU[2] 		: Fan Level: 255 (100.0)%
Traceback (most recent call last):
  File "/usr/bin/rocm-smi", line 1074, in <module>
    showCurrentFans(deviceList)
  File "/usr/bin/rocm-smi", line 563, in showCurrentFans
    fanspeed = getFanSpeed(device)
  File "/usr/bin/rocm-smi", line 358, in getFanSpeed
    fanLevel = int(getSysfsValue(device, 'fan'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
root@ubuntu:/home/tux# 
```

It does not seem to affect usability and performance so far.