# Does powerplay still work in ROCm 3.8?

> **Issue #1228**
> **状态**: closed
> **创建时间**: 2020-09-22T09:21:04Z
> **更新时间**: 2020-12-14T06:18:42Z
> **关闭时间**: 2020-12-03T07:48:23Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1228

## 描述

Before it was possible to undervolt or otherwise tweak the voltage/frequency with powerplay, e.g. by writing to 
/sys/class/drm/card0/device/pp_od_clk_voltage

(to enable PP one had to boot with amdgpu.ppfeaturemask=0xffffffff or similar)

Did ROCm 3.8 change the way PP works? is it still possible to tweak voltage/frequency -- in a different way / how?


---

## 评论 (5 条)

### 评论 #1 — valeriob01 (2020-09-22T10:14:58Z)

This is how I set frequency, maybe it still works?

```
/opt/rocm-3.3.0/bin/rocm-smi --resetprofile
/opt/rocm-3.3.0/bin/rocm-smi --setsclk 8
/opt/rocm-3.3.0/bin/rocm-smi --setmclk 2
/opt/rocm-3.3.0/bin/rocm-smi --autorespond y --setoverdrive 2
/opt/rocm-3.3.0/bin/rocm-smi --autorespond y --setmemoverdrive 10

```


---

### 评论 #2 — kentrussell (2020-11-18T11:54:01Z)

PP has been undergoing changes, but it should still be possible to adjust the voltages and frequency. What do you get when you cat the pp_od_clk_voltage file?

---

### 评论 #3 — ROCmSupport (2020-12-03T07:47:37Z)

Hi @preda 
It should work as the same way you tried.

---

### 评论 #4 — preda (2020-12-12T09:59:34Z)

Yes, I think everything is fine and it works, it must have been that I forgot to add "amdgpu.ppfeaturemask=0xffffffff" to /etc/default/grub


---

### 评论 #5 — ROCmSupport (2020-12-14T06:18:41Z)

Thanks @preda for the update.

---
