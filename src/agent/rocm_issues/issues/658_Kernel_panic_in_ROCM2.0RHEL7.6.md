# Kernel panic in ROCM2.0/RHEL7.6

> **Issue #658**
> **状态**: closed
> **创建时间**: 2019-01-02T22:26:20Z
> **更新时间**: 2023-12-12T19:15:58Z
> **关闭时间**: 2023-12-12T19:15:58Z
> **作者**: sdh4
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/658

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Boot failure after installing ROCM on RHEL7.6 (Radeon Pro WX 5100).
Get a kernel oops (paging failure) inside kfree() in amdgpu_driver_postclose_kms() and (perhaps) amdgpu_vm_fini(). 

Symptoms: 
- Multiple "missing firmware" messages on install (attached) 
[rocminstall.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722233/rocminstall.txt)
- Kernel messages from boot (captured via netconsole) (attached)
[netconsole_boot.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722241/netconsole_boot.txt)
- Kernel messages from running rocminfo from single user mode (attached)
[netconsole_rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722245/netconsole_rocminfo.txt)
- Kernel messages from running clinfo from single user mode (attached)
[netconsole_clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722246/netconsole_clinfo.txt)



 

---

## 评论 (9 条)

### 评论 #1 — jlgreathouse (2019-01-02T22:53:15Z)

The missing firmware messages should not be a problem. These are known missing -- either older GPUs that we don't support, or newer GPUs that are not yet supported in ROCm. Your Polaris 10 firmware is not in the list of missing firmware.

Could you describe your hardware and software setup? Are you running in a virtual machine? Do you have PCIe Large BAR (a.k.a. "Above 4G Decoding") enabled in your BIOS? Do you have more than one GPU?

I see that it takes 2 minutes for this problem to appear in your `netconsole_boot.txt` log. Are you running any software in that time, or is this just sitting at a console?

---

### 评论 #2 — sdh4 (2019-01-03T04:13:10Z)

This is running directly (no virtualization) on a  GIGABYTE MZ31-AR0-00 with an AMD EPYC 7351P. 
The system has a ton of hardware attached -- framegrabber, data acquisition, some of which is in an external PCI chassis, etc. There is no second GPU, but there is a motherboard VGA device which is not disableable in the bios :
`43:00.0 VGA compatible controller: ASPEED Technology, Inc. ASPEED Graphics Family (rev 41) (prog-if 00 [VGA controller])`
I have it disabled by binding it to the pci-stub driver on the kernel command line. 

I am 100% confident that Above 4G decoding is enabled in the BIOS.  lspci for the Radeon card shows `Memory at 14400000000 (64-bit, prefetchable) [size=8G]`, which wouldn't be possible without above 4G decoding, no?  In any case I can double check tomorrow when I have physical access. 

The Radeon graphics card works fine using the RedHat supplied graphics drivers built into rhel 7.6 (with xorg.conf configured to ignore the ASPEED device). ROCM 1.8 worked fine on this same config with RHEL7.5: The RH drivers for graphics and ROCM for compute. 

I have never had any luck with the AMD proprietary drivers on this HW -- presumably because of the ASPEED device that cannot be turned off. 

The 2 minute delay shown in netconsole_boot.txt comes from booting as single user, manually configuring netconsole, and then pressing ctrl-d to continue the boot. 

Manually starting X.org from single user mode seems to give a working 2D X display. I haven't messed with it a lot (just run an xterm in it). From the crash dump, I'm pretty sure the crash is coming from /usr/libexec/gnome-session-check-accelerated -- which would make sense that the problem starts when it  starts direct rendering. 

Looks a bit like a free-twice or memory corruption bug... not pleasant to troubleshoot or fix unfortunately... especially without valgrind. 

p.s. the content of register RCX in 2 of the 3 dumps looks suspicious to me. 

---

### 评论 #3 — dreitzle (2019-01-22T15:22:53Z)

I might be affected by the same issue. This happens on a machine with 2x Xeon E5-2640v4, 8x R9 Nano and also a ASPEED VGA device running CentOS 7.6 and ROCM 2.0.
The ASPEED device is used for output (no X) and the R9s for compute. The machine seems to boot fine, but freezes as soon as rocminfo, clinfo or any other openCL program is executed. I managed to capture the oops via netconsole and it looks very similar to the ones reported above:
[rocm_panic.txt](https://github.com/RadeonOpenCompute/ROCm/files/2783377/rocm_panic.txt)

dmesg after boot and output of lshw -c video:
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2783358/dmesg.txt)
[video.txt](https://github.com/RadeonOpenCompute/ROCm/files/2783362/video.txt)


Update:
amdgpu-pro 18.50 also crashes. Attaching dmesg after boot and oops:
[amdgpu-panic.txt](https://github.com/RadeonOpenCompute/ROCm/files/2792592/amdgpu-panic.txt)
[dmesg2.txt](https://github.com/RadeonOpenCompute/ROCm/files/2792594/dmesg2.txt)
I hadn't noticed before since i switched to ROCM along the update from CentOS 7.5 to 7.6.
On CentOS 7.5 i used amdgpu-pro (up to) 18.30, which worked as expected.

So is this the right place for this? Or should i report it somewhere else?

Update2:
Still happens with ROCM 2.1. Blacklisting the ast driver does not help.
Any news on this?

---

### 评论 #4 — sdh4 (2019-02-08T22:25:17Z)

For me with ROCM2.1 I am no longer getting the kernel panic, but ROCM isn't working either.  rocminfo output looks normal [rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2847092/rocminfo.txt), but clinfo (including the version in /opt/rocm/opencl/bin/) segfaults
inside /opt/rocm/opencl/lib/x86_64/libamdocl64.so

If it would be helpful I could provide a core dump. Or a better stac.k trace if you can point me to the proper debuginfo.

---

### 评论 #5 — kentrussell (2019-06-07T12:18:59Z)

The kernel oops should be addressed in 2.5. If rocminfo is working correctly, that points to an issue with OpenCL. You might get a bit more traction if you post the bug in their repo (https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime) 

---

### 评论 #6 — dreitzle (2019-06-12T15:43:41Z)

Thank you. I tried 2.5 and i don't see the oops any more.
It still does't work, but that seems to be a different issue.

---

### 评论 #7 — tasso (2023-12-11T17:13:05Z)

Is this still an issue? If not, can we please close it?

---

### 评论 #8 — sdh4 (2023-12-12T19:10:26Z)

No longer have the ability to check. Go ahead and close.

Thanks,

Steve 
On Mon, 2023-12-11 at 09:13 -0800, Tasso wrote:
> Is this still an issue? If not, can we please close it?
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>

-- 
Stephen D. Holland
Professor
Department of Aerospace Engineering
Iowa State University
http://thermal.cnde.iastate.edu
***@***.***




---

### 评论 #9 — tasso (2023-12-12T19:15:57Z)

Thanks Steve!


---
