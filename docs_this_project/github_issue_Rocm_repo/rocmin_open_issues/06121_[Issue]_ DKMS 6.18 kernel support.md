# [Issue]: DKMS 6.18 kernel support

- **Issue #:** 6121
- **State:** open
- **Created:** 2026-04-06T04:11:06Z
- **Updated:** 2026-04-10T22:21:41Z
- **Labels:** AMD Radeon RX 7900 XTX, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6121

### Problem Description

Please add support the latest `stable` Linux `6.18` kernel.

```py
In file included from ./amd/amdgpu/../backport/backport.h:30,
                 from <command-line>:
././include/kcl/kcl_preempt.h:57:29: error: static declaration of ‘migrate_disable’ follows non-static declaration
   57 | static __always_inline void migrate_disable(void)
      |                             ^~~~~~~~~~~~~~~
In file included from /home/diego/linux-6.18.15/include/linux/percpu.h:12,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/msr.h:16,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/tsc.h:11,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/timex.h:6,
                 from /home/diego/linux-6.18.15/include/linux/timex.h:67,
                 from /home/diego/linux-6.18.15/include/linux/time32.h:13,
                 from /home/diego/linux-6.18.15/include/linux/time.h:60,
                 from /home/diego/linux-6.18.15/include/linux/stat.h:19,
                 from /home/diego/linux-6.18.15/include/linux/module.h:13,
                 from ././include/kcl/kcl_moduleparam.h:5,
                 from ./amd/amdgpu/../backport/backport.h:7:
/home/diego/linux-6.18.15/include/linux/sched.h:2430:13: note: previous declaration of ‘migrate_disable’ with type ‘void(void)’
 2430 | extern void migrate_disable(void);
      |             ^~~~~~~~~~~~~~~
././include/kcl/kcl_preempt.h:61:29: error: static declaration of ‘migrate_enable’ follows non-static declaration
   61 | static __always_inline void migrate_enable(void)
      |                             ^~~~~~~~~~~~~~
/home/diego/linux-6.18.15/include/linux/sched.h:2431:13: note: previous declaration of ‘migrate_enable’ with type ‘void(void)’
 2431 | extern void migrate_enable(void);
      |             ^~~~~~~~~~~~~~
  CC [M]  amd/amdgpu/aldebaran.o
  CC [M]  amd/amdgpu/soc21.o
  CC [M]  amd/amdgpu/soc24.o
In file included from ./amd/amdgpu/../backport/backport.h:30,
                 from <command-line>:
././include/kcl/kcl_preempt.h:57:29: error: static declaration of ‘migrate_disable’ follows non-static declaration
   57 | static __always_inline void migrate_disable(void)
      |                             ^~~~~~~~~~~~~~~
In file included from /home/diego/linux-6.18.15/include/linux/percpu.h:12,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/msr.h:16,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/tsc.h:11,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/timex.h:6,
                 from /home/diego/linux-6.18.15/include/linux/timex.h:67,
                 from /home/diego/linux-6.18.15/include/linux/time32.h:13,
                 from /home/diego/linux-6.18.15/include/linux/time.h:60,
                 from /home/diego/linux-6.18.15/include/linux/stat.h:19,
                 from /home/diego/linux-6.18.15/include/linux/module.h:13,
                 from ././include/kcl/kcl_moduleparam.h:5,
                 from ./amd/amdgpu/../backport/backport.h:7:
/home/diego/linux-6.18.15/include/linux/sched.h:2430:13: note: previous declaration of ‘migrate_disable’ with type ‘void(void)’
 2430 | extern void migrate_disable(void);
      |             ^~~~~~~~~~~~~~~
././include/kcl/kcl_preempt.h:61:29: error: static declaration of ‘migrate_enable’ follows non-static declaration
   61 | static __always_inline void migrate_enable(void)
      |                             ^~~~~~~~~~~~~~
/home/diego/linux-6.18.15/include/linux/sched.h:2431:13: note: previous declaration of ‘migrate_enable’ with type ‘void(void)’
 2431 | extern void migrate_enable(void);
      |             ^~~~~~~~~~~~~~
  CC [M]  amd/amdgpu/sienna_cichlid.o
In file included from ./amd/amdgpu/../backport/backport.h:30,
                 from <command-line>:
././include/kcl/kcl_preempt.h:57:29: error: static declaration of ‘migrate_disable’ follows non-static declaration
   57 | static __always_inline void migrate_disable(void)
      |                             ^~~~~~~~~~~~~~~
In file included from /home/diego/linux-6.18.15/include/linux/percpu.h:12,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/msr.h:16,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/tsc.h:11,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/timex.h:6,
                 from /home/diego/linux-6.18.15/include/linux/timex.h:67,
                 from /home/diego/linux-6.18.15/include/linux/time32.h:13,
                 from /home/diego/linux-6.18.15/include/linux/time.h:60,
                 from /home/diego/linux-6.18.15/include/linux/stat.h:19,
                 from /home/diego/linux-6.18.15/include/linux/module.h:13,
                 from ././include/kcl/kcl_moduleparam.h:5,
                 from ./amd/amdgpu/../backport/backport.h:7:
/home/diego/linux-6.18.15/include/linux/sched.h:2430:13: note: previous declaration of ‘migrate_disable’ with type ‘void(void)’
 2430 | extern void migrate_disable(void);
      |             ^~~~~~~~~~~~~~~
././include/kcl/kcl_preempt.h:61:29: error: static declaration of ‘migrate_enable’ follows non-static declaration
   61 | static __always_inline void migrate_enable(void)
      |                             ^~~~~~~~~~~~~~
/home/diego/linux-6.18.15/include/linux/sched.h:2431:13: note: previous declaration of ‘migrate_enable’ with type ‘void(void)’
 2431 | extern void migrate_enable(void);
      |             ^~~~~~~~~~~~~~
amd/amdkcl/kcl_suspend.c:32:6: warning: no previous prototype for ‘amdkcl_suspend_init’ [-Wmissing-prototypes]
   32 | void amdkcl_suspend_init(void)
      |      ^~~~~~~~~~~~~~~~~~~
  CC [M]  amd/amdgpu/smu_v13_0_10.o
In file included from ./amd/amdgpu/../backport/backport.h:30,
                 from <command-line>:
././include/kcl/kcl_preempt.h:57:29: error: static declaration of ‘migrate_disable’ follows non-static declaration
   57 | static __always_inline void migrate_disable(void)
      |                             ^~~~~~~~~~~~~~~
In file included from /home/diego/linux-6.18.15/include/linux/percpu.h:12,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/msr.h:16,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/tsc.h:11,
                 from /home/diego/linux-6.18.15/arch/x86/include/asm/timex.h:6,
                 from /home/diego/linux-6.18.15/include/linux/timex.h:67,
                 from /home/diego/linux-6.18.15/include/linux/time32.h:13,
                 from /home/diego/linux-6.18.15/include/linux/time.h:60,
                 from /home/diego/linux-6.18.15/include/linux/stat.h:19,
                 from /home/diego/linux-6.18.15/include/linux/module.h:13,
                 from ././include/kcl/kcl_moduleparam.h:5,
                 from ./amd/amdgpu/../backport/backport.h:7:
/home/diego/linux-6.18.15/include/linux/sched.h:2430:13: note: previous declaration of ‘migrate_disable’ with type ‘void(void)’
 2430 | extern void migrate_disable(void);
      |             ^~~~~~~~~~~~~~~
././include/kcl/kcl_preempt.h:61:29: error: static declaration of ‘migrate_enable’ follows non-static declaration
   61 | static __always_inline void migrate_enable(void)
      |                             ^~~~~~~~~~~~~~
/home/diego/linux-6.18.15/include/linux/sched.h:2431:13: note: previous declaration of ‘migrate_enable’ with type ‘void(void)’
```



### Operating System

Ubuntu 24.0

### CPU

AMD ZEN3

### GPU

7900 XTX

### ROCm Version

Latest Stable

### ROCm Component

_No response_

### Steps to Reproduce

Install amdgpu-dkms under LInux 6.18.*


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_