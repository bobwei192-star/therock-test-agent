# System fails to boot after upgrading to ROCm 2.2

> **Issue #735**
> **状态**: closed
> **创建时间**: 2019-03-14T04:29:36Z
> **更新时间**: 2019-03-14T23:48:12Z
> **关闭时间**: 2019-03-14T23:15:23Z
> **作者**: SandboChang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/735

## 描述

Hi,

First of all, my system is:
-AMD Threadripper 1950X
-Vega FE*2 + Radeon VII
-ubuntu 18.04, kernel 4.18.0-16-generic

I just upgraded to ROCm 2.2, unfortunately that was done with apt upgrade so there are other items, thus I don't mean to be conclusive.

After the upgrade, I found the system failed to boot. I entered grub and tried to remove quiet splash to see through the log, unfortunately it froze at different point everytime, will all lines being shown saying "OK" in green.
Then, I followed some online guides to add "nomodeset" to grub, with that the systems boots normally. However, it doesn't load the GPUs in the kernel and I can't see them in clinfo anymore nor using them.

The new kernel 4.18.0-16 was installed on 03-07 and a reboot was done on 03-11 without any issues, so I assumed that wasn't the cause.
I tried to use autoremove to remove rocm, but the problem persists (after removal, still only nomodeset allows the system to boot). Could that be still related to ROCm? It would be great if you can confirm if the removal should have got rid of the cause, I shall forward this issue elsewhere.

The below is a list of upgrades installed on 2019-03-13, in case anything looked fishy, unfortunately it's quite long.

```
Start-Date: 2019-03-13  22:28:08
Commandline: apt upgrade
Requested-By: sandbo (1000)
Upgrade: hsa-rocr-dev:amd64 (1.1.9-49-g39f1af5, 1.1.9-55-gbac2a9b), 
libxcb-present-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
hsakmt-roct-dev:amd64 (1.0.9-111-gc65f2de, 1.0.9-121-g876627e), 
libseccomp2:amd64 (2.3.1-2.1ubuntu4, 2.3.1-2.1ubuntu4.1), 
hsakmt-roct:amd64 (1.0.9-111-gc65f2de, 1.0.9-121-g876627e), 
virtinst:amd64 (1:1.5.1-0ubuntu1.1, 1:1.5.1-0ubuntu1.2), 
libxcb-xfixes0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rock-dkms:amd64 (2.1-96, 2.2-31), 
rocm-opencl:amd64 (1.2.0-2019020110, 1.2.0-2019030702), 
libsystemd0:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libsystemd0:i386 (237-3ubuntu10.13, 237-3ubuntu10.15), 
hip_base:amd64 (1.5.19025, 1.5.19055), 
libxcb-present0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-present0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
hsa-ext-rocr-dev:amd64 (1.1.9-49-g39f1af5, 1.1.9-55-gbac2a9b), 
libxcb-xfixes0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocrand:amd64 (1.8.2, 1.8.2), rocfft:amd64 (0.8.9.0, 0.9.0.0), 
google-chrome-stable:amd64 (72.0.3626.121-1, 73.0.3683.75-1), 
hcc:amd64 (1.3.19045, 1.3.19092), 
udev:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-shm0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shm0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-randr0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-render0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-render0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libudev1:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libudev1:i386 (237-3ubuntu10.13, 237-3ubuntu10.15), 
comgr:amd64 (1.1.0, 1.1.0), 
libtiff5:amd64 (4.0.9-5ubuntu0.1, 4.0.9-5ubuntu0.2), 
libtiff5:i386 (4.0.9-5ubuntu0.1, 4.0.9-5ubuntu0.2), 
libxcb-randr0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri3-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb1:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shape0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libnss-myhostname:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-res0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-libs:amd64 (2.1.96, 2.2.31), 
systemd-sysv:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
rocm-dev:amd64 (2.1.96, 2.2.31), 
libxcb-xv0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-utils:amd64 (2.1.96, 2.2.31), 
libpam-systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
libxcb-render0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-shape0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
virt-manager:amd64 (1:1.5.1-0ubuntu1.1, 1:1.5.1-0ubuntu1.2), 
systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
hip_doc:amd64 (1.5.19025, 1.5.19055), 
libnss-systemd:amd64 (237-3ubuntu10.13, 237-3ubuntu10.15), 
miopen-hip:amd64 (1.7.1, 1.7.1), 
rocm-device-libs:amd64 (0.0.1, 0.0.1), 
hip_hcc:amd64 (1.5.19025, 1.5.19055), 
rocm-opencl-dev:amd64 (1.2.0-2019020110, 1.2.0-2019030702), 
hip_samples:amd64 (1.5.19025, 1.5.19055), 
libxcb-sync-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
cxlactivitylogger:amd64 (5.6.7254, 5.6.7259), 
libxcb-dri2-0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-glx0-dev:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
rocprofiler-dev:amd64 (1.0.0, 1.0.0), 
libxcb-dri2-0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri2-0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-smi:amd64 (1.0.0-100-g3cacdb9, 1.0.0-102-gdb444a9), 
libxcb-dri3-0:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-dri3-0:i386 (1.13-1, 1.13-2~ubuntu18.04), 
rocm-dkms:amd64 (2.1.96, 2.2.31), 
libxcb-xkb1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-sync1:amd64 (1.13-1, 1.13-2~ubuntu18.04), 
libxcb-sync1:i386 (1.13-1, 1.13-2~ubuntu18.04)
End-Date: 2019-03-13  22:29:28

```

---

## 评论 (13 条)

### 评论 #1 — MichaelEssich (2019-03-14T09:20:51Z)

Same here.
Upgraded to ROCm 2.2 and after that the system won't boot.

System:
Vega 56, Ryzen 2600, Ubuntu 18.04 with Kernel 4.18.0-16-generic

Upgraded packages:
```
code/stable 1.32.2-1552488294 amd64 [aktualisierbar von: 1.32.1-1552006243]
comgr/Ubuntu 16.04 1.1.0 amd64 [aktualisierbar von: 1.1.0]
cxlactivitylogger/Ubuntu 16.04 5.6.7259 amd64 [aktualisierbar von: 5.6.7254]
evolution-ews/bionic-updates 3.28.5-0ubuntu0.18.04.1 amd64 [aktualisierbar von: 3.28.1-1]
hcc/Ubuntu 16.04 1.3.19092 amd64 [aktualisierbar von: 1.3.19045]
hip_base/Ubuntu 16.04 1.5.19055 amd64 [aktualisierbar von: 1.5.19025]
hip_doc/Ubuntu 16.04 1.5.19055 amd64 [aktualisierbar von: 1.5.19025]
hip_hcc/Ubuntu 16.04 1.5.19055 amd64 [aktualisierbar von: 1.5.19025]
hip_samples/Ubuntu 16.04 1.5.19055 amd64 [aktualisierbar von: 1.5.19025]
hsa-ext-rocr-dev/Ubuntu 16.04 1.1.9-55-gbac2a9b amd64 [aktualisierbar von: 1.1.9-49-g39f1af5]
hsa-rocr-dev/Ubuntu 16.04 1.1.9-55-gbac2a9b amd64 [aktualisierbar von: 1.1.9-49-g39f1af5]
hsakmt-roct/Ubuntu 16.04 1.0.9-121-g876627e amd64 [aktualisierbar von: 1.0.9-111-gc65f2de]
hsakmt-roct-dev/Ubuntu 16.04 1.0.9-121-g876627e amd64 [aktualisierbar von: 1.0.9-111-gc65f2de]
libnss-myhostname/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
libnss-systemd/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
libpam-modules/bionic-updates 1.1.8-3.6ubuntu2.18.04.1 amd64 [aktualisierbar von: 1.1.8-3.6ubuntu2]
libpam-modules-bin/bionic-updates 1.1.8-3.6ubuntu2.18.04.1 amd64 [aktualisierbar von: 1.1.8-3.6ubuntu2]
libpam-runtime/bionic-updates,bionic-updates 1.1.8-3.6ubuntu2.18.04.1 all [aktualisierbar von: 1.1.8-3.6ubuntu2]
libpam-systemd/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
libpam0g/bionic-updates 1.1.8-3.6ubuntu2.18.04.1 amd64 [aktualisierbar von: 1.1.8-3.6ubuntu2]
libseccomp2/bionic-updates 2.3.1-2.1ubuntu4.1 amd64 [aktualisierbar von: 2.3.1-2.1ubuntu4]
libsystemd0/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
libudev1/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
libxcb-dri2-0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-dri3-0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-glx0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-present0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-randr0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-render0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-res0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-shape0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-shm0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-sync1/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-xfixes0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-xinerama0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-xkb1/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb-xv0/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb1/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
libxcb1-dev/bionic-updates 1.13-2~ubuntu18.04 amd64 [aktualisierbar von: 1.13-1]
miopen-hip/Ubuntu 16.04 1.7.1 amd64 [aktualisierbar von: 1.7.1]
rocblas/Ubuntu 16.04 2.0.1.0 amd64 [aktualisierbar von: 2.0.1.0]
rocfft/Ubuntu 16.04 0.9.0.0 amd64 [aktualisierbar von: 0.8.9.0]
rock-dkms/Ubuntu 16.04 2.2-31 all [aktualisierbar von: 2.1-96]
rocm-dev/Ubuntu 16.04 2.2.31 amd64 [aktualisierbar von: 2.1.96]
rocm-device-libs/Ubuntu 16.04 0.0.1 amd64 [aktualisierbar von: 0.0.1]
rocm-dkms/Ubuntu 16.04 2.2.31 amd64 [aktualisierbar von: 2.1.96]
rocm-libs/Ubuntu 16.04 2.2.31 amd64 [aktualisierbar von: 2.1.96]
rocm-opencl/Ubuntu 16.04 1.2.0-2019030702 amd64 [aktualisierbar von: 1.2.0-2019020110]
rocm-opencl-dev/Ubuntu 16.04 1.2.0-2019030702 amd64 [aktualisierbar von: 1.2.0-2019020110]
rocm-smi/Ubuntu 16.04 1.0.0-102-gdb444a9 amd64 [aktualisierbar von: 1.0.0-100-g3cacdb9]
rocm-utils/Ubuntu 16.04 2.2.31 amd64 [aktualisierbar von: 2.1.96]
rocprofiler-dev/Ubuntu 16.04 1.0.0 amd64 [aktualisierbar von: 1.0.0]
rocrand/Ubuntu 16.04 1.8.2 amd64 [aktualisierbar von: 1.8.2]
systemd/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
systemd-sysv/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
udev/bionic-updates 237-3ubuntu10.15 amd64 [aktualisierbar von: 237-3ubuntu10.13]
```

I had no time to remove quiet splash and analyze output and just restored a backup right before installing updates. If needed, I can do the upgrade again later and report the output without quiet splash.

---

### 评论 #2 — kentrussell (2019-03-14T10:03:17Z)

This is a known issue with 2.2 with the 4.18 kernel. The fix will be included in 2.3. For now, you'll need to stick with the upstream kernel, or downgrade to 4.15. I have updated the documentation at https://github.com/RadeonOpenCompute/ROCm/pull/736 to clarify this. Thanks for the bug report. I'll leave it open until 2.3 so that other users can hopefully find it
You can also build the kernel yourself from the ROCK github code tree (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) and install that instead of using the DKMS package, as it's just the DKMS package that has the issue (the monolithic kernel works, and is based on 4.18).
(Copy/pasting because it's the same response, hopefully other users find one of these Issue Reports to save some time/effort/sanity) . 

---

### 评论 #3 — SandboChang (2019-03-14T13:51:58Z)

Thanks Kent for the clarification.
I did spend some time trying to solve it without success, including booting with 4.15. Interestingly though, with 4.15 I saw an actual error saying 
`[FAILED] Failed to start User Manager for UID 120`
and this kept on repeating till like session c17.

Searching the web, it seems to be related to a bug with Wayland/GDM3 with some GPUs:
https://askubuntu.com/questions/1036242/17-10-to-18-04-upgrade-freezes-during-boot (see update 7)

The mistake I then made was I assumed the error applied also to 4.18, so I disabled Wayland and only tried to boot with 4.18. I will try later today to boot again with 4.15 with Wayland disabled.

If nothing works, I may have to either reinstall (should have backed up) or wait for 2.3, but I believe the latter will take a while.


---

### 评论 #4 — jlgreathouse (2019-03-14T14:48:47Z)

It's possible that when you updated to kernel 4.18 and installed ROCm, the `rock-dkms` module only attempted to build for the most up-to-date kernel (4.18). As such, when you boot into 4.15 (e.g. if you're just choosing that as a Grub option) you also do not have a `rock-dkms` module loaded.

If you can get to a command prompt, can you run `dkms status`?

---

### 评论 #5 — SandboChang (2019-03-14T15:18:13Z)

Hello Joseph,

That's a good point, I will try later when I get home (it can get stuck and I have no way to reset the server remotely, so I'd better let it stay at 4.18 with nomodeset for now).
On 4.18 where I reinstalled rocm (after the removal), it now shows 
`amdgpu, 2.2-31: added`

I will test again after I have switched to 4.15.

---

### 评论 #6 — jlgreathouse (2019-03-14T15:23:32Z)

Based on your output, yes, the `rock-dkms` driver is not being loaded even for your older kernel. Do you have 4.15 _installed_on your system? e.g. what is the output of `ls /boot/vmlinuz-*`?

If you have 4.15 installed, you could at least try running:
```
sudo dkms build amdgpu/2.2-31 -k {4.15 kernel number}
sudo dkms install amdgpu/2.2-31 -k {4.15 kernel number}
```

For example, if your highest 4.15 kernel is 4.15.0-45-generic, you could run:
```
sudo dkms build amdgpu/2.2-31 -k 4.15.0-45-generic
sudo dkms install amdgpu/2.2-31 -k 4.15.0-45-generic
```

You can do this even if you're currently booted into 4.18 (it doesn't make any modifications to 4.18).
If you then see `dkms status` show that you have amdgpu "installed" for that kernel, then you should be able to boot into 4.15.0-45-generic and have the amdgpu driver load.

---

### 评论 #7 — SandboChang (2019-03-14T16:05:35Z)

> Based on your output, yes, the `rock-dkms` driver is not being loaded even for your older kernel. Do you have 4.15 _installed_on your system? e.g. what is the output of `ls /boot/vmlinuz-*`?
> 
> If you have 4.15 installed, you could at least try running:
> 
> ```
> sudo dkms build amdgpu/2.2-31 -k {4.15 kernel number}
> sudo dkms build amdgpu/2.2-31 -k {4.15 kernel number}
> ```
> For example, if your highest 4.15 kernel is 4.15.0-45-generic, you could run:
> 
> ```
> sudo dkms build amdgpu/2.2-31 -k 4.15.0-45-generic
> sudo dkms build amdgpu/2.2-31 -k 4.15.0-45-generic
> ```
> You can do this even if you're currently booted into 4.18 (it doesn't make any modifications to 4.18).
> If you then see `dkms status` show that you have amdgpu "installed" for that kernel, then you should be able to boot into 4.15.0-45-generic and have the amdgpu driver load.

Having done this in 4.18, it now prints
`amdgpu, 2.2-31, 4.15.0-46-generic, x86_64: built`

That probably was the cause why 4.15 failed to boot.
I will try to boot into 4.15 once I have a chance, thanks a lot for your advice.

---

### 评论 #8 — jlgreathouse (2019-03-14T16:06:52Z)

Oops. My post was wrong. For the second command, could you run `sudo dkms install` instead of `sudo dkms build`. I didn't mean to type `build` twice.

---

### 评论 #9 — SandboChang (2019-03-14T16:13:16Z)

> Oops. My post was wrong. For the second command, could you run `sudo dkms install` instead of `sudo dkms build`. I didn't mean to type `build` twice.

right, now it shows
`amdgpu, 2.2-31, 4.15.0-46-generic, x86_64: installed`
LOL, I was wondering why it was run twice, but sometimes weird thing happens and it wasn't uncommon.

---

### 评论 #10 — jlgreathouse (2019-03-14T16:17:54Z)

Great, thanks for the prompt response. I apologize for my typos before.

I think that now if you boot into 4.15.0-46 it should work. We'll see. :)

---

### 评论 #11 — SandboChang (2019-03-14T22:47:08Z)

> Great, thanks for the prompt response. I apologize for my typos before.
> 
> I think that now if you boot into 4.15.0-46 it should work. We'll see. :)

Just want to report that you saved the day! 
I re-enabled Wayland believing it was OK, then I was able to boot into 4.15 without nomodeset.
Running some tests with OpenCL and all are well..

So the cause for the error `[FAILED] Failed to start User Manager for UID 120` was indeed the `rocm-dkms` was not correctly installed on 4.15 when I upgrade `rocm` on 4.18. 

---

### 评论 #12 — jlgreathouse (2019-03-14T23:15:23Z)

Cool, glad we were able to get that worked out.

If you don't mind, I'll close this issue then. The original problem is that 4.18 does not work with ROCm 2.1 or 2.2 at this time, as indicated by @kentrussell .  However, we are also tracking that issue in #731. As such, to prevent duplicates, I'll close this and point any 4.18 users to watch that issue.

I was leaving this one open today since you had a second problem (the 4.15 `rocm-dkms` thing). :)

---

### 评论 #13 — SandboChang (2019-03-14T23:48:11Z)

Sure, thanks for the help. Please kindly  considered this solved. 

---
