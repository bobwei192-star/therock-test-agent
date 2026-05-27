# ROCm doesn't detect GPU.

> **Issue #1204**
> **状态**: closed
> **创建时间**: 2020-08-25T14:05:55Z
> **更新时间**: 2021-01-08T05:27:30Z
> **关闭时间**: 2021-01-08T05:27:30Z
> **作者**: JoseVSeb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1204

## 描述

My laptop: ASUS TUF Gaming FX505DY-BQ024T.
I'm trying to set it up so that I can do mild training and running of TF models for my projects.
There's an internal Vega graphics as well as dedicated RX 560X 4GB.
I can't get the ROCm to detect my GPU using rocminfo or clinfo. Both int gpu and dedicated are detected in rocm-smi. What do I do?
rocminfo shows the resource exhausted problem. clinfo shows the number of devices as 0.
I'm using Ubuntu 20.04.1.
Should I change my ubuntu version or something?

---

## 评论 (16 条)

### 评论 #1 — rkothako (2020-08-27T05:46:22Z)

Hi @JoseVSeb,
can you please share the output of the rocminfo or clinfo log?


---

### 评论 #2 — JoseVSeb (2020-08-27T06:16:01Z)

@rkothako , output of rocminfo and clinfo (I've been trying to fix it for sometime now. this is not the first output that i got):



>jvs@JVSTUF:~$ rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Bad address
jvs is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
jvs@JVSTUF:~$ clinfo
dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3182.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 
  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0


---

### 评论 #3 — rkothako (2020-08-27T07:23:57Z)

Looks like installation is not proper.
**/opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory**

Are you trying to install ROCm 3.1? If yes, its very old.
Ubuntu 20.04 support is officially enabled from the latest ROCm release: 3.7

---

### 评论 #4 — JoseVSeb (2020-08-27T09:00:22Z)

> Looks like installation is not proper.
> **/opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory**
> 
> Are you trying to install ROCm 3.1? If yes, its very old.
> Ubuntu 20.04 support is officially enabled from the latest ROCm release: 3.7

@rkothako
that doesn't matter, it's leftover from another try. The installed version is 3.7 itself

---

### 评论 #5 — JoseVSeb (2020-08-27T09:10:40Z)

I think my issue is very similar to this: https://github.com/RadeonOpenCompute/ROCm/issues/1205
I have a similar setup. Laptop with AMD CPU, internal Vega 8 GPU and dedicated AMD Radeon GPU.

---

### 评论 #6 — data-stepper (2020-08-31T15:05:41Z)

I am experiencing almost the same issue on a Mac Pro 5,1 using ubuntu 20.04.1 LTS.
At first I tried installing rocm exactly using the instructions given on the amd website and everything installed properly. rocm-smi is detecting my gpu (RX580 8GB) and showing me VRAM usage and so on but rocminfo only detects my CPU as the only HSA agent.

I first experienced this issue with kernel 5.4.0-42-generic and then I read on the amd website that only kernel 5.3 was supported so I downgraded to kernel 5.3.0-050300-generic and retried the entire install and ended up with exactly the same result.

(rocminfo, clinfo and rocm-smi outputs attached)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5151052/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5151054/rocminfo.txt)
[rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/5151055/rocm-smi.txt)




---

### 评论 #7 — JoseVSeb (2020-09-08T06:05:36Z)

Please, I need a solution. I'm here for using tensorflow with enough juice from my lap gpu. I can't (and don't know how to) fix the problems that arise in the installation of this software. I've tried everything that i could from my limited knowledge of how linux works and what i could find by scouring the issues. but nothing gives any direct indication to my problem. please help

---

### 评论 #8 — JoseVSeb (2020-09-13T06:15:34Z)

Someone please say something!!! How can I get past this? Should I try an older ubuntu (currently using 20.04)? Should I try installing some other driver like amdgpu-pro before installing this (I tried once and it only introducing clash between the two)? Please, I've been stuck here for a month now. I need a way forward.

---

### 评论 #9 — ksteimel (2020-09-18T16:24:59Z)

@data-stepper PCIe 3.0 atomics are required for using rocm with polaris graphics cards like your RX580 8GB. Your machine does not have these.

---

### 评论 #10 — ksteimel (2020-09-18T16:27:00Z)

@JoseVSeb can you post the full output of `sudo lspci -vvv ` and `lspci -tv`? This will let me see if pcie 3.0 atomics are supported on your machine.

---

### 评论 #11 — baryluk (2020-10-05T18:37:18Z)

@ksteimel BTW. It looks like this machine is using AMD Ryzen 5-3550H. It is Zen+ based. So it should support PCIe Gen3 + PCIe Atomics.



---

### 评论 #12 — ksteimel (2020-10-05T18:40:37Z)

#response_container_BBPPID{font-family: initial; font-size:initial; color: initial;} Yes it should but every stage between the cpu and the gpu needs to support it. The motherboard could lack support for pcie v3 atomics even if every other part of the pipline does.                                                                                                                                                                           From: notifications@github.comSent: October 5, 2020 2:37 PMTo: ROCm@noreply.github.comReply-to: reply@reply.github.comCc: ksteimel@iu.edu; mention@noreply.github.comSubject: [External] Re: [RadeonOpenCompute/ROCm] ROCm doesn't detect GPU. (#1204)  This message was sent from a non-IU address. Please exercise caution when clicking links or opening attachments from external sources.
@ksteimel BTW. It looks like this machine is using AMD Ryzen 5-3550H. It is Zen+ based. So it should support PCIe Gen3 + PCIe Atomics.

—You are receiving this because you were mentioned.Reply to this email directly, view it on GitHub, or unsubscribe.

---

### 评论 #13 — baryluk (2020-10-05T21:38:08Z)

@ksteimel Fair enough, it might be something with BIOS, or who knows. Best to check `lspci` as you suggested.

---

### 评论 #14 — ROCmSupport (2020-12-16T10:22:23Z)

Hi @JoseVSeb 
Is the issue still observed?
Can you please check with the latest ROCm 3.10 and update the status.
Thank you.

---

### 评论 #15 — ROCmSupport (2021-01-05T07:48:48Z)

Hi @JoseVSeb 
Are you able to overcome this issue?
Can you try with the latest ROCm 4.0 and share an update asap?
I am not able to reproduce with the latest ROCm 4.0 + Ubuntu 20.04.1 + Vega64

---

### 评论 #16 — ROCmSupport (2021-01-08T05:27:30Z)

No update for the last 3 to 4 weeks.
Hope issue is resolved.
Request t file a new issue, if any, we will handle with more speed.
Thank you.

---
