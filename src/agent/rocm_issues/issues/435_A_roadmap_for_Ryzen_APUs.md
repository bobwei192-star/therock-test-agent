# A roadmap for Ryzen APUs

> **Issue #435**
> **状态**: closed
> **创建时间**: 2018-06-15T01:09:42Z
> **更新时间**: 2018-11-22T22:46:18Z
> **关闭时间**: 2018-09-14T13:50:22Z
> **作者**: pmarcelll
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/435

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Embedded Ryzen APUs were recently launched and a Kickstarter campain was also started for the [Udoo Bolt](https://www.kickstarter.com/projects/udoo/udoo-bolt-raising-the-maker-world-to-the-next-leve) maker board with an embedded Ryzen V1000 series APU. They advertise this board as a good choice for AI and machine learning projects.

It seems that Tensorflow will soon be capable of running on AMD GPUs by default, thanks to ROCm and HIP, but in my opinion the lack of ROCm/proper Tensorflow support for Ryzen APUs will seriously hurt the perception of AMD among machine learning enthusiasts (who spend $300+ on a maker board that turns out to be almost useless for them) and engineering students (who need to buy a laptop with a discrete GPU, and most cheaper laptops with discrete GPUs are Intel+Nvidia solutions).

Laptops with Ryzen PRO APUs and boards with embedded Ryzen APUs are launching soon. Are there at least any plans to support APUs eventually?

---

## 评论 (17 条)

### 评论 #1 — zpodlovics (2018-06-16T18:59:06Z)

FYI: https://github.com/RadeonOpenCompute/ROCm/issues/399#issuecomment-386922775

---

### 评论 #2 — pmarcelll (2018-07-06T16:43:03Z)

Thanks, now that a lot of stuff is being mainlined hopefully it will be easier for the team.

---

### 评论 #3 — vulturm (2018-07-13T15:18:04Z)

I suppose the support is almost ready: https://lists.freedesktop.org/archives/amd-gfx/2018-July/024094.html

---

### 评论 #4 — pmarcelll (2018-07-13T15:33:39Z)

I just saw the article about it on Phoronix, it's great news.

---

### 评论 #5 — kentrussell (2018-09-14T13:50:22Z)

That's something you should bring up in the HCC github Bug Reports (https://github.com/RadeonOpenCompute/hcc). ROCK/ROCT/ROCR support APUs, but HCC doesn't. If you want to get TensorFlow support for APUs, I'd bring it to their attention directly. The base has support (kernel/thunk/runtime), but HCC obviously needs to support it to get in there

---

### 评论 #6 — briansp2020 (2018-09-14T17:54:31Z)

I'm not sure whether this is the right place to ask...
Is GPU ISA so different between different generations of graphics cards that each different generation requires compiler changes? I understand GPU ISA is still evolving but I thought that code compiled for older GCN would run on new hardware...

---

### 评论 #7 — jlgreathouse (2018-09-14T18:20:53Z)

The ISA _does_ have meaningful changes each generation. In particular, the binary encoding of even similar instructions can change slightly each generation. As such, moving between e.g. gfx7 to gfx8 or gfx9 GPUs is likely to result in binaries that are wholly incompatible.

As [described here](https://llvm.org/docs/AMDGPUUsage.html#processors), one of the major difference between the dGPU and APU instruction sets (e.g. gfx900 dGPU and gfx902 APU) is the required support for XNACK. XNACK is needed so that the GPU can take precise exceptions on particular memory accesses for things like page faults. Our current dGPUs do not need this, so the compiler does not create code with XNACK -- this offers higher performance in these GPUs. The APUs do need these, if we want to run code in "HSA" mode where the CPU and GPU share a virtual memory space with [IOMMU support](http://pages.cs.wisc.edu/~basu/isca_iommu_tutorial/index.htm). So the compiler must target these differently.

---

### 评论 #8 — jlgreathouse (2018-09-14T18:36:24Z)

Note that we do publish our ISA specifications, so you see the differences between the major generations in the following manuals:
  * [ISA manual for "Sea Islands", gfx7](http://developer.amd.com/wordpress/media/2013/07/AMD_Sea_Islands_Instruction_Set_Architecture.pdf)
  * [ISA manual for "GCN3", gfx8](https://32ipi028l5q82yhj72224m8j-wpengine.netdna-ssl.com/wp-content/uploads/2016/08/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf)
  * [ISA manual for "Vega", gfx9](https://developer.amd.com/wordpress/media/2017/08/Vega_Shader_ISA_28July2017.pdf)

Also, as an aside, some of the sub-generation specifiers also demarcate compiler-driven workarounds for  hardware idiosyncrasies. So if you try to run one sub-generation on a GPU we've marked as another sub-generation, you may run into instability, even if the official ISA is the same.

---

### 评论 #9 — pmarcelll (2018-09-15T13:53:37Z)

@kentrussell Can you please, clarify your comment?

The readme says these APUs are currently not supported by ROCm at this time, but clearly, support is under development. So what is currently supported? Does ROCm support OpenCL on Ryzen APUs? I'm asking mainly because these boards with embedded Ryzen APUs (like the UDOO Bolt) are advertised with Tensorflow, or at least accelerated machine learning support, and I think customers rightfully expect this in these small boards, the relatively big GPU/compute power is their main selling point. Most of these systems use Linux, so the best option would be Tensorflow with all the fine tuned libraries, the second best would be another ML framework on top of OpenCL 1.2, but I also can't find any useful information about the proprietary OpenCL runtime (i think it's called PAL).

Thanks.

---

### 评论 #10 — kentrussell (2018-09-16T12:41:38Z)

You can refer to the list of supported chips through a couple spots, but the easiest one to navigate and read would be in the ROCT topology:
https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/master/src/topology.c#L85

There we have the Kaveris, Carrizos, and Raven. That's what's supported with the ROCK/ROCT/ROCR/SMI . For TensorFlow, you'll need HCC, so that list is in their "is_valid" list : https://github.com/RadeonOpenCompute/hcc-clang-upgrade/blob/be6eeeeffb62557a79a6b559b7b633fb29e5d8e4/lib/Driver/ToolChains/Hcc.cpp#L311 

That's got gfx701 (Hawaii), gfx803 (Fiji/Polaris10/Polaris11), gfx900 (Vega10) and gfx903 (Vega20). You can use the topology.c list to reference the gfx numbers as well (I often do, since I can't keep them all straight). Hopefully that clarifies things a little bit. 

For OpenCL, I think that their list would be easiest to reference at https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/15fb9b06ecfb8fd87df2578657a49b0a56886245/runtime/device/rocm/rocdevice.cpp#L78 . That includes Hawaii, Tonga, Fiji, Vega10/12/20, and the Carrizo/Raven APUs.

---

### 评论 #11 — imyxh (2018-09-16T19:21:48Z)

@kentrussell, thanks for clarifying the state about OpenCL and such. This whole time I've been thinking my Raven APU isn't able to use ROCm just because it isn't supported as it says on the README. Perhaps that should be updated to reflect different levels of support for each chip—I'd do it if I knew what I was talking about. 

---

### 评论 #12 — jlgreathouse (2018-09-16T19:29:47Z)

Hi @pmarcelll 

To add a bit more detail, the kernel driver (amdkfd, "ROCK") has a list of devices that should work with it here: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L276

If the kernel driver does not have a device in that list, ROCm definitely won't work with it, since that is the lowest level of the stack that is required for a device to work in ROCm. I bring this up because I see at least one unreleased device in the ROCT topology list that is not in the ROCK device list. That device will not work with current versions of ROCm.

@kentrussell's description of the other layers is accurate. While the kernel driver, thunk, and runtime may all have code enabling certain hardware devices, that does not mean they will work with the rest of the ROCm stack. If the HCC compiler does not enable certain device generations, then multiple pieces of the ROCm software stack will not work on those devices. For instance, HIP currently relies on this compiler, so programs that use HIP will not compile for architectures that HCC does not target.

Also note that the HIP runtime has some pre-compiled kernels internally for things like data movement -- as such, [the runtime itself must also be targeted towards particular device generations when it is compiled](https://github.com/ROCm-Developer-Tools/HIP/blob/master/CMakeLists.txt#L215). It currently targets gfx701, gfx803, gfx900, and gfx906.

Similarly, elsewhere in the software stack, our libraries such as [rocBLAS](https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/develop/CMakeLists.txt#L184), [Tensile](https://github.com/ROCmSoftwarePlatform/Tensile/blob/master/Tensile/Source/TensileConfig.cmake#L106), [rocFFT](https://github.com/ROCmSoftwarePlatform/rocFFT/blob/develop/CMakeLists.txt#L133), [rocPRIM](https://github.com/ROCmSoftwarePlatform/rocPRIM/blob/master/CMakeLists.txt#L70), and [MIOpen](https://github.com/ROCmSoftwarePlatform/MIOpen/blob/master/CMakeLists.txt#L123) would need to be recompiled to enable other architectures. Right now, these libraries target gfx803 and gfx900 because those are the officially supported architectures in ROCm.

I have been very careful to not use the word "support" until now, because I am trying to prevent confusion. What @kentrussell and I are describing is what the software is capable of or can be configured to do. This is not to say that AMD or the ROCm team officially claims to support a GPU just because it is listed in the code for ROCK/ROCT/etc. Our official support list can be found [on the front page of the ROCm site](https://github.com/RadeonOpenCompute/ROCm/#hardware-support). A much more detailed list of what is supported, what "should work", and what is known not to work can be found [on our github.io site](https://rocm.github.io/hardware.html).

The last one, in particular, discusses some of what has been described here -- that while the kernel driver and Thunk may work with certain APUs, AMD does not make claims of support for this, and other layers in the ROCm stack may not be enabled for these devices.

There's also a note about our Tonga GPUs, specifically, that describe how they are known *not* to work with current drivers, even though they are included in the ROCK and ROCT code. This is important to note, because I want to make it clear that just because a GPU is listed in the ROCK or ROCT code, that does not mean that AMD will ensure that it works. Devices not on our official support list go through much less rigorous testing before releases.

That said, with all of these links here, you may be able to build a custom version of our software stack that would work on your GPU. AMD won't guarantee this will work, however. And if you submit bugs to projects like MIOpen or our branch of tensorflow and say "things are broken for gfx902", they will likely close them as "this is an unsupported hardware configuration". They may accept patches (I can't speak for them to guarantee this), but they won't guarantee to spend any time helping you debug things in such unsupported hardware configs.

---

### 评论 #13 — jlgreathouse (2018-09-16T19:50:22Z)

Hi @imyxh

I should also point out that, even with code in ROCK to enable particular APUs, you may have difficulty getting `amdkfd` to come up on such devices. When trying to come up on an APU, the `amdkfd` driver expects your system BIOS to make a CRAT (component resource affinity table) available that describes the layout of the hardware (and the GPU in particular).

We have found that OEMs and ODMs that sold machines built using AMD APUs often did not make this table available in their system BIOS. As such, in the past we found that users were often unable to properly use APUs because of hardware settings outside of our control.

I don't know if this situation has improved with Raven Ridge, but it's something to keep in mind if you try to go off the "supported systems" path. :)

---

### 评论 #14 — kentrussell (2018-09-17T10:10:23Z)

Thanks for mentioning that @jlgreathouse . All of my comments have been "this is what's in the source code" but mobile chips (APU and GPU) have always been an issue with KFD (and even Catalyst Drivers on Windows). Reminds me of my old days at AMD Customer Care... 

Laptop manufacturers tend to make a lot of changes to the functionality of the chips (GPU and APU) to ensure that they fit certain specifications (keeping them under a certain power draw, price point, etc). So while the kernel can support the device ID, there could be other issues preventing them from working properly. Like the CRAT table, which we've seen more than a few times while bringing up Kaveri, Carrizo and Raven.

---

### 评论 #15 — jarvis-hal (2018-09-30T14:54:08Z)

> That's something you should bring up in the HCC github Bug Reports (https://github.com/RadeonOpenCompute/hcc). ROCK/ROCT/ROCR support APUs, but HCC doesn't. If you want to get TensorFlow support for APUs, I'd bring it to their attention directly. The base has support (kernel/thunk/runtime), but HCC obviously needs to support it to get in there

> 

I have raised an issue at Issue Reports in HCC for v1000. We have been testing V1000 working with our partners and it will be exciting if APU in AMD Ryzen Embedded V1000 can be leveraged.  Here is the link to the issue I raised [
https://github.com/RadeonOpenCompute/hcc/issues/883](
https://github.com/RadeonOpenCompute/hcc/issues/883)


---

### 评论 #16 — lsr0 (2018-10-01T14:00:37Z)

Apologies I should've mentioned I also created an issue for hcc: https://github.com/RadeonOpenCompute/hcc/issues/879

There was a great response that linked to a thread on AMD's forum (https://community.amd.com/thread/232266)

The most pertinent detail in this context was in the last post from Gregory Stoner: 
> Also, the team has been working on Raven Support for ROCm it just taken a bit longer to get all the foundation we need in place

---

### 评论 #17 — exilef (2018-11-22T22:45:23Z)

Is there any news on this? I am having trouble to getting OpenCL-OpenGL interop going on Ryzen V1000 series APUs. While I can get graphics+OpenCL to work separately, the interop still does not work (IOMMUv2 is enabled). I tried the following setups:

1) Ubuntu 18.04 with 4.15.39 kernel and default ROCm dkms install: this results in a blank screen after boot and some error messages in the kernel log: `[drm:construct [amdgpu]] *ERROR* construct: Invalid Connector ObjectID from Adapter Service for connector index:2!`

2) Ubuntu 18.04 / 18.10 with 4.19 kernel and non-dkms ROCm install (as described in #588): here, both graphics and OpenCL work, but the CL-GL interop does not.

I know that the source of the problem does not lie in my code becasue it works on both macOS and on the same system using configuration 1) with a discrete Vega 64 card.

Is there any roadmap for the interop working on later versions of ROCm? Thanks for your help!

---
