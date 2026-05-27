# Wrong installation directory of rocprofiler-dev - /home/jenkins/jenkins-root/workspace

> **Issue #628**
> **状态**: closed
> **创建时间**: 2018-11-27T21:55:32Z
> **更新时间**: 2018-12-04T14:52:15Z
> **关闭时间**: 2018-12-04T14:52:15Z
> **作者**: misos1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/628

## 描述

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


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-12-04T02:33:44Z)

Thanks for catching this. This should be fixed now -- could you try uninstalling/reinstalling the `rocprofiler-dev` package? e.g. `sudo apt update; sudo apt remove rocprofiler-dev; sudo apt install rocprofiler-dev`

---
