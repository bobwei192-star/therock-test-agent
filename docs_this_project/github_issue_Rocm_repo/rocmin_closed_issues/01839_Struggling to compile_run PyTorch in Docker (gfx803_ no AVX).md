# Struggling to compile/run PyTorch in Docker (gfx803, no AVX)

- **Issue #:** 1839
- **State:** closed
- **Created:** 2022-10-14T12:11:21Z
- **Updated:** 2024-05-09T16:30:43Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/1839

Hi!

I'm trying to compile PyTorch from source within the `rocm/pytorch:latest-base` Docker image by following the instructions in the docs ([here](https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.3/page/Frameworks_Installation.html) under option 3).

I run `env PYTORCH_ROCM_ARCH=gfx803 ./.jenkins/pytorch/build.sh` and eventually I end up with this error:

```
[ 92%] Linking CXX executable ../bin/MaybeOwned_test
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
```

Trying to work around the tests being unable to link, I run `env PYTORCH_ROCM_ARCH=gfx803 ATEN_NO_TEST=1 BUILD_TEST=0 ./.jenkins/pytorch/build.sh`:

```
[ 97%] Linking CXX executable ../../../../bin/torch_shm_manager
[100%] Built target torch_python
Consolidate compiler generated dependencies of target functorch
Consolidate compiler generated dependencies of target nnapi_backend
[100%] Built target nnapi_backend
[100%] Built target functorch
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
make[2]: *** [caffe2/torch/lib/libshm/CMakeFiles/torch_shm_manager.dir/build.make:118: bin/torch_shm_manager] Error 1
make[1]: *** [CMakeFiles/Makefile2:6477: caffe2/torch/lib/libshm/CMakeFiles/torch_shm_manager.dir/all] Error 2
make: *** [Makefile:146: all] Error 2
```
libtinfo is installed:

```
jenkins@desktop:/sd/pytorch$ apt search libtinfo
Sorting... Done
Full Text Search... Done
libtinfo5/now 6.2-0ubuntu2 amd64 [installed,local]
  shared low-level terminfo library (legacy version)

libtinfo6/now 6.2-0ubuntu2 amd64 [installed,local]
  shared low-level terminfo library for terminal handling

jenkins@desktop:/sd/pytorch$ ldd /opt/rocm-5.3.0/lib/libamd_comgr.so.2
	linux-vdso.so.1 (0x00007fffdbbd8000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fb06bd89000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fb06bd83000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fb06bd60000)
	libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x00007fb06bd30000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fb06bb4e000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fb06b9fd000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fb06b9e2000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb06b7f0000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fb0742b6000)
jenkins@desktop:/sd/pytorch$ ls -l /lib/x86_64-linux-gnu/libtinfo.so.6
lrwxrwxrwx 1 root root 15 Feb 26  2020 /lib/x86_64-linux-gnu/libtinfo.so.6 -> libtinfo.so.6.2
jenkins@desktop:/sd/pytorch$ ls -l /lib/x86_64-linux-gnu/libtinfo.so.6.2
-rw-r--r-- 1 root root 192032 Feb 26  2020 /lib/x86_64-linux-gnu/libtinfo.so.6.2
```