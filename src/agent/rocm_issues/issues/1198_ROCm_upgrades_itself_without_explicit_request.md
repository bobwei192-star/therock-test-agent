# ROCm upgrades itself without explicit request

> **Issue #1198**
> **状态**: closed
> **创建时间**: 2020-08-22T13:41:01Z
> **更新时间**: 2022-02-27T19:31:17Z
> **关闭时间**: 2022-02-27T19:31:16Z
> **作者**: seesturm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1198

## 描述

Just doing normal ubuntu updates causes ROCm to upgrade itself. With normal debian repositories this would not be a problem. But ROCm is different: The [Release Notes](https://github.com/RadeonOpenCompute/ROCm#fresh-installation-of-amd-rocm-v37-recommended) of ROCM 3.7 state that "fresh and clean installation of AMD ROCm v3.7 is recommended".

The reason for this statement becomes obvious after such an involuntary upgrade: the whole ROCm installation is broken and must be fixed by manually executing the steps described in the installation guide. Several issues reported in this project already document this behavior.

While it is can be reasonable to have a manual upgrade process for ROCm software it is not reasonable to expect users to disable all updates for ubuntu. Updates are needed in order to keep the installation secure and to have bugs in other software packages fixed.

---

## 评论 (32 条)

### 评论 #1 — srinivamd (2020-08-22T16:10:24Z)

Please try rocminstall.py script (available at https://github.com/srinivamd/rocminstaller) to install ROCm. It incorporates best practices to install ROCm to avoid issues such as what you experienced. One of the suggested best practices is to install ROCm packages with release-version suffix which avoids these unintended updates.

---

### 评论 #2 — seesturm (2020-08-22T18:20:25Z)

Hi @srinivamd. What is your relation to ROCm? My issue is not a support request but a defect report.

Can you give a pointer where these are documented? Nothing of this is stated in the [Installation Guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#installing-a-rocm-package-from-a-debian-repository). Essentially the Installation Guide does not follow your mentioned "best practices to install ROCm".

ROCm software currently does not have the best reputation among its users and things like this are contributing. I sort of know how to keep my installation working. But why does every single user has to learn the same the hard way?

---

### 评论 #3 — srinivamd (2020-08-22T20:38:39Z)

@seesturm If "Just doing normal ubuntu updates causes ROCm to upgrade itself" is the problem, try the rocminstall.py script (available at https://github.com/srinivamd/rocminstaller) here that I have used to make my experience simpler.

---

### 评论 #4 — baryluk (2020-11-23T17:44:04Z)

@seesturm This is not a defect, but intentional.

If you want to use only specific version of ROCm you can do that by installing specific version of ROCm using versioned packages.

What do you mean by:

> whole ROCm installation is broken and must be fixed by manually executing the steps described in the installation guide

?

---

### 评论 #5 — seesturm (2020-11-23T18:08:48Z)

@baryluk ROCm team has to choose and document the intended upgrade method:

- Either normal debian style "automatic" upgrades are supported - without the need to (manually) uninstall previous installation, or
- ROCm is meant to be manually upgraded. In which case upgrade must not happen automatically.

According to current [Release Notes](https://github.com/RadeonOpenCompute/ROCm#fresh-installation-of-amd-rocm-v39-recommended) the manual upgrade method is implied: "_A fresh and clean installation of AMD ROCm v3.9 is recommended. An upgrade from previous releases to AMD ROCm v3.9 is not supported_". But yet upgrades happen automatically - and break the installation.

> What do you mean by:
> 
> > whole ROCm installation is broken and must be fixed by manually executing the steps described in the installation guide
> 
> ?

After involuntary upgrade ROCm installation is in an inconsitent state. It simply does not work for me anymore. E.g. I cannot execute tensorflow applications. And there are lots of issues in this tracker which are just caused by these involuntary upgrades. Most of the time the those "issues" are "solved" by a fresh install.



---

### 评论 #6 — baryluk (2020-11-23T22:03:11Z)

If the upgrade doesn't work properly, then it is a bug indeed.

It would be good to track what is the issue.

Where there any warnings or errors during the apt upgrade?

What is the output of `rocminfo` after an upgrade?

What is the content of `/opt/` after the upgrade? (Is it just `rocm`, or is there something more?)

What is the output of `grep -H . /etc/ld.so.conf.d/*rocm*conf` and `grep -H . /etc/OpenCL/vendors/amd*icd` after the upgrade.

What is the output of `/usr/bin/clinfo` and  `env /opt/rocm*/opencl/bin/clinfo` after the upgrade?



---

### 评论 #7 — ROCmSupport (2020-11-24T07:10:49Z)

Thanks @seesturm for reaching out.
Currently we are not supporting ROCm upgrade functionality and so it can/might not work.
We understand the query and we will get back asap on this.


---

### 评论 #8 — srinivamd (2020-11-24T14:54:21Z)

@seesturm As mentioned earlier, try the rocminstall.py script  (available at https://github.com/srinivamd/rocminstaller) to install ROCm version on your system to avoid accidental updates, etc. However, before using the script you would have to remove all ROCm packages, reboot, and then install ROCm using the rocminstall.py (use --rev option) to select a specific ROCm version/release to install.
Please remove any existing ROCm repo setup on your system.
The rocminstall.py script is open sourced, source code can be reviewed.
It installs ROCm using the "version-suffixed" named packages instead of generic named packages. In other words, install rocm-dev3.7.0 (for 3.7 release) instead of rocm-dev (generic name). That allows the system to be keyed on the specific set of packages installed, and not get updated when new release of ROCm is published with updated generic-named packages but different version-suffix-named packages - the version-suffix packages will have to be explicitly installed. THe rocminstall.py script encodes these details in it.
When a new ROCm release is announced, you can use rocminstall.py script to install the new release, side-to-side to the existing installed release without having to uninstall ROCm first as a "fresh and clean" install would require.
You can select the ROCm version to use by using /opt/rocm-X.Y.Z/bin to invoke the specific version. Or create a symbolic link to use a specific version by default.
HTH.

---

### 评论 #9 — ROCmSupport (2020-11-25T07:10:41Z)

Hi @seesturm 

This falls into the path of ROCm upgrade and as we all know that upgrade does not work for now. 
So we request to uninstall the and install the ROCm version of choice.
Once we enable ROCm upgrade, this will be taken care.
Hope this helps.
Thank you.



---

### 评论 #10 — seesturm (2020-11-25T07:45:08Z)

Installation instructions don't document how to "install the ROCm version of choice". [Installation Guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) explicitly requests following entry for apt
`deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main'`

When following these instructions ROCm upgrades without request.

---

### 评论 #11 — ROCmSupport (2020-11-25T08:15:46Z)

Hi @seesturm 
I will reach docs team and will ask them to update/modify to call specific rocm versions also.
For now you can install specific ROCm version as **deb [arch=amd64] https://repo.radeon.com/rocm/apt/3.7/ xenial main**
You can replace by changing 3.7 to any other version like 3.6, 3.5, 3.9 etc.,.

---

### 评论 #12 — baryluk (2020-11-25T19:58:33Z)

@seesturm BTW. The Installation guide do have a section about removing ROCm, so it should be relatively well working method: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#uninstalling-rocm-packages-from-ubuntu 

Once you remove all relevant pacakges (verify by checking `dpkg -l | grep rocm` or similar), reboot, then try doing an update and installing again.

@ROCmSupport  I added some fixes to the installation guide, to point some of these issues https://github.com/RadeonOpenCompute/ROCm_Documentation/pull/103



---

### 评论 #13 — baryluk (2020-11-25T19:59:56Z)

@seesturm Yes, it is known the installation doesn't fully follow Debian policies. There are multiple bugs about that already open. The issue with the upgrade process are known to users and ROCm team. It is slowly being worked on.

---

### 评论 #14 — ROCmSupport (2020-11-26T09:00:26Z)

Hi @seesturm 
I request to close this ticket, if you feel that you got reasonable answers.
Thank you.

---

### 评论 #15 — seesturm (2020-11-26T09:23:45Z)

When following the installation instructions ROCm still upgrades itself. So issue is not solved yet.

---

### 评论 #16 — ROCmSupport (2020-11-26T11:06:23Z)

Currently ROCm upgrades automatically along with OS upgrade.
So request to uninstall ROCm and install ROCm again, until we enable ROCm upgrade functionality officially.
Thank you.

---

### 评论 #17 — seesturm (2020-11-26T19:52:24Z)

This issue is not meant as a support request, but intended for tracking a defect. Maybe the defect is fixed by changing the documentation (e.g. use the fixed-version repo path) or by crafting the packages according to debian standard. My understanding is that we can agree on that.

So, do you want this issue tracker for defect tracking? If yes, then I'd say we should keep this issue open until it is solved. Or if it is a duplicate, then please inform about actual defect tracking issue ID.
Thank you.

---

### 评论 #18 — baryluk (2020-11-26T20:00:21Z)

Yeah, I think the bug can stay open. I don't see any existing open issue with the same topic.

Leaving it open is good for tracking, and for making sure people in the future can easily find it by search.

---

### 评论 #19 — ROCmSupport (2020-11-27T13:11:41Z)

Hi @seesturm 
I will work with documentation team on this and will make sure that this point is covered.
Thank you.

---

### 评论 #20 — ROCmSupport (2020-12-15T10:20:14Z)

Hi @seesturm, this has been updated in ROCm docs @ 
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#build-amd-rocm

**After an operating system upgrade, AMD ROCm may upgrade automatically and result in an error. This is because AMD ROCm does not support upgrades currently. You must uninstall and reinstall AMD ROCm after an operating system upgrade.**

---

### 评论 #21 — seesturm (2020-12-15T10:59:49Z)

So you are closing this issue without a fix?
The problem is still present: ROCm upgrades itself automatically and as a consequence gets broken. Each and every ROCm user will be hit by this by surprise when they least expect it!

---

### 评论 #22 — ROCmSupport (2020-12-15T11:03:40Z)

Hi @seesturm 
As I mentioned, its not a different issue than ROCm upgrade.
When upgrade works, this will be taken care automatically and so its not a separate issue.
For now, As I promised, we have updated the documentation with the information.
We have plans to make ROCm upgrade works well at 4.2 or 4.3 time frame.

---

### 评论 #23 — seesturm (2020-12-15T11:08:28Z)

No, the instructions don't provide information on how to deal with this. They basically just give a warning that a ROCm can break at any time. Just putting a warning is not a fix.

Furthermore: The way it is written one might read it as only releveant when Ubuntu upgrades say from 20.04 to 20.10. But ROCm breaks when ROCm is (automatically) upgraded.

---

### 评论 #24 — ROCmSupport (2020-12-15T11:56:48Z)

Hi @seesturm 
The answer is simple again.
ROCm upgrade does not work for now.
Once ROCm upgrade works, all kind of scenarios will/should work.
This scenario is also a child of ROCm upgrade.
Anyway I will keep it open until ROCm upgrade functionality comes back to working mode in 4.2 or 4.3

---

### 评论 #25 — ROCmSupport (2022-02-22T13:04:51Z)

Hi @seesturm 
"ROCm upgrade" matured a lot, should work well now and I request to try and update asap.
let me know if you find any problems with upgrade so that we can fix the issues.
Thank you.

---

### 评论 #26 — seesturm (2022-02-22T13:09:50Z)

Still have Vega 56 hardware. What is the release in which this was fixed and does this release support Vega 56?

---

### 评论 #27 — ROCmSupport (2022-02-22T13:56:02Z)

Hi @seesturm 
Vega10/MI25 is dropped from supported list from ROCm 4.5. Thank you.

---

### 评论 #28 — seesturm (2022-02-22T15:23:03Z)

Hi @ROCmSupport 
I'm now confused. Can I test this with my hardware or not?

---

### 评论 #29 — ROCmSupport (2022-02-23T11:27:27Z)

Hi @seesturm,
I suggest to try with the supported hardware. Thank you.

---

### 评论 #30 — seesturm (2022-02-23T17:49:07Z)

Hi @ROCmSupport 
I hope it is a misunderstanding but your phrasing sounds like you want me to buy new hardware. But I'm not planning to buy new hardware. Can you clarify?

---

### 评论 #31 — ROCmSupport (2022-02-24T04:59:38Z)

Hi @seesturm 
Sorry for misunderstanding :)
I am saying that, if possible, try it on a supported hardware. Because though upgrade works now, your hardware does not support it.
Request to take your call. Thank you.

---

### 评论 #32 — seesturm (2022-02-27T19:31:16Z)

My interpretation of the answer is that my hardware is no longer supported. Closing issue since ROCm is no longer useful for me.

---
