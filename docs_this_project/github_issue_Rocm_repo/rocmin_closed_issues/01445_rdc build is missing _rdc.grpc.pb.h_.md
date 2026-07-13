# rdc build is missing "rdc.grpc.pb.h"

- **Issue #:** 1445
- **State:** closed
- **Created:** 2021-04-09T01:56:16Z
- **Updated:** 2021-12-28T05:37:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/1445

I downloaded, built and isntalled grpc OK onto default path however rdc build is complaining about this missing file. Seached in source code, /usr/local location but nowehere to be found:



~/ROCm-4.1/rdc/build# cmake -DROCM_DIR=/opt/rocm  -DGRPC_ROOT="$GRPC_PROTOC_ROOT" ..
Package version:
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
Build Configuration:
-----------GRPC ROOT:
-----------ROCM_DIR : /opt/rocm
protoc command returned: No such file or directory
GRPC_PLUGIN=/bin/grpc_cpp_plugin)
protoc cmd:
  $ /bin/protoc --proto_path=/root/ROCm-4.1/rdc/protos
    --grpc_out=/root/ROCm-4.1/rdc/build
....--plugin=protoc-gen-grpc="/bin/grpc_cpp_plugin" /root/ROCm-4.1/rdc/protos/rdc.proto
protoc command returned: No such file or directory
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                             Cmake Server
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Build Configuration:
-------------BuildType:
--------------Compiler: /usr/bin/c++
---------------Version: 7.5.0
----------Proj Src Dir: /root/ROCm-4.1/rdc
----------Proj Bld Dir: /root/ROCm-4.1/rdc/build
----------Proj Lib Dir: /root/ROCm-4.1/rdc/build/lib
----------Proj Exe Dir: /root/ROCm-4.1/rdc/build/bin
----------RSMI Lib Dir: /opt/rocm/rocm_smi/lib
----------RSMI Inc Dir: /opt/rocm/rocm_smi/include
---------GRPC Root Dir:
---Server Install Path: /

SERVER_SRC_LIST=src/rdc_rsmi_service.cc;src/rdc_admin_service.cc;src/rdc_api_service.cc;src/rdc_server_main.cc;/root/ROCm-4.1/rdc/common/rdc_utils.cc;/root/ROCm-4.1/rdc/common/rdc_capabilities.cc
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Finished Cmake Server
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                       Cmake Client Lib
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Build Configuration:
-------------BuildType:
--------------Compiler: /usr/bin/c++
---------------Version: 7.5.0
----------Proj Src Dir: /root/ROCm-4.1/rdc
----------Proj Bld Dir: /root/ROCm-4.1/rdc/build
----------Proj Lib Dir: /root/ROCm-4.1/rdc/build/lib
----------Proj Exe Dir: /root/ROCm-4.1/rdc/build/bin
----------RSMI Lib Dir: /opt/rocm/rocm_smi/lib
----------RSMI Inc Dir: /opt/rocm/rocm_smi/include
---------GRPC Root Dir:
-Client Install Prefix: opt/rocm

SOVERSION: 0.5
CLIENT_LIB_SRC_LIST=/root/ROCm-4.1/rdc/client/src/rdc_client.cc;/root/ROCm-4.1/rdc/client/src/rdc_client_main.cc;/root/ROCm-4.1/rdc/client/src/rdc_client_utils.cc;/root/ROCm-4.1/rdc/common/rdc_utils.cc
-- Found Doxygen: /usr/bin/doxygen (found version "1.8.13") found components: doxygen missing components: dot
-- Could NOT find LATEX (missing: LATEX_COMPILER PDFLATEX)
Doxygen or Latex is not found. Will not generate documents.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Finished Cmake Client Lib
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                             Cmake rdci
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Build Configuration:
-----------BuildType:
------------Compiler: /usr/bin/c++
-------------Version: 7.5.0
------Install Prefix: /
-Pkg.-Install Prefix: /
-CMake inst. Bindir :
--------Proj Src Dir: /root/ROCm-4.1/rdc
--------Proj Bld Dir: /root/ROCm-4.1/rdc/build
--------Proj Lib Dir: /root/ROCm-4.1/rdc/build/lib
--------Proj Exe Dir: /root/ROCm-4.1/rdc/build/bin
--------RSMI Lib Dir: /opt/rocm/rocm_smi/lib
--------RSMI Inc Dir: /opt/rocm/rocm_smi/include
-------GRPC ROOT Dir:

RDCI_SRC_LIST=/root/ROCm-4.1/rdc/rdci/src/rdci.cc;/root/ROCm-4.1/rdc/rdci/src/RdciDiscoverySubSystem.cc;/root/ROCm-4.1/rdc/rdci/src/RdciSubSystem.cc;/root/ROCm-4.1/rdc/rdci/src/RdciGroupSubSystem.cc;/root/ROCm-4.1/rdc/rdci/src/RdciFieldGroupSubSystem.cc;/root/ROCm-4.1/rdc/rdci/src/RdciDmonSubSystem.cc;/root/ROCm-4.1/rdc/rdci/src/RdciStatsSubSystem.cc;/root/ROCm-4.1/rdc/common/rdc_utils.cc;/root/ROCm-4.1/rdc/common/rdc_fields_supported.cc
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Finished Cmake rdci
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                       Cmake RDC Lib
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Build Configuration:
-----------BuildType:
------------Compiler: /usr/bin/c++
-------------Version: 7.5.0
--------Proj Src Dir: /root/ROCm-4.1/rdc
--------Proj Bld Dir: /root/ROCm-4.1/rdc/build
--------Proj Lib Dir: /root/ROCm-4.1/rdc/build/lib
--------Proj Exe Dir: /root/ROCm-4.1/rdc/build/bin
--------RSMI Lib Dir: /opt/rocm/rocm_smi/lib
--------RSMI Inc Dir: /opt/rocm/rocm_smi/include

SOVERSION: 0.5
BOOTSTRAP_LIB_INC_LIST=/root/ROCm-4.1/rdc/include/rdc/rdc.h;/root/ROCm-4.1/rdc/include/rdc_lib/rdc_common.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcLogger.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcHandler.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcLibraryLoader.h;/root/ROCm-4.1/rdc/common/rdc_fields_supported.h
RDC_LIB_INC_LIST=/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcEmbeddedHandler.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcMetricFetcher.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcMetricFetcherImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcGroupSettings.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcGroupSettingsImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcCacheManager.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcCacheManagerImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcMetricsUpdater.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcMetricsUpdaterImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcWatchTable.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcWatchTableImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcRasLib.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcSmiLib.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcModuleMgrImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcModuleMgr.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcTelemetry.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcTelemetryModule.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcNotification.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcNotificationImpl.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RsmiUtils.h;/root/ROCm-4.1/rdc/common/rdc_fields_supported.h;/root/ROCm-4.1/rdc/common/rdc_capabilities.h
RDCCLIENT_LIB_INC_LIST=/root/ROCm-4.1/rdc/include/rdc/rdc.h;/root/ROCm-4.1/rdc/include/rdc_lib/RdcHandler.h;/root/ROCm-4.1/rdc/include/rdc_lib/impl/RdcStandaloneHandler.h
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Finished Cmake RDC Lib
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                             Cmake Example
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Build Configuration:
-----------BuildType:
------------Compiler: /usr/bin/c++
-------------Version: 7.5.0
--------Proj Src Dir: /root/ROCm-4.1/rdc
--------Proj Bld Dir: /root/ROCm-4.1/rdc/build
--------Proj Lib Dir: /root/ROCm-4.1/rdc/build/lib
--------Proj Exe Dir: /root/ROCm-4.1/rdc/build/bin
--------RSMI Lib Dir: /opt/rocm/rocm_smi/lib
--------RSMI Inc Dir: /opt/rocm/rocm_smi/include

JOBSTATS_EXAMPLE_SRC_LIST=/root/ROCm-4.1/rdc/example/job_stats_example.cc
FIELDVALUE_EXAMPLE_SRC_LIST=/root/ROCm-4.1/rdc/example/field_value_example.cc
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Finished Cmake Example
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Using Linux Distro: NAME="Ubuntu"
Using CPACK_DEBIAN_PACKAGE_RELEASE local
Using CPACK_RPM_PACKAGE_RELEASE local
-- Configuring done
-- Generating done
-- Build files have been written to: /root/ROCm-4.1/rdc/build
root@sriov-guest:~/ROCm-4.1/rdc/build# make -j`nproc`
/usr/local/bin/cmake -S/root/ROCm-4.1/rdc -B/root/ROCm-4.1/rdc/build --check-build-system CMakeFiles/Makefile.cmake 0
/usr/local/bin/cmake -E cmake_progress_start /root/ROCm-4.1/rdc/build/CMakeFiles /root/ROCm-4.1/rdc/build/CMakeFiles/progress.marks
make -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/root/ROCm-4.1/rdc/build'
make -f rdc_libs/CMakeFiles/rdc_bootstrap.dir/build.make rdc_libs/CMakeFiles/rdc_bootstrap.dir/depend
make -f client/CMakeFiles/rdc_client_smi.dir/build.make client/CMakeFiles/rdc_client_smi.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/rdc/build'
cd /root/ROCm-4.1/rdc/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/rdc /root/ROCm-4.1/rdc/rdc_libs /root/ROCm-4.1/rdc/build /root/ROCm-4.1/rdc/build/rdc_libs /root/ROCm-4.1/rdc/build/rdc_libs/CMakeFiles/rdc_bootstrap.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/rdc/build'
cd /root/ROCm-4.1/rdc/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/rdc /root/ROCm-4.1/rdc/client /root/ROCm-4.1/rdc/build /root/ROCm-4.1/rdc/build/client /root/ROCm-4.1/rdc/build/client/CMakeFiles/rdc_client_smi.dir/DependInfo.cmake --color=
Scanning dependencies of target rdc_bootstrap
Scanning dependencies of target rdc_client_smi
make[2]: Leaving directory '/root/ROCm-4.1/rdc/build'
make -f rdc_libs/CMakeFiles/rdc_bootstrap.dir/build.make rdc_libs/CMakeFiles/rdc_bootstrap.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/rdc/build'
make[2]: Entering directory '/root/ROCm-4.1/rdc/build'
make -f client/CMakeFiles/rdc_client_smi.dir/build.make client/CMakeFiles/rdc_client_smi.dir/build
make[2]: Entering directory '/root/ROCm-4.1/rdc/build'
[  2%] Building CXX object rdc_libs/CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLogger.cc.o
[  4%] Building CXX object rdc_libs/CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLibraryLoader.cc.o
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/bin/c++  -Drdc_bootstrap_EXPORTS -I/opt/rocm/rocm_smi/include -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/common -I/root/ROCm-4.1/rdc/rdc_libs/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLogger.cc.o -c /root/ROCm-4.1/rdc/rdc_libs/bootstrap/src/RdcLogger.cc
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/bin/c++  -Drdc_bootstrap_EXPORTS -I/opt/rocm/rocm_smi/include -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/common -I/root/ROCm-4.1/rdc/rdc_libs/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLibraryLoader.cc.o -c /root/ROCm-4.1/rdc/rdc_libs/bootstrap/src/RdcLibraryLoader.cc
[  6%] Building CXX object rdc_libs/CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcBootStrap.cc.o
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/bin/c++  -Drdc_bootstrap_EXPORTS -I/opt/rocm/rocm_smi/include -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/common -I/root/ROCm-4.1/rdc/rdc_libs/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcBootStrap.cc.o -c /root/ROCm-4.1/rdc/rdc_libs/bootstrap/src/RdcBootStrap.cc
[ 10%] Building CXX object client/CMakeFiles/rdc_client_smi.dir/src/rdc_client.cc.o
[ 10%] Building CXX object rdc_libs/CMakeFiles/rdc_bootstrap.dir/__/common/rdc_fields_supported.cc.o
[ 12%] Building CXX object client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_main.cc.o
[ 14%] Building CXX object client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_utils.cc.o
cd /root/ROCm-4.1/rdc/build/client && /usr/bin/c++  -Drdc_client_smi_EXPORTS -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/client/include -I/root/ROCm-4.1/rdc/build -I/include -I/opt/rocm/rocm_smi/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_client_smi.dir/src/rdc_client.cc.o -c /root/ROCm-4.1/rdc/client/src/rdc_client.cc
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/bin/c++  -Drdc_bootstrap_EXPORTS -I/opt/rocm/rocm_smi/include -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/common -I/root/ROCm-4.1/rdc/rdc_libs/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_bootstrap.dir/__/common/rdc_fields_supported.cc.o -c /root/ROCm-4.1/rdc/common/rdc_fields_supported.cc
cd /root/ROCm-4.1/rdc/build/client && /usr/bin/c++  -Drdc_client_smi_EXPORTS -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/client/include -I/root/ROCm-4.1/rdc/build -I/include -I/opt/rocm/rocm_smi/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_client_smi.dir/src/rdc_client_main.cc.o -c /root/ROCm-4.1/rdc/client/src/rdc_client_main.cc
cd /root/ROCm-4.1/rdc/build/client && /usr/bin/c++  -Drdc_client_smi_EXPORTS -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/client/include -I/root/ROCm-4.1/rdc/build -I/include -I/opt/rocm/rocm_smi/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_client_smi.dir/src/rdc_client_utils.cc.o -c /root/ROCm-4.1/rdc/client/src/rdc_client_utils.cc
[ 16%] Building CXX object client/CMakeFiles/rdc_client_smi.dir/__/common/rdc_utils.cc.o
cd /root/ROCm-4.1/rdc/build/client && /usr/bin/c++  -Drdc_client_smi_EXPORTS -I/root/ROCm-4.1/rdc -I/root/ROCm-4.1/rdc/include -I/root/ROCm-4.1/rdc/client/include -I/root/ROCm-4.1/rdc/build -I/include -I/opt/rocm/rocm_smi/include  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG -fPIC   -o CMakeFiles/rdc_client_smi.dir/__/common/rdc_utils.cc.o -c /root/ROCm-4.1/rdc/common/rdc_utils.cc
/root/ROCm-4.1/rdc/client/src/rdc_client_main.cc:29:10: fatal error: rdc.grpc.pb.h: No such file or directory
 #include "rdc.grpc.pb.h"  // NOLINT
          ^~~~~~~~~~~~~~~
compilation terminated.
client/CMakeFiles/rdc_client_smi.dir/build.make:78: recipe for target 'client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_main.cc.o' failed
make[2]: *** [client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_main.cc.o] Error 1
make[2]: *** Waiting for unfinished jobs....
In file included from /root/ROCm-4.1/rdc/client/src/rdc_client.cc:29:0:
/root/ROCm-4.1/rdc/client/include/rdc/rdc_client_main.h:32:10: fatal error: rdc.grpc.pb.h: No such file or directory
 #include "rdc.grpc.pb.h"  // NOLINT
          ^~~~~~~~~~~~~~~
compilation terminated.
/root/ROCm-4.1/rdc/client/src/rdc_client_utils.cc:24:10: fatal error: rdc.grpc.pb.h: No such file or directory
 #include "rdc.grpc.pb.h"  // NOLINT
          ^~~~~~~~~~~~~~~
compilation terminated.
client/CMakeFiles/rdc_client_smi.dir/build.make:65: recipe for target 'client/CMakeFiles/rdc_client_smi.dir/src/rdc_client.cc.o' failed
make[2]: *** [client/CMakeFiles/rdc_client_smi.dir/src/rdc_client.cc.o] Error 1
client/CMakeFiles/rdc_client_smi.dir/build.make:91: recipe for target 'client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_utils.cc.o' failed
make[2]: *** [client/CMakeFiles/rdc_client_smi.dir/src/rdc_client_utils.cc.o] Error 1
make[2]: Leaving directory '/root/ROCm-4.1/rdc/build'
CMakeFiles/Makefile2:213: recipe for target 'client/CMakeFiles/rdc_client_smi.dir/all' failed
make[1]: *** [client/CMakeFiles/rdc_client_smi.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 18%] Linking CXX shared library librdc_bootstrap.so
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/local/bin/cmake -E cmake_link_script CMakeFiles/rdc_bootstrap.dir/link.txt --verbose=1
/usr/bin/c++ -fPIC  -Wall -Wextra -m64 -msse -msse2 -std=c++11  -ggdb -O0 -DDEBUG  -shared -Wl,-soname,librdc_bootstrap.so.0 -o librdc_bootstrap.so.0.5 CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcBootStrap.cc.o CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLogger.cc.o CMakeFiles/rdc_bootstrap.dir/bootstrap/src/RdcLibraryLoader.cc.o CMakeFiles/rdc_bootstrap.dir/__/common/rdc_fields_supported.cc.o  -lpthread -ldl
cd /root/ROCm-4.1/rdc/build/rdc_libs && /usr/local/bin/cmake -E cmake_symlink_library librdc_bootstrap.so.0.5 librdc_bootstrap.so.0 librdc_bootstrap.so
make[2]: Leaving directory '/root/ROCm-4.1/rdc/build'
[ 18%] Built target rdc_bootstrap
make[1]: Leaving directory '/root/ROCm-4.1/rdc/build'
Makefile:154: recipe for target 'all' failed
make: *** [all] Error 2


 find /usr/local -name "rdc.grpc.pb.h"
 find /usr/ -name "rdc.grpc.pb.h"
 find  /git.co/grpc/ -name rdc.grpc.pb.h
 nano -w /root/ROCm-4.1/rdc/client/src/rdc_client_main.cc
