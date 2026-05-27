# All OpenCL programs hang on Solus

> **Issue #1000**
> **状态**: closed
> **创建时间**: 2020-01-16T20:25:53Z
> **更新时间**: 2023-12-14T08:12:23Z
> **关闭时间**: 2023-12-14T08:12:22Z
> **作者**: Tzigamm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1000

## 描述

I'm currently trying to package ROC 2.10.0 for Solus and I ran into an issue, I'm using a RX5700XT with an AMD A10-6700 and I'm running kernel 5.4.8.

At the moment I think ROCr-Runtime is working fine as rocminfo reports my GPU correctly, I'm having a problem with ROCm-OpenCL-Runtime though. As soon as a program tries to start OpenCL it hangs and use 100% of a CPU core. For instance, clinfo hangs without printing anything and Blender becomes irresponsive when I try to open the settings panel (that's when it looks for OpenCL devices) I need to CTRL-C clinfo and kill blender or they won't ever exit.

Here are the logs I see you've asked in other posts:
[lspci -v](https://pastebin.com/LcMtu0UV)
[rocminfo](https://pastebin.com/Rm9LTthF)
[groups](https://pastebin.com/PfQPnQ3a)

[strace clinfo](https://pastebin.com/4AgDB6tF)
[ldd clinfo](https://pastebin.com/7T47YDqG)

As you can see in Solus we don't use /opt so all binaries and libs are in /usr/bin/ and /usr/lib64, the binaries and libs created by rocm-opencl-runtime are located in /usr/bin/rocm-opencl and /usr/bin/rocm-opencl but since rocminfo runs fine and the strace shows clinfo can find everything it needs to I don't think it's a problem

---

## 评论 (5 条)

### 评论 #1 — ddobreff (2020-01-17T08:56:03Z)

#998 

---

### 评论 #2 — Tzigamm (2020-01-20T09:16:06Z)

Okay so you think it could be navi related? In that case wouldn't rocminfo throw an error?

---

### 评论 #3 — saitam757 (2020-03-29T14:27:21Z)

@Tzigamm Some time ago I tried packaging ROCM for Solus but I gave up. Some days ago was a post in the [Solus Forum](https://discuss.getsol.us/d/4167-i-built-rocm-for-solus-i-need-someone-to-test-it) that someone packaged ROCM up to OpenCl for Solus and needs Tester/Reviewer. I started yesterday the building of those packages and gave some feedback on the corresponding [respository](https://github.com/emaimx/Solus-ROCm-build). Maybe we can concentrate our efforts here to get the stuff running ?

---

### 评论 #4 — nartmada (2023-12-14T03:11:01Z)

Hi @Tzigamm, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #5 — Tzigamm (2023-12-14T08:12:23Z)

Hey @nartmada, sorry for letting this go stale, I haven't used Solus in a while so I can't test if the issue is still there. Closing this

---
