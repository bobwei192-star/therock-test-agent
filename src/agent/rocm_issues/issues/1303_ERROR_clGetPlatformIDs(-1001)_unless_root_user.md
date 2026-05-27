# ERROR: clGetPlatformIDs(-1001) unless root user

> **Issue #1303**
> **状态**: closed
> **创建时间**: 2020-11-23T22:20:51Z
> **更新时间**: 2020-12-10T21:52:43Z
> **关闭时间**: 2020-12-10T21:52:43Z
> **作者**: uliw
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1303

## 描述

clinfo will return `ERROR: clGetPlatformIDs(-1001)` for a regular user but will work as expected for root. I am aware of most posts, around this issue, but none of the previously mentioned issues appear to apply here.

This is with kernel 5.9.8-2-default and a Navi 10 5700 XT GPU. The user account is part of the video and render groups. The permissions on /dev/kfd and /dev/dri are as follows
```
crw-rw-rw-+ 1 root video 241, 0 Nov 23 14:12 /dev/kfd
drwxr-xr-x   2 root root         80 Nov 23 14:12 by-path
crw-rw----+  1 root video  226,   0 Nov 23 14:13 card0
crw-rw-rw-   1 root render 226, 128 Nov 23 14:12 renderD128
```

the files in /etc/ld.so.conf.d appear to point to valid locations which are linked against  the rocm-3.9.0 directory.

I've attached the output of clinfo as root, as well as the strace clinfo as regular user below.

I'd be grateful for any hints

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5586080/clinfo.txt)
[clinfo_trace.txt](https://github.com/RadeonOpenCompute/ROCm/files/5586081/clinfo_trace.txt)





---

## 评论 (24 条)

### 评论 #1 — baryluk (2020-11-23T22:37:16Z)

Could you share output of `id` or `groups` run as normal user? Just to be sure.

Did you run `ldconfig` after editing files in `ld.so.conf.d`? It is required to run it to update caches.

Also which `clinfo` are you running, the one from ROCm (`/opt/rocm-../opencl/bin/clinfo`), or the other-one (`/usr/bin/rocminfo`).

Maybe you have something wrong with `PATH`? Show `echo $PATH` on root and normal user.


---

### 评论 #2 — ROCmSupport (2020-11-24T07:15:59Z)

Hi @uliw 
Thanks for reaching out.
Can you please provide answers to the immediate above comment.

---

### 评论 #3 — uliw (2020-11-24T13:02:12Z)


Yes, I did ran ldconfig, and to be on the safe side, I did a reboot. The path statement needs clean up, but otherwise, I see nothing wrong with it. I also linked all /opt/rcom/bin to /usr/local/bin/ since the install script did not create any links (I also had to link /opt/rocm-3.9.0 to /opt/rcom/ since all the names under ld.so.config point to /opt/rcom/

```
uliw@bonk:~> groups
users render docker vboxusers systemd-journal video

uliw@bonk:~> id
uid=500(uliw) gid=100(users) groups=100(users),460(render),462(docker),464(vboxusers),481(systemd-journal),482(video)

uliw@bonk:~> echo $PATH
/export/bonk/uliw/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/X11R6/bin:/usr/games:/opt/bin:/opt/kde3/bin:/usr/lib/mit/bin:/usr/lib/mit/sbin:/usr/local/bin::/export/bonk/uliw/.local/peace_bash_scripts:/usr/local/bin::/home/uliw/.local/bin/

and as root
bonk:~ # echo $PATH
/sbin:/usr/sbin:/usr/local/sbin:/root/bin:/usr/local/bin:/usr/bin:/bin

uliw@bonk:~> /opt/rocm/opencl/bin/clinfo 
ERROR: clGetPlatformIDs(-1001)
```

---

### 评论 #4 — baryluk (2020-11-24T18:32:57Z)

@uliw Thanks. That is really weird indeed. It should work, and looks like some deeper issue.

Let try running `sudo dpkg-reconfigure rocm-opencl3.9.0` or `sudo dpkg-reconfigure rocm-opencl` (depending which one you installed), and testing `clinfo` from the user again.

If this doesn't solve the issue, how about the output of these:

* `grep -rH . /etc/OpenCL/vendors/`
* as root and user: `echo $LD_LIBRARY_PATH`
* as root and user: `echo $OCL_ICD_VENDORS`
* as root and user: `echo $OCL_ICD_FILENAMES`
* as root and user: `echo $ROCM_PATH`

(please do it, even if you didn't set these variables).

and of `find /etc/OpenCL/vendors/ -name '*.icd' | while read OPENCL_VENDOR_PATH ; do clinfo -l > /dev/null ; echo "$? ${OPENCL_VENDOR_PATH}" ; done` , as root and user.


---

### 评论 #5 — valeriob01 (2020-11-24T18:54:40Z)

I have mentioned this issue before. It has always been like that for me. GPU programs only work as root, including gpuowl. No matter the system, I have tested on Debian and Ubuntu, the issue is the same.


---

### 评论 #6 — uliw (2020-11-24T20:08:16Z)

ahh, found it!

my bashrc file set `$OCL_ICD_VENDORS` and that was pointing to an old icd file...

clinfo works now as expected.Thanks!

---

### 评论 #7 — baryluk (2020-11-24T20:52:38Z)

@uliw You are welcome!


---

### 评论 #8 — baryluk (2020-11-24T20:52:59Z)

> I have mentioned this issue before. It has always been like that for me. GPU programs only work as root, including gpuowl. No matter the system, I have tested on Debian and Ubuntu, the issue is the same.

@valeriob01  Then your setup is broken.

It works for me from normal non-root user on Debian.


---

### 评论 #9 — uliw (2020-11-24T21:01:51Z)

much appreciated!

On Tue, Nov 24, 2020 at 3:52 PM Witold Baryluk <notifications@github.com>
wrote:

> @uliw <https://github.com/uliw> You are welcome!
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1303#issuecomment-733226913>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABWSVAXMMMUOBR4C6PZYHFLSRQMKJANCNFSM4UACMSAQ>
> .
>


-- 
Ulrich G. Wortmann
https://www.es.utoronto.ca/people/faculty/wortmann-ulrich/
Dept. of Earth Sciences     Fax  : 416 978 3938
University of Toronto       Phone: 416 978 7084
22 Ursula Franklin Street, Toronto, ON, Canada M5S 3B1


---

### 评论 #10 — valeriob01 (2020-11-25T05:01:58Z)

> > I have mentioned this issue before. It has always been like that for me. GPU programs only work as root, including gpuowl. No matter the system, I have tested on Debian and Ubuntu, the issue is the same.
> 
> @valeriob01 Then your setup is broken.
> 
> It works for me from normal non-root user on Debian.

If I was you I would think better before making such strong assumptions. If my setup is broken it means that the standard install instructions are broken.
I have installed ROCm on a dozen systems, following the web-site instructions, each time it works like that.


---

### 评论 #11 — ROCmSupport (2020-11-25T07:17:45Z)

Hi @uliw 
Thanks that your issue is resolved due to icd file.

Hi @valeriob01 
I am not sure why the things work for you with root user only.
The steps in the rocm docs work for non-root user perfectly. Can you please share the steps you followed in step-by-step procedure for better understanding.

---

### 评论 #12 — valeriob01 (2020-11-25T08:27:33Z)

> Hi @uliw
> Thanks that your issue is resolved due to icd file.
> 
> Hi @valeriob01
> I am not sure why the things work for you with root user only.
> The steps in the rocm docs work for non-root user perfectly. Can you please share the steps you followed in step-by-step procedure for better understanding.

The steps are here https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

just tested another time to be sure, the result is the same.


---

### 评论 #13 — ROCmSupport (2020-11-25T09:48:36Z)

Hi @valeriob01 
It will be good if you show step by step procedure you followed.
Because these instructions [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu](url) worked perfect always. Our test teams always install ROCm with non root user only. We never used root user for rocm.

As you said that you created symolic link to/opt/rocm on your own and it was not created by default, I can feel that somewhere installation not happened smoothly.
Make sure that your user is part of sudo, render and video groups always.

Can you please share below information also.

    /opt/rocm/bin/rocminfo
    /opt/rocm/bin/rocm-bandwidth-test
    /opt/rocm/opencl/bin/clinfo
    /opt/rocm/bin/rocm-smi


---

### 评论 #14 — valeriob01 (2020-11-25T10:14:16Z)

/opt/rocm/bin/rocminfo
ROCk module is loaded
xxx is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

---

### 评论 #15 — valeriob01 (2020-11-25T10:15:45Z)

 /opt/rocm/bin/rocm-smi

========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK     MCLK     Fan     Perf    PwrCap  VRAM%  GPU%  
1    82.0c  251.0W  1714Mhz  1100Mhz  57.65%  manual  250.0W   25%   100%  
2    69.0c  147.0W  1392Mhz  1100Mhz  74.9%   manual  250.0W   25%   100%  
3    78.0c  200.0W  1572Mhz  1100Mhz  74.9%   manual  250.0W   25%   100%  
4    77.0c  246.0W  1714Mhz  1100Mhz  74.9%   manual  250.0W   25%   100%  
================================================================================
==============================End of ROCm SMI Log ==============================


---

### 评论 #16 — valeriob01 (2020-11-25T10:18:37Z)

rocm-bandwidth-test and clinfo : no such file or directory.

Anyway I say again that I can live with it. No problems.
I do not store each step I followed so the only report I can send is the entire procedure.


---

### 评论 #17 — valeriob01 (2020-11-25T10:19:59Z)

BTW, clinfo is never installed by default, it is an additional install manually.


---

### 评论 #18 — ROCmSupport (2020-11-25T11:18:02Z)

Ok. Thanks for the preliminary information. Looks like some packages are missed to install.
SMI is detecting GPUs but rocminfo fails to detect GPUs.

Can you please show the output of **ls -l /opt/rocm** for better understanding.
And also show the contents of below commands too.
sudo dpkg -l | grep rocm
sudo dpkg -l | grep rock
sudo dpkg -l | grep hsa
sudo dpkg -l | grep hip
sudo dpkg -l | grep llvm

---

### 评论 #19 — valeriob01 (2020-11-25T14:48:58Z)

 ls -l /opt/rocm
lrwxrwxrwx 1 root root 15 Apr  2  2020 /opt/rocm -> /opt/rocm-3.3.0


 ls -l /opt/rocm-3.3.0/
total 44
drwxrwxr-x 2 root root 4096 Apr  4  2020 bin
drwxrwxr-x 8 root root 4096 Apr  2  2020 hcc
drwxrwxr-x 8 root root 4096 Apr  2  2020 hip
drwxrwxr-x 4 root root 4096 Apr  2  2020 hsa
drwxrwxr-x 3 root root 4096 Apr  2  2020 hsa-amd-aqlprofile
drwxrwxr-x 2 root root 4096 Apr  4  2020 include
drwxrwxr-x 3 root root 4096 Apr  4  2020 lib
drwxrwxr-x 5 1001 1001 4096 Apr  2  2020 opencl
drwxrwxr-x 6 root root 4096 Apr  4  2020 rocprofiler
drwxrwxr-x 5 root root 4096 Apr  4  2020 roctracer
drwxrwxr-x 6 root root 4096 Apr  2  2020 share


---

### 评论 #20 — baryluk (2020-11-25T18:55:29Z)

> > > I have mentioned this issue before. It has always been like that for me. GPU programs only work as root, including gpuowl. No matter the system, I have tested on Debian and Ubuntu, the issue is the same.
> > 
> > 
> > @valeriob01 Then your setup is broken.
> > It works for me from normal non-root user on Debian.
> 
> If I was you I would think better before making such strong assumptions. If my setup is broken it means that the standard install instructions are broken.
> I have installed ROCm on a dozen systems, following the web-site instructions, each time it works like that.

Yes, instructions are most likely incorrect or not fully correct. That is likely, and would be nice to fix them.

---

### 评论 #21 — baryluk (2020-11-25T19:09:33Z)

@valeriob01 

This bug is about `clGetPlatformIDs`. If your issues are not relevant to this (you claim you don't have installed clinfo, so it seems completly different issue), please open separate bug, with all important information: CPU, GPU, distro, distro version, kernel version, do you use upstream amdgpu driver or one from rocm-dkms, and which ROCm version you installed, as well if you have any other version of ROCm installed before on this system.

---

### 评论 #22 — ROCmSupport (2020-11-26T05:57:33Z)

> 
> 
> ls -l /opt/rocm
> lrwxrwxrwx 1 root root 15 Apr 2 2020 /opt/rocm -> /opt/rocm-3.3.0
> 
> ls -l /opt/rocm-3.3.0/
> total 44
> drwxrwxr-x 2 root root 4096 Apr 4 2020 bin
> drwxrwxr-x 8 root root 4096 Apr 2 2020 hcc
> drwxrwxr-x 8 root root 4096 Apr 2 2020 hip
> drwxrwxr-x 4 root root 4096 Apr 2 2020 hsa
> drwxrwxr-x 3 root root 4096 Apr 2 2020 hsa-amd-aqlprofile
> drwxrwxr-x 2 root root 4096 Apr 4 2020 include
> drwxrwxr-x 3 root root 4096 Apr 4 2020 lib
> drwxrwxr-x 5 1001 1001 4096 Apr 2 2020 opencl
> drwxrwxr-x 6 root root 4096 Apr 4 2020 rocprofiler
> drwxrwxr-x 5 root root 4096 Apr 4 2020 roctracer
> drwxrwxr-x 6 root root 4096 Apr 2 2020 share

rocm-smi is missed in this. You said you have created sym link to /opt/rocm manually. You are running clinfo not from /opt/rocm as its not available.
Based on these 3 points I can say that your installation did not go well.
Installation failures might happen in diff ways. Mainly it might be like your previous ROCm uninstallation might not go well.

So I recommend to uninstall ROCm completely using sudo apt autoremove rocm-dkms first and then make sure that all packages are removed. Recommend to check sudo dpkg -l | grep hsa . Replace hsa with hip, llvm, rocm, rock and make sure that all packages are removed. Recommend to purge/remove all packages as, for ex: **sudo apt purge hsa-rocr-dev** and do the same for all other additional packages also which are left(which can be seen by 'sudo dpkg -l | grep <component>')

Once you make sure that its clean, now try to install ROCm again.
I hope this helps.

---

### 评论 #23 — valeriob01 (2020-11-26T19:07:03Z)

> > ls -l /opt/rocm
> > lrwxrwxrwx 1 root root 15 Apr 2 2020 /opt/rocm -> /opt/rocm-3.3.0
> > ls -l /opt/rocm-3.3.0/
> > total 44
> > drwxrwxr-x 2 root root 4096 Apr 4 2020 bin
> > drwxrwxr-x 8 root root 4096 Apr 2 2020 hcc
> > drwxrwxr-x 8 root root 4096 Apr 2 2020 hip
> > drwxrwxr-x 4 root root 4096 Apr 2 2020 hsa
> > drwxrwxr-x 3 root root 4096 Apr 2 2020 hsa-amd-aqlprofile
> > drwxrwxr-x 2 root root 4096 Apr 4 2020 include
> > drwxrwxr-x 3 root root 4096 Apr 4 2020 lib
> > drwxrwxr-x 5 1001 1001 4096 Apr 2 2020 opencl
> > drwxrwxr-x 6 root root 4096 Apr 4 2020 rocprofiler
> > drwxrwxr-x 5 root root 4096 Apr 4 2020 roctracer
> > drwxrwxr-x 6 root root 4096 Apr 2 2020 share
> 
> rocm-smi is missed in this. You said you have created sym link to /opt/rocm manually. You are running clinfo not from /opt/rocm as its not available.
> Based on these 3 points I can say that your installation did not go well.
> Installation failures might happen in diff ways. Mainly it might be like your previous ROCm uninstallation might not go well.
> 
> So I recommend to uninstall ROCm completely using sudo apt autoremove rocm-dkms first and then make sure that all packages are removed. Recommend to check sudo dpkg -l | grep hsa . Replace hsa with hip, llvm, rocm, rock and make sure that all packages are removed. Recommend to purge/remove all packages as, for ex: **sudo apt purge hsa-rocr-dev** and do the same for all other additional packages also which are left(which can be seen by 'sudo dpkg -l | grep ')
> 
> Once you make sure that its clean, now try to install ROCm again.
> I hope this helps.

I don't touch my production machines as the program is running smoothly and fast with ROCm 3.3. Successive ROCm versions show a slowdown. Probably in a new installation, when ROCm has taken care of performance issues, I will install the new version, probably 4.0 or 5.0 .


---

### 评论 #24 — baryluk (2020-12-10T21:42:57Z)

@uliw Please close the bug.

---
