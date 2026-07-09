# ARM AArch64: cannot find -lhsakmt on AArch64 based System via KVM

- **Issue #:** 187
- **State:** closed
- **Created:** 2017-08-24T08:48:54Z
- **Updated:** 2018-06-03T15:00:09Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/187

I am trying to build ROCT-Thunk-Interface and ROCR-Runtime on my ubunu16.04-arm64 server which is running on qemu. Here are my steps:
First build ROCT-Thunk-Interface,
1.make
2.make deb
3.sudo dpkg -i build/deb/hsakmt-dev-2.0.0-arm64.deb
after that, path /opt/rocm/libhsakmt and /opt/rocm/include /opt/rocm/lib generated,

Then build ROCR-Runtime,
1.cd src
2.mkdir build & cd build
3.cmake -D CMAKE_PREFIX_PATH=/opt/rocm/libhsakmt ../
4.make
on the 4th step, error occurs as follows:

[100%] Linking CXX shared library libhsa-runtime64.so
/usr/bin/ld: cannot find -lhsakmt
collect2: error: ld returned 1 exit status
CMakeFiles/hsa-runtime64.dir/build.make:927: recipe for target 'libhsa-runtime64.so.1.0.0' failed
make[2]: *** [libhsa-runtime64.so.1.0.0] Error 1
CMakeFiles/Makefile2:104: recipe for target 'CMakeFiles/hsa-runtime64.dir/all' failed
make[1]: *** [CMakeFiles/hsa-runtime64.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2

