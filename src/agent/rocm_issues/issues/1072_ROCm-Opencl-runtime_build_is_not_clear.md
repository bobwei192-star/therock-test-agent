# ROCm-Opencl-runtime build is not clear.

> **Issue #1072**
> **状态**: closed
> **创建时间**: 2020-04-04T09:11:25Z
> **更新时间**: 2021-04-05T10:07:43Z
> **关闭时间**: 2021-04-05T10:07:43Z
> **作者**: gggh900
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1072

## 描述

The README.txt contains instruction to use cmake with several flags:
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=<path-to-llvm-include> -DCMAKE_PREFIX_PATH=<path-to-amd_comgr> -DUSE_COMGR_LIBRARY=yes .

It is not clear what path to use for DLLVM_INCLUDES and DCMAKE_PREFIX_PATH as Rocm source seem to have many copies of same:
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name llvm | grep include
../../aomp/llvm-project/llvm/utils/gn/secondary/llvm/include/llvm
../../aomp/llvm-project/llvm/include/llvm
../../hcc/build/llvm-project/llvm/include/llvm
../../hcc/llvm-project/llvm/utils/gn/secondary/llvm/include/llvm
../../hcc/llvm-project/llvm/include/llvm
../../llvm_amd-stg-open/llvm/utils/gn/secondary/llvm/include/llvm
../../llvm_amd-stg-open/llvm/include/llvm
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name comgr
../../ROCm-CompilerSupport/lib/comgr
../../aomp/rocm-compilersupport/lib/comgr


Tried with same of the path but always ended with missing cmake files:
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=../../hcc/build/llvm-project/llvm/include -DCMAKE_PREFIX_PATH=../../ROCm-CompilerSupport/lib/comgr -DUSE_COMGR_LIBRARY=yes ..
    amd_comgrConfig.cmake
    amd_comgr-config.cmake

Full log:

root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=../../hcc/build/llvm-project/llvm/include -DCMAKE_PREFIX_PATH=../../ROCm-CompilerSupport/lib/comgr -DUSE_COMGR_LIBRARY=yes ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
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
-- Found ROCT: /opt/rocm/include
-- Found ROCR: /opt/rocm/include/hsa
CMake Error at api/opencl/amdocl/CMakeLists.txt:32 (find_package):
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:

    amd_comgrConfig.cmake
    amd_comgr-config.cmake

  Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
  "amd_comgr_DIR" to a directory containing one of the above files.  If
  "amd_comgr" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
See also "/root/ROCm/ROCm-OpenCL-Runtime/build/CMakeFiles/CMakeOutput.log".
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name amd_comgrConfig.cmake
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name amd_comgr-config.cmake
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build#



---

## 评论 (17 条)

### 评论 #1 — tonysy (2020-06-10T19:27:56Z)

same problem 

---

### 评论 #2 — Randrianasulu (2020-10-04T21:25:50Z)

Try instructions from PKGBUILD script in Arach?

https://github.com/rocm-arch/rocm-arch/blob/master/comgr/PKGBUILD
```
wget https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/archive/rocm-3.8.0.tar.gz
tar -xf rocm-3.8.0.tar.gz
cd ROCm-CompilerSupport-rocm-3.8.0/ 
 cmake -B build -Wno-dev -DCMAKE_INSTALL_PREFIX=/opt/rocm  -DCMAKE_PREFIX_PATH="/opt/rocm/llvm;/opt/rocm"  "lib/comgr"  
 make -C build 
```

for me it fails with error, but probably due to llvm 10 ?

```
 cmake -B build -Wno-dev -DCMAKE_INSTALL_PREFIX=/opt/rocm  -DCMAKE_PREFIX_PATH="/opt/rocm/llvm;/opt/rocm"  "lib/comgr"
-- The C compiler identification is Clang 10.0.1
-- The CXX compiler identification is Clang 10.0.1
-- Check for working C compiler: /usr/bin/clang
-- Check for working C compiler: /usr/bin/clang - works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/clang++
-- Check for working CXX compiler: /usr/bin/clang++ - works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Could NOT find ROCM (missing: ROCM_DIR)
CMake Warning at CMakeLists.txt:26 (find_package):
  By not providing "FindAMDDeviceLibs.cmake" in CMAKE_MODULE_PATH this
  project has asked CMake to find a package configuration file provided by
  "AMDDeviceLibs", but CMake did not find one.

  Could not find a package configuration file provided by "AMDDeviceLibs"
  with any of the following names:

    AMDDeviceLibsConfig.cmake
    amddevicelibs-config.cmake

  Add the installation prefix of "AMDDeviceLibs" to CMAKE_PREFIX_PATH or set
  "AMDDeviceLibs_DIR" to a directory containing one of the above files.  If
  "AMDDeviceLibs" provides a separate development package or SDK, be sure it
  has been installed.



------------LLVM_DIR: /usr/lib/cmake/llvm
---LLVM_INCLUDE_DIRS: /usr/include
---LLVM_LIBRARY_DIRS: /usr/lib
-----------Clang_DIR: /usr/lib/cmake/clang
--CLANG_INCLUDE_DIRS: /usr/include
----LLD_INCLUDE_DIRS:
---AMDDeviceLibs_DIR: AMDDeviceLibs_DIR-NOTFOUND
------------ROCM_DIR: ROCM_DIR-NOTFOUND

-- Configuring done
-- Generating done
-- Build files have been written to: /dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build
guest@slax:/dev/shm/ROCm-CompilerSupport-rocm-3.8.0$ make -C build
make: вход в каталог «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
make[1]: вход в каталог «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
make[2]: вход в каталог «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
Scanning dependencies of target amd_comgr
make[2]: выход из каталога «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
make[2]: вход в каталог «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
[  1%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-compiler.cpp.o
[  2%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-disassembly.cpp.o
[  3%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-elfdump.cpp.o
[  4%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-env.cpp.o
[  6%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-metadata.cpp.o
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:587:13: error: no member named 'EF_AMDGPU_MACH_AMDGCN_GFX1030' in namespace 'llvm::ELF'; did you mean 'EF_AMDGPU_MACH_AMDGCN_GFX1010'?
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1030:
       ~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            EF_AMDGPU_MACH_AMDGCN_GFX1010
/usr/include/llvm/BinaryFormat/ELF.h:708:3: note: 'EF_AMDGPU_MACH_AMDGCN_GFX1010' declared here
  EF_AMDGPU_MACH_AMDGCN_GFX1010 = 0x033,
  ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:587:8: error: duplicate case value 'EF_AMDGPU_MACH_AMDGCN_GFX1010'
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1030:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:612:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameV3<llvm::object::ELFType<llvm::support::little, false> >' requested here
    return getElfIsaNameV3(Obj, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:624:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameImpl<llvm::object::ELFType<llvm::support::little, false> >' requested here
    return getElfIsaNameImpl(ELF32LE, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:578:8: note: previous case defined here
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1010:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:587:8: error: duplicate case value 'EF_AMDGPU_MACH_AMDGCN_GFX1010'
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1030:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:612:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameV3<llvm::object::ELFType<llvm::support::little, true> >' requested here
    return getElfIsaNameV3(Obj, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:626:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameImpl<llvm::object::ELFType<llvm::support::little, true> >' requested here
    return getElfIsaNameImpl(ELF64LE, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:578:8: note: previous case defined here
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1010:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:587:8: error: duplicate case value 'EF_AMDGPU_MACH_AMDGCN_GFX1010'
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1030:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:612:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameV3<llvm::object::ELFType<llvm::support::big, false> >' requested here
    return getElfIsaNameV3(Obj, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:628:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameImpl<llvm::object::ELFType<llvm::support::big, false> >' requested here
    return getElfIsaNameImpl(ELF32BE, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:578:8: note: previous case defined here
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1010:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:587:8: error: duplicate case value 'EF_AMDGPU_MACH_AMDGCN_GFX1010'
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1030:
       ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:612:12: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameV3<llvm::object::ELFType<llvm::support::big, true> >' requested here
    return getElfIsaNameV3(Obj, Size, IsaName);
           ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:630:10: note: in instantiation of function template specialization 'COMGR::metadata::getElfIsaNameImpl<llvm::object::ELFType<llvm::support::big, true> >' requested here
  return getElfIsaNameImpl(ELF64BE, Size, IsaName);
         ^
/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/lib/comgr/src/comgr-metadata.cpp:578:8: note: previous case defined here
  case ELF::EF_AMDGPU_MACH_AMDGCN_GFX1010:
       ^
5 errors generated.
make[2]: *** [CMakeFiles/amd_comgr.dir/build.make:135: CMakeFiles/amd_comgr.dir/src/comgr-metadata.cpp.o] Ошибка 1
make[2]: выход из каталога «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
make[1]: *** [CMakeFiles/Makefile2:175: CMakeFiles/amd_comgr.dir/all] Ошибка 2
make[1]: выход из каталога «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
make: *** [Makefile:183: all] Ошибка 2
make: выход из каталога «/dev/shm/ROCm-CompilerSupport-rocm-3.8.0/build»
```

Ah, it wants something else first (AMDDeviceLibs_DIR, ROCM_DIR) ..still, I hope  looking at those PKGBUILDS will be useful!





---

### 评论 #3 — Dan-RAI (2020-11-09T15:58:15Z)


Did someone solve this issue ? 

Have a similar problem, and would be very interested to learn a solution for the missing ```amd_comgrConfig.cmake```



```***** Library versions from dpkg *****

rocm-dev VERSION: 3.9.0.30900-17
rocm-device-libs VERSION: 1.0.0.637-rocm-rel-3.9-17-db8c0c3
rocm-libs VERSION: 3.9.0.30900-17
hsakmt-roct VERSION: 20200924.0.55-mainline-20200924-0-gcd55f1f
hsakmt-roct-dev VERSION: 20200924.0.55-mainline-20200924-0-gcd55f1f
hsa-rocr-dev VERSION: 1.2.30900.0-rocm-rel-3.9-17-75f9b74a

***** Library versions from cmake find_package *****

CMake Error at /usr/share/cmake-3.18/Modules/CMakeFindDependencyMacro.cmake:47 (find_package):
  By not providing "Findamd_comgr.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "amd_comgr", but CMake did not find one.

  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:

    amd_comgrConfig.cmake
    amd_comgr-config.cmake

  Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
  "amd_comgr_DIR" to a directory containing one of the above files.  If
  "amd_comgr" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  /opt/rocm/hip/lib/cmake/hip/hip-config.cmake:112 (find_dependency)
  cmake/public/LoadHIP.cmake:131 (find_package)
  cmake/public/LoadHIP.cmake:170 (find_package_and_print_version)
  cmake/Dependencies.cmake:1154 (include)
  CMakeLists.txt:513 (include)```


---

### 评论 #4 — rkothako (2020-11-10T07:09:33Z)

Thanks all for the info.
Hi @Dan-RAI or @ggghamd , can you please share the exact steps(one by one) you followed.

---

### 评论 #5 — Dan-RAI (2020-11-10T08:24:41Z)

sure,

for me:

* Installing ROCm on Ubuntu 18.04.5 LTS via apt as described on the official site (single installation mode + all extra packages).

* Compiling pytorch from the official ROCm fork (I tried master + all other branches with 3.9 in the name)

---

### 评论 #6 — rkothako (2020-11-10T09:28:02Z)

> 
> 
> Did someone solve this issue ?
> 
> Have a similar problem, and would be very interested to learn a solution for the missing `amd_comgrConfig.cmake`
> 
> ```
> 
> rocm-dev VERSION: 3.9.0.30900-17
> rocm-device-libs VERSION: 1.0.0.637-rocm-rel-3.9-17-db8c0c3
> rocm-libs VERSION: 3.9.0.30900-17
> hsakmt-roct VERSION: 20200924.0.55-mainline-20200924-0-gcd55f1f
> hsakmt-roct-dev VERSION: 20200924.0.55-mainline-20200924-0-gcd55f1f
> hsa-rocr-dev VERSION: 1.2.30900.0-rocm-rel-3.9-17-75f9b74a
> 
> ***** Library versions from cmake find_package *****
> 
> CMake Error at /usr/share/cmake-3.18/Modules/CMakeFindDependencyMacro.cmake:47 (find_package):
>   By not providing "Findamd_comgr.cmake" in CMAKE_MODULE_PATH this project
>   has asked CMake to find a package configuration file provided by
>   "amd_comgr", but CMake did not find one.
> 
>   Could not find a package configuration file provided by "amd_comgr" with
>   any of the following names:
> 
>     amd_comgrConfig.cmake
>     amd_comgr-config.cmake
> 
>   Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
>   "amd_comgr_DIR" to a directory containing one of the above files.  If
>   "amd_comgr" provides a separate development package or SDK, be sure it has
>   been installed.
> Call Stack (most recent call first):
>   /opt/rocm/hip/lib/cmake/hip/hip-config.cmake:112 (find_dependency)
>   cmake/public/LoadHIP.cmake:131 (find_package)
>   cmake/public/LoadHIP.cmake:170 (find_package_and_print_version)
>   cmake/Dependencies.cmake:1154 (include)
>   CMakeLists.txt:513 (include)```
> ```

Can you please share the exact steps to reproduce this problem

---

### 评论 #7 — Dan-RAI (2020-11-10T16:35:18Z)

I think I said already everything of relevance.

If you look into the ```LoadHIP.cmake``` of pytorch in your ROCm pytorch fork repo, you will find 

```
message("\n***** Library versions from cmake find_package *****\n")

  set(CMAKE_HCC_FLAGS_DEBUG ${CMAKE_CXX_FLAGS_DEBUG})
  set(CMAKE_HCC_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
  ### Remove setting of Flags when FindHIP.CMake PR #558 is accepted.###

  set(hip_DIR ${HIP_PATH}/lib/cmake/hip)
  set(AMDDeviceLibs_DIR ${ROCM_PATH}/lib/cmake/AMDDeviceLibs)
  set(amd_comgr_DIR ${ROCM_PATH}/lib/cmake/amd_comgr)
  set(rocrand_DIR ${ROCRAND_PATH}/lib/cmake/rocrand)
  set(hiprand_DIR ${HIPRAND_PATH}/lib/cmake/hiprand)
  set(rocblas_DIR ${ROCBLAS_PATH}/lib/cmake/rocblas)
  set(miopen_DIR ${MIOPEN_PATH}/lib/cmake/miopen)
  set(rocfft_DIR ${ROCFFT_PATH}/lib/cmake/rocfft)
  set(hipsparse_DIR ${HIPSPARSE_PATH}/lib/cmake/hipsparse)
  set(rccl_DIR ${RCCL_PATH}/lib/cmake/rccl)
  set(rocprim_DIR ${ROCPRIM_PATH}/lib/cmake/rocprim)
  set(hipcub_DIR ${HIPCUB_PATH}/lib/cmake/hipcub)
  set(rocthrust_DIR ${ROCTHRUST_PATH}/lib/cmake/rocthrust)

  find_package_and_print_version(hip REQUIRED)
  find_package_and_print_version(amd_comgr REQUIRED)
```

I am asking for what this ```amd_comgr``` is, as I do not have it in my full ROCm 3.9 installation. At least not in the rocm/lib/cmake path . All the other packages do show up in my installation ...

Thanks



---

### 评论 #8 — rkothako (2020-11-11T10:08:07Z)

Hi @Dan-RAI 
Can you plesae try installing comgr as "sudo apt install comgr" and check whether the issue is resolved.
Thank you.

---

### 评论 #9 — Dan-RAI (2020-11-11T10:12:59Z)

Hi,

its already installed:

```Reading package lists... Done
Building dependency tree       
Reading state information... Done
comgr is already the newest version (1.9.0.194-rocm-rel-3.9-17-0fa438b).
The following packages were automatically installed and are no longer required:
  libllvm9 librhash0 nsight-compute-2019.5.0
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 21 not upgraded.
```

Though there does not appear to be corresponding package in the rocm/lib/cmake folder ...

---

### 评论 #10 — rkothako (2020-11-11T11:40:37Z)

Once you have comgr installed in machine, you will find comgr folder and files @ /opt/rocm-3.9.0/lib/cmake/amd_comgr
comgr is needed and will be installed automatically as part of OpenCL.

Comgr is code object manager tool for inspecting code objects.
Check this for more information: https://github.com/RadeonOpenCompute/ROCm-CompilerSupport

---

### 评论 #11 — Dan-RAI (2020-11-11T11:47:14Z)

Thanks,

I just did a 

```apt install comgr --reinstall```  

and now the package shows up in the lib/cmake folder.


---

### 评论 #12 — rkothako (2020-11-11T11:59:44Z)

Good to know @Dan-RAI 
Can you please proceed with compilation by calling pointing comgr path, if required.
Please update once done.
Thank you.

---

### 评论 #13 — Dan-RAI (2020-11-11T12:12:37Z)

For compiling, he finds now automatically ```amd_comgr``` but is stuck in the next step:

```Could not find a package configuration file provided by "hsa-runtime64"
  with any of the following names:

    hsa-runtime64Config.cmake
    hsa-runtime64-config.cmake
```
However, these files I can find in the lib/cmake/hsa-runtime64. Setting the path manually via CMAKE_PREFIX_PATH, does not help. 


---

### 评论 #14 — rkothako (2020-11-12T07:24:08Z)

Hi @Dan-RAI 
Looks like its a new issue(hsa runtime detection missing), which was not before.
I recommend to do clean of rocm and then try installing rocm again to overcome subsequent problems.

---

### 评论 #15 — gggh000 (2020-11-12T17:45:26Z)

> Hi @Dan-RAI
> Looks like its a new issue(hsa runtime detection missing), which was not before.
> I recommend to do clean of rocm and then try installing rocm again to overcome subsequent problems.

I dont think this is a feasible/reasonable solution at all. All did was following the instruction and it is not working. 

---

### 评论 #16 — Dan-RAI (2020-11-12T22:03:10Z)

Well, purging + reinstall of amd doesn't help. 

Rather, it seems that most of the branches in the rocm pytorch repo are just plain broken. The only branch I had some success with is ```rocm3.9_nightly_wheel```. However, that one requires in addition ```rccl```, which in turn needs ```nccl```. This is funny: In order to be able to compile for AMD, I need to join Nvidia's Dev club ;) 

With that I reach 77%, until hitting a compile fail in some .hip. 

That AMD only pushes out a docker for pytorch etc, which is a joke, just shows how confident AMD actually is about the quality of their codebase ...

---

### 评论 #17 — ROCmSupport (2021-04-05T10:07:43Z)

Hi @ggghamd 
Hope this issue is resolved, closing it right now.
Feel free to open a new issue if any for quick resolution.
Thank you.

---
