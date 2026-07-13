# rocm source code compile, on ubunu16.04-arm64 server

- **Issue #:** 183
- **State:** closed
- **Created:** 2017-08-22T03:05:38Z
- **Updated:** 2018-06-03T14:59:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/183

I want to compile ROCR-Runtime, I follow the steps like followings:
install the necessary libs:
* libelf-dev
* g++
* libc6-dev-i386 (for libhsakmt 32bit)
libpci-dev    fakeroot

then I do the followings:
cd src dir;
    mkdir build
    cd build
    cmake -D CMAKE_PREFIX_PATH=/opt/rocm/libhsakmt \
          ..
    make
in the dir  /opt/rocm/libhsakmt, it has lib and include sub dirs. Have libhsakmt.so.1 and hsakmt.h.

But when I make , I get the errors: 
[100%] Linking CXX shared library libhsa-runtime64.so
/usr/bin/ld: cannot find -lhsakmt
collect2: error: ld returned 1 exit status
CMakeFiles/hsa-runtime64.dir/build.make:927: recipe for target 'libhsa-runtime64.so.1.0.0' failed
make[2]: *** [libhsa-runtime64.so.1.0.0] Error 1
CMakeFiles/Makefile2:104: recipe for target 'CMakeFiles/hsa-runtime64.dir/all' failed
make[1]: *** [CMakeFiles/hsa-runtime64.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 

I serch the code, no 'libhsa-runtime64.so.* found, how can I solve it.