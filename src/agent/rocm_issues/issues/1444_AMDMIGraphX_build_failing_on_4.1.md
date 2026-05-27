# AMDMIGraphX build failing on 4.1

> **Issue #1444**
> **状态**: closed
> **创建时间**: 2021-04-09T01:24:37Z
> **更新时间**: 2021-05-07T12:01:39Z
> **关闭时间**: 2021-05-07T12:01:39Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1444

## 描述

Both cmake .. and rbuild to install dependency is showing following error about can not find 2 cmake files:

root@guest:~/ROCm-4.1/AMDMIGraphX/build# rbuild build -d depend --cxx=/opt/rocm/llvm/bin/clang++
cget -p depend clean -y
cget -p depend init --cxx /opt/rocm/llvm/bin/clang++
cget -p depend ignore danmar/cppcheck
Ignore package danmar/cppcheck
cget -p depend ignore RadeonOpenCompute/clang-ocl
Ignore package RadeonOpenCompute/clang-ocl
cget -p depend ignore RadeonOpenCompute/rocm-cmake
Ignore package RadeonOpenCompute/rocm-cmake
cget -p depend ignore ROCm-Developer-Tools/HIP
Ignore package ROCm-Developer-Tools/HIP
cget -p depend ignore ROCmSoftwarePlatform/MIOpen
Ignore package ROCmSoftwarePlatform/MIOpen
cget -p depend ignore ROCmSoftwarePlatform/MIOpenGEMM
Ignore package ROCmSoftwarePlatform/MIOpenGEMM
cget -p depend ignore ROCmSoftwarePlatform/rocBLAS
Ignore package ROCmSoftwarePlatform/rocBLAS
cget -p depend install -f requirements.txt
cmake -DCMAKE_TOOLCHAIN_FILE=depend/cget/cget.cmake /root/ROCm-4.1/AMDMIGraphX/build
CMake Error at CMakeLists.txt:22 (find_package):
  By not providing "Findnlohmann_json.cmake" in CMAKE_MODULE_PATH this
  project has asked CMake to find a package configuration file provided by
  "nlohmann_json", but CMake did not find one.

  Could not find a package configuration file provided by "nlohmann_json"
  (requested version 3.8.0) with any of the following names:

    nlohmann_jsonConfig.cmake
    nlohmann_json-config.cmake

  Add the installation prefix of "nlohmann_json" to CMAKE_PREFIX_PATH or set
  "nlohmann_json_DIR" to a directory containing one of the above files.  If
  "nlohmann_json" provides a separate development package or SDK, be sure it
  has been installed.


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.1/AMDMIGraphX/build/CMakeFiles/CMakeOutput.log".
Traceback (most recent call last):
  File "/usr/local/bin/rbuild", line 11, in <module>
    load_entry_point('rbuild==0.0.1', 'console_scripts', 'rbuild')()
  File "/usr/local/lib/python2.7/dist-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python2.7/dist-packages/click/core.py", line 1259, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python2.7/dist-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python2.7/dist-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rbuild/cli.py", line 279, in w
    f(make_builder, *args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rbuild/cli.py", line 308, in build
    b.configure(clean=True)
  File "/usr/local/lib/python2.7/dist-packages/rbuild/cli.py", line 257, in configure
    self.cmake('-DCMAKE_TOOLCHAIN_FILE='+toolchain_file, self.get_source_dir(), *make_defines(self.get_defines()), cwd=self.get_build_dir())
  File "/usr/local/lib/python2.7/dist-packages/rbuild/cli.py", line 208, in cmake
    self.cmd(['cmake'] + sanitize_cmake_args(list(args)), **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/rbuild/cli.py", line 202, in cmd
    subprocess.check_call(c, **kwargs)
  File "/usr/lib/python2.7/subprocess.py", line 190, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['cmake', u'-DCMAKE_TOOLCHAIN_FILE=depend/cget/cget.cmake', '/root/ROCm-4.1/AMDMIGraphX/build']' returned non-zero exit status 1
root@guest:~/ROCm-4.1/AMDMIGraphX/build# nano -w ../README.md
root@guest:~/ROCm-4.1/AMDMIGraphX/build# ls -l /opt/rocm/llvm/bin/clang++
lrwxrwxrwx 1 root root 5 Apr  3 06:56 /opt/rocm/llvm/bin/clang++ -> clang
root@guest:~/ROCm-4.1/AMDMIGraphX/build# nano -w ../README.md


---

## 评论 (7 条)

### 评论 #1 — gggh000 (2021-04-09T01:25:57Z)

Culd not find those files anywhere? 

root@guest:~/ROCm-4.1/AMDMIGraphX/build# find /opt/ -name nlohmann_jsonConfig.cmake
amdgpu/     amdgpu-pro/ rocm/       rocm-4.1.0/
root@guest:~/ROCm-4.1/AMDMIGraphX/build# find /opt/rocm-4.1.0/ -name nlohmann_jsonConfig.cmake
root@guest:~/ROCm-4.1/AMDMIGraphX/build#


---

### 评论 #2 — ROCmSupport (2021-04-09T07:20:40Z)

Thanks @gggh000 for reaching out.
I am checking this for you.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-04-09T07:22:48Z)

Looks like I have not seen any issue like yours.

**-- Found nlohmann_json: /home/master/AMDMIGraphX/depend/lib/cmake/nlohmann_json/nlohmann_jsonConfig.cmake (found suitable version "3.8.0", minimum required is "3.8.0")**

My config is: MI25 + ROCm 4.1 + Ubuntu 18.04.5 + 5.4.0-70-generic


---

### 评论 #4 — ROCmSupport (2021-04-09T07:30:30Z)

I followed below steps and I have not seen any issues.

#install rocm 
1. Install ROCm 4.1 + rocm-libs etc.,.

#install rbuild
2. sudo apt install python3-pip
3. pip3 install https://github.com/RadeonOpenCompute/rbuild/archive/master.tar.gz 
4. git clone https://github.com/ROCmSoftwarePlatform/AMDMIGraphX -b rocm-4.1.x && cd AMDMIGraphx
5. export PATH=$HOME/.local/bin:$PATH
6. rbuild build -d depend --cxx=/opt/rocm/llvm/bin/clang++

Output: Installation successful

Please let me know if you need any more information.
Thank you.


---

### 评论 #5 — gggh000 (2021-04-13T16:37:42Z)

I followed your steps but running into issue. There has to be something else breaking that preinstalled or preconfigured on your system. 

---

### 评论 #6 — pfultz2 (2021-04-13T20:32:51Z)

Its missing nlohmann_json, but rbuild should install it. You can see a list of dependencies that rbuild installed by doing `cget -p depend ls`. It would be useful to see the output you see when rbuild tries to build nlohmann_json, this may give insights into why it was skipped or not found.

---

### 评论 #7 — ROCmSupport (2021-05-07T12:01:39Z)

Hi @gggh000 
nlohmann_json is a third party package and its mostly available in all of the machines.
I recommend you to try on a clean/different system.
I tried in 4 machines and no installation issues observed as per the above steps mentioned.
Thank you.




---
