# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

- **Issue #:** 617
- **State:** closed
- **Created:** 2018-11-19T07:28:08Z
- **Updated:** 2019-03-11T04:19:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/617

I've tried most of the solution suggestions from similar issues, but it doesn't seem to resolve this issue. 
Btw, the error is not stable. /opt/rocm/bin/rocminfo works at times. 

Details: 
Vega, Ubuntu 16.04

dkms status
amdgpu, 1.9-224, 4.15.0-38-generic, x86_64: installed
amdgpu, 1.9-224, 4.15.0-39-generic, x86_64: installed

uname -a
Linux All-Series 4.15.0-39-generic #42~16.04.1-Ubuntu SMP Wed Oct 24 17:09:54 UTC 2018 x86_64 x86_64 x86_64

