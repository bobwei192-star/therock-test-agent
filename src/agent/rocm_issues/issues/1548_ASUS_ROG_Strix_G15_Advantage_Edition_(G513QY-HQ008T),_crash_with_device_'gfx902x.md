# ASUS ROG Strix G15 Advantage Edition (G513QY-HQ008T), crash with device 'gfx902:xnack-'

> **Issue #1548**
> **状态**: closed
> **创建时间**: 2021-08-06T15:51:55Z
> **更新时间**: 2021-08-11T09:50:41Z
> **关闭时间**: 2021-08-10T12:50:41Z
> **作者**: rudolfgh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1548

## 描述

        Hi
        I'm doing some basic OpenCL programming and things are working fine
        with my 'main PC' with an 'AMD Radeon PRO WX 7100 8GB PCIe 3.0'.

        clGetDeviceIDs() reports one device of CL_DEVICE_TYPE_GPU for
        the platform and clGetDeviceInfo() reports 'gfx803' as CL_DEVICE_NAME.

        A few days ago I bought the mentioned notebook but things did not
        work as expected. This notebook has an AMD Ryzen 9 5900HX CPU and an
        AMD Radeon RX 6800M GPU.

        Now clGetDeviceIDs() reports two devices of CL_DEVICE_TYPE_GPU for
        the platform and clGetDeviceInfo() shows 'gfx1031' and 'gfx902:xnack-'
        for CL_DEVICE_NAME.

        With my OpenCL programm I can use device 'gfx1031' but when trying
        to use device 'gfx902:xnack-' I get 'random errors'.

        Comparable problems also occur with clinfo. The symptoms are:

        When run the first time after power up of the PC the programs
        run up to some point and then stop with this error:

        Memory access fault by GPU node-2 (Agent handle: 0x5652e8860350) on address (nil). Reason: Unknown.

        In this case dmesg is showing things like these:

[  199.015019] amdgpu 0000:07:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:173 vmid:8 pasid:32772, for process clinfo pid 1382 thread clinfo pid 1382)
[  199.015026] amdgpu 0000:07:00.0: amdgpu:   in page starting at address 0x0000000000000000 from IH client 0x1b (UTCL2)
[  199.015035] amdgpu 0000:07:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840A51
[  199.015036] amdgpu 0000:07:00.0: amdgpu:      Faulty UTCL2 client ID: CPC (0x5)
[  199.015037] amdgpu 0000:07:00.0: amdgpu:      MORE_FAULTS: 0x1
[  199.015038] amdgpu 0000:07:00.0: amdgpu:      WALKER_ERROR: 0x0
[  199.015038] amdgpu 0000:07:00.0: amdgpu:      PERMISSION_FAULTS: 0x5
[  199.015039] amdgpu 0000:07:00.0: amdgpu:      MAPPING_ERROR: 0x0
[  199.015039] amdgpu 0000:07:00.0: amdgpu:      RW: 0x1

        When rerun the programs do NOT stop but seem to be in a busy loop
        with top showing about 100% CPU for the process. I do not see dmesg
        messages in this case.

        In my OpenCL program the last activity before the crash is just
        before I call clCreateContext().
        For clinfo the last messages printed on the screen before the crash
        are these:

...
  Device Name                                     gfx902:xnack-
  Device Vendor                                   Advanced Micro Devices, Inc.
...
...
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
*** crash***

        BTW, I first noticed this problem with my Arch Linux and ROCm 4.3
        (and also 4.2) which I installed from the AUR.

        In order to make sure that the problem was not introduced by some
        error in the Arch installation I set up a fresh UBUNTU 20.04.02
        and installed the latest ROCm according to instructions from here:

        https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#supported-operating-systems

        After some minor correction for LD_LIBRARY_PATH I could/can run
        clinfo and my program also on UBUNTU 20.04.02 but the crash I see
        still is there. So the problem should not be with the Arch installation.

        Would anybody have a clue what might be the problem here or what
        could we do to narrow down the problem?

        BTW rocminfo does run without problems in any case.

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-08-09T05:26:27Z)

Thanks @rudolfgh for reaching out.
Looks like gfx902(GPU) is not supported card. Request to check for supported hardware section @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)

Meanwhile can you please share the output of **/opt/rocm/bin/rocminfo** and **/opt/rocm/opencl/bin/clinfo**
And also please share the output of **lspci -nn | grep AMD/ATI** for better understanding of the problem.
Thank you.


---

### 评论 #2 — rudolfgh (2021-08-09T14:42:46Z)

        Thanks for the info. Indeed I was not aware that

        'The integrated GPUs of Ryzen are not officially supported targets for ROCm'

        as can be read at the link you mentioned. This might well be the
        problem I ran into now. I just read somewhere that the integrated
        graphics for my CPU are based on GCN and GCN should be supported by 
        ROCm. But perhaps because it is 'integrated' into the CPU it will 
        nevertheless not work?

        Anyway I've generated the requested logs. Interestingly on my freshly
        installed UBUNTU 20.04.02 I can find two clinfo binaries and these
        produce (slightly) different output but both do crash at the end:

        -rwxr-xr-x 1 root root  80568 Jul 25 19:12 /opt/rocm/opencl/bin/clinfo*
        -rwxr-xr-x 1 root root 110136 Dez 19  2018 /usr/bin/clinfo*

        Log files included as uploaded files...

[rog_lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/6955202/rog_lspci.txt)
[rog_opt_rocm_bin_rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6955203/rog_opt_rocm_bin_rocminfo.txt)
[rog_opt_rocm_opencl_bin_clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6955204/rog_opt_rocm_opencl_bin_clinfo.txt)
[rog_usr_bin_clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6955205/rog_usr_bin_clinfo.txt)



---

### 评论 #3 — ROCmSupport (2021-08-10T12:50:41Z)

Hi @rudolfgh 
Thanks for sharing the information.
ROCm supports GCN based cards but not all. gfx902 is not a ROCm supported card and as I told integrated GPUs are not supported. Only discrete cards are supported as of now.
Please check for supported hardwares @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support.
And also you have Navi10 XL card which is also unsupported with ROCm.
Thank you.

---

### 评论 #4 — rudolfgh (2021-08-10T13:54:00Z)

Hi,

thanks again for the 'refresh'. So I guess chances are low to see my
integrated GPU running (soon) with ROCm:-(

But one last question: you mention a 'Navi10 XL card' which is not
supported. If I'm right, isn't the dedicated GPU in my Notebook
(AMD Radeon RX 6800M) based on RDNA2 / Navi 22 and not Navi10?

Interestingly this GPU IS running since ROCm 4.2. So obviously there IS
some sort of support in ROCm for this GPU, even if not officially.

And yes, you're right, 'intergrated' GPUs are not supported, as I had to
learn. But even then I'd not expect programs to crash if an attempt is
made to use such an unsupported card when using officially documented APIs.
Instead a decent message like:

        GPU not supported

would be more appropriate than a 'Memory access fault'. The latter rather
seems to me like a programming error and does not necessarily refer to
supported or unsupported hardware. So perhaps your programmers might have
a chance to avoid this 'Memory access fault'?


BR

R. Schubert

--
Rudolf Schubert                 \
Kirchstr. 18a                    \  ***@***.***
D-82054 Sauerlach                /  http://www.dose.muc.de
Tel. 08104/908311               /


On Tue, 10 Aug 2021, ROCmSupport wrote:

> 
> Hi @rudolfgh
> Thanks for sharing the information.
> ROCm supports GCN based cards but not all. gfx902 is not a ROCm supported card and as I told integrated GPUs
> are not supported. Only discrete cards are supported as of now.
> Please check for supported hardwares @
> https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support.
> And also you have Navi10 XL card which is also unsupported with ROCm.
> Thank you.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or unsubscribe.
> Triage notifications on the go with GitHub Mobile for iOS orAndroid.[AVDS43EPVF45IWSDB2PH5QTT4EOCXA5CNFSM5BWFHSUKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOOR
> PWSZGOGVT6D2A.gif]
> 
> 
> 

---

### 评论 #5 — ROCmSupport (2021-08-11T07:32:10Z)

Thanks @rudolfgh for the suggestions on showing a decent message like: GPU not supported for non-supported cards.
Let me work on this and I am creating an internal issue to move it further.
Thank you.

---

### 评论 #6 — ROCmSupport (2021-08-11T09:50:41Z)

I created an internal ticket on this.
Thank you.

---
