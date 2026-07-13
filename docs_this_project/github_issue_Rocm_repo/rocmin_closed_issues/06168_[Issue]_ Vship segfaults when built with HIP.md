# [Issue]: Vship segfaults when built with HIP

- **Issue #:** 6168
- **State:** closed
- **Created:** 2026-04-21T11:39:36Z
- **Updated:** 2026-06-01T20:10:40Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6168

### Problem Description

Hi, I am the developper of https://codeberg.org/Line-fr/Vship/releases
Since around 6 months, I have seen reports on issues on my repo that did not exist before, with gpu segfault. This was at first specific to some configurations of OS and HW. However, This has now been spreading over every configurations and more specifically windows even. It seems to be related to amd driver updates. Countless errors of that type have been happening on the ROCm repo. I believe Vship is a nice case study here because it is directly written in HIP, no ROCm library call or python intermediate or anything.
Recently I have also seens errors that do not result in crash but the program always return perfect score.

Reasons why I am convinced it's not an issue in vship:
- The vulkan implementation (which is sort of copy pasted from the hip one) works like a charm
- The cuda version which is litteraly a C preprocessed version of the hip code works and pass every cuda memcheck tests/synccheck or anything with success
- It works on machine using relatively older amd drivers versions like my ubuntu 24

This is getting out of hand and I believe in my next release I will actively discourage people from using the HIP version (even though it is faster than the vulkan version). I hope that you will be able to resolve this issue.

### Operating System

Windows & Linux (arch, cachyOS, ...)

### CPU

Any

### GPU

Any, but specifically observed on RX 7900XTX, RX 9070XT for example

### ROCm Version

Observed at first on ROCm 7 but also on ROCm 6.2 (it seems to come from a driver and not ROCm)

### ROCm Component

HIP

### Steps to Reproduce

- Use relatively recent amd drivers (or even eventually a windows)
- install ffvship HIP backend
there is a good chance you'll get issues (running ffvship on 2 different videos may give > 99 SSIMULACRA2 or might segfault and crash the graphical driver)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

This is a following on a previous issue that I posted accompagnied by one of the first case of this, now it happens to so many people I am redoing this issue.

Vship uses relatively simple HIP features, most notably Streams if it matters here.