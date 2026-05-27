# ROCm Platform not found error

> **Issue #508**
> **状态**: closed
> **创建时间**: 2018-08-22T14:26:36Z
> **更新时间**: 2018-09-17T23:28:27Z
> **关闭时间**: 2018-08-23T15:16:42Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/508

## 描述

I have installed ROCm on both Debian 9 and Ubuntu 16 and 18. The error is persistent on both systems.

The hardware is:
- Mainboard: Gigabyte H110-D3A
- GPU: Asus Radeon RX580


---

## 评论 (16 条)

### 评论 #1 — valeriob01 (2018-08-22T14:30:38Z)

I must say that the hardware in question "as configured" works with amdgpu-pro. So I don't think it is a configuration issue.

The program I use terminates with error -1001.


---

### 评论 #2 — jlgreathouse (2018-08-22T14:42:30Z)

ROCm has different hardware requirements than amdgpu-pro, so I believe this could still be a configuration issue.

Could you tell me which of the PCIe slots on your motherboard you're using? I see that this is a board with a significnat number of PCIe gen 2 x1 slots: are you using these or the Gen 3 x16 slot?

Could you run the following commands for me?

- `lsmod | grep amdgpu`
- `lsmod | grep amdkfd`
- `groups`
- `lspci | grep VGA`
- `lspci -vvv`
- `lspci -tv`
- `lspci -n`
- After a reboot: `dmesg`
- `/opt/rocm/bin/rocminfo`
- `/opt/rocm/opencl/bin/x86_64/clinfo`

---

### 评论 #3 — valeriob01 (2018-08-22T15:43:30Z)

The five x1 slots are configured as Gen1, they are all used. The x16 slot is empty.
Thank you for helping.


---

### 评论 #4 — jlgreathouse (2018-08-22T15:47:03Z)

Hi @valeriob01 

Unfortunately, we do not support PCIe gen 1 operation on Radeon RX 580. This is a Polaris (gfx8) class GPU, and the ROCm software stack requires PCIe gen 3 atomic support to work on these GPUs. We support PCIe gen 1 and 2 operation on our Vega (gfx9) GPUs by disabling the SDMA engines, but your device requires PCIe gen 3 with atomics support.

---

### 评论 #5 — valeriob01 (2018-08-22T15:56:06Z)

I will try to configure the hardware as you say with Gen3 and see if it works.


---

### 评论 #6 — valeriob01 (2018-08-22T16:21:01Z)

Test done. With Gen3 configured, Ubuntu doesn't boot at all.


---

### 评论 #7 — jlgreathouse (2018-08-22T16:23:07Z)

If you uninstall ROCm (e.g. `sudo apt purge rocm-dkms`), does it boot?

---

### 评论 #8 — valeriob01 (2018-08-23T07:19:50Z)

I have reset the bios to Gen1 but Ubuntu doesn't boot anymore, I have to redo the installation but I haven't the time at the moment, I will see this later or tomorrow.


---

### 评论 #9 — jlgreathouse (2018-08-23T13:45:20Z)

I apologize about the problems, though I should ask: When you say "reset the BIOS to gen 1" does that mean that your previous test was using the same x1 slots, but with a BIOS setting change?

I ask because, according to your motherboard's manual, all of the PCIe x1 slots are only Gen 2 compliant. The only Gen 3 compliant slot is the x16 at the top.

---

### 评论 #10 — valeriob01 (2018-08-23T13:55:48Z)

Yes I changed the bios setting. The bios setting is general for all the slots, there isn't in the bios a setting for every slot, but only one general setting. 

---

### 评论 #11 — jlgreathouse (2018-08-23T14:12:17Z)

Then I suspect that even after changing your BIOS setting, ROCm will not work on your system so long as all of your GPUs are in the x1 slot.

When using a Radeon RX 580, ROCm requires the GPU to be in a PCIe Gen 3 slot. The only PCIe Gen 3 slot in your motherboard (regardless of BIOS settings) is the x16 slot. As such, you will only be able to use at most one GPU -- and only then if it's in the x16 slot.

That said, I haven't tested this motherboard, so I am also not sure if that setting would work. If the motherboard manufacturer put that x16 slot behind a PCIe switch that does not properly forward atomics, ROCm may still not work no your GPU. It's worth testing, however.

---

### 评论 #12 — valeriob01 (2018-08-23T15:01:53Z)

Ok. Then I think I will not be able to use ROCm with this hardware. It is surprising to see so restrictive demands on the hardware. But please contact me when you think I can try again.



---

### 评论 #13 — jlgreathouse (2018-08-23T15:16:42Z)

Hi @valeriob01 

I apologize that our software stack is unable to run on your hardware. We are working to build up support within ROCm, and with our current resources, we have focused our efforts on particular software domains (machine learning, enterprise computing, HPC, etc.). We want to continue to extend support, but there's only so much time in the day -- not that this reasoning helps you out much. :)

For reference, we require [PCIe Gen 3 atomics](https://github.com/RadeonOpenCompute/ROCm_Documentation/blob/master/Installation_Guide/More-about-how-ROCm-uses-PCIe-Atomics.rst) in an effort to increase the performance of launching work to the GPU and receiving completion signals from the GPU. On supported platforms (such as in the domains we are targeting), this performance benefit can be a big win over more-broadly-supported-but-slower solutions.

That said, we have heard many requests from the crypto-mining community to support PCIe slots without atomics, specifically so folks can put as many GPUs into a box as they can fit. We've heard this, and have added a ROCm operating mode that bypasses this atomic requirement on our Vega 10 GPUs. We are still evaluating this feature on our gfx8 GPUs (such as your Polaris GPU), but we have not had the resources to make the changes and properly validate them at this time.

Thanks for your interest, and I apologize for not being able to meet your needs. If we get the proper support in place, I will try to get in contact.

---

### 评论 #14 — valeriob01 (2018-08-26T10:40:27Z)

I don't do crypto-mining. I do HPC and I am experimentally doing it with a multi GPU mainboard.


---

### 评论 #15 — gmls22 (2018-09-10T02:18:08Z)

@jlgreathouse I'm also on the GFX8 Series and trying to use my GPU for deep learning; 

Is there any ETA on when the completed patches might be released for GFX8 support? 

Is it possible to experiment with atomics disabled (without validation) on a GFX8 card by compiling manually, and if so, what parameters and environment variables would be required for testing?

---

### 评论 #16 — jlgreathouse (2018-09-10T13:29:02Z)

Hello @gmls22 

With respect to your desire to run gfx8 series GPUs on deep learning workloads, I do want to note that Fiji, Polaris 10, and Polaris 11 (all gfx803) are supported in ROCm so long as your CPU and PCIe connections all support PCIe gen 3 with atomics. We *do* support these platforms, so I just want to make sure there's no confusion about that.

Unfortunately, I am unable to disclose any such roadmap information about supporting these devices without PCIe atomics.

I suspect that you would be unable to run any tests with atomics disabled. PCIe atomics are used for communication between the host and device when putting information into the user-level HSA queues. The command processor is the receiver of these packets, and AMD must modify the firmware running on this processor to be able to deal with user-level queues that will be accessed without PCIe atomics. AMD has made these firmware changes for gfx900 (Vega 10), but the public firmware for gfx803 does not include this.

---
