# ROCm on Bristol Ridge + ASUS prime X370-pro ?

> **Issue #121**
> **状态**: closed
> **创建时间**: 2017-05-15T12:44:03Z
> **更新时间**: 2017-08-30T22:35:40Z
> **关闭时间**: 2017-07-02T17:45:04Z
> **作者**: oheid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/121

## 描述

Is there any experience with runing ROCm-1.5.x on Bristol Ridge (A12-9800) + ASUS Prime X370-Pro? I use Fedora 25. The ROCK 4.9.0 kernel seems to have a problem with this hardware setup: Lightdm login manager or X launched from text console via startx hangs the machine after one or two seconds.
The ROCR example/test program crashes with
```
./vector_copy 
Profiling of privileged counters is not available
Profiling is not available
CPU Node [1] has no GPU connected
vector_copy: /home/heid/sonst/ROCR-Runtime/src/core/runtime/amd_topology.cpp:178: void amd::BuildTopology(): Assertion `!(cpu == NULL && gpu == NULL)' failed.
```
Is there any way to fix that?
I use kernel parameters "amd_iommu=on iommu=pt" - is this advisable?

The relevant kernel modules seem to be there
```
lsmod | grep amd -i
amdkfd                219075  1
amd_iommu_v2            8347  1 amdkfd
amdgpu               1441978  1
edac_mce_amd           19427  0
ttm                    87495  1 amdgpu
drm_kms_helper        139401  1 amdgpu
drm                   327504  4 amdgpu,ttm,drm_kms_helper
i2c_algo_bit            6079  2 igb,amdgpu
```
and IOMMUv2 is present:
```Hi,
dmesg | grep iommu -i
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.9.0 root=UUID=401c6f91-f069-42b4-856e-1f24b13edda3 ro amd_iommu=on iommu=pt
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.9.0 root=UUID=401c6f91-f069-42b4-856e-1f24b13edda3 ro amd_iommu=on iommu=pt
[    0.964991] AMD-Vi: IOMMU performance counters supported
[    0.965918] iommu: Adding device 0000:00:01.0 to group 0
[    0.966108] iommu: Using direct mapping for device 0000:00:01.0
[    0.966244] iommu: Adding device 0000:00:01.1 to group 0
[    0.966420] iommu: Adding device 0000:00:02.0 to group 1
[    0.966555] iommu: Using direct mapping for device 0000:00:02.0
[    0.966676] iommu: Adding device 0000:00:02.4 to group 1
[    0.966800] iommu: Adding device 0000:00:02.5 to group 1
[    0.966964] iommu: Adding device 0000:00:03.0 to group 2
[    0.967082] iommu: Using direct mapping for device 0000:00:03.0
[    0.967220] iommu: Adding device 0000:00:08.0 to group 3
[    0.967337] iommu: Using direct mapping for device 0000:00:08.0
[    0.967481] iommu: Adding device 0000:00:09.0 to group 4
[    0.967597] iommu: Using direct mapping for device 0000:00:09.0
[    0.967699] iommu: Adding device 0000:00:09.2 to group 4
[    0.967844] iommu: Adding device 0000:00:10.0 to group 5
[    0.967960] iommu: Using direct mapping for device 0000:00:10.0
[    0.968113] iommu: Adding device 0000:00:11.0 to group 6
[    0.968247] iommu: Using direct mapping for device 0000:00:11.0
[    0.968408] iommu: Adding device 0000:00:14.0 to group 7
[    0.968540] iommu: Using direct mapping for device 0000:00:14.0
[    0.968658] iommu: Adding device 0000:00:14.3 to group 7
[    0.968856] iommu: Adding device 0000:00:18.0 to group 8
[    0.968997] iommu: Using direct mapping for device 0000:00:18.0
[    0.969110] iommu: Adding device 0000:00:18.1 to group 8
[    0.969211] iommu: Adding device 0000:00:18.2 to group 8
[    0.969313] iommu: Adding device 0000:00:18.3 to group 8
[    0.969413] iommu: Adding device 0000:00:18.4 to group 8
[    0.969512] iommu: Adding device 0000:00:18.5 to group 8
[    0.969610] iommu: Adding device 0000:05:00.0 to group 1
[    0.969705] iommu: Adding device 0000:05:00.1 to group 1
[    0.969807] iommu: Adding device 0000:05:00.2 to group 1
[    0.969905] iommu: Adding device 0000:1d:00.0 to group 1
[    0.970014] iommu: Adding device 0000:1d:02.0 to group 1
[    0.970128] iommu: Adding device 0000:1d:03.0 to group 1
[    0.970244] iommu: Adding device 0000:1d:04.0 to group 1
[    0.970358] iommu: Adding device 0000:1d:06.0 to group 1
[    0.970472] iommu: Adding device 0000:1d:07.0 to group 1
[    0.970592] iommu: Adding device 0000:25:00.0 to group 1
[    0.970713] iommu: Adding device 0000:26:00.0 to group 1
[    0.970834] iommu: Adding device 0000:28:00.0 to group 1
[    0.971461] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    0.974898] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)
[    6.102064] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
```


---

## 评论 (5 条)

### 评论 #1 — oheid (2017-05-15T13:16:16Z)

The GPU seems to be detected:
```
cat /sys/class/kfd/kfd/topology/nodes/0/properties
cpu_cores_count 4
simd_count 32
mem_banks_count 0
caches_count 8
io_links_count 0
cpu_core_id_base 16
simd_id_base 2147483648
max_waves_per_simd 10
lds_size_in_kb 64
gds_size_in_kb 0
wave_front_size 64
array_count 1
simd_arrays_per_engine 1
cu_per_simd_array 10
simd_per_cu 4
max_slots_scratch_cu 32
vendor_id 4098
device_id 39028
location_id 8
max_engine_clk_fcompute 1107
local_mem_size 0
fw_version 705
capability 4738
max_engine_clk_ccompute 3800
```
and dmesg gives
```

[    6.282137] Parsing CRAT table with 2 nodes
[    6.282258] Creating topology SYSFS entries
[    6.282446] Finished initializing topology
[    6.286468] kfd kfd: Initialized module
[    6.287474] [drm] initializing kernel modesetting (CARRIZO 0x1002:0x9874 0x1043:0x8719 0xE1).
[    6.287702] [drm] register mmio base: 0xFE900000
[    6.287811] [drm] register mmio size: 262144
[    6.288099] [drm] UVD is enabled in physical mode
[    6.288208] [drm] VCE enabled in physical mode
[    6.303142] [drm] BIOS signature incorrect 5b 7
[    6.303320] ATOM BIOS: 109-C95010-003
[    6.303422] [drm] GPU post is not needed
[    6.303896] amdgpu 0000:00:01.0: VRAM: 512M 0x0000000000000000 - 0x000000001FFFFFFF (512M used)
[    6.304072] amdgpu 0000:00:01.0: GTT: 32768M 0x0000000020000000 - 0x000000081FFFFFFF
[    6.304250] [drm] Detected VRAM RAM=512M, BAR=512M
[    6.304354] [drm] RAM width 64bits UNKNOWN
[    6.304849] [TTM] Zone  kernel: Available graphics memory: 14857282 kiB
[    6.304949] [TTM] Initializing pool allocator
[    6.305043] [TTM] Initializing DMA pool allocator
[    6.305164] [drm] amdgpu: 512M of VRAM memory ready
[    6.305254] [drm] amdgpu: 32768M of GTT memory ready.
[    6.305381] [drm] GART: num cpu pages 8388608, num gpu pages 8388608
[    6.306812] [drm] PCIE GART of 32768M enabled (table at 0x0000000000040000).
[    6.307012] amdgpu 0000:00:01.0: amdgpu: using MSI.
[    6.307101] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    6.307191] [drm] Driver supports precise vblank timestamp query.
[    6.307307] [drm] amdgpu: irq initialized.
[    6.307418] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    6.308072] [drm] AMDGPU Display Connectors
[    6.308174] [drm] Connector 0:
[    6.308268] [drm]   DP-1
[    6.308355] [drm]   HPD1
[    6.308443] [drm]   DDC: 0x4868 0x4868 0x4869 0x4869 0x486a 0x486a 0x486b 0x486b
[    6.308583] [drm]   Encoders:
[    6.308670] [drm]     DFP1: INTERNAL_UNIPHY
[    6.308775] [drm] Connector 1:
[    6.308870] [drm]   HDMI-A-1
[    6.308956] [drm]   HPD2
[    6.311837] [drm]   DDC: 0x486c 0x486c 0x486d 0x486d 0x486e 0x486e 0x486f 0x486f
[    6.311952] [drm]   Encoders:
[    6.312023] [drm]     DFP2: INTERNAL_UNIPHY
[    6.317216] amdgpu 0000:00:01.0: fence driver on ring 0 use gpu addr 0x0000000020000010, cpu addr 0xffff9b2a5972b010
[    6.317646] amdgpu 0000:00:01.0: fence driver on ring 1 use gpu addr 0x0000000020000020, cpu addr 0xffff9b2a5972b020
[    6.317863] amdgpu 0000:00:01.0: fence driver on ring 2 use gpu addr 0x0000000020000030, cpu addr 0xffff9b2a5972b030
[    6.318056] amdgpu 0000:00:01.0: fence driver on ring 3 use gpu addr 0x0000000020000040, cpu addr 0xffff9b2a5972b040
[    6.318242] amdgpu 0000:00:01.0: fence driver on ring 4 use gpu addr 0x0000000020000050, cpu addr 0xffff9b2a5972b050
[    6.318433] amdgpu 0000:00:01.0: fence driver on ring 5 use gpu addr 0x0000000020000060, cpu addr 0xffff9b2a5972b060
[    6.318656] amdgpu 0000:00:01.0: fence driver on ring 6 use gpu addr 0x0000000020000070, cpu addr 0xffff9b2a5972b070
[    6.318892] amdgpu 0000:00:01.0: fence driver on ring 7 use gpu addr 0x0000000020000080, cpu addr 0xffff9b2a5972b080
[    6.319197] amdgpu 0000:00:01.0: fence driver on ring 8 use gpu addr 0x0000000020000090, cpu addr 0xffff9b2a5972b090
[    6.319375] amdgpu 0000:00:01.0: fence driver on ring 9 use gpu addr 0x00000000200000a4, cpu addr 0xffff9b2a5972b0a4
[    6.319988] amdgpu 0000:00:01.0: fence driver on ring 10 use gpu addr 0x00000000200000b4, cpu addr 0xffff9b2a5972b0b4
[    6.320195] amdgpu 0000:00:01.0: fence driver on ring 11 use gpu addr 0x00000000200000c4, cpu addr 0xffff9b2a5972b0c4
[    6.321057] [drm] Found UVD firmware Version: 1.87 Family ID: 11
[    6.322100] amdgpu 0000:00:01.0: fence driver on ring 12 use gpu addr 0x00000000040946e0, cpu addr 0xffffa9ae49c416e0
[    6.322804] [drm] Found VCE firmware Version: 52.4 Binary ID: 3
[    6.323038] amdgpu 0000:00:01.0: fence driver on ring 13 use gpu addr 0x00000000200000e4, cpu addr 0xffff9b2a5972b0e4
[    6.323245] amdgpu 0000:00:01.0: fence driver on ring 14 use gpu addr 0x00000000200000f4, cpu addr 0xffff9b2a5972b0f4
[    6.329877] [drm] ring test on 0 succeeded in 8 usecs
[    6.330098] [drm] ring test on 9 succeeded in 6 usecs
[    6.330253] [drm] ring test on 1 succeeded in 5 usecs
[    6.330401] [drm] ring test on 2 succeeded in 2 usecs
[    6.330530] [drm] ring test on 3 succeeded in 1 usecs
[    6.330659] [drm] ring test on 4 succeeded in 1 usecs
[    6.330801] [drm] ring test on 5 succeeded in 1 usecs
[    6.330931] [drm] ring test on 6 succeeded in 1 usecs
[    6.331061] [drm] ring test on 7 succeeded in 1 usecs
[    6.331191] [drm] ring test on 8 succeeded in 1 usecs
[    6.331308] [drm] ring test on 10 succeeded in 2 usecs
[    6.331375] [drm] ring test on 11 succeeded in 2 usecs
[    7.357804] [drm] ring test on 12 succeeded in 0 usecs
[    7.357945] [drm] UVD initialized successfully.
[    7.558844] [drm] ring test on 13 succeeded in 8 usecs
[    7.558936] [drm] ring test on 14 succeeded in 1 usecs
[    7.559013] [drm] VCE initialized successfully.
[    7.559793] [drm] ib test on ring 0 succeeded
[    7.559948] [drm] ib test on ring 1 succeeded
[    7.560059] [drm] ib test on ring 2 succeeded
[    7.560167] [drm] ib test on ring 3 succeeded
[    7.560278] [drm] ib test on ring 4 succeeded
[    7.560385] [drm] ib test on ring 5 succeeded
[    7.560493] [drm] ib test on ring 6 succeeded
[    7.560600] [drm] ib test on ring 7 succeeded
[    7.560721] [drm] ib test on ring 8 succeeded
[    7.560815] [drm] ib test on ring 9 succeeded
[    7.560905] [drm] ib test on ring 10 succeeded
[    7.560994] [drm] ib test on ring 11 succeeded
[    7.561430] [drm] ib test on ring 12 succeeded
[    7.561574] [drm] ib test on ring 13 succeeded
[    7.563636] amdgpu: [powerplay] min_core_set_clock not set
[    7.564098] amdgpu: [powerplay] min_core_set_clock not set
[    7.564927] amdgpu: [powerplay] min_core_set_clock not set
[    7.654950] [drm] fb mappable at 0x403415000
[    7.655041] [drm] vram apper at 0x3FF000000
[    7.655124] [drm] size 33177600
[    7.655206] [drm] fb depth is 24
[    7.655288] [drm]    pitch is 15360
[    7.655617] fbcon: amdgpudrmfb (fb0) is primary device
[    7.656766] amdgpu: [powerplay] min_core_set_clock not set
[    7.666042] amdgpu: [powerplay] min_core_set_clock not set
[    7.667410] amdgpu: [powerplay] min_core_set_clock not set
[    7.668078] amdgpu: [powerplay] min_core_set_clock not set
[    7.669063] amdgpu: [powerplay] min_core_set_clock not set
[    7.670060] amdgpu: [powerplay] min_core_set_clock not set
[    7.671066] amdgpu: [powerplay] min_core_set_clock not set
[    7.672065] amdgpu: [powerplay] min_core_set_clock not set
[    7.759429] amdgpu: [powerplay] min_core_set_clock not set
[    7.760251] amdgpu: [powerplay] min_core_set_clock not set
[    7.761229] amdgpu: [powerplay] min_core_set_clock not set
[    7.762233] amdgpu: [powerplay] min_core_set_clock not set
[    7.774081] Console: switching to colour frame buffer device 480x135
[    7.785380] amdgpu 0000:00:01.0: fb0: amdgpudrmfb frame buffer device
[    7.788859] amdgpu: [powerplay] min_core_set_clock not set
[    7.799589] kfd kfd: Allocated 3969056 bytes on gart for device(1002:9874)
[    7.799645] kfd kfd: Reserved 2 pages for cwsr.
[    7.799715] kfd kfd: added device (1002:9874)
[    7.799720] [drm] Initialized amdgpu 3.13.0 20150101 for 0000:00:01.0 on minor 0
```


---

### 评论 #2 — oheid (2017-05-16T14:14:27Z)

X slows down/hangs very quickly but the machine allows remote ssh ! Fedora koji kernel version 4.11.1 has the same issue, so it seems not ROCK kernel specific. Booting with iommu=soft or deactivating IOMMU in BIOS seems to be the only solution but that also disables ROCm. Bummer.
Both kernel versions (rebuilt on the respective target machines) work nicely on a Ryzen 1700x + R9 480 + Asus crosshair VI hero combo so I tend to believe that this is a BIOS issue (0604) rather than Ubuntu 16 (supported) vs. Fedora 25 (unsupported?).

---

### 评论 #3 — gstoner (2017-05-16T14:18:26Z)


On May 16, 2017, at 9:14 AM, oheid <notifications@github.com<mailto:notifications@github.com>> wrote:


X slows down/hangs very quickly but the machine allows remote ssh ! Fedora koji kernel version 4.11.1 has the same issue, so it seems not ROCK kernel specific. Booting with iommu=soft or deactivating IOMMU in BIOS seems to be the only solution but that also disables ROCm. Bummer.
Both kernel versions (rebuilt on the respective target machines) work nicely on a Ryzen 1700x + R9 480 + Asus crosshair VI hero combo so I tend to believe that this is a BIOS issue (0604) rather than Ubuntu 16 (supported) vs. Fedora 25 (unsupported?).

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/121#issuecomment-301795623>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuV81Ah6HaQBc2C1o3Gt-9hY0qMtBks5r6a9EgaJpZM4NbFLV>.

We just received one of these motherboard,   we try it with Bristolridge in the Lab.

Greg


---

### 评论 #4 — jcoiner (2017-08-30T15:15:50Z)

Is there any update on this?

I have a Bristol Ridge with similar symptoms: X starts up glacially slow and does not get faster. On the other hand, I can run the sample OpenCL vector_copy program from the terminal successfully.

While X is being slow, 'top' reports near 100% idle, with near 0% values for us[er], sy[stem], and wa[iting for IO]. However the system load average never dips below 1.00 which seems weird. Something is doing a lot of waiting and it's counting toward the load average.

I also can disable IOMMU and then X will run using the older ati/radeon driver. That would be a good workaround for many purposes, however I'm hoping to do OpenCL development on this system so I'm looking forward to using ROCm!

Details:
 * Bristol Ridge A8-9600
 * Asrock A320M PRO4 motherboard, bios version 3.0
 * Ubuntu 16.04.3
   - first, I updated to the "hwe" versions of Xorg (1.19) and linux kernel (4.10)
   - then, I added the ROCm repo and installed rocm, rocm-opencl, rocm-opencl-dev, which pulled in the 4.11 rocm linux kernel. The system is now booting from this kernel.

Another workaround is to boot at runlevel 3 (no gui) and then ssh into the system, which is working.

I'm getting interesting dmesg chatter, for example:

[ 2786.497886] ------------[ cut here ]------------
[ 2786.497908] WARNING: CPU: 1 PID: 2695 at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/kernel/drivers/gpu/drm/drm_atomic_helper.c:1122 drm_atomic_helper_wait_for_vblanks.part.16+0x25f/0x270 [drm_kms_helper]
[ 2786.497909] [CRTC:40] vblank wait timed out
[ 2786.497910] Modules linked in: ctr ccm arc4 rt2800usb rt2x00usb rt2800lib rt2x00lib mac80211 cfg80211 ip6table_filter ip6_tables iptable_filter ip_tables x_tables pci_stub vboxpci(OE) vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) input_leds edac_mce_amd edac_core kvm_amd kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc aesni_intel aes_x86_64 crypto_simd snd_hda_codec_realtek snd_hda_codec_generic glue_helper snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi snd_seq cryptd snd_seq_device snd_timer snd fam15h_power soundcore k10temp 8250_dw i2c_designware_platform shpchp i2c_piix4 i2c_designware_core binfmt_misc mac_hid cuse parport_pc ppdev lp parport autofs4 hid_logitech_hidpp hid_logitech_dj hid_generic amdkfd amd_iommu_v2 amdgpu
[ 2786.497964]  i2c_algo_bit ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid fb_sys_fops r8169 mii ahci drm libahci wmi gpio_amdpt video gpio_generic
[ 2786.497980] CPU: 1 PID: 2695 Comm: kworker/1:1 Tainted: G        W  OE   4.11.0-kfd-compute-rocm-rel-1.6-148 #1
[ 2786.497981] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./A320M Pro4, BIOS P3.00 07/14/2017
[ 2786.497988] Workqueue: events console_callback
[ 2786.497990] Call Trace:
[ 2786.497999]  dump_stack+0x63/0x90
[ 2786.498003]  __warn+0xcb/0xf0
[ 2786.498006]  warn_slowpath_fmt+0x4b/0x60
[ 2786.498017]  drm_atomic_helper_wait_for_vblanks.part.16+0x25f/0x270 [drm_kms_helper]
[ 2786.498021]  ? wake_atomic_t_function+0x60/0x60
[ 2786.498031]  drm_atomic_helper_wait_for_vblanks+0x14/0x20 [drm_kms_helper]
[ 2786.498144]  amdgpu_dm_atomic_commit_tail+0x8aa/0xb80 [amdgpu]
[ 2786.498232]  ? dm_plane_helper_prepare_fb+0x12d/0x1b0 [amdgpu]
[ 2786.498242]  ? drm_atomic_helper_wait_for_dependencies+0x9c/0x160 [drm_kms_helper]
[ 2786.498252]  commit_tail+0x3f/0x70 [drm_kms_helper]
[ 2786.498261]  drm_atomic_helper_commit+0xa9/0x110 [drm_kms_helper]
[ 2786.498290]  drm_atomic_commit+0x4b/0x50 [drm]
[ 2786.498299]  drm_fb_helper_pan_display+0x1d7/0x2a0 [drm_kms_helper]
[ 2786.498304]  fb_pan_display+0xcf/0x160
[ 2786.498307]  bit_update_start+0x20/0x50
[ 2786.498309]  fbcon_switch+0x3b6/0x600
[ 2786.498313]  redraw_screen+0x151/0x220
[ 2786.498315]  ? fb_blank+0x94/0xb0
[ 2786.498317]  fbcon_blank+0x111/0x330
[ 2786.498322]  ? get_cpu_iowait_time_us+0x5a/0xd0
[ 2786.498325]  ? lock_timer_base+0x7d/0xa0
[ 2786.498328]  ? __internal_add_timer+0x1f/0x60
[ 2786.498330]  ? mod_timer+0x193/0x2d0
[ 2786.498333]  ? pick_next_task_fair+0x116/0x530
[ 2786.498336]  do_unblank_screen+0xd3/0x1a0
[ 2786.498338]  poke_blanked_console+0xbc/0xc0
[ 2786.498340]  console_callback+0x150/0x160
[ 2786.498343]  process_one_work+0x16b/0x480
[ 2786.498345]  worker_thread+0x4b/0x500
[ 2786.498348]  kthread+0x109/0x140
[ 2786.498350]  ? process_one_work+0x480/0x480
[ 2786.498352]  ? kthread_create_on_node+0x40/0x40
[ 2786.498357]  ret_from_fork+0x2c/0x40
[ 2786.498359] ---[ end trace 0ab3d1bb902727af ]---
[ 2796.682703] [drm:drm_atomic_helper_commit_cleanup_done [drm_kms_helper]] *ERROR* [CRTC:40:crtc-0] flip_done timed out


---

### 评论 #5 — jcoiner (2017-08-30T22:35:40Z)

Maybe I found the answer. It sounds like ROCm is intended for headless server development and maybe isn't expected to work with a display. I'm looking at the first response from gstoner here:
  https://community.amd.com/thread/214501

Please let me know if I'm misinterpreting this, but for now I'll just run ROCm headless which is fine for what I'm doing.


---
