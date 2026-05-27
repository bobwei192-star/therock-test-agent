# MI100 never cools down properly

> **Issue #1468**
> **状态**: closed
> **创建时间**: 2021-05-11T12:58:38Z
> **更新时间**: 2022-03-07T03:37:39Z
> **关闭时间**: 2021-06-02T11:53:24Z
> **作者**: athas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1468

## 描述

* RHEL 8.3
* [Installed ROCM 4.1 via these instructions](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel)
* Machine is an HPE server with two Epyc CPUs.  An identitical system contains an NVIDIA A100 with no issues (all temperatures low).

Just after boot, the MI100 GPU has these temperatures:

```
amdgpu-pci-2900
Adapter: PCI adapter
vddgfx:       +0.62 V
fan1:           0 RPM  (min =    0 RPM, max = 3850 RPM)
edge:         +53.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
junction:     +59.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
mem:          +55.0°C  (crit = +94.0°C, hyst = -273.1°C)
                       (emerg = +99.0°C)
power1:       49.00 W  (cap = 290.00 W)
```

If I then run an OpenCL program that hammers memory (in my case, summing 4GiB of floats 10000 times), the temperature grows significantly, and for `mem` it even hits the limit, leading to this message in dmesg:

```
amdgpu 0000:29:00.0: WARN: GPU thermal throttling temperature reached, expect performance decrease. HBM.
```

That's perhaps fine by itself, and maybe the MI100 needs more airflow than we're giving it, but the weird thing is that the idle temperature then gets stuck about 10C higher than at boot:

```
amdgpu-pci-2900
Adapter: PCI adapter
vddgfx:       +0.63 V
fan1:           0 RPM  (min =    0 RPM, max = 3850 RPM)
edge:         +66.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
junction:     +71.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
mem:          +68.0°C  (crit = +94.0°C, hyst = -273.1°C)
                       (emerg = +99.0°C)
power1:       54.00 W  (cap = 290.00 W)
```

This of course also means that it overheats much faster in subsequent executions.  It remains hot until we reboot the machine, which makes little sense to me.  Is this normal?  Should the critical temperature for the memory be increased?

---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-05-12T06:48:50Z)

Thanks @athas for reaching out.
Can you please share the OpenCL code/program that you used(share me the steps too to run the program), so that I will try here locally and will try to reproduce the problem.
Thank you.

---

### 评论 #2 — athas (2021-05-12T08:09:07Z)

My reproducer is a generated (so impractically large) program: https://sigkill.dk/junk/sum.c

Compile with `gcc sum.c -o sum -lOpenCL -lm` and run as `echo 1000 1000000000 | ./sum`.  The first number is the count of runs, and the second the number of `f32` floats that are summed.  I can try to write a smaller program if that would be useful.

---

### 评论 #3 — ROCmSupport (2021-05-12T08:27:38Z)

Thanks @athas for the details. They are helpful.
I tried on MI25 +ROCm 4.1.1 now and please find the results here.

Before running the OpenCL program, temperatures were low like 47, 47 and 47 degrees for edge, junction and memory.
While program is running, temperatures increased to 54, 68 and 68 respectively.
Once after program is finished, temperatures again down to 43, 43 and 43 respectively.
So I can say that temperature values are good for MI25.

I am trying to check it on MI100 also and will update you. 
Thank you.

---

### 评论 #4 — ROCmSupport (2021-05-12T08:59:43Z)

Hi @athas 
I tried it on MI100*2 cards now with the latest ROCm 4.2 GA.
Please find the results below.

Below program runs, the temperature values are: 32, 34 and 32 degrees of edge, junction and memory values respectively.
While the program is running, temperature values increased to: 39, 52 and 55 respectively
Once program completed, again temperature values came down to 34, 36 and 32 respectively.

So I wish to say that its working good in my machine.
After program is completed, I just rebooted my machine and its working good and showing low temperature values after reboot also.

Conclusions:
1. Most likely problem with your cards. Might be some hardware problem.
2. Might be VBIOS problem also, not sure, you might need to try with the latest VBIOS.
3. Recommend to try with the latest ROCm 4.2 GA also once and compare.

Thank you.

---

### 评论 #5 — athas (2021-05-12T09:23:24Z)

I'll try with ROCm 4.2 once it percolates its way to the RPM repositories (which I think is now/soon).  How do I try the lastest VBIOS?  Is it part of ROCm itself?

---

### 评论 #6 — athas (2021-05-26T20:46:51Z)

Sadly ROCm 4.2 made no difference.  I guess the card or sensor must be defective.

---

### 评论 #7 — ROCmSupport (2021-06-02T11:53:24Z)

Thanks @athas.
So I will close this issue as its no longer related to ROCm.
Thank you.

---

### 评论 #8 — athas (2021-06-15T09:25:07Z)

In case anyone comes across this issue later, we mitigated it by setting the fans in the chassis to maximum.  I don't know whether the machine as a whole was misconfigured in the first place, or whether the MI100 just requires more airflow than the A100 we have in an otherwise identical machine, but it seems stable now.

---

### 评论 #9 — sunway513 (2022-03-07T03:37:38Z)

> In case anyone comes across this issue later, we mitigated it by setting the fans in the chassis to maximum. I don't know whether the machine as a whole was misconfigured in the first place, or whether the MI100 just requires more airflow than the A100 we have in an otherwise identical machine, but it seems stable now.

It seems like the systems was not properly configured to read MI100 GPU temperature, hence can not adjust the fan speeds when GPUs are under loads.. The issue should be reported to the system provider and they should be able to get it properly fixed.. 

---
