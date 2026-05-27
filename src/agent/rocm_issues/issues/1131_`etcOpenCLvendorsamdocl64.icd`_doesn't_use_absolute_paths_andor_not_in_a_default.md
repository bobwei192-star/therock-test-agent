# `/etc/OpenCL/vendors/amdocl64.icd` doesn't use absolute paths and/or not in a default LD_LIBRARY_PATH

> **Issue #1131**
> **状态**: closed
> **创建时间**: 2020-06-04T14:20:31Z
> **更新时间**: 2021-08-08T13:01:32Z
> **关闭时间**: 2021-08-04T09:56:14Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1131

## 描述

Something does install `/etc/OpenCL/vendors/amdocl64.icd` but it isn't in any package, so I suspect this is put there by some post-install script, which feels unnecessary.

Also it simply doesn't work because it is only using the name of the .so file without the path:

```
$ cat /etc/OpenCL/vendors/amdocl64.icd 
libamdocl64.so
$
```

So by default `ocl-icd-libopencl1` (providing `/usr/lib/x86_64-linux-gnu/libOpenCL.so.1.0.0`)  will not be able to find it and simply ignore it.

Tested with `clinfo` version 2.2.18.04.06-1 (https://github.com/Oblomov/clinfo) and `ocl-icd-libopencl1` version 2.2.12-4 ( https://forge.imag.fr/projects/ocl-icd/ ) generic loader. 

```
$ clinfo | egrep -i 'Parallel|HSA'
$
```


Putting absolute path into the icd defintion:

```
$ cat /etc/OpenCL/vendors/amdocl64.icd
/opt/rocm-3.5.0/opencl/lib/libamdocl64.so
$
```

solves it:

```
$ clinfo | egrep -i 'Parallel|HSA'
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Name                                   AMD Accelerated Parallel Processing
  Driver Version                                  3137.0 (HSA1.1,LC)
$
```



---

## 评论 (15 条)

### 评论 #1 — ableeker (2020-06-06T14:37:51Z)

I'm by no means an expert, but I think this is the .icd-file is correct, even though it only contains the filename, and not the full path.

`According to OpenCL specifications from Khronos, the ICD Loader looks for files into /etc/OpenCL/vendors/ directory and, for each file whose name ends with .icd, the ICD Loader loads with dlopen(3) the shared library whose name is on the first line of the .icd file.`

`Shared library name in ".icd" files can have its path, or it can be a plain filename. In the latter case, the ICD shared library will be looked for into the standard dynamic loader paths.`

Actually I don't have installed any other OpenCL packages, only "rocm-dev". I haven't installed ocl-libopencl1, or clinfo, I think they're already included. On my system libOpenCL.so isn't available in /usr/lib either. However if I use clinfo, I get this:

`Platform Name     AMD Accelerated Parallel Processing`
`Platform Name     AMD Accelerated Parallel Processing`
`Driver Version      3137.0 (HSA1.1,LC)`
`Platform Name     AMD Accelerated Parallel Processing`
`Platform Name     AMD Accelerated Parallel Processing`
`Platform Name     AMD Accelerated Parallel Processing`

This doesn't use LD_LIBRARY_PATH, but it uses ldconfig, and files in /etc/ld.so.conf.d. 'ldconfig -p | grep OpenCL' shows this:

`libOpenCL.so.1 (libc6,x86-64) => /opt/rocm/opencl/lib/libOpenCL.so.1`
`libOpenCL.so.1 (libc6,x86-64) => /opt/rocm/lib/libOpenCL.so.1`
`libOpenCL.so (libc6,x86-64) => /opt/rocm/opencl/lib/libOpenCL.so`
`libOpenCL.so (libc6,x86-64) => /opt/rocm/lib/libOpenCL.so`

This way the OpenCL files are included in the library path, and OpenCL can and will be found and used by OpenCL programs.

---

### 评论 #2 — Aceler (2020-06-06T14:58:29Z)

It seems that the right way to fix that is to add a file to /etc/ld.so.conf.d/ which will contain a path to /opt/rocm-VERSION/opencl/lib/.

And this file should be in rocm-opencl package.

---

### 评论 #3 — Aceler (2020-06-06T15:21:51Z)

> `libOpenCL.so.1 (libc6,x86-64) => /opt/rocm/opencl/lib/libOpenCL.so.1`
> `libOpenCL.so.1 (libc6,x86-64) => /opt/rocm/lib/libOpenCL.so.1`
> `libOpenCL.so (libc6,x86-64) => /opt/rocm/opencl/lib/libOpenCL.so`
> `libOpenCL.so (libc6,x86-64) => /opt/rocm/lib/libOpenCL.so`
 
BTW, you have rocm installed in /opt/rocm, while baryluk and me have rocm installed in /opt/rocm-3.5.0

---

### 评论 #4 — ableeker (2020-06-06T16:08:04Z)

This is about ROCm 3.5.0 (version 3137.0), the ROCm file structure for 3.5.0 has been changed to make the files available.

For 3.3.0 I have added a file libopencl.conf to /etc/ld.so.conf.d containing the following path:

`/opt/rocm/opencl/lib/x86_64`

Then I added the path with ldconfig.

Oddly enough some programs still were able to use OpenCL even without this path.

Since 3.3, if you install rocm-dkms, or rocm-dev, it will install ROCm to folder /opt/rocm-3.x.0, but it will also create a symlink /opt/rocm pointing to this folder.

---

### 评论 #5 — baryluk (2020-06-06T17:55:44Z)

I am just asking to do this so it is easier to install and use ROCm, needing to modify `LD_LIBRARY_PATH` and `PATH` for every user or even modifying it system wide is a pain.

With all paths encoded properly one would not need to mess with this, and it will work out of the box after installing deb packages.

Multiple versions of ROCm installed at the same time can be handled in Debian and Ubuntu using `update-alternatives(1)` mechanism, which will still make it all work out of the box nicely.


In my installation there are hsa files in `/etc/ld.so.conf.d/`, but non of them has `/opt/rocm-3.5.0/opencl/lib/` path, so ld can't actually find it:

```
$ ldconfig -p | grep -i OpenCL
	libOpenCL.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libOpenCL.so.1
	libOpenCL.so.1 (libc6) => /lib/i386-linux-gnu/libOpenCL.so.1
	libOpenCL.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libOpenCL.so
	libMesaOpenCL.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libMesaOpenCL.so.1
	libMesaOpenCL.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libMesaOpenCL.so
	libBullet3OpenCL_clew.so.2.88 (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew.so.2.88
	libBullet3OpenCL_clew.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew.so
	libBullet3OpenCL_clew-float64.so.2.88 (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew-float64.so.2.88
	libBullet3OpenCL_clew-float64.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew-float64.so
$
```

Also there are wrong paths there:

```
root$ ldconfig -v 2>&1 | grep 'rocm'  | grep 'No such file or directory'
ldconfig: Can't stat /opt/rocm/hsa/lib: No such file or directory
root$
```

Here are the files:

```
root$ grep . /etc/ld.so.conf.d/hsa-*
/etc/ld.so.conf.d/hsa-ext-rocr-dev.conf:/opt/rocm/hsa/lib
/etc/ld.so.conf.d/hsa-rocr-dev.conf:/opt/rocm-3.5.0/hsa/lib
root$
```

Adding it one to point to the opencl and reruning ldconfig, it does start to work:

```
root$ echo "/opt/rocm-3.5.0/opencl/lib" > /etc/ld.so.conf.d/rocm-opencl.conf
root$ ldconfig
root$
$ ldconfig -p | grep OpenCL
	libamdocl64.so (libc6,x86-64) => /opt/rocm-3.5.0/opencl/lib/libamdocl64.so
	libOpenCL.so.1 (libc6,x86-64) => /opt/rocm-3.5.0/opencl/lib/libOpenCL.so.1
	libOpenCL.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libOpenCL.so.1
	libOpenCL.so.1 (libc6) => /lib/i386-linux-gnu/libOpenCL.so.1
	libOpenCL.so (libc6,x86-64) => /opt/rocm-3.5.0/opencl/lib/libOpenCL.so
	libOpenCL.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libOpenCL.so
	libMesaOpenCL.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libMesaOpenCL.so.1
	libMesaOpenCL.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libMesaOpenCL.so
	libBullet3OpenCL_clew.so.2.88 (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew.so.2.88
	libBullet3OpenCL_clew.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew.so
	libBullet3OpenCL_clew-float64.so.2.88 (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew-float64.so.2.88
	libBullet3OpenCL_clew-float64.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libBullet3OpenCL_clew-float64.so
```


So, my bug is still valid icd file shoudl either use absolute path (it will work with `dlopen`, and I tested it), or in default LD_LIBRARY_PATH (or in `ld.so.conf.d` directory). But in my installation it isn't.

```
$ dpkg -l | egrep 'rocm|hsa' | grep '^ii' | awk '{print $2, $3; }'
comgr 1.6.0.143-rocm-rel-3.5-30-e24e8c1
hsa-ext-rocr-dev 1.1.30500.0-rocm-rel-3.5-30-def83d8
hsa-rocr-dev 1.1.30500.0-rocm-rel-3.5-30-def83d8
hsakmt-roct 1.0.9-347-gd4b224f
rocm-clang-ocl 0.5.0.51-rocm-rel-3.5-30-74b3b81
rocm-opencl 2.0.20191
rocm-opencl-dev 2.0.20191
rocm-utils 3.5.0-30
rocminfo 1.30500.0
```

PS. The `clinfo` in rocm is a different clinfo that I use, but I use Oblomov's clinfo, because it is in my PATH by default, I know it works fine with Nvidia, Intel and Mesa Clover and pocl OpenCL implementations, and I don't want to loose compatibility. And I didn't want to use clinfo bundled with rocm, because I would suspect it has own hardcoded path and/or uses own location to figure the location of the rocm OpenCL loader, which I shouldn't too use.



---

### 评论 #6 — Aceler (2020-06-06T18:05:22Z)

Yes, the bug is still a bug. It is just there are several ways to workaround it, and there are certain conditions where it is not appear.

---

### 评论 #7 — baryluk (2020-06-06T18:07:40Z)

I think one of the solutions (other than using absolute path, or putting rocm in `/usr/local` instead of `/opt`), is to make `rocm-opencl` ship with proper `/etc/ld.so.conf.d/rocm-opencl.conf` file, and call `ldcondig` in post-inst script.


---

### 评论 #8 — ableeker (2020-06-06T22:03:00Z)

ROCm 3.5.0 creates file /etc/ld.so.conf.d/x86_64-libhsakmt.conf, that points to folder /opt/rocm/lib. This folder contains libOpenCL.so, libOpenCL.so.1, and libOpenCL.so.1.2. These three files are all symlinks to file /opt/rocm/opencl/lib/libOpenCL.so.1.2, which is a real file.

When I check ldconfig, I can see that it can find libOpenCL.so, and libOpenCL.so.1, which I guess ought to make OpenCL work. However, I need to add file libopencl.conf to folder /etc/ld.so.conf.d, containing path /opt/rocm/opencl/lib, in order get some OpenCL programs to work. I agree that the installation command should have been done this.

---

### 评论 #9 — ableeker (2020-06-10T22:13:45Z)

I've had another look, and for ROCm 3.5.0 at least, you don't have do the stuff mentioned earlier, 3.5.0 does it for you.

I've decided I only want to install OpenCL, because I don't need the other stuff, so I've removed rocm-dev, and then installed only rocm-opencl. And after doing that, I've linked /opt/rocm to /opt/rocm-3.5.0.

Well, rocm-opencl actually creates files x86_64-rocm-opencl.conf, and x86_64-libhsakmt.conf in folder /etc/ld.so.conf.d (these add paths /opt/rocm/opencl/lib, and /opt/rocm/lib), and then runs ldconfig, so the library path should already be fine.

---

### 评论 #10 — baryluk (2020-09-22T20:03:29Z)

Still broken in ROCm 3.8.0

---

### 评论 #11 — baryluk (2020-11-16T21:04:51Z)

Still broken in ROCm 3.9.0.

I believe I found the issue.

the `postinst` script of the `rocm-opencl3.9.0` uses wrong paths:

```bash
do_ldconfig() {
  if [ -e "/opt/rocm/opencl" ] ; then
    echo /opt/rocm/opencl/lib > /etc/ld.so.conf.d/x86_64-rocm-opencl.conf && ldconfig
  fi
  mkdir -p /etc/OpenCL/vendors && (echo libamdocl64.so > /etc/OpenCL/vendors/amdocl64_30900.icd)
}

INSTALL_PATH=/opt/rocm-3.9.0/opencl
ROCM_LIBPATH=/opt/rocm-3.9.0/lib

case "$1" in
  abort-deconfigure|abort-remove|abort-upgrade)
    echo "$1"
  ;;
  configure)
    mkdir -p ${ROCM_LIBPATH}
    ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so ${ROCM_LIBPATH}/libOpenCL.so
    ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so.1 ${ROCM_LIBPATH}/libOpenCL.so.1
    ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so.1.2 ${ROCM_LIBPATH}/libOpenCL.so.1.2
    do_ldconfig
  ;;

```


As you can see the `do_ldconfig` function uses wrong paths, and the file in ld.so.conf.d is not versioned properly.

The issue is, that it is not really possible to have two different versions installed and both present in ld.so.conf.d. It must be one.

This should probably be managed using debian alternative mechanism.


---

### 评论 #12 — ROCmSupport (2021-02-15T14:42:15Z)

Thanks @baryluk for reaching out.
I will check this for you.

---

### 评论 #13 — ROCmSupport (2021-07-27T12:10:02Z)

Got an update:
Issue is fixed in 4.3 internal code and it will be available soon to public.
Request you to verify with ROCm 4.3 and close accordingly.
Thank you.

---

### 评论 #14 — ROCmSupport (2021-08-04T09:56:14Z)

Verified with ROCm 4.3 and issue is fixed and no more observed.

taccuser@taccuser-SYS-4028GR-TR2:~$ /opt/rocm/opencl/bin/clinfo | egrep -i 'Parallel|HSA'
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Name:                                 AMD Accelerated Parallel Processing
  Driver version:                                3305.0 (HSA1.1,LC)
  Driver version:                                3305.0 (HSA1.1,LC)

---

### 评论 #15 — baryluk (2021-08-08T13:01:32Z)

Still broken in ROCm 4.3.

```
root@debian:~# dpkg -l | egrep 'rocm|hsa|comgr'
ii  comgr                                                       2.1.0.40300-52                         amd64        Library to provide support functions
ii  hsa-rocr-dev                                                1.3.0.40300-52                         amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  hsakmt-roct                                                 20210520.3.071986.40300-52             amd64        HSAKMT library for AMD KFD support
ii  rocm-opencl                                                 2.0.0.40300-52                         amd64        OpenCL: Open Computing Language on ROCclr
ii  rocminfo                                                    1.0.0.40300-52                         amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
root@debian:~# 
```



---
