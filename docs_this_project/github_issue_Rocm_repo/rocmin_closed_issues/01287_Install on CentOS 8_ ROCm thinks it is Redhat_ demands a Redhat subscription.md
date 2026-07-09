# Install on CentOS 8, ROCm thinks it is Redhat, demands a Redhat subscription.

- **Issue #:** 1287
- **State:** closed
- **Created:** 2020-11-13T01:36:56Z
- **Updated:** 2020-11-16T05:44:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1287

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

