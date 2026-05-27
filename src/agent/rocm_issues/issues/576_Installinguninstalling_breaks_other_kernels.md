# Installing/uninstalling breaks other kernels

> **Issue #576**
> **状态**: closed
> **创建时间**: 2018-10-06T20:23:25Z
> **更新时间**: 2021-01-07T09:56:49Z
> **关闭时间**: 2021-01-07T09:56:49Z
> **作者**: suvayu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/576

## 描述

I have encountered a strange issue, I am on Fedora 28 and I wanted to try out ROCm.  So I installed the 4.19.0-rc6 mainline kernel, and installed rocm from the Centos repos.  But I encountered the *Updating firmware may not trigger a rebuilding of ramfs* issue mentioned in the [install FAQ](https://rocm.github.io/install_issues.html). I eventually uninstalled the kernel and rocm, however now my older kernels also have the same problem!

I have tried reinstalling the old kernels, regenerating the initramfs as recommended by the FAQ, reinstalled the firmware and tried regenerating the initramfs again, nothing seems to help.  Any thoughts what I can do?  

---

## 评论 (22 条)

### 评论 #1 — jlgreathouse (2018-10-08T18:39:44Z)

First thought: don't directly install `rocm-dkms` on unsupported distributions. :)

That's not a very helpful response, I'll admit. However, for reference, if you're using the upstream kernel then you may not want to install the DKMS kernel drivers on your distribution. Our `rock-dkms` kernel drivers are only _officially_ supported on Ubuntu 16.04, Ubuntu 18.04, and RHEL/CentoS 7.4 and 7.5.

A few questions:
* What GPU are you using?
* What kernel version? (e.g. are you running Fedora 28's bleeding edge, or are you on an older release)
* What commands did you run to do the installation? What commands did you run after that? (It's going to be hard to give you an exact set of steps to fix your system since I don't have any idea what state your system is in at the moment).
* What files are in `/lib/firmware/amdgpu`
* What output do you see from `dkms status`
* What output of `dmesg` and what errors, in particular, are you seeing?

---

### 评论 #2 — suvayu (2018-10-08T23:14:06Z)

Hi @jlgreathouse,

Sorry, my report was not detailed.  I am not very familiar with all the internals, so wasn't sure how to get more relevant info.  Some details: the latest official Fedora kernel I have is 4.18.11.  However I tried this with 4.19.0-rc6 (and rc7 since I opened this issue).  The 4.19 series is a vanilla kernel compiled for Fedora, and [maintained by Thorsten Leemhuis](https://fedoraproject.org/wiki/Kernel_Vanilla_Repositories).  

To answer your questions:

- I'm on an APU: Ryzen 2400G
- I have tried this with 4.19.0-rc6/7 (and it breaks my 4.18.x kernels even after uninstallation)
- I went through my shell and `dnf` history, and this is what what I see:
  1. install kernel 4.19.0-rc6
  2. install the kernel devel package
  3. install `rocm-dkms`
  4. reboot

  But now I think maybe I should have rebooted after 1 (or maybe 2), because while looking through my dnf install history, I see during installation the `rocm-dkms` build failed for the 4.18 kernel, which was the kernel that I was already running.  But I'm not sure if that matters, as `dkms` should have rebuilt for 4.19 when I rebooted in step (iv), am I right?
- `/lib/firmware/amdgpu` has the binary blobs, mine includes Raven Ridge files.

      $ ls -1 /lib/firmware/amdgpu/raven_*
      /lib/firmware/amdgpu/raven_asd.bin
      /lib/firmware/amdgpu/raven_ce.bin
      /lib/firmware/amdgpu/raven_gpu_info.bin
      /lib/firmware/amdgpu/raven_me.bin
      /lib/firmware/amdgpu/raven_mec2.bin
      /lib/firmware/amdgpu/raven_mec.bin
      /lib/firmware/amdgpu/raven_pfp.bin
      /lib/firmware/amdgpu/raven_rlc.bin
      /lib/firmware/amdgpu/raven_sdma.bin
      /lib/firmware/amdgpu/raven_vcn.bin
- I can't accurately answer your last two questions, as I have uninstalled everything right now.  But that's actually my issue, now normal amdgpu functionality is broken (which was working wonderfully before I decided to try this experiment).  I will try to install everything again, and try to report back with answers to these questions.

---

### 评论 #3 — rhlug (2018-10-09T00:00:07Z)

When I run this old 4.17 kernel, I get /dev/kfd and a working opencl environment under rocm 1.9.x

```
# uname -a
Linux localhost  4.17.0-rc2-180424-fkxamd #1 SMP PREEMPT Wed Apr 25 17:53:26 CDT 2018 x86_64 x86_64 x86_64 GNU/Linux

# ls -la /dev/kfd
crw-rw---- 1 root video 239, 0 Oct  8 22:31 /dev/kfd

# /opt/rocm/opencl/bin/x86_64/clinfo  | egrep -e "Board|units"
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 56
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 64
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 56
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 56
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 64
  Board name:					 Vega [Radeon RX Vega]
  Max compute units:				 56
```

As soon as I upgrade to amd-staging-drm-next or drm-next-4.20-wip,  I have no /dev/kfd, and nothing works.    Not sure whats missing.   I added /etc/udev/rules.d/70-kfd.rules like the instructions said.


---

### 评论 #4 — suvayu (2018-10-09T09:55:29Z)

Hi @jlgreathouse,

I reinstalled `rocm-dkms`.  The answers to your last two questions are:

- The `dkms` build [fails](https://github.com/RadeonOpenCompute/ROCm/files/2459816/make.txt)  during installation, although output to `dkms status` is:

      # dkms status 
      amdgpu, 1.9-224.el7: added
- In the journal I see `amdgpu` fails to load even though the drivers are present (as shown above)

      kfd kfd: Initialized module
      [drm] initializing kernel modesetting (RAVEN 0x1002:0x15DD 0x1458:0xD000 0xC6).
      [drm] register mmio base: 0xFE600000
      [drm] register mmio size: 524288
      [drm] add ip block number 0 <soc15_common>
      [drm] add ip block number 1 <gmc_v9_0>
      [drm] add ip block number 2 <vega10_ih>
      [drm] add ip block number 3 <psp>
      [drm] add ip block number 4 <powerplay>
      [drm] add ip block number 5 <dm>
      [drm] add ip block number 6 <gfx_v9_0>
      [drm] add ip block number 7 <sdma_v4_0>
      [drm] add ip block number 8 <vcn_v1_0>
      amdgpu 0000:06:00.0: Direct firmware load for amdgpu/raven_gpu_info.bin failed with error -2
      amdgpu 0000:06:00.0: Failed to load gpu_info firmware "amdgpu/raven_gpu_info.bin"
      amdgpu 0000:06:00.0: Fatal error during GPU init
      [drm] amdgpu: finishing device.
      amdgpu: probe of 0000:06:00.0 failed with error -2

  It's strange that this happens even when I remove `rocm-dkms` (it was fine before I tried ROCm).

I guess in my attempts to fix the situation, a combination of `rocm-dkms` and `dracut --regenerate-all --force` messed up my old kernels/kernel config, and now even reinstalling an existing kernel/installing a new kernel from the Fedora repos do not work.


---

### 评论 #5 — suvayu (2018-10-23T06:12:55Z)

This issue was caused by dracut misconfiguration.  The ROCm installation leaves behind dracut configuration files under `/etc/dracut.conf.d` which incorrectly point to `/lib/firmware/<kernel-version>` as the firmware directory.  Removing the files, resolved my issue.  You can find the details [here](https://lists.fedoraproject.org/archives/list/users@lists.fedoraproject.org/message/P2I5SBOCHQVODZP3AVIFVMHANOTDZBJX/).

I guess the uninstallation scripts in the rpm need to be fixed.

---

### 评论 #6 — jlgreathouse (2018-10-23T21:49:14Z)

Hi @suvayu 

Thank you for looking into this. I'd like to pass this to our driver team so we can make a fix, but I have a request to see if you can help me.

### Request
Could you perhaps give me the directions to reproduce this issue from the start? I'm not sure that I'm able recreate the issue, either on CentOS 7.5 (upgrading to 4.19) or on Fedora 28. Following the various install and uninstall scripts, it appears that we *should* be deleting those files when uninstall and ROCm drivers.

### How ROCm Drivers Are Installed/Uninstalled on RHEL/CentOS
The `rock-dkms` package installs the ROCm drivers as a DKMS module. This comes with source code, and scripts that DKMS will call while adding/building the module and when uninstalling the module. For instance, the ROCm firmware and the file in `/etc/dracut.conf.d/` are added by `/usrc/src/amdgpu-1.9-224.el7/pre-build.sh:44-50`. In other words, the firmware is moved and the dracut file is created right before the DKMS module is built with the `dkms build amdgpu-1.9-224.el7` command (numbers may change depending on ROCm version and OS, but you get the point). This DKMS build command is called by the install script in the rock-dkms RPM.

When you _remove_ the DKMS module, the script `/usr/src/amdgpu-1.9-224.el7/post-remove.sh` is called, and lines 3-7 delete the ROCm firmware directories in `/lib/firmware/<kernel-version>/` and then `rm -f /etc/dracut.conf.d/amdgpu-<kernel-version>.conf`.

When you uninstall the `rock-dkms` package, it should call `dkms remove amdgpu-1.9-224.el7`, which will then call that post-remove script. If you look at the scripts run from `rock-dkms-1.9-224.el7.noarch.rpm` by running `rpm -qp --scripts ./rock-dkms-1.9-224.el7.noarch.rpm` you'll see the following uninstall scriptlet:
```
preuninstall scriptlet (using /bin/sh):
dkms remove -m amdgpu -v 1.9-224.el7 --all --rpm_safe_upgrade
exit $?
```
So when you `yum remove rock-dkms` (or `dnf remove rock-dkms`) it will call that scriptlet, which runs  `dkms remove amdgpu`, which will then call the `post-remove.sh` script, which will remove the amdgpu files in `/etc/dracut.conf.d/` and in `/lib/firmware/`.

### Guess at a Reason
As such, I'm not sure how your system has entered the state you're in. My first guess is that perhaps you installed `rocm-dkms` (which installs `rock-dkms`). The kernel driver did not build correctly (because `rock-dkms` is currently broken on kernels newer than 4.15), but the build process still puts the dracut.conf.d and firmware files in place. If you then did `yum autoremove rocm-dkms`, it may have left the `rock-dkms` package (I'm still exploring this, but I've seen autoremove not remove `rock-dkms`). So this may have left files in your dracut.conf.d, though it still should have left the firmware files as well.

I'm not sure, however, how the scripts would have deleted the firmware from `/lib/firmware/` but not deleted the conf file in `/etc/dracut.conf.d/`.

So some further questions:
- Do you have any files in `/lib/firmware/<kernel-version>`?
- Is `rock-dkms` still installed on your system? (e.g. if you run `yum info rock-dkms` is it showed as installed?)
- If you can recreate this issue, if you do `yum autoremove rock-dkms`, does that fix the problem?

---

### 评论 #7 — suvayu (2018-10-24T00:32:44Z)

Hi @jlgreathouse, I would be happy to give you detailed steps.  But as Fedora isn't quite supported, I had to hackaround a bit. Now that I understand what went wrong, I will reproduce everything and document over the weekend.  I hope that is okay.

Btw, I would be happy to test any fixes that makes Fedora fully supported platform :).

---

### 评论 #8 — jlgreathouse (2018-10-24T00:41:59Z)

Hi @suvayu 

No worries, and I apologize that this is causing you so many problems. I'm not sure if AMD will ever "support" ROCm on Fedora (where support implies some large amount of testing on a large number of hardware configurations before each release, as hardware companies are fond of doing). However, I too would like to make sure that ROCm is "enabled" on platforms such as Fedora and other distros -- meaning that the code _should_ work even if we don't perform a huge amount of testing on it before a release hits the internet. The distinction may seem somewhat academic from the outside, but various managers in the company imply there's a difference. :)

For "enabled" or "working towards enabled" platforms, feedback like you're delivering here is invaluable.

Some things that you could test on your system now (if your system is still working and you haven't formatted/reinstalled since the problems initially came up): the first two bullets at the end of my last post (data in `/lib/firmware/<kernel-version>` and whether `rock-dkms` is still installed) are actually questions about your system as it is right now.

---

### 评论 #9 — suvayu (2018-10-24T02:07:35Z)

Hi @jlgreathouse,

I can live with "enabled" on Fedora :)

A quick response to your bullet points:
- as it stands, the firmware on my system is provided by the package `linux-firmware` from the official Fedora repos.  They are not in a kernel version specific directory.

      # lt /lib/firmware/amdgpu/raven_*
      -rw-r--r--. 1 root root 334K Oct 15 17:52 /lib/firmware/amdgpu/raven_vcn.bin
      -rw-r--r--. 1 root root  17K Oct 15 17:52 /lib/firmware/amdgpu/raven_sdma.bin
      -rw-r--r--. 1 root root  39K Oct 15 17:52 /lib/firmware/amdgpu/raven_rlc.bin
      -rw-r--r--. 1 root root  22K Oct 15 17:52 /lib/firmware/amdgpu/raven_pfp.bin
      -rw-r--r--. 1 root root 262K Oct 15 17:52 /lib/firmware/amdgpu/raven_mec.bin
      -rw-r--r--. 1 root root 262K Oct 15 17:52 /lib/firmware/amdgpu/raven_mec2.bin
      -rw-r--r--. 1 root root  18K Oct 15 17:52 /lib/firmware/amdgpu/raven_me.bin
      -rw-r--r--. 1 root root  316 Oct 15 17:52 /lib/firmware/amdgpu/raven_gpu_info.bin
      -rw-r--r--. 1 root root 9.2K Oct 15 17:52 /lib/firmware/amdgpu/raven_ce.bin
      -rw-r--r--. 1 root root  37K Oct 15 17:52 /lib/firmware/amdgpu/raven_asd.bin
- `rock-dkms` is definitely not installed.  I'm infact slightly confused if I need this package.  I was under the impression that this package provides the `amdkfd` module, which creates the `/dev/kfd` device needed for ROCm to work.  I'm currently booted into `4.19.0-rc8` (unofficial Fedora compatible vanilla kernel), and both are present on my system.

      # lt /dev/kfd
      crw-rw-rw-. 1 root render 237, 0 Oct 23 08:00 /dev/kfd
      # lsmod | grep kfd
      amdkfd                229376  1
      amd_iommu_v2           20480  1 amdkfd
  I'm not sure if this is also true with the `4.18.x` series (official Fedora kernel). I can check that for my detailed report.
- `yum` is (supported but) deprecated on Fedora, and the equivalent command would be `dnf autoremove rock-dkms`.  However, I had uninstalled with: `dnf history undo <transaction-id>`.  They are similar; infact in my opinion, this is more deterministic than `autoremove`.  Essentially it reverses the transaction.  Say, after I install with `dnf install rocm-dkms`, which has the transaction id `518`, doing `dnf history undo 518` reverses the installation in its entirety. On my system:

      # dnf history list 
      ...
      522 | history undo 518         | 2018-10-10 18:59 | Erase          |   74 EE
      ...
      518 | install rocm-dkms        | 2018-10-09 14:25 | Install        |   74 >E
  The `E` in the `518` line is because the dkms build had failed.

I hope I have answered satisfactorily to your bullet points for now :)

---

### 评论 #10 — jlgreathouse (2018-10-24T02:55:59Z)

Hi @suvayu 

Yep, that's great. I wasn't familiar with `dnf history undo` -- the problem I was looking at was one I ran across while trying to recreate your problem: our `yum/dnf autoremove` for `rocm-dkms` does not appear to remove `rock-dkms` because of some idiosyncrasies in its Obsoletes list. I'm tracking that problem down, but I wanted to see if perhaps keeping some series of commands had left `rock-dkms` installed and thus left its dracut.conf.d files sitting on your disk.

That said, I suppose my next question would be how `dnf history undo` handles "undoing" a transaction. For instance, since installing the RPM creates some DKMS data on the disk, and that DKMS build creates some *other* files -- does the dnf undo get rid of all of those files? Or does it just uninstall the packages and ask that they properly remove all of the files they may create?

To answer your question: you're correct. you *do not* need rock-dkms for your Fedora 28 system. You should be able to use the upstream `amdgpu` and `amdkfd` along with the user-space ROCm software. That said, this whole problem is happening because somewhere along the way the `rock-dkms` package was installed (likely because you installed `rocm-dkms`, which depends on it). I'm just wanting to make sure it's really uninstalled. Since it is, the next question is why it left those files sitting around in the dracut conf folder.

Finally: I understand that the firmware you're using is in the proper `/lib/firmware/amdgpu/` directory. My question is more specifically: are there *any* files in `/lib/firmware/<kernel-version>`? These would have been installed by the `rock-dkms` package, and I'd like to know if those were deleted even though the `dracut.conf.d` file wasn't.

---

### 评论 #11 — suvayu (2018-10-24T05:33:05Z)

Hi @jlgreathouse,

Thanks for sharing your thought process :).

- > how dnf history undo handles "undoing" a transaction

  As far as I understand it, dnf keeps track of every rpm transaction in a db of its own.  When asked to undo, it "undoes" by rolling back the transactions from that db according to a predetermined logic using rpm. *At no point it bye-passes rpm*.

  I took a quick look at the dnf source, the different undoing actions are collected [here](https://github.com/rpm-software-management/dnf/blob/7ee18b471625d5cda45a915a9dd01733c3feb365/dnf/base.py#L2153-L2167):

      # map actions to their opposites
      action_map = {
          libdnf.transaction.TransactionItemAction_DOWNGRADE: None,
          libdnf.transaction.TransactionItemAction_DOWNGRADED: libdnf.transaction.TransactionItemAction_UPGRADE,
          libdnf.transaction.TransactionItemAction_INSTALL: libdnf.transaction.TransactionItemAction_REMOVE,
          libdnf.transaction.TransactionItemAction_OBSOLETE: None,
          libdnf.transaction.TransactionItemAction_OBSOLETED: libdnf.transaction.TransactionItemAction_INSTALL,
          libdnf.transaction.TransactionItemAction_REINSTALL: None,
          # reinstalls are skipped as they are considered as no-operation from history perspective
          libdnf.transaction.TransactionItemAction_REINSTALLED: None,
          libdnf.transaction.TransactionItemAction_REMOVE: libdnf.transaction.TransactionItemAction_INSTALL,
          libdnf.transaction.TransactionItemAction_UPGRADE: None,
          libdnf.transaction.TransactionItemAction_UPGRADED: libdnf.transaction.TransactionItemAction_DOWNGRADE,
          libdnf.transaction.TransactionItemAction_REASON_CHANGE: None,
      }
- Regarding the firmware directory, I can't give you a definitive answer until later today.  I do not have access to my machine right now.  That said, as far as I recall I have not seen any kernel specific firmware directory under `/lib/firmware`. Maybe the `post-remove.sh` script failed halfway through? While going through the `dnf` transaction history earlier, I recall the `dnf history undo 518` command list some output from the dkms uninstallation, but nothing seemed out of the ordinary.

That said, it's probably best not to speculate. I'll report back with a precise recipe, and maybe even attempt to install only the user space packages to get ROCm working ;). Thanks a lot for your patience :)

---

### 评论 #12 — suvayu (2018-10-24T17:02:52Z)

Hi @jlgreathouse,

About the kernel specific firmware directory, it turns out I recalled incorrectly!  The directories are still there.

    # lt -d /lib/firmware/4*
    drwxr-xr-x. 4 root root 4.0K Oct  1 19:41 /lib/firmware/4.18.10-200.fc28.x86_64
    drwxr-xr-x. 4 root root 4.0K Oct  4 15:17 /lib/firmware/4.19.0-0.rc6.git0.1.vanilla.knurd.1.fc28.x86_64
    drwxr-xr-x. 4 root root 4.0K Oct  8 18:52 /lib/firmware/4.19.0-0.rc7.git0.1.vanilla.knurd.1.fc28.x86_64

I also had a closer look at my dnf transaction history.  During installation, the dkms build had failed like this:

    1 Loading new amdgpu-1.9-224.el7 DKMS files...
    2 Building for 4.19.0-0.rc7.git0.1.vanilla.knurd.1.fc28.x86_64
    3 Building initial module for 4.19.0-0.rc7.git0.1.vanilla.knurd.1.fc28.x86_64
    4 Error! Bad return status for module build on kernel: 4.19.0-0.rc7.git0.1.vanilla.knurd.1.fc28.x86_64 (x86_64)
    5 Consult /var/lib/dkms/amdgpu/1.9-224.el7/build/make.log for more information.
    6 warning: %post(rock-dkms-0:1.9-224.el7.noarch) scriptlet failed, exit status 10

Strangely however, uninstallation seems to have gone on without errors!

    1
    2 ------------------------------
    3 Deleting module version: 1.9-224.el7
    4 completely from the DKMS tree.
    5 ------------------------------
    6 Done.

I hope for the moment this is sufficient for you to go on.

---

### 评论 #13 — jlgreathouse (2018-10-24T17:20:27Z)

Thanks for the update. Could you look in those firmware directories to see if there are any amdgpu-related subdirs?

---

### 评论 #14 — suvayu (2018-10-24T17:31:45Z)

Yes there were, with firmware files like: `amdgpu/{vega,raven,polaris}*` and `radeon/{hawaii,kaveri}*`.

---

### 评论 #15 — jlgreathouse (2018-10-25T02:02:49Z)

OK, the firmware files still sitting around implies that the DKMS post-install.sh script wasn't properly called. In the lines before the "Deleting module version: 1.0-224.el7", did you see other lines such as the following? 
```
$ sudo dkms remove amdgpu/1.9-224 --all

-------- Uninstall Beginning --------
Module:  amdgpu
Version: 1.9-224
Kernel:  4.15.0-33-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

amdgpu.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdttm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkcl.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdchash.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amd-sched.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkfd.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


Running the post_remove script:
depmod...

Backing up initrd.img-4.15.0-33-generic to /boot/initrd.img-4.15.0-33-generic.old-dkms
Making new initrd.img-4.15.0-33-generic
(If next boot fails, revert to initrd.img-4.15.0-33-generic.old-dkms image)
update-initramfs......

DKMS: uninstall completed.
```
This is an example from an Ubuntu system, but these are the steps that DKMS calls goes through for each of the installed kernel versions listed there (so if you did a full `dkms remove amdgpu/1.0-224.el7 --all` it should have called that for 4.18.10-200.fc28, 4.19.0-0.rc6,.. and 4.19.0-0.rc7..)

You'll note the important line in there, `Running the post_remove script:`

---

### 评论 #16 — suvayu (2018-10-25T02:45:36Z)

Unfortunately this is all I see :-|.  I retrieved that from the dnf transaction history.

---

### 评论 #17 — jlgreathouse (2018-10-25T03:10:33Z)

Hm. I'm now wondering if this is some kind of incompatibility with `dnf history undo`. It *shouldn't* be broken, since (as you point out) the opposite of installing those packages should just be removing them. And we've seen that it's *trying* to remove the DKMS package..

At the moment, I'm stumped. I don't mean to make you keep messing with your system, but I think I'm at my end as far as being able to post-hoc debug. I'll probably need a guide to recreate the problem so I can watch what ends up going wrong.. Sorry. :(

---

### 评论 #18 — suvayu (2018-10-25T06:41:47Z)

Hi, well as per the action map I posted earlier, `dnf history undo` simply uninstalls the package (i.e. `rpm --erase`), nothing special. It just ensures all the transactions are reversed without solely relying on rpm dependency metadata.

That said, I don't think the transaction history captures the install/uninstall script output in their entirety.  In any case, thanks for your patience :). I will report back with a precise recipe over the weekend.

---

### 评论 #19 — suvayu (2018-10-29T23:42:27Z)

Hi @jlgreathouse,

Firstly, sorry for the delay, my bug report follows.

# Preparing to install ROCm on Fedora 28

The `hcc` compiler depends on the GNU Portable Threads (`Pth`) library.  However, that has not had a new release since 2006. So, on Fedora this has been deprecated for some years for GNU New
Portable Threads (`nPth`).  However Fedora had continued packaging `Pth` until F27 for backwards compatibility.  I had asked on an [issue](https://github.com/RadeonOpenCompute/hcc/issues/884) if it was possible to compile `hcc` against `nPth`, but didn't receive any useful response.  I decided resurrecting the F27 `Pth` package was probably the easiest approach.  So I setup [this](https://copr.fedorainfracloud.org/coprs/fatka/pth/) copr repo.  I enabled it before installing ROCm.


# Installing ROCm on Fedora 28

After enabling the ROCm and the repository mentioned above, `dnf install rocm-dkms`.  As expected, this pulls in everything.

Unfortunately I didn't realise I didn't have the latest Fedora kernel on my system, so the above pulled in the latest `kernel-headers` package (`4.18.16`, whereas my kernel was `4.18.14`).  This led to a skipped dmks build with the following message:

    1 Loading new amdgpu-1.9-224.el7 DKMS files...
    2 Building for 4.18.14-200.fc28.x86_64
    3 Module build for kernel 4.18.14-200.fc28.x86_64 was skipped since the
    4 kernel headers for this kernel does not seem to be installed.

So I manually installed `4.18.16`, which triggered a dkms build, but as reported earlier, it failed:

    1 Error! Bad return status for module build on kernel: 4.18.16-200.fc28.x86_64 (x86_64)
    2 Consult /var/lib/dkms/amdgpu/1.9-224.el7/build/make.log for more information.

You can find the log [here](https://github.com/RadeonOpenCompute/ROCm/files/2527429/make.txt).  Is this expected because of the much newer kernel version?

I checked the initrd image, it had the drivers **and** the firmware files, albeit under `usr/lib/firmware`.  Since `amdgpu` and `amdkfd` are already present in the `4.18.x` series, I still rebooted and expected
it to work.

    # lsmod | grep -e amdgpu -e amdkfd
    amdkfd                221184  1
    amd_iommu_v2           20480  1 amdkfd
    amdgpu               3375104  5
    chash                  16384  1 amdgpu
    i2c_algo_bit           16384  1 amdgpu
    gpu_sched              28672  1 amdgpu
    drm_kms_helper        196608  1 amdgpu
    ttm                   126976  1 amdgpu
    drm                   475136  8 gpu_sched,drm_kms_helper,amdgpu,ttm
    # lt /dev/kfd
    crw-rw-rw-. 1 root render 237, 0 Oct 29 20:55 /dev/kfd


# After reboot

The boot went fine, without the "failed to load firmware" error I was receiving before.  However I cannot run, e.g. `rocminfo`.

    $ /opt/rocm/bin/rocminfo
    hsa api call failure at line 900, file: /home/1019/git/rocm-rel-1.9-211/rocminfo/rocminfo.cc. Call returned 4104

I don't know if things will work if I proceed further (e.g. trying to compile tensorflow).


# Checking uninstall

I decided to check what would be the difference in behaviour between `dnf histo undo <transaction>` and `dnf autoremove rocm-dkms`.  They are nearly identical, apart from that `autoremove` does not uninstall `kernel-devel`, which was pulled in during the installation.  This is understandable because AFAIK, all `kernel*` packages (and probably a few others like `rpm*`, `dnf*`, etc) are excluded from automatic uninstallation.

With that settled, I proceeded with the uninstallation with `autoremove`.  As before, during the uninstallation I got:

    1
    2 ------------------------------
    3 Deleting module version: 1.9-224.el7
    4 completely from the DKMS tree.
    5 ------------------------------
    6 Done.

And as before, both the dracut conf files and the kernel specific firmware files were not removed:

    # ls /etc/dracut.conf.d/
    amdgpu-4.18.16-200.fc28.x86_64.conf
    # ls /lib/firmware/4.18.16-200.fc28.x86_64/
    amdgpu  radeon

Although, I think this time around I would not have noticed since the firmware loaded without problems.

Another observation, the `/opt/rocm/` directory tree is also remaining; all the files have been removed, but the directories are still there.

    $ tree /opt/rocm/
    /opt/rocm/
    ├── include
    │   └── profiler
    ├── opencl
    │   ├── bin
    │   │   └── x86_64
    │   ├── include
    │   │   └── CL
    │   └── lib
    │       └── x86_64
    │           └── bitcode
    └── profiler
        └── CXLActivityLogger
            ├── bin
            │   ├── x86
            │   └── x86_64
            ├── doc
            └── include


# Remarks

This is quite puzzling!  I thought of a possibility, do you think the uninstallation doesn't complete even though no errors are reported by dkms because the initial dkms build had failed?

About installing only the userspace libraries and the `rocminfo` crash, I will fiddle around a bit and see how far I go.  I guess I should open a new issue for that?

Thanks a lot for your time and patience.

Cheers,

---

### 评论 #20 — Johnreidsilver (2018-11-14T10:15:16Z)

For tensorflow over ROCm you'll need to enable Raven Ridge in HIP/HCC. And it's not guaranteed to work.
I have no idea how to do this myself and would like to have detailed instructions.

---

### 评论 #21 — suvayu (2018-11-14T10:47:59Z)

Thanks for pointing this out, I was vaguely aware of this issue.  

---

### 评论 #22 — ROCmSupport (2021-01-07T09:56:49Z)

Hi @suvayu 
There is no update for more than 2 years and so closing this for now.
Request you to open a new issue if you observe the same or any new, for fast progress.
Thank you.

---
