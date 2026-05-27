# Partial ROCm support for AMD Rdeon SSG Pro ?

> **Issue #485**
> **状态**: closed
> **创建时间**: 2018-08-01T06:55:11Z
> **更新时间**: 2023-04-01T08:39:56Z
> **关闭时间**: 2018-08-01T11:48:59Z
> **作者**: computingdolas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/485

## 描述

Hey guys, after several GitHub issues : 
here https://github.com/ROCmSoftwarePlatform/Tensile/issues/300 and
https://github.com/baidu-research/DeepBench/issues/105

I am under impression that, ROCm support for AMD SSD Pro is not fully operational. I also got to know that AMD SSD Pro is not one of the flagship deep learning GPUs. ROCm support should be generalised across entire range of radeon GPUs so that every faction can use it properly not just certain brands of radeon instinct GPUs. I have AMD Radeon Instinct SSD Pro and ROCm does not behave as intended with roubles giving me 1/10 of performance of MI25. I can extract 90% performance of GCN assembly level code but not from ROCm framework. 

Why it is like this ? Any specific reason to do that ?

---

## 评论 (7 条)

### 评论 #1 — jlgreathouse (2018-08-01T11:48:58Z)

Hi @computingdolas ,

This seems to be a duplicate of the question you've asked in those other issues you raised. Your question seems to be: why does a particular piece of software running on top of ROCm not perform well. That is a question for that piece of software, I believe. The ROCm issue tracker shouldn't be a clearinghouse for questions about every piece of software that runs on top of it.

I believe that @sunway513 is incorrect to state that the Radeon SSG Pro is unsupported in the **ROCm** stack. ROCm may not support e.g. the on-board SSG memory, but I believe we still support it as a Vega 10 GPU. @dagamayank mentioned in his response that it is not currently an optimization target for AMD's deep learning software frameworks. Those are slightly different things.

If those issues come back with information indicating that there is a problem elsewhere in the ROCm stack, please feel free to open an issue related to that. At the moment, I'm closing this as a duplicate of issues reported elsewhere.

---

### 评论 #2 — computingdolas (2018-08-01T11:56:40Z)

I think you misunderstood my question ? Let me reframe, why it is AMD SSD Pro is not currently a optimisation target although having same underlying architecture. Does this question does not bother how ROCm functions and its optimisation target architectures ?

---

### 评论 #3 — jlgreathouse (2018-08-01T12:06:02Z)

I understand the question, and I'm saying that, from a technical perspective, this question is better suited for the deep learning frameworks, MIOpen, Tensile, or rocBLAS (depending on where the issue is manifesting). If they find that the performance regression is within their code, it is those projects that will need to track any fixes. If the problem lies elsewhere in the software stack (e.g. if something in the ROC runtime is causing this issue), then I'm OK re-raising this issue here with enough technical details to help target the bug report to the proper sub-project. At the moment, I believe the proper target of the report is the software that is showing the performance regression (looking at the Tensile report, likely that project).

From the perspective of "why is AMD not targeting the Radeon Pro SSG as an optimization target for MI workloads", I cannot comment on that.

---

### 评论 #4 — computingdolas (2018-08-01T12:08:38Z)

Ok I understand that @jlgreathouse but I am really not happy with way that full ROCm support is available only for limited number of AMD GPUs.

---

### 评论 #5 — gstoner (2018-08-01T13:48:46Z)

@computingdolas  I am sorry your unhappy,  The required driver for RadeonPro  SSG is our AMDGPUpro driver.   ROCm should run on the Vega10 ASIC on board.   Now ROCm primary mission is not as a workstation driver, but for headless servers.  So when we enable solution like this we have to look at more robust and scalable solution then being used in the current AMDGPUpro driver which is the primary driver for this card.   And the solution has to work with our Radeon Instinct Product with Multiple GPU as well.   

RadeonPro SSG  is workstation card,  Vega10 ASIC + PLX + SSD which Share PCIe Bus to the host.   What were you expecting was the benefit of SSG Card with Deep Learning.  The filesystem for Linux still needs CPU intervention so you now sharing the PCIe bus for SSD and GPU.  So current benefit is limited due to this issue above where we get PCIe conflicts using the current limits OS stack.  

We have been exploring a proper solution for GPU and SSD communicate via more of Persistent Memory API supporting NVMe devices, but this is still a work in progress.  But we have to design for larger scale solution aka when multiple NVMe devices behind much larger  PCIe Switch on motherboard and also utilizing extra lanes of newer CPUs.  Also, deal with Multiple PCIe Root I/O.  

Please be patient as we look this problem for the Domian we focused on for ROCm driver.  Deep Learning and HPC. 

One thing AMDGPUpro will get the Full Deep Learning support, it just resourcing, focus and timing issue.   But you have it on AMDGPUpro Linux and Windows in the future. 

---

### 评论 #6 — computingdolas (2018-08-02T06:19:59Z)

@gstoner That was the answer I was looking for. Thanks for the detailed explanation and the future plans. I am looking forward to it. 

---

### 评论 #7 — snapo (2023-04-01T08:39:56Z)

This 2TB card would be awesome for current Machine learning models like the LLAMA 65B .... 

---
