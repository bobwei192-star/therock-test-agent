# Dual Radeon VII, X370 board, Tensorflow, Total Kernel Module Fail.

- **Issue #:** 858
- **State:** closed
- **Created:** 2019-08-08T04:28:21Z
- **Updated:** 2024-01-11T03:40:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/858

**Synopsis**

Multi-GPU ROCm experiences amdgpu kernel module corruption.
Running process on either GPU individually succeeds: this is using either PCIe slot.
Running process on both GPUs simultaneously fails.
Both slots are PCIe3 x8 directly attached to CPU, no PCIe switch involved. 
GPU located in either slot works with ROCm, the fail only happens when I try to use both GPUs at the same time.

**System details**

2 Radeon VII with vbios 106 patch applied.
Ryzen 1600X CPU
Asus Prime X370 Pro, BIOS July 2019
64 GB DDR4 2666 (GSkill F4-266615D-32GVR, 2 kits)
850W Thermaltake (mumble mumble) PSU
Ubuntu 18.04.3
Kernel "Linux gpu 4.15.0-55-generic #60-Ubuntu SMP Tue Jul 2 18:22:20 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux"
ROCm 2.6 rocm-dkms
Tensorflow-rocm 1.14 for Python 2.7 installed via pip.

**What I am trying to do**

Trying to run Tensorflow slim's models/research/slim/train_image_classifier.py script utilizing both GPUs. Model is inceptionv1, data is 250 categories grabbed at random from imagenet 2012 challenge dataset. This script works flawlessly on multi-GPU setups from the Green Team.

**What's happening**

If I restrict TF to use either GPU individually by setting environment variable CUDA_VISIBLE_DEVICES to 0 or 1, and passing "--num_clones 1" to train_image_classifier.py then training proceeds on the indicated GPU in the normal manner.

If I unset CUDA_VISIBLE_DEVICES and pass "--num_clones 2" to train_image_classifier.py, then both GPUs are utilized but after a short while several bad things happen:

Bad thing 1) TF freezes,

Bad thing 2) rocm-smi errors out (strings of equals sign in the header & footer removed, they confuse github formatting):

```
	root@gpu:~# rocm-smi
 
       ROCm System Management Interface
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/temp1_input
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/temp1_input
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/power1_average
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/pp_dpm_sclk
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/pp_dpm_mclk
 	WARNING: GPU[0] : Unable to read /sys/class/hwmon/hwmon0/pwm1
 	WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/gpu_busy_percent
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/temp1_input
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/temp1_input
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/power1_average
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/pp_dpm_sclk
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/pp_dpm_mclk
 	WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon1/pwm1
 	WARNING: GPU[1] : Unable to read /sys/class/drm/card1/device/gpu_busy_percent
 	GPU  Temp  AvgPwr  SCLK  MCLK  Fan    Perf  PwrCap  VRAM%  GPU%
 	0    N/A   N/A     N/A   N/A   None%  auto  250.0W   54%   N/A
 	1    N/A   N/A     N/A   N/A   None%  auto  250.0W   53%   N/A
	End of ROCm SMI Log 
 

```

Bad thing 3: syslog and kernlog receive messages:
```
Aug  8 01:32:52 localhost kernel: [ 3147.377086] Started restoring pasid 32768
Aug  8 01:32:52 localhost kernel: [ 3147.377847] Restoring PASID 32768 queues
Aug  8 01:32:52 localhost kernel: [ 3147.377856] Restoring PASID 32768 queues
Aug  8 01:32:52 localhost kernel: [ 3147.377870] Finished restoring pasid 32768
Aug  8 01:33:08 localhost kernel: [ 3163.119865] Signal event wasn't created because limit was reached
Aug  8 01:33:26 localhost kernel: [ 3181.587314] pcieport 0000:00:03.1: AER: Multiple Uncorrected (Fatal) error received: id=0000
Aug  8 01:33:26 localhost kernel: [ 3181.629625] pcieport 0000:00:03.1: PCIe Bus Error: severity=Uncorrected (Fatal), type=Transaction Layer, id=0019(Receiver ID)
Aug  8 01:33:26 localhost kernel: [ 3181.630510] pcieport 0000:00:03.1:   device [1022:1453] error status/mask=00040000/04400000
Aug  8 01:33:26 localhost kernel: [ 3181.631159] pcieport 0000:00:03.1:    [18] Malformed TLP          (First)
Aug  8 01:33:26 localhost kernel: [ 3181.631687] pcieport 0000:00:03.1:   TLP Header: 1f000001 00000000 00000000 e750772f
Aug  8 01:33:26 localhost kernel: [ 3181.632291] pcieport 0000:00:03.1: broadcast error_detected message
Aug  8 01:33:26 localhost kernel: [ 3181.632294] amdgpu 0000:0a:00.0: device has no AER-aware driver
Aug  8 01:33:26 localhost kernel: [ 3181.632296] snd_hda_intel 0000:0a:00.1: device has no AER-aware driver
Aug  8 01:33:27 localhost kernel: [ 3182.429577] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.430155] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.430156] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.431463] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.432037] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.432037] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.432702] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.433288] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.433289] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.433390] amdgpu: [powerplay] Failed to send message 0x2d, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.433963] amdgpu: [powerplay] [GetCurrentClkFreq] Attempt to get Current Frequency Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.433964] amdgpu: [powerplay] Attempt to get current gfx clk Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.434060] amdgpu: [powerplay] Failed to send message 0x2d, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.434633] amdgpu: [powerplay] [GetCurrentClkFreq] Attempt to get Current Frequency Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.434634] amdgpu: [powerplay] Attempt to get current mclk freq Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.435319] amdgpu: [powerplay] Failed to send message 0x3c, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.435894] amdgpu: [powerplay] Attempt to get current RPM from SMC Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.437320] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff
Aug  8 01:33:27 localhost kernel: [ 3182.437894] amdgpu: [powerplay] [CopyTableFromSMC] Attempt to Set Dram Addr High Failed!
Aug  8 01:33:27 localhost kernel: [ 3182.437894] amdgpu: [powerplay] Failed to export SMU metrics table!
Aug  8 01:33:27 localhost kernel: [ 3182.673399] pcieport 0000:00:03.1: Root Port link has been reset
Aug  8 01:33:27 localhost kernel: [ 3182.673404] pcieport 0000:00:03.1: AER: Device recovery failed
Aug  8 01:33:28 localhost kernel: [ 3183.492500] amdgpu: [powerplay] Failed to send message 0x10, response 0xffffffff

```
ad infinitum.

Bad thing 4: the screen goes blank, and the machine requires a hard reset to recover.

The fail happens after a few tens of iterations, up to 170 iterations.

Googling for solutions, here are things that had no effect on either single GPU or dual GPU training runs:

1. Dis/abling IOMMU in BIOS has no effect.
2. Uninstall ROCM. Reboot. Reinstall ROCM.
3. Uninstall tensorflow et al. Reinstall tensorflow et al.
4. Add "pci=noaer" to grub linux command line makes the TLP & AER error messages go away but TF still fails and rocm-smi cannot read anything under /sys.
 
Has anyone solved this kind of problem before?

I **_think_** there is a problem with the GPUs trying to communicate with each other across PCIe and addressing bytes above a 4GB ceiling - this may be the source of the "Malformed TLP" error message.

Can anyone either tell me that my though is completely wrong, or point me at info about how to configure the address range windows used by the GPUs (PCIe BARs I think they are called)?
The mobo has no BIOS option to enable or disable above 4GB addressing in it's PCIe settings.

(BTW, even if it's not your specific area of work, congrats on Rome: it looks like an Intel Killer.)
