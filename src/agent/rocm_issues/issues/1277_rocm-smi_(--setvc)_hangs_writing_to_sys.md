# rocm-smi (--setvc) hangs writing to /sys

> **Issue #1277**
> **状态**: closed
> **创建时间**: 2020-11-06T09:01:01Z
> **更新时间**: 2020-11-18T07:32:32Z
> **关闭时间**: 2020-11-18T07:32:32Z
> **作者**: nirno
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1277

## 描述

When I run

    /opt/rocm-3.9.0/bin/rocm_smi_deprecated.py --device 1 --setvc 2 1750 800

it hangs indefinitely.  When I run strace on the process, it reveals:

    write(3, "vc 2 1750 800\n", 14)         = 0
    write(3, "vc 2 1750 800\n", 14)         = 0
    write(3, "vc 2 1750 800\n", 14)         = 0
    write(3, "vc 2 1750 800\n", 14)         = 0
    write(3, "vc 2 1750 800\n", 14)         = 0
... and so on, very rapidly.

IOW, rocm-smi has entered an infinite loop.

Using lsof, I find out the file rocm-smi is writing to: it is

    /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/0000:02:00.0/0000:03:00.0/pp_od_clk_voltage

When I now try to write to the same file manually:

    echo 'vc 2 1750 800' > /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/0000:02:00.0/0000:03:00.0/pp_od_clk_voltage

the command hangs too.  Running the same command under strace, I see:

    write(1, "vc 2 1750 800\n", 14)         = 0
    write(1, "vc 2 1750 800\n", 14)         = 0
    write(1, "vc 2 1750 800\n", 14)         = 0
    write(1, "vc 2 1750 800\n", 14)         = 0
    write(1, "vc 2 1750 800\n", 14)         = 0
    write(1, "vc 2 1750 800\n", 14)         = 0
... and so on.

The shell does not respond to ^C, and it cannot be killed with simple 'kill' from another shell; I can only get rid of it by 'kill -9'.

At the same time, the command has succeeded, in the sense that when I look at the values with ``rocm_smi_deprecated.py --showvc``, I see that the new value is in effect.

This means that I can change voltage parameters of the GPU manually, but it would be cumbersome to do it from non-interactive  scripts.  (Although I guess it would be still possible: run the command in a subshell in the background, kill the subshell after a short time, check values.)

What's going on?   (Why does write() return 0 instead of 14 (number of bytes written))?  What am I doing wrong or what is wrong with my system?  How to set the values without getting stuck in infinite loops?

I am running Ubuntu 20.04 (focal) on Linux 5.4.0-52-generic, with three Radeon RX 5700 cards.

Thanks and regards,
T.


---

## 评论 (2 条)

### 评论 #1 — rkothako (2020-11-06T09:48:43Z)

Hi @nirno 
Thanks for reaching us.
Currently we are not supporting Navi10 series of cards for ROCm.
Please look @ [1271 ](https://github.com/RadeonOpenCompute/ROCm/issues/1271) for more information.

---

### 评论 #2 — rkothako (2020-11-09T05:55:59Z)

Hi @nirno 
Request to close this issue as per the comments above.
Please reach if you need anymore information.

---
