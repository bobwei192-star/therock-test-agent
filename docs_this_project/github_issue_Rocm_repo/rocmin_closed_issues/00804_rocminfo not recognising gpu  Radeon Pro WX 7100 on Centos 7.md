# rocminfo not recognising gpu  Radeon Pro WX 7100 on Centos 7

- **Issue #:** 804
- **State:** closed
- **Created:** 2019-05-22T06:06:59Z
- **Updated:** 2019-05-24T11:03:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/804

$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/sandbox-centos/rocm-rel-2.1/rocm-2.1-96-20190201/centos/rocminfo/rocminfo.cc. Call returned 4104


[rocm@rocm ~]$ dmesg | grep kfd
[    2.558244] kfd kfd: Initialized module
[    2.562957] kfd kfd: skipped device 1002:67c4, PCI rejects atomics
[    3.359595] kfd kfd: skipped device 1002:67c4, PCI rejects atomics


[rocm@rocm ~]$ dkms status
amdgpu, 19.10-782345.el7, 3.10.0-957.el7.x86_64, x86_64: built (original_module exists)
amdgpu, 2.4-25.el7, 3.10.0-957.12.2.el7.x86_64, x86_64: installed (original_module exists)
amdgpu, 2.4-25.el7, 3.10.0-957.el7.x86_64, x86_64: installed (original_module exists)



-[0000:00]-+-00.0  Intel Corporation 5500 I/O Hub to ESI Port
             +-01.0-[01-04]----00.0-[02-04]--+-08.0-[03]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon Pro WX 7100]
             |                               |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580]
             |                               \-10.0-[04]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon Pro WX 7100]
