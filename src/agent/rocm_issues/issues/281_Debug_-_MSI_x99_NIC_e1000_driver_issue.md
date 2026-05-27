# Debug - MSI x99 NIC e1000 driver issue 

> **Issue #281**
> **状态**: closed
> **创建时间**: 2017-12-21T22:17:06Z
> **更新时间**: 2020-11-18T11:34:59Z
> **关闭时间**: 2020-11-18T11:34:59Z
> **作者**: pszi1ard
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/281

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Any GPU tool or application is started it gets immediately killed. Kernel message below.

```
[ 3063.518775] BUG: unable to handle kernel paging request at ffffaad345941000
[ 3063.520296] IP: memset_erms+0x9/0x10
[ 3063.521807] PGD 4aec9b067
[ 3063.521808] PUD 4aec9c067
[ 3063.523312] PMD 4a1889067
[ 3063.524817] PTE 0
[ 3063.526319]
[ 3063.529273] Oops: 0002 [#5] SMP
[ 3063.530683] Modules linked in: xt_multiport iptable_filter ip_tables x_tables nfsv3 nfs_acl nfs lockd grace fscache binfmt_misc nls_iso8859_1 intel_rapl edac_core x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel kvm snd_hda_codec_hdmi irqbypass crct10dif_pclmul snd_hda_intel crc32_pclmul snd_hda_codec ghash_clmulni_intel snd_hda_core pcbc snd_hwdep snd_pcm aesni_intel snd_timer snd 8021q soundcore garp aes_x86_64 mrp crypto_simd mei_me stp glue_helper llc input_leds cryptd mei lpc_ich shpchp mac_hid sunrpc lp parport autofs4 hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu mxm_wmi i2c_algo_bit ttm drm_kms_helper syscopyarea sysfillrect e1000e sysimgblt fb_sys_fops ahci drm ptp libahci pps_core wmi
[ 3063.539426] CPU: 12 PID: 2814 Comm: rocminfo Tainted: G      D         4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[ 3063.540901] Hardware name: MSI MS-7885/X99S SLI PLUS (MS-7885), BIOS 1.D0 07/15/2016
[ 3063.542387] task: ffff9950e8ba2a00 task.stack: ffffaad345918000
[ 3063.543884] RIP: 0010:memset_erms+0x9/0x10
[ 3063.545365] RSP: 0018:ffffaad34591bd00 EFLAGS: 00010286
[ 3063.546849] RAX: ffff9950e85568ff RBX: 0000000000000008 RCX: 0000000000001000
[ 3063.548352] RDX: 0000000000009000 RSI: 00000000000000ff RDI: ffffaad345941000
[ 3063.549845] RBP: ffffaad34591bd48 R08: ffff9950ef51e440 R09: ffffaad345939000
[ 3063.551347] R10: ffff9950e8556800 R11: 0000000000000901 R12: ffff9950e2c2bd60
[ 3063.552839] R13: ffff9950e440dd80 R14: ffffaad34591bdf8 R15: ffff9950e2c2bc00
[ 3063.554316] FS:  00007fd2c03b3780(0000) GS:ffff9950ef500000(0000) knlGS:0000000000000000
[ 3063.555801] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 3063.557273] CR2: ffffaad345941000 CR3: 00000004a91b2000 CR4: 00000000001406e0
[ 3063.558766] Call Trace:
[ 3063.560262]  ? kfd_event_create+0x36c/0x550 [amdkfd]
[ 3063.561767]  kfd_ioctl_create_event+0x8a/0x160 [amdkfd]
[ 3063.563272]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[ 3063.564764]  ? kfd_ioctl_destroy_event+0x20/0x20 [amdkfd]
[ 3063.566271]  ? common_mmap+0x48/0x50
[ 3063.567767]  ? apparmor_mmap_file+0x18/0x20
[ 3063.569274]  do_vfs_ioctl+0x92/0x5a0
[ 3063.570772]  SyS_ioctl+0x79/0x90
[ 3063.572264]  entry_SYSCALL_64_fastpath+0x1e/0xad
[ 3063.573747] RIP: 0033:0x7fd2bf8ccf07
[ 3063.575212] RSP: 002b:00007fffe1c93fe8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[ 3063.576714] RAX: ffffffffffffffda RBX: 0000000001a81530 RCX: 00007fd2bf8ccf07
[ 3063.578228] RDX: 00007fffe1c94040 RSI: 00000000c0204b08 RDI: 0000000000000003
[ 3063.579744] RBP: 0000000000000000 R08: 0000000000000000 R09: 70fb000100003000
[ 3063.581260] R10: 000000000000046c R11: 0000000000000246 R12: 0000000000000000
[ 3063.582732] R13: 0000000001a878c0 R14: 0000000000000002 R15: 00007fffe1c94040
[ 3063.584160] Code: 48 c1 e9 03 40 0f b6 f6 48 b8 01 01 01 01 01 01 01 01 48 0f af c6 f3 48 ab 89 d1 f3 aa 4c 89 c8 c3 90 49 89 f9 40 88 f0 48 89 d1 <f3> aa 4c 89 c8 c3 90 49 89 fa 40 0f b6 ce 48 b8 01 01 01 01 01
[ 3063.587152] RIP: memset_erms+0x9/0x10 RSP: ffffaad34591bd00
[ 3063.588645] CR2: ffffaad345941000
[ 3063.590114] ---[ end trace 87f56add3e2b9acb ]---

```

---

## 评论 (60 条)

### 评论 #1 — gstoner (2017-12-21T23:13:07Z)

Which hardware? 

Greg

---

### 评论 #2 — gstoner (2017-12-21T23:14:12Z)

Also did you do this 

With move to upstreaming the KFD driver and the support of DKMS, for all Console aka headless user, you will need to add all your users to the ‘video” group by setting the Unix permissions

```shell
sudo usermod -a -G video <username>

---

### 评论 #3 — pszi1ard (2017-12-22T01:33:36Z)

> Which hardware?

 X99 + i7 5960X CPU.

The video group does not help now, I assume that will be needed in the future?

> With move to upstreaming the KFD driver and the support of DKMS,

From which Linux release has upstreaming started (wasn't it 4.15?); mine is still only 4.11.

---

### 评论 #4 — gstoner (2017-12-22T22:26:54Z)

For ROCm 1.7 you have to use this command it not future thing,   sudo usermod -a -G video <username>

For this release you do not need to use  4.11 any longer just the standard Ubuntu  Linux kernel that came with Ubuntu 16.04.3 LTS    This new release use DKMS, not replacing the Linux kernel like in the past.  Just like how AMDGPUpro installs 

---

### 评论 #5 — gstoner (2017-12-23T15:46:20Z)

Can you put a clean install of Ubuntu on the system 

sudo apt update
sudo apt dist-upgrade
sudo reboot

Then follow the instructions.   we run with same CPU on ASUS x99 system 

---

### 评论 #6 — gstoner (2017-12-28T18:52:30Z)

It looks like it issue with the Hawaii hardware and the driver, can you try it with just the Vega10 cards 

---

### 评论 #7 — richardmembarth (2018-01-03T17:30:50Z)

I've the same issue using the Radeon Pro WX 7100 (same kernel message).

---

### 评论 #8 — pszi1ard (2018-01-04T00:35:19Z)

@gstoner My machine had only a Fiji and a Vega10 card plugged in, so I don't think it's caused by Hawaii in my case either.

---

### 评论 #9 — VincentSC (2018-01-04T16:29:00Z)

Did you remove the special kernels for ROCm 1.6, make sure the default kernels are installed and reinstall ROCm 1.7?
````
# Search all old ROCm-enabled kernels, as these cannot be used for the DKMS'ed ROCM 1.7
apt-cache search compute-rocm

# when for example 1.6-148 and 1.6-180 were found:
apt remove linux-image-4.11.0-kfd-compute-rocm-rel-1.6-180 linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-180
apt remove linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148

# Make sure the default kernels are installed
apt-get install linux-headers-generic linux-image-generic

# Be sure you update Grub the right way - depending on your distribution and version it is quite different.
# Grub method 1
update-grub
# Grub method 2
grub-mkconfig -o /boot/grub/grub.cfg

# remove ROCm completely. 
apt-get autoremove rocm-profiler rocm-opencl-dev rocm-dev rocm-dkms
# Double check if all is gone
apt-cache search rocm
apt-cache search hsa

# install the new ROCm.
sudo apt-get install libnuma-dev rocm-dkms rocm-opencl-dev
````

---

### 评论 #10 — richardmembarth (2018-01-05T09:45:34Z)

@VincentSC Thanks for the hint, that solved the issue!

The system was booting an old ROCm-enabled kernel.

---

### 评论 #11 — VincentSC (2018-01-05T10:33:55Z)

Great it helped you! @gstoner, could you please update the wiki?

---

### 评论 #12 — spozi (2018-01-05T10:44:27Z)

Thank you @VincentSC. However, when I compile the hello world example, I got this error:

```
Failed to find any OpenCL platforms.
Failed to create OpenCL context.

```
It seems that there is no driver installed for my GPU (RX Vega 64). Should I install amdgpupro?


---

### 评论 #13 — richardmembarth (2018-01-05T10:46:47Z)

@spozi I had to disable Secure Boot - otherwise I couldn't load the amdgpu kernel module.

---

### 评论 #14 — spozi (2018-01-05T10:59:08Z)

Thank you @richardmembarth and @VincentSC  . After performing https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-355328679 and then  https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-355328679, I managed to run the Hello World example.

Thank you all.

---

### 评论 #15 — VincentSC (2018-01-05T11:02:38Z)

@spozi It says the module is not installed properly. Check using `dkms status`
```
$ sudo dkms status
rock, 1.7.60-ubuntu, 4.4.0-104-generic, x86_64: installed
````

---

### 评论 #16 — spozi (2018-01-05T11:06:25Z)

@VincentSC I need to disable Secure Boot in order to properly load the module.

---

### 评论 #17 — pszi1ard (2018-01-08T17:05:19Z)

I can confirm that the issue was caused by the incompatibility of the dkms modules with the custom KFD kernels. On a side note: it would have been good to avoid such breakage resulting from a simple package update and make sure to at least somehow warn about this (but new ROCm packages could have perhaps conflicted with the *kfd-compute-rocm kernel packages).

Related: which kernels (Ubuntu default/hwe) is the dkms compatible with? and which ones should it work best with, are there performance differences (in particular wrt better PCIe transfer)?

---

### 评论 #18 — pszi1ard (2018-01-10T20:28:14Z)

Update: I have been trying to use the 4.4 kernel, but for some reason (perhaps unrelated to the KFD module, my NIC is dropping connection repeatedly until the machine locks up and this has been occurring mostly/only[?] during benchmarking).

I've upgraded to the Ubuntu HWE kernel 4.13 after which I am getting kfd-related messages in kern.log and the machine seems to ultimately crash.

```
enqueue_ih_ring_entry: 4109 callbacks suppressed
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
enqueue_ih_ring_entry: 5618 callbacks suppressed
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
kfd kfd: Interrupt ring overflow, dropping interrupt 0
[...]
```



---

### 评论 #19 — gstoner (2018-01-11T00:06:50Z)

Can you run this 

sudo –s
echo 0 > /sys/module/amdkfd/parameters/noretry

sudo usermod -a -G video $LOGNAME

sudo vi /etc/modprobe.d/amdgpu.conf
options amdgpu vm_update_mode=0
options amdkfd cwsr_enable=0
sudo update-initramfs -u

Reboot and test

---

### 评论 #20 — pszi1ard (2018-01-11T01:02:14Z)

> sudo usermod -a -G video $LOGNAME

Already have it:
$ groups
ipausers video [...]

With the suggested parameters I still get (after reboot and during a benchmark run):
```
$ dmesg | tail
[  146.954919] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955030] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955130] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955230] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955329] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955427] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955526] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955625] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955723] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  146.955822] kfd kfd: Interrupt ring overflow, dropping interrupt 0
```

BTW, is it reasonable to assume that the NIC going down is related to the KFD module?



---

### 评论 #21 — gstoner (2018-01-11T01:18:31Z)

Your thinking we have shared interrupt issue 

---

### 评论 #22 — pszi1ard (2018-01-11T01:30:05Z)

This did not help, the machine went down again. In the meantime I realized however that
``echo 0 > /sys/module/amdkfd/parameters/noretry`` before reboot is not particularly useful, is it?

---

### 评论 #23 — gstoner (2018-01-11T01:31:02Z)

It is once we figure out the IRQ issue

On Jan 10, 2018, at 5:30 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


This did not help, the machine went down again. In the meantime I realized however that
echo 0 > /sys/module/amdkfd/parameters/noretry before reboot is not particularly useful, is it?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-356794955>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQiUl923tVUTLQlRA28qC_2rP7Sdks5tJWQegaJpZM4RKa3T>.



---

### 评论 #24 — pszi1ard (2018-01-11T01:42:29Z)

OK, let me know if you need more feedback!

---

### 评论 #25 — gstoner (2018-01-11T01:46:26Z)

Can we look at this 

=== Debugging ===

If you switch on CONFIG_IRQ_DOMAIN_DEBUG (which depends on
CONFIG_IRQ_DOMAIN and CONFIG_DEBUG_FS), you will find a new file in
your debugfs mount point, called irq_domain_mapping. This file
contains a live snapshot of all the IRQ domains in the system:

 name              mapped  linear-max  direct-max  devtree-node
 pl061                  8           8           0  /smb/gpio@e0080000
 pl061                  8           8           0  /smb/gpio@e1050000
 pMSI                   0           0           0  /interrupt-controller@e1101000/v2m@e0080000
 MSI                   37           0           0  /interrupt-controller@e1101000/v2m@e0080000
 GICv2m                37           0           0  /interrupt-controller@e1101000/v2m@e0080000
 GICv2                448         448           0  /interrupt-controller@e1101000

it also iterates over the interrupts to display their mapping in the
domains, and makes the domain stacking visible:


irq    hwirq    chip name        chip data           active  type            domain
    1  0x00019  GICv2            0xffff00000916bfd8     *    LINEAR          GICv2
    2  0x0001d  GICv2            0xffff00000916bfd8          LINEAR          GICv2
    3  0x0001e  GICv2            0xffff00000916bfd8     *    LINEAR          GICv2
    4  0x0001b  GICv2            0xffff00000916bfd8     *    LINEAR          GICv2
    5  0x0001a  GICv2            0xffff00000916bfd8          LINEAR          GICv2
[...]
   96  0x81808  MSI              0x          (null)           RADIX          MSI
   96+ 0x00063  GICv2m           0xffff8003ee116980           RADIX          GICv2m
   96+ 0x00063  GICv2            0xffff00000916bfd8          LINEAR          GICv2
   97  0x08800  MSI              0x          (null)     *     RADIX          MSI
   97+ 0x00064  GICv2m           0xffff8003ee116980     *     RADIX          GICv2m
   97+ 0x00064  GICv2            0xffff00000916bfd8     *    LINEAR          GICv2

Here, interrupts 1-5 are only using a single domain, while 96 and 97
are build out of a stack of three domain, each level performing a
particular function.

---

### 评论 #26 — pszi1ard (2018-01-12T01:46:24Z)

If I understand correctly, that requires me to build a kernel. Will carve out some time to do that if there's no way around it, hopefully within a few days.

---

### 评论 #27 — gstoner (2018-01-12T02:17:14Z)

It ok I talked to the kernel team. The message are as they put it harmless debug message.    I have new PCIe performances test for you

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Szilárd Páll <notifications@github.com>
Sent: Thursday, January 11, 2018 5:46:25 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Debug - Linux Kernel issue with pszi1ard system post ROCm 1.7 DKMS install - Need more info (#281)


If I understand correctly, that requires me to build a kernel. Will carve out some time to do that if there's no way around it, hopefully within a few days.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-357119044>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuV3krf4uU32yu72RNgUmeo3QZalaks5tJrlxgaJpZM4RKa3T>.


---

### 评论 #28 — pszi1ard (2018-01-18T17:12:52Z)

> It ok I talked to the kernel team. The message are as they put it harmless debug message.

Does that mean that my NIC drops are not related? (Note that on an otherwise identical machine with no ROCm installed I do not see such issues.)

Any further thoughts on how to make ROCm 1.7 work in my setup? Otherwise I'd have to revert to 1.6 to be able to do development.

>  have new PCIe performances test for you

You mean a new tool or updates regarding the performance? I still see pretty slow PCIe transfers with ROCm 1.7 too (in particular with Fiji as well as on a Xeon-SP platform with R560)..

---

### 评论 #29 — gstoner (2018-01-18T17:15:37Z)

Fiji, right now SDMA is turned off for transfer it using BLT kernel right now it was in 1.6 as well,  on Vega10 SDMA is on,  We have new drop of 1.7.1 coming out in next couple of  weeks.

Greg.

On Jan 18, 2018, at 11:12 AM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


It ok I talked to the kernel team. The message are as they put it harmless debug message.

Does that mean that my NIC drops are not related? (Note that on an otherwise identical machine with no ROCm installed I do not see such issues.)

Any further thoughts on how to make ROCm 1.7 work in my setup? Otherwise I'd have to revert to 1.6 to be able to do development.

have new PCIe performances test for you

You mean a new tool or updates regarding the performance? I still see pretty slow PCIe transfers with ROCm 1.7 too (in particular with Fiji as well as on a Xeon-SP platform with R560)..

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-358715506>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYxbyGvrQ1wf2GI1LeCxdXvp0tz2ks5tL3uWgaJpZM4RKa3T>.



---

### 评论 #30 — pszi1ard (2018-01-19T00:12:31Z)

> Fiji, right now SDMA is turned off for transfer it using BLT kernel right now it was in 1.6 as well,

Is that true for Polaris-based consumer cards too?

> We have new drop of 1.7.1 coming out in next couple of  weeks.

Can I expect that to fix the kernel issue (that you suggested was an IRQ clash)?


---

### 评论 #31 — gstoner (2018-01-19T01:24:39Z)

Is that true for Polaris-based consumer cards too?
yes.. 



---

### 评论 #32 — boxerab (2018-01-19T12:07:10Z)

Are there plans to enable SDMA at some point for Polaris ? 

---

### 评论 #33 — gstoner (2018-01-19T14:20:20Z)

We working with the SDMA Firmware team what can be done, since without the fix you have stability issue 

---

### 评论 #34 — psn9 (2018-01-30T05:28:09Z)

Hello @VincentSC , I followed the procedure as specified by you in [this comment](https://github.com/RadeonOpenCompute/ROCm/issues/281#issuecomment-355328679) .

and this is my `sudo dkms status` : 

rock, 1.7.60-ubuntu: added

But when I try the sample square program in HIP, I get - 

```
/opt/rocm/bin/rocminfo: error while loading shared libraries: libhsakmt.so.1: cannot open shared object file: No such file or directory
ld: cannot find -lhsakmt
clang-6.0: error: linker command failed with exit code 1 (use -v to see invocation)
Died at /opt/rocm/hip/bin/hipcc line 500
```

How to get libhsakmt.so.1 ? 

I couldn't locate the shared object either. I usually find it in **_/opt/rocm/lib_** but it doesn't exist there.

FYI, I also got this error while installing libnuma-dev & rocm-dkms : 

_ERROR (dkms apport): kernel package linux-headers-4.11.12-041112-generic is not supported 
Error! Bad return status for module build on kernel: 4.11.12-041112-generic (x86_64)
Consult /var/lib/dkms/rock/1.7.60-ubuntu/build/make.log for more information._

Found this in the error log file : 

_/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c: In function ‘acp_hw_init’:
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c:330:4: error: ‘DW_I2S_QUIRK_16BIT_IDX_OVERRIDE’ undeclared (first use in this function)
    DW_I2S_QUIRK_16BIT_IDX_OVERRIDE;
    ^
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c:330:4: note: each undeclared identifier is reported only once for each function it appears in
scripts/Makefile.build:294: recipe for target '/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.o' failed
make[2]: *** [/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.o] Error 1
make[2]: *** Waiting for unfinished jobs...._

any leads ?

---

### 评论 #35 — VincentSC (2018-01-30T11:33:21Z)

Seems something did not go well. There should be `/opt/rocm/lib/libhsakmt.so` and `/opt/rocm/libhsakmt/lib/`.

---

### 评论 #36 — psn9 (2018-01-30T12:00:57Z)

@VincentSC I erased everything and installed Ubuntu 16.04 fresh. Then I followed the same procedure to install rocm 1.7 as in the repo. Now am ending up with something like 

`There is no device can be used to do the computation`

It seems a problem with HCC. is that so ?

my dkms status : 

`rock, 1.7.60-ubuntu, 4.13.0-32-generic, x86_64: installed`

---

### 评论 #37 — VincentSC (2018-01-30T12:23:19Z)

After a reboot, do:
```
sudo apt install clinfo
clinfo
````
What does it say?

---

### 评论 #38 — psn9 (2018-01-30T12:28:24Z)

I get this, 

`Number of platforms                               0`

additional info, I get this on running `/opt/rocm/bin/rocm_agent_enumerator` : 

gfx000
gfx803

and after I rebooted , all my icons & display look larger , I guess I lost the gpu driver .


---

### 评论 #39 — VincentSC (2018-01-30T12:32:37Z)

What is your device? 

---

### 评论 #40 — psn9 (2018-01-30T12:33:27Z)

VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca)

Processor : Intel® Core™ i5-4440 CPU @ 3.10GHz × 4 

---

### 评论 #41 — VincentSC (2018-01-30T12:55:24Z)

A Nano? That triggered me. On one freshly installed machine we have the same - it has a Vega Frontier Edition and a Nano, but it only recognised the Vega. Difference with this machine and most others is that it has Ubuntu 17.10 instead of 16.04.3.

---

### 评论 #42 — VincentSC (2018-01-30T13:00:00Z)

Since you 16.04, I have no idea what could be a common cause

---

### 评论 #43 — psn9 (2018-01-30T13:00:32Z)

I don't get it. Rocm 1.7 not suitable for my GPU ?

---

### 评论 #44 — VincentSC (2018-01-30T13:01:36Z)

It should, but possibly the Nano is not recognised by ROCm 1.7.

---

### 评论 #45 — psn9 (2018-01-30T13:05:15Z)

Is it a known problem already ? any immediate solutions ?

---

### 评论 #46 — gstoner (2018-01-30T13:42:50Z)

Fiji Nano will always be recognized by  ROCm since it was the first card we built ROCm around.   Only issue we need to retest is  4.10 and AMDGPU  DKMS/KCL installing correctly,  We have 1.7.1 on coming out I have the team looking at 4.4, 4.10 and 4.13 compatibility before we release it,  Note we test Fiji Nano, RX480, RX470, Vega10, MI25 the most in SQE.  

---

### 评论 #47 — psn9 (2018-01-30T14:27:06Z)

So , on suspecting linux kernel version to be the problem , I reverted back to 4.10 and installed rocm 1.7 fresh.

This is my `sudo dkms status` output : 

`rock, 1.7.60-ubuntu, 4.10.0-28-generic, x86_64: installed`
`rock, 1.7.60-ubuntu, 4.13.0-32-generic, x86_64: installed`

and `uname -a` output : 

`Linux psn 4.10.0-28-generic #32~16.04.2-Ubuntu SMP Thu Jul 20 10:19:48 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux`

But I still end up with : `There is no device can be used to do the computation` 

Is there by any chance , the 4.10 dkms is not being used and 4.13 dkms is the one actually being used ? is this possible ?


---

### 评论 #48 — VincentSC (2018-01-30T15:02:19Z)

@gstoner, are the devices that are (not) accepted logged? And is there some sort of debug-mode to get more info during this phase?

---

### 评论 #49 — pszi1ard (2018-02-01T17:58:43Z)

@gstoner this thread has derailed quite a bit, but I'd really like to know whether I should expect that my X99 machine will be usable with the next patch release. Right now I can neither use it (if I use NFS or even are logged in over ssh, the machine crashes) nor downgrade to ROCm 1.6.

---

### 评论 #50 — gstoner (2018-02-01T18:50:46Z)

We run ASUS x99 machine with FIJI and Vega10 now with Haswell based I7.  It is the X99-E WS,  So we know it not Intel Extreme Edition issue nor x99 Chipset issue.   We need to retest with your particular motherboard when we get 1.7.1 out. 
 

---

### 评论 #51 — pszi1ard (2018-02-01T19:10:35Z)

Thanks for the feedback. Is there anything more I can do to facilitate the testing? Nightly builds would be useful for that.

---

### 评论 #52 — psn9 (2018-02-14T04:34:54Z)

@VincentSC  @gstoner Just an update from my side.

I had to **disable Secure Boot while installing a fresh Ubuntu** to get rocm 1.7 working.Here's what I did : 

Mine is an Asus PC and doing a F2 while booting led me to the Boot Menu.
Where I selected 'Advanced Options' within which I selected "Boot".
And then , I found the Secure Boot to be enabled.
So I did a "Clear all Saved Keys" which disabled the Secure Boot.

Then I did a fresh Ubuntu 16.04.3 install which contained : 
linux-image-4.10.0-28-generic &
linux-image-4.13.0-32-generic

Last, I did a rocm 1.7 installation as described here : [Rocm 1.7 install ](https://github.com/RadeonOpenCompute/ROCm#first-make-sure-your-system-is-up-to-date)

Rebooted the system and everything works fine now.

---

### 评论 #53 — VincentSC (2018-02-14T14:12:45Z)

Maybe a section "current limitations" can be added, where "no/limited support for secure boot" can be listed.

---

### 评论 #54 — pszi1ard (2018-05-16T16:12:51Z)

Just installed ROCm 1.8 and my dmesg is still full of " e1000e: eth0 NIC Link is Down" followed by process hung messages when my process tries to write to NFS.

This is getting problematic, we've spent ~5 months hoping for a fix with temporary dev machines and time-consuming debugging and workarounds. Can you please advise me whether there is a solution in the pipeline or we should just forget about this platform/machine?


---

### 评论 #55 — gstoner (2018-05-16T16:21:09Z)

If you run the motherboard without the ROCm driver installed does the nic behave properly running NFS.  



---

### 评论 #56 — gstoner (2018-05-16T16:22:16Z)

Also, can you try CENTOS 7.4 with ROCm 1.8 on this board? It may be a driver issue in Ubuntu.

---

### 评论 #57 — gstoner (2018-05-16T16:35:34Z)

Also, did you look on Intel site about the Ethernet controller I am seeing an issue with MSI-X in the readme note https://downloadcenter.intel.com/download/15817  There is a newer driver at Intel site. 

---

### 评论 #58 — pszi1ard (2018-05-31T18:22:05Z)

I've now tried the latest e1000e drivers:
```
$ modinfo -F version e1000e
3.4.0.2-NAPI
```
but as soon as I plugged the card and started a run and some network activity concurrently the NIC link went down. As I was in the server room with the display connected to the Vega GPU I noticed that the screen started to flicker and went blank. Found these in the kern.log:
```
May 31 19:17:40 dev-haswell-gpu01 kernel: [  977.050305] nfs: server fs.tcblab not responding, still trying
May 31 19:17:55 dev-haswell-gpu01 kernel: [  991.744164] [drm] SADs count is: -2, don't need to read it
May 31 19:18:04 dev-haswell-gpu01 kernel: [ 1001.044417] [drm] SADs count is: -2, don't need to read it
May 31 19:18:09 dev-haswell-gpu01 kernel: [ 1006.144562] [drm] SADs count is: -2, don't need to read it
May 31 19:18:15 dev-haswell-gpu01 kernel: [ 1011.864726] [drm] SADs count is: -2, don't need to read it
May 31 19:18:19 dev-haswell-gpu01 kernel: [ 1016.094837] [drm] SADs count is: -2, don't need to read it
```

---

### 评论 #59 — pszi1ard (2018-08-24T18:40:07Z)

Any update?

The issue still persists; the last thing I tried is installing the 1.173.1 linux-firmware, but installing it on Ubuntu 16.04 with 4.15 kernels makes clinfo not report any devices (but the kernel does initalize them and rocm-smi displays them). Is this expected?

---

### 评论 #60 — ROCmSupport (2020-11-18T11:28:01Z)

Thanks @pszi1ard
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---
