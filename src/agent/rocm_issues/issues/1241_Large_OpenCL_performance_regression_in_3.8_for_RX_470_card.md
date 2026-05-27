# Large OpenCL performance regression in 3.8 for RX 470 card

> **Issue #1241**
> **状态**: closed
> **创建时间**: 2020-09-24T12:22:37Z
> **更新时间**: 2020-12-11T06:07:50Z
> **关闭时间**: 2020-12-11T06:07:50Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1241

## 描述

Ubuntu 18 w/ 5.4.0-48 kernel.
RX 470 GPU
Skylake CPU

Under 3.5, my kernels would take 13.8 ms to complete. With latest 3.8 upgrade, 
time increases to 17.8 ms. So, around 30% slower. 

---

## 评论 (11 条)

### 评论 #1 — baryluk (2020-10-05T18:32:47Z)

Are you using the upstream amdgpu, or the `rocm-dkms` driver?

Could you provide some minimal code example (C/C++ code + embeded kernel)? Smaller the better.



---

### 评论 #2 — boxerab (2020-10-05T18:54:23Z)

Thanks. Does rocm work with amdgpu ? How can I tell which driver is being used ?

---

### 评论 #3 — baryluk (2020-10-05T19:03:59Z)

It should work with amdgpu just fine with your kernel. I am using amdgpu with kernel 5.6, but also used it with earlier kernels like yours.

Try:

`sudo modinfo amdgpu | egrep 'filename|vermagic'`
`sudo dkms status`
`sudo dpkg -l rocm-dkms`
`sudo zgrep 'Initialized amdgpu' /var/log/kern.log*`
`sudo cat /sys/module/amdgpu/version`


---

### 评论 #4 — boxerab (2020-10-05T19:06:52Z)

@baryluk thanks. What happened with my upgrades was strange:

After 3.5, I upgraded with each point release, but the performance of my kernels remained the same. However, 
upgrades 3.6, 3.7 and 3.8 did not install an opencl directory in the release folders, so I continued using the 3.5 directory and the 3.5 .so library.

Finally, I did a fresh install of the OS with 3.8, and then the performance went down.





---

### 评论 #5 — ROCmSupport (2020-11-18T10:54:10Z)

Hi @boxerab 
Can you please share the code if its opensource and let us know the steps to reproduce the problem too.
Thank you.

---

### 评论 #6 — boxerab (2020-11-19T03:50:35Z)

@ROCmSupport thanks, unfortunately this is not open source code.

---

### 评论 #7 — ROCmSupport (2020-11-19T05:22:18Z)

Hi @boxerab 
We need some sample piece of code to verify locally and understand the problem.
Hope you got my point.

---

### 评论 #8 — baryluk (2020-11-19T16:03:57Z)

@boxerab Without some source code for the kernel that shows these performance issues, there is nothing anybody can do to help you.


---

### 评论 #9 — ROCmSupport (2020-12-03T11:57:50Z)

Hi @boxerab 
Recommend to close this issue, if you are not able to share execution steps/process to reproduce the problem.
Thank you.

---

### 评论 #10 — boxerab (2020-12-03T14:37:54Z)

I will at least identify which version of ROCm causes the slowdown.

---

### 评论 #11 — ROCmSupport (2020-12-11T06:07:50Z)

Hi @boxerab 
Until we validate/verify with the code, we are not in a position to understand and fix the issue.
Hope you got it.
Thank you.

---
