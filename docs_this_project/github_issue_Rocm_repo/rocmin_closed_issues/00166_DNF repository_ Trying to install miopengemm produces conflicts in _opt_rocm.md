# DNF repository: Trying to install miopengemm produces conflicts in /opt/rocm

- **Issue #:** 166
- **State:** closed
- **Created:** 2017-07-19T16:32:23Z
- **Updated:** 2018-06-03T14:59:53Z
- **Labels:** Bug_Functional_Issue
- **Assignees:** pfultz2, dagamayank
- **URL:** https://github.com/ROCm/ROCm/issues/166

Hello again,

```
mmxgn@emerdesktop:~> sudo dnf install miopengemm
[sudo] password for mmxgn: 
Last metadata expiration check: 3:55:37 ago on Wed 19 Jul 2017 13:34:36 BST.
Dependencies resolved.
=========================================================================================================================================================================================================
 Package                                            Arch                                           Version                                          Repository                                      Size
=========================================================================================================================================================================================================
Installing:
 miopengemm                                         x86_64                                         1.0.1-1                                          remote                                         613 k

Transaction Summary
=========================================================================================================================================================================================================
Install  1 Package

Total size: 613 k
Installed size: 2.5 M
Is this ok [y/N]: y
Downloading Packages:
[SKIPPED] miopengemm-1.0.1-Linux.rpm: Already downloaded                                                                                                                                                
Running transaction check
Transaction check succeeded.
Running transaction test
The downloaded packages were saved in cache until the next successful transaction.
You can remove cached packages by executing 'dnf clean packages'.
Error: Transaction check error:
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_base-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsakmt-roct-dev-1.0.6_3_gd13b4e2-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hsa-ext-rocr-dev-1.1.6_21_g171a2d4-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-utils-1.0.0-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-profiler-5.1.6386-gbaddcc9.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_doc-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_samples-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package hip_hcc-1.2.17263-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm/include from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm/lib from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-device-libs-0.0.1-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-dev-1.6.77-1.x86_64
  file /opt/rocm from install of miopengemm-1.0.1-1.x86_64 conflicts with file from package rocm-1.6.77-1.x86_64

Error Summary
-------------

```

My rocm.repo:

```
Error Summary
-------------

mmxgn@emerdesktop:~> cat /etc/yum.repos.d/rocm.repo 
[remote]

name=ROCm Repo

baseurl=http://repo.radeon.com/rocm/yum/rpm/

enabled=1

gpgcheck=0


```

Kind regards,