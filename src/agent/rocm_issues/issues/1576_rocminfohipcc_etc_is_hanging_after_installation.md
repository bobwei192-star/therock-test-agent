# rocminfo/hipcc etc is hanging after installation

> **Issue #1576**
> **状态**: closed
> **创建时间**: 2021-09-24T04:13:38Z
> **更新时间**: 2021-10-06T02:18:57Z
> **关闭时间**: 2021-10-06T02:18:57Z
> **作者**: uday610
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1576

## 描述

Hi, I installed latest Rocm (it shows as version 4.3.0) in Ubuntu 20.04.1 LTS. After this if I do "rocminfo" it just hangs after saying "ROCk module is loaded" , executing anything else also results the same, for example

rocminfo --help
ROCk module is loaded
^C

rocminfo --version
ROCk module is loaded
^C

I have not seen any alarming message while installing rocm (sudo apt install rocm-dkms). 

Any clue? 


---

## 评论 (13 条)

### 评论 #1 — ROCmSupport (2021-09-24T06:56:08Z)

Thanks @uday610 for reaching out.
I certainly understood the problem.
Can you please help me with the outputs of /opt/rocm/opencl/bin/clinfo and /opt/rocm/bin/rocminfo.
Also share the details of GPU.

Thank you.

---

### 评论 #2 — uday610 (2021-09-24T16:44:43Z)

Thank you @ROCmSupport for replying back.

No output for the first command, hang
```
/opt/rocm/opencl/bin/clinfo    
^C
```
One line output for the second command, then hang

```
/opt/rocm/bin/rocminfo
ROCk module is loaded
^C

```

lspci output, you see I am using MI-25

```
 lspci -vd 1002:
27:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon Instinct MI25] (rev 01) (prog-if 00 [VGA controller])
        Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon PRO V320
        Flags: bus master, fast devsel, latency 0, IRQ 46, NUMA node 1
        Memory at 2c000000000 (64-bit, prefetchable) [size=16G]
        Memory at 2c500000000 (64-bit, prefetchable) [size=2M]
        Memory at c4000000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at <ignored> [disabled]
        Capabilities: <access denied>
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu
```

There is nothing wrong with this GPU, I have been using this GPU for last couple of months with another server (AMD EPYC 7F32 8-Core Processor). . If I remember correctly I installed Rocm 4.2 that time without any problem and used the GPU with HIP application. But now I lost possession on that server, so I am trying to install Rocm in a new server (AMD EPYC 7F52 16-Core Processor) and now I am getting this problem. 

---

### 评论 #3 — ROCmSupport (2021-09-27T07:25:28Z)

Thanks for the information @uday610 
Can you please share the output of dmesg command, which gives better idea now as there is no proper output from rocminfo and clinfo commands.
Thank you.

---

### 评论 #4 — uday610 (2021-09-27T16:39:30Z)

@ROCmSupport , dmesg output is nothing. I cleared the dmesg (sudo dmesg -C) to make sure. This is something to do with userspace which is not reaching the driver. 

---

### 评论 #5 — ROCmSupport (2021-09-28T04:57:58Z)

Hi @uday610 
In similar cases, we found dmesg is very useful and so looking for the same.
I recommend you to capture dmesg once again after reboot of the machine and try running rocminfo and clinfo commands.
Thank you.


---

### 评论 #6 — uday610 (2021-09-28T06:05:02Z)

Hello @ROCmSupport , as I said there is no dmesg output.  I mean 0 output.  I cleaned the dmesg and see no dmesg is coming when I do rocminfo,, things are not at all reaching the driver. Even hipcc (which has nothing to do with driver) that also hangs. 

---

### 评论 #7 — uday610 (2021-09-29T19:45:21Z)

Hello @ROCmSupport , 

We think this issue has to do with new Rocm-4.3. Can you please let me know the instruction of installing Rocm-4.2, which worked nicely before (as I said couple of months before we installed Rocm 4.2 and it all worked). 

If I see the current installation page, the instruction has been changed. I dont have any way to look for the old instruction:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#installing-a-rocm-package-from-a-debian-repository

The section below which tells about the link "https://repo.radeon.com/rocm/apt/debian/ "  have been changed by your team.  Can you provide me the earlier 4.2 version of the installation guide page.. If that works then we will have a solution for now (and also it will confirm the new version has the problem). 

-----
sudo apt install wget gnupg2

wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -

echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
------

---

### 评论 #8 — ROCmSupport (2021-09-30T06:12:44Z)

Hi @uday610 
The below works for ROCm 4.3.1, 4.3 and 4.2.
For 4.3, instead of **debian**, use 4.3 and similarly for other versions like 4.2 also.

sudo apt install wget gnupg2
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/**debian**/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list

Please let me know if you find any problem. Thank you.

---

### 评论 #9 — uday610 (2021-09-30T06:50:12Z)

Hi @ROCmSupport ,

I uninstalled 4.3 and installed 4.2 and now everything working fine, output of rocminfo is working good. 

It is possibly to do with Linux kernel version. I am working on a Dell Server with AMD EPYC 7F52. This uses GA Kernel (normally stable kernel version), which is 5.4.0-88-generic in my server. So it might possible Rocm-4.3 has problem with this, but 4.2 is good. Maybe you can confirm? 

As of now I will use this 4.2 version. 

Thank you

---

### 评论 #10 — ROCmSupport (2021-09-30T07:20:49Z)

Yes @uday610 
Thanks for additional information.
ROCm 4.3 does not work with 5.4 kernels. So to make ROCm 4.3 work perfect, please try with the latest kernels like 5.11/5.8 etc.,.
Please feel free to close the ticket, once you are happy with the resolutions provided. Thank you.

---

### 评论 #11 — uday610 (2021-09-30T14:07:26Z)

@ROCmSupport , Few comments though: 

1) The hang of all rocminfo, hipcc is pretty drastic. You and me both did not suspect anything about Linux kernel version, right? Maybe installation should have been failed, or rocminfo first check the Linux kernel version and error out upfront? 

2) Curious what special is introduced in Rocm-4.3 that prohibits Rocm working on GA kernel? 

I am not closing this ticket because you may want to comment something regarding my above 2 points. However, you can close this ticket. 

---

### 评论 #12 — ROCmSupport (2021-09-30T16:13:05Z)

Hi @uday610 
ROCm 4.2 is old code which was based on old amdgpu driver, which inturns based on old kernel.
As we start supporting latest kernels like 5.11 and above and as our amdgpu(base kernel driver) is also built using latest kernels, we started supporting newer kernels and similarly we drop support on older kernels with newer ROCm versions.
Hope this helps.
Thank you.

---

### 评论 #13 — ROCmSupport (2021-10-06T02:18:57Z)

I hope I helped with needed information.
I am closing this ticket now.
Feel free to open a new ticket, for any, for quick resolutions.
Thank you.

---
