# [Issue]: rocminfo - Unable to open /dev/kfd read-write: Invalid argument

- **Issue #:** 6166
- **State:** closed
- **Created:** 2026-04-21T00:32:28Z
- **Updated:** 2026-04-24T19:42:21Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6166

### Problem Description

The `rocminfo` command returns an error:

```
ROCk module is loaded
Unable to open /dev/kfd read-write: Invalid argument
x1unix is member of render group
```



### Operating System

Arch Linux (Linux 6.19.12-arch1-1)

### CPU

AMD Ryzen 5 7600X 6-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.2.2

### ROCm Component

rocminfo

### Steps to Reproduce

Run `rocminfo`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

I am not able to run `rocminfo --support` due to a `/dev/kfd` error described in this issue.

### Additional Information

I'm already a member of `render` group:

```
$ stat /dev/kfd
  File: /dev/kfd
  Size: 0         	Blocks: 0          IO Block: 4096   character special file
Device: 0,6	Inode: 524         Links: 1     Device type: 237,0
Access: (0666/crw-rw-rw-)  Uid: (    0/    root)   Gid: (  989/  render)
Access: 2026-04-20 20:07:00.323751788 -0400
Modify: 2026-04-20 20:07:00.323751788 -0400
Change: 2026-04-20 20:07:00.323751788 -0400
 Birth: 2026-04-20 20:06:56.196999863 -0400

$ groups
x1unix sys lock vboxusers wireshark libvirt docker systemd-journal video uucp render kvm input disk wheel adm plugdev

$ lspci | grep VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 48 [Radeon RX 9070/9070 XT/9070 GRE] (rev c0)
```

Here is the strace which might be helpful: [strace.txt](https://github.com/user-attachments/files/26996630/strace.txt)