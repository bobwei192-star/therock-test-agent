# MASSIVE OpenGL / WebGL performance degradation after ROCm installation

> **Issue #1239**
> **状态**: closed
> **创建时间**: 2020-09-23T17:58:16Z
> **更新时间**: 2024-01-14T03:58:38Z
> **关闭时间**: 2024-01-14T03:58:37Z
> **作者**: robinchrist
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1239

## 描述

Today I've run into a weird issue:

I'm working on an Electron application that uses three.js / WebGL.
Without ROCm installed everything's fine: The all-open amdgpu drivers provide smooth 60fps.

After installation of ROCm, however, I'm barely getting 4 (four) FPS!


Ubuntu 20.04 @ 5.4.0-48-generic
Radeon VII

Only difference I notice is that pre-ROCm, glxinfo reports `Device: AMD Radeon VII (VEGA20, DRM 3.35.0, 5.4.0-48-generic, LLVM 10.0.0) (0x66af)`, with ROCm it's `Device: AMD Radeon VII (VEGA20, DRM 3.40.0, 5.4.0-48-generic, LLVM 10.0.0) (0x66af)`

Any ideas?

NOTE: Even after installation of ROCm, Unigine Superposition runs at well over 100FPS, i.e. performance compared with pre-ROCm is the change.

---

## 评论 (17 条)

### 评论 #1 — baryluk (2020-09-23T22:33:12Z)

This doesn't look to be related to ROCm.

Maybe you messed up your Mesa installation, and it is falling back to software rasterizer.

What does this output:

`glxinfo | grep 'OpenGL version string'`

`dpkg -l libgl1-mesa-dri:amd64`

?

---

### 评论 #2 — robinchrist (2020-09-23T22:50:16Z)

Before:
glxinfo: `OpenGL version string: 4.6 (Compatibility Profile) Mesa 20.0.8`
dpkg: `ii  libgl1-mesa-dri:amd64 20.0.8-0ubuntu1~20.04.1 amd64        free implementation of the OpenGL API -- DRI modules`

Electron Application: Smooth



Install ROCm via `sudo apt install rocm-dkms && sudo reboot`
glxinfo: `OpenGL version string: 4.6 (Compatibility Profile) Mesa 20.0.8`
dpkg: `ii  libgl1-mesa-dri:amd64 20.0.8-0ubuntu1~20.04.1 amd64        free implementation of the OpenGL API -- DRI modules`

Electron Application: Unusable.



After removing ROCm via `sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils && sudo dpkg --purge rock-dkms && sudo reboot`

glxinfo: `OpenGL version string: 4.6 (Compatibility Profile) Mesa 20.0.8`
dpkg: `ii  libgl1-mesa-dri:amd64 20.0.8-0ubuntu1~20.04.1 amd64        free implementation of the OpenGL API -- DRI modules`

Electron Application: Smooth


I can repeat this cycle as often as I want (already tested about 5 times). After removing ROCm, everything works as before, the Electron application is smooth. Reinstall ROCm -> 4FPS. Remove it....

~~Another that caught my attention: Rendering bug when windows are not focused anymore. That does not happen when ROCm is not present.~~

![image](https://user-images.githubusercontent.com/22774099/94081836-d75e7100-fdff-11ea-9143-69e03301ac83.png)

**EDIT: NVM, that also happens without ROCm.**
 

---

### 评论 #3 — robinchrist (2020-09-23T23:25:44Z)

[report_good.txt](https://github.com/RadeonOpenCompute/ROCm/files/5272509/report_good.txt)
[report_bad.txt](https://github.com/RadeonOpenCompute/ROCm/files/5272510/report_bad.txt)

Electron `chrome://gpu` reports. So yes, Electron indeed falls back to software rendering. The system Chrome browser works as expected.
[chrome_rocm.txt](https://github.com/RadeonOpenCompute/ROCm/files/5272514/chrome_rocm.txt)

...but why?



---

### 评论 #4 — robinchrist (2020-09-23T23:41:43Z)

...seems like, for some reason, ROCm triggers an entry on the chromium GPU blacklist.
Adding ` --ignore-gpu-blacklist` enables GPU acceleration.

---

### 评论 #5 — robinchrist (2020-09-24T00:14:18Z)

Relevant chromium commit is `d81b8386aa656f8324959a81e3cc236c8d68adf5`
https://chromium.googlesource.com/chromium/src/+/d81b8386aa656f8324959a81e3cc236c8d68adf5%5E%21/#F0

`ROCm` identifies as `AMD (Brahma)`.

The `software_rendering_list.json` in Electron 8.0.1's chromium rev. does not contain the Brahma exception.

What's the reason for this name? 

---

### 评论 #6 — saadrahim (2020-09-25T15:06:23Z)

Where do you find ROCm identifying as AMD (Brahma)? This is likely a bug.

Please provide instructions to get that string.

---

### 评论 #7 — robinchrist (2020-09-25T15:49:08Z)

I thought I also spotted `Brahma` in glxinfo, however I was wrong. `Brahma` only occurs in the Chrome GPU info.

I have digged through the chromium source code and discovered that in their ANGLE library (it was factored out of chromium at some point), they hard set `driverVendor` to `AMD (Brahma)` if the AMD Vendor ID is detected, see https://github.com/google/angle/blob/ff0ec95b929e880ded5a835e96851219566a69f1/src/gpu_info_util/SystemInfo_linux.cpp#L96-L103

So yeah, this is, in fact, a chromium thing (or bug if you want). I don't know what's the best thing to do at this point, but it might be a good idea for AMD to speak with Google to see whether there's anything that needs to be and can be done about this. 

---

### 评论 #8 — baryluk (2020-09-25T16:27:13Z)

I looks they directly read the amdgpu module version from stars, and if
there are any letters  or dashes, in the version they assume it is
proprietary driver.

It should be easy to fix, possibly add a minimum amdgpu version instead.



---

### 评论 #9 — saadrahim (2020-09-25T16:30:27Z)

Please give me the actual strings you are seeing for amdgpu module version from stars. What is stars?

I am not very familiar with this part of Linux as I don't use a Linux desktop.

---

### 评论 #10 — baryluk (2020-09-25T16:31:07Z)

I mean from statfs.


---

### 评论 #11 — saadrahim (2020-09-25T16:32:38Z)

> 
> I mean from statfs.
> […](#)
> On Fri, 25 Sep 2020, 18:26 Witold Baryluk, ***@***.***> wrote: I looks they directly read the amdgpu module version from stars, and if there are any letters or dashes, in the version they assume it is proprietary driver. It should be easy to fix, possibly add a minimum amdgpu version instead. On Fri, 25 Sep 2020, 17:49 Robin Christ, ***@***.***> wrote: > I thought I also spotted Brahma in glxinfo, however I was wrong. Brahma > only occurs in the Chrome GPU info. > > I have digged through the chromium source code and discovered that in > their ANGLE library (it was factored out of chromium at some point), they > hard set driverVendor to AMD (Brahma) if the AMD Vendor ID is detected, > see > https://github.com/google/angle/blob/ff0ec95b929e880ded5a835e96851219566a69f1/src/gpu_info_util/SystemInfo_linux.cpp#L96-L103 > > So yeah, this is, in fact, a chromium thing (or bug if you want). I don't > know what's the best thing to do at this point, but it might be a good idea > for AMD to speak with Google to see whether there's anything that needs to > be and can be done about this. > > — > You are receiving this because you commented. > Reply to this email directly, view it on GitHub > <[#1239 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1239#issuecomment-699006303)>, > or unsubscribe > <https://github.com/notifications/unsubscribe-auth/AAA254RWVYNXLD2GMXP2NGDSHS3YJANCNFSM4RXKYDPA> > . >

Send me the outputs so that I can identify which part of rocm it is. Seems like a simple fix if I can get the offending line in a rocm repository.

---

### 评论 #12 — baryluk (2020-09-25T16:43:47Z)

https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L97

says:

```c
#define AMDGPU_VERSION		"5.6.15"
...
...
MODULE_VERSION(AMDGPU_VERSION);
```


so this should work and be normal in `/sys/module/amdgpu/version`

Maybe the dkms code is slightly modified to the the tree there.

The Chromium / ANGLE parsing code is here:

https://chromium.googlesource.com/angle/angle/+/refs/heads/master/src/gpu_info_util/SystemInfo_linux.cpp#42

https://chromium.googlesource.com/angle/angle/+/refs/heads/master/src/gpu_info_util/SystemInfo.cpp#163

```c
bool ParseAMDBrahmaDriverVersion(const std::string &content, std::string *version)
{
    const size_t begin = content.find_first_of("0123456789");
    if (begin == std::string::npos)
    {
        return false;
    }
    const size_t end = content.find_first_not_of("0123456789.", begin);
    if (end == std::string::npos)
    {
        *version = content.substr(begin);
    }
    else
    {
        *version = content.substr(begin, end - begin);
    }
    return true;
}
```

I don't use the dkms driver from rocm, so I can't check what it says exactly.

@robinchrist  Please provide content of `/sys/module/amdgpu/version` when the rocm-dkms is installed (you probably need a reboot after install).


On semi-vanilla kernel (Debian testing, 5.7.6-1), it doesn't even exist:

```
$ sudo modinfo amdgpu | grep version
vermagic:       5.7.0-1-amd64 SMP mod_unload modversions 
$ sudo cat /sys/module/amdgpu/version
cat: /sys/module/amdgpu/version: No such file or directory
$
```


nor is says "amdgpu version" in dmesg:

```
$ grep amdgpu  /var/log/kern.log   | grep version
$
```

This is probably because of this piece:

https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/commit/5ffc9d9d589b8d14b77d47bdedbe3afcc7e21146

which is not upstreamed , thus making behavior different.


---

### 评论 #13 — baryluk (2020-09-25T16:51:05Z)

I was wrong in saying "it assumes it is propietery driver" if there are no-digits detected.

In fact it assumes it is propietary driver, if the `/sys/module/amdgpu/version` exists, and contains any numbers. The returned version is stripped from non-digit suffix for consumption later in the stack. But mare presence is enough to trigger the logic.


---

### 评论 #14 — baryluk (2020-11-23T17:40:59Z)

@robinchrist Did you have time to report this issue to chromium developers?

---

### 评论 #15 — ROCmSupport (2021-01-05T07:39:39Z)

Hi @robinchrist 
Is this issue is still observed with ROCm 4.0? Can you please check and confirm.
Thank you.

---

### 评论 #16 — ROCmSupport (2021-03-01T08:34:24Z)

Hi @robinchrist 
Can you please respond by trying it on ROCm 4.0.
Else request you to close this issue if not reproducible.
Thank you.

---

### 评论 #17 — nartmada (2024-01-14T03:58:37Z)

Closing this ticket as there is no response from @robinchrist.  If the issue still exists with latest ROCm6.0.0, please re-open the ticket.  Thanks.

---
