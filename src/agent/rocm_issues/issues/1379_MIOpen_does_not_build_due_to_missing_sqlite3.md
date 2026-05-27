# MIOpen does not build due to missing sqlite3

> **Issue #1379**
> **状态**: closed
> **创建时间**: 2021-02-11T22:28:09Z
> **更新时间**: 2021-05-31T11:16:23Z
> **关闭时间**: 2021-05-31T11:16:23Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1379

## 描述

Even after sqlite3 installed, it is not building. It not clear what particular sqlite3 it is asking for.

apt install sqlite3

Reading package lists... 0%

Reading package lists... 100%

Reading package lists... Done


Building dependency tree... 0%

Building dependency tree... 0%

Building dependency tree... 50%

Building dependency tree... 50%

Building dependency tree       


Reading state information... 0%

Reading state information... 0%

Reading state information... Done

The following package was automatically installed and is no longer required:
  libfprint-2-tod1
Use 'sudo apt autoremove' to remove it.
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  sqlite3
0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.
Need to get 860 kB of archives.
After this operation, 2,803 kB of additional disk space will be used.

0% [Working]
            
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 sqlite3 amd64 3.31.1-4ubuntu0.2 [860 kB]

1% [1 sqlite3 14.2 kB/860 kB 2%]
                                
100% [Working]
              
Fetched 860 kB in 1s (1,255 kB/s)

Selecting previously unselected package sqlite3.
(Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 271130 files and directories currently installed.)
Preparing to unpack .../sqlite3_3.31.1-4ubuntu0.2_amd64.deb ...
Progress: [  0%] [.............................................................................................................................] Progress: [ 20%] [#########################....................................................................................................] Unpacking sqlite3 (3.31.1-4ubuntu0.2) ...
Progress: [ 40%] [##################################################...........................................................................] Setting up sqlite3 (3.31.1-4ubuntu0.2) ...
Progress: [ 60%] [###########################################################################..................................................] Progress: [ 80%] [####################################################################################################.........................] Processing triggers for man-db (2.9.1-1) ...

:~/ROCm/MIOpen/build# sudo apt install sqlite3apt-cache search sqlitesearchsqlitecmake -DMIOPEN_BACKEND=OpenCL ..
-- Checking for module 'sqlite3'
--   No package 'sqlite3' found
CMake Error at /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:463 (message):
  A required package was not found
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:643 (_pkg_check_modules_internal)
  CMakeLists.txt:60 (pkg_check_modules)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm/MIOpen/build/CMakeFiles/CMakeOutput.log".
:~/ROCm/MIOpen/build# sqlite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> quit()
   ...> ^C^C^Croot@guyen-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# dpkg -l | grep sqlite3
ii  libsqlite3-0:amd64                         3.31.1-4ubuntu0.2                            amd64        SQLite 3 shared library
ii  sqlite3                                    3.31.1-4ubuntu0.2                            amd64        Command line interface for SQLite 3


:~/ROCm/MIOpen/build# cmake -DMIOPEN_BACKEND=OpenCL ..
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'sqlite3'
--   No package 'sqlite3' found
CMake Error at /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:463 (message):
  A required package was not found
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:643 (_pkg_check_modules_internal)
  CMakeLists.txt:60 (pkg_check_modules)


-- Configuring incomplete, errors occurred!




---

## 评论 (17 条)

### 评论 #1 — ROCmSupport (2021-02-12T04:51:29Z)

Thanks @gggh000 for reaching us.
I will check this for you and share an update asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-02-12T05:20:23Z)

Hi @gggh000 
Can you please install **libsqlite3-dev** and update the status.
I tried locally and its working perfect in my case. I will make sure that MIOpen documentation is updated with this information.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-02-12T07:50:24Z)

Hi @gggh000 
Got an update for you.
Raised an internal ticket to MIOpen for doc changes accordingly.
Thank you.

---

### 评论 #4 — gggh000 (2021-02-12T08:29:02Z)

It worked, now it is  getting another error:

root@johndoe-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen# apt install libsqlite3-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  libfprint-2-tod1
Use 'apt autoremove' to remove it.
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  libsqlite3-dev
0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.
Need to get 696 kB of archives.
After this operation, 2,372 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 libsqlite3-dev amd64 3.31.1-4ubuntu0.2 [696 kB]
Fetched 696 kB in 1s (1,067 kB/s)
Selecting previously unselected package libsqlite3-dev:amd64.
(Reading database ... 271137 files and directories currently installed.)
Preparing to unpack .../libsqlite3-dev_3.31.1-4ubuntu0.2_amd64.deb ...
Unpacking libsqlite3-dev:amd64 (3.31.1-4ubuntu0.2) ...
Setting up libsqlite3-dev:amd64 (3.31.1-4ubuntu0.2) ...
root@johndoe-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen# cmake -DMIOPEN_BACKEND=OpenCL ..
CMake Error: The source directory "/root/ROCm" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
root@johndoe-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen# cd build/
root@johndoe-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# cmake -DMIOPEN_BACKEND=OpenCL ..
-- Checking for module 'sqlite3'
--   Found sqlite3, version 3.31.1
-- Could NOT find BZip2 (missing: BZIP2_LIBRARIES BZIP2_INCLUDE_DIR)
-- Performing Test HAS_HIP
-- Performing Test HAS_HIP - Failed
-- Found OPENCL: /opt/rocm/lib/libOpenCL.so
hip compiler: /opt/rocm/llvm/bin/clang++
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Build with HIP 4.0.20496
-- Hip compiler flags:  -xhip    -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/../include -isystem /opt/rocm/llvm/lib/clang/12.0.0/include/..  -D__HIP_PLATFORM_HCC__=1  -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/include -isystem /opt/rocm/include -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64 --hip-link    -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64
-- OpenCL backend selected.
-- clang-offload-bundler found: /opt/rocm/llvm/bin/clang-offload-bundler
-- AMDGCN assembler: /opt/rocm/llvm/bin/clang
-- Could NOT find miopengemm (missing: miopengemm_DIR)
-- Build without miopengemm
-- Found Boost: /usr/lib/x86_64-linux-gnu/cmake/Boost-1.71.0/BoostConfig.cmake (found version "1.71.0") found components: filesystem
-- Clang tidy found: 12.0.0git
-- Clang tidy checks: *,-abseil-string-find-startswith,-android-cloexec-fopen,-cert-msc30-c,-bugprone-exception-escape,-cert-env33-c,-cert-msc32-c,-cert-msc50-cpp,-cert-msc51-cpp,-clang-analyzer-alpha.core.CastToStruct,-clang-analyzer-optin.performance.Padding,-clang-diagnostic-deprecated-declarations,-clang-diagnostic-extern-c-compat,-clang-diagnostic-unused-command-line-argument,-cppcoreguidelines-avoid-c-arrays,-cppcoreguidelines-avoid-magic-numbers,-cppcoreguidelines-explicit-virtual-functions,-cppcoreguidelines-init-variables,-cppcoreguidelines-macro-usage,-cppcoreguidelines-non-private-member-variables-in-classes,-cppcoreguidelines-pro-bounds-array-to-pointer-decay,-cppcoreguidelines-pro-bounds-constant-array-index,-cppcoreguidelines-pro-bounds-pointer-arithmetic,-cppcoreguidelines-pro-type-member-init,-cppcoreguidelines-pro-type-reinterpret-cast,-cppcoreguidelines-pro-type-union-access,-cppcoreguidelines-pro-type-vararg,-cppcoreguidelines-special-member-functions,-fuchsia-*,-google-explicit-constructor,-google-readability-braces-around-statements,-google-readability-todo,-google-runtime-int,-google-runtime-references,-hicpp-braces-around-statements,-hicpp-explicit-conversions,-hicpp-no-array-decay,-hicpp-avoid-c-arrays,-hicpp-signed-bitwise,-hicpp-special-member-functions,-hicpp-uppercase-literal-suffix,-hicpp-use-auto,-hicpp-use-equals-default,-hicpp-use-override,-llvm-header-guard,-llvm-include-order,-misc-misplaced-const,-misc-non-private-member-variables-in-classes,-modernize-avoid-bind,-modernize-avoid-c-arrays,-modernize-pass-by-value,-modernize-use-auto,-modernize-use-default-member-init,-modernize-use-equals-default,-modernize-use-trailing-return-type,-modernize-use-transparent-functors,-performance-unnecessary-value-param,-readability-braces-around-statements,-readability-else-after-return,-readability-isolate-declaration,-readability-magic-numbers,-readability-named-parameter,-readability-uppercase-literal-suffix,-readability-convert-member-functions-to-static
-- Could NOT find LATEX (missing: LATEX_COMPILER)
Latex builder not found. Latex builder is required only for building the PDF documentation for MIOpen and is not necessary for building the library, or any other components. To build PDF documentation run make in /root/ROCm/MIOpen/doc/pdf, once a latex builder is installed.
-- MIOpen_VERSION= 2.9.0.8252-64506314
-- CMAKE_BUILD_TYPE= Release
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- MIOpen linking OpenCL: /usr/local/include
-- Librt: /usr/lib/x86_64-linux-gnu/librt.so
-- Performing Test MIOPEN_HAS_address
-- Performing Test MIOPEN_HAS_address - Failed
-- Performing Test MIOPEN_HAS_thread
-- Performing Test MIOPEN_HAS_thread - Failed
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
/root/ROCm/MIOpen/src/BZIP2_INCLUDE_DIR
   used as include directory in directory /root/ROCm/MIOpen/src
BZIP2_LIBRARY
    linked by target "MIOpen" in directory /root/ROCm/MIOpen/src

-- Configuring incomplete, errors occurred!
See also "/root/ROCm/MIOpen/build/CMakeFiles/CMakeOutput.log".
See also "/root/ROCm/MIOpen/build/CMakeFiles/CMakeError.log".


---

### 评论 #5 — gggh000 (2021-02-12T08:34:01Z)

[cmakeOutput.log](https://github.com/RadeonOpenCompute/ROCm/files/5970504/cmakeOutput.log)
[CMakeError.log](https://github.com/RadeonOpenCompute/ROCm/files/5970505/CMakeError.log)


---

### 评论 #6 — ROCmSupport (2021-02-12T08:44:01Z)

Hi @gggh000 
miopengemm is missing.
miopengemm is a dependency for MIOpen. Please install it by _sudo apt install miopengemm_ and try again.
Thank you.

---

### 评论 #7 — gggh000 (2021-02-12T18:49:58Z)

i installed it is not working. It also seem complained about add'l apps which when insatlled, still not building

  468  apt install miopengemm -y
  476  apt install texlive-full =y
  477  apt install texlive-full -y
  478  apt install texmaker -y
root@johndoe-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# apt install -y libzip5
Reading package lists... Done
Building dependency tree
Reading state information... Done
libzip5 is already the newest version (1.5.1-0ubuntu1).
libzip5 set to manually installed.
The following package was automatically installed and is no longer required:
  libfprint-2-tod1
Use 'apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 8 not upgraded.
root@guyen-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# cmake -DMIOPEN_BACKEND=OpenCL ..
-- Could NOT find BZip2 (missing: BZIP2_LIBRARIES BZIP2_INCLUDE_DIR)
hip compiler: /opt/rocm/llvm/bin/clang++
-- Build with HIP 4.0.20496
-- Hip compiler flags:  -xhip    -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/../include -isystem /opt/rocm/llvm/lib/clang/12.0.0/include/..  -D__HIP_PLATFORM_HCC__=1  -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/include -isystem /opt/rocm/include -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64 --hip-link    -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64
-- OpenCL backend selected.
-- clang-offload-bundler found: /opt/rocm/llvm/bin/clang-offload-bundler
-- AMDGCN assembler: /opt/rocm/llvm/bin/clang
-- Build with miopengemm
-- Clang tidy found: 12.0.0git
-- Clang tidy checks: *,-abseil-string-find-startswith,-android-cloexec-fopen,-cert-msc30-c,-bugprone-exception-escape,-cert-env33-c,-cert-msc32-c,-cert-msc50-cpp,-cert-msc51-cpp,-clang-analyzer-alpha.core.CastToStruct,-clang-analyzer-optin.performance.Padding,-clang-diagnostic-deprecated-declarations,-clang-diagnostic-extern-c-compat,-clang-diagnostic-unused-command-line-argument,-cppcoreguidelines-avoid-c-arrays,-cppcoreguidelines-avoid-magic-numbers,-cppcoreguidelines-explicit-virtual-functions,-cppcoreguidelines-init-variables,-cppcoreguidelines-macro-usage,-cppcoreguidelines-non-private-member-variables-in-classes,-cppcoreguidelines-pro-bounds-array-to-pointer-decay,-cppcoreguidelines-pro-bounds-constant-array-index,-cppcoreguidelines-pro-bounds-pointer-arithmetic,-cppcoreguidelines-pro-type-member-init,-cppcoreguidelines-pro-type-reinterpret-cast,-cppcoreguidelines-pro-type-union-access,-cppcoreguidelines-pro-type-vararg,-cppcoreguidelines-special-member-functions,-fuchsia-*,-google-explicit-constructor,-google-readability-braces-around-statements,-google-readability-todo,-google-runtime-int,-google-runtime-references,-hicpp-braces-around-statements,-hicpp-explicit-conversions,-hicpp-no-array-decay,-hicpp-avoid-c-arrays,-hicpp-signed-bitwise,-hicpp-special-member-functions,-hicpp-uppercase-literal-suffix,-hicpp-use-auto,-hicpp-use-equals-default,-hicpp-use-override,-llvm-header-guard,-llvm-include-order,-misc-misplaced-const,-misc-non-private-member-variables-in-classes,-modernize-avoid-bind,-modernize-avoid-c-arrays,-modernize-pass-by-value,-modernize-use-auto,-modernize-use-default-member-init,-modernize-use-equals-default,-modernize-use-trailing-return-type,-modernize-use-transparent-functors,-performance-unnecessary-value-param,-readability-braces-around-statements,-readability-else-after-return,-readability-isolate-declaration,-readability-magic-numbers,-readability-named-parameter,-readability-uppercase-literal-suffix,-readability-convert-member-functions-to-static
-- MIOpen_VERSION= 2.9.0.8252-64506314
-- CMAKE_BUILD_TYPE= Release
-- MIOpen linking OpenCL: /usr/local/include
-- Librt: /usr/lib/x86_64-linux-gnu/librt.so
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
/root/ROCm/MIOpen/src/BZIP2_INCLUDE_DIR
   used as include directory in directory /root/ROCm/MIOpen/src
BZIP2_LIBRARY
    linked by target "MIOpen" in directory /root/ROCm/MIOpen/src

-- Configuring incomplete, errors occurred!


---

### 评论 #8 — gggh000 (2021-02-12T18:53:07Z)

You are saying you tried locally and working perfect. Are you doing this on a preconfigured system? Then you are not going to see what customer who is fresh onto building afresh seeing. This is not going to solve the problem. I am kind of surprised on this. 

---

### 评论 #9 — Moading (2021-02-13T08:51:13Z)

Howdy,
your log says "Could NOT find BZip2". I guess you have to install libbz2-dev and you will be fine:
sudo apt install libbz2-dev
Greetings!

---

### 评论 #10 — ROCmSupport (2021-02-15T04:54:23Z)

Hi @gggh000 
Can you please install bzip2 as libbz2 and update please.
Thank you.

---

### 评论 #11 — gggh000 (2021-03-12T05:03:11Z)

I installed libbz2-dev and error disappeared. Now I see following error. pls REmember it is fresh Ubuntu 20.04 installation

root@Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# cmake -DMIOPEN_BACKEND=OpenCL ..
hip compiler: /opt/rocm/llvm/bin/clang++
-- Build with HIP 4.0.20496
-- Hip compiler flags:  -xhip    -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/../include -isystem /opt/rocm/llvm/lib/clang/12.0.0/include/..  -D__HIP_PLATFORM_HCC__=1  -D__HIP_ROCclr__=1 -isystem /opt/rocm-4.0.0/hip/include -isystem /opt/rocm/include -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64 --hip-link    -L/opt/rocm/llvm/lib/clang/12.0.0/include/../lib/linux -lclang_rt.builtins-x86_64
-- OpenCL backend selected.
-- clang-offload-bundler found: /opt/rocm/llvm/bin/clang-offload-bundler
-- AMDGCN assembler: /opt/rocm/llvm/bin/clang
-- Build with miopengemm
-- Clang tidy found: 12.0.0git
-- Clang tidy checks: *,-abseil-string-find-startswith,-android-cloexec-fopen,-cert-msc30-c,-bugprone-exception-escape,-cert-env33-c,-cert-msc32-c,-cert-msc50-cpp,-cert-msc51-cpp,-clang-analyzer-alpha.core.CastToStruct,-clang-analyzer-optin.performance.Padding,-clang-diagnostic-deprecated-declarations,-clang-diagnostic-extern-c-compat,-clang-diagnostic-unused-command-line-argument,-cppcoreguidelines-avoid-c-arrays,-cppcoreguidelines-avoid-magic-numbers,-cppcoreguidelines-explicit-virtual-functions,-cppcoreguidelines-init-variables,-cppcoreguidelines-macro-usage,-cppcoreguidelines-non-private-member-variables-in-classes,-cppcoreguidelines-pro-bounds-array-to-pointer-decay,-cppcoreguidelines-pro-bounds-constant-array-index,-cppcoreguidelines-pro-bounds-pointer-arithmetic,-cppcoreguidelines-pro-type-member-init,-cppcoreguidelines-pro-type-reinterpret-cast,-cppcoreguidelines-pro-type-union-access,-cppcoreguidelines-pro-type-vararg,-cppcoreguidelines-special-member-functions,-fuchsia-*,-google-explicit-constructor,-google-readability-braces-around-statements,-google-readability-todo,-google-runtime-int,-google-runtime-references,-hicpp-braces-around-statements,-hicpp-explicit-conversions,-hicpp-no-array-decay,-hicpp-avoid-c-arrays,-hicpp-signed-bitwise,-hicpp-special-member-functions,-hicpp-uppercase-literal-suffix,-hicpp-use-auto,-hicpp-use-equals-default,-hicpp-use-override,-llvm-header-guard,-llvm-include-order,-misc-misplaced-const,-misc-non-private-member-variables-in-classes,-modernize-avoid-bind,-modernize-avoid-c-arrays,-modernize-pass-by-value,-modernize-use-auto,-modernize-use-default-member-init,-modernize-use-equals-default,-modernize-use-trailing-return-type,-modernize-use-transparent-functors,-performance-unnecessary-value-param,-readability-braces-around-statements,-readability-else-after-return,-readability-isolate-declaration,-readability-magic-numbers,-readability-named-parameter,-readability-uppercase-literal-suffix,-readability-convert-member-functions-to-static
-- MIOpen_VERSION= 2.9.0.8252-64506314
-- CMAKE_BUILD_TYPE= Release

-- MIOpen linking OpenCL: /usr/local/include
-- Librt: /usr/lib/x86_64-linux-gnu/librt.so
-- Configuring done
CMake Error in src/CMakeLists.txt:
  Found relative path while evaluating include directories of "MIOpen":

    "HALF_INCLUDE_DIR-NOTFOUND"



CMake Error in src/CMakeLists.txt:
  Found relative path while evaluating include directories of "MIOpen":

    "HALF_INCLUDE_DIR-NOTFOUND"



CMake Error in driver/CMakeLists.txt:
  Target "MIOpen" contains relative path in its
  INTERFACE_INCLUDE_DIRECTORIES:

    "HALF_INCLUDE_DIR-NOTFOUND"




---

### 评论 #12 — ROCmSupport (2021-03-12T05:52:43Z)

"apt install half" solves the problem.

---

### 评论 #13 — gggh000 (2021-03-23T07:53:01Z)

I re-tested today and built fine, however prerequisites in the readme remains obscure. 

---

### 评论 #14 — ROCmSupport (2021-03-23T08:24:32Z)

Thanks @gggh000 for confirming that issue is gone.
Prerequisites for MIOpen: [https://github.com/ROCmSoftwarePlatform/MIOpen#prerequisites](url)
I am working with MIOpen team on this via internal ticket, docs will be updated very soon.
Thank you.

---

### 评论 #15 — ROCmSupport (2021-03-23T08:25:51Z)

Sorry for the closure.
I will close this ticket once the docs are updated. I will keep you posted.
Thank you.

---

### 评论 #16 — gggh000 (2021-05-17T22:29:06Z)

I think this can be closed once doc is updated. For now, I am maintaining personal prereq list.

---

### 评论 #17 — ROCmSupport (2021-05-31T11:16:23Z)

Hi @gggh000 
Docs updated now. You can check the latest docs at @ https://github.com/ROCmSoftwarePlatform/MIOpen
Thank you.

---
