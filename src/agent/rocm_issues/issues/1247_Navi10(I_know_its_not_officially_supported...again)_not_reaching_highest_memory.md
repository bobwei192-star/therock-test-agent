# Navi10(I know its not officially supported...again) not reaching highest memory state when overclocked.

> **Issue #1247**
> **状态**: closed
> **创建时间**: 2020-09-28T08:36:13Z
> **更新时间**: 2020-12-03T12:13:03Z
> **关闭时间**: 2020-12-03T12:13:03Z
> **作者**: ddobreff
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1247

## 描述

Hello, since 3.8.0 was released, when you use pp_od_clk_voltage and overclock memory above stock(875) it results in this:
 cat pp_dpm_mclk
```
0: 100Mhz
1: 500Mhz
2: 625Mhz *
3: 900Mhz
```
Only way to bypass limitation is to use manual performance state but for my line of work it's unstable. Using ROCm 3.5.1 has no such issue.
Reproduce by using:
```
echo "s 1 1460" > pp_od_clk_voltage
echo "m 1 900" > pp_od_clk_voltage
echo "vc 2 1460 800" > pp_od_clk_voltage
echo c > pp_od_clk_voltage
```
I was about to submit this to amd official gitlab issues but yet again, I have no idea which commit breaks it or series.


---

## 评论 (2 条)

### 评论 #1 — ddobreff (2020-09-30T08:22:19Z)

Update: Seems like Fine graned DPM is not working correct, when pptable is set to enable SnapToDiscrete and NumDiscreteLevels = NUM_UCLK_DPM_LEVELS in DpmDescriptor[SMU_11_0_PPCLOCK_UCLK] it all works normally and mclk is at its highest dpm.

---

### 评论 #2 — rkothako (2020-11-18T08:42:12Z)

Hi @ddobreff 
As we are not officially supporting navi10 for rocm, we can not comment.
Thank you.

---
