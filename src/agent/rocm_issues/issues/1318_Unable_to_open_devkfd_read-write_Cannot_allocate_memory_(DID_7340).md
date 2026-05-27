# Unable to open /dev/kfd read-write: Cannot allocate memory (DID 7340)

> **Issue #1318**
> **状态**: closed
> **创建时间**: 2020-12-03T15:54:47Z
> **更新时间**: 2021-01-04T06:46:51Z
> **关闭时间**: 2020-12-03T16:44:38Z
> **作者**: polauf1234
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1318

## 描述

When running:
```
$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
Failed to get user name to check for render group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
When i looked to dmesg:
```
$ sudo dmesg | grep kfd
[    2.244241] kfd kfd: DID 7340 is missing in supported_devices
[    2.244243] kfd kfd: kgd2kfd_probe failed
```

Info:
```
$ uname -a
Linux ... 5.4.0-54-generic #60-Ubuntu SMP Fri Nov 6 10:37:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```
On 5.4.0-56 kmod compilation gives me error. (didn't record that error and rebooted. :-1:  )

```
$ lspci | grep VGA
2f:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (rev c5)
```
I found in /usr/src/amdgpu-3.10-27/amd/amdkfd/kfd_device.c#447
```
...
static const struct kfd_device_info navi14_device_info = {
	.asic_family = CHIP_NAVI14,
	.asic_name = "navi14",
        ....
```
Maybe ID of this card is not listed?

Thanks for help.


---

## 评论 (8 条)

### 评论 #1 — ddobreff (2020-12-03T16:18:33Z)

To save support the answer:
gfx10x0 are not officially supported by ROCm :)

---

### 评论 #2 — polauf1234 (2020-12-03T16:23:23Z)

OK, unofficially?
Basically its looks that there is a support:
amdgpu_drv.c#1102	`{0x1002, 0x7340, PCI_ANY_ID, PCI_ANY_ID, 0, 0, CHIP_NAVI14},`

Can i try? (Somehow)

---

### 评论 #3 — jlgreathouse (2020-12-03T16:28:33Z)

To give a bit more detail about the specific error described here:
 - The ROCK DKMS driver (which you see in `/usr/src/amdgpu-3.10-27/` did not compile correctly on 5.4.0-56. This is a known problem, See #1307 and #1315 
- If you originally had 5.4.0-56 installed when you installed ROCm, it is likely the case that the ROCK DKMS driver did not build for 5.4.0-54. As such, your system probably falls back to using the upstream 5.4.0 driver.
- 5.4.0 KFD [does not include support for Navi 14](https://github.com/torvalds/linux/blob/v5.4/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L354).
- Navi 14 support was not added upstream until [5.5](https://github.com/torvalds/linux/blob/v5.5/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L443).

With that in mind, could you please show me the output of `dkms status`? I suspect that you will *not* see it say `amdgpu, 3.10-27, 5.4.0-54-generic, x86_64: installed`.

If so, could you please try running:
```
sudo dkms remove amdgpu/3.10-27 --all
sudo dkms add amdgpu/3.10-27
sudo dkms install amdgpu/3.10-27
```

Reboot and see what `dkms status` and `dmesg | grep kfd`  say.

---

### 评论 #4 — polauf1234 (2020-12-03T16:29:59Z)

Now:`
amdgpu, 3.10-27, 5.4.0-53-generic, x86_64: installed`

---

### 评论 #5 — jlgreathouse (2020-12-03T16:31:05Z)

So your output of `uname -r` is `5.4.0-54-generic` and the output of dkms shows `5.4.0-53-generic`? If so, yes, you do not have the DKMS module installed for your current kernel. Try the remove/add/install/ cycle.

---

### 评论 #6 — polauf1234 (2020-12-03T16:44:38Z)

Heh, yes that was in for now. (To many kernels; forgot about that.) Opencl now works. Waiting for HIP support.
Thank you for help.

---

### 评论 #7 — YuaJuan (2020-12-21T12:56:43Z)

> So your output of `uname -r` is `5.4.0-54-generic` and the output of dkms shows `5.4.0-53-generic`? If so, yes, you do not have the DKMS module installed for your current kernel. Try the remove/add/install/ cycle.

Hi,I have the same problem,but when I exec 'sudo dkms remove amdgpu/3.9-27 --all':
```
root@vegacloud:~# sudo dkms remove amdgpu/3.9-27 --all
Error! There are no instances of module: amdgpu
3.9-27 located in the DKMS tree.
```
dkms status :
```
root@vegacloud:~# dkms status
amdgpu, 3.9-17, 4.15.0-122-generic, x86_64: installed
nvidia, 450.80.02, 4.15.0-122-generic, x86_64: installed
nvidia, 450.80.02, 4.15.0-126-generic, x86_64: installed
nvidia, 450.80.02, 4.15.0-128-generic, x86_64: installed
```
So what's module'name I should write , thanks a lot.

---

### 评论 #8 — jlgreathouse (2021-01-04T06:46:51Z)

Sounds like you should do `sudo dkms remove amdgpu/3.9-17`, since that is the version you appear to have installed.

---
