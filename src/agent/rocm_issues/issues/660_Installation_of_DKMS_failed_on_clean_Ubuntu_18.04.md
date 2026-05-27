# Installation of DKMS failed on clean Ubuntu 18.04

> **Issue #660**
> **状态**: closed
> **创建时间**: 2019-01-03T15:33:55Z
> **更新时间**: 2019-01-08T00:03:08Z
> **关闭时间**: 2019-01-08T00:03:08Z
> **作者**: arakan94
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/660

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

I tried installing ROCm 2.0 following instructions here (https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) and failed.

I have run upgrade to get latest packages and it is clean Ubuntu installation for the sole purpose of using ROCm (never tried it previously). I have kernel 4.15.0-43-generic and Radeon RX 580. 

Here is the terminal output: [https://pastebin.com/W7CLmfvE](url)

dkms status outputs this:
`amdgpu, 2.0-89, 4.15.0-43-generic, x86_64: built`

(after I run the install again & it failed with same output.. Before, dkms status showed this:
`amdgpu, 2.0-89: added`)

---

## 评论 (5 条)

### 评论 #1 — arakan94 (2019-01-03T16:02:17Z)

So I just tried again (for the 4th time) before giving up and it did something different and it seems like a success.. Log: https://pastebin.com/nxhb63bH


---

### 评论 #2 — jlgreathouse (2019-01-03T16:19:12Z)

I am unable to reproduce this problem on any of multiple Ubuntu 18.04 (4.15.0-43) systems, with RX 580 GPUs or other models. Some questions:

- Are you running in a virtual machine, container, or bare hardware?
- Do you have enough free hard drive space?
- What version of Ubuntu 18.04 is this? (Desktop? Server?)
- When you did the setup, did you do a "Normal Installation" or "Minimal Installation"?
  - Did you download updates while installing Ubuntu?
- This isn't shown in your logs, likely because it was before a reboot, but can you verify that you did the `sudo apt dist-upgrade; sudo apt install libnuma-dev` commands?
- I don't expect this would matter, but are you using an encrypted hard disk? Or on an LVM?
- Can you verify that the `sha1sum` of the `rocm.gpg.key` that you downloaded is `f7f8147431c75e505c58a6f3a3548510869357a6`?

---

### 评论 #3 — arakan94 (2019-01-03T17:36:27Z)

- It's bare hardware (Ryzen 1600, ASUS PRIME X370).
- Yes.
- Desktop.
- Minimal installation and yes, download updates during install.
- Yes - every step of the installation as is in the link.
- No, normal ext4 Primary partition
- Yes, SHA1 is same

---

### 评论 #4 — arakan94 (2019-01-03T17:50:58Z)

Anyway, it seems to be working now - I ran example from Quickstart guide [https://rocm.github.io/QuickStartOCL.html](url) and it seems to be working.

But it's weird that it took 4 attempts before the DKMS install finished.. If you point me to some log files that might be helpful, I'll be happy to post them here..

---

### 评论 #5 — jlgreathouse (2019-01-08T00:03:08Z)

I'm also not sure why the dkms installation took multiple attempts, and unfortunately, getting more log information would require uninstalling/reinstalling the driver to try to reproduce the problem. If you're willing to try that, I could try to walk you through some steps. But considering this problem appears to be rare (I've never seen it before), for now I'll close the issue.

If you'd like to try to gather more information, just respond again to the ticket. Thanks!

---
