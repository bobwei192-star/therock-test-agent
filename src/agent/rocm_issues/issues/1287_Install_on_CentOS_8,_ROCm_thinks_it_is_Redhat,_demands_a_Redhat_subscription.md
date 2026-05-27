# Install on CentOS 8, ROCm thinks it is Redhat, demands a Redhat subscription.

> **Issue #1287**
> **状态**: closed
> **创建时间**: 2020-11-13T01:36:56Z
> **更新时间**: 2020-11-16T05:44:44Z
> **关闭时间**: 2020-11-13T18:41:26Z
> **作者**: emerth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1287

## 描述

Using instructions at https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel

I am already running EPEL and the recommended kernel. 

So I added a /etc/yum.repos.d/rocm.repo file containing this:

```
[ROCm]
    name=ROCm
    baseurl=https://repo.radeon.com/rocm/centos8/rpm
    enabled=1
    gpgcheck=1
    gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key

```

Install ROCm:

```
[root@localhost ~]# yum install rocm-dkms
Updating Subscription Management repositories.
Unable to read consumer identity
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Warning: failed loading '/etc/yum.repos.d/rocm.repo', skipping.
Last metadata expiration check: 0:08:21 ago on Thu 12 Nov 2020 06:26:18 PM MST.
No match for argument: rocm-dkms
Error: Unable to find a match: rocm-dkms


```

So, the instructions say CentOS does not need this Redhat subscription nonsense, but the installation thinks it cannot load the ROCm repo because the machine does not have a Redhat subscription.

It's a catch 22.

Ubuntu does work, but of late Ubuntu is moving a bit too fast for my taste. I'd like to use something more conservative, like CentOS.



---

## 评论 (4 条)

### 评论 #1 — rkothako (2020-11-13T05:50:14Z)

Hi @emerth 
Thanks for reaching out.

Its strange that CentOS is looking for RHEL subscription.
Can you please share the output of **cat /etc/os-release**

---

### 评论 #2 — emerth (2020-11-13T18:36:47Z)

Hi tkothoka,

Hanging my head in shame I must report this is a PEBKAC issue. I had to remove the subscription-manager, this got rid of the expectation to be registered with Redhat. IDK why that was there in the first place. 

`yum --disablerepo=\* remove subscription-manager`


---

### 评论 #3 — emerth (2020-11-13T18:41:21Z)

One small thing I should add, for the edification of other ppl like me.

Copy/paste the rocm.repo file contents from the ROCm Github install instructions put 3 or 4 leading spaces in front of the lines in the [ROCm] section:

```
[ROCm]
    name=ROCm
    baseurl=https://repo.radeon.com/rocm/centos8/rpm
    enabled=1
    gpgcheck=1
    gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key

```
... and yum does not like those spaces at all. It has to be without any leading spaces, then yum will load the ROCm repo:

```
[ROCm]
name=ROCm
baseurl=https://repo.radeon.com/rocm/centos8/rpm
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key

```

---

### 评论 #4 — rkothako (2020-11-16T05:44:44Z)

Thanks @emerth
I have already fixed the spacing issue.

---
