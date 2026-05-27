# hsa_init fails (0x1008)

> **Issue #95**
> **状态**: closed
> **创建时间**: 2017-03-07T17:25:32Z
> **更新时间**: 2017-07-02T17:27:03Z
> **关闭时间**: 2017-07-02T17:27:03Z
> **作者**: jrprice
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/95

## 描述

I am using an S9150 with an i5-6600 (Skylake) host CPU, on Fedora 23.

The `vector_copy` sample fails in `hsa_init` with the status `0x1008` (out of resources?). The output of `rocm-smi` is below:

```
===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : GPU ID: 0x67a0
============================================================================
============================================================================
GPU[0]          : Temperature: 35.0c
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: None (None)
GPU[0]          : GPU Memory Clock Level: None (None)
============================================================================
============================================================================
GPU[0]          : Fan Level: 255 (100.0)%
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0]          : Cannot get OverDrive value: OverDrive not supported
============================================================================
============================================================================
GPU[0]          : Compute Power Profile not supported
============================================================================
============================================================================
============================================================================
===================          End of ROCm SMI Log         ===================
```


---

## 评论 (10 条)

### 评论 #1 — gstoner (2017-03-08T04:40:12Z)

Can you first check your dmesages, It sound like the KFD did not load.

Greg


On Mar 7, 2017, at 11:25 AM, James Price <notifications@github.com<mailto:notifications@github.com>> wrote:


I am using an S9150 with an i5-6600 (Skylake) host CPU, on Fedora 23.

The vector_copy sample fails in hsa_init with the status 0x1008 (out of resources?). The output of rocm-smi is below:

===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : GPU ID: 0x67a0
============================================================================
============================================================================
GPU[0]          : Temperature: 35.0c
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: None (None)
GPU[0]          : GPU Memory Clock Level: None (None)
============================================================================
============================================================================
GPU[0]          : Fan Level: 255 (100.0)%
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0]          : Cannot get OverDrive value: OverDrive not supported
============================================================================
============================================================================
GPU[0]          : Compute Power Profile not supported
============================================================================
============================================================================
============================================================================
===================          End of ROCm SMI Log         ===================


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/95>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQLkaLwF12k4bIVxpm1Nsac1ygHQks5rjZMNgaJpZM4MVyEE>.



---

### 评论 #2 — jrprice (2017-03-08T09:11:17Z)

This is the only line mentioning `kfd` in `dmesg`:

    [    1.356129] kfd kfd: Initialized module

Here's a `grep` for `radeon` as well:

```
[    1.347605] [drm] radeon kernel modesetting enabled.
[    1.357109] radeon 0000:02:00.0: VRAM: 16384M 0x0000000000000000 - 0x00000003FFFFFFFF (16384M used)
[    1.357110] radeon 0000:02:00.0: GTT: 2048M 0x0000000400000000 - 0x000000047FFFFFFF
[    1.357391] [drm] radeon: 16384M of VRAM memory ready
[    1.357392] [drm] radeon: 2048M of GTT memory ready.
[    1.371196] [drm] radeon: dpm initialized
[    1.378771] radeon 0000:02:00.0: WB enabled
[    1.378775] radeon 0000:02:00.0: fence driver on ring 0 use gpu addr 0x0000000400000c00 and cpu addr 0xffff9d63e8b3ec00
[    1.378775] radeon 0000:02:00.0: fence driver on ring 1 use gpu addr 0x0000000400000c04 and cpu addr 0xffff9d63e8b3ec04
[    1.378776] radeon 0000:02:00.0: fence driver on ring 2 use gpu addr 0x0000000400000c08 and cpu addr 0xffff9d63e8b3ec08
[    1.378777] radeon 0000:02:00.0: fence driver on ring 3 use gpu addr 0x0000000400000c0c and cpu addr 0xffff9d63e8b3ec0c
[    1.378777] radeon 0000:02:00.0: fence driver on ring 4 use gpu addr 0x0000000400000c10 and cpu addr 0xffff9d63e8b3ec10
[    1.379171] radeon 0000:02:00.0: fence driver on ring 5 use gpu addr 0x0000000000078d30 and cpu addr 0xffffb80b06c38d30
[    1.379357] radeon 0000:02:00.0: fence driver on ring 6 use gpu addr 0x0000000400000c18 and cpu addr 0xffff9d63e8b3ec18
[    1.379357] radeon 0000:02:00.0: fence driver on ring 7 use gpu addr 0x0000000400000c1c and cpu addr 0xffff9d63e8b3ec1c
[    1.379380] radeon 0000:02:00.0: radeon: using MSI.
[    1.379401] [drm] radeon: irq initialized.
[    2.615531] [drm] Radeon Display Connectors
[    2.823930] radeon 0000:02:00.0: No connectors reported connected with modes
[    2.824839] fbcon: radeondrmfb (fb0) is primary device
[    2.835653] radeon 0000:02:00.0: fb0: radeondrmfb frame buffer device
[    2.845215] [drm] Initialized radeon 2.46.0 20080528 for 0000:02:00.0 on minor 0
```

and a `grep` for `AMD`:

```
[    1.349759] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    1.349760] AMD IOMMUv2 functionality not available on this system
```

Full [`dmesg` log here](https://gist.github.com/jrprice/dae6e13163e37d841b3c9afb8a92c2fd#file-dmesg-log).




---

### 评论 #3 — jrprice (2017-03-08T15:27:40Z)

Running `strace` indicates that `hsa_init` is trying to open `/sys/devices/virtual/kfd/kfd/topology/system_properties` which doesn't exist.

```
[root@node33 ~]# ls -l /sys/devices/virtual/kfd/kfd/
total 0
-r--r--r-- 1 root root 4096 Mar  8 15:00 dev
drwxr-xr-x 2 root root    0 Mar  8 15:00 power
lrwxrwxrwx 1 root root    0 Mar  8 15:00 subsystem -> ../../../../class/kfd
-rw-r--r-- 1 root root 4096 Mar  8 15:00 uevent
[root@node33 ~]# cat /sys/devices/virtual/kfd/kfd/dev 
243:0
```

---

### 评论 #4 — gstoner (2017-03-09T04:17:50Z)

It what I thought your KFD did not load.

You followed these instructions with  Fedora 23
RPM repository - dnf (yum)

A dnf (yum) repository is also available for installation of rpm packages. To configure a system to use the ROCm rpm directory create the file /etc/yum.repos.d/rocm.repo with the following contents:

[remote]

name=ROCm Repo

baseurl=http://packages.amd.com/rocm/yum/rpm/

enabled=1

gpgcheck=0


Execute the following commands:

sudo dnf clean all
sudo dnf install rocm


As with the debian packages, it is possible to install rocm-dev or rocm-kernel individually. To uninstall the packages execute:

sudo dnf remove rocm


#### Manual installation steps for Fedora 23

A fully functional Fedora installation requires a few manual steps to properly setup, including: * Building compatible libc++ and libc++abi libraries for Fedora<https://github.com/RadeonOpenCompute/hcc/wiki#fedora>

Verify Installation

To verify that the ROCm stack completed successfully you can execute to HSA vectory_copy sample application (we do recommend that you copy it to a separate folder and invoke make therein):

cd /opt/rocm/hsa/sample
make
./vector_copy



Greg
On Mar 8, 2017, at 9:27 AM, James Price <notifications@github.com<mailto:notifications@github.com>> wrote:


Running strace indicates that hsa_init is trying to open /sys/devices/virtual/kfd/kfd/topology/system_properties which doesn't exist.

[root@node33 ~]# ls -l /sys/devices/virtual/kfd/kfd/
total 0
-r--r--r-- 1 root root 4096 Mar  8 15:00 dev
drwxr-xr-x 2 root root    0 Mar  8 15:00 power
lrwxrwxrwx 1 root root    0 Mar  8 15:00 subsystem -> ../../../../class/kfd
-rw-r--r-- 1 root root 4096 Mar  8 15:00 uevent
[root@node33 ~]# cat /sys/devices/virtual/kfd/kfd/dev
243:0


—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/95#issuecomment-285071985>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaOLvJtXtAho-PwqcXUS3Jrpamg_ks5rjsjtgaJpZM4MVyEE>.



---

### 评论 #5 — jrprice (2017-03-09T13:22:55Z)

OK, turns out I was still booting into the regular Fedora kernel. Maybe worth a note in the ROCm installation docs that you need to change the default kernel in GRUB if working remotely?

The `vector_copy` sample gets further, but now hangs just after "Loading the code object succeeded". This line shows up in `dmesg`:

    [   87.753631] kfd kfd: HSA Process (PID 1185) got unhandled exception

---

### 评论 #6 — gstoner (2017-03-09T13:56:51Z)

Thanks,  you see we have this part of the Ubuntu interactions.  I will get the team to add this to the Instructions.    Tell Simon hello..

Greg


On Mar 9, 2017, at 7:22 AM, James Price <notifications@github.com<mailto:notifications@github.com>> wrote:


OK, turns out I was still booting into the regular Fedora kernel. Maybe worth a note in the ROCm installation docs that you need to change the default kernel in GRUB if working remotely?

The vector_copy sample gets further, but now hangs just after "Loading the code object succeeded". This line shows up in dmesg:

[   87.753631] kfd kfd: HSA Process (PID 1185) got unhandled exception


—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/95#issuecomment-285349787>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DufvmoLhreA4OWJ2LXIIIW-oQQ5pdks5rj_0wgaJpZM4MVyEE>.



---

### 评论 #7 — jedwards-AMD (2017-03-09T14:48:13Z)

Instructions on changing the default kernel are given here: https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#install-or-update

I can see how this is a little confusing, because it is under the Ubuntu install header, but the instruction are the same for Fedora. I will add a comment in the Fedora section that reminds users to check this.

---

### 评论 #8 — jrprice (2017-03-09T15:02:37Z)

Thanks, looks good now.

How should I go about trying to debug the hang in the `vector_copy` sample? Seems to hang with that unhandled exception as soon as it hits `hsa_executable_freeze`, and OpenCL codes have the same issue.


---

### 评论 #9 — jedwards-AMD (2017-03-09T15:10:07Z)

There is no need to debug, I know the problem. It is a defect in the microcode on Fedora 23 for Hawaii ASICs. We have a fix for it, but it hasn't been released (or tested) yet. Let me look into providing you a patch to try in the next few days.

---

### 评论 #10 — jrprice (2017-03-09T15:16:09Z)

Great, thanks!

We should hopefully be getting a Polaris GPU soon as well, so we can give that a go in the meantime.

---
