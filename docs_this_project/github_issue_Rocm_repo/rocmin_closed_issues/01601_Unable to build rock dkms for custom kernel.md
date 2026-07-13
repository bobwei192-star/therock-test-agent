# Unable to build rock dkms for custom kernel

- **Issue #:** 1601
- **State:** closed
- **Created:** 2021-10-27T23:11:51Z
- **Updated:** 2024-01-24T22:32:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1601

What i did:

rpm -ivh rock-dkms-4.3-59.el7.noarch.rpm rock-dkms-firmware-4.3-59.el7.noarch.rpm
dkms build -m amdgpu -v 4.3-59.el7 -k 5.12.0
where 5.12.0 is a custom kernel
I got:
https://pastebin.com/AYf7DmTB
"gcc: fatal error: cannot specify -o with -c, -S or -E with multiple files"

I investigated a little up to the running make with debug and i know it's running something like:
https://pastebin.com/sSYqWppF
and the problem is `-I./include ./include/linux/compiler-version.h` stanza which incorrect in terms of syntax, but now i'm struggling to figure out where it's coming from in makefiles.

I know that this problem was reported relatively recently for ubuntu as well.
https://github.com/RadeonOpenCompute/ROCm/issues/1125