# FR: allow fine-tuned voltage/frequency control

> **Issue #512**
> **状态**: closed
> **创建时间**: 2018-08-23T23:37:38Z
> **更新时间**: 2019-01-04T00:05:18Z
> **关闭时间**: 2019-01-04T00:05:18Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/512

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

amdgpu-pro allows setting the frequency and voltage per power state by writing to 
/sys/class/drm/card0/device/pp_od_clk_voltage, e.g.:
echo "s 4 900 1050" > pp_od_clk_voltage
echo c > pp_od_clk_voltage
as described here:
https://www.reddit.com/r/Amd/comments/8weeln/you_can_undervolt_vegas_in_linux_now/

Could ROCm offer a similar functionality?


---

## 评论 (4 条)

### 评论 #1 — preda (2018-08-24T00:45:06Z)

Similar to what is described in: https://github.com/RadeonOpenCompute/ROCm/issues/463
but could this be in ROCm "out of the box" instead of requiring custom compilation as described there.

---

### 评论 #2 — preda (2018-08-24T10:41:12Z)

Interesting, this seems to be working with ROCm 1.8.2 with Fiji GPUs, but not with Vega.
```
[  405.541346] amdgpu: [powerplay] pp_odn_edit_dpm_table was not implemented.
```

---

### 评论 #3 — preda (2018-08-24T11:29:25Z)

pp_od_clk_voltage also works "out of the box" in kernel 4.18 (Ubuntu 18.04). It would be so nice if the next ROCm would work on this kernel.. (4.18)

---

### 评论 #4 — preda (2019-01-04T00:05:18Z)

This seems to work with ROCm too, closing.

---
