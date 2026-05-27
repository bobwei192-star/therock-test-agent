# Create a github issue template with instruction how to provide system information

> **Issue #1305**
> **状态**: closed
> **创建时间**: 2020-11-25T20:22:01Z
> **更新时间**: 2020-12-16T17:06:24Z
> **关闭时间**: 2020-12-16T05:13:51Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1305

## 描述

For Debian / Ubuntu based systems here is my recommended template:

* Distribution and version (`lsb_release -a`)
* GPU used
  * Attach output of `sudo lspci -vvv`
* CPU used: `lscpu`
* Kernel and system version: `uname -a`
* Installed kernels: `dpkg -l | egrep "linux-image|firmware-amd-graphics|dkms"`
* Used repositories: `grep -rH radeon /etc/apt/sources.list.d/`
* Installed relevant packages: `dpkg -l | egrep "roc[mkrt]|hsa|\bhip|opencl|clinfo|llvm" | awk '{print $1, $2, $3;}'`
* If `inxi` is installed, most of the above can be replaced by output of `inxi -SMCGrsxxz`
* Kernel modules: `sudo dkms status`
* Information if you previously had any other ROCm version installed on this system
* ROCm related information:
```sh
ls -l /opt/rocm*
/opt/rocm/bin/rocminfo
/opt/rocm/bin/rocm-smi
/opt/rocm/opencl/bin/clinfo
/opt/rocm/bin/rocm-bandwidth-test
/opt/rocm/bin/rocm-bandwidth-test -t
/opt/rocm/bin/hipconfig
pip3 list | egrep 'tensor|rocm'
```
* `sudo dmesg > dmesg.txt`
  * (Upload the `dmesg.txt` file as attachment to this issue. It is good idea to grab it soon after reboot or after experiencing an issue that you are reporting. If the dmesg doesn't contain all the information check `/var/log/kern.log*` files.)
* `/usr/bin/clinfo` (if installed)
* `grep -rH . /etc/ld.so.conf.d/`
* `/sbin/ldconfig -p | grep -i rocm`
* `ls -l /dev/kfd /dev/dri/card* /dev/dri/render*`
* As normal user: `groups`
* `grep -rH . /etc/OpenCL/vendors/`
* Environment variables used (as normal user and as root - do not use `sudo` here!):
  * `echo -e "PATH=$PATH\nROCM_PATH=$ROCM_PATH\nLD_LIBRARY_PATH=$LD_LIBRARY_PATH\nLD_PRELOAD=$LD_PRELOAD\nOCL_ICD_VENDORS=$OCL_ICD_VENDORS\nOCL_ICD_FILENAMES=$OCL_ICD_FILENAMES"
`
* `find /etc/OpenCL/vendors/ -name '*.icd' | while read OPENCL_VENDOR_PATH ; do clinfo -l > /dev/null ; echo "$? ${OPENCL_VENDOR_PATH}" ; done`

If any of the above fails, please include the full output (including invocation) of error message received.

**Note**: If using versioned pacakges, replace `/opt/rocm` with a proper path, like `/opt/rocm-3.9.0`. **Include the used path in the issue text.** Other option is to ensure there is a symbolic link, i.e. `sudo ln -s /opt/rocm-* /opt/rocm`.



---

## 评论 (7 条)

### 评论 #1 — kentrussell (2020-12-03T18:19:48Z)

Speaking solely from the kernel perspective, I find that a full dmesg is more useful than grepping for amd, as there are some other non-AMD things that we find in there that contribute to issues on occasion. But GPU/OS/kernel/dkms status/rocminfo/rocm-smi is definitely what the kernel starts with when investigating.

---

### 评论 #2 — baryluk (2020-12-10T21:44:32Z)

> Speaking solely from the kernel perspective, I find that a full dmesg is more useful than grepping for amd, as there are some other non-AMD things that we find in there that contribute to issues on occasion. But GPU/OS/kernel/dkms status/rocminfo/rocm-smi is definitely what the kernel starts with when investigating.

@kentrussell Yes, that makes sense. But maybe attach as a separate file.

My dmesg is spamming constantly `Maybe the USB cable is bad?`:

```
$ sudo dmesg | grep 'usb usb8-port1: Cannot enable. Maybe the USB cable is bad' | wc -l
13222
$
```
So, including full dmesg isn't always best solution. :)


---

### 评论 #3 — ROCmSupport (2020-12-11T06:15:15Z)

Hi @baryluk 
Its always recommended to have complete dmesg which has all info.
We can grab the relavent info whenever we need and that too dmesg log occupies less space.
Pulling specific information by grepping from dmesg is not always helpful and we can not give guarantee that captured information from dmesg statisfies our needs always. So its always recommended to map complete dmesg.

---

### 评论 #4 — kentrussell (2020-12-11T11:20:43Z)

@baryluk While comments like that may nothelp, it's still a lot easier for a dev to ignore those lines, than it is to hope that the reporter filtered out the right stuff. I don't think I've ever wished that someone would have filtered their dmesg when I am dealing with investigating issues, because 99% of the time when someone filters out the dmesg, they cut out something that they think is unimportant but still has relevance, and I have to get them to get a full dmesg for me.

And if the person investigating really dislikes it, they can just sed it themselves :) But I completely agree, have it as a separate file. It makes it easier to read, and avoids cluttering up the Bug Report which contains the "meat" of the issue

---

### 评论 #5 — baryluk (2020-12-11T11:51:38Z)

OK. I made adjustments, so full dmesg is shared by default. I agree, it is easier to include it full, and dev to analyse it quick, that possibly miss stuff.

I also made some other commands easier to execute (i.e. environment variable report is single line command, instead 5 separate ones), and made `ldconfig` use absolute path, so it can be run from non-root easily too.

---

### 评论 #6 — ROCmSupport (2020-12-16T05:13:51Z)

Its a ticket template, nothing to work functionally.

---

### 评论 #7 — baryluk (2020-12-16T17:06:24Z)

@ROCmSupport 

> Its a ticket template, nothing to work functionally.

The bug reporting workflow is part of functionality.

The ROCm repo issue tracker still doesn't have any ticket template. And that is my point.



---
