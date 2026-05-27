# Driver not building on Ubuntu 18.04 with kernel 4.18

> **Issue #731**
> **状态**: closed
> **创建时间**: 2019-03-13T09:37:20Z
> **更新时间**: 2019-05-03T16:03:23Z
> **关闭时间**: 2019-05-03T16:03:23Z
> **作者**: sebpuetz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/731

## 负责人

- kentrussell

## 描述


My system is running Ubuntu 18.04 with default kernel (4.18), previously it ran fine on ROCm 2.1. Today I upgraded to ROCm 2.2 through apt and ROCK-dkms fails to build:

```
sudo apt install rocm-dkms
.
.
.
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.crash'
Error! Bad return status for module build on kernel: 4.18.0-16-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.2-31/build/make.log for more information.
```

My GPU is a Radeon VII.
I tried reinstalling by following the instructions provided in the README.md, but to no avail. Downgrading doesn't appear to be an option as 2.1 doesn't seem to be in the apt repo anymore?

_edit:_ Attached the log file of the failing build.
[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2960792/make.log)


---

## 评论 (9 条)

### 评论 #1 — sebpuetz (2019-03-14T00:57:24Z)

Seems like someone else is running into issues on 4.18, too: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/345#issuecomment-472641875

I upgraded to kernel 5.0 to get rid of software rendering mode, which in turn leads to a performance regression as described in: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/329

_edit:_ Downgrading to 4.15 also fixes the issue, failing build seems to be related to 4.18.

---

### 评论 #2 — kentrussell (2019-03-14T10:02:29Z)

This is a known issue with 2.2 with the 4.18 kernel. The fix will be included in 2.3. For now, you'll need to stick with the upstream kernel, or downgrade to 4.15. I have updated the documentation at https://github.com/RadeonOpenCompute/ROCm/pull/736 to clarify this. Thanks for the bug report. I'll leave it open until 2.3 so that other users can hopefully find it
You can also build the kernel yourself from the ROCK github code tree (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) and install that instead of using the DKMS package, as it's just the DKMS package that has the issue (the monolithic kernel works, and is based on 4.18).
(Copy/pasting because it's the same response, hopefully other users find one of these Issue Reports to save some time/effort/sanity) . 

---

### 评论 #3 — JMadgwick (2019-03-15T14:57:57Z)

Fortunately for me I have seen this issue before upgrading my rocm installation to 2.2.
The Readme needs the "Using AMD's rock-dkms package" Table updating, it still says:
> Not currently supported on kernels newer than 4.18

The AMD subreddit had a number of users with a similar problem because they had apt updates installing automatically which installed 4.18 along with ROCm 2.2, braking their systems.
I am on 4.18 and the easiest way to avoid this problem (while being able to update other packages) is by temporarily disabling the ROCm repo. This will prevent ROCm packages from updating automatically without needing to put a hold on every single package. If I need to upgrade to 2.2 then I will build the ROCK kernel.

---

### 评论 #4 — sebpuetz (2019-03-17T17:28:07Z)

Oddly enough, the upstream kernel doesn't seem to work right away, either? I had to re-install Ubuntu today and neither of the 5.0.x kernels got me out of software rendering mode. I then tried installing 4.15 and getting the driver through `apt install rocm-dkms` which gave me a functioning driver for that kernel.

After getting 4.15 to work, I unintenionally booted into the upstream kernel 5.0.1 and ended up with a working driver there, too. Although during installation of `rocm-dkms` on 4.15 I got the expected error message that building `rock-dkms` failed for kernel 5.01, it now works for some reason. 

---

### 评论 #5 — JishinMaster (2019-03-18T16:24:43Z)

Hi,

I have had the same problem.
Everything was working great with RoCM-2.1 on Ubuntu18.04, kernel 4.18.0-16.
After an apt upgrade, switching to RoCM-2.2 broke amdkfd.

I have found a patch to this problem (with help from this post : https://github.com/RadeonOpenCompute/ROCm/issues/719) :
dkms status -> gives me "amdgpu 2.2.31"
sudo dkms remove amdgpu/2.2.31 --all
sudo dkms add amdgpu/2.2.31
sudo dkms install amdgpu/2.2.31 will fail because it cannot find pcie_get_speed_cap and pcie_get_width_cap (lines 3653 and 3654).
You need to add "kcl_" to those lines in /var/lib/dkms/amdgpu/2.2-31/source/amd/amdgpu/amdgpu_device.c
Then you can do : sudo dkms install amdgpu/2.2.31
After a reboot everything was working.

---

### 评论 #6 — alexpattyn (2019-04-03T23:50:29Z)

I've just built a new system with a Ryzen 5 2400G and a Radeon VII and wanted to ask if there is a workaround to getting ROCm 2.2 working on Ubuntu 18.04 with the 4.18 kernel? I've tried 4.15 but then my system doesn't have internet (MSI B450 Ethernet port doesn't work with 4.15) and neither the Radeon or integrated graphics work on that kernel (everything is just outputted to a lower resolution and is slow to render). I've tried to use AMDGPU-PRO just so I can have OpenCL working but that has issues on the 4.18 kernel as well. 

Am I just going to have to wait until ROCm 2.3 comes out?  

Edit: I should also add I tried the OpenCL only install of ROCm 2.2 and still no luck.

---

### 评论 #7 — JMadgwick (2019-04-04T07:42:40Z)

Everything you need to know [is in this post further up](https://github.com/RadeonOpenCompute/ROCm/issues/731#issuecomment-472782999).

> You can also build the kernel yourself from the ROCK github code tree (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) and install that instead of using the DKMS package, as it's just the DKMS package that has the issue (the monolithic kernel works, and is based on 4.18).

It looks like that is the only fix for now, 2.3 will likely be out quite soon though.

---

### 评论 #8 — Djip007 (2019-05-01T22:42:56Z)

In fact for koenigjaeger it is a more complicate because off is Ryzen 5 2400G with is APU with VEGA gpu...
cf: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-450692695
may be he can desactivate de VEGA GPU... (I can't on my laptop;))

---

### 评论 #9 — sebpuetz (2019-05-03T16:03:23Z)

Closing this, as the problem was resolved with the new version.

---
