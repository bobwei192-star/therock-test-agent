# Reference to closed issue without being resolved

> **Issue #1377**
> **状态**: closed
> **创建时间**: 2021-02-11T02:25:35Z
> **更新时间**: 2021-04-08T11:38:34Z
> **关闭时间**: 2021-04-08T11:38:34Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1377

## 描述

I revisited this issue which was closed without resolving.
ROCclr build issue, make failed. #1358

It was closed because it is waited too long. Waiting too long does not resolve the issue, why you (rocm-support) think doing so will resolve the issue itself?
This will cause test escape and problem to escape and only to regress later. 

I have revisited the problem and found the problem for you at no cost when rocm-support did not root cause but instead chose to close.
The export statement in the README is wrong and does not set path correct. Please revisit the closed one and found yourself. 

It should be rocm-support's responsibility to root cause not me and test their solution on their end not me as submitter. 
I was able to build but I am not going to post the solution as it should have been your responsibility. 
You should not close this one either until instruction is corrected in the README that led to a successfull build no longer how long the issue stays dormant. Because otherwise you dont root cause, yet you close the issue when the problem exist, that is bad practice for rocm-support. 




---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-02-11T07:06:55Z)

Thanks @gggh000 
We have not closed intentionally.
As we did follow up with you for 3 times and as there was no response, it was closed.
Atleast we request you to put some response so that the ticket will be active until its resolved.

Reg the real issue:
We always wish to keep our documentation perfect and we word hard towards maintaining good documentation.
We already shaped up our docs in a better way and we are still working on improvements.
There might be still some issues and we are always ready to resolve whenever found.

Thank you.



---

### 评论 #2 — ROCmSupport (2021-02-11T07:58:09Z)

And also I am not able to reproduce this issue anytime.

Before that I installed ROCm using apt install rocm-dkms and then I blindly followed steps given in _https://github.com/ROCm-Developer-Tools/ROCclr_ and all went well for me.

Can you please point me to the exact problem so that I will try for resolution asap.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-02-11T15:15:32Z)

Kindly find the logs attached.  
When I said we are not able to reproduce we mean it. 
We can solve anything when there is any problem. If there is no problem witness by us we cannot solve the same.

[OpenCL_compilation_logs.txt](https://github.com/RadeonOpenCompute/ROCm/files/5966344/OpenCL_compilation_logs.txt)


---

### 评论 #4 — gggh000 (2021-02-12T00:08:28Z)

Your compilation is half baked. there is no way it can compile following the instruction without satisfying prerequisite in the README file in the 4.0x. You did not even include what you did for satisfying prereq. I am not satisfied with your response. 

---

### 评论 #5 — gggh000 (2021-02-12T00:10:13Z)

Here is the original log, I am wasting so much time on your trying to explain what is wrong with the build instruction.

I filed this bug here since there seems no ROCclr project on its own.
I downloaded source for 4.0.0 but ROCclr build problem.

I built and installed llvm, ROCm-Compiler-support and ROCm-device-libs ok as prereq.

But build instruction for ROCclr as follows:

Set the environment variables
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
Build ROCclr
Here is command to build ROCclr:

cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)
It appears settings OPENCL_DIR is necessary. So i set the env variable and make sure it is ok (below).
But "make" command after cmake resulted in following error:

oot@sriov-guest:~/ROCm/ROCclr/build# env | grep ROCclr
OPENCL_DIR=/root/ROCm/ROCclr/build/ROCm-OpenCL-Runtime
OLDPWD=/root/ROCm/ROCclr
PWD=/root/ROCm/ROCclr/build
ROCclr_DIR=/root/ROCm/ROCclr/build/ROCclr

"root@sriov-guest:~/ROCm/ROCclr/build# make
[ 2%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o
In file included from /root/ROCm/ROCclr/device/rocm/roccounters.hpp:24:0,
from /root/ROCm/ROCclr/device/rocm/roccounters.cpp:21:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
#include "CL/opencl.h"
^~~~~~~~~~~~~
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:62: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/all' failed
make[1]: *** [device/rocm/CMakeFiles/oclrocm.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
"

I dont think building ROCm-OpenCL-Runtime is prereq because 1. it does not say so in the ROCclr's readme and ROCm-OpenCL-Runtime build readme specified ROCclr build is a prereq.

---

### 评论 #6 — ROCmSupport (2021-02-12T11:08:13Z)

Hi @gggh000 
I got your problem and am able to reproduce your problem now.

Initial steps are:
git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git

Both(ROCclr and OpenCL Runtime) are different repositories and so both should be cloned in the same directory path one after the other. For example, clone both in user space, means: cd ~ and then clone both spaces one by one.

But in your case, you cloned OpenCL runtime inside ROCclr and so its not able to find the headers. Request you to not to do the same.

_The conclusion is_
The steps in the documentation are clear and they are still perfect too. We do not see any issues when we follow the steps exactly as mentioned in the document.
So request you to exactly follow(or copy-paste the steps mentioned) in [https://github.com/ROCm-Developer-Tools/ROCclr](url) for good experience.
Thank you.

Please let me know if you have any more issues.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-02-12T11:22:33Z)

Request you to clone both ROCclr and ROCm-OpenCL-Runtime in the same directory path. Then your issue will go away.


---

### 评论 #8 — ROCmSupport (2021-02-16T08:03:17Z)

Hi @gggh000 
Request you to update on this asap. Close it if the above solution solves your issue.
Thank you.

---

### 评论 #9 — ROCmSupport (2021-04-08T11:38:34Z)

Cloning both ROCclr and ROCm-OpenCL-Runtime in the same directory path makes issue go away.

---
