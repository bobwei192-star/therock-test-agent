# ROCM fails with supported hardware on mainboard Asus Prime B450-Plus Ryzen CPU/APU combo

- **Issue #:** 1013
- **State:** closed
- **Created:** 2020-02-15T11:13:06Z
- **Updated:** 2023-12-15T11:52:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1013

Good Evening, I had rocm 1.8 set up and running awhile back but only with a single card and I just ended up reinstalling and bringing everything up to the latest versions. 

Initially I seemed to be getting hit with the segfault issue on a 5.3.0-28 18.04 LTS ubuntu kernel after install (fresh OS) when running both rocminfo/clinfo on version 3.0. Quite a number of other people seem to be having this issue as well and posted a proposed workaround (downgrading).

Downgrading both the package and its dependencies to 2.10 seemed to fix that particular issue but I'm still having some problems.  I'm hoping someone can help me work through or around this. 

I currently have a Ryzen 5 2400G CPU/APU running on an Asus Prime 450-Plus mainboard  along with a RX560 14cu dgpu. My setup is intended to save the 2400G APU for the hardware acceleration for the xserver running the desktop and nothing else, and then offload tensorflow/pytorch to the RX560 for my studies. I've done this by having randr set the sink to offload to just the igpu.

Just to be clear, I'm trying to get rocm working with just the RX560. I understand the memory model is different between the two cards and I'm not trying to get both running in parallel, only one (the RX560), with the other (Raven) handling desktop/media acceleration.

As an additional detail, I've confirmed the EFI Utility is running the latest version firmware available from ASUS, and its been set to have both enabled cards enabled (amd/amd). The BIOS setting has two values other than disabled, under the setting iGPU Multi-Monitor Support:  Enabled and HybridMode. I've tried both of them with no outward change in behavior following a cold boot inbetween (which seems to be necessary when toggling to or from disabled).

After reading many of the issues and trying/tinkering with the udev rules, I think I'm running into at least two problems but I'm not sure how to fix either at this point.

The first challenge is rocminfo is failing with an error (listed below). rocm-smi detects both cards some stats don't make sense and there are warnings (see below) for other stats. The second issue is clinfo is failing as well with the clGetDeviceIDs(-1) error. 

I've confirmed the kernel has all three options necessary for kfd built by checking /boot/config-$(uname -r) and the user is located in the video group (ubuntu doesn't use a render group). 

Usually my installation workflow starts with testing smi,rocminfo, and then clinfo prior to passing /dev/kfd for use in a docker container as these seem to be fairly solid milestones in ensuring everything is working properly on the host first.

The weird part is rocminfo will work properly when sudoed, but only after a completely cold boot when the igpu setting in bios has been disabled and the only card detected is then the dgpu, otherwise it fails with the listed error at the below line or line 900. clinfo doesn't work in any case (same error). 

Booting with both igpu+dgpu enabled (even if only using the latter) seems to introduce problems. Digging into an strace for clinfo it looked like two likely might have been a missing so (libamdocl-orca64.so/included with amdgpu-pro) or a permission issue on kfd. Changing the udev.rules to include MODE="0666" seemed to correct the silent permission denied entry in the strace log but did nothing to correct any of the main issues, and setting other permissions for kfd to read/write would likely have security implications and doesn't seem to provide any benefit.

I'd appreciate any help you can provide in getting rocm working. I've been at this for a few days and tomorrow I plan on downgrading to 2.9 to see if there are any changes.

[Edit]: Downgrading to 2.9 resulted in no changes in either utility's output.

Please let me know if any additional information is needed.

**strace clinfo**
https://pastebin.com/gz3gUBGA

**strace rocminfo**
https://pastebin.com/cJA7dgD5

**cpuinfo**
https://pastebin.com/LFHGqZ57

**#> rocminfo (output):**

ROCk module is loaded
user is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-2.10/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

**#>clinfo (output):**
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3019.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

**#> lspci | grep "VGA":**
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X] (rev e5)
09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series] (rev c6)

**#> rocm-smi**

ROCm System Management Interface
WARNING: GPU[0]	: Unable to read /sys/class/hwmon/hwmon0/temp1_input
WARNING: GPU[0]	: Unable to read /sys/class/hwmon/hwmon0/temp1_input
WARNING: GPU[0]	: Unable to read /sys/class/hwmon/hwmon0/power1_average
WARNING: GPU[0]	: Unable to read /sys/class/hwmon/hwmon0/pwm1
WARNING: GPU[1]	: Unable to read /sys/class/drm/card1/device/gpu_busy_percent
GPU  Temp   AvgPwr  SCLK    MCLK     Fan    Perf  PwrCap  VRAM%  GPU%  
0    N/A    N/A     N/A     N/A      None%  off   46.0W     0%   0%    
1    33.0c  N/A     400Mhz  1067Mhz  None%  auto  N/A      39%   N/A   
==================End of ROCm SMI Log ==================

**#> inxi -G**
Graphics:  Card-1: Advanced Micro Devices [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
           Card-2: Advanced Micro Devices [AMD/ATI] Raven Ridge [Radeon Vega Series / Radeon Vega Mobile Series]
           Display Server: X.Org 1.20.5 drivers: amdgpu,amdgpu
           Resolution: 1920x1080@60.00hz
           OpenGL: renderer: AMD RAVEN (DRM 3.33.0, 5.3.0-28-generic, LLVM 9.0.0)
           version: 4.5 Mesa 19.2.8
