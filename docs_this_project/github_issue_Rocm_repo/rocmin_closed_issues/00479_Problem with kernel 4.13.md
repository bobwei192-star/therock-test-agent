# Problem with kernel 4.13

- **Issue #:** 479
- **State:** closed
- **Created:** 2018-07-29T19:36:35Z
- **Updated:** 2018-07-30T19:11:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/479

This is 4x RX580 GPU system, AMD 970 motherboard, booting from USB flash.

On a fresh Ubuntu 16.04 LTS I am trying to install ROCM per this manual:

https://rocm.github.io/ROCmInstall.html

Since it suggests installing kernel 4.13, I decided to do so. After kernel installs and I reboot, I am getting lots of amd-vi completion-wait loop timed out messages. The system boots, however I cannot ssh to it (connection refused), I cannot login locally either: after I type in my username, I get the Login: prompt again w/o asking for password. So, I cannot reboot and I force power off. After that I cannot boot at all, I get the grub error "unknown file system" (not even getting to grub boot menu).

I did it 3 times, and it's always the same. With 4.4.0-116 I can boot normally. This setup also runs with amdgpu-pro w/o any problems under 4.4.0-116. Any ideas, please?