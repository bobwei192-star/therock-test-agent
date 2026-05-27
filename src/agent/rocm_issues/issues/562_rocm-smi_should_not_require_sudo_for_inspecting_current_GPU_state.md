# rocm-smi should not require sudo for inspecting current GPU state

> **Issue #562**
> **状态**: closed
> **创建时间**: 2018-09-27T13:17:59Z
> **更新时间**: 2018-12-24T22:48:05Z
> **关闭时间**: 2018-12-24T22:47:59Z
> **作者**: seibert
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/562

## 描述

The `rocm-smi` tool currently tries to relaunch itself with sudo privileges, even when only trying to display the current GPU state.  Looking at the code, it seems that write access to `/sys` is only needed to modify power profiles, clocks, etc, but the script attempts to relaunch itself with sudo regardless of whether read or write operations need to be performed.  This prevents rocm-smi from being used by normal users who can run GPU code, but also want to monitor the GPU load, temperature, etc.

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-09-27T14:24:23Z)

The comment you're basing this request on (https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-1.9.x/rocm_smi.py#L24) is somewhat outdated to the rest of the code. The enumerated list of reasons why `rocm-smi` may relaunch itself as with sudo [is shown here](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-1.9.x/rocm_smi.py#L1154).

In particular, the [request to show power](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-1.9.x/rocm_smi.py#L654) must access `/sys/kernel/debug/dri/{gpu_num}/amdgpu_pm_info`. This interface requires root access.

If you would like to avoid `rocm-smi` asking for a password all the time, you could try [this workaround](https://github.com/RadeonOpenCompute/ROC-smi/issues/23#issuecomment-369727625). Basically, because `rocm-smi` is an interpreted script, you can't just run it with setuid or setgid, this workaround allows anyone in the "video" group to run `rocm-smi` as root through the [super](https://www.unix.com/man-page/All/1/super/) utility. Note that this is not guaranteed to be secure; as a system administrator, you may not want random users to have access to `/sys/kernel/debug/dri/`, and you likely would not want an interpreter to have unfettered root access.

---

### 评论 #2 — kentrussell (2018-10-03T12:34:39Z)

I have a fix internally to push for 1.9.2 where we don't need sudo to do anything except for setting variables. The issue is what @jlgreathouse said, where trying to get the Power Consumption was only obtainable through debugfs, which requires sudo. I have been able to make a change to read a new sysfs file that reports the value as well, we just have to wait for 1.9.2 to push it out.

---

### 评论 #3 — jlgreathouse (2018-12-24T22:47:59Z)

I believe this was fixed as of ROCm 2.0.0. I just tested `rocm-smi` with no arguments on such a system and it no longer requires a `sudo` password. `rocm-smi --showallinfo` also returns everything without needing `sudo`.

---
