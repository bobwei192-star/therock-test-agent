# DNF repository: miopen-hip-1.0.0-1.x86_64 tries to pull nonexistent rocm-opencl-dev

- **Issue #:** 165
- **State:** closed
- **Created:** 2017-07-19T16:29:32Z
- **Updated:** 2018-06-03T14:49:40Z
- **Labels:** Bug_Functional_Issue
- **Assignees:** pfultz2, dagamayank
- **URL:** https://github.com/ROCm/ROCm/issues/165

Hello,

```
~> sudo dnf install miopen-hip
Last metadata expiration check: 3:48:39 ago on Wed 19 Jul 2017 13:34:36 BST.
Error: 
 Problem: conflicting requests
  - nothing provides rocm-opencl-dev needed by miopen-hip-1.0.0-1.x86_64

```
But rocm-opencl-devel exists instead:

```
mmxgn@emerdesktop:~> dnf search rocm-opencl-dev
Last metadata expiration check: 2:03:19 ago on Wed 19 Jul 2017 15:22:47 BST.
===================================================================================== 
Name Matched: rocm-opencl-dev
=====================================================================================
rocm-opencl-devel.x86_64 : OpenCL/ROCm
```

My rocm.repo

```
mmxgn@emerdesktop:~> cat /etc/yum.repos.d/rocm.repo 
[remote]

name=ROCm Repo

baseurl=http://repo.radeon.com/rocm/yum/rpm/

enabled=1

gpgcheck=0

```

Regards,