# [Issue]: -cl-fast-relaxed-math broken on ROCm 6.3.0

- **Issue #:** 4143
- **State:** closed
- **Created:** 2024-12-09T16:19:44Z
- **Updated:** 2025-02-21T15:31:42Z
- **Labels:** Under Investigation, Radeon Instinct MI60, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4143

### Problem Description

Updated my System to ROCm 6.3.0 now linking OpenCL Program segfaults if the compiler or linker arguments contain "-cl-fast-relaxed-math".

Example:
main.cpp
```C++
#include <string>
using std::string;
#include <vector>
using std::vector;
#include <iostream>
using std::cout, std::endl;

#include <CL/opencl.hpp>
using cl::Context, cl::Device, cl::linkProgram, cl::Platform, cl::Program;

int main() {
	string linkOptions = "-cl-fast-relaxed-math";
	string compileOptions = "-cl-fast-relaxed-math";

	vector<Platform> platforms;
	Platform::get(&platforms);

	vector<Device> devices;

	platforms[0].getDevices(CL_DEVICE_TYPE_ALL, &devices);

	Context context = Context(devices[0]); // MI60

	string src = R"(kernel void tet() {
						const long m = get_global_id(0);
						printf("ID %ld\n", m);
					}
					)";

	string src2 = R"(
					kernel void other() {
						const long n = get_global_id(0);
						printf("Do not print %ld\n", n);
					}
					)";

	Program p(context, src);
	p.compile(compileOptions);

	Program p2(context, src2);
	p2.compile(compileOptions);

	vector<Program> programs = {p, p2};
	int errorCode;
	cout << "Works until here" << endl;
	Program program = linkProgram(programs, linkOptions, nullptr, nullptr, &errorCode);
	cout << "Segfaults before error: " << errorCode << endl;

	cl::Kernel kernel{program, "tet"};

	auto queue = cl::CommandQueue(context);

	queue.enqueueNDRangeKernel(kernel, cl::NullRange,  cl::NDRange(2),  cl::NDRange(2));
	queue.finish();
}
```

CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.18)

project(
	FluidX3D
	VERSION 0.2.4
	DESCRIPTION "LBM simulation software"
	LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_compile_options(-pedantic)

# set install prefix if not specified otherwise
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
	set(CMAKE_INSTALL_PREFIX "${CMAKE_CURRENT_SOURCE_DIR}/install" CACHE PATH "Installation folder" FORCE)
endif()

## Libraries

# Download dependencies
file(
	DOWNLOAD
	https://github.com/cpm-cmake/CPM.cmake/releases/download/v0.40.2/CPM.cmake
	${CMAKE_CURRENT_BINARY_DIR}/cmake/CPM.cmake
	EXPECTED_HASH SHA256=c8cdc32c03816538ce22781ed72964dc864b2a34a310d3b7104812a5ca2d835d
)
include(${CMAKE_CURRENT_BINARY_DIR}/cmake/CPM.cmake)

# Downloads OpenCL libs linked in src
# License: Apache-2.0 license
# master might be unstable -> Needs to use tag and manual update
message("Downloading OpenCL libs ...")
CPMAddPackage("gh:KhronosGroup/OpenCL-Headers#v2024.10.24")
CPMAddPackage("gh:KhronosGroup/OpenCL-ICD-Loader#v2024.10.24")
CPMAddPackage(
	GITHUB_REPOSITORY KhronosGroup/OpenCL-CLHPP
	VERSION 2024.10.24
	EXCLUDE_FROM_ALL YES
	SYSTEM YES
	OPTIONS "BUILD_EXAMPLES OFF"
)
target_compile_definitions(HeadersCpp INTERFACE CL_HPP_TARGET_OPENCL_VERSION=300) # Use OpenCl 3.0
message("Finished downloading OpenCL libs.")

# For easy linking: Just always link everything
set(dependencies OpenCL::Headers OpenCL::OpenCL OpenCL::HeadersCpp)

ADD_EXECUTABLE(FluidX3D main.cpp)
target_link_libraries(FluidX3D PUBLIC ${dependencies})

# Moves the executeable and its dependencies to the install folder
install(TARGETS FluidX3D DESTINATION .)
```

### Operating System

Manjaro Linux

### CPU

N/A

### GPU

Radeon Instinct MI60

### ROCm Version

ROCm 6.3.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.14
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    13th Gen Intel(R) Core(TM) i9-13900K
  Uuid:                    CPU-XX                             
  Marketing Name:          13th Gen Intel(R) Core(TM) i9-13900K
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5500                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65540648(0x3e81228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65540648(0x3e81228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65540648(0x3e81228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65540648(0x3e81228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx906                             
  Uuid:                    GPU-0ba4694172da5ee7               
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      8192(0x2000) KB                    
  Chip ID:                 26273(0x66a1)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1800                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 472                                
  SDMA engine uCode::      145                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    33538048(0x1ffc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***  

### Additional Information

_No response_