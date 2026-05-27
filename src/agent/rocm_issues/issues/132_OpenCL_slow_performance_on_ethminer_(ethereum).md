# OpenCL "slow" performance on ethminer (ethereum)

> **Issue #132**
> **状态**: closed
> **创建时间**: 2017-06-21T10:27:24Z
> **更新时间**: 2025-01-14T15:33:24Z
> **关闭时间**: 2018-09-18T15:32:27Z
> **作者**: gsedej
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/132

## 描述

The good news is that you can use "ROCm driver" for cpp-ethminer. Which does fail on amdgpu-pro 17.10. (at least on RX 480). I am posting this here, since I couldn't find anyone using ROCm for mining.

_I do not know what are differences between amdgpu-pro and ROCm version of OpenCL (AMD-APP), if someone explain it would be nice_

The "problem" is performance. The performance on RX 480 using amdgpu-pro should be ~ 22MH/s [*], but the max I can get is ~19MH/s. The more interesting thing is, if I manually underclock to 900MHz [**] (level 2 in `pp_dpm_sclk`) the speed stays the same, but there is much reduction of noise heat and power consumption.

Is there any known reason for slower mining speed and not scaling on higher frequencises?

[*] http://www.phoronix.com/scan.php?page=article&item=ethminer-linux-gpus&num=2
[**]
```
sudo su
echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
echo 2 > /sys/class/drm/card0/device/pp_dpm_sclk
cat /sys/class/drm/card0/device/pp_dpm_sclk
```

---

## 评论 (25 条)

### 评论 #1 — gsedej (2017-07-03T11:26:01Z)

Installing ROCm-1.6 further decreases performance to 15MH/s (vs 22 in AMDGPU-PRO 16.40)

---

### 评论 #2 — gstoner (2017-07-03T15:09:35Z)

Ok positive is it runs,  we have team looking mining on ROCm now  we have the deep learning work  the first milestone released 

---

### 评论 #3 — gsedej (2017-07-04T07:04:02Z)

Thanks for the reply and for looking for problem.
I think it's general OpenCL performance issue. I tested LuxMark "Luxball HDR" and I get around 10300 score [1]. RX r480 with AMDGPU-PRO gets around 14k, which makes rocm 73% peroformace. The ethminer gets arund 16 MH/s vs 22 MH/s also around 72%.

The difference (rocm 1.4 vs AMDGPU-PRO) was also benched by Phoronix - the result is similar to mine (see LuxMark 3.0, OpenCL Device: GPU - Scene: Luxball HDR) [2]

[1] http://www.luxmark.info/node/4487
[2] http://www.phoronix.com/scan.php?page=article&item=rocm-opencl-linux&num=1

---

### 评论 #4 — gstoner (2017-07-04T17:58:41Z)

Now the AMDGPUpro driver for Vega10 supports the new lighting compiler and ROCm stack as well 

When we started the ROCm project, we made a decision to build out fully open source solution, which meant we need to move away from the traditional Shader Compiler used in our graphics stack since it was staying proprietary.    The traditional flow was two-stage compiler; we would compile the code to an intermediate language, HSAIL, then it would be picked up finalized and compiled by our shader compiler.  This same backend used by Graphics shaders. 

This journey started in earnest a little over a year ago to look the best way forward to fully open source compiler.  We began with the LLVM R600 codebase which needed a bit of work to get to be production class compiler.  But it was the right foundation to meet our goal of a  fully open stack,  

With this transition, we know we will have performance gaps, which we are working to close.   What we need help with from the community is assist us in testing a broader set of applications and reporting the and do some analysis potentially why.  One thing we have seen as well sometimes you need to code differently for LLVM compiler then the SC based compiler to get the best performance out if it.   

We are now active in the LLVM community, pushing upgrades to the code base to better enable GPU computing.  Also, changes are also up-streamed into LLVM repository. 

Note one significant changes the compiler now generate GCN ISA binary object directly.  With this change, it makes it easier for the compiler supports Inline ASM support for all of our languages ( OpenCL, HCC, HIP)   and also native assembler and disassembler support.  It is also a critical foundation for our math library and MiOpen projects. 

 For the last year, we have spent more time focusing on  FIJI and Vega10 with  Deep Learning Frameworks, MIOpen, and GEMM solvers.  We also have been filling in the gaps in LLVM for the optimization we need for GPU Computing, also improving the scheduler, register allocator, loop optimizer and lot more.  It is a bit of work as you can imagine.  But we already saw where the effort been worth it since it faster on a number of the codes.   

We test thing like follow on the compiler 
- Benchmarks: Bablestream, SHOC, Mixbench, Lattice, ViennaCL, COMD, Lulesh, xsbench.  Rodina, DeepBench
- Libraries: clFFT, rocBLAS, rocFFT, MIOpen 
- Application: 
    - OpenCL:  Torch-CL, Gromacs;  
    - HIP:  Caffe Torch, Tensorflow, 
    - HCC: NAMD 
- Internal test we built up for performance for OpenCL 
- Conformance tests for 
     - OpenCL 1.2 and 2.0 Conformance tests 
     - HCC conformance test 
Note above is a small sample of what we run on the compiler. We do A/B compares 

New test recently added: Radeon Rays, SideFX Houdini Test, Blender, Radeon ProRender, 
In the process of adding a number of currency mining apps 

On Ray Tracer we are just starting our performance analysis and optimization that more specific to this class of work, What you see over the summer is we will be focusing on optimization for the compiler for currency mining and raytracing.  I just have to stage this work in with the team.  I saw you referenced Phoronix article,  for ROCm 1.5 the new compiler was faster than LLVM/HSAIL/SC on FIJI for Blender, but for Luxmark we were slower.  http://www.phoronix.com/scan.php?page=article&item=rocm-15-opencl&num=2

One thing I will leave you with is we build standardized loader and linker and object format, with this it allows us to do some you never could do with AMGGPUpro driver, upgrades the compiler before we release a new driver.  So we can now address issue independently of the base driver for  OpenCL, HCC, and HIP and the base LLVM compiler foundation.  

Hope this helps 

---

### 评论 #5 — gsedej (2017-07-05T10:20:59Z)

Dear gstoner,

thank you very much for detailed explanation of internal works of ROCm. I didn't find other such explanations of ROCm elsewhere on the internet. I also think it should be posted somewhere more publicly.

I did use ethereum and LuxMark as benchmark, since it's hard do find other tools to make performance measurements (Blender does not include standard benchmark). Some benchmarks simply didn’t know how install or use. I didn't knew other benchmarks that  you mentioned. Will try to use in the future. I missed the part ROCm being faster than AMDGPU-pro. Congratulations to whole team. Many kudos!

The reason you decided to go fully open-source and linux as base platform is why I chose AMD graphics for my workstation. My colleagues opted for nvidia since it has traditionally better support for research (cuda applications, Matlab support (essential!)). Also our institute recently bought "supercomputer" that has 4x Titan X gpus and we are suggested to use it. I am happy that I can develop/test neural networks on my PC (rx 480) and then deeply it to "nvidia based supercomuter" (simply many times faster). For smaller network the rocCaffe works fast enough.
_I am also very happy with opensource OpenGL work by AMD - pushing "radeonsi" to exceed (FGLRX/AMDGPU-pro) and matching nvidia proprietary driver. The graphics team have also very talented people (i hope you are cooperating). The possibility to use PPA and have almost instant driver update when code changes is also great._   

The sole reason for being open-source and standard (opencl, hip, mesa, opengl, vulkan, freesync, ...) motivates me to use AMD products against proprietary and closed-source (cuda, gsync, shaddowplay, PhysX...). I hope that also AMDs CPU market will be more open-source frendly (the RYZEN's security platform and temperature sensors). Also with my own budget, I am opting AMD - I am buying RYZEN pc in near future. I also wish the ROCm will "ROCK", becoming popular enough so also my insittute will get AMD supercomputer solution. But with my work budget I simply cannot afford VEGA:FE-class compute gpu in near future.

I have question about LLVM r600 - are you also reusing the open-source OpenCL code ("clover", opencl 1.1)?

I am not opencl developer, but I am iterested what is the reason for not having Opencl 2.0 (or 2.1) device driver? (the opencl 2.0 was already supported on FGRLX on my previous HD 5670)

Last question - I had it for months - are you planning to support older GNC based gpus (e.g. R9 270)?

---

### 评论 #6 — lecbee (2017-07-05T11:59:31Z)

> I am posting this here, since I couldn't find anyone using ROCm for mining.

You won't find many people currently.
Most miners use low-end CPU (eg. Celeron or old C2D) and plug their GPU in PCIe x1 ports (which conforms to PCIe v2.0 most of the time).
This hardware lacks PCIe-atomics operation (which is part of PCIe v3.0) which is currently mandatory to use ROCm.

---

### 评论 #7 — gstoner (2017-07-06T01:11:22Z)

I have a question about LLVM r600 - are you also reusing the open-source OpenCL code ("clover", OpenCL 1.1)?

No it is not based on Clover,  this is based on the core OpenCL language runtime and Frontend we support on AMDGPUpro and Windows driver, but we map it to ROCr runtime API.


I am not OpenCL developer, but I am interested what is the reason for not having OpenCL 2.0 (or 2.1) device driver? (the OpenCL 2.0 was already supported on FGRLX on my previous HD 5670). 

OpenCL 2.0 was really designed for APU or SOC devices,  ROCm OpenCL support all the 2.0 API minus Pipe and clEnqueue, both which really need more time in spec development.  We are looking at OpenCL 2.1 to bring across  ROCm, AMDGPUpro and Windows Driver,  but it still under evaluation.   One thing majority of  OpenCL code is still OpenCL 1.1 and 1.2 so they can be compatible with NVIDIA and Intel.

Last question - I had it for months - are you planning to support older GCN based GPU's (e.g. R9 270)?

That is Tonga,  we were going back and forth on this one.  We need special firmware and capabilities which really Fiji forward have.  Hawaii we experimented with so we could have a large memory and 1/2 precision, but Vega10 take care the large memory issue.

Greg





---

### 评论 #8 — gstoner (2017-07-07T14:24:56Z)

So I was looking at the data put the integer performance into Roofline plot to understand performance when and where which stack is faster.   


What you see is the current miners are using very low IOPS/byte.  Right now you see crossover point for the two stacks is 8.25 IOPS/byte then they merge again at about 2.25 IOPS/byte. 

<img width="842" alt="screen shot 2017-07-07 at 9 11 09 am" src="https://user-images.githubusercontent.com/4129721/27961554-bb7fe224-62f4-11e7-96e5-55ccad2f2967.png">

Now on SGEMM the cross over is 24.25 Flops per byte   

<img width="534" alt="screen shot 2017-07-07 at 9 21 02 am" src="https://user-images.githubusercontent.com/4129721/27961841-b7ed7cec-62f5-11e7-9ce5-598e22d2a8f4.png">

This will show why FFT was slower on ROCm, GEMM is doing well ROCm.    

We dig into this more and get you guys update patch. 

---

### 评论 #9 — gstoner (2017-07-22T17:07:23Z)

Status Update,  So I personally we have been digging through performance issues and doing code review on the entire source base of the driver.  My team normally sits above the Thunk layer on what we work on.  But we now going down and debugging firmware and base Linux kernel and AMDGPU driver to sort where sources is. 

The issue with Ryzen was a Linux Kernel issue, 

We found in the AMDGPU base driver an issue power management code not correctly setting voltages forcing the chip not run efficiently on Vega 10. 

We found few another issue in the base kernel driver.  Based on this 1.6.1 is moving to Linux Kernel 4.11 and the respective AMDGPU base driver that goes with it.   

At the Thunk Layer, We found VMA alignment issue  that affects GFX8 devices ( Fiji and Polaris 10, which the fix is now in 1.6.1 

At the ROCr runtime time level we are now seeing, we have an internal test we use. 

Fiji Device Memory, Coarse-Grained
  Load:  458.7 GiB/s. = 492 GB/s 
  Store: 333.1 GiB/s = 355 GB/s 

Polaris 10 Device Memory, Coarse-Grained
  Load:  193.5 GiB/s = 207.8 GB/s
  Store: 174.9 GiB/s=187.8 GB/s 

Vega10 Device Memory, Coarse-Grained
  Load:  347.4 GiB/s =  373 GB/s 
  Store: 349.2 GiB/s = 374.9

We are now back up through the language stack to push them on getting memory performance. 
On Vega10 we looking at few other ideas to close the gap.  As you can see FIJI is north of 90% efficiency on Loads 

On ethash if we comment out isolate flag: and also set the compiler parameters --cl-local-work 512 --cl-global-work 10752 we see big jump in performance to 37 Mh/s

One thing with the new compiler the same flag and setting you did in the past for HSAIL/SC compiler may not work on LLVM based OpenCL compiler to get the best performance.  

--- a/libethash-cl/ethash_cl_miner_kernel.cl
+++ b/libethash-cl/ethash_cl_miner_kernel.cl
@@ -221,7 +221,7 @@ static void keccak_f1600_no_absorb(uint2* a, uint out_size, uint isolate)
                // much we try and help the compiler save VGPRs because it seems to throw
                // that information away, hence the implementation of keccak here
                // doesn't bother.
-               if (isolate)
+//             if (isolate)
                {
                        keccak_f1600_round(a, r++);
                        //if (r == 23) o = out_size;


We are finalizing 1.6.1, which I am hoping we have out by Tuesday,  note we will have 1.6.2 release following this release,  I am looking at few other areas right now I like to address in the HIP and OpenCL Runtime which will not make it into 1.6.1 

---

### 评论 #10 — gsedej (2017-07-26T08:50:12Z)

Thanks for making tests. The lastest rocm version 1.6.115 performance goes back to ~18Mh/s. Changing `if (isolate)` didn't differ for me.

I did not realize that --cl-... flags matter so much till now. When setting --cl-local-work 256 and --cl-global-work 8192 I did get around 21 Mh/s, which is same as AMDGPU-pro.

### ALSO BIG NOTICE
I noticed in the past that setting to manual performance level below max heped the noise, but didn't inflict lower performance. Now i found out that lowering GPU core freq actually helps.
```
echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
echo 3 > /sys/class/drm/card0/device/pp_dpm_sclk

ethminer -G -M  --cl-local-work 256 --cl-global-work 1800
#min/mean/max: 20480000/21503999/22186666 H/s

echo 7 > /sys/class/drm/card0/device/pp_dpm_sclk
ethminer -G -M  --cl-local-work 256 --cl-global-work 1800
#min/mean/max: 19968000/20582400/21504000 H/s
```
also the heat and fan are higher.

Any idea why?

Also you can use triple ` for start and for end of code section. _it's hard to read code on github since it makes markup..._


```
cat /sys/class/drm/card0/device/pp_dpm_sclk 
0: 300Mhz 
1: 608Mhz 
2: 910Mhz 
3: 1077Mhz *
4: 1145Mhz 
5: 1191Mhz 
6: 1236Mhz 
7: 1306Mhz 
```

---

### 评论 #11 — gstoner (2017-08-09T22:17:22Z)


Update  On 8 GB Vega10 we measuring this with a new build. 

|Vega                                                    | OCLWin10  |Eff    |Rocm OCL |Eff        |  Rocr API/ASM  |Eff           |
|:-----------------------------------|:--------|:-------|:----------|:---------|:---------------|:--------|
|OCLPerfDevMemReadSpeed (GB/s) | 392.28 | 81.08% | 411.598 | 85.08%   | 425.52.             | 87.95%|
|OCLPerfDevMemWriteSpeed(GB/s) | 386.484 | 79.89% | 413.551 | 85.48% | 424.12               | 87.66%|

On second test  for 8GB Vega10
- Load: 361 GiB/s (81% peak) = 387.7 GB/s
- Store: 386 GiB/s (86% peak) = 414.6 GB/s

We also seeing good number with this update for Ethereum

---

### 评论 #12 — gstoner (2017-08-24T01:52:22Z)

We rolled out ROCm 1.6.3 with 2MB support.   I working to release a firmware solution to get you to symmetric 413 GB/s on one our key memory tests

---

### 评论 #13 — jstefanop (2017-08-25T18:45:23Z)

@gstoner what are you guys getting for ethereum with the rocr API? Im assuming this is not a straightforward change from the ethminer codebase to run it with this API?

---

### 评论 #14 — gstoner (2017-08-25T18:55:15Z)

Can I contact you like to do firmware beta test  this second piece of puzzle

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: jstefanop <notifications@github.com>
Sent: Friday, August 25, 2017 11:45:24 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL "slow" performance on ethminer (ethereum) (#132)


@gstoner<https://github.com/gstoner> what are you guys getting for ethereum with the rocr API? Im assuming this is not a straightforward change from the ethminer codebase to run it with this API?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/132#issuecomment-325006049>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVzFtp-9NH1_n4lLFLgRYq4Hwny4ks5sbxZEgaJpZM4OAwtd>.


---

### 评论 #15 — jstefanop (2017-08-25T19:37:41Z)

@gstoner sure...same handle on Skype. 

---

### 评论 #16 — gstoner (2017-08-25T19:42:23Z)

Ok.  I am flying home now. I ping you tonight or Monday.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: jstefanop <notifications@github.com>
Sent: Friday, August 25, 2017 12:37:42 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL "slow" performance on ethminer (ethereum) (#132)


@gstoner<https://github.com/gstoner> sure...same handle on Skype.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/132#issuecomment-325016952>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuThLVK9JISLsu_4gXBrXBl65bHxCks5sbyKGgaJpZM4OAwtd>.


---

### 评论 #17 — int03h (2017-08-29T04:53:53Z)

This thread seems to be going places. Glad to see that. No intent to highjack, but  I was wondering if I may be so bold as to throw a few quick questions in here, directly related perhaps: 

a) Are you guys aware of the DAG slowdown issue at all ? ( http://1stminingrig.com/amd-working-on-ethereum-mining-hashrate-drop-fix-for-polaris-gpus/ ) - it has something to with the pipelining .. I don't want to go into detail if this is within the scope of this problem, or being addressed elsewhere. 

b) ADL does still allow you to change some of the settings and there are other methods that involve kernel " patches" that allow you to change the GPU frequency .. all of them give MUCH better TDP (half), but don't affect performance. I get 23Mh/s on ETH on 910Mhz at approx 80W on a RX 480 8GB. It seem that @gsedej and I are more interested in running in  a smaller thermal envelope rather than burning up the silicon.  AMD makes this very hard. Most people are reflashing their cards to accomplish this, the *NIX tools provided are not great. More than anything I would love it if you could expand rocm-smi and at least give us what ADL can and /still sort of still does/did. I assembled everything in Linux that Windows can do, so I know it is ALL possible. I can't understand how Windoze gets a pretty front end and we get a half working python script that moans about every little thing. I have heard the objections about a lot of it being related to upstream changes to the kernel requirements, but oddly this tool https://github.com/matszpk/amdcovc can do a lot of it too - without new kernels or ROCM, and as I mentioned ADL can also get some of it done, even on new silicon. The fact that it's all doable with a patchwork of bits and pieces rather than a nice clean tool is what boggles my mind.

c) I have 3 cards that throw NMI errors under load.  I have had some of them replaced by the manufacturer and they don't believe me that the cards are "faulty". Without going into any great amount of detail .. The error manifests by repeatedly throwing NMIs that look like this : 
Message from syslogd@noc at Jun 17 16:58:36 ...        1d20h 0.10 4x0.6GHz 971M16% 2017-06-17 16:58:36
 kernel: [  208.016971] NMI watchdog: Watchdog detected hard LOCKUP on cpu 1#001dModules linked in: ppdev intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel cryptd intel_cstate intel_rapl_perf input_leds serio_raw lpc_ich snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm parport_pc parport snd_timer snd mei_me mei shpchp soundcore soc_button_array mac_hid ib_iser rdma_cm iw_cm ib_cm ib_core configfs iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs xor raid6_pq amdkfd amd_iommu_v2 amdgpu(OE) amdttm(OE) ahci libahci fjes r8169 mii i915 video amdkcl(OE) i2c_algo_bit drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops drm

and then the card just loops through VM PROTECTION FAULTS on that slot over and over and over again. I have isolated everything and I am convinced there is a bug in the firmware somewhere or the driver (I have tried every driver and just about every kernel version). I am not sure what my escalation path for this is, but I am very tired of trying to convince someone that there is something wrong with them. They have never been flashed/modified in anyway, and they exhibit this behavior without any optimisations. **If there is new firmware going around I would be more than game to try it out**. I have 3x 8GB Ellesmeres (out of a fairly large population) that are currently paperweights, and I do have machines that satisfy the RoCM requirements for PCIe Atomics, and I do have some experience mining with the ROCM stack. (not a lot because it was slow- i.e. the reason for this ticket).  I used sgminer which I could only compile using gcc. If ethminer compiles with clang/llvm I would be keen to try that out!

Thanks.. apologies for the diversion. If anyone can address what you can, ignore what you can't or don't feel is relevant. 

---

### 评论 #18 — gstoner (2017-08-29T14:14:42Z)

@int03h 
You need ROCm 1.6.3 + 2MB PTE fragments for Ellesmere are enabled with a grub option:
    amdgpu.vm_fragment_size=9

GRUB_CMDLINE_LINUX="... amdgpu.vm_fragment_size=9"

To see it worked at the shell prompt

dmesg | grep fragment

ROCm-SMI allow you to set frequencies on ROCm stack  

NMI issue I have not seen on Polaris card but we mostly work Radeon Instinct cards 

---

### 评论 #19 — int03h (2017-08-30T19:32:04Z)

@gstoner  Thanks ! Let me give that a spin! 

Yeah - ROCm-SMI lets you set GPU Frequency and fans  etc:  It does not allow you to  change the voltages like: 

https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/amd-linux/918649-underclocking-undervolting-the-rx-470-with-amdgpu-pro-success

Nor does it let you change the memory frequency. 

My settings 2050Mhz - 910 Mhz - 818mV - got like 21Mh/s before the slowdown. With 5xRX480 8GB cards at 339W at the wall TOTAL ( including Mobo etc ) .. I am sure I could get more if I fiddled with the memory straps, but I don't want to flash the cards with non-reference bioses. 

As I say .. this is not done via vBIOS flash, and has been up to 25 days uptime, very low hardware error rate. Temps are at about 45C with fans at 80% ( I don't let the fans autorange - they don't seem to do a good job of figuring this all out since they stop turning for minutes).

As I say - windows users can break their cards with a few clicks. Seems like giving  bunch of kids all the power and "us"  nothing of substance. 

I even know of someone that is modifying memory straps in memory! So it is all possible, just a matter of will. 

---

### 评论 #20 — k3dar (2018-03-18T01:29:21Z)

@tekcomm hi, can you please post some more details? thanks :)
btw: now i have problem that RX580 is not detected with sgminer-gm-555 with ROCM OpenCL (amdgpu-pro 17.50) i try install also "--opencl=legacy,rocm", but still is detected in sgminer only Vega...

---

### 评论 #21 — bumi001 (2018-06-30T21:13:41Z)

Hi, You have taken quite a different route - highly technical - than the rest of the posts I have read on increasing MH/s. Not sure if you have seen https://access.redhat.com/solutions/2144921. Would you still use your custom init? If so, why?

---

### 评论 #22 — bumi001 (2018-06-30T23:52:13Z)

OK. Thank you. To me that means your performance of 44 MH/s is not related to your init, but rather mainly to pinning the gpus to the appropriate cpus, right? Am I simplifying it too much?

---

### 评论 #23 — bumi001 (2018-06-30T23:54:13Z)

Also, I am not sure how qrng and watchdog are related? I mean what is the idea?

---

### 评论 #24 — bumi001 (2018-07-01T00:03:23Z)

In one paragraph you say, "The overclocking of the cards is set in the 256k bios directly and the voltage is set there for undervolting" and in the next paragraph you say, "I don't oc and I don't use external fans". Could you add some context to those statements so I can better understand?

Can I access your beta somewhere?

---

### 评论 #25 — DeafMan1983 (2025-01-14T15:33:22Z)

Sorry for old thread! I suggest you to develop 3D software rendering with old OpenCL-2.x I tested over 600 FPS on 3D Software Rendering with SDL_Surface + OpenCL 1.1 = great performance for gaming. Please stop mining it! Because old graphic cards work only software rendering of game development like example Half-Life or Quake 2 with OpenCL then you will be happy if you play game as well. 

Reason: mining can't do high speed but it can eat much power/energy and you will get high billing. Please don't use mining if you use old graphic card. My graphic card is quite old and it called Radeon RX 480 8GB. Over 9 years old. But I worked on Ubuntu 24.04.1. 

Thanks for understanding me! Give up to mine and work with 3D rasterization of SDL2 or SDL3!

---
