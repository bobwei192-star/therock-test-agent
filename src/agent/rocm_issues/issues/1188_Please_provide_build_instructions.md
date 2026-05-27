# Please provide build instructions

> **Issue #1188**
> **状态**: closed
> **创建时间**: 2020-08-05T21:32:49Z
> **更新时间**: 2024-01-19T23:46:15Z
> **关闭时间**: 2024-01-19T23:46:15Z
> **作者**: rigtorp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1188

## 描述

There are no working build instructions for ROCm. The instructions in the individual README files are mostly wrong. Please provide working build instructions.

---

## 评论 (32 条)

### 评论 #1 — Djip007 (2020-08-05T23:01:44Z)

I use to have a look here: https://github.com/justxi/rocm
gentoo ebuild is prety nice for that... 

For fedora here are some commandes I use to make woking some time-ago (no garantie it work with last rocm...) but if I read correctly your other post you have succes this part ;)

```sh
#==================================================
#> ROCT-Thunk-Interface: (hsakmt-roct + hsakmt-roct-dev)
# - https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
#  == hsakmt-roct-1.0.9-245-gc0e4b8d-Linux.rpm
#  ++ hsakmt-roct-dev-1.0.9-245-gc0e4b8d-Linux.rpm

export ROC_VERSION=2.9.0
git clone https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface.git
#wget -O ROCT-Thunk-Interface-roc-${ROC_VERSION}.tar.gz https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/archive/roc-${ROC_VERSION}.tar.gz
#tar -xvf ROCT-Thunk-Interface-roc-${ROC_VERSION}.tar.gz; mv ROCT-Thunk-Interface-roc-${ROC_VERSION} ROCT-Thunk-Interface

cd ROCT-Thunk-Interface

#> pour compiler il y a qq pres-requi... (ou sont-ils defini?)
# - libpci
sudo dnf install pciutils-devel
# - numa.h 
sudo dnf install numactl-devel

# rm -rf build
mkdir -p build
cd build
#> par defaut dans /usr/local/...  avantage de mettre dans /opt/rocm menage facile!!!
#cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm ..
#echo /opt/rocm/lib64 | sudo tee /etc/ld.so.conf.d/hsa-roct-dev.conf
#sudo ldconfig
cmake ..

# make help
make
sudo make install

-- Install configuration: ""
-- Installing: /usr/local/lib64/libhsakmt.so.1.0.6
-- Installing: /usr/local/lib64/libhsakmt.so.1
-- Installing: /usr/local/lib64/libhsakmt.so
-- Installing: /usr/local/share/doc/hsakmt/LICENSE.md
# sudo rm -rf /usr/local/lib64/libhsakmt.*
# sudo rm -rf /usr/local/share/doc/hsakmt
# sudo rm -rf /opt/rocm/

#> devel... est-ce util?
make build-dev
sudo make install-dev

#==================================================
#> ROCR-Runtime/src
#- https://github.com/RadeonOpenCompute/ROCR-Runtime
#  == hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm
#  == hsa-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm

git clone https://github.com/RadeonOpenCompute/ROCR-Runtime.git
cd ROCR-Runtime/src/

#> compilation:
# rm -rf build
mkdir -p build
cd build
#> par defaut dans /usr/local/hsa/...  avantage de mettre dans /opt/rocm menage facile!!!
#echo /opt/rocm/lib     | sudo tee -a /etc/ld.so.conf.d/hsa-roct-dev.conf
#echo /opt/rocm/hsa/lib | sudo tee -a /etc/ld.so.conf.d/hsa-roct-dev.conf
#sudo ldconfig
cmake -DHSAKMT_INC_PATH:STRING=/opt/rocm/include -DHSAKMT_LIB_PATH:STRING=/opt/rocm/lib64 -DCMAKE_INSTALL_PREFIX=/opt/rocm ..

make
sudo make install

-- Install configuration: ""
-- Installing: /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9
-- Installing: /opt/rocm/hsa/lib/libhsa-runtime64.so.1
-- Installing: /opt/rocm/hsa/lib/libhsa-runtime64.so
-- Installing: /opt/rocm/hsa/include/hsa
-- Installing: /opt/rocm/hsa/include/hsa/amd_hsa_common.h
-- Installing: /opt/rocm/hsa/include/hsa/amd_hsa_kernel_code.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_ext_finalize.h
-- Installing: /opt/rocm/hsa/include/hsa/amd_hsa_elf.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa.h
-- Installing: /opt/rocm/hsa/include/hsa/Brig.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_ven_amd_loader.h
-- Installing: /opt/rocm/hsa/include/hsa/amd_hsa_signal.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_api_trace.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_ext_amd.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_ven_amd_aqlprofile.h
-- Installing: /opt/rocm/hsa/include/hsa/amd_hsa_queue.h
-- Installing: /opt/rocm/hsa/include/hsa/hsa_ext_image.h
-- Installing: /opt/rocm/include/hsa
-- Installing: /opt/rocm/lib/libhsa-runtime64.so

#==================================================
#> rocminfo
git clone https://github.com/RadeonOpenCompute/rocminfo.git
cd rocminfo

# rm -rf build
mkdir -p build
cd build
cmake -DROCM_DIR:STRING=/opt/rocm -DCMAKE_INSTALL_PREFIX=/opt/rocm ..
#cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH=/opt/rocm ..
make
#> a priorie c'est non opensources => install binaire seulement!
> LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
> LoadLib(libhsa-ext-image64.so.1) failed: libhsa-ext-image64.so.1: cannot open shared object file: No such file or directory
#> recupere les lib depuis: hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm

#> => install dans /opt/rocm/bin ou /usr/local/bin
sudo make install
```

---

### 评论 #2 — rigtorp (2020-08-06T02:39:42Z)

Instructions for the ridiculously complicated build: https://gist.github.com/rigtorp/d9483af100fb77cee57e4c9fa3c74245


---

### 评论 #3 — rigtorp (2020-08-24T20:36:53Z)

This repository provides build recipes for Arch Linux: https://github.com/rocm-arch/rocm-arch/
Looks like a good reference for how to build ROCm.

---

### 评论 #4 — Rmalavally (2020-08-24T20:46:53Z)

You may also refer to installation instructions for ArchLinux at:

https://community.amd.com/thread/253882

Note: The installation instructions for ArchLinux are contributed by users. AMD ROCm does not support Arch Linux currently  and there is no obligation to correct issues that are observed or occur.  Please submit any issues you encounter at the rocm-arch `issue tracker`_.

---

### 评论 #5 — rigtorp (2020-08-25T21:59:29Z)

@Rmalavally I'm asking for AMD to provide working build instructions for ROCm. The official documentation is mostly wrong.

---

### 评论 #6 — Rmalavally (2020-08-25T22:10:15Z)

Thank you for your feedback. Are you suggesting that the build instructions on http://rocmdocs.amd.com are incorrect? If you can specify the inaccuracies, it will be helpful. 

---

### 评论 #7 — rigtorp (2020-08-25T22:15:41Z)

There are no build instructions! Under the heading "Build AMD ROCm" (https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#build-amd-rocm) are instructions on how to install ROCm from binary packages. 

---

### 评论 #8 — Rmalavally (2020-08-25T22:55:40Z)

You are right. We are sorry that you were not able to find the information you needed to build AMD ROCm. We have noted your request for additional details and I will discuss it with my team. If you have further questions or comments, please let us know.


---

### 评论 #9 — rigtorp (2020-08-25T23:41:23Z)

I've created my own partial instructions here https://gist.github.com/rigtorp/d9483af100fb77cee57e4c9fa3c74245. But the fact that so many steps are required is also a problem.

---

### 评论 #10 — xuhuisheng (2020-08-26T00:37:59Z)

There is only docs for downloading source codes with repo. What is it next step we should to do? there are so many modules in ROCm. We really need a simple way to bulid them all,
I found a repo https://github.com/RadeonOpenCompute/Experimental_ROC/, it supports installation scripts for rocm-2.0, please upgrade it for latest version of rocm.

---

### 评论 #11 — baryluk (2020-09-26T21:13:44Z)

I wish there was a script in the ROCm main repo that at least goes into each directory in proper order for doing builds. It would be best if the ROCm and all libraries are built and installed in place, so entire stack can be tested without installing (or requiring root).

I don't even know in what order to start building components.

I tried HIP first, but it can't find HCC, and I don't know where it is either.

EDIT: After some digging, I noticed build ROCclr first, and put bunch of other defines, and it tries, but now it can't find hsa-runtime64. Eh.


---

### 评论 #12 — seesturm (2020-09-27T11:23:55Z)

I've created now [HIP build instructions for rocm-3.8.0 ](https://gist.github.com/seesturm/a830a59d834c51163aa84575d765595b) based on [How to build rocm 3.6.x beta from source ](https://gist.github.com/rigtorp/d9483af100fb77cee57e4c9fa3c74245). It is as "clean" as I could get it within a few hours. Shouldn't be too hard to fully script it.

Last step (Update dynamic linker config) is important in order for compiled HIP programs to find "hsa-runtime64".

---

### 评论 #13 — baryluk (2020-09-28T01:12:23Z)

@seesturm Testing now. You can add `--depth 1` to git clone, to reduce time of checkout and save network usage / disk space.

Also you can use `cmake --build .`, instead of `make`. This way if somebody default to using for example ninja, instead of make, it will work too.

I will publish a gist with my modifications.


---

### 评论 #14 — xuhuisheng (2020-09-28T02:36:25Z)

I uploaded my build scripts for rocm-3.8.0.
<https://github.com/xuhuisheng/rocm-build>

Definitely not perfect, Somebody who interested could have a look.


---

### 评论 #15 — baryluk (2020-09-28T03:32:17Z)

@xuhuisheng FYI. You don't need to download `repo` tool binary from google. It is available in Debian and Ubuntu normal repositories. Just `sudo apt install -y repo`, and then just use `repo`.




---

### 评论 #16 — xuhuisheng (2020-09-28T03:52:00Z)

@baryluk Weired, apt-get can find repo on ubuntu-18.04, but ubuntu-20.04 doesnot, while ubuntu-20.10 can find repo.

**update**: https://askubuntu.com/questions/1247103/why-is-the-repo-package-unavailable-in-ubuntu-20-04-how-can-i-install-it

---

### 评论 #17 — baryluk (2020-09-28T19:19:46Z)

@xuhuisheng Good to know.


---

### 评论 #18 — baryluk (2020-09-28T21:08:07Z)

So, I did manage to build few components (`llvm-project`/clang, `ROCT-Thunk-Interface`, `ROCm-Device-Libs`), but got issues when trying to build `ROCR-Runtime`. I am trying to compile all the pieces without installing them (so they can be tested independently from system install, and not require root, it should also make it easier to package without root or polluting the system).

Unfortunately I am getting:

```
+ rm -rf /home/user/rocm-build/ROCR-Runtime
+ CC=/home/user/rocm-build/llvm-project/bin/clang
+ generic_make ROCR-Runtime /src -DCMAKE_BUILD_TYPE=Release '-DCMAKE_PREFIX_PATH=/home/user/rocm-build/ROCT-Thunk-Interface;/home/user/rocm-build/ROCm-Device-Libs;/home/user/rocm-build/llvm-project' -DLLVM_DIR=/home/user/rocm-build/llvm-project -Dhsakmt_DIR=/home/user/rocm-build/ROCT-Thunk-Interface -DHSAKMT_BUILD_INC_PATH=/home/user/rocm-src/ROCT-Thunk-Interface/include -DHSAKMT_BUILD_LIB_PATH=/home/user/rocm-build/ROCT-Thunk-Interface
+ echo

+ echo

+ echo

+ NAME=ROCR-Runtime
+ shift
+ SUBDIR=/src
+ shift
+ mkdir -p /home/user/rocm-build/ROCR-Runtime
+ cd /home/user/rocm-build/ROCR-Runtime
+ SRC=/home/user/rocm-src/ROCR-Runtime
+ cmake -G Ninja -DCMAKE_INSTALL_PREFIX=/opt/rocm-git -DCMAKE_BUILD_TYPE=Release '-DCMAKE_PREFIX_PATH=/home/user/rocm-build/ROCT-Thunk-Interface;/home/user/rocm-build/ROCm-Device-Libs;/home/user/rocm-build/llvm-project' -DLLVM_DIR=/home/user/rocm-build/llvm-project -Dhsakmt_DIR=/home/user/rocm-build/ROCT-Thunk-Interface -DHSAKMT_BUILD_INC_PATH=/home/user/rocm-src/ROCT-Thunk-Interface/include -DHSAKMT_BUILD_LIB_PATH=/home/user/rocm-build/ROCT-Thunk-Interface /home/user/rocm-src/ROCR-Runtime/src
-- The C compiler identification is Clang 11.0.0
-- The CXX compiler identification is Clang 11.0.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /home/user/rocm-build/llvm-project/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /home/user/rocm-build/llvm-project/bin/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
fatal: Not a valid object name origin/HEAD
-- Found LibElf: /usr/lib/x86_64-linux-gnu/libelf.so  
-- Performing Test ELF_GETSHDRSTRNDX
-- Performing Test ELF_GETSHDRSTRNDX - Success
CMake Error at /home/user/rocm-build/ROCT-Thunk-Interface/hsakmt-config.cmake:37 (include):
  include could not find load file:

    /home/user/rocm-build/ROCT-Thunk-Interface/hsakmtTargets.cmake
Call Stack (most recent call first):
  CMakeLists.txt:109 (find_package)


-- Looking for __NR_memfd_create
-- Looking for __NR_memfd_create - found
CMake Warning at cmake_modules/utils.cmake:68 (message):
  BITCODE_DIR not located during path search.
Call Stack (most recent call first):
  cmake_modules/utils.cmake:86 (get_path)
  image/blit_src/CMakeLists.txt:53 (get_include_path)


CMake Error at image/blit_src/CMakeLists.txt:85 (message):
  Configuration halted.


-- Configuring incomplete, errors occurred!
See also "/home/user/rocm-build/ROCR-Runtime/CMakeFiles/CMakeOutput.log".
```

I don't understand `cmake` enough to know how to fix it.

`/home/user/rocm-build/ROCT-Thunk-Interface/hsakmt-config.cmake:37` tries to include `/home/user/rocm-build/ROCT-Thunk-Interface/hsakmtTargets.cmake`, but this files is instead in `/home/user/rocm-build/ROCT-Thunk-Interface/CMakeFiles/Export/lib/cmake/hsakmt/hsakmtTargets.cmake` 

---

### 评论 #19 — xuhuisheng (2020-09-28T23:33:05Z)

I suggest to install ROCm modules one by one to /opt/rocm/. I had add `ninja package` and `sudo dpkg -i *.deb` in build scripts.
ROCm used cmake to find the dependencies, default path is /opt/rocm/. The dependencies may be includes, libs, even binaries. It also provide a series of cmake scripts named rocm-cmake, to help modules export <module>-config.cmake to let other modules depends.

---

### 评论 #20 — baryluk (2020-09-29T00:46:31Z)

@xuhuisheng I know that would probably work. But I want to avoid install. I want to build all components without doing install, messing existing (working) rocm install, or requiring root.

---

### 评论 #21 — xuhuisheng (2020-09-29T02:22:17Z)

@baryluk Some weeks earlier, I try to install these modules to a custom path like /opt/rocm-custom, and then find It is will cost too much time to find the related config. So I gave up eventually.
Guess the CMAKE_PREFIX_PATH will give a chance to let cmake find related modules from custom path. But donot know where is *-config.cmake and *-target.cmake come from. Now I used docker to prepare clean environment, and store the deb package for next usage.
Maybe we could just package deb and install them to a custom path, which doesnot need root privilleges?

---

### 评论 #22 — baryluk (2020-10-04T08:02:12Z)

Workarounds are easy sure. Trivial almost. I want to find a proper way to do it. I am not cmake expert, and I am probably missing some `cmake` flag or a fix to `CMakeList.txt`.

---

### 评论 #23 — ROCmSupport (2020-11-23T11:50:19Z)

Hi @rigtorp and All,
We are working on this and will provide an update asap.
Thank you.

---

### 评论 #24 — baryluk (2021-01-07T08:33:22Z)

I think this is a critical issue. It is really hard to contribute patches to ROCm, without being able to quickly compile and test the changes, i.e. in the compiler, and other libraries. Even just debugging in gdb, is hard because of that. It also makes harder for distributions to ship pre-packaged ROCm, for easy install and use. Yes, it can be done, but at a lot of pain and re-discovery / hacking needed by everybody trying to attempt it. Me, despite knowing a lot about building things from source, still failed building ROCm to be usable.
 

---

### 评论 #25 — ROCmSupport (2021-01-07T09:08:34Z)

Thanks @baryluk for more information. Yes, this definitely needs lot of work. Hence we need more time to stabilize the things.
We started working on this and will share progress asap.
Thank you.


---

### 评论 #26 — ROCmSupport (2021-02-01T07:18:41Z)

Just an update on this:
We are working on this and it might take more time than expected.
Please stay tuned for updates and we will try to provide proper build instructions as soon as possible.
Thanks for understanding.

---

### 评论 #27 — flowpoint (2021-07-03T14:29:08Z)

> So, I did manage to build few components (`llvm-project`/clang, `ROCT-Thunk-Interface`, `ROCm-Device-Libs`), but got issues when trying to build `ROCR-Runtime`. I am trying to compile all the pieces without installing them (so they can be tested independently from system install, and not require root, it should also make it easier to package without root or polluting the system).
> 
> Unfortunately I am getting:
> 
> ```
> + rm -rf /home/user/rocm-build/ROCR-Runtime
> + CC=/home/user/rocm-build/llvm-project/bin/clang
> + generic_make ROCR-Runtime /src -DCMAKE_BUILD_TYPE=Release '-DCMAKE_PREFIX_PATH=/home/user/rocm-build/ROCT-Thunk-Interface;/home/user/rocm-build/ROCm-Device-Libs;/home/user/rocm-build/llvm-project' -DLLVM_DIR=/home/user/rocm-build/llvm-project -Dhsakmt_DIR=/home/user/rocm-build/ROCT-Thunk-Interface -DHSAKMT_BUILD_INC_PATH=/home/user/rocm-src/ROCT-Thunk-Interface/include -DHSAKMT_BUILD_LIB_PATH=/home/user/rocm-build/ROCT-Thunk-Interface
> + echo
> 
> + echo
> 
> + echo
> 
> + NAME=ROCR-Runtime
> + shift
> + SUBDIR=/src
> + shift
> + mkdir -p /home/user/rocm-build/ROCR-Runtime
> + cd /home/user/rocm-build/ROCR-Runtime
> + SRC=/home/user/rocm-src/ROCR-Runtime
> + cmake -G Ninja -DCMAKE_INSTALL_PREFIX=/opt/rocm-git -DCMAKE_BUILD_TYPE=Release '-DCMAKE_PREFIX_PATH=/home/user/rocm-build/ROCT-Thunk-Interface;/home/user/rocm-build/ROCm-Device-Libs;/home/user/rocm-build/llvm-project' -DLLVM_DIR=/home/user/rocm-build/llvm-project -Dhsakmt_DIR=/home/user/rocm-build/ROCT-Thunk-Interface -DHSAKMT_BUILD_INC_PATH=/home/user/rocm-src/ROCT-Thunk-Interface/include -DHSAKMT_BUILD_LIB_PATH=/home/user/rocm-build/ROCT-Thunk-Interface /home/user/rocm-src/ROCR-Runtime/src
> -- The C compiler identification is Clang 11.0.0
> -- The CXX compiler identification is Clang 11.0.0
> -- Detecting C compiler ABI info
> -- Detecting C compiler ABI info - done
> -- Check for working C compiler: /home/user/rocm-build/llvm-project/bin/clang - skipped
> -- Detecting C compile features
> -- Detecting C compile features - done
> -- Detecting CXX compiler ABI info
> -- Detecting CXX compiler ABI info - done
> -- Check for working CXX compiler: /home/user/rocm-build/llvm-project/bin/clang++ - skipped
> -- Detecting CXX compile features
> -- Detecting CXX compile features - done
> fatal: Not a valid object name origin/HEAD
> -- Found LibElf: /usr/lib/x86_64-linux-gnu/libelf.so  
> -- Performing Test ELF_GETSHDRSTRNDX
> -- Performing Test ELF_GETSHDRSTRNDX - Success
> CMake Error at /home/user/rocm-build/ROCT-Thunk-Interface/hsakmt-config.cmake:37 (include):
>   include could not find load file:
> 
>     /home/user/rocm-build/ROCT-Thunk-Interface/hsakmtTargets.cmake
> Call Stack (most recent call first):
>   CMakeLists.txt:109 (find_package)
> 
> 
> -- Looking for __NR_memfd_create
> -- Looking for __NR_memfd_create - found
> CMake Warning at cmake_modules/utils.cmake:68 (message):
>   BITCODE_DIR not located during path search.
> Call Stack (most recent call first):
>   cmake_modules/utils.cmake:86 (get_path)
>   image/blit_src/CMakeLists.txt:53 (get_include_path)
> 
> 
> CMake Error at image/blit_src/CMakeLists.txt:85 (message):
>   Configuration halted.
> 
> 
> -- Configuring incomplete, errors occurred!
> See also "/home/user/rocm-build/ROCR-Runtime/CMakeFiles/CMakeOutput.log".
> ```
> 
> I don't understand `cmake` enough to know how to fix it.
> 
> `/home/user/rocm-build/ROCT-Thunk-Interface/hsakmt-config.cmake:37` tries to include `/home/user/rocm-build/ROCT-Thunk-Interface/hsakmtTargets.cmake`, but this files is instead in `/home/user/rocm-build/ROCT-Thunk-Interface/CMakeFiles/Export/lib/cmake/hsakmt/hsakmtTargets.cmake`

if you or anyone is still hitting this, like me, the solution seems to be setting
cmake ... -DBITCODE_DIR=path_to_rocm/ROCm/ROCm-Device-Libs/build/dist/amdgcn/bitcode ...

---

### 评论 #28 — keryell (2022-04-05T16:15:06Z)

@ROCmSupport any news on this? This issue is almost 2 year old.
Probably a good start is to read the current documentation and fix the typos, the broken links... before diving into the core details.
For example half of the links in https://docs.amd.com/category/compilers_and_tools are broken.

---

### 评论 #29 — Rmalavally (2022-04-05T16:28:10Z)

Thank you for your feedback. Please ensure you refresh the browser when you access the documentation portal at https://docs.amd.com.
 
The documentation links for Compilers and Tools work well for us. Let us know if you continue to experience issues with accessing the content. 

AMD ROCm Documentation Team


---

### 评论 #30 — keryell (2022-04-05T16:42:06Z)

> Thank you for your feedback. Please ensure you refresh the browser when you access the documentation portal at https://docs.amd.com.

Actually this works. Strange.
But remains the core of this issue: providing a recipe to build everything from scratch, since this is supposed to be good open-source code.
Thanks.

---

### 评论 #31 — Rmalavally (2022-04-05T16:50:50Z)

Glad to know the links work, and we are glad we could be of assistance to you. 

I agree with your suggestion to make the build instructions publicly available. We are actively working with the internal teams to understand the scope and the nature of this effort. Please continue to send your recommendations and observations for ROCm documentation. 

AMD ROCm Documentation Team

---

### 评论 #32 — nartmada (2024-01-19T20:23:56Z)

Hi @rigtorp, please close this ticket if it is no longer needed.  Thank you.

---
