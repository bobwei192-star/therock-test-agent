# Ubuntu 17.10, amdgpu not working properly after kernel upgrade to 4.13.0-36

> **Issue #344**
> **状态**: closed
> **创建时间**: 2018-02-22T01:54:20Z
> **更新时间**: 2018-06-03T14:40:12Z
> **关闭时间**: 2018-06-03T14:40:12Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/344

## 描述

I was happily using ROCm 1.7 on Ubuntu 17.10, with kernel 4.13.0-32.
Today I did a "apt upgrade" and updated, among others, the kernel to 4.13.0-36.

After this, when I boot the new kernel (4.13.0-36) the GPU is not initialized properly: every graphic refresh is extremely slow, and the GPU fan has a different speed. Also, OpenCL and clinfo don't detect any platform.
```
$ dmesg | grep -i amd
[    0.000000] Linux version 4.13.0-36-generic (buildd@lcy01-amd64-017) (gcc version 7.2.0 (Ubuntu 7.2.0-8ubuntu3.2)) #40-Ubuntu SMP Fri Feb 16 20:07:48 UTC 2018 (Ubuntu 4.13.0-36.40-generic 4.13.13)
[    0.000000]   AMD AuthenticAMD
[    0.000000] RAMDISK: [mem 0x31de1000-0x34ee7fff]
[   27.477761] [drm] amdgpu kernel modesetting enabled.
```

I can still boot the previous kernel, 4.13.0-32, and then everything works fine: many more "amdgpu" lines in dmesg, OpenCL working correctly, screen update is fast, fan is low.

Any hint about what causes this? any fix/workaround I can try?

---

## 评论 (13 条)

### 评论 #1 — simonwaid (2018-02-23T06:22:11Z)

Similar thing here. After upgrade to 4.13.0-36 on Ubuntu 17.10 the screen stays black and booting takes an eternity.

---

### 评论 #2 — gstoner (2018-02-23T14:04:23Z)

@Unkraut3 @preda  I sent this issue over to the base Linux driver team since the error is in the DAL code now know as the DC code.  I will ping them again to see what they are seeing 

---

### 评论 #3 — gstoner (2018-02-23T14:11:46Z)

I also have them double check the KCL as well. 

---

### 评论 #4 — dfad44 (2018-02-23T14:53:57Z)

After upgrading i lost complete functionality on one gfx900. Although i think it was already falling apart as that rig kept having persistent node errors until the card in question was replaced. And yes it is a Hynix.

---

### 评论 #5 — krrk (2018-02-28T19:06:02Z)

I had the same issue on Ubuntu 16.04 after finally rebooting today into 4.13.0-36 (from 4.13.0-32). I was able to get OpenCL working again by recompiling the kernel module:

```
sudo dkms remove rock/1.7.60-ubuntu
sudo dkms install --force rock/1.7.60-ubuntu
```

Then I added `amdkfd` to `/etc/initramfs-tools/modules` and `/etc/modules` (I already had `amdgpu` in these files) and rebuilt the initramfs `sudo update-initramfs -u`. Upon reboot everything seems to be working fine both graphics and OpenCL. I'm not sure if its necessary to add amdkfd to the initramfs, but it was not loaded upon boot and loading it with modprobe didn't make OpenCL to work. On the previous kernel amdkfd was already loaded upon boot so I'm not sure why this became necessary.


---

### 评论 #6 — gstoner (2018-03-02T23:01:10Z)

@preda @krrk @dfad44 @Unkraut3   can you try this beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2

---

### 评论 #7 — dfad44 (2018-03-02T23:09:52Z)

Thank you. Will do as soon as possible

---

### 评论 #8 — gstoner (2018-03-02T23:11:11Z)

it support the 4.13 linux kernel we finding this best base 

---

### 评论 #9 — krrk (2018-03-03T00:34:24Z)

@gstoner Thanks. I have some initial comments about the install process. I assumed as a beta you wanted to test also how upgrades would work so I performed a `sudo dpkg --install *.deb`.

The package miopen-opencl had the following error:
```
Unpacking miopen-opencl (1.2.1-cf3d051) ...
dpkg: error processing archive MIOpen-OpenCL-1.2.1-cf3d051-Linux.deb (--install):
 trying to overwrite '/opt/rocm/miopen/include/miopen/config.h', which is also in package miopen-hip 1.2.1-cf3d051
dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
```

When dkms-rock was installing I found the same problem I've been having with dkms-rock since I've started using it (1.7.60) upon each kernel update. dkms does not install the built version of amdgpu.ko because one already exists in the kernel from the `linux-image-extra-<kernelversion>-generic` package. It looks like dkms is looking at the srcversion string that modinfo returns:

```
Building initial module for 4.13.0-36-generic
Done.

amdgpu:
Running module version sanity check.
Error! Module version C502C9F63988A81945CAABD for amdgpu.ko
is not newer than what is already found in kernel 4.13.0-36-generic (D3580B8CE287C145D0DC895).
You may override by specifying --force.
```

I have checked that the checksum `D3580B8CE287C145D0DC895` is the same as the module in linux-image-extra-4.13.0-36-generic and since this is a "higher" version of the new module it isn't replaced, yet there are some differences being reported by modinfo here is a diff of the old version on left versus new version on right:

```
1c1
< filename:       /lib/modules/4.13.0-36-generic/updates/amdgpu.ko
---
> filename:       /var/lib/dkms/rock/1.7.137-ubuntu/4.13.0-36-generic/amd64/module/amdgpu.ko
82d81
< firmware:       amdgpu/vega10_smc.bin
91a91
> firmware:       amdgpu/raven_asd.bin
92a93
> firmware:       amdgpu/polaris12_mec2_2.bin
93a95
> firmware:       amdgpu/polaris12_mec_2.bin
94a97
> firmware:       amdgpu/polaris12_me_2.bin
95a99
> firmware:       amdgpu/polaris12_pfp_2.bin
96a101
> firmware:       amdgpu/polaris12_ce_2.bin
98a104
> firmware:       amdgpu/polaris10_mec2_2.bin
99a106
> firmware:       amdgpu/polaris10_mec_2.bin
100a108
> firmware:       amdgpu/polaris10_me_2.bin
101a110
> firmware:       amdgpu/polaris10_pfp_2.bin
102a112
> firmware:       amdgpu/polaris10_ce_2.bin
104a115
> firmware:       amdgpu/polaris11_mec2_2.bin
105a117
> firmware:       amdgpu/polaris11_mec_2.bin
106a119
> firmware:       amdgpu/polaris11_me_2.bin
107a121
> firmware:       amdgpu/polaris11_pfp_2.bin
108a123
> firmware:       amdgpu/polaris11_ce_2.bin
194a210,211
> firmware:       amdgpu/vega10_acg_smc.bin
> firmware:       amdgpu/vega10_smc.bin
207c224
< srcversion:     D3580B8CE287C145D0DC895
---
> srcversion:     C502C9F63988A81945CAABD
418,419c435
< depends:        drm,drm_kms_helper,ttm,i2c-algo-bit
< intree:         Y
---
> depends:        drm,drm_kms_helper,amdttm,amdkcl,i2c-algo-bit
423c439,441
< parm:           gartsize:Size of PCIE/IGP gart to setup in megabytes (32, 64, etc., -1 = auto) (int)
---
> parm:           vis_vramlimit:Restrict visible VRAM for testing, in megabytes (int)
> parm:           gartsize:Size of GART to setup in megabytes (32, 64, etc., -1=auto) (uint)
> parm:           gttsize:Size of the GTT domain in megabytes (-1 = auto) (int)
440a459
> parm:           vm_fragment_size:VM fragment size in bits (4, 5, etc. 4 = 64K (default), Max 9 = 2M) (int)
444,445c463,464
< parm:           vm_update_mode:VM update using CPU (0 = never (default except for large BAR(LB)), 1 = Graphics only, 2 = Compute only (default for LB), 3 = Both (int)
< parm:           vram_page_split:Number of pages after we split VRAM allocations (default 1024, -1 = disable) (int)
---
> parm:           vm_update_mode:VM update using CPU (0 = never (default), 1 = Graphics only, 2 = Compute only, 3 = Both, -1 = Compute only for Large Bar (int)
> parm:           vram_page_split:Number of pages after we split VRAM allocations (default 512, -1 = disable) (int)
446a466
> parm:           dc:Display Core driver (1 = enable, 0 = disable, -1 = auto (default)) (int)
449c469
< parm:           ppfeaturemask:all power features enabled (default)) (int)
---
> parm:           ppfeaturemask:all power features enabled (default)) (uint)
451a472
> parm:           ssg:SSG support (1 = enable, 0 = disable (default)) (int)
455a477
> parm:           sdma_phase_quantum:SDMA context switch phase quantum (x 1K GPU clock cycles, 0 = no change (default 32)) (uint)
465,466c487,489
< parm:           si_support:SI support (1 = enabled, 0 = disabled (default)) (int)
< parm:           cik_support:CIK support (1 = enabled, 0 = disabled (default)) (int)
---
> parm:           compute_multipipe:Force compute queues to be spread across pipes (1 = enable, 0 = disable, -1 = auto) (int)
> parm:           si_support:SI support (1 = enabled (default), 0 = disabled) (int)
> parm:           cik_support:CIK support (1 = enabled (default), 0 = disabled) (int)
```

So there are differences and the new version is important. The good news is I see that the new version now depends on amdkcl which means I probably won't need to list amdkfd or amdkcl in the initramfs modules.

I would also recommend that you set BUILD_EXCLUSIVE_KERNEL in /usr/share/rock-1.7.137-ubuntu/dkms.conf since we know the module will fail to build on other kernels. For example when I first started using rocm I had kernel 4.15 installed, but I decided to remove it because every kernel upgrade dkms tried to build amdgpu for kernel 4.15 just to fail every time. Here is an explanation of the parameter from `man dkms`:

```
       BUILD_EXCLUSIVE_KERNEL=
              This  optional  directive  allows you to specify a regular expression which defines the subset of kernels which DKMS is allowed to
              build your module for.  If the kernel being built for does not match against this regular expression, the dkms  build  will  error
              out.  For example, if you set it as ="^2.4.*", your module would not be built for 2.6 kernels.
```

Other things I've noticed about the packaging are that `hcfft` no longer seems to be necessary (but perhaps you repaced this by rocfft?) and apt wants to install the repo version of `rocm-device-libs` over the version you provides us in the beta when I do an apt upgrade.

I'll let you know if I have other troubles after rebooting.

---

### 评论 #10 — Mandrewoid (2018-03-03T00:44:17Z)

Hi @krrk  I had the same problem in installation: #350 Except it presented a bit differently at first.
It appears you cant have MIOpen-HIP and MIOpen-OpenCL both installed.

---

### 评论 #11 — gstoner (2018-03-03T01:53:28Z)

@krrk Thanks this is what i am looking for, we get this cleaned up and update for Monday 

---

### 评论 #12 — ghost (2018-03-15T16:58:29Z)

Please see top comment, 14 days left to the beaver lts, 16.04.04 is going to need backports. 18.04 or the downgrade to the .32 kernel. I have had it working selinux=0 in grub and disable apparmor

---

### 评论 #13 — ghost (2018-03-17T21:13:50Z)

Also, since kernel 4.13, adding the amdgpu.si_support=1 radeon.si_support=0 or amdgpu.cik_support=1 radeon.cik_support=0 kernel parameter is required. Otherwise, AMDGPU will not start and you will end up with either radeon being used instead or the display being frozen during the boot.

AMD DC on pre-Vega cards
AMD DC (display code), introduced in linux 4.15

Here is the latest firmware too
https://www.archlinux.org/packages/?name=linux-firmware


---
