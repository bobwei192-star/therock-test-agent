# OpenCL enabled apps locks Raven Ridge APU to 399MHz on all cores

> **Issue #976**
> **状态**: closed
> **创建时间**: 2019-12-20T10:39:41Z
> **更新时间**: 2023-12-14T11:36:18Z
> **关闭时间**: 2023-12-14T11:36:17Z
> **作者**: btspce
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/976

## 描述

Raven Ridge APU downclocks and locks all cores at 399MHz as soon as certain OpenCL enabled applications is started and as long as they are running. ROCm 2.2 is used due to issue #768 

HP Elitebook 745 G5 with Raven Ridge 2700u APU and 32GB RAM
Fedora 31 x64 fully updated
CPU governor: default (ondemand)
Kernel: 5.3.16-300.fc31.x86_64
Darktable 2.6.3 (downclocks to 399MHz with or without OpenCL enabled)
Davinci Resolve 16.1.2 (downclocks to 399MHz with or without OpenCL enabled)
Both of these above checks for OpenCL at launch

Gimp 2.10 (does not downclock and works OpenCL enabled)
Setting CPU governor to performance does not help as long as the application is running.

Moving amdocl64.icd fixes the problem and Darktable does not lock the cpu cores to 399MHz but removes OpenCL support
`sudo mv /etc/OpenCL/vendors/amdocl64.icd ./amdocl64.icd.old`

Firefox running:
`$ sudo cpupower monitor

    | Mperf              || Idle_Stats         
 CPU| C0   | Cx   | Freq  || POLL | C1   | C2    
   0|  2.23| 97.77|  1282||  0.00|  2.00| 95.84
   1|  0.55| 99.45|  1324||  0.00|  1.04| 98.35
   2|  2.04| 97.96|  1278||  0.00|  3.33| 94.71
   3|  1.71| 98.29|  1281||  0.00|  3.41| 94.91
   4|  1.97| 98.03|  1318||  0.00|  0.41| 97.61
   5|  4.27| 95.73|  1249||  0.00|  4.24| 91.98
   6|  1.22| 98.78|  1274||  0.00|  3.52| 95.31
   7|  0.93| 99.07|  1300||  0.00|  0.67| 98.36`

Darktable or Davinci running:
`$ sudo cpupower monitor
    | Mperf              || Idle_Stats         
 CPU| C0   | Cx   | Freq  || POLL | C1   | C2    
   0| 13.06| 86.94|   398||  0.00| 11.26| 75.94
   1|  3.10| 96.90|   399||  0.00|  0.97| 95.95
   2| 17.40| 82.60|   398||  0.00| 15.85| 66.95
   3| 11.15| 88.85|   399||  0.00| 15.43| 73.57
   4| 11.32| 88.68|   398||  0.00| 11.99| 76.90
   5|  9.80| 90.20|   398||  0.00|  5.58| 84.81
   6| 10.55| 89.45|   399||  0.00|  6.63| 83.03
   7|  6.59| 93.41|   398||  0.00|  2.15| 91.41`

Below when running darktable or Davinci Resolve
`$ cat /proc/cpuinfo
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.072
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 1
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.217
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 0
cpu cores	: 4
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 2
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 398.946
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 1
cpu cores	: 4
apicid		: 2
initial apicid	: 2
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 3
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.243
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 1
cpu cores	: 4
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 4
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.221
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 2
cpu cores	: 4
apicid		: 4
initial apicid	: 4
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 5
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 398.974
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 2
cpu cores	: 4
apicid		: 5
initial apicid	: 5
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 6
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.141
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 3
cpu cores	: 4
apicid		: 6
initial apicid	: 6
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]

processor	: 7
vendor_id	: AuthenticAMD
cpu family	: 23
model		: 17
model name	: AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
stepping	: 0
microcode	: 0x8101016
cpu MHz		: 399.128
cache size	: 512 KB
physical id	: 0
siblings	: 8
core id		: 3
cpu cores	: 4
apicid		: 7
initial apicid	: 7
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb hw_pstate sme ssbd sev ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif overflow_recov succor smca
bugs		: sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
bogomips	: 4392.00
TLB size	: 2560 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 43 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]`

---

## 评论 (8 条)

### 评论 #1 — btspce (2019-12-20T17:02:08Z)

Samme issue on ROCm 2.9 which is the latest version where hsa-ext-rocr-dev works

---

### 评论 #2 — btspce (2019-12-20T22:16:21Z)

Found the problem:

$ rocm-smi -l

GPU[0] 		: 
GPU[0] 		: NUM        MODE_NAME BUSY_SET_POINT FPS USE_RLC_BUSY MIN_ACTIVE_LEVEL
GPU[0] 		:   0 BOOTUP_DEFAULT :             70  60          0              0
GPU[0] 		:   1 3D_FULL_SCREEN :             70  60          1              3
GPU[0] 		:   2   POWER_SAVING :             90  60          0              0
GPU[0] 		:   3          VIDEO :             70  60          0              0
GPU[0] 		:   4             VR :             70  90          0              0
GPU[0] 		:   5        COMPUTE*:             30  60          0              6

As long as the level is set to COMPUTE all cores on a Raven Ridge 2700u APU is downclocked to 399MHz and locked there making all programs unusable to work with as there is no cpu left. I guess this is to free resources/tdp for the GPU. Changing the level to 0,1,2,3 or 4 immediately let the cpu jump to ~1300Mhz and boost to 3GHz when required. Tested with Davinci Resolve 16 and Darktable.

---

### 评论 #3 — beatboxa (2019-12-21T21:29:04Z)

Still a no-go for me on Ubuntu.  

I tried manually (and completely) removing all rocm 2.2 packages, removing amdocl64.icd, installing comgr, and then manually installing the 3.0 packages, but my opencl shows:

> ERROR: clGetDeviceIDs(-1)

and DaVinci Resolve fails to launch.

Downgrading back to 2.2 fixes the issue for me.

---

### 评论 #4 — btspce (2019-12-22T19:59:29Z)

3.0 is not working. I made an error in an previous comment and ended up with both 2.2 repo and 3.0 in my rocm.repo after switching back and forth a few times. I have deleted my previous comment that stated that this was fixed.

---

### 评论 #5 — btspce (2020-04-24T18:14:07Z)

Still the same issue with 3.3. And I can no longer force the cpu clocks up again due to rocm-smi not working

$ sudo /opt/rocm-3.3.0/bin/rocm-smi --setprofile 3

========================ROCm System Management Interface========================
Traceback (most recent call last):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2995, in <module>
    setProfile(deviceList, args.setprofile)
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2434, in setProfile
    if writeProfileSysfs(device, profile):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 677, in writeProfileSysfs
    if not verifySetProfile(device, value):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 583, in verifySetProfile
    maxProfileLevel = getMaxLevel(device, 'profile')
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 856, in getMaxLevel
    return int(levels.splitlines()[-1][0])
ValueError: invalid literal for int() with base 10: ' '


---

### 评论 #6 — btspce (2020-05-03T20:13:46Z)

Can someone at AMD please check why ROCm behaves this way and tanks the performance at the same time. Using OpenCL extracted from amdgpu-pro does not do this and clocking for CPU and GPU works as expected but breaks OpenGL instead so we can't use that either.

---

### 评论 #7 — nartmada (2023-12-13T23:09:43Z)

Hi @btspce, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #8 — btspce (2023-12-14T11:36:17Z)

I don't have this laptop anymore so I can't verify if it is fixed. Closing for now.

---
