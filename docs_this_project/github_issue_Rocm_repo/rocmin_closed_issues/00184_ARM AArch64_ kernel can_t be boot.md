# ARM AArch64: kernel can't be boot

- **Issue #:** 184
- **State:** closed
- **Created:** 2017-08-22T06:36:47Z
- **Updated:** 2020-11-18T01:38:35Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/184

I have been trying to build ROCK-Kernel-Driver on my ubunu16.04-arm64 server, here are my steps:
1. make defconfig
2. make
3. sudo make modules_install
4. sudo make install

On the 4th step, there is some message like 'W: mdadm: /etc/mdadm/mdadm.conf defines no arrays.' , 
and when I restart the operating system and select the new kernel, it gets stuck,  and the system can't be started. Output of the terminal is as follows:

Loading Linux 4.9.0 ...
Loading initial ramdisk ...
EFI stub: Booting Linux Kernel...
EFI stub: Using DTB from configuration table
EFI stub: Exiting boot services and installing virtual address map...

please tell me how can I fix it? @gstoner 