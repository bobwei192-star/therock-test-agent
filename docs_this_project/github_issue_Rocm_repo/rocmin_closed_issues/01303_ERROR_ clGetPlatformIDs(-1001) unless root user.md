# ERROR: clGetPlatformIDs(-1001) unless root user

- **Issue #:** 1303
- **State:** closed
- **Created:** 2020-11-23T22:20:51Z
- **Updated:** 2020-12-10T21:52:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1303

clinfo will return `ERROR: clGetPlatformIDs(-1001)` for a regular user but will work as expected for root. I am aware of most posts, around this issue, but none of the previously mentioned issues appear to apply here.

This is with kernel 5.9.8-2-default and a Navi 10 5700 XT GPU. The user account is part of the video and render groups. The permissions on /dev/kfd and /dev/dri are as follows
```
crw-rw-rw-+ 1 root video 241, 0 Nov 23 14:12 /dev/kfd
drwxr-xr-x   2 root root         80 Nov 23 14:12 by-path
crw-rw----+  1 root video  226,   0 Nov 23 14:13 card0
crw-rw-rw-   1 root render 226, 128 Nov 23 14:12 renderD128
```

the files in /etc/ld.so.conf.d appear to point to valid locations which are linked against  the rocm-3.9.0 directory.

I've attached the output of clinfo as root, as well as the strace clinfo as regular user below.

I'd be grateful for any hints

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5586080/clinfo.txt)
[clinfo_trace.txt](https://github.com/RadeonOpenCompute/ROCm/files/5586081/clinfo_trace.txt)



