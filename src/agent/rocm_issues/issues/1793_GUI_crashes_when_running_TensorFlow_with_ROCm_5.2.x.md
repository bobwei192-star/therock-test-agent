# GUI crashes when running TensorFlow with ROCm 5.2.x

> **Issue #1793**
> **状态**: closed
> **创建时间**: 2022-08-20T11:23:29Z
> **更新时间**: 2024-03-16T03:10:20Z
> **关闭时间**: 2024-03-16T03:10:20Z
> **作者**: thesleort
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1793

## 描述

I want to perform training on my local computer using `tensorflow-rocm`, but currently it only works if I do it in a non-graphical view or stay at the login screen, while I SSH into the computer. This really defeats the purpose of training locally, as I then need my laptop to access and use TensorFlow on the desktop computer.

I suspect it might have something to do with video memory. When using `radeontop` it starts to consume all memory (shows it uses more than what is available)  when ever the smallest TensorFlow problem is started. This appears to be okay when in non-graphical mode, but using the GUI (Gnome 42) it freezes the GUI and crashes, and sends me back to the login screen (it logs me out). It also crashes the execution of the TensorFlow model/code, thus leaving me with nothing.

I have a Radeon VII installed with Ubuntu 22.04.1 LTS

[gui_dmesg.log](https://github.com/RadeonOpenCompute/ROCm/files/9386954/gui_dmesg.log)
[rocminfo.log](https://github.com/RadeonOpenCompute/ROCm/files/9386957/rocminfo.log)

Here is a simple example that fails to run in GUI mode, but runs without flaws and quickly in non-graphical mode.
[simple_example.zip](https://github.com/RadeonOpenCompute/ROCm/files/9386970/simple_example.zip)

---

## 评论 (5 条)

### 评论 #1 — Rlhoste (2023-02-12T19:10:47Z)

I have the same issue, did you find a solution?

---

### 评论 #2 — LucasSnatiago (2023-10-25T22:20:36Z)

Same issue here.

---

### 评论 #3 — thesleort (2023-10-26T05:53:56Z)

My temporary solution is/was to use my desktop as a home server when using TensorFlow. I start it up without a desktop/GUI. I then set up a Jupyter server that I can connect to from anywhere. This works incredibly well from my laptop, as I have the jupyter file locally, but all computation is performed on my desktop. This also means that I can work on my stuff from anywhere in the world, as I can always offload the computation with jupyter notebooks to the desktop-server at home.

---

### 评论 #4 — nartmada (2023-12-18T21:02:50Z)

Hi @thesleort, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #5 — nartmada (2024-03-16T03:10:20Z)

Closing the ticket as there is a temporary solution.  @thesleort, please re-open if you still observe this issue with latest ROCm 6.0.2.  Thanks.

---
