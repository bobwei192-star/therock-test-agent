# hipfort install fails with trying to overwrite '/opt/rocm-3.9.0/bin/gputable.txt', which is also in package openmp-extras

> **Issue #1267**
> **状态**: closed
> **创建时间**: 2020-10-28T22:30:04Z
> **更新时间**: 2020-10-30T19:28:32Z
> **关闭时间**: 2020-10-30T19:28:32Z
> **作者**: jeffhammond
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1267

## 描述

I tried an install from scratch following https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu.

This is how I got there:
```
sudo apt update
sudo apt dist-upgrade
wget -q -O - http://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms
sudo apt-get install hipify-clang hipfort hipcub hipblas hipsparse miopen-hip
```
This is the error:
```
$ sudo apt-get install hipify-clang hipfort hipcub hipblas hipsparse 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
hipblas is already the newest version (0.36.0.0-rocm-rel-3.9-17-e4d9e7b).
hipcub is already the newest version (2.10.5.0-rocm-rel-3.9-17-7bda2e4).
hipify-clang is already the newest version (12.0.0).
hipsparse is already the newest version (1.9.4.0-rocm-rel-3.9-17-c5e4633).
The following NEW packages will be installed:
  hipfort
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
8 not fully installed or removed.
Need to get 0 B/699 kB of archives.
After this operation, 1,025 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
(Reading database ... 354918 files and directories currently installed.)
Preparing to unpack .../hipfort_0.2-0.33-rocm-rel-3.9-17-0b90b4d_amd64.deb ...
Unpacking hipfort (0.2-0.33-rocm-rel-3.9-17-0b90b4d) ...
dpkg: error processing archive /var/cache/apt/archives/hipfort_0.2-0.33-rocm-rel-3.9-17-0b90b4d_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-3.9.0/bin/gputable.txt', which is also in package openmp-extras 12.9-0
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/hipfort_0.2-0.33-rocm-rel-3.9-17-0b90b4d_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
# Linux
```
$ uname -a
Linux jrhammon-nuc 5.4.0-52-generic #57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/*release*
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.1 LTS"
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.1 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

# Hardware
I have Vega M in a Hades Canyon NUC.
```
$ lscpu
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   39 bits physical, 48 bits virtual
CPU(s):                          8
On-line CPU(s) list:             0-7
Thread(s) per core:              2
Core(s) per socket:              4
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           158
Model name:                      Intel(R) Core(TM) i7-8809G CPU @ 3.10GHz
Stepping:                        9
CPU MHz:                         800.020
CPU max MHz:                     8300.0000
CPU min MHz:                     800.0000
BogoMIPS:                        6199.99
Virtualization:                  VT-x
L1d cache:                       128 KiB
L1i cache:                       128 KiB
L2 cache:                        1 MiB
L3 cache:                        8 MiB
NUMA node0 CPU(s):               0-7
Vulnerability Itlb multihit:     KVM: Mitigation: Split huge pages
Vulnerability L1tf:              Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable
Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT vulnerable
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Full generic retpoline, IBPB conditional, IBRS_FW, STIBP conditional, RSB filling
Vulnerability Srbds:             Mitigation; Microcode
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch
                                 _perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2
                                 apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexprior
                                 ity ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hw
                                 p hwp_notify hwp_act_window hwp_epp md_clear flush_l1d
```

---

## 评论 (1 条)

### 评论 #1 — pramenku (2020-10-30T19:28:01Z)

Issue will be fixed in next release. It's know in current release. Please stay tuned.

Please follow https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#known-issues 
for workaround for the time being.

---
