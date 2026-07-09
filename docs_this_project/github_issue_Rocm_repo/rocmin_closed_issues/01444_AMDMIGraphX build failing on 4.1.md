# AMDMIGraphX build failing on 4.1

- **Issue #:** 1444
- **State:** closed
- **Created:** 2021-04-09T01:24:37Z
- **Updated:** 2021-05-07T12:01:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1444

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
