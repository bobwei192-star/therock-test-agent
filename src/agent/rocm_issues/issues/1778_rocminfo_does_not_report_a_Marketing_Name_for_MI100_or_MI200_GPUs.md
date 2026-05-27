# rocminfo does not report a "Marketing Name" for MI100 or MI200 GPUs

> **Issue #1778**
> **状态**: closed
> **创建时间**: 2022-08-04T17:13:00Z
> **更新时间**: 2024-05-09T16:21:32Z
> **关闭时间**: 2024-05-09T16:21:32Z
> **作者**: bigtrak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1778

## 负责人

- saadrahim

## 描述

I earlier reported an issue with HIP (to the HIP group) that HIP was not returning device
properties for some GPU models.

I recalled an earlier issue with rocminfo not reporting the "Marketing Name" (human readable
GPU name) for some GPUs.

Upon examining this issue again, the same GPUs (MI100, MI200) which do not report a marketing name
via rocminfo, also do not report the device name at the HIP level.

Marketing Name is reported for an MI25.  I don't have an MI50 or MI60 to test behavior on those models.

The repeater is to run rocminfo (5.2.0 version is latest, with corresponding amdgpu driver on enterprise
linux 8 (or SLES)) and observe that "Marketing Name" is blank for MI100 and MI200, and populated for MI25.

---

## 评论 (15 条)

### 评论 #1 — al42and (2022-09-16T12:03:23Z)

Can confirm the same issue for MI50 and Radeon RX6600

Update Dec 2023:

- ROCm 5.7 + RX6400, 6.2.0-37-generic kernel: "AMD Radeon RX 6400" :heavy_check_mark: 

- ROCm (5.3.0, 5.4.1, 5.6.0) + MI50 (Vega 20), 5.15.0-56-generic kernel: "" :x: 

- ROCm (5.2.3, 5.3.3) + MI250X, 5.14.21-150400.24.81_12.0.75-cray_shasta_c kernel: "" :x: 

Related to https://gitlab.freedesktop.org/mesa/drm/-/commit/613cc945b36e7ba3ce8de0e42b5057b32bc7c69c not being ported, perhaps?

---

### 评论 #2 — milthorpe (2023-12-10T23:19:16Z)

Also confirming that `hipGetDeviceProperties` does not return a value for `hipDeviceProp_t.name` for MI250X (OLCF Frontier) with either ROCM/5.4.0 or ROCM/5.7.0.

ROCM/5.4.0 also does not return a device name for MI60.

In contrast, `hipDeviceProp_t.name` is correctly returned by ROCM/5.4.0 for a Vega 20 as "AMD Radeon VII" and for MI100 as "AMD Instinct MI100".

---

### 评论 #3 — nartmada (2023-12-19T02:50:36Z)

Can you guys please try the latest ROCm 6.0.0 to see if your issue has been resolved ?  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — al42and (2023-12-19T13:48:13Z)

@nartmada:

ROCm 6.0.0 and MI50, 5.15.0-91-generic kernel.

- `rocminfo`: "Marketing name" is still empty.

- `rocm-smi` now tries to show the name, but trims it down to "deon Instinct MI50" (admittedly, the best way to trim the string in this case).

---

### 评论 #5 — nartmada (2023-12-19T14:19:36Z)

Hi @al42and, thanks for your response.  Let me check with the internal team on your finding and will get back to you.  Thanks.

---

### 评论 #6 — kzhuravl (2023-12-19T15:58:20Z)

Should go to runtime, not compiler. Saad, please reassign.

---

### 评论 #7 — dayatsin-amd (2023-12-19T19:07:03Z)

This information comes from package: libdrm-amdgpu. @bigtrak @al42and @milthorpe, can you please check that you have a recent version of libdrm-amdgpu installed.

libdrm usually stores this information here:
/opt/amdgpu/share/libdrm/amdgpu.ids

---

### 评论 #8 — al42and (2023-12-19T19:25:02Z)

@dayatsin-amd

> This information comes from package: libdrm-amdgpu.

I cannot find this package in ROCm repos and the file does not exist neither in Ubuntu nor on HPE/Cray systems. There is `/usr/share/libdrm/amdgpu.ids` file, but the only "Instinct" GPU it contains is MI25. I checked Ubuntu 22.04 (with HWE kernel), Ubuntu 20.04, and HPE/Cray stack (based on SLES 15).

The Ubuntu 22.04 version seems to correspond to https://gitlab.freedesktop.org/mesa/drm/-/commit/e214a6a6e88610aed09a046aac23e61430b76975, the HPE/Cray has an even older version.

---

### 评论 #9 — dayatsin-amd (2023-12-19T19:52:41Z)

It looks like it comes from this package:
apt install libdrm-amdgpu-common

And that will install the file here:
/opt/amdgpu/share/libdrm/amdgpu.ids

---

### 评论 #10 — bigtrak (2023-12-21T01:13:18Z)

As of the the June 2023 rocm, 5.6.0 rocminfo returns the correct names for the GPUs I have -- mi25, mi100, mi210.
I've checked the installed amdgpu.ids file, and it contains a full list.  This is on enterprise linux 8.8.   

I'll check HIP when I have a chance as well, as well as some of the off-site platforms.

---

### 评论 #11 — kentrussell (2024-01-02T14:48:25Z)

Note that the distro-provided libdrm-amdgpu-common version of amdgpu.ids will be outdated compared to the one provided by ROCm on pretty much every release . So if the ROCm-distributed libdrm-amdgpu-common doesn't get installed, you'll have the amdgpu.ids provided by your distro. And that can be significantly different from one distro to the next in terms of how often they update. 
The package is a weak dependency for the thunk (for Debian-based systems it's a requirement, but for RPM-based systems it's a recommendation depending on if the OS supports "recommends"). 

---

### 评论 #12 — milthorpe (2024-01-05T00:17:56Z)

Our system (MI60 Ubuntu 22.04.3 with ROCM 5.4.3 and ROCM 6.0 installed as modules) has both `/usr/share/libdrm/amdgpu.ids` and `/opt/amdgpu/share/libdrm/amdgpu.ids`. The former is out of date; the latter has the product names for the newer GPUs including MI50/60 and MI250X. Since installing ROCM 6.0, `hipDeviceProp_t.name` now returns "AMD Radeon Graphics", rather than "AMD Instinct MI60" as expected.
There seems to be a sort of version number in the header of the `amdgpu.ids` file, but as it's always "1.0.0", I guess the only way to tell which version we have is a comparison against each released version.

---

### 评论 #13 — kentrussell (2024-01-10T14:48:30Z)

@milthorpe The one in /usr/share will be from the OS-distributed libdrm. That we don't have much control over, as the distro will update it on their schedule. The one in /opt/amdgpu will be from the ROCm (or amdgpu-pro) install and will be the up-to-date one. I do agree that versioning should be used here, since 1.0.0 doesn't really help much. But with how much churn there is for marketing names, it's probably not feasible.

@yanbosmu The ROCm release will support MI250X. There are no "driver files of MI250X" to speak of, they're all in the regular ROCm release. Install ROCm on a supported OS, and MI250X will work.


---

### 评论 #14 — ppanchad-amd (2024-05-09T15:22:36Z)

@bigtrak Has this been resolved for you? If so, please close ticket. Thanks!

---

### 评论 #15 — bigtrak (2024-05-09T16:21:32Z)

As of ROCm 6.0 (only version I have available) this issue is fixed.
It may have been fixed earlier than that, I don't have the 5.x versions
available to check.


---
