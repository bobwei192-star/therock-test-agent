# `error: .amdhsa_reserve_xnack_mask does not match target id` when building gcc-11 w/ rocm-4.2

> **Issue #1476**
> **状态**: closed
> **创建时间**: 2021-05-19T17:51:30Z
> **更新时间**: 2024-04-19T21:15:50Z
> **关闭时间**: 2024-04-19T21:15:49Z
> **作者**: nolta
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1476

## 描述

I'm trying to build gcc v11.1.0 with [offload support for AMD GPUs](https://gcc.gnu.org/wiki/Offloading#For_AMD_GCN:), using the LLVM that comes with ROCm.

I can successfully build using ROCm v4.0.1, [after patching gcc  for an issue in LLVM 11](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=97827).

However, with v4.2.0 i see the following error in `gfx900/libgcc/config.log`:

```
/tmp/cc4xyz0B.s:32:4: error: .amdhsa_reserve_xnack_mask does not match target id
          .amdhsa_reserve_xnack_mask    0
          ^~~~~~~~~~~~~~~~~~~~~~~~~~
/tmp/cc4xyz0B.s:33:4: error: unknown directive
          .amdhsa_private_segment_fixed_size    16384
          ^
/tmp/cc4xyz0B.s:34:4: error: unknown directive
          .amdhsa_group_segment_fixed_size      65536
          ^
/tmp/cc4xyz0B.s:35:4: error: unknown directive
          .amdhsa_float_denorm_mode_32  3
          ^
/tmp/cc4xyz0B.s:36:4: error: unknown directive
          .amdhsa_float_denorm_mode_16_64       3
          ^
/tmp/cc4xyz0B.s:37:2: error: unknown directive
        .end_amdhsa_kernel
        ^
```

Here's a bash script to reproduce the issue:
<details>

```bash
#!/bin/bash
set -eufx -o pipefail

rocm=/opt/rocm-4.2.0

# install directory
prefix=$(mktemp -d)

# build directory
cd "$(mktemp -d)"

# download gcc
gcc="gcc-11.1.0"
archive="$gcc.tar.xz"
url="https://gcc.gnu.org/pub/gcc/releases/$gcc/$archive"
wget "$url"
tar -xaf "$archive"

# download prerequisites
pushd "$gcc"
./contrib/download_prerequisites
popd

offload_target=amdgcn-amdhsa

# gcc assembler doesn't handle amd gcn yet, so use llvm
mkdir -p "$prefix/$offload_target/bin"
src="$rocm/llvm/bin"
dst="$prefix/$offload_target/bin"
ln -s "$src/llvm-ar"    "$dst/ar"
ln -s "$src/llvm-ar"    "$dst/ranlib"
ln -s "$src/llvm-lipo"  "$dst/lipo"
ln -s "$src/llvm-mc"    "$dst/as"
ln -s "$src/llvm-nm"    "$dst/nm"
ln -s "$src/llvm-strip" "$dst/strip"
ln -s "$src/lld"        "$dst/ld"

# download newlib
newlib="newlib-4.1.0"
archive="$newlib.tar.gz"
wget "ftp://sourceware.org/pub/newlib/$archive"
tar -xaf "$archive"

# prep gcc
pushd "$gcc"
ln -s ../$newlib/newlib newlib
target=$(./config.guess)
popd

# build offload compiler
mkdir build-offload
pushd build-offload
../$gcc/configure --prefix="$prefix" \
    --disable-libquadmath \
    --disable-sjlj-exceptions \
    --enable-as-accelerator-for="$target" \
    --enable-languages=c,c++,fortran,lto \
    --enable-newlib-io-long-long \
    --target="$offload_target" \
    --with-build-time-tools="$prefix/$offload_target/bin" \
    --with-newlib
make -j"$(nproc)"
popd
```

</details>

---

## 评论 (25 条)

### 评论 #1 — ROCmSupport (2021-06-01T10:33:53Z)

Thanks @nolta for reaching out.
I will check and get back asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-06-01T10:55:14Z)

Hi @nolta 
I am observing below error.

checking whether ln -s works... yes
checking for amdgcn-amdhsa-gcc... /tmp/tmp.i7Ti5PFAyn/build-offload/./gcc/xgcc -B/tmp/tmp.i7Ti5PFAyn/build-offload/./gcc/ -nostdinc -B/tmp/tmp.i7Ti5PFAyn/build-offload/amdgcn-amdhsa/gfx900/newlib/ -isystem /tmp/tmp.i7Ti5PFAyn/build-offload/amdgcn-amdhsa/gfx900/newlib/targ-include -isystem /tmp/tmp.i7Ti5PFAyn/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.3fCulup2CT/amdgcn-amdhsa/bin/ -B/tmp/tmp.3fCulup2CT/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.3fCulup2CT/amdgcn-amdhsa/include -isystem /tmp/tmp.3fCulup2CT/amdgcn-amdhsa/sys-include  -march=gfx900
checking for suffix of object files... mv -f .deps/libcp1plugin.Tpo .deps/libcp1plugin.Plo
/bin/bash ./libtool --tag=CXX   --mode=link g++ -W -Wall  -fvisibility=hidden -fcf-protection  -g -O2 -module -export-symbols ../../gcc-11.1.0/libcc1/libcp1plugin.sym  -Xcompiler '-static-libstdc++' -Xcompiler '-static-libgcc' -o libcp1plugin.la -rpath /tmp/tmp.3fCulup2CT/lib/gcc/amdgcn-amdhsa/11.1.0/plugin libcp1plugin.lo callbacks.lo connection.lo marshall.lo   -Wc,../libiberty/pic/libiberty.a
configure: error: in `/tmp/tmp.i7Ti5PFAyn/build-offload/amdgcn-amdhsa/gfx900/libgcc':
configure: error: cannot compute suffix of object files: cannot compile
See `config.log' for more details
make[1]: *** [Makefile:14657: configure-target-libgcc] Error 1
make[1]: *** Waiting for unfinished jobs....
libtool: link: g++  -fPIC -DPIC -shared -nostdlib /usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu/crti.o /usr/lib/gcc/x86_64-linux-gnu/9/crtbeginS.o  .libs/libcp1plugin.o .libs/callbacks.o .libs/connection.o .libs/marshall.o   -L/usr/lib/gcc/x86_64-linux-gnu/9 -L/usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu -L/usr/lib/gcc/x86_64-linux-gnu/9/../../../../lib -L/lib/x86_64-linux-gnu -L/lib/../lib -L/usr/lib/x86_64-linux-gnu -L/usr/lib/../lib -L/usr/lib/gcc/x86_64-linux-gnu/9/../../.. -lstdc++ -lm -lc -lgcc_s /usr/lib/gcc/x86_64-linux-gnu/9/crtendS.o /usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu/crtn.o  -static-libstdc++ -static-libgcc ../libiberty/pic/libiberty.a   -Wl,-soname -Wl,libcp1plugin.so.0 -Wl,-retain-symbols-file -Wl,../../gcc-11.1.0/libcc1/libcp1plugin.sym -o .libs/libcp1plugin.so.0.0.0
libtool: link: (cd ".libs" && rm -f "libcp1plugin.so.0" && ln -s "libcp1plugin.so.0.0.0" "libcp1plugin.so.0")
libtool: link: (cd ".libs" && rm -f "libcp1plugin.so" && ln -s "libcp1plugin.so.0.0.0" "libcp1plugin.so")
libtool: link: ( cd ".libs" && rm -f "libcp1plugin.la" && ln -s "../libcp1plugin.la" "libcp1plugin.la" )
make[3]: Leaving directory '/tmp/tmp.i7Ti5PFAyn/build-offload/libcc1'
make[2]: Leaving directory '/tmp/tmp.i7Ti5PFAyn/build-offload/libcc1'
make[1]: Leaving directory '/tmp/tmp.i7Ti5PFAyn/build-offload'
make: *** [Makefile:950: all] Error 2


---

### 评论 #3 — ROCmSupport (2021-06-03T09:46:39Z)

Hi @nolta 
Request you to check my previous comment and help me with more information.
Thank you.

---

### 评论 #4 — nolta (2021-06-03T14:55:06Z)

Yes, if you look in `/tmp/tmp.i7Ti5PFAyn/build-offload/amdgcn-amdhsa/gfx900/libgcc/config.log`, you'll see the error message.

---

### 评论 #5 — ROCmSupport (2021-06-15T06:31:13Z)

I found below errors from config.log. Rest all looks good for me.

xgcc: error: unrecognized command-line option '-V'
xgcc: fatal error: no input files
compilation terminated.
configure:3546: $? = 1
configure:3535: /tmp/tmp.tEy6eB7xw3/build-offload/./gcc/xgcc -B/tmp/tmp.tEy6eB7xw3/build-offload/./gcc/ -nostdinc -B/tmp/tmp.tEy6eB7xw3/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.tEy6eB7xw3/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.tEy6eB7xw3/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.uInp3iqDeG/amdgcn-amdhsa/bin/ -B/tmp/tmp.uInp3iqDeG/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.uInp3iqDeG/amdgcn-amdhsa/include -isystem /tmp/tmp.uInp3iqDeG/amdgcn-amdhsa/sys-include    -qversion >&5
xgcc: error: unrecognized command-line option '-qversion'; did you mean '--version'?
xgcc: fatal error: no input files
compilation terminated.


---

### 评论 #6 — nolta (2021-06-15T13:40:56Z)

Yes, i see those messages too.

Maybe it will help if you add the following line to the end of my original script:

```
grep -C3 error: build-offload/amdgcn-amdhsa/gfx900/libgcc/config.log
```

---

### 评论 #7 — nolta (2021-06-15T13:53:32Z)

You'll also need to add the line `set +e` before calling `make`.

---

### 评论 #8 — ROCmSupport (2021-07-06T05:53:13Z)

Hi @nolta 
I am still observing the same issue after above checks.
Can you please share more information to proceed further.
Thank you.

---

### 评论 #9 — nolta (2021-07-06T15:55:41Z)

Can you post your copy of `build-offload/amdgcn-amdhsa/gfx900/libgcc/config.log`?

---

### 评论 #10 — ROCmSupport (2021-07-07T10:28:16Z)

taccuser@taccuser-GA-990FXA-UD5:~$ cat /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/libgcc/config.log
This file contains any messages produced by compilers while
running configure, to aid debugging if configure makes a mistake.

It was created by GNU C Runtime Library configure 1.0, which was
generated by GNU Autoconf 2.69.  Invocation command line was

  $ /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/libgcc/configure --srcdir=../../../gcc-11.1.0/libgcc --cache-file=./config.cache --with-newlib --enable-multilib --with-cross-host=x86_64-pc-linux-gnu --prefix=/tmp/tmp.k7ZL0TEufW --disable-libquadmath --disable-sjlj-exceptions --enable-as-accelerator-for=x86_64-pc-linux-gnu --enable-newlib-io-long-long --with-build-time-tools=/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin --with-newlib --enable-languages=c,c++,fortran,lto --program-transform-name=s&^&amdgcn-amdhsa-& --disable-option-checking --with-target-subdir=amdgcn-amdhsa --build=x86_64-pc-linux-gnu --host=amdgcn-amdhsa --target=amdgcn-amdhsa

## --------- ##
## Platform. ##
## --------- ##

hostname = taccuser-GA-990FXA-UD5
uname -m = x86_64
uname -r = 5.8.0-59-generic
uname -s = Linux
uname -v = #66~20.04.1-Ubuntu SMP Thu Jun 17 11:14:10 UTC 2021

/usr/bin/uname -p = x86_64
/bin/uname -X     = unknown

/bin/arch              = x86_64
/usr/bin/arch -k       = unknown
/usr/convex/getsysinfo = unknown
/usr/bin/hostinfo      = unknown
/bin/machine           = unknown
/usr/bin/oslevel       = unknown
/bin/universe          = unknown

PATH: /home/taccuser/.local/bin
PATH: /usr/local/sbin
PATH: /usr/local/bin
PATH: /usr/sbin
PATH: /usr/bin
PATH: /sbin
PATH: /bin
PATH: /usr/games
PATH: /usr/local/games
PATH: /snap/bin


## ----------- ##
## Core tests. ##
## ----------- ##

configure:2079: creating cache ./config.cache
configure:2300: checking build system type
configure:2314: result: x86_64-pc-linux-gnu
configure:2334: checking host system type
configure:2347: result: amdgcn-unknown-amdhsa
configure:2450: checking for --enable-version-specific-runtime-libs
configure:2463: result: no
configure:2534: checking for a BSD-compatible install
configure:2602: result: /usr/bin/install -c
configure:2618: checking for gawk
configure:2645: result: mawk
configure:2752: checking for amdgcn-amdhsa-ar
configure:2779: result: amdgcn-amdhsa-ar
configure:2844: checking for amdgcn-amdhsa-lipo
configure:2871: result: amdgcn-amdhsa-lipo
configure:2936: checking for amdgcn-amdhsa-nm
configure:2963: result: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/nm
configure:3028: checking for amdgcn-amdhsa-ranlib
configure:3055: result: amdgcn-amdhsa-ranlib
configure:3120: checking for amdgcn-amdhsa-strip
configure:3147: result: amdgcn-amdhsa-strip
configure:3209: checking whether ln -s works
configure:3213: result: yes
configure:3230: checking for amdgcn-amdhsa-gcc
configure:3257: result: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include
configure:3526: checking for C compiler version
configure:3535: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    --version >&5
xgcc (GCC) 11.1.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

configure:3546: $? = 0
configure:3535: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    -v >&5
Reading specs from /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/specs
COLLECT_GCC=/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc
COLLECT_LTO_WRAPPER=/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/lto-wrapper
Target: amdgcn-amdhsa
Configured with: ../gcc-11.1.0/configure --prefix=/tmp/tmp.k7ZL0TEufW --disable-libquadmath --disable-sjlj-exceptions --enable-as-accelerator-for=x86_64-pc-linux-gnu --enable-languages=c,c++,fortran,lto --enable-newlib-io-long-long --target=amdgcn-amdhsa --with-build-time-tools=/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin --with-newlib
Thread model: gcn
Supported LTO compression algorithms: zlib
gcc version 11.1.0 (GCC)
configure:3546: $? = 0
configure:3535: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    -V >&5
xgcc: error: unrecognized command-line option '-V'
xgcc: fatal error: no input files
compilation terminated.
configure:3546: $? = 1
configure:3535: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    -qversion >&5
xgcc: error: unrecognized command-line option '-qversion'; did you mean '--version'?
xgcc: fatal error: no input files
compilation terminated.
configure:3546: $? = 1
configure:3562: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    -o conftest -g -O2   conftest.c  >&5
/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/as: 106: exec: -triple=amdgcn--amdhsa: not found
configure:3565: $? = 1
configure:3778: checking for suffix of object files
configure:3800: /tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include    -c -g -O2  conftest.c >&5
/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/as: 106: exec: -triple=amdgcn--amdhsa: not found
configure:3804: $? = 1
configure: failed program was:
| /* confdefs.h */
| #define PACKAGE_NAME "GNU C Runtime Library"
| #define PACKAGE_TARNAME "libgcc"
| #define PACKAGE_VERSION "1.0"
| #define PACKAGE_STRING "GNU C Runtime Library 1.0"
| #define PACKAGE_BUGREPORT ""
| #define PACKAGE_URL "http://www.gnu.org/software/libgcc/"
| /* end confdefs.h.  */
|
| int
| main ()
| {
|
|   ;
|   return 0;
| }
configure:3818: error: in `/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/libgcc':
configure:3820: error: cannot compute suffix of object files: cannot compile
See `config.log' for more details

## ---------------- ##
## Cache variables. ##
## ---------------- ##

ac_cv_build=x86_64-pc-linux-gnu
ac_cv_env_CC_set=set
ac_cv_env_CC_value='/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include   '
ac_cv_env_CFLAGS_set=set
ac_cv_env_CFLAGS_value='-g -O2'
ac_cv_env_CPPFLAGS_set=set
ac_cv_env_CPPFLAGS_value=
ac_cv_env_CPP_set=
ac_cv_env_CPP_value=
ac_cv_env_LDFLAGS_set=set
ac_cv_env_LDFLAGS_value=
ac_cv_env_LIBS_set=
ac_cv_env_LIBS_value=
ac_cv_env_build_alias_set=set
ac_cv_env_build_alias_value=x86_64-pc-linux-gnu
ac_cv_env_host_alias_set=set
ac_cv_env_host_alias_value=amdgcn-amdhsa
ac_cv_env_target_alias_set=set
ac_cv_env_target_alias_value=amdgcn-amdhsa
ac_cv_host=amdgcn-unknown-amdhsa
ac_cv_prog_AR=amdgcn-amdhsa-ar
ac_cv_prog_AWK=mawk
ac_cv_prog_CC='/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include   '
ac_cv_prog_LIPO=amdgcn-amdhsa-lipo
ac_cv_prog_NM=/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/nm
ac_cv_prog_RANLIB=amdgcn-amdhsa-ranlib
ac_cv_prog_STRIP=amdgcn-amdhsa-strip

## ----------------- ##
## Output variables. ##
## ----------------- ##

AR='amdgcn-amdhsa-ar'
AWK='mawk'
CC='/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/xgcc -B/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/ -nostdinc -B/tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/ -isystem /tmp/tmp.e2lZV6kwY8/build-offload/amdgcn-amdhsa/newlib/targ-include -isystem /tmp/tmp.e2lZV6kwY8/gcc-11.1.0/newlib/libc/include -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/bin/ -B/tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/lib/ -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/include -isystem /tmp/tmp.k7ZL0TEufW/amdgcn-amdhsa/sys-include   '
CET_FLAGS=''
CFLAGS='-g -O2'
CPP=''
CPPFLAGS=''
DEFS=''
ECHO_C=''
ECHO_N='-n'
ECHO_T=''
EGREP=''
EXEEXT=''
GREP=''
INSTALL_DATA='/usr/bin/install -c -m 644'
INSTALL_PROGRAM='/usr/bin/install -c'
INSTALL_SCRIPT='/usr/bin/install -c'
LDFLAGS=''
LIBOBJS=''
LIBS=''
LIPO='amdgcn-amdhsa-lipo'
LN_S='ln -s'
LTLIBOBJS=''
MAINT='#'
NM='/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/nm'
OBJEXT=''
PACKAGE_BUGREPORT=''
PACKAGE_NAME='GNU C Runtime Library'
PACKAGE_STRING='GNU C Runtime Library 1.0'
PACKAGE_TARNAME='libgcc'
PACKAGE_URL='http://www.gnu.org/software/libgcc/'
PACKAGE_VERSION='1.0'
PATH_SEPARATOR=':'
PICFLAG='-fPIC'
RANLIB='amdgcn-amdhsa-ranlib'
SHELL='/bin/bash'
STRIP='amdgcn-amdhsa-strip'
ac_ct_CC=''
accel_dir_suffix=''
asm_hidden_op=''
bindir='${exec_prefix}/bin'
build='x86_64-pc-linux-gnu'
build_alias='x86_64-pc-linux-gnu'
build_cpu='x86_64'
build_libsubdir='build-x86_64-pc-linux-gnu'
build_os='linux-gnu'
build_subdir='build-x86_64-pc-linux-gnu'
build_vendor='pc'
cpu_type=''
datadir='${datarootdir}'
datarootdir='${prefix}/share'
decimal_float=''
docdir='${datarootdir}/doc/${PACKAGE_TARNAME}'
double_type_size=''
dvidir='${docdir}'
enable_decimal_float=''
enable_execute_stack=''
enable_gcov='yes'
enable_shared='yes'
enable_vtable_verify='no'
exec_prefix='NONE'
extra_parts=''
fixed_point=''
force_explicit_eh_registry=''
get_gcc_base_ver=''
host='amdgcn-unknown-amdhsa'
host_alias='amdgcn-amdhsa'
host_cpu='amdgcn'
host_noncanonical='amdgcn-amdhsa'
host_os='amdhsa'
host_subdir='.'
host_vendor='unknown'
htmldir='${docdir}'
includedir='${prefix}/include'
infodir='${datarootdir}/info'
libdir='${exec_prefix}/lib'
libexecdir='${exec_prefix}/libexec'
libgcc_topdir='../../../gcc-11.1.0/libgcc/..'
localedir='${datarootdir}/locale'
localstatedir='${prefix}/var'
long_double_type_size=''
mandir='${datarootdir}/man'
md_unwind_header=''
oldincludedir='/usr/include'
pdfdir='${docdir}'
prefix='/tmp/tmp.k7ZL0TEufW'
program_transform_name='s&^&amdgcn-amdhsa-&'
psdir='${docdir}'
real_host_noncanonical=''
sbindir='${exec_prefix}/sbin'
set_have_cc_tls=''
set_use_emutls=''
sfp_machine_header=''
sharedstatedir='${prefix}/com'
slibdir='$(exec_prefix)/$(host_noncanonical)/lib'
solaris_ld_v2_maps=''
sysconfdir='${prefix}/etc'
target_alias='amdgcn-amdhsa'
target_noncanonical='amdgcn-amdhsa'
target_subdir='amdgcn-amdhsa'
thread_header=''
tm_defines=''
tm_file=''
tmake_file=''
toolexecdir='$(exec_prefix)/$(target_noncanonical)'
toolexeclibdir='$(toolexecdir)/lib'
unwind_header=''
use_tm_clone_registry=''
vis_hide=''
with_aix_soname='aix'

## ----------- ##
## confdefs.h. ##
## ----------- ##

/* confdefs.h */
#define PACKAGE_NAME "GNU C Runtime Library"
#define PACKAGE_TARNAME "libgcc"
#define PACKAGE_VERSION "1.0"
#define PACKAGE_STRING "GNU C Runtime Library 1.0"
#define PACKAGE_BUGREPORT ""
#define PACKAGE_URL "http://www.gnu.org/software/libgcc/"

configure: exit 1

---

### 评论 #11 — nolta (2021-07-07T14:20:34Z)

That's not the right file: you posted `build-offload/amdgcn-amdhsa/libgcc/config.log`, not `build-offload/amdgcn-amdhsa/gfx900/libgcc/config.log`. Note the `gfx900`.

---

### 评论 #12 — ROCmSupport (2021-07-07T14:37:18Z)

Hi @nolta 
There is no gfx900 folder path.
build-offload/amdgcn-amdhsa/libgcc/config.log only available in the path.

---

### 评论 #13 — nolta (2021-07-07T14:45:16Z)

Have you changed your setup? It apparently existed when you first tried on June 1:

```
configure: error: in /tmp/tmp.i7Ti5PFAyn/build-offload/amdgcn-amdhsa/gfx900/libgcc':
  configure: error: cannot compute suffix of object files: cannot compile See config.log' for more details
```

---

### 评论 #14 — ROCmSupport (2021-07-07T14:56:35Z)

True @nolta 
I changed the machine to Radeon7 as this is the available machine right now.

---

### 评论 #15 — ROCmSupport (2021-07-08T09:04:44Z)

Please let me know to move further.
Thank you.

---

### 评论 #16 — nolta (2021-07-08T13:15:57Z)

I don't know what's wrong with your current setup:

```
/tmp/tmp.e2lZV6kwY8/build-offload/./gcc/as: 106: exec: -triple=amdgcn--amdhsa: not found
```

Can you go back to your original setup?

---

### 评论 #17 — ROCmSupport (2021-07-16T06:57:51Z)

Sure Nolta, that old machine is not accessible. Let me try on a different machine and update you asap.
Thank you.

---

### 评论 #18 — ams-cs (2021-07-16T12:27:51Z)

Hi @nolta , GCC has not been tested with that version of LLVM. Please try again with LLVM9, as per the Wiki instructions. Newer versions had incompatible changes made.

We're working on supporting LLVM12+ in GCC 12, but for now the recommended version is LLVM9.

---

### 评论 #19 — ROCmSupport (2021-07-19T10:03:37Z)

Hi @nolta
Request to follow as per previous comment by @ams-cs and share an update.
Thank you.

---

### 评论 #20 — ams-cs (2021-07-20T10:43:07Z)

I have updated the GCC wiki to make the LLVM version requirements explicit.

I think LLVM 10 might work, but have not tested it extensively. LLVM 11 and 12 have known issues. The issues that are LLVM bugs have been fixed upstream and should be in the next LLVM release. The compatibility issues will be addressed in GCC 12.

---

### 评论 #21 — ROCmSupport (2021-11-16T10:16:44Z)

Hi @nolta 
Hope this issue is fixed with the latest ROCm 4.5 as LLVM 13 is part of ROCm 4.5.
Please verify and let me know. Thank you.

---

### 评论 #22 — ams-cs (2021-11-16T10:24:55Z)

LLVM 13 is not compatible with GCC 11.

The majority of the compatibility issues will be fixed in GCC 12, but there remains at least one known issue that may have to be fixed on the LLVM side; full compatibility may have to wait for LLVM 14 or maybe a 13.x point release.

Please continue to use LLVM 9 with GCC, for now.

---

### 评论 #23 — abhimeda (2024-01-22T22:45:22Z)

@nolta Hi, is this issue still persisting on the latest version of ROCm? If not can we close this ticket?

---

### 评论 #24 — ams-cs (2024-01-23T09:13:07Z)

As far as I know, the problem was resolved with GCC 12 and LLVM 13.0.1.

---

### 评论 #25 — nartmada (2024-04-19T21:15:49Z)

Closing the ticket.  @nolta, please reopen if you still see the issue in latest ROCm 6.1.0.  Thanks.

---
