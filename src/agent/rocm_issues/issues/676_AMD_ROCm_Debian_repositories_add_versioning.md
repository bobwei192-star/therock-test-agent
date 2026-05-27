# AMD ROCm Debian repositories add versioning

> **Issue #676**
> **状态**: closed
> **创建时间**: 2019-01-17T08:55:33Z
> **更新时间**: 2023-12-12T19:19:41Z
> **关闭时间**: 2023-12-12T19:19:41Z
> **作者**: kinred
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/676

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Please add versioning to the Debian http://repo.radeon.com/rocm/apt/debian/ ROCm repositories.

Currently only the latest ROCm version and depending packages seems to be available in the Debian repository. 

Otherwise a necessary downgrade or deployment with a specified ROCm version is very hard to achieve.

In this specific case ROCm 1.9.2 is needed as Tensorflow has issues with ROCm 2.0.

---

## 评论 (7 条)

### 评论 #1 — jlgreathouse (2019-01-17T18:09:52Z)

Hi @kinred 

To note, we do have scripts that simplify the installation of previous versions of ROCm available as part of the [Experimental ROC project](https://github.com/RadeonOpenCompute/Experimental_ROC). For example, if you want to install ROCm 1.9.2, just switch to the roc-1.9.2  branch, and you can run the .deb installation scripts from there.

That said, I'll pass this request along.

---

### 评论 #2 — ghost (2019-01-25T22:05:11Z)

Hi together
I just executed the steps @jlgreathouse  mentioned, it worked fine on my machine.
A possible set of commands can be seen here: https://github.com/RadeonOpenCompute/ROCm/issues/668#issuecomment-457742455
The repo also contains ROCm 1.9.1, you just need to replace the version used in the git command if you want this one.

Thank you for this possibility @jlgreathouse !

---

### 评论 #3 — kinred (2019-01-29T12:22:44Z)

@jlgreathouse thank you for the info.

Looking into the Experimental ROC project script, there is shown that there is already an archive of ROCM debian packages at: http://repo.radeon.com/rocm/archive

So with following procedure an defined ROCm version can be installed (e.g. 1.9.2):

```
wget http://repo.radeon.com/rocm/archive/apt_1.9.2.tar.bz2
tar xf apt_1.9.2.tar.bz2
cat ./apt_1.9.2.307/rocm.gpg.key | sudo apt-key add -
echo "deb [trusted=yes arch=amd64] file:///$(pwd)/apt_1.9.2.307/ xenial main" | sudo tee /etc/apt/sources.list.d/rocm.list

sudo apt update
```

The advantage changing the package source instead of using the Experimental_ROC
 script is that one has better control which packages should then be installed with apt, as the options with the Experimental_ROC script are limited as it only mounts the package source temporarily.

If only one could host the source packages in an uncompressed folder structure, it would spare downloading the whole archive and probably fix the issue for most deb based distros.

Also an script for removing the current version of ROCm completely would be nice, as some packages are missed by "apt autoremove rocm-dkms rocm-dev rocm-utils" (like miopengemm and hsakmt-roct).

---

### 评论 #4 — Bengt (2019-05-28T11:51:07Z)

Here is another use case, where a downgrade avoids regressions with gfx900 / Vega GPUs:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/343#issuecomment-470282471

---

### 评论 #5 — dahabakuk (2019-08-03T05:39:13Z)

thanks for the hint to the archive, this made my darktable working again :) ( #846 )

---

### 评论 #6 — tasso (2023-12-08T17:54:47Z)

Is this still an issue?  If not; can we please close it?  Thanks!

---

### 评论 #7 — tasso (2023-12-12T19:19:41Z)

If you go to the following link:

http://repo.radeon.com/rocm/apt/debian/pool/main/r/

All the components and their versions can be found.  Closing issue but if you need further assistant. You can open a new ticket and we will be more than happy to help.

---
