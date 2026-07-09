# [Issue]: [rocm-opencl] DaVinci Resolve - CTDs with ROCm 7.2

- **Issue #:** 5970
- **State:** closed
- **Created:** 2026-02-16T15:35:49Z
- **Updated:** 2026-04-07T13:14:38Z
- **Labels:** status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5970

### Problem Description

Several end users are reporting that ROCm 7.2 introduces an issue with the DFP application [Davinci Resolve Studio](https://www.blackmagicdesign.com/products/davinciresolve/studio).

They note that rolling back to ROCm 7.11 works around these failures. There are several posts describing this issue across various forums and communities:

- [Lemmy.world | PSA for those using DaVinci Resolve with AMD GPUs, don't install ROCM 7.2, stay on 7.1.1](https://lemmy.world/post/43115302)
- [EndeavourOS Forums | Can´t use Davinci Resolve Studio | Crash to Desktop](https://forum.endeavouros.com/t/can-t-use-davinci-resolve-studio-crash-to-desktop/77870/11)
- [ArchLinux Pacages | davinci-resolve-studio 20.3.2-1](https://aur.archlinux.org/packages/davinci-resolve-studio#comment-1058336)

The last resource notes:

<img width="1241" height="165" alt="Image" src="https://github.com/user-attachments/assets/59164246-c943-4143-a223-4584a84d2671" />

...this seems to be related to rocm-opencl in the 7.2 package.

I'll borrow one of the system configurations from the forum posts as I've not directly reproduced the issue.

(any AMDers with questions can reach out to Vik (UserExp.&StrategyUK) on teams)

### Operating System

EndeavourOS

### CPU

AMD Ryzen 5 3600

### GPU

EndeavourOS Graphics card: AMD

### ROCm Version

ROCm 7.2

### ROCm Component

_No response_

### Steps to Reproduce

1. (Borrowing repro steps from https://forum.endeavouros.com/t/can-t-use-davinci-resolve-studio-crash-to-desktop/77870 )
2. Provision any contemporary linux distro with hw / sw support for ROCm 7.2. Ubuntu should reproduce this issue as well as others
3. Install DaVinci Resolve Studio (will require sign-up)
4. Launch DaVinci Resolve Studio and create a new project
5. Once the environment has loaded, attempt to import any video, or click on the cut or edit menu options
6. Observe CTD

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Console & log output:
```[sfox~]$ /opt/resolve/bin/resolve  
ActCCMessage Already in Table: Code= c005, Mode= 13, Level=  1, CmdKey= -1, Option= 0  
ActCCMessage Already in Table: Code= c006, Mode= 13, Level=  1, CmdKey= -1, Option= 0  
ActCCMessage Already in Table: Code= c007, Mode= 13, Level=  1, CmdKey= -1, Option= 0  
ActCCMessage Already in Table: Code= 2282, Mode=  0, Level=  0, CmdKey= 8, Option= 0  
20.3.1.0006 Linux/Clang x86_64  
Main thread starts: D71D0000  
0x7fd5d71d0000 | Undefined            | INFO  | 2026-01-30 16:11:01,630 | --------------------------------------------------------------------------------  
0x7fd5d71d0000 | Undefined            | INFO  | 2026-01-30 16:11:01,630 | Loaded log config from /home/sfox/.local/share/DaVinciResolve/configs/log-conf.xml  
0x7fd5d71d0000 | Undefined            | INFO  | 2026-01-30 16:11:01,630 | --------------------------------------------------------------------------------  
FusionScript Server [36924] Started  
Host 'Resolve' [36476] Added  
Host 'Resolve' Killed  
FusionScript Server [36924] Terminated  
[sfox~]$



==========[CRASH DUMP]==========  
#TIME Fri Jan 30 16:00:08 2026 - Uptime 00:00:15 (hh:mm:ss)  
#PROGRAM_NAME DaVinci Resolve Studio v20.3.1.0006 (Linux/Clang x86_64)  
#BMD_ARCHITECTURE x86_64  
#BMD_BUILD_UUID 5f90fb54-d661-4f14-9db1-3148eb6eb0f  
#BMD_GIT_COMMIT d031039b09e055f0d8d437a51ff3d87f364f4765  
#BMD_UTIL_VERSION 20.3.1.0006  
#OS Linux  
  
/opt/resolve/bin/resolve() [0x6087e49]  
/opt/resolve/bin/resolve() [0x6087012]  
/usr/lib/libc.so.6(+0x3e4d0) [0x7f4543c4d4d0]  
/opt/resolve/bin/../libs/libProResRAW.so(_ZNSt10filesystem7__cxx114path14_M_split_cmptsEv+0x38) [0x7f45358da708]  
/usr/lib/libRusticlOpenCL.so.1(+0xb17c39) [0x7f44e9517c39]  
/usr/lib/libRusticlOpenCL.so.1(+0xb1fcea) [0x7f44e951fcea]  
/usr/lib/libRusticlOpenCL.so.1(+0xb109b6) [0x7f44e95109b6]  
/usr/lib/libRusticlOpenCL.so.1(+0x25a902) [0x7f44e8c5a902]  
/usr/lib/libRusticlOpenCL.so.1(+0x235bf7) [0x7f44e8c35bf7]  
/usr/lib/libRusticlOpenCL.so.1(+0x2350a4) [0x7f44e8c350a4]  
/usr/lib/libRusticlOpenCL.so.1(+0x170400) [0x7f44e8b70400]  
/usr/lib/libRusticlOpenCL.so.1(+0x4039e5) [0x7f44e8e039e5]  
/usr/lib/libRusticlOpenCL.so.1(+0x44c2dd) [0x7f44e8e4c2dd]  
/usr/lib/libc.so.6(+0x9698b) [0x7f4543ca598b]  
/usr/lib/libc.so.6(+0x11aa0c) [0x7f4543d29a0c]  
Signal Number = 11  
  
================================