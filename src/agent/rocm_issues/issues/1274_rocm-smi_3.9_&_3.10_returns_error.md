# rocm-smi 3.9 & 3.10 returns error

> **Issue #1274**
> **状态**: closed
> **创建时间**: 2020-11-01T14:19:48Z
> **更新时间**: 2024-06-01T15:28:07Z
> **关闭时间**: 2020-12-11T05:27:27Z
> **作者**: eBellmer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1274

## 描述

I updated my Ubuntu 20.04 container to ROCm 3.9 from 3.8, and rocm-smi now produces the following error:
`ERROR:root:ROCm SMI returned 8 (the expected value is 0)`

Running rocm_smi.py produces the same error, but rocm_smi_deprecated.py seems to work as expected with the following output:
```
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK     MCLK    Fan   Perf  PwrCap  VRAM%  GPU%  
1    31.0c  7.0W    1269Mhz  945Mhz  0.0%  auto  220.0W    0%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```

I have tried completely uninstalling ROCm and reinstalling but the error persists.

**rocm-smi Version:** 3.9.0
**Kernel version:** 5.4.65-1-pve (container host is running ProxMox)
**GPU:** Radeon Instinct MI25

---

## 评论 (23 条)

### 评论 #1 — rkothako (2020-11-02T10:09:12Z)

Hi @eBellmer 
Thanks for logging issue.
Can you please clearly share the steps you followed.
Looks like you are using old python version. Can you please try with python3 /opt/rocm/bin/rocm_smi.py.

I tried on my local MI25 + ROCm 3.9, rocm-smi is showing details properly with the all 3 different commands, like below.

**Commands used:**
/opt/rocm/bin/rocm-smi
python3 /opt/rocm/bin/rocm_smi_deprecated.py
python3 /opt/rocm/bin/rocm_smi.py

**Output got(in all 3 ways):**
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%
0    32.0c  3.0W    300Mhz  167Mhz  0.0%  auto  110.0W    0%   0%


---

### 评论 #2 — eBellmer (2020-11-02T13:13:19Z)

Hi @rkothako 
Thanks for your response.

The Ubuntu 20.04 container is running Python 3.6.12, and the ProxMox host is running 3.7.3.

Running `/opt/rocm/bin/rocm-smi` and `python3 /opt/rocm/bin/rocm_smi.py` both result in the `ROCm SMI returned 8 (the expected value is 0)` error.
Running `python3 /opt/rocm/bin/rocm_smi_deprecated.py` produces the correct SMI output.

If I run the commands on the ProxMox host I get the following error when running rocm-smi & rocm_smi.py:
`Unable to load the rocm_smi library. 
Set LD_LIBRARY_PATH to the folder containing librocm_smi64.`

I don't have the full ROCm stack installed on the ProxMox host, just the `rocm-smi` & `rocm-smi-lib64` packages.
Running `python3 rocm_smi_deprecated.py` produces the correct output on the ProxMox host. 

---

### 评论 #3 — rkothako (2020-11-03T11:17:13Z)

Thanks @eBellmer 
We found the rootcause of the issue, I am working with our team for the fix.

---

### 评论 #4 — kentrussell (2020-11-03T11:23:05Z)

Hi @eBellmer 
This is a known issue for 3.9. When we transitioned the rocm_smi from the old method (parsing sysfs files directly in Python) to the new method (using the rocm_smi_lib backend) in 3.9, we relied on ldconfig being configured properly to handle this. Unfortunately, starting with ROCm 3.6 the ROCm infrastructure team made a move to not use ldconfig, so they could support multiple ROCm installations on the same system. This disconnect is causing the issue that you see here.

This will be fixed in 3.10, but for now the easiest solution is to use the deprecated rocm_smi CLI until the next release. Trying to manually edit the lib-backed SMI is a lot more work and runs the risk of errors, and 3.10 will be coming out reasonably soon so it's just a temporary (albeit annoying) situation. Thanks for your patience during this transition

---

### 评论 #5 — baryluk (2020-11-18T19:35:08Z)

Will new method work for non-root users too? I hope so.

`/opt/rocm-3.9.0/bin/rocm_smi_deprecated.py` works for me.

A new `/opt/rocm-3.9.0/bin/rocm-smi`, has issues loading rocm_smi library.

```
ii  rocm-smi-lib643.9.0                                         2.7.0.5-rocm-rel-3.9-17-8f9f943            amd64        AMD System Management libraries
ii  rocm-smi3.9.0                                               1.0.0-206-rocm-rel-3.9-17-ge39c0e2         amd64        System Management Interface for ROCm
```

```
$ sudo ldconfig  -p | grep rocm
	libhsa-runtime64.so.1 (libc6,x86-64) => /opt/rocm-3.9.0/hsa/lib/libhsa-runtime64.so.1
	libhsa-runtime64.so (libc6,x86-64) => /opt/rocm-3.9.0/hsa/lib/libhsa-runtime64.so
	libamdocl64.so (libc6,x86-64) => /opt/rocm-3.9.0/opencl/lib/libamdocl64.so
	libOpenCL.so.1 (libc6,x86-64) => /opt/rocm-3.9.0/opencl/lib/libOpenCL.so.1
	libOpenCL.so (libc6,x86-64) => /opt/rocm-3.9.0/opencl/lib/libOpenCL.so
$
```

```
$ ls -lh `dpkg -L rocm-smi-lib643.9.0  | grep librocm`
lrwxrwxrwx 1 1001 root   32 Oct 21 19:56 /opt/rocm-3.9.0/lib/librocm_smi64.so -> ../rocm_smi/lib/librocm_smi64.so
lrwxrwxrwx 1 1001 root   34 Oct 21 19:56 /opt/rocm-3.9.0/lib/librocm_smi64.so.2 -> ../rocm_smi/lib/librocm_smi64.so.2
lrwxrwxrwx 1 1001 root   18 Oct 21 19:56 /opt/rocm-3.9.0/rocm_smi/lib/librocm_smi64.so -> librocm_smi64.so.2
lrwxrwxrwx 1 1001 root   26 Oct 21 19:56 /opt/rocm-3.9.0/rocm_smi/lib/librocm_smi64.so.2 -> librocm_smi64.so.2.7.30900
-rw-r--r-- 1 1001 root 532K Oct 21 19:56 /opt/rocm-3.9.0/rocm_smi/lib/librocm_smi64.so.2.7.30900
$
```

Looks good.

But, this doesn't look correct:

If I modified the `rsmiBindings.py` to not catch the exception, it shows this:

```
$ python3 /opt/rocm-3.9.0/bin/rsmiBindings.py 
Traceback (most recent call last):
  File "/opt/rocm-3.9.0/bin/rsmiBindings.py", line 13, in <module>
    cdll.LoadLibrary(path_librocm)
  File "/usr/lib/python3.8/ctypes/__init__.py", line 451, in LoadLibrary
    return self._dlltype(name)
  File "/usr/lib/python3.8/ctypes/__init__.py", line 373, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: librocm_smi64.so: cannot open shared object file: No such file or directory
$
```

I am not sure, but it looks to me it is trying to open the file using relative path name from the local directory maybe?

Or maybe it should be added to `/etc/ld.so.conf.d/`

Once I create a `/etc/ld.so.conf.d/x86_64-rocm-smi.conf`, with this content:

```
/opt/rocm-3.9.0/lib
/opt/rocm-3.9.0/rocm_smi/lib
```

run `sudo ldconfig`, it appears to start working:

```
$ sudo ldconfig  -p | grep rocm | grep smi
	librocm_smi64.so.2 (libc6,x86-64) => /opt/rocm-3.9.0/lib/librocm_smi64.so.2
	librocm_smi64.so.2 (libc6,x86-64) => /opt/rocm-3.9.0/rocm_smi/lib/librocm_smi64.so.2
	librocm_smi64.so (libc6,x86-64) => /opt/rocm-3.9.0/lib/librocm_smi64.so
	librocm_smi64.so (libc6,x86-64) => /opt/rocm-3.9.0/rocm_smi/lib/librocm_smi64.so
$
```

and the `cdll` is able to dlopen the library, hower it fails now with:

```
$ /opt/rocm-3.9.0/bin/rocm_smi.py 
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
$
```


---

### 评论 #6 — kentrussell (2020-11-18T19:43:38Z)

It should be working in 3.10 as before, it's just a hiccup during our transition to the new LIB-backing for the SMI CLI. The SMI LIB assumed ldconfig would be performed, but that isn't guaranteed as we support multiple ROCm installs on the same system. If the issue isn't fixed in 3.10 (or if you're hitting that SMI error value 8), then I'd open an issue in the rocm_smi_lib project to ensure the most visibility. The general ROCm bin can cause issues to get missed sometimes, but the specific projects have their component owners watching them to ensure that things get addressed quickly.

---

### 评论 #7 — ghost (2020-12-04T11:27:08Z)

Hey guys, I'm brand new to rocm and I just followed the installation guide today for rocm & tensorflow.

This is everything I installed (I'm on ubuntu 18.04) :

```bash
apt list libnuma-dev rocm-dkms rocm-libs rccl hipcub miopen-hip

Listing... Done
hipcub/Ubuntu 16.04,now 2.10.5.207-rocm-rel-3.10-27-7bda2e4 amd64 [installed]
libnuma-dev/bionic-updates,now 2.0.11-2.1ubuntu0.1 amd64 [installed]
miopen-hip/Ubuntu 16.04,now 2.9.0.8250-rocm-rel-3.10-27-8a4af47d amd64 [installed]
rccl/Ubuntu 16.04,now 2.7.8.490-rocm-rel-3.10-27-937aec9 amd64 [installed]
rocm-dkms/Ubuntu 16.04,now 3.10.0.31000-27 amd64 [installed]
rocm-libs/Ubuntu 16.04,now 3.10.0.31000-27 amd64 [installed]
```

@kentrussell, I'm getting the exact same error as @eBellmer with rocm-smi

Also, when I try to use tensorflow, I get another error, which is I guess related : 

```py
Python 3.8.0 (default, Oct 28 2019, 16:14:01) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> x = tf.Variable(3, name="x")
2020-12-04 12:24:43.546214: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
Aborted (core dumped)
```

I guess I'll try to uninstall rocm and install an older version for now. Maybe there's a workaround though ?

---

### 评论 #8 — kentrussell (2020-12-04T11:33:08Z)

@crouinicrouina That 2nd issue should be resolved in 3.10, as there were some runtime changes needed to accommodate some kernel changes. As for the first one, you should be set using the deprecated SMI, we're planning to officially deprecate the old SMI completely soon, but you can still use the old SMI CLI in the interim without any significant problem or missing functionality

---

### 评论 #9 — ghost (2020-12-04T11:48:47Z)

@kentrussell Thank you for the super faster response ! I'll try to install 3.10 from the start once again and hopefully, the tensorflow error will go away ^^

---

### 评论 #10 — baryluk (2020-12-04T13:23:52Z)

`rocm-smi` works nicely for me in ROCm 3.10. No issues. Clean install.

---

### 评论 #11 — ghost (2020-12-04T13:42:07Z)

After uninstalling/re-installing ROCm 3.10, I still had the same issues.

However, after that, I came across [this issue](https://github.com/RadeonOpenCompute/ROCm/issues/1265) stating that ROCm 3.7+ was broken on gfx803 (and I have an RX580). I guess my issue was actually tied to this other issue rather than this one.

I ended up following the advice in the issue and I installed ROCm 3.5.1 instead.
`rocm-smi` and Tensorflow both work perfectly for me now.

Thank you guys for the work on this library :+1: !

---

### 评论 #12 — eBellmer (2020-12-04T14:23:18Z)

I performed a clean install for 3.10 yesterday on both my Debian host and Ubuntu container, and the `ERROR:root:ROCm SMI returned 8 (the expected value is 0)` error is still occurring. 
I have exposed /dev/dri/card1, /dev/dri/renderD128, and /dev/kfd to the container but I'm wondering if something else is required from the host to allow the new ROCm-SMI to work outside of these modules?

clinfo, rocm_smi_deprecated, rocminfo, etc all work as expected. 

---

### 评论 #13 — kentrussell (2020-12-04T14:37:05Z)

As a workaround, you'd can edit "rsmiBindings.py" , as the path there is looking for a specific route to get to the librocm_smi64.so . Originally we were fine using ldconfig, but ROCm disabled ldconfig due to wanting to support multiple ROCms on the same system. We're still finding bugs with our new approach as we try to stabilize it all.

Locally I've made the following change as a possible stopgap for this in rsmiBindings.py:

`# Use ROCm installation path if running from standard installation`
`path_librocm = os.path.dirname(os.path.realpath(__file__)) + '/../lib/librocm_smi64.so'`
`+if not os.path.isfile(path_librocm):`
`+    for root, dirs, files in os.walk('/opt'):`
`+        if 'librocm_smi64.so' in files:`
`+            path_librocm = os.path.join(root, 'librocm_smi64.so')`
`# ----------> TODO: Support static libs as well as SO`

It may not work for all cases, but it seemed to help when I had the rocm_smi.py in a separate folder and is a little more forgiving when it comes to these paths. 

---

### 评论 #14 — ROCmSupport (2020-12-07T09:00:01Z)

Hi @eBellmer and @crouinicrouina 
We are able to reproduce this issue, still, in a few machines only, but not in all machines.
I am working with SMI team for the additional fixes to be ported into 4.0.

---

### 评论 #15 — ROCmSupport (2020-12-11T05:27:27Z)

Hi All,
We tried with the latest ROCm 3.10 repo(which is updated with fixes for rock-dkms rock-dkms-firmware (I mean new packages)) and not able to reproduce this issue now.
Recommend to do a fresh/clean uninstall of existing ROCm and install new 3.10 ROCm freshly and verify.
Issue should be gone.
Thank you.

---

### 评论 #16 — manmohanbrahma (2021-02-11T11:26:44Z)

Seems like the same issue evolved again with rocm 4.0.0

---

### 评论 #17 — eBellmer (2021-02-11T11:50:18Z)

The issue never went away for me. My setup doesn't use the rock-dkms package, so I couldn't reinstall them. 

---

### 评论 #18 — ROCmSupport (2021-02-11T11:59:27Z)

Hi @manmohanbrahma 
Request you to share the exact configuration details with us for better understanding like CPU, GPU, OS, ROCm version etc.,.
And also as this issue is closed, request you to open a new issue for better tracking and analysis.
Thank you

---

### 评论 #19 — damora (2021-03-06T13:32:51Z)

Running into the same issue reported above with 4.0.0 on RHEL8.3.  is the fix recommended by @kentrussell the best remedy at this point?
i.e. edit local rsmiBindings.py

---

### 评论 #20 — kentrussell (2021-03-08T12:44:40Z)

4.1 will have this fix included, so the edit above is the quickest way to get around things until that new drop occurs.

---

### 评论 #21 — evilbulgarian (2021-03-24T18:32:33Z)

same issue with 4.1 @kentrussell :
`
vladi@vladi-TB250-BTC:~$ rocm-smi
Failed to get "domain" properity from properties files for kfd node 1.
rsmi_init() failed
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
vladi@vladi-TB250-BTC:~$ sudo ldconfig  -p | grep rocm | grep smi
[sudo] password for vladi:
        librocm_smi64.so.3 (libc6,x86-64) => /opt/rocm/lib/librocm_smi64.so.3
        librocm_smi64.so.3 (libc6,x86-64) => /opt/rocm/rocm_smi/lib/librocm_smi64.so.3
        librocm_smi64.so (libc6,x86-64) => /opt/rocm/lib/librocm_smi64.so
        librocm_smi64.so (libc6,x86-64) => /opt/rocm/rocm_smi/lib/librocm_smi64.so
vladi@vladi-TB250-BTC:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal
`

---

### 评论 #22 — ROCmSupport (2021-03-25T02:43:33Z)

As this thread is closed, recommend to open a new issue and discuss there for fast response.
Thank you.

---

### 评论 #23 — spirosbond (2024-06-01T15:28:05Z)

If you are here because of the below error when running rocm-smi:
```
Unable to load the rocm_smi library.
Set LD_LIBRARY_PATH to the folder containing librocm_smi64.so.1
Please refer to https://github.com/RadeonOpenCompute/rocm_smi_lib for the installation guide.

```

I managed to fix it by:
1. Installing python 3.11. I had the issue with python 3.12
2. Updating the libgcc to its latest version. 

For point 2, if you are running conda/miniconda you might need to use the conda-forge channel since it has a later version:
`conda install -c conda-forge libgcc`

After that, rocm-smi works as expected.

---
