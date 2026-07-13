# Wrong installation directory of rocprofiler-dev - /home/jenkins/jenkins-root/workspace

- **Issue #:** 628
- **State:** closed
- **Created:** 2018-11-27T21:55:32Z
- **Updated:** 2018-12-04T14:52:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/628

It was previously in /opt/rocm.

```
$ dpkg -L rocprofiler-dev
/home
/home/jenkins
/home/jenkins/jenkins-root
/home/jenkins/jenkins-root/workspace
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/bin
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/bin/rpl_run.sh
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/bin/tblextr.py
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/bin/txt2xml.sh
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/include
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/include/rocprofiler.h
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib/gfx_metrics.xml
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib/librocprofiler64.so.1.0.0
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib/metrics.xml
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/tool
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/tool/ctrl
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/tool/libtool.so
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/bin/rocprof
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib/librocprofiler64.so
/home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/out/ubuntu-16.04/16.04/lib/librocprofiler64.so.1
```
