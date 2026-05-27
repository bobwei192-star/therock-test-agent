# ROCm-1.3 linker problem.

> **Issue #47**
> **状态**: closed
> **创建时间**: 2016-11-12T05:51:57Z
> **更新时间**: 2016-11-30T05:26:47Z
> **关闭时间**: 2016-11-30T05:26:47Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/47

## 描述

I tried to build my code at [cs344 Problem Set 1](https://github.com/briansp2020/cs344/tree/master/Problem%20Sets/Problem%20Set%201) and I get errors.

> $ make
hipcc -o HW1 main.o student_func.o compare.o reference_calc.o -L /usr/lib -lopencv_core -lopencv_imgproc -lopencv_highgui -g -hc -std=c++amp
/opt/rocm/hcc-lc/compiler/bin/clamp-link: line 302: cd: /home/briansp/git/cs344/Problem: No such file or directory
objdump: 'main.o': No such file
objdump: 'student_func.o': No such file
objdump: 'compare.o': No such file
objdump: 'reference_calc.o': No such file
ld: cannot find main.o: No such file or directory
ld: cannot find student_func.o: No such file or directory
ld: cannot find compare.o: No such file or directory
ld: cannot find reference_calc.o: No such file or directory
clang-3.5: error: linker command failed with exit code 1 (use -v to see invocation)
Died at /opt/rocm/bin/hipcc line 365.
Makefile:37: recipe for target 'student' failed
make: *** [student] Error 1

Then, I copy the code to ~/dev/cs344 and it builds fine. It looks like the linker is not handling space in the path properly. I'm reporting it here since I'm not sure whether the linker is part of llvm or hcc or clang or lld.

---

## 评论 (4 条)

### 评论 #1 — gstoner (2016-11-12T15:48:12Z)

Is this 16.04. If so we found known issue in GCC tool supplied with 16.04.

Get Outlook for iOShttps://aka.ms/o0ukef

On Fri, Nov 11, 2016 at 11:52 PM -0600, "Brian" <notifications@github.com<mailto:notifications@github.com>> wrote:

I tried to build my code at cs344 Problem Set 1https://github.com/briansp2020/cs344/tree/master/Problem%20Sets/Problem%20Set%201 and I get errors.

$ make
hipcc -o HW1 main.o student_func.o compare.o reference_calc.o -L /usr/lib -lopencv_core -lopencv_imgproc -lopencv_highgui -g -hc -std=c++amp
/opt/rocm/hcc-lc/compiler/bin/clamp-link: line 302: cd: /home/briansp/git/cs344/Problem: No such file or directory
objdump: 'main.o': No such file
objdump: 'student_func.o': No such file
objdump: 'compare.o': No such file
objdump: 'reference_calc.o': No such file
ld: cannot find main.o: No such file or directory
ld: cannot find student_func.o: No such file or directory
ld: cannot find compare.o: No such file or directory
ld: cannot find reference_calc.o: No such file or directory
clang-3.5: error: linker command failed with exit code 1 (use -v to see invocation)
Died at /opt/rocm/bin/hipcc line 365.
Makefile:37: recipe for target 'student' failed
make: **\* [student] Error 1

Then, I copy the code to ~/dev/cs344 and it builds fine. It looks like the linker is not handling space in the path properly. I'm reporting it here since I'm not sure whether the linker is part of llvm or hcc or clang or lld.

## 

You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/47, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuQFv7dom3Amrn5qLxtleXrKcybofks5q9VP9gaJpZM4KwVh-.


---

### 评论 #2 — briansp2020 (2016-11-12T17:37:20Z)

Yes 16.04


---

### 评论 #3 — scchan (2016-11-12T18:56:58Z)

I opened a new issue against hcc (RadeonOpenCompute/hcc#161) and will continue to track it there


---

### 评论 #4 — briansp2020 (2016-11-30T05:26:47Z)

Looks like this is fixed in ROCm 1.3.1

---
