# [Issue]: AMDGPU DKMS fails to build on kernel 6.12

- **Issue #:** 5111
- **State:** open
- **Created:** 2025-07-28T15:14:27Z
- **Updated:** 2025-11-08T23:46:16Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5111

### Problem Description

Attempting to install amdgpu-dkms from the Ubuntu/Debian sources using any kernel version in the 6.12 series causes installation to fail. Upon inspection, for the current Debian Unstable/Devuan Ceres kernel version, the end of the build log looks like this:

```
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
grep: /usr/src/ofa_kernel/x86_64/6.12.33+deb13-amd64/Module.symvers: No such file or directory
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for module configuration... done
configure: creating ./config.status
config.status: creating config/config.h
Makefile:54: *** dma_resv->seq is missing. exit....  Stop.

# exit code: 2
# elapsed time: 00:00:13
```

[make.log](https://github.com/user-attachments/files/21471718/make.log)

Symlinking `/usr/src/linux-headers-6.12.38+deb13-amd64` to `/usr/src/ofa_kernel/x86_64/6.12.38+deb13-amd64` produces the following output:

```
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for nproc... (cached) yes
checking for module configuration... done
configure: creating ./config.status
config.status: creating config/config.h
Makefile:54: *** dma_resv->seq is missing. exit....  Stop.

# exit code: 2
# elapsed time: 00:00:13
----------------------------------------------------------------
```

[make.log](https://github.com/user-attachments/files/21472014/make.log)

This same behavior is experienced on kernel versions 6.12.33, 6.12.37, and 6.12.38. This same behavior is experienced on Debian and Devuan, which is to be expected as both are identical save for their init systems. 

This result is unexpected, as amdgpu-dkms is explicitly supported on kernel 6.11, and will apparently be supported on 6.14 after the official Ubuntu 24.04.3 HWE kernel release. 6.12 is in between the two, yet fails to work. 

### Operating System

Devuan Excalibur/Ceres (equivalent to Debian Trixie/Sid)

### CPU

AMD Ryzen 7 5700X 8-Core Processor

### GPU

 Advanced Micro Devices [AMD/ATI] Navi 23 [Radeon RX 6650 XT / 6700S 6800S]

### ROCm Version

ROCm 6.4.2, ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

1. Install Debian Trixie/Devuan Excalibur 
2. (Alternatively) Install Debian Bookworm/Devuan Daedalus and add `testing` or `unstable` repositories
3. Upgrade linux-image and linux-headers to their up-to-date versions
4. Install the ROCm repository
5. Attempt to install amdgpu-dkms
6. Curse the darkness

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Debian Trixie is due to release on August 9th, 2 days after the Ubuntu HWE kernel release on the 7th. It will use some point release of kernel 6.12. Neither 6.14 nor 6.11 are offered in the Debian package repositories of Trixie or Sid, precluding their installation. It would be appreciated if ROCm were able to support 6.12, so that Debian users do not have to choose between a functioning AMDGPU setup and a new version of their operating system. 

Barring that, it would be nice if uninstalling amdgpu-dkms also removed `/etc/modprobe.d/blacklist-amdgpu.conf` so that users aren't left with a fallback graphics stack when they fail to install amdgpu-dkms. 