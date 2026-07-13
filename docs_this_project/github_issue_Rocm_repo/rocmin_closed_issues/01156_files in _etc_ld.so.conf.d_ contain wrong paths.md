# files in /etc/ld.so.conf.d/ contain wrong paths

- **Issue #:** 1156
- **State:** closed
- **Created:** 2020-06-21T18:06:21Z
- **Updated:** 2020-06-24T23:47:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1156

System: openSUSE Tumbleweed, but should apply to SUSE too

During installation, ROCm packages will create files in /etc/ld.so.conf.d/, for example:
/etc/ld.so.conf.d/hsa-rocr-dev.conf

This file points to a nonexistent location:
```
$ cat hsa-rocr-dev.conf 
/opt/rocm/hsa/lib
```

/opt/rocm doesn't exist anymore, since all rocm stuff is in versioned folders like /opt/rocm-3.5.1 now.