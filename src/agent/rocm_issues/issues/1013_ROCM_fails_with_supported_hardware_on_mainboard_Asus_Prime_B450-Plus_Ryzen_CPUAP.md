# ROCM fails with supported hardware on mainboard Asus Prime B450-Plus Ryzen CPU/APU combo

> **Issue #1013**
> **状态**: closed
> **创建时间**: 2020-02-15T11:13:06Z
> **更新时间**: 2023-12-15T11:52:58Z
> **关闭时间**: 2023-12-15T11:52:58Z
> **作者**: dundir
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1013

## 描述

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


---

## 评论 (15 条)

### 评论 #1 — dundir (2020-02-17T07:48:07Z)

After quite a lot of trial and nonsensical output/errors, I cannot stress enough the need to completely cold boot the system when anyone is troubleshooting and making any kind of BIOS setting changes with the ASUS Prime B450-Plus mainboards (possibly other mainboards which support APU's as well). 

It is not enough to simply reboot, or power-off, or do a quick toggle of your physical switch on the PSU unit. 

Some state seems to remain for a small window of time after power disconnect unless you take similar steps as one would when draining the flea power on a blade server. (i.e. make the change in BIOS, shutdown, disconnect power Inputs, hold the power-on button for x seconds, reconnect power, boot). If this isn't done (and even if it was done and you still see this behavior try power cycling one more time) you end up with nonsensical output/errors, and if one doesn't realize this during troubleshooting they can waste a lot of time.

So, it appears I can have 2.9 running properly now with just a single card (dgpu:enabled , igpu:disabled + full cold boot). I would still like to be able to run both cards side-by-side (but not in parallel) but this will have to do for now. I'll post the logs/coredumps for the latest version I can get installed without problems with a single card. I'll keep you posted.

Edit: 3.0 works just fine when the problematic APU is disabled and state is thoroughly flushed. 

I've attached a tarball with rocminfo, clinfo, and opencl exercise test 02 along with the appropriate strace and crash/core dumps. Hopefully this will provide enough information to nail down the problematic parts. If not, and additional information is needed please reach out as I can replicate the issue on demand (and I want to see this fixed).

3.0_preboot (fresh install, no reboot)
3.0_disabled (iGPU disabled, only dGPU, note: rocminfo still detects the APU?)
3.0_enabled (iGPU+dGPU, rocminfo works, clinfo segfaults, ocltest02 segfaults)
3.0_hybrid (iGPU+dGPU, rocm segfault, clinfo clgetDevice(-1), ocltest02 hang requiring -9 signal)

[3.0.ocl-rocm-logs.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/4212919/3.0.ocl-rocm-logs.tar.gz)




---

### 评论 #2 — dundir (2020-02-26T03:22:37Z)

As a follow-up, I won't be able to test this any further. I've had to send the mainboard back to ASUS after it bricked. The issue was present on BIOS rev 0604 and 2008 which was supposed to include a number of stability fixes. 

There seemed to be a minor issue after the firmware upgrade (USB Mouse wasn't detected after bootup into BIOS without hotplugging) and about a week after the upgrade following a restart for changing the BIOS settings for GPUs it ended up bricking the motherboard completely. 

No POST and no beepcodes when you remove all RAM. Power button would turn the fans on but no power to USB devices, chirp at boot, or POST, and ASUS firmware crash recovery doesn't start so its a dead duck.

Resetting the CMOS did fix the bootup chirp, beepcodes, and USB power issue; but it still would never make it to POST without signifying any error (No video output), and it would never make it past POST, or into BIOS when pressing the appropriate buttons without a display. 
  
The motherboard Is now being sent back for RMA/repair.

In case someone from AMD would like to follow-up with Asus, I've included the specific changes which seem to have triggered the brick, the only other possibillity is some form of memory bug in the new BIOS which eventually caused a resource exhaustion or corruption issue. The hardware is about a year old and has been running without issue until now so its unlikely that its a hardware issue.

Aside from the state issues mentioned in my previous posts, the changes made to the BIOS only involved setting the primary from PCIe to Internal GPU (Ryzen 5 APU 2400G) and the shared memory size to 3G (from a 16Gb Viper stick) with multimonitor support turned off, the dGPU inslot was a 14cu RX560 at the time. 

On the previous firmware (0604) this left the system without post until the dGPU was removed after which you could boot up and fix settings. In the latest update (2008) this appears to cause a brick.  I was testing this as I realized I had forgotten that test case when testing the above settings.

Output was tested from both GPU/APU HDMI ports (there was none), and all other previous troubleshooting was performed first with the bare minimum component system, and then with the dGPU installed (to rule out all options).

I doubt anything rocm related was at issue, but I'll know more once ASUS has had a chance to examine the motherboard. I've been told to expect it to take at least 14 days plus shipping. I'll post an update when I know more.

---

### 评论 #3 — dundir (2020-03-15T01:34:17Z)

Received a brand new Asus Prime B450 Plus board (same bios revision), and back to ye olde segment fault with clinfo. Seems it now no longer allows IGFX to be selected as the primary when IGFX Multimonitor is disabled in the BIOS (i.e. the setting that bricked the old one). 


---

### 评论 #4 — dundir (2020-03-26T23:48:26Z)

ping... 

It looks like 3.1 gets a little bit further but OpenCL is still broken, and with multimonitor support enabled I was able to import pytorch and get a segmentation fault with the stack trace referencing compute engine cpp.

---

### 评论 #5 — dundir (2020-04-13T07:07:51Z)

Tested 3.3 with the same options. ROCM is still nonfunctional, problems with the unpinned compute engine.cpp at line 126, segmentation fault, or system hang depending on the various BIOS settings and tests run.

There has been no response or assignment in the past 2 months, at this point I'm moving on. 
Its become clear to me that ROCM as a platform simply is not a priority or up and coming platform and any deep learning student is better served purchasing nvidia hardware as much as I loathe to say it. 

I ended up buying a Nvidia Jetson developer kit in the interim and the Nvidia customer service is quite possibly some of the worst I've ever interacted with; Instructing a customer seeking an RMA to post in a community forum as a first step for a defective unit rather than starting a formal RMA is fairly dubious and high on my list of overall worst-case experiences (this happened with the Jetson).

For anyone running into the same problem. From what I've been able to gather, there appears to be two things happening here, one is a firmware bug with my, and possibly several other motherboard models with regard to Ryzen CPU/APU combos, and possibly the ACPI Component Resource Affinity Tables not being properly structured/exposed. The tables are speculation at this point because its outside my personal expertise, and there is no one to get help from since there has been no response over the last several months. The other issue is ROCM as far as I've been able to tell doesn't have any way of selecting specific HSA agents and instead walks the agent list which then fails the process, or segfaults.

Symptoms you might see include ROCM segfaulting when it attempts to enumerate all HSA agents. Anyone with a Ryzen 5 2400G CPU/APU and that motherboard combo may run into unpinned compute engine errors, and will be unable to run rocm tests without error while the IGFX BIOS option is enabled. OpenCL won't work, TF2, and Pytorch won't work.

The APU is detected as an agent, and there doesn't appear to be any way to have amdkfd ignore the APU as an agent without disabling it in the BIOS at boot. 

If you wanted to solely use the APU to render X11 while at the same time as using the dGPU for deep learning, as far as I've been able to tell over the last two months of dredging this problem; it can't be done.

I've tested rolling back my kernel and using the old dkms modules, using previous versions and I would have to rollback to rocm v1.9, and kernel 4.18 to have it work again which is not possible given my current environment requirements. 

Additionally disabling the BIOS options for the multimonitor support allow testing to get further in the process but rocm hangs when running standard pytorch tests, and OpenCL still fails, and disabling multi-monitor option setting while setting IGFX as the primary with RAM allocation set to 1-3GB after a cold flea-power drain boot ...yes ... still bricks the device permanently with firmware version 2008 (yes it happened a second time). It looks like I'll have to RMA the mainboard replacement I received back to ASUS. Last time it took about a month and they sent me a new board; I may just go with another manufacturer (not ASUS) instead of dealing with this.

At this point I can't consider AMD cards a viable alternative to Nvidia for deep learning research, and there just isn't enough of a skilled community to handle the troubleshooting aspects. The project looked promising but given the current level of QA, and the challenges that need to be address; rather than waste time spinning wheels in the dark, I think It would be better to shelve the entire project until the necessary resources can be brought in to provide a base level of support towards correcting the QA issues. The testing and verification of ROCM functionality to ensure its working properly shouldn't be contingent on specific motherboard firmware or BIOS options when the hardware is listed as supported, or untested.

---

### 评论 #6 — dundir (2020-04-13T07:20:30Z)

I've attached the CRAT table dump in the case someone comes along that would find it useful with following up on this issue. I saved a full ACPI dump to file; if its needed feel free to reach out.

I don't know enough about low level structures to be able to do anything with this. I'll make it available for the next six months.

[acpi-crat.dump.txt](https://github.com/RadeonOpenCompute/ROCm/files/4468432/acpi-crat.dump.txt)



---

### 评论 #7 — seesturm (2020-04-13T10:39:45Z)

Maybe it does not help, but did you ever try to restrict the visible devices? There are some methods available. E.g. environment variable ROCR_VISIBLE_DEVICES=0 for if you want only the first device "visible".

---

### 评论 #8 — dundir (2020-04-13T20:39:51Z)

@seesturm Thanks. I wasn't aware of those options and I'd been searching fairly regularly for the past several months. It would have been something additional I could have tried. 

Unfortunately the BIOS settings bricked the replacement board, again, so it doesn't POST and I won't have anything to test on until the second RMA replacement comes back if I end up going that route. 

At this point, I'm thinking I probably will just wash my hands of this and scrap my original plans of having an AMD based deep learning rig. The software just isn't at a QA level where a fairly experienced professional system admin can get the platform verified up and running anymore and there's too much floating outdated and unusable information out there with regard to troubleshooting.

---

### 评论 #9 — dundir (2020-07-19T04:42:35Z)

I have the new motherboard back from RMA (no longer bricked).

@kentrussell At this point, I'd be willing to donate a problematic but functional unit (ASUS motherboard/Ryzen 5 2400G APU combo) if it means the issue gets some attention, I was testing the setup with an RX560 [14 compute unit]. In either case, ASUS is not addressing the problem with their firmware at all and I've managed to brick several motherboards now just toggling BIOS options (from the UEFI manager). Main problems occur when APU/CPU/dGPU are detected as enabled, or plugged in. 

```lspci -vvv -s XX:XX.X|grep Atomic``` shows t for both APU/dGPU show:

AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
			 AtomicOpsCtl: ReqEn+


Setting ROCR_VISIBLE_DEVICES had some unexpected behavior in a docker image prior to the v2020 AGESA firmware update; haven't been able to test afterwards as testing on the host fails with a hang. Prior (v2008 firmware) Value of 0 had shown both CPU/APU as HSA agents, Value of 1 showed Ryzen 5 CPU/dGPU as HSA agents, both still failed sample tests. Firmware update causes rocminfo to hang with processes that eventually go defunct.

Looks like the first node being created by kfd is an APU topology node [0x0:0x0] and then dGPU node is added to the topology, then the APU is added last. Testing was done with 20.04 LTS using the 5.4 upstream kernel. 

rocminfo throws a bad address error right before hanging. Let me know if you need anything from me but at this point I'm looking to purchase hardware that actually works (ASUS... never again). Edit: The hardware may either be sold at a loss or donated depending on the effort needed, given the current status of CV19 shutdowns. I'd rather have it go towards something productive.


<summary>dmesg (relevant?)(summarized) </summary>
<details >
...

[    0.000000] No NUMA configuration found
...
[    0.743873] Parsing CRAT table with 1 nodes
[    0.743878] Creating topology SYSFS entries
[    0.743926] Topology: Add APU node [0x0:0x0]
[    0.743927] Finished initializing topology
[    0.744014] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xe0000000 -> 0xefffffff
[    1.695461] kfd kfd: Allocated 3969056 bytes on gart
[    1.696210] Virtual CRAT table created for GPU
[    1.696211] Parsing CRAT table with 1 nodes
[    1.696215] Creating topology SYSFS entries
[    1.696283] Topology: Add dGPU node [0x67ef:0x1002]
[    1.696285] kfd kfd: added device 1002:67ef
[    1.696325] [drm] Cannot find any crtc or sizes
[    2.011956] [drm] VCN decode and encode initialized successfully(under SPG Mode).
[    2.012789] kfd kfd: Allocated 3969056 bytes on gart
[    2.013017] Topology: Add dGPU node [0x67ef:0x1002]
[    2.013019] kfd kfd: added device 1002:15dd
[    2.014334] [drm] fb mappable at 0x40BC1000
...

</details>

<summary> Full dmesg
</summary>
<details full>

...
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-5.4.0-40-generic root=/dev/mapper/thorshamma--vg-base ro quiet splash vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Hygon HygonGenuine
[    0.000000]   Centaur CentaurHauls
[    0.000000]   zhaoxin   Shanghai  
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000000a0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000009e0ffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000009e10000-0x0000000009ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x000000000a000000-0x000000000a1fffff] usable
[    0.000000] BIOS-e820: [mem 0x000000000a200000-0x000000000a20afff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000000a20b000-0x000000000affffff] usable
[    0.000000] BIOS-e820: [mem 0x000000000b000000-0x000000000b01ffff] reserved
[    0.000000] BIOS-e820: [mem 0x000000000b020000-0x0000000031502fff] usable
[    0.000000] BIOS-e820: [mem 0x0000000031503000-0x000000003151efff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000003151f000-0x000000003a3d9fff] usable
[    0.000000] BIOS-e820: [mem 0x000000003a3da000-0x000000003a4f1fff] reserved
[    0.000000] BIOS-e820: [mem 0x000000003a4f2000-0x000000003a500fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x000000003a501000-0x000000003a603fff] usable
[    0.000000] BIOS-e820: [mem 0x000000003a604000-0x000000003a9befff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x000000003a9bf000-0x000000003b77afff] reserved
[    0.000000] BIOS-e820: [mem 0x000000003b77b000-0x000000003dffffff] usable
[    0.000000] BIOS-e820: [mem 0x000000003e000000-0x00000000bfffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fd100000-0x00000000fd1fffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fea00000-0x00000000fea0ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000feb80000-0x00000000fec01fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec10000-0x00000000fec10fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec30000-0x00000000fec30fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed40000-0x00000000fed44fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed80000-0x00000000fed8ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedc2000-0x00000000fedcffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedd4000-0x00000000fedd5fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000feefffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000043f33ffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] e820: update [mem 0x1cdf7018-0x1ce14257] usable ==> usable
[    0.000000] e820: update [mem 0x1cdf7018-0x1ce14257] usable ==> usable
[    0.000000] e820: update [mem 0x1cde8018-0x1cdf6057] usable ==> usable
[    0.000000] e820: update [mem 0x1cde8018-0x1cdf6057] usable ==> usable
[    0.000000] e820: update [mem 0x1cdda018-0x1cde7457] usable ==> usable
[    0.000000] e820: update [mem 0x1cdda018-0x1cde7457] usable ==> usable
[    0.000000] extended physical RAM map:
[    0.000000] reserve setup_data: [mem 0x0000000000000000-0x000000000009ffff] usable
[    0.000000] reserve setup_data: [mem 0x00000000000a0000-0x00000000000fffff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000000100000-0x0000000009e0ffff] usable
[    0.000000] reserve setup_data: [mem 0x0000000009e10000-0x0000000009ffffff] reserved
[    0.000000] reserve setup_data: [mem 0x000000000a000000-0x000000000a1fffff] usable
[    0.000000] reserve setup_data: [mem 0x000000000a200000-0x000000000a20afff] ACPI NVS
[    0.000000] reserve setup_data: [mem 0x000000000a20b000-0x000000000affffff] usable
[    0.000000] reserve setup_data: [mem 0x000000000b000000-0x000000000b01ffff] reserved
[    0.000000] reserve setup_data: [mem 0x000000000b020000-0x000000001cdda017] usable
[    0.000000] reserve setup_data: [mem 0x000000001cdda018-0x000000001cde7457] usable
[    0.000000] reserve setup_data: [mem 0x000000001cde7458-0x000000001cde8017] usable
[    0.000000] reserve setup_data: [mem 0x000000001cde8018-0x000000001cdf6057] usable
[    0.000000] reserve setup_data: [mem 0x000000001cdf6058-0x000000001cdf7017] usable
[    0.000000] reserve setup_data: [mem 0x000000001cdf7018-0x000000001ce14257] usable
[    0.000000] reserve setup_data: [mem 0x000000001ce14258-0x0000000031502fff] usable
[    0.000000] reserve setup_data: [mem 0x0000000031503000-0x000000003151efff] ACPI data
[    0.000000] reserve setup_data: [mem 0x000000003151f000-0x000000003a3d9fff] usable
[    0.000000] reserve setup_data: [mem 0x000000003a3da000-0x000000003a4f1fff] reserved
[    0.000000] reserve setup_data: [mem 0x000000003a4f2000-0x000000003a500fff] ACPI data
[    0.000000] reserve setup_data: [mem 0x000000003a501000-0x000000003a603fff] usable
[    0.000000] reserve setup_data: [mem 0x000000003a604000-0x000000003a9befff] ACPI NVS
[    0.000000] reserve setup_data: [mem 0x000000003a9bf000-0x000000003b77afff] reserved
[    0.000000] reserve setup_data: [mem 0x000000003b77b000-0x000000003dffffff] usable
[    0.000000] reserve setup_data: [mem 0x000000003e000000-0x00000000bfffffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fd100000-0x00000000fd1fffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fea00000-0x00000000fea0ffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000feb80000-0x00000000fec01fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fec10000-0x00000000fec10fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fec30000-0x00000000fec30fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fed40000-0x00000000fed44fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fed80000-0x00000000fed8ffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fedc2000-0x00000000fedcffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fedd4000-0x00000000fedd5fff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000fee00000-0x00000000feefffff] reserved
[    0.000000] reserve setup_data: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] reserve setup_data: [mem 0x0000000100000000-0x000000043f33ffff] usable
[    0.000000] efi: EFI v2.60 by American Megatrends
[    0.000000] efi:  ACPI 2.0=0x31503000  ACPI=0x31503000  SMBIOS=0x3b649000  SMBIOS 3.0=0x3b648000  ESRT=0x37cf6e18  MEMATTR=0x37d75018 
[    0.000000] secureboot: Secure boot disabled
[    0.000000] SMBIOS 3.1.1 present.
[    0.000000] DMI: System manufacturer System Product Name/PRIME B450-PLUS, BIOS 2202 07/14/2020
[    0.000000] tsc: Fast TSC calibration failed
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] last_pfn = 0x43f340 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF write-through
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 000000000000 mask FFFF80000000 write-back
[    0.000000]   1 base 000080000000 mask FFFFC0000000 write-back
[    0.000000]   2 disabled
[    0.000000]   3 disabled
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000] TOM2: 0000000440000000 aka 17408M
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
[    0.000000] last_pfn = 0x3e000 max_arch_pfn = 0x400000000
[    0.000000] esrt: Reserving ESRT space from 0x0000000037cf6e18 to 0x0000000037cf6e50.
[    0.000000] e820: update [mem 0x37cf6000-0x37cf6fff] usable ==> reserved
[    0.000000] check: Scanning 1 areas for low memory corruption
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x3f9801000, 0x3f9801fff] PGTABLE
[    0.000000] BRK [0x3f9802000, 0x3f9802fff] PGTABLE
[    0.000000] BRK [0x3f9803000, 0x3f9803fff] PGTABLE
[    0.000000] BRK [0x3f9804000, 0x3f9804fff] PGTABLE
[    0.000000] BRK [0x3f9805000, 0x3f9805fff] PGTABLE
[    0.000000] BRK [0x3f9806000, 0x3f9806fff] PGTABLE
[    0.000000] BRK [0x3f9807000, 0x3f9807fff] PGTABLE
[    0.000000] BRK [0x3f9808000, 0x3f9808fff] PGTABLE
[    0.000000] BRK [0x3f9809000, 0x3f9809fff] PGTABLE
[    0.000000] BRK [0x3f980a000, 0x3f980afff] PGTABLE
[    0.000000] BRK [0x3f980b000, 0x3f980bfff] PGTABLE
[    0.000000] BRK [0x3f980c000, 0x3f980cfff] PGTABLE
[    0.000000] secureboot: Secure boot disabled
[    0.000000] RAMDISK: [mem 0x1ce15000-0x220ddfff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x0000000031503000 000024 (v02 ALASKA)
[    0.000000] ACPI: XSDT 0x00000000315030A8 0000CC (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x000000003150EA58 000114 (v06 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: DSDT 0x0000000031503210 00B841 (v02 ALASKA A M I    01072009 INTL 20120913)
[    0.000000] ACPI: FACS 0x000000003A9A8E00 000040
[    0.000000] ACPI: APIC 0x000000003150EB70 00015E (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x000000003150ECD0 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FIDT 0x000000003150ED18 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: SSDT 0x000000003150EDB8 000094 (v02 ALASKA CPUSSDT  01072009 AMI  01072009)
[    0.000000] ACPI: SSDT 0x000000003151D148 0010AF (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x000000003150EEA8 005419 (v02 AMD    AmdTable 00000002 MSFT 04000000)
[    0.000000] ACPI: SSDT 0x00000000315142C8 00378A (v01 AMD    AMD AOD  00000001 INTL 20120913)
[    0.000000] ACPI: MCFG 0x0000000031517A58 00003C (v01 ALASKA A M I    01072009 MSFT 00010013)
[    0.000000] ACPI: HPET 0x0000000031517A98 000038 (v01 ALASKA A M I    01072009 AMI  00000005)
[    0.000000] ACPI: UEFI 0x0000000031517AD0 000042 (v01                 00000000      00000000)
[    0.000000] ACPI: BGRT 0x0000000031517B18 000038 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: IVRS 0x0000000031517B50 0000D0 (v02 AMD    AMD IVRS 00000001 AMD  00000000)
[    0.000000] ACPI: SSDT 0x0000000031517C20 00119C (v01 AMD    AMD CPU  00000001 AMD  00000001)
[    0.000000] ACPI: CRAT 0x0000000031518DC0 000810 (v01 AMD    AMD CRAT 00000001 AMD  00000001)
[    0.000000] ACPI: CDIT 0x00000000315195D0 000029 (v01 AMD    AMD CDIT 00000001 AMD  00000001)
[    0.000000] ACPI: SSDT 0x0000000031519600 000C34 (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x000000003151A238 0010AC (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x000000003151B2E8 000050 (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x000000003151B338 001D4A (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x000000003151D088 0000BF (v01 AMD    AMD PT   00001000 INTL 20120913)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000043f33ffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x43f315000-0x43f33ffff]
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000043f33ffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009ffff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x0000000009e0ffff]
[    0.000000]   node   0: [mem 0x000000000a000000-0x000000000a1fffff]
[    0.000000]   node   0: [mem 0x000000000a20b000-0x000000000affffff]
[    0.000000]   node   0: [mem 0x000000000b020000-0x0000000031502fff]
[    0.000000]   node   0: [mem 0x000000003151f000-0x000000003a3d9fff]
[    0.000000]   node   0: [mem 0x000000003a501000-0x000000003a603fff]
[    0.000000]   node   0: [mem 0x000000003b77b000-0x000000003dffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000043f33ffff]
[    0.000000] Zeroed struct page in unavailable ranges: 16886 pages
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000043f33ffff]
[    0.000000] On node 0 totalpages: 3653130
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 27 pages reserved
[    0.000000]   DMA zone: 3999 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 3821 pages used for memmap
[    0.000000]   DMA32 zone: 244523 pages, LIFO batch:63
[    0.000000]   Normal zone: 53197 pages used for memmap
[    0.000000]   Normal zone: 3404608 pages, LIFO batch:63
[    0.000000] ACPI: PM-Timer IO Port: 0x808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 9, version 33, address 0xfec00000, GSI 0-23
[    0.000000] IOAPIC[1]: apic_id 10, version 33, address 0xfec01000, GSI 24-55
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 low level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x10228201 base: 0xfed00000
[    0.000000] e820: update [mem 0x36dd3000-0x36ec6fff] usable ==> reserved
[    0.000000] smpboot: Allowing 32 CPUs, 24 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x09e10000-0x09ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0x0a200000-0x0a20afff]
[    0.000000] PM: Registered nosave memory: [mem 0x0b000000-0x0b01ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x1cdda000-0x1cddafff]
[    0.000000] PM: Registered nosave memory: [mem 0x1cde7000-0x1cde7fff]
[    0.000000] PM: Registered nosave memory: [mem 0x1cde8000-0x1cde8fff]
[    0.000000] PM: Registered nosave memory: [mem 0x1cdf6000-0x1cdf6fff]
[    0.000000] PM: Registered nosave memory: [mem 0x1cdf7000-0x1cdf7fff]
[    0.000000] PM: Registered nosave memory: [mem 0x1ce14000-0x1ce14fff]
[    0.000000] PM: Registered nosave memory: [mem 0x31503000-0x3151efff]
[    0.000000] PM: Registered nosave memory: [mem 0x36dd3000-0x36ec6fff]
[    0.000000] PM: Registered nosave memory: [mem 0x37cf6000-0x37cf6fff]
[    0.000000] PM: Registered nosave memory: [mem 0x3a3da000-0x3a4f1fff]
[    0.000000] PM: Registered nosave memory: [mem 0x3a4f2000-0x3a500fff]
[    0.000000] PM: Registered nosave memory: [mem 0x3a604000-0x3a9befff]
[    0.000000] PM: Registered nosave memory: [mem 0x3a9bf000-0x3b77afff]
[    0.000000] PM: Registered nosave memory: [mem 0x3e000000-0xbfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xc0000000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfd0fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfd100000-0xfd1fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfd200000-0xfe9fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea00000-0xfea0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea10000-0xfeb7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfeb80000-0xfec01fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec02000-0xfec0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec10000-0xfec10fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec11000-0xfec2ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec30000-0xfec30fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec31000-0xfecfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed00000-0xfed00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed01000-0xfed3ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed40000-0xfed44fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed45000-0xfed7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed80000-0xfed8ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed90000-0xfedc1fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedc2000-0xfedcffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd0000-0xfedd3fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd4000-0xfedd5fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd6000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfeefffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfef00000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] [mem 0xc0000000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:32 nr_cpu_ids:32 nr_node_ids:1
[    0.000000] percpu: Embedded 54 pages/cpu s184320 r8192 d28672 u262144
[    0.000000] pcpu-alloc: s184320 r8192 d28672 u262144 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 [0] 08 09 10 11 12 13 14 15 
[    0.000000] pcpu-alloc: [0] 16 17 18 19 20 21 22 23 [0] 24 25 26 27 28 29 30 31 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 3596021
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-5.4.0-40-generic root=/dev/mapper/thorshamma--vg-base ro quiet splash vt.handoff=7
[    0.000000] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes, linear)
[    0.000000] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:on, heap free:off
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 14007520K/14612520K available (14339K kernel code, 2397K rwdata, 4952K rodata, 2712K init, 4992K bss, 605000K reserved, 0K cma-reserved)
[    0.000000] random: get_random_u64 called from kmem_cache_open+0x2d/0x410 with crng_init=0
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=32, Nodes=1
[    0.000000] ftrace: allocating 44488 entries in 174 pages
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000] rcu: 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=32.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=32
[    0.000000] NR_IRQS: 524544, nr_irqs: 1224, preallocated irqs: 16
[    0.000000] random: crng done (trusting CPU's manufacturer)
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] printk: console [tty0] enabled
[    0.000000] ACPI: Core revision 20190816
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484873504 ns
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.004000] Switched APIC routing to physical flat.
[    0.004000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.032000] tsc: PIT calibration matches HPET. 2 loops
[    0.032000] tsc: Detected 3593.198 MHz processor
[    0.000004] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x33cb39bf08d, max_idle_ns: 440795316800 ns
[    0.000006] Calibrating delay loop (skipped), value calculated using timer frequency.. 7186.39 BogoMIPS (lpj=14372792)
[    0.000008] pid_max: default: 32768 minimum: 301
[    0.003380] LSM: Security Framework initializing
[    0.003391] Yama: becoming mindful.
[    0.003528] AppArmor: AppArmor initialized
[    0.003632] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.003668] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.003689] *** VALIDATE tmpfs ***
[    0.003871] *** VALIDATE proc ***
[    0.004017] *** VALIDATE cgroup1 ***
[    0.004018] *** VALIDATE cgroup2 ***
[    0.004203] LVT offset 1 assigned for vector 0xf9
[    0.004243] LVT offset 2 assigned for vector 0xf4
[    0.004256] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 512
[    0.004257] Last level dTLB entries: 4KB 1536, 2MB 1536, 4MB 768, 1GB 0
[    0.004261] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
[    0.004262] Spectre V2 : Mitigation: Full AMD retpoline
[    0.004262] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
[    0.004263] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.004263] Spectre V2 : User space: Vulnerable
[    0.004264] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.004449] Freeing SMP alternatives memory: 40K
[    0.114766] smpboot: CPU0: AMD Ryzen 5 2400G with Radeon Vega Graphics (family: 0x17, model: 0x11, stepping: 0x0)
[    0.115134] Performance Events: Fam17h+ core perfctr, AMD PMU driver.
[    0.115137] ... version:                0
[    0.115138] ... bit width:              48
[    0.115138] ... generic registers:      6
[    0.115139] ... value mask:             0000ffffffffffff
[    0.115139] ... max period:             00007fffffffffff
[    0.115139] ... fixed-purpose events:   0
[    0.115139] ... event mask:             000000000000003f
[    0.115180] rcu: Hierarchical SRCU implementation.
[    0.115810] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.116005] smp: Bringing up secondary CPUs ...
[    0.116005] x86: Booting SMP configuration:
[    0.116005] .... node  #0, CPUs:        #1  #2  #3  #4  #5  #6  #7
[    0.130368] smp: Brought up 1 node, 8 CPUs
[    0.130368] smpboot: Max logical packages: 4
[    0.130368] smpboot: Total of 8 processors activated (57491.16 BogoMIPS)
[    0.132070] devtmpfs: initialized
[    0.132070] x86/mm: Memory block size: 128MB
[    0.132972] PM: Registering ACPI NVS region [mem 0x0a200000-0x0a20afff] (45056 bytes)
[    0.132972] PM: Registering ACPI NVS region [mem 0x3a604000-0x3a9befff] (3911680 bytes)
[    0.132972] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.132972] futex hash table entries: 8192 (order: 7, 524288 bytes, linear)
[    0.133206] pinctrl core: initialized pinctrl subsystem
[    0.133326] PM: RTC time: 03:08:24, date: 2020-07-19
[    0.133531] NET: Registered protocol family 16
[    0.133609] audit: initializing netlink subsys (disabled)
[    0.133615] audit: type=2000 audit(1595128103.164:1): state=initialized audit_enabled=0 res=1
[    0.133615] EISA bus registered
[    0.133615] cpuidle: using governor ladder
[    0.133615] cpuidle: using governor menu
[    0.133615] ACPI: bus type PCI registered
[    0.133615] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.133615] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.133615] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.133615] PCI: Using configuration type 1 for base access
[    0.136330] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.136330] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.140169] ACPI: Added _OSI(Module Device)
[    0.140170] ACPI: Added _OSI(Processor Device)
[    0.140170] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.140171] ACPI: Added _OSI(Processor Aggregator Device)
[    0.140172] ACPI: Added _OSI(Linux-Dell-Video)
[    0.140173] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
[    0.140173] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
[    0.152571] ACPI: 11 ACPI AML tables successfully acquired and loaded
[    0.154256] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.156427] ACPI: Interpreter enabled
[    0.156440] ACPI: (supports S0 S3 S4 S5)
[    0.156441] ACPI: Using IOAPIC for interrupt routing
[    0.156797] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.157155] ACPI: Enabled 4 GPEs in block 00 to 1F
[    0.172280] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.172286] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
[    0.172553] acpi PNP0A08:00: _OSC: platform does not support [SHPCHotplug LTR]
[    0.172809] acpi PNP0A08:00: _OSC: OS now controls [PCIeHotplug PME AER PCIeCapability]
[    0.172824] acpi PNP0A08:00: [Firmware Info]: MMCONFIG for domain 0000 [bus 00-3f] only partially covers this bridge
[    0.173148] PCI host bridge to bus 0000:00
[    0.173150] pci_bus 0000:00: root bus resource [io  0x0000-0x03af window]
[    0.173150] pci_bus 0000:00: root bus resource [io  0x03e0-0x0cf7 window]
[    0.173151] pci_bus 0000:00: root bus resource [io  0x03b0-0x03df window]
[    0.173152] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
[    0.173153] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.173153] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.173154] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfec2ffff window]
[    0.173155] pci_bus 0000:00: root bus resource [mem 0xfee00000-0xffffffff window]
[    0.173156] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.173165] pci 0000:00:00.0: [1022:15d0] type 00 class 0x060000
[    0.173290] pci 0000:00:00.2: [1022:15d1] type 00 class 0x080600
[    0.173442] pci 0000:00:01.0: [1022:1452] type 00 class 0x060000
[    0.173540] pci 0000:00:01.1: [1022:15d3] type 01 class 0x060400
[    0.173656] pci 0000:00:01.1: PME# supported from D0 D3hot D3cold
[    0.173791] pci 0000:00:01.2: [1022:15d3] type 01 class 0x060400
[    0.173846] pci 0000:00:01.2: enabling Extended Tags
[    0.173912] pci 0000:00:01.2: PME# supported from D0 D3hot D3cold
[    0.174051] pci 0000:00:08.0: [1022:1452] type 00 class 0x060000
[    0.174160] pci 0000:00:08.1: [1022:15db] type 01 class 0x060400
[    0.174218] pci 0000:00:08.1: enabling Extended Tags
[    0.174279] pci 0000:00:08.1: PME# supported from D0 D3hot D3cold
[    0.174391] pci 0000:00:08.2: [1022:15dc] type 01 class 0x060400
[    0.174451] pci 0000:00:08.2: enabling Extended Tags
[    0.174515] pci 0000:00:08.2: PME# supported from D0 D3hot D3cold
[    0.174669] pci 0000:00:14.0: [1022:790b] type 00 class 0x0c0500
[    0.174843] pci 0000:00:14.3: [1022:790e] type 00 class 0x060100
[    0.175036] pci 0000:00:18.0: [1022:15e8] type 00 class 0x060000
[    0.175079] pci 0000:00:18.1: [1022:15e9] type 00 class 0x060000
[    0.175121] pci 0000:00:18.2: [1022:15ea] type 00 class 0x060000
[    0.175163] pci 0000:00:18.3: [1022:15eb] type 00 class 0x060000
[    0.175204] pci 0000:00:18.4: [1022:15ec] type 00 class 0x060000
[    0.175245] pci 0000:00:18.5: [1022:15ed] type 00 class 0x060000
[    0.175289] pci 0000:00:18.6: [1022:15ee] type 00 class 0x060000
[    0.175331] pci 0000:00:18.7: [1022:15ef] type 00 class 0x060000
[    0.175466] pci 0000:01:00.0: [1002:67ef] type 00 class 0x030000
[    0.175510] pci 0000:01:00.0: reg 0x10: [mem 0xe0000000-0xefffffff 64bit pref]
[    0.175524] pci 0000:01:00.0: reg 0x18: [mem 0xf0000000-0xf01fffff 64bit pref]
[    0.175532] pci 0000:01:00.0: reg 0x20: [io  0xf000-0xf0ff]
[    0.175539] pci 0000:01:00.0: reg 0x24: [mem 0xfcf00000-0xfcf3ffff]
[    0.175547] pci 0000:01:00.0: reg 0x30: [mem 0xfcf40000-0xfcf5ffff pref]
[    0.175668] pci 0000:01:00.0: supports D1 D2
[    0.175669] pci 0000:01:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.175824] pci 0000:01:00.1: [1002:aae0] type 00 class 0x040300
[    0.175861] pci 0000:01:00.1: reg 0x10: [mem 0xfcf60000-0xfcf63fff 64bit]
[    0.175995] pci 0000:01:00.1: supports D1 D2
[    0.176161] pci 0000:00:01.1: PCI bridge to [bus 01]
[    0.176166] pci 0000:00:01.1:   bridge window [io  0xf000-0xffff]
[    0.176169] pci 0000:00:01.1:   bridge window [mem 0xfcf00000-0xfcffffff]
[    0.176174] pci 0000:00:01.1:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.176240] pci 0000:02:00.0: [1022:43d5] type 00 class 0x0c0330
[    0.176269] pci 0000:02:00.0: reg 0x10: [mem 0xfcda0000-0xfcda7fff 64bit]
[    0.176318] pci 0000:02:00.0: enabling Extended Tags
[    0.176380] pci 0000:02:00.0: PME# supported from D3hot D3cold
[    0.176476] pci 0000:02:00.1: [1022:43c8] type 00 class 0x010601
[    0.176537] pci 0000:02:00.1: reg 0x24: [mem 0xfcd80000-0xfcd9ffff]
[    0.176546] pci 0000:02:00.1: reg 0x30: [mem 0xfcd00000-0xfcd7ffff pref]
[    0.176554] pci 0000:02:00.1: enabling Extended Tags
[    0.176603] pci 0000:02:00.1: PME# supported from D3hot D3cold
[    0.176672] pci 0000:02:00.2: [1022:43c6] type 01 class 0x060400
[    0.176730] pci 0000:02:00.2: enabling Extended Tags
[    0.176785] pci 0000:02:00.2: PME# supported from D3hot D3cold
[    0.176908] pci 0000:00:01.2: PCI bridge to [bus 02-08]
[    0.176913] pci 0000:00:01.2:   bridge window [io  0xe000-0xefff]
[    0.176916] pci 0000:00:01.2:   bridge window [mem 0xfcc00000-0xfcdfffff]
[    0.177018] pci 0000:03:00.0: [1022:43c7] type 01 class 0x060400
[    0.177082] pci 0000:03:00.0: enabling Extended Tags
[    0.177150] pci 0000:03:00.0: PME# supported from D3hot D3cold
[    0.177254] pci 0000:03:01.0: [1022:43c7] type 01 class 0x060400
[    0.177318] pci 0000:03:01.0: enabling Extended Tags
[    0.177386] pci 0000:03:01.0: PME# supported from D3hot D3cold
[    0.177476] pci 0000:03:04.0: [1022:43c7] type 01 class 0x060400
[    0.177540] pci 0000:03:04.0: enabling Extended Tags
[    0.177608] pci 0000:03:04.0: PME# supported from D3hot D3cold
[    0.177699] pci 0000:03:06.0: [1022:43c7] type 01 class 0x060400
[    0.177762] pci 0000:03:06.0: enabling Extended Tags
[    0.177830] pci 0000:03:06.0: PME# supported from D3hot D3cold
[    0.177920] pci 0000:03:07.0: [1022:43c7] type 01 class 0x060400
[    0.177984] pci 0000:03:07.0: enabling Extended Tags
[    0.178052] pci 0000:03:07.0: PME# supported from D3hot D3cold
[    0.178161] pci 0000:02:00.2: PCI bridge to [bus 03-08]
[    0.178166] pci 0000:02:00.2:   bridge window [io  0xe000-0xefff]
[    0.178169] pci 0000:02:00.2:   bridge window [mem 0xfcc00000-0xfccfffff]
[    0.178241] pci 0000:04:00.0: [10ec:8168] type 00 class 0x020000
[    0.178289] pci 0000:04:00.0: reg 0x10: [io  0xe000-0xe0ff]
[    0.178330] pci 0000:04:00.0: reg 0x18: [mem 0xfcc04000-0xfcc04fff 64bit]
[    0.178355] pci 0000:04:00.0: reg 0x20: [mem 0xfcc00000-0xfcc03fff 64bit]
[    0.178516] pci 0000:04:00.0: supports D1 D2
[    0.178516] pci 0000:04:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[    0.178738] pci 0000:03:00.0: PCI bridge to [bus 04]
[    0.178744] pci 0000:03:00.0:   bridge window [io  0xe000-0xefff]
[    0.178747] pci 0000:03:00.0:   bridge window [mem 0xfcc00000-0xfccfffff]
[    0.178797] pci 0000:03:01.0: PCI bridge to [bus 05]
[    0.178853] pci 0000:03:04.0: PCI bridge to [bus 06]
[    0.178910] pci 0000:03:06.0: PCI bridge to [bus 07]
[    0.178966] pci 0000:03:07.0: PCI bridge to [bus 08]
[    0.179114] pci 0000:09:00.0: [1002:15dd] type 00 class 0x030000
[    0.179160] pci 0000:09:00.0: reg 0x10: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.179177] pci 0000:09:00.0: reg 0x18: [mem 0xd0000000-0xd01fffff 64bit pref]
[    0.179189] pci 0000:09:00.0: reg 0x20: [io  0xd000-0xd0ff]
[    0.179200] pci 0000:09:00.0: reg 0x24: [mem 0xfcb00000-0xfcb7ffff]
[    0.179220] pci 0000:09:00.0: enabling Extended Tags
[    0.179234] pci 0000:09:00.0: BAR 0: assigned to efifb
[    0.179339] pci 0000:09:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.179464] pci 0000:09:00.1: [1002:15de] type 00 class 0x040300
[    0.179493] pci 0000:09:00.1: reg 0x10: [mem 0xfcb88000-0xfcb8bfff]
[    0.179564] pci 0000:09:00.1: enabling Extended Tags
[    0.179634] pci 0000:09:00.1: PME# supported from D1 D2 D3hot D3cold
[    0.179705] pci 0000:09:00.2: [1022:15df] type 00 class 0x108000
[    0.179755] pci 0000:09:00.2: reg 0x18: [mem 0xfca00000-0xfcafffff]
[    0.179786] pci 0000:09:00.2: reg 0x24: [mem 0xfcb8c000-0xfcb8dfff]
[    0.179806] pci 0000:09:00.2: enabling Extended Tags
[    0.179965] pci 0000:09:00.3: [1022:15e0] type 00 class 0x0c0330
[    0.179999] pci 0000:09:00.3: reg 0x10: [mem 0xfc900000-0xfc9fffff 64bit]
[    0.180062] pci 0000:09:00.3: enabling Extended Tags
[    0.180139] pci 0000:09:00.3: PME# supported from D0 D3hot D3cold
[    0.180224] pci 0000:09:00.4: [1022:15e1] type 00 class 0x0c0330
[    0.180259] pci 0000:09:00.4: reg 0x10: [mem 0xfc800000-0xfc8fffff 64bit]
[    0.180319] pci 0000:09:00.4: enabling Extended Tags
[    0.180396] pci 0000:09:00.4: PME# supported from D0 D3hot D3cold
[    0.180496] pci 0000:09:00.6: [1022:15e3] type 00 class 0x040300
[    0.180525] pci 0000:09:00.6: reg 0x10: [mem 0xfcb80000-0xfcb87fff]
[    0.180596] pci 0000:09:00.6: enabling Extended Tags
[    0.180665] pci 0000:09:00.6: PME# supported from D0 D3hot D3cold
[    0.180809] pci 0000:00:08.1: PCI bridge to [bus 09]
[    0.180814] pci 0000:00:08.1:   bridge window [io  0xd000-0xdfff]
[    0.180817] pci 0000:00:08.1:   bridge window [mem 0xfc800000-0xfcbfffff]
[    0.180822] pci 0000:00:08.1:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.180902] pci 0000:0a:00.0: [1022:7901] type 00 class 0x010601
[    0.180987] pci 0000:0a:00.0: reg 0x24: [mem 0xfce00000-0xfce007ff]
[    0.181006] pci 0000:0a:00.0: enabling Extended Tags
[    0.181095] pci 0000:0a:00.0: PME# supported from D3hot D3cold
[    0.181240] pci 0000:00:08.2: PCI bridge to [bus 0a]
[    0.181248] pci 0000:00:08.2:   bridge window [mem 0xfce00000-0xfcefffff]
[    0.181786] ACPI: PCI Interrupt Link [LNKA] (IRQs 4 5 7 10 11 14 15) *0
[    0.181844] ACPI: PCI Interrupt Link [LNKB] (IRQs 4 5 7 10 11 14 15) *0
[    0.181892] ACPI: PCI Interrupt Link [LNKC] (IRQs 4 5 7 10 11 14 15) *0
[    0.181954] ACPI: PCI Interrupt Link [LNKD] (IRQs 4 5 7 10 11 14 15) *0
[    0.182010] ACPI: PCI Interrupt Link [LNKE] (IRQs 4 5 7 10 11 14 15) *0
[    0.182054] ACPI: PCI Interrupt Link [LNKF] (IRQs 4 5 7 10 11 14 15) *0
[    0.182101] ACPI: PCI Interrupt Link [LNKG] (IRQs 4 5 7 10 11 14 15) *0
[    0.182146] ACPI: PCI Interrupt Link [LNKH] (IRQs 4 5 7 10 11 14 15) *0
[    0.182586] iommu: Default domain type: Translated 
[    0.182586] SCSI subsystem initialized
[    0.182586] libata version 3.00 loaded.
[    0.182586] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.182586] pci 0000:09:00.0: vgaarb: setting as boot VGA device
[    0.182586] pci 0000:09:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.182586] pci 0000:01:00.0: vgaarb: bridge control possible
[    0.182586] pci 0000:09:00.0: vgaarb: bridge control possible
[    0.182586] vgaarb: loaded
[    0.182586] ACPI: bus type USB registered
[    0.182586] usbcore: registered new interface driver usbfs
[    0.182586] usbcore: registered new interface driver hub
[    0.182586] usbcore: registered new device driver usb
[    0.182586] pps_core: LinuxPPS API ver. 1 registered
[    0.182586] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.182586] PTP clock support registered
[    0.182586] EDAC MC: Ver: 3.0.0
[    0.184147] Registered efivars operations
[    0.184147] PCI: Using ACPI for IRQ routing
[    0.186909] PCI: pci_cache_line_size set to 64 bytes
[    0.187012] e820: reserve RAM buffer [mem 0x09e10000-0x0bffffff]
[    0.187013] e820: reserve RAM buffer [mem 0x0a200000-0x0bffffff]
[    0.187014] e820: reserve RAM buffer [mem 0x0b000000-0x0bffffff]
[    0.187014] e820: reserve RAM buffer [mem 0x1cdda018-0x1fffffff]
[    0.187015] e820: reserve RAM buffer [mem 0x1cde8018-0x1fffffff]
[    0.187016] e820: reserve RAM buffer [mem 0x1cdf7018-0x1fffffff]
[    0.187017] e820: reserve RAM buffer [mem 0x31503000-0x33ffffff]
[    0.187017] e820: reserve RAM buffer [mem 0x36dd3000-0x37ffffff]
[    0.187018] e820: reserve RAM buffer [mem 0x37cf6000-0x37ffffff]
[    0.187019] e820: reserve RAM buffer [mem 0x3a3da000-0x3bffffff]
[    0.187020] e820: reserve RAM buffer [mem 0x3a604000-0x3bffffff]
[    0.187020] e820: reserve RAM buffer [mem 0x3e000000-0x3fffffff]
[    0.187021] e820: reserve RAM buffer [mem 0x43f340000-0x43fffffff]
[    0.187123] NetLabel: Initializing
[    0.187123] NetLabel:  domain hash size = 128
[    0.187124] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.187141] NetLabel:  unlabeled traffic allowed by default
[    0.187154] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.187154] hpet0: 3 comparators, 32-bit 14.318180 MHz counter
[    0.189057] clocksource: Switched to clocksource tsc-early
[    0.198658] *** VALIDATE bpf ***
[    0.198761] VFS: Disk quotas dquot_6.6.0
[    0.198782] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.198808] *** VALIDATE ramfs ***
[    0.198811] *** VALIDATE hugetlbfs ***
[    0.198901] AppArmor: AppArmor Filesystem Enabled
[    0.198928] pnp: PnP ACPI init
[    0.199083] system 00:00: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.199087] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.199150] system 00:01: [mem 0x40000000-0xbfffffff window] has been reserved
[    0.199152] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.199304] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.199451] system 00:03: [io  0x0300-0x030f] has been reserved
[    0.199452] system 00:03: [io  0x0230-0x023f] has been reserved
[    0.199453] system 00:03: [io  0x0290-0x029f] has been reserved
[    0.199455] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.199752] pnp 00:04: [dma 0 disabled]
[    0.199793] pnp 00:04: Plug and Play ACPI device, IDs PNP0501 (active)
[    0.199993] system 00:05: [io  0x04d0-0x04d1] has been reserved
[    0.199994] system 00:05: [io  0x040b] has been reserved
[    0.199994] system 00:05: [io  0x04d6] has been reserved
[    0.199995] system 00:05: [io  0x0c00-0x0c01] has been reserved
[    0.199996] system 00:05: [io  0x0c14] has been reserved
[    0.199997] system 00:05: [io  0x0c50-0x0c51] has been reserved
[    0.199997] system 00:05: [io  0x0c52] has been reserved
[    0.199998] system 00:05: [io  0x0c6c] has been reserved
[    0.199999] system 00:05: [io  0x0c6f] has been reserved
[    0.200000] system 00:05: [io  0x0cd0-0x0cd1] has been reserved
[    0.200000] system 00:05: [io  0x0cd2-0x0cd3] has been reserved
[    0.200001] system 00:05: [io  0x0cd4-0x0cd5] has been reserved
[    0.200002] system 00:05: [io  0x0cd6-0x0cd7] has been reserved
[    0.200002] system 00:05: [io  0x0cd8-0x0cdf] has been reserved
[    0.200003] system 00:05: [io  0x0800-0x089f] has been reserved
[    0.200004] system 00:05: [io  0x0b00-0x0b0f] has been reserved
[    0.200005] system 00:05: [io  0x0b20-0x0b3f] has been reserved
[    0.200005] system 00:05: [io  0x0900-0x090f] has been reserved
[    0.200006] system 00:05: [io  0x0910-0x091f] has been reserved
[    0.200008] system 00:05: [mem 0xfec00000-0xfec00fff] could not be reserved
[    0.200009] system 00:05: [mem 0xfec01000-0xfec01fff] could not be reserved
[    0.200010] system 00:05: [mem 0xfedc0000-0xfedc0fff] has been reserved
[    0.200011] system 00:05: [mem 0xfee00000-0xfee00fff] has been reserved
[    0.200012] system 00:05: [mem 0xfed80000-0xfed8ffff] could not be reserved
[    0.200013] system 00:05: [mem 0xfec10000-0xfec10fff] has been reserved
[    0.200014] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.200016] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.200495] pnp: PnP ACPI: found 6 devices
[    0.201813] thermal_sys: Registered thermal governor 'fair_share'
[    0.201814] thermal_sys: Registered thermal governor 'bang_bang'
[    0.201814] thermal_sys: Registered thermal governor 'step_wise'
[    0.201815] thermal_sys: Registered thermal governor 'user_space'
[    0.201815] thermal_sys: Registered thermal governor 'power_allocator'
[    0.206381] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.206413] pci 0000:00:01.1: PCI bridge to [bus 01]
[    0.206416] pci 0000:00:01.1:   bridge window [io  0xf000-0xffff]
[    0.206421] pci 0000:00:01.1:   bridge window [mem 0xfcf00000-0xfcffffff]
[    0.206424] pci 0000:00:01.1:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.206430] pci 0000:03:00.0: PCI bridge to [bus 04]
[    0.206432] pci 0000:03:00.0:   bridge window [io  0xe000-0xefff]
[    0.206436] pci 0000:03:00.0:   bridge window [mem 0xfcc00000-0xfccfffff]
[    0.206445] pci 0000:03:01.0: PCI bridge to [bus 05]
[    0.206457] pci 0000:03:04.0: PCI bridge to [bus 06]
[    0.206468] pci 0000:03:06.0: PCI bridge to [bus 07]
[    0.206480] pci 0000:03:07.0: PCI bridge to [bus 08]
[    0.206492] pci 0000:02:00.2: PCI bridge to [bus 03-08]
[    0.206494] pci 0000:02:00.2:   bridge window [io  0xe000-0xefff]
[    0.206498] pci 0000:02:00.2:   bridge window [mem 0xfcc00000-0xfccfffff]
[    0.206506] pci 0000:00:01.2: PCI bridge to [bus 02-08]
[    0.206507] pci 0000:00:01.2:   bridge window [io  0xe000-0xefff]
[    0.206512] pci 0000:00:01.2:   bridge window [mem 0xfcc00000-0xfcdfffff]
[    0.206521] pci 0000:00:08.1: PCI bridge to [bus 09]
[    0.206527] pci 0000:00:08.1:   bridge window [io  0xd000-0xdfff]
[    0.206531] pci 0000:00:08.1:   bridge window [mem 0xfc800000-0xfcbfffff]
[    0.206535] pci 0000:00:08.1:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.206540] pci 0000:00:08.2: PCI bridge to [bus 0a]
[    0.206544] pci 0000:00:08.2:   bridge window [mem 0xfce00000-0xfcefffff]
[    0.206553] pci_bus 0000:00: resource 4 [io  0x0000-0x03af window]
[    0.206554] pci_bus 0000:00: resource 5 [io  0x03e0-0x0cf7 window]
[    0.206555] pci_bus 0000:00: resource 6 [io  0x03b0-0x03df window]
[    0.206555] pci_bus 0000:00: resource 7 [io  0x0d00-0xffff window]
[    0.206556] pci_bus 0000:00: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.206557] pci_bus 0000:00: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.206558] pci_bus 0000:00: resource 10 [mem 0xc0000000-0xfec2ffff window]
[    0.206559] pci_bus 0000:00: resource 11 [mem 0xfee00000-0xffffffff window]
[    0.206560] pci_bus 0000:01: resource 0 [io  0xf000-0xffff]
[    0.206560] pci_bus 0000:01: resource 1 [mem 0xfcf00000-0xfcffffff]
[    0.206561] pci_bus 0000:01: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.206562] pci_bus 0000:02: resource 0 [io  0xe000-0xefff]
[    0.206562] pci_bus 0000:02: resource 1 [mem 0xfcc00000-0xfcdfffff]
[    0.206563] pci_bus 0000:03: resource 0 [io  0xe000-0xefff]
[    0.206564] pci_bus 0000:03: resource 1 [mem 0xfcc00000-0xfccfffff]
[    0.206565] pci_bus 0000:04: resource 0 [io  0xe000-0xefff]
[    0.206565] pci_bus 0000:04: resource 1 [mem 0xfcc00000-0xfccfffff]
[    0.206566] pci_bus 0000:09: resource 0 [io  0xd000-0xdfff]
[    0.206567] pci_bus 0000:09: resource 1 [mem 0xfc800000-0xfcbfffff]
[    0.206568] pci_bus 0000:09: resource 2 [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.206569] pci_bus 0000:0a: resource 1 [mem 0xfce00000-0xfcefffff]
[    0.206674] NET: Registered protocol family 2
[    0.206918] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes, linear)
[    0.207036] TCP established hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[    0.207233] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    0.207301] TCP: Hash tables configured (established 131072 bind 65536)
[    0.207365] UDP hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    0.207407] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    0.207498] NET: Registered protocol family 1
[    0.207502] NET: Registered protocol family 44
[    0.207550] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
[    0.207778] pci 0000:09:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.207785] pci 0000:09:00.1: D0 power state depends on 0000:09:00.0
[    0.207791] pci 0000:09:00.3: extending delay after power-on from D3hot to 20 msec
[    0.207966] pci 0000:09:00.4: extending delay after power-on from D3hot to 20 msec
[    0.208056] PCI: CLS 64 bytes, default 64
[    0.208097] Trying to unpack rootfs image as initramfs...
[    0.361647] Initramfs unpacking failed: Decoding failed
[    0.374578] Freeing initrd memory: 84772K
[    0.374704] pci 0000:00:00.2: AMD-Vi: Unable to read/write to IOMMU perf counter.
[    0.374815] pci 0000:00:00.2: can't derive routing for PCI INT A
[    0.374815] pci 0000:00:00.2: PCI INT A: not connected
[    0.375405] pci 0000:00:01.0: Adding to iommu group 0
[    0.375647] pci 0000:00:01.1: Adding to iommu group 1
[    0.375928] pci 0000:00:01.2: Adding to iommu group 2
[    0.376156] pci 0000:00:08.0: Adding to iommu group 3
[    0.376425] pci 0000:00:08.1: Adding to iommu group 4
[    0.376725] pci 0000:00:08.2: Adding to iommu group 5
[    0.376942] pci 0000:00:14.0: Adding to iommu group 6
[    0.376964] pci 0000:00:14.3: Adding to iommu group 6
[    0.377287] pci 0000:00:18.0: Adding to iommu group 7
[    0.377311] pci 0000:00:18.1: Adding to iommu group 7
[    0.377333] pci 0000:00:18.2: Adding to iommu group 7
[    0.377354] pci 0000:00:18.3: Adding to iommu group 7
[    0.377376] pci 0000:00:18.4: Adding to iommu group 7
[    0.377397] pci 0000:00:18.5: Adding to iommu group 7
[    0.377419] pci 0000:00:18.6: Adding to iommu group 7
[    0.377440] pci 0000:00:18.7: Adding to iommu group 7
[    0.377706] pci 0000:01:00.0: Adding to iommu group 8
[    0.377765] pci 0000:01:00.0: Using iommu direct mapping
[    0.377814] pci 0000:01:00.1: Adding to iommu group 8
[    0.377958] pci 0000:02:00.0: Adding to iommu group 9
[    0.377994] pci 0000:02:00.1: Adding to iommu group 9
[    0.378028] pci 0000:02:00.2: Adding to iommu group 9
[    0.378051] pci 0000:03:00.0: Adding to iommu group 9
[    0.378073] pci 0000:03:01.0: Adding to iommu group 9
[    0.378095] pci 0000:03:04.0: Adding to iommu group 9
[    0.378118] pci 0000:03:06.0: Adding to iommu group 9
[    0.378140] pci 0000:03:07.0: Adding to iommu group 9
[    0.378172] pci 0000:04:00.0: Adding to iommu group 9
[    0.378534] pci 0000:09:00.0: Adding to iommu group 10
[    0.378645] pci 0000:09:00.0: Using iommu direct mapping
[    0.378814] pci 0000:09:00.1: Adding to iommu group 11
[    0.378856] pci 0000:09:00.2: Adding to iommu group 11
[    0.378897] pci 0000:09:00.3: Adding to iommu group 11
[    0.378938] pci 0000:09:00.4: Adding to iommu group 11
[    0.378979] pci 0000:09:00.6: Adding to iommu group 11
[    0.379193] pci 0000:0a:00.0: Adding to iommu group 12
[    0.379493] pci 0000:00:00.2: AMD-Vi: Found IOMMU cap 0x40
[    0.379494] pci 0000:00:00.2: AMD-Vi: Extended features (0x4f77ef22294ada):
[    0.379495]  PPR NX GT IA GA PC GA_vAPIC
[    0.379496] AMD-Vi: Interrupt remapping enabled
[    0.379497] AMD-Vi: Virtual APIC enabled
[    0.379679] AMD-Vi: Lazy IO/TLB flushing enabled
[    0.380579] amd_uncore: AMD NB counters detected
[    0.380591] amd_uncore: AMD LLC counters detected
[    0.380811] check: Scanning for low memory corruption every 60 seconds
[    0.382701] Initialise system trusted keyrings
[    0.382792] Key type blacklist registered
[    0.382880] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    0.383778] zbud: loaded
[    0.384102] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.384254] fuse: init (API version 7.31)
[    0.384279] *** VALIDATE fuse ***
[    0.384281] *** VALIDATE fuse ***
[    0.384443] Platform Keyring initialized
[    0.388195] Key type asymmetric registered
[    0.388196] Asymmetric key parser 'x509' registered
[    0.388202] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 244)
[    0.388253] io scheduler mq-deadline registered
[    0.389192] pcieport 0000:00:01.1: PME: Signaling with IRQ 26
[    0.389246] pcieport 0000:00:01.1: AER: enabled with IRQ 26
[    0.389406] pcieport 0000:00:01.2: PME: Signaling with IRQ 27
[    0.389480] pcieport 0000:00:01.2: AER: enabled with IRQ 27
[    0.389624] pcieport 0000:00:08.1: PME: Signaling with IRQ 28
[    0.389831] pcieport 0000:00:08.2: PME: Signaling with IRQ 29
[    0.389877] pcieport 0000:00:08.2: AER: enabled with IRQ 29
[    0.390842] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
[    0.390883] efifb: probing for efifb
[    0.390917] efifb: showing boot graphics
[    0.394281] efifb: framebuffer at 0xc0000000, using 8100k, total 8100k
[    0.394282] efifb: mode is 1920x1080x32, linelength=7680, pages=1
[    0.394282] efifb: scrolling: redraw
[    0.394283] efifb: Truecolor: size=8:8:8:8, shift=24:16:8:0
[    0.394334] fbcon: Deferring console take-over
[    0.394335] fb0: EFI VGA frame buffer device
[    0.394428] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    0.394445] ACPI: Power Button [PWRB]
[    0.394468] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    0.394493] ACPI: Power Button [PWRF]
[    0.394532] Monitor-Mwait will be used to enter C-1 state
[    0.395377] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.416275] 00:04: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    0.417526] Linux agpgart interface v0.103
[    0.420996] loop: module loaded
[    0.421205] libphy: Fixed MDIO Bus: probed
[    0.421205] tun: Universal TUN/TAP device driver, 1.6
[    0.421256] PPP generic driver version 2.4.2
[    0.421311] VFIO - User Level meta-driver version: 0.3
[    0.421420] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.421425] ehci-pci: EHCI PCI platform driver
[    0.421441] ehci-platform: EHCI generic platform driver
[    0.421449] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.421451] ohci-pci: OHCI PCI platform driver
[    0.421460] ohci-platform: OHCI generic platform driver
[    0.421466] uhci_hcd: USB Universal Host Controller Interface driver
[    0.421611] xhci_hcd 0000:02:00.0: xHCI Host Controller
[    0.421616] xhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 1
[    0.476940] xhci_hcd 0000:02:00.0: hcc params 0x0200ef81 hci version 0x110 quirks 0x0000000000000410
[    0.477151] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    0.477152] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.477153] usb usb1: Product: xHCI Host Controller
[    0.477153] usb usb1: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.477154] usb usb1: SerialNumber: 0000:02:00.0
[    0.477275] hub 1-0:1.0: USB hub found
[    0.477291] hub 1-0:1.0: 10 ports detected
[    0.482565] xhci_hcd 0000:02:00.0: xHCI Host Controller
[    0.482567] xhci_hcd 0000:02:00.0: new USB bus registered, assigned bus number 2
[    0.482569] xhci_hcd 0000:02:00.0: Host supports USB 3.1 Enhanced SuperSpeed
[    0.482611] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.482624] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    0.482625] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.482626] usb usb2: Product: xHCI Host Controller
[    0.482626] usb usb2: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.482627] usb usb2: SerialNumber: 0000:02:00.0
[    0.482723] hub 2-0:1.0: USB hub found
[    0.482731] hub 2-0:1.0: 4 ports detected
[    0.484927] xhci_hcd 0000:09:00.3: xHCI Host Controller
[    0.484930] xhci_hcd 0000:09:00.3: new USB bus registered, assigned bus number 3
[    0.485114] xhci_hcd 0000:09:00.3: hcc params 0x0270ffe5 hci version 0x110 quirks 0x0000000840000410
[    0.485575] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    0.485576] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.485577] usb usb3: Product: xHCI Host Controller
[    0.485577] usb usb3: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.485578] usb usb3: SerialNumber: 0000:09:00.3
[    0.485659] hub 3-0:1.0: USB hub found
[    0.485669] hub 3-0:1.0: 4 ports detected
[    0.486097] xhci_hcd 0000:09:00.3: xHCI Host Controller
[    0.486098] xhci_hcd 0000:09:00.3: new USB bus registered, assigned bus number 4
[    0.486100] xhci_hcd 0000:09:00.3: Host supports USB 3.1 Enhanced SuperSpeed
[    0.486123] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.486135] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    0.486136] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.486137] usb usb4: Product: xHCI Host Controller
[    0.486137] usb usb4: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.486138] usb usb4: SerialNumber: 0000:09:00.3
[    0.486234] hub 4-0:1.0: USB hub found
[    0.486246] hub 4-0:1.0: 4 ports detected
[    0.486378] usb: port power management may be unreliable
[    0.486747] xhci_hcd 0000:09:00.4: xHCI Host Controller
[    0.486750] xhci_hcd 0000:09:00.4: new USB bus registered, assigned bus number 5
[    0.486906] xhci_hcd 0000:09:00.4: hcc params 0x0260ffe5 hci version 0x110 quirks 0x0000000840000410
[    0.487315] usb usb5: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
[    0.487315] usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.487316] usb usb5: Product: xHCI Host Controller
[    0.487317] usb usb5: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.487317] usb usb5: SerialNumber: 0000:09:00.4
[    0.487409] hub 5-0:1.0: USB hub found
[    0.487418] hub 5-0:1.0: 1 port detected
[    0.487513] xhci_hcd 0000:09:00.4: xHCI Host Controller
[    0.487516] xhci_hcd 0000:09:00.4: new USB bus registered, assigned bus number 6
[    0.487519] xhci_hcd 0000:09:00.4: Host supports USB 3.1 Enhanced SuperSpeed
[    0.487542] usb usb6: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.487555] usb usb6: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
[    0.487556] usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.487556] usb usb6: Product: xHCI Host Controller
[    0.487557] usb usb6: Manufacturer: Linux 5.4.0-40-generic xhci-hcd
[    0.487557] usb usb6: SerialNumber: 0000:09:00.4
[    0.487640] hub 6-0:1.0: USB hub found
[    0.487649] hub 6-0:1.0: 1 port detected
[    0.487726] i8042: PNP: No PS/2 controller found.
[    0.487799] mousedev: PS/2 mouse device common for all mice
[    0.487910] rtc_cmos 00:02: RTC can wake from S4
[    0.488152] rtc_cmos 00:02: registered as rtc0
[    0.488161] rtc_cmos 00:02: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    0.488164] i2c /dev entries driver
[    0.488198] device-mapper: uevent: version 1.0.3
[    0.488259] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
[    0.488274] platform eisa.0: Probing EISA bus 0
[    0.488275] platform eisa.0: EISA: Cannot allocate resource for mainboard
[    0.488276] platform eisa.0: Cannot allocate resource for EISA slot 1
[    0.488277] platform eisa.0: Cannot allocate resource for EISA slot 2
[    0.488277] platform eisa.0: Cannot allocate resource for EISA slot 3
[    0.488278] platform eisa.0: Cannot allocate resource for EISA slot 4
[    0.488279] platform eisa.0: Cannot allocate resource for EISA slot 5
[    0.488279] platform eisa.0: Cannot allocate resource for EISA slot 6
[    0.488280] platform eisa.0: Cannot allocate resource for EISA slot 7
[    0.488281] platform eisa.0: Cannot allocate resource for EISA slot 8
[    0.488281] platform eisa.0: EISA: Detected 0 cards
[    0.488427] ledtrig-cpu: registered to indicate activity on CPUs
[    0.488430] EFI Variables Facility v0.08 2004-May-17
[    0.515526] drop_monitor: Initializing network drop monitor service
[    0.515690] NET: Registered protocol family 10
[    0.521150] Segment Routing with IPv6
[    0.521171] NET: Registered protocol family 17
[    0.521239] Key type dns_resolver registered
[    0.521744] RAS: Correctable Errors collector initialized.
[    0.521778] microcode: CPU0: patch_level=0x08101016
[    0.521786] microcode: CPU1: patch_level=0x08101016
[    0.521793] microcode: CPU2: patch_level=0x08101016
[    0.521800] microcode: CPU3: patch_level=0x08101016
[    0.521802] microcode: CPU4: patch_level=0x08101016
[    0.521807] microcode: CPU5: patch_level=0x08101016
[    0.521815] microcode: CPU6: patch_level=0x08101016
[    0.521822] microcode: CPU7: patch_level=0x08101016
[    0.521843] microcode: Microcode Update Driver: v2.2.
[    0.521847] IPI shorthand broadcast: enabled
[    0.521865] sched_clock: Marking stable (553835280, -31994409)->(526133780, -4292909)
[    0.521963] registered taskstats version 1
[    0.521971] Loading compiled-in X.509 certificates
[    0.523333] Loaded X.509 cert 'Build time autogenerated kernel key: c7397aba4b613cce0e4070f289f6e01155c15620'
[    0.523369] zswap: loaded using pool lzo/zbud
[    0.523452] Key type ._fscrypt registered
[    0.523452] Key type .fscrypt registered
[    0.528712] Key type big_key registered
[    0.530873] Key type encrypted registered
[    0.530874] AppArmor: AppArmor sha1 policy hashing enabled
[    0.531663] integrity: Loading X.509 certificate: UEFI:db
[    0.532623] integrity: Loaded X.509 cert 'ASUSTeK MotherBoard SW Key Certificate: da83b990422ebc8c441f8d8b039a65a2'
[    0.532623] integrity: Loading X.509 certificate: UEFI:db
[    0.532787] integrity: Loaded X.509 cert 'ASUSTeK Notebook SW Key Certificate: b8e581e4df77a5bb4282d5ccfc00c071'
[    0.532787] integrity: Loading X.509 certificate: UEFI:db
[    0.532844] integrity: Loaded X.509 cert 'Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4'
[    0.532844] integrity: Loading X.509 certificate: UEFI:db
[    0.532912] integrity: Loaded X.509 cert 'Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53'
[    0.532913] integrity: Loading X.509 certificate: UEFI:db
[    0.533082] integrity: Loaded X.509 cert 'Canonical Ltd. Master Certificate Authority: ad91990bc22ab1f517048c23b6655a268e345a63'
[    0.536002] ima: No TPM chip found, activating TPM-bypass!
[    0.536031] ima: Allocated hash algorithm: sha1
[    0.536037] ima: No architecture policies found
[    0.536050] evm: Initialising EVM extended attributes:
[    0.536050] evm: security.selinux
[    0.536051] evm: security.SMACK64
[    0.536051] evm: security.SMACK64EXEC
[    0.536051] evm: security.SMACK64TRANSMUTE
[    0.536051] evm: security.SMACK64MMAP
[    0.536052] evm: security.apparmor
[    0.536052] evm: security.ima
[    0.536052] evm: security.capability
[    0.536052] evm: HMAC attrs: 0x1
[    0.536867] PM:   Magic number: 12:812:108
[    0.537018] rtc_cmos 00:02: setting system clock to 2020-07-19T03:08:24 UTC (1595128104)
[    0.537271] acpi_cpufreq: overriding BIOS provided _PSD data
[    0.538797] Freeing unused decrypted memory: 2040K
[    0.539253] Freeing unused kernel image memory: 2712K
[    0.552362] Write protecting the kernel read-only data: 22528k
[    0.552938] Freeing unused kernel image memory: 2008K
[    0.553196] Freeing unused kernel image memory: 1192K
[    0.561907] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    0.561910] Run /init as init process
[    0.630908] ACPI: Video Device [VGA] (multi-head: yes  rom: no  post: no)
[    0.631207] acpi device:02: registered as cooling_device8
[    0.631255] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:01/LNXVIDEO:00/input/input2
[    0.645302] acpi PNP0C14:01: duplicate WMI GUID 05901221-D566-11D1-B2F0-00A0C9062910 (first instance was on PNP0C14:00)
[    0.653011] ahci 0000:02:00.1: version 3.0
[    0.653270] ahci 0000:02:00.1: SSS flag set, parallel bus scan disabled
[    0.653365] ahci 0000:02:00.1: AHCI 0001.0301 32 slots 8 ports 6 Gbps 0x33 impl SATA mode
[    0.653368] ahci 0000:02:00.1: flags: 64bit ncq sntf stag pm led clo only pmp pio slum part sxs deso sadm sds apst 
[    0.654292] scsi host0: ahci
[    0.660499] scsi host1: ahci
[    0.662373] scsi host2: ahci
[    0.664534] scsi host3: ahci
[    0.664830] scsi host4: ahci
[    0.665397] scsi host5: ahci
[    0.665573] scsi host6: ahci
[    0.666686] libphy: r8169: probed
[    0.666987] r8169 0000:04:00.0 eth0: RTL8168h/8111h, a8:5e:45:5a:cc:9f, XID 541, IRQ 60
[    0.666989] r8169 0000:04:00.0 eth0: jumbo features [frames: 9200 bytes, tx checksumming: ko]
[    0.669372] scsi host7: ahci
[    0.669448] ata1: SATA max UDMA/133 abar m131072@0xfcd80000 port 0xfcd80100 irq 59
[    0.669451] ata2: SATA max UDMA/133 abar m131072@0xfcd80000 port 0xfcd80180 irq 59
[    0.669451] ata3: DUMMY
[    0.669452] ata4: DUMMY
[    0.669459] ata5: SATA max UDMA/133 abar m131072@0xfcd80000 port 0xfcd80300 irq 59
[    0.669461] ata6: SATA max UDMA/133 abar m131072@0xfcd80000 port 0xfcd80380 irq 59
[    0.669462] ata7: DUMMY
[    0.669462] ata8: DUMMY
[    0.669772] ahci 0000:0a:00.0: AHCI 0001.0301 32 slots 1 ports 6 Gbps 0x2 impl SATA mode
[    0.669775] ahci 0000:0a:00.0: flags: 64bit ncq sntf ilck pm led clo only pmp fbs pio slum part 
[    0.670111] scsi host8: ahci
[    0.670257] scsi host9: ahci
[    0.670369] ata9: DUMMY
[    0.670380] ata10: SATA max UDMA/133 abar m2048@0xfce00000 port 0xfce00180 irq 63
[    0.677112] piix4_smbus 0000:00:14.0: SMBus Host Controller at 0xb00, revision 0
[    0.677114] piix4_smbus 0000:00:14.0: Using register 0x02 for SMBus port selection
[    0.682210] AMD-Vi: AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    0.682286] cryptd: max_cpu_qlen set to 1000
[    0.688729] AVX2 version of gcm_enc/dec engaged.
[    0.688733] AES CTR mode by8 optimization enabled
[    0.728052] r8169 0000:04:00.0 enp4s0: renamed from eth0
[    0.743664] [drm] amdgpu kernel modesetting enabled.
[    0.743688] vga_switcheroo: detected switching method \_SB_.PCI0.GP17.VGA_.ATPX handle
[    0.743809] ATPX version 1, functions 0x00000000
[    0.743873] Parsing CRAT table with 1 nodes
[    0.743878] Creating topology SYSFS entries
[    0.743926] Topology: Add APU node [0x0:0x0]
[    0.743927] Finished initializing topology
[    0.744014] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xe0000000 -> 0xefffffff
[    0.744015] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xf0000000 -> 0xf01fffff
[    0.744016] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xfcf00000 -> 0xfcf3ffff
[    0.744018] checking generic (c0000000 7e9000) vs hw (e0000000 10000000)
[    0.744019] checking generic (c0000000 7e9000) vs hw (f0000000 200000)
[    0.744019] checking generic (c0000000 7e9000) vs hw (fcf00000 40000)
[    0.744051] amdgpu 0000:01:00.0: enabling device (0000 -> 0003)
[    0.744215] [drm] initializing kernel modesetting (POLARIS11 0x1002:0x67EF 0x1682:0x956D 0xE5).
[    0.744235] [drm] register mmio base: 0xFCF00000
[    0.744235] [drm] register mmio size: 262144
[    0.744251] [drm] add ip block number 0 <vi_common>
[    0.744252] [drm] add ip block number 1 <gmc_v8_0>
[    0.744253] [drm] add ip block number 2 <tonga_ih>
[    0.744253] [drm] add ip block number 3 <gfx_v8_0>
[    0.744254] [drm] add ip block number 4 <sdma_v3_0>
[    0.744255] [drm] add ip block number 5 <powerplay>
[    0.744255] [drm] add ip block number 6 <dm>
[    0.744256] [drm] add ip block number 7 <uvd_v6_0>
[    0.744257] [drm] add ip block number 8 <vce_v3_0>
[    0.821282] usb 1-7: new low-speed USB device number 2 using xhci_hcd
[    0.995065] ATOM BIOS: 113-P21_XL_170217_4G_D5_HM_1500_SF_W81
[    0.995087] [drm] UVD is enabled in VM mode
[    0.995088] [drm] UVD ENC is enabled in VM mode
[    0.995091] [drm] VCE enabled in VM mode
[    0.995103] [drm] GPU posting now...
[    1.081176] usb 1-7: New USB device found, idVendor=1bcf, idProduct=0880, bcdDevice= 0.52
[    1.081180] usb 1-7: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[    1.081182] usb 1-7: Product: USB Optical Mouse 
[    1.152295] ata1: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.153593] ata1.00: ATA-8: TOSHIBA HDWD130, MX6OACF0, max UDMA/133
[    1.153595] ata1.00: 5860533168 sectors, multi 16: LBA48 NCQ (depth 32), AA
[    1.154891] ata1.00: configured for UDMA/133
[    1.155123] scsi 0:0:0:0: Direct-Access     ATA      TOSHIBA HDWD130  ACF0 PQ: 0 ANSI: 5
[    1.155296] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    1.155378] sd 0:0:0:0: [sda] 5860533168 512-byte logical blocks: (3.00 TB/2.73 TiB)
[    1.155379] sd 0:0:0:0: [sda] 4096-byte physical blocks
[    1.155390] sd 0:0:0:0: [sda] Write Protect is off
[    1.155392] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
[    1.155408] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    1.156039] ata10: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.156374] ata10.00: supports DRM functions and may not be fully accessible
[    1.157224] ata10.00: ATA-11: Samsung SSD 860 EVO M.2 250GB, RVT21B6Q, max UDMA/133
[    1.157225] ata10.00: 488397168 sectors, multi 1: LBA48 NCQ (depth 32), AA
[    1.159592] ata10.00: supports DRM functions and may not be fully accessible
[    1.162359] ata10.00: configured for UDMA/133
[    1.189034] usb 2-3: new SuperSpeed Gen 1 USB device number 2 using xhci_hcd
[    1.213806] usb 2-3: New USB device found, idVendor=154b, idProduct=0095, bcdDevice=10.75
[    1.213808] usb 2-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.213809] usb 2-3: Product: USB 3.0 FD
[    1.213810] usb 2-3: Manufacturer: PNY Technologies
[    1.213811] usb 2-3: SerialNumber: 992838854
[    1.360399] usb-storage 2-3:1.0: USB Mass Storage device detected
[    1.360660] scsi host10: usb-storage 2-3:1.0
[    1.360799] usbcore: registered new interface driver usb-storage
[    1.362354] usbcore: registered new interface driver uas
[    1.408048] usb 1-10: new low-speed USB device number 3 using xhci_hcd
[    1.451301] tsc: Refined TSC clocksource calibration: 3593.233 MHz
[    1.451308] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x33cb5b25ea5, max_idle_ns: 440795305334 ns
[    1.451564] clocksource: Switched to clocksource tsc
[    1.468559] [drm] vm size is 64 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[    1.468609] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    1.468610] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    1.468622] [drm] Detected VRAM RAM=4096M, BAR=256M
[    1.468623] [drm] RAM width 128bits GDDR5
[    1.468684] [TTM] Zone  kernel: Available graphics memory: 7162624 KiB
[    1.468685] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
[    1.468685] [TTM] Initializing pool allocator
[    1.468688] [TTM] Initializing DMA pool allocator
[    1.468719] [drm] amdgpu: 4096M of VRAM memory ready
[    1.468722] [drm] amdgpu: 4096M of GTT memory ready.
[    1.468732] [drm] GART: num cpu pages 65536, num gpu pages 65536
[    1.472408] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[    1.472540] [drm] Chained IB support enabled!
[    1.473668] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[    1.473765] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[    1.474759] ata2: SATA link down (SStatus 0 SControl 300)
[    1.474860] [drm] Found VCE firmware Version: 53.26 Binary ID: 3
[    1.489101]  sda: sda1 sda2 sda3
[    1.489982] sd 0:0:0:0: [sda] Attached SCSI disk
[    1.565303] [drm] DM_PPLIB: values for Engine clock
[    1.565304] [drm] DM_PPLIB:	 214000
[    1.565304] [drm] DM_PPLIB:	 603000
[    1.565305] [drm] DM_PPLIB:	 958000
[    1.565305] [drm] DM_PPLIB:	 1060000
[    1.565305] [drm] DM_PPLIB:	 1076000
[    1.565305] [drm] DM_PPLIB:	 1116000
[    1.565306] [drm] DM_PPLIB:	 1156000
[    1.565306] [drm] DM_PPLIB:	 1196000
[    1.565306] [drm] DM_PPLIB: Validation clocks:
[    1.565306] [drm] DM_PPLIB:    engine_max_clock: 119600
[    1.565307] [drm] DM_PPLIB:    memory_max_clock: 150000
[    1.565307] [drm] DM_PPLIB:    level           : 8
[    1.565308] [drm] DM_PPLIB: values for Memory clock
[    1.565308] [drm] DM_PPLIB:	 300000
[    1.565308] [drm] DM_PPLIB:	 625000
[    1.565309] [drm] DM_PPLIB:	 1500000
[    1.565309] [drm] DM_PPLIB: Validation clocks:
[    1.565309] [drm] DM_PPLIB:    engine_max_clock: 119600
[    1.565309] [drm] DM_PPLIB:    memory_max_clock: 150000
[    1.565309] [drm] DM_PPLIB:    level           : 8
[    1.566388] [drm] Display Core initialized with v3.2.48!
[    1.567169] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.567169] [drm] Driver supports precise vblank timestamp query.
[    1.594116] [drm] UVD and UVD ENC initialized successfully.
[    1.669238] usb 1-10: New USB device found, idVendor=1a2c, idProduct=2d23, bcdDevice= 1.10
[    1.669240] usb 1-10: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.669241] usb 1-10: Product: USB Keyboard
[    1.669243] usb 1-10: Manufacturer: USB
[    1.683280] hidraw: raw HID events driver (C) Jiri Kosina
[    1.694072] [drm] VCE initialized successfully.
[    1.695461] kfd kfd: Allocated 3969056 bytes on gart
[    1.696210] Virtual CRAT table created for GPU
[    1.696211] Parsing CRAT table with 1 nodes
[    1.696215] Creating topology SYSFS entries
[    1.696283] Topology: Add dGPU node [0x67ef:0x1002]
[    1.696285] kfd kfd: added device 1002:67ef
[    1.696325] [drm] Cannot find any crtc or sizes
[    1.709899] [drm] Initialized amdgpu 3.35.0 20150101 for 0000:01:00.0 on minor 0
[    1.709933] amdgpu 0000:09:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xc0000000 -> 0xcfffffff
[    1.709935] amdgpu 0000:09:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xd0000000 -> 0xd01fffff
[    1.709936] amdgpu 0000:09:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xfcb00000 -> 0xfcb7ffff
[    1.709938] checking generic (c0000000 7e9000) vs hw (c0000000 10000000)
[    1.709938] fb0: switching to amdgpudrmfb from EFI VGA
[    1.710001] amdgpu 0000:09:00.0: vgaarb: deactivate vga console
[    1.710161] [drm] initializing kernel modesetting (RAVEN 0x1002:0x15DD 0x1043:0x876B 0xC6).
[    1.710170] [drm] register mmio base: 0xFCB00000
[    1.710170] [drm] register mmio size: 524288
[    1.710196] [drm] add ip block number 0 <soc15_common>
[    1.710196] [drm] add ip block number 1 <gmc_v9_0>
[    1.710197] [drm] add ip block number 2 <vega10_ih>
[    1.710198] [drm] add ip block number 3 <psp>
[    1.710199] [drm] add ip block number 4 <gfx_v9_0>
[    1.710200] [drm] add ip block number 5 <sdma_v4_0>
[    1.710200] [drm] add ip block number 6 <powerplay>
[    1.710201] [drm] add ip block number 7 <dm>
[    1.710202] [drm] add ip block number 8 <vcn_v1_0>
[    1.727164] usbcore: registered new interface driver usbhid
[    1.727165] usbhid: USB HID core driver
[    1.734563] [drm] BIOS signature incorrect 0 0
[    1.734585] ATOM BIOS: 113-PICASSO-115
[    1.734614] [drm] VCN decode is enabled in VM mode
[    1.734615] [drm] VCN encode is enabled in VM mode
[    1.734615] [drm] VCN jpeg decode is enabled in VM mode
[    1.734619] vga_switcheroo: enabled
[    1.734643] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[    1.734649] amdgpu 0000:09:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
[    1.734650] amdgpu 0000:09:00.0: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    1.734651] amdgpu 0000:09:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[    1.734653] [drm] Detected VRAM RAM=2048M, BAR=2048M
[    1.734654] [drm] RAM width 64bits DDR4
[    1.734670] [drm] amdgpu: 2048M of VRAM memory ready
[    1.734672] [drm] amdgpu: 3072M of GTT memory ready.
[    1.734681] [drm] GART: num cpu pages 262144, num gpu pages 262144
[    1.734810] [drm] PCIE GART of 1024M enabled (table at 0x000000F400900000).
[    1.736068] [drm] use_doorbell being set to: [true]
[    1.736132] amdgpu: [powerplay] hwmgr_sw_init smu backed is smu10_smu
[    1.736226] [drm] Found VCN firmware Version ENC: 1.9 DEC: 1 VEP: 0 Revision: 28
[    1.736228] [drm] PSP loading VCN firmware
[    1.756961] [drm] reserve 0x400000 from 0xf47f800000 for PSP TMR
[    1.763636] input: USB Optical Mouse  Keyboard as /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-7/1-7:1.0/0003:1BCF:0880.0001/input/input3
[    1.790692] ata5: SATA link down (SStatus 0 SControl 330)
[    1.820109] input: USB Optical Mouse  Mouse as /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-7/1-7:1.0/0003:1BCF:0880.0001/input/input4
[    1.820181] hid-generic 0003:1BCF:0880.0001: input,hidraw0: USB HID v1.10 Keyboard [USB Optical Mouse ] on usb-0000:02:00.0-7/input0
[    1.820327] input: USB USB Keyboard as /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-10/1-10:1.0/0003:1A2C:2D23.0002/input/input5
[    1.880160] hid-generic 0003:1A2C:2D23.0002: input,hidraw1: USB HID v1.10 Keyboard [USB USB Keyboard] on usb-0000:02:00.0-10/input0
[    1.880479] input: USB USB Keyboard Consumer Control as /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-10/1-10:1.1/0003:1A2C:2D23.0003/input/input6
[    1.941409] input: USB USB Keyboard System Control as /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-10/1-10:1.1/0003:1A2C:2D23.0003/input/input7
[    1.941513] hid-generic 0003:1A2C:2D23.0003: input,hidraw2: USB HID v1.10 Device [USB USB Keyboard] on usb-0000:02:00.0-10/input1
[    1.970744] [drm] DM_PPLIB: values for F clock
[    1.970746] [drm] DM_PPLIB:	 400000 in kHz, 3649 in mV
[    1.970746] [drm] DM_PPLIB:	 933000 in kHz, 4074 in mV
[    1.970746] [drm] DM_PPLIB:	 1067000 in kHz, 4250 in mV
[    1.970747] [drm] DM_PPLIB: values for DCF clock
[    1.970748] [drm] DM_PPLIB:	 300000 in kHz, 3649 in mV
[    1.970748] [drm] DM_PPLIB:	 600000 in kHz, 4074 in mV
[    1.970749] [drm] DM_PPLIB:	 626000 in kHz, 4250 in mV
[    1.970749] [drm] DM_PPLIB:	 654000 in kHz, 4399 in mV
[    1.974606] [drm] Display Core initialized with v3.2.48!
[    1.999879] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    1.999880] [drm] Driver supports precise vblank timestamp query.
[    2.011956] [drm] VCN decode and encode initialized successfully(under SPG Mode).
[    2.012789] kfd kfd: Allocated 3969056 bytes on gart
[    2.013017] Topology: Add dGPU node [0x67ef:0x1002]
[    2.013019] kfd kfd: added device 1002:15dd
[    2.014334] [drm] fb mappable at 0x40BC1000
[    2.014335] [drm] vram apper at 0x40000000
[    2.014335] [drm] size 8294400
[    2.014336] [drm] fb depth is 24
[    2.014336] [drm]    pitch is 7680
[    2.014393] fbcon: amdgpudrmfb (fb0) is primary device
[    2.014394] fbcon: Deferring console take-over
[    2.014396] amdgpu 0000:09:00.0: fb0: amdgpudrmfb frame buffer device
[    2.032069] amdgpu 0000:09:00.0: ring gfx uses VM inv eng 0 on hub 0
[    2.032071] amdgpu 0000:09:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    2.032072] amdgpu 0000:09:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    2.032073] amdgpu 0000:09:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    2.032074] amdgpu 0000:09:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    2.032075] amdgpu 0000:09:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    2.032076] amdgpu 0000:09:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    2.032077] amdgpu 0000:09:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    2.032078] amdgpu 0000:09:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    2.032079] amdgpu 0000:09:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    2.032079] amdgpu 0000:09:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[    2.032080] amdgpu 0000:09:00.0: ring vcn_dec uses VM inv eng 1 on hub 1
[    2.032081] amdgpu 0000:09:00.0: ring vcn_enc0 uses VM inv eng 4 on hub 1
[    2.032082] amdgpu 0000:09:00.0: ring vcn_enc1 uses VM inv eng 5 on hub 1
[    2.032083] amdgpu 0000:09:00.0: ring vcn_jpeg uses VM inv eng 6 on hub 1
[    2.048631] [drm] Initialized amdgpu 3.35.0 20150101 for 0000:09:00.0 on minor 1
[    2.106704] ata6: SATA link down (SStatus 0 SControl 330)
[    2.106973] scsi 9:0:0:0: Direct-Access     ATA      Samsung SSD 860  1B6Q PQ: 0 ANSI: 5
[    2.107185] ata10.00: Enabling discard_zeroes_data
[    2.107196] sd 9:0:0:0: Attached scsi generic sg1 type 0
[    2.107281] sd 9:0:0:0: [sdb] 488397168 512-byte logical blocks: (250 GB/233 GiB)
[    2.107294] sd 9:0:0:0: [sdb] Write Protect is off
[    2.107298] sd 9:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    2.107320] sd 9:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.120380] ata10.00: Enabling discard_zeroes_data
[    2.123141] ata10.00: Enabling discard_zeroes_data
[    2.124267] sd 9:0:0:0: [sdb] supports TCG Opal
[    2.124269] sd 9:0:0:0: [sdb] Attached SCSI disk
[    2.352839] bcache: bch_journal_replay() journal replay done, 2164 keys in 68 entries, seq 7202744
[    2.352925] bcache: register_cache() registered cache device sdb
[    2.397744] bcache: register_bdev() registered backing device sda3
[    2.444100] bcache: bch_cached_dev_attach() Caching sda3 as bcache0 on set 21d7ffda-1db2-4847-86c7-9ca8b3a79691
[   15.183149] EXT4-fs (dm-1): mounted filesystem with ordered data mode. Opts: (null)
[   15.324874] systemd[1]: Inserted module 'autofs4'
[   15.389301] systemd[1]: systemd 245.4-4ubuntu3.1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=hybrid)
[   15.408056] systemd[1]: Detected architecture x86-64.
[   15.430780] systemd[1]: Set hostname to <thorshammer>.
[   15.530442] systemd[1]: /lib/systemd/system/dbus.socket:5: ListenStream= references a path below legacy directory /var/run/, updating /var/run/dbus/system_bus_socket → /run/dbus/system_bus_socket; please update the unit file accordingly.
[   15.572721] systemd[1]: /lib/systemd/system/docker.socket:6: ListenStream= references a path below legacy directory /var/run/, updating /var/run/docker.sock → /run/docker.sock; please update the unit file accordingly.
[   15.598388] systemd[1]: Created slice Virtual Machine and Container Slice.
[   15.598875] systemd[1]: Created slice system-modprobe.slice.
[   15.599181] systemd[1]: Created slice Cryptsetup Units Slice.
[   15.599481] systemd[1]: Created slice system-systemd\x2dfsck.slice.
[   15.599740] systemd[1]: Created slice User and Session Slice.
[   15.599808] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[   15.600164] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
[   15.600237] systemd[1]: Reached target User and Group Name Lookups.
[   15.600270] systemd[1]: Reached target Remote File Systems.
[   15.600302] systemd[1]: Reached target Slices.
[   15.600343] systemd[1]: Reached target Libvirt guests shutdown.
[   15.600423] systemd[1]: Listening on Device-mapper event daemon FIFOs.
[   15.600545] systemd[1]: Listening on LVM2 poll daemon socket.
[   15.600637] systemd[1]: Listening on Syslog Socket.
[   15.600711] systemd[1]: Listening on fsck to fsckd communication Socket.
[   15.600768] systemd[1]: Listening on initctl Compatibility Named Pipe.
[   15.600922] systemd[1]: Listening on Journal Audit Socket.
[   15.600993] systemd[1]: Listening on Journal Socket (/dev/log).
[   15.601077] systemd[1]: Listening on Journal Socket.
[   15.601160] systemd[1]: Listening on udev Control Socket.
[   15.601230] systemd[1]: Listening on udev Kernel Socket.
[   15.602009] systemd[1]: Mounting Huge Pages File System...
[   15.602801] systemd[1]: Mounting POSIX Message Queue File System...
[   15.603805] systemd[1]: Mounting Kernel Debug File System...
[   15.605098] systemd[1]: Mounting Kernel Trace File System...
[   15.606499] systemd[1]: Starting Journal Service...
[   15.607545] systemd[1]: Starting Availability of block devices...
[   15.608715] systemd[1]: Starting Set the console keyboard layout...
[   15.609670] systemd[1]: Starting Create list of static device nodes for the current kernel...
[   15.610711] systemd[1]: Starting Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling...
[   15.610753] systemd[1]: Condition check resulted in Load Kernel Module drm being skipped.
[   15.611295] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
[   15.611326] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
[   15.613789] systemd[1]: Starting Load Kernel Modules...
[   15.614894] systemd[1]: Starting Remount Root and Kernel File Systems...
[   15.616361] systemd[1]: Starting udev Coldplug all Devices...
[   15.617676] systemd[1]: Starting Uncomplicated firewall...
[   15.619859] systemd[1]: Mounted Huge Pages File System.
[   15.620199] systemd[1]: Mounted POSIX Message Queue File System.
[   15.620343] systemd[1]: Mounted Kernel Debug File System.
[   15.620455] systemd[1]: Mounted Kernel Trace File System.
[   15.621279] systemd[1]: Finished Availability of block devices.
[   15.623529] systemd[1]: Finished Create list of static device nodes for the current kernel.
[   15.624506] systemd[1]: Finished Uncomplicated firewall.
[   15.629080] EXT4-fs (dm-1): re-mounted. Opts: errors=remount-ro
[   15.630702] systemd[1]: Finished Remount Root and Kernel File Systems.
[   15.631255] systemd[1]: Condition check resulted in Rebuild Hardware Database being skipped.
[   15.631286] systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
[   15.632636] systemd[1]: Starting Load/Save Random Seed...
[   15.633927] systemd[1]: Starting Create System Users...
[   15.637109] lp: driver loaded but no devices found
[   15.644775] ppdev: user-space parallel port driver
[   15.650408] systemd[1]: Finished Load Kernel Modules.
[   15.651470] systemd[1]: Mounting FUSE Control File System...
[   15.652775] systemd[1]: Mounting Kernel Configuration File System...
[   15.653799] systemd[1]: Starting Apply Kernel Variables...
[   15.654413] systemd[1]: Finished Load/Save Random Seed.
[   15.655438] systemd[1]: Mounted FUSE Control File System.
[   15.656107] systemd[1]: Mounted Kernel Configuration File System.
[   15.657626] systemd[1]: Finished Create System Users.
[   15.658922] systemd[1]: Starting Create Static Device Nodes in /dev...
[   15.668896] systemd[1]: Finished Apply Kernel Variables.
[   15.673392] systemd[1]: Finished Create Static Device Nodes in /dev.
[   15.674728] systemd[1]: Starting udev Kernel Device Manager...
[   15.693175] systemd[1]: Finished Set the console keyboard layout.
[   15.718153] systemd[1]: Finished udev Coldplug all Devices.
[   15.729822] systemd[1]: Finished Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling.
[   15.730003] systemd[1]: Reached target Local File Systems (Pre).
[   15.733550] systemd[1]: Mounting Mount unit for core18, revision 1754...
[   15.734849] systemd[1]: Mounting Mount unit for core18, revision 1880...
[   15.736874] systemd[1]: Mounting Mount unit for gnome-3-28-1804, revision 128...
[   15.739950] systemd[1]: Mounting Mount unit for gnome-3-34-1804, revision 33...
[   15.741940] systemd[1]: Mounting Mount unit for gnome-3-34-1804, revision 36...
[   15.744066] systemd[1]: Mounting Mount unit for gtk-common-themes, revision 1506...
[   15.745644] systemd[1]: Mounting Mount unit for snap-store, revision 415...
[   15.747266] systemd[1]: Mounting Mount unit for snap-store, revision 467...
[   15.748867] systemd[1]: Mounting Mount unit for snapd, revision 8140...
[   15.750875] systemd[1]: Mounting Mount unit for snapd, revision 8542...
[   15.750916] systemd[1]: Condition check resulted in Virtual Machine and Container Storage (Compatibility) being skipped.
[   15.750990] systemd[1]: Reached target Containers.
[   15.753674] systemd[1]: Started udev Kernel Device Manager.
[   15.755112] systemd[1]: Starting Show Plymouth Boot Screen...
[   15.778505] systemd[1]: plymouth-start.service: Succeeded.
[   15.779076] systemd[1]: Started Show Plymouth Boot Screen.
[   15.779241] systemd[1]: Condition check resulted in Dispatch Password Requests to Console Directory Watch being skipped.
[   15.779387] systemd[1]: Started Forward Password Requests to Plymouth Directory Watch.
[   15.864615] systemd[1]: Mounted Mount unit for core18, revision 1754.
[   15.864825] systemd[1]: Mounted Mount unit for gnome-3-34-1804, revision 33.
[   15.884730] systemd[1]: Mounted Mount unit for gnome-3-28-1804, revision 128.
[   15.933536] systemd[1]: Mounted Mount unit for gnome-3-34-1804, revision 36.
[   15.972908] systemd[1]: Created slice system-systemd\x2dbacklight.slice.
[   15.974122] systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:acpi_video0...
[   15.976898] systemd[1]: Mounted Mount unit for gtk-common-themes, revision 1506.
[   15.984774] systemd[1]: Finished Load/Save Screen Backlight Brightness of backlight:acpi_video0.
[   16.032857] systemd[1]: Mounted Mount unit for core18, revision 1880.
[   16.033108] systemd[1]: Mounted Mount unit for snapd, revision 8542.
[   16.061085] systemd[1]: Mounted Mount unit for snap-store, revision 467.
[   16.080797] systemd[1]: Started Journal Service.
[   16.094649] asus_wmi: ASUS WMI generic driver loaded
[   16.096638] asus_wmi: Initialization: 0x0
[   16.096681] asus_wmi: BIOS WMI version: 0.9
[   16.096885] asus_wmi: SFUN value: 0x0
[   16.096888] eeepc-wmi eeepc-wmi: Detected ASUSWMI, use DCTS
[   16.097516] input: Eee PC WMI hotkeys as /devices/platform/eeepc-wmi/input/input8
[   16.111456] systemd-journald[577]: Received client request to flush runtime journal.
[   16.165695] kvm: Nested Virtualization enabled
[   16.165740] kvm: Nested Paging enabled
[   16.165741] SVM: Virtual VMLOAD VMSAVE supported
[   16.165741] SVM: Virtual GIF supported
[   16.169660] MCE: In-kernel MCE decoding enabled.
[   16.171719] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.171721] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.244769] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.244771] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.256650] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
[   16.256653] snd_hda_intel 0000:01:00.1: Force to non-snoop mode
[   16.257051] snd_hda_intel 0000:09:00.1: Handle vga_switcheroo audio client
[   16.265630] snd_hda_intel 0000:01:00.1: bound 0000:01:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[   16.270840] snd_hda_intel 0000:09:00.1: bound 0000:09:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[   16.271572] input: HD-Audio Generic HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:08.1/0000:09:00.1/sound/card1/input14
[   16.271931] input: HDA ATI HDMI HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.1/0000:01:00.1/sound/card0/input9
[   16.272000] input: HDA ATI HDMI HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.1/0000:01:00.1/sound/card0/input10
[   16.272775] input: HDA ATI HDMI HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.1/0000:01:00.1/sound/card0/input11
[   16.272841] input: HDA ATI HDMI HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.1/0000:01:00.1/sound/card0/input12
[   16.272892] input: HDA ATI HDMI HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.1/0000:01:00.1/sound/card0/input13
[   16.332564] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.332566] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.334125] snd_hda_codec_realtek hdaudioC2D0: autoconfig for ALC887-VD: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:line
[   16.334129] snd_hda_codec_realtek hdaudioC2D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
[   16.334131] snd_hda_codec_realtek hdaudioC2D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
[   16.334132] snd_hda_codec_realtek hdaudioC2D0:    mono: mono_out=0x0
[   16.334133] snd_hda_codec_realtek hdaudioC2D0:    dig-out=0x11/0x0
[   16.334134] snd_hda_codec_realtek hdaudioC2D0:    inputs:
[   16.334136] snd_hda_codec_realtek hdaudioC2D0:      Front Mic=0x19
[   16.334137] snd_hda_codec_realtek hdaudioC2D0:      Rear Mic=0x18
[   16.334139] snd_hda_codec_realtek hdaudioC2D0:      Line=0x1a
[   16.351447] input: HD-Audio Generic Front Mic as /devices/pci0000:00/0000:00:08.1/0000:09:00.6/sound/card2/input15
[   16.351507] input: HD-Audio Generic Rear Mic as /devices/pci0000:00/0000:00:08.1/0000:09:00.6/sound/card2/input16
[   16.351559] input: HD-Audio Generic Line as /devices/pci0000:00/0000:00:08.1/0000:09:00.6/sound/card2/input17
[   16.351618] input: HD-Audio Generic Line Out as /devices/pci0000:00/0000:00:08.1/0000:09:00.6/sound/card2/input18
[   16.351692] input: HD-Audio Generic Front Headphone as /devices/pci0000:00/0000:00:08.1/0000:09:00.6/sound/card2/input19
[   16.417657] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.417660] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.504661] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.504663] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.592511] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.592513] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.668588] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.668591] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.710300] bcache: register_bcache() error : device already registered
[   16.768595] EDAC amd64: Node 0: DRAM ECC disabled.
[   16.768597] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
                Either enable ECC checking or force module loading by setting 'ecc_enable_override'.
                (Note that use of the override may cause unknown side effects.)
[   16.780094] Adding 1048572k swap on /dev/mapper/thorshamma--vg-swap.  Priority:-2 extents:1 across:1048572k SSFS
[   16.832108] EXT4-fs (dm-2): mounted filesystem with ordered data mode. Opts: (null)
[   17.075727] bcache: register_bcache() error : device already registered (emitting change event)
[   17.227517] EXT4-fs (sda2): mounted filesystem with ordered data mode. Opts: (null)
[   17.296240] audit: type=1400 audit(1595128121.254:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-xpdfimport" pid=1322 comm="apparmor_parser"
[   17.296490] audit: type=1400 audit(1595128121.258:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-senddoc" pid=1326 comm="apparmor_parser"
[   17.301543] audit: type=1400 audit(1595128121.262:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oopslash" pid=1319 comm="apparmor_parser"
[   17.302937] audit: type=1400 audit(1595128121.262:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="virt-aa-helper" pid=1317 comm="apparmor_parser"
[   17.305137] audit: type=1400 audit(1595128121.266:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=1320 comm="apparmor_parser"
[   17.306110] audit: type=1400 audit(1595128121.266:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="lsb_release" pid=1321 comm="apparmor_parser"
[   17.308070] audit: type=1400 audit(1595128121.270:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=1323 comm="apparmor_parser"
[   17.308074] audit: type=1400 audit(1595128121.270:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=1323 comm="apparmor_parser"
[   17.308077] audit: type=1400 audit(1595128121.270:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=1323 comm="apparmor_parser"
[   17.308080] audit: type=1400 audit(1595128121.270:11): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/{,usr/}sbin/dhclient" pid=1323 comm="apparmor_parser"
[   18.366830] aufs 5.4.3-20200302
[   18.490140] Generic FE-GE Realtek PHY r8169-400:00: attached PHY driver [Generic FE-GE Realtek PHY] (mii_bus:phy_addr=r8169-400:00, irq=IGNORE)
[   18.601210] r8169 0000:04:00.0 enp4s0: Link is Down
[   18.682906] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[   18.683867] virbr0: port 1(virbr0-nic) entered blocking state
[   18.683869] virbr0: port 1(virbr0-nic) entered disabled state
[   18.683933] device virbr0-nic entered promiscuous mode
[   18.696947] Started bpfilter
[   18.696955] bpfilter: Loaded bpfilter_umh pid 1874
[   18.866573] virbr0: port 1(virbr0-nic) entered blocking state
[   18.866575] virbr0: port 1(virbr0-nic) entered listening state
[   18.894003] virbr0: port 1(virbr0-nic) entered disabled state
[   21.904575] r8169 0000:04:00.0 enp4s0: Link is Up - 1Gbps/Full - flow control rx/tx
[   21.904593] IPv6: ADDRCONF(NETDEV_CHANGE): enp4s0: link becomes ready
[   24.604464] kauditd_printk_skb: 28 callbacks suppressed
[   24.604466] audit: type=1400 audit(1595128128.566:40): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=3471 comm="apparmor_parser"
[   24.760236] Bridge firewalling registered
[   24.806854] Initializing XFRM netlink socket
[   26.004852] rfkill: input handler disabled
[   30.190056] rfkill: input handler enabled
[   32.566403] rfkill: input handler disabled
[  282.986062] Failure to set tba address. error -1.

 </details>

---

### 评论 #10 — kentrussell (2020-07-20T12:07:55Z)

@fxkamd Is this similar to something else you were discussing in the ROCK Bug Report with a similar issue regarding the BIOS not configuring the CRAT correctly? I have a vague recollection of you mentioning something along those lines, but can't seem to find the notifications in my inbox and Outlook didn't find anything either.

---

### 评论 #11 — ROCmSupport (2021-04-19T12:55:48Z)

Hi @dundir 
Thanks for reaching out.
Can you please check and share the latest status on ROCm 4.1
Thank you.

---

### 评论 #12 — dundir (2021-04-20T17:48:13Z)

Thank you for the update.

It may be about a week before I can test this as the system is currently running a series of batches on Nvidia hardware. I'll provide an update once I have had a chance to replace the AMD hardware and run the tests on the latest version. I'll reach out once I have an update.

---

### 评论 #13 — nartmada (2023-12-14T03:31:17Z)

Hi @dundir, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #14 — dundir (2023-12-15T02:15:17Z)

Hi Adam,

Unfortunately, I no longer have the mainboard that had this issue.
The Asus B450 Prime Plus with built-in APU (on CPU), failed earlier this
year from a bad PSU unit.

Should I leave this issue open in the meantime, in the case that someone
that has this board can test and verify if the issue persists?
As these issues were largely related to poor implementation by ASUS
regarding PCIe Atomics, I don't see how software would resolve this, but
this isn't my area of expertise.

Best Regards,
dundir

On Wed, Dec 13, 2023 at 7:31 PM Adam Tran ***@***.***> wrote:

> Hi @dundir <https://github.com/dundir>, please check latest ROCm
> Documentation and ROCm 5.7.1 to see if your query has been resolved. If
> resolved, please close the ticket. Thanks.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/ROCm/ROCm/issues/1013#issuecomment-1855071143>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AASY2BLEPG2Y6L3VD3BYVY3YJJXJDAVCNFSM4KVXXMZ2U5DIOJSWCZC7NNSXTN2JONZXKZKDN5WW2ZLOOQ5TCOBVGUYDOMJRGQZQ>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


---

### 评论 #15 — nartmada (2023-12-15T02:59:46Z)

Hi @dundir, 

Thank you for your response.  Let's close the ticket as it has been opened for more than 3 yrs.

If another community member runs into the same failure again on ASUS Prime B450-Plus, they can file a new ticket for investigation.

Thanks for your support,
Adam


---
