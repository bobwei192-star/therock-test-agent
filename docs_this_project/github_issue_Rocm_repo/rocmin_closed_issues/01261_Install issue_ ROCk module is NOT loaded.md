# Install issue: ROCk module is NOT loaded

- **Issue #:** 1261
- **State:** closed
- **Created:** 2020-10-16T09:29:40Z
- **Updated:** 2020-10-16T10:03:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/1261

I'm trying to install ROCm via the instructions at https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel.
My system:
AMD Ryzen 5 2400G, NVIDIA GTX 1050Ti
Centos 7, kernel 3.10.0-1127.19.1.el7.x86_64
gcc 7.3.1 via devtoolset

I skipped the RHEL steps
Steps taken:
```
sudo yum install -y epel-release
sudo yum install -y dkms kernel-headers-`uname -r` kernel-devel-`uname -r`
```
Create /etc/yum.repos.d/rocm.repo with contents:
```
[ROCm]
ROCm
baseurl=http://repo.radeon.com/rocm/yum/rpm
enabled=1
gpgcheck=1
gpgkey=http://repo.radeon.com/rocm/rocm.gpg.key
```
If there are leading spaces, like on the webpage, I get parsing errors while reading the file.
```
sudo yum install rocm-dkms && sudo reboot
```
This restarts the system and should create the `/dev/kfd` device. This device is not seed via `ls /dev` and when executing `/opt/rocm/bin/rocminfo` results in 
```ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
username is member of video group
hsa api call failure at: /data/jenkins_workspace/centos_pipeline_job_3.8/rocm-rel-3.8/rocm-3.8-30-20200915/7.7/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```