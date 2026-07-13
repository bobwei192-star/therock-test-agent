# pp_table issue: sclk dependant on voltage on latest kernels

- **Issue #:** 433
- **State:** closed
- **Created:** 2018-06-13T19:41:01Z
- **Updated:** 2019-01-08T01:06:09Z
- **URL:** https://github.com/ROCm/ROCm/issues/433

There may be a new issue around pp_table on latest kernels.   I wanted to record it here in case it flows through to amdgpu-pro or rocm via dkms being loaded.

I was testing powerplay in kernel drm-next-4.19-wip.

I setup a pp_table on a couple vega64 cards for 1390mhz/1090mhz/900mv

Both cards say they are running those clocks (via /sys/class/drm/*)

```
# clocks
3: 1090Mhz *
7: 1390Mhz *
3: 1090Mhz *
7: 1390Mhz *
```

However, getting data from  /sys/kernel/debug/dri/*/amdgpu_pm_info,  its different.

```
1390/1090/900mv (4.17.0-rc5-20180610-drm-next-4.19-wip)

 ID       Name  Sclk  Mclk mVolt Watts  Temp   Fan
============================================================
  0   rxvega64  1334  1090   937   115    62   40%
  1   rxvega64  1316  1090   900   102    60   26%
============================================================
```

I dont have any idea where gpu #0 gets 937mv.  Not from pp_table, thats for sure.

I cant get to 1390mhz core unless I up voltage over 975mv.   Here is 925mv, 950mv, 975mv

```
============================================================
  1   rxvega64  1334  1090   925   117    63   37%
  1   rxvega64  1356  1090   950   129    62   48%
  1   rxvega64  1388  1090   975   137    62   37%
============================================================
```

Reverting back to 4.17.0-rc2-180424-fkxamd, what I set in pp_table is really happening

```
1390/1090/900mv (4.17.0-rc2-180424-fkxamd)

 ID       Name  Sclk  Mclk mVolt Watts  Temp   Fan
============================================================
  0   rxvega64  1390  1090   900   113    61   26%
  1   rxvega64  1390  1090   900   114    62   26%
============================================================
```



