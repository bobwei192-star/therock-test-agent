# Remove hardcoded values for NBIT and NBITSTR based on checks for x86_64 only in rocminfo

- **Issue #:** 1223
- **State:** closed
- **Created:** 2020-09-17T21:55:32Z
- **Updated:** 2021-01-28T11:05:57Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1223

rocminfo source code sets:

x86_64 specific!
## Extend Compiler flags based on Processor architecture
if ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64  -msse -msse2" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86" )
  set ( NBIT 32 )
  set ( NBITSTR "" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32" )
endif ()

This makes it harder to port the tool to ppc64le which is 64bit but needs something like:

## Extend Compiler flags based on Processor architecture
if ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86_64" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64  -msse -msse2" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "x86" )
  set ( NBIT 32 )
  set ( NBITSTR "" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32" )
elseif ( ${CMAKE_SYSTEM_PROCESSOR} STREQUAL "ppc64le" )
  set ( NBIT 64 )
  set ( NBITSTR "64" )
  set ( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64 " )
endif ()

Other architectures that are 64 bit wide (aarch64) may also be affected by this code that makes assumptions based on amd64 architecture. 