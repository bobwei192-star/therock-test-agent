# libamdocl64.so: cannot open shared object file

> **Issue #1331**
> **状态**: closed
> **创建时间**: 2020-12-11T19:45:59Z
> **更新时间**: 2021-09-24T20:37:12Z
> **关闭时间**: 2020-12-14T07:35:53Z
> **作者**: Dan-RAI
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1331

## 描述

apt update send rocm 3.9 to 3.10. 

manually removed via apt remove rocm* and hsa* .

reinstalled rocm via apt. (3.10).

calling clinfo yields

clinfo
dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory
Number of platforms:				 1






---

## 评论 (7 条)

### 评论 #1 — preda (2020-12-12T09:56:18Z)

It is in
/opt/rocm-3.10.0/opencl/lib/

(i.e. drop "x86_64")

---

### 评论 #2 — Dan-RAI (2020-12-12T19:02:10Z)

That is on a clean install and should not happen. 

Also, no idea why they have rocm-3.1.0 in the path. 

---

### 评论 #3 — ROCmSupport (2020-12-14T05:53:11Z)

Hi @Dan-RAI 
Thanks for reaching out.
Looks like ROCm 3.1 is there somewhere in the machine and so its showing dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so

Hence recommend to do a clean uninstall of complete ROCm (and delete any extra packages by checking like sudo dpkg -l | grep rocm, replace rocm with hsa, hip, llvm, rock, comgr etc and remove one by one using sudo apt purge <pkg>.)
At present ROCm upgrade does not work and so recommend to do a clean install always.
Thank you.

---

### 评论 #4 — Dan-RAI (2020-12-14T07:49:44Z)

Removed everything as listed above and reinstalled. Still getting same
error:

clinfo
dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open
shared object file: No such file or directory

Note: I never had rocm-3.1.0 installed on that machine ...



On Mon, Dec 14, 2020 at 8:36 AM ROCmSupport <notifications@github.com>
wrote:

> Closed #1331 <https://github.com/RadeonOpenCompute/ROCm/issues/1331>.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1331#event-4107633756>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AE575QWMJCIRTHT3EO5KVTDSUW56RANCNFSM4UXEUDXQ>
> .
>


---

### 评论 #5 — ROCmSupport (2020-12-14T08:06:20Z)

> 
> Removed everything as listed above and reinstalled. Still getting same error: clinfo dlerror: /opt/rocm-3.1.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory Note: I never had rocm-3.1.0 installed on that machine ...
> […](#)
> On Mon, Dec 14, 2020 at 8:36 AM ROCmSupport ***@***.***> wrote: Closed #1331 <#1331>. — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <[#1331 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1331#event-4107633756)>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AE575QWMJCIRTHT3EO5KVTDSUW56RANCNFSM4UXEUDXQ> .

Looks like some residue is there somewhere and hence its still pointing to 3.1.
Please do the below way.

Uninstallation:
1. sudo apt autoremove rocm-dkms
2. Check whether all pkgs are removed or not as shown below
   sudo dpkg -l | grep rocm
   sudo dpkg -l | grep rock
   sudo dpkg -l | grep hsa
   sudo dpkg -l | grep hip
   sudo dpkg -l | grep llvm
   sudo dpkg -l | grep comgr
   sudo dpkg -l | grep hcc
3. After step2, no package should be left ideally. If any packages are visible, then remove one by one as shown below.
   sudo apt purge <pkg>
  --> Repeat step3 for all leftover packages.
4. Once all removed, can say that all ROCm packages are removed and its clean now
5. Now check OpenCL icd file, whether its pointing to latest ROCm or old ROCm, correct it as needed.
6. Reboot machine

Install:
Once machine is clean from above uninstallion steps, now map the latest ROCm(3.10) and install it as shown below.
sudo apt install rocm-dkms --> should install ROCm well.

Thank you.


---

### 评论 #6 — Dan-RAI (2020-12-14T10:06:10Z)

Removing and re-installing did not solve this. 

However, the solution is to manually change:

/etc/OpenCL/vendors/amdocl64.icd

---

### 评论 #7 — FCLC (2021-09-24T20:37:12Z)

a safe way to test the above is to rename the files that seem to be causing errors. 

in my case the relevant command was to execute 
`mv amdocl64-orca.icd amdocl64-orca.icd.bk`

.bk is not a real extension, it simply will stop clinfo from throwing an error. 

otherwise, change the contents of the .icd to be the correct name of the openCL library 

i.e.  [correct name].so


---
