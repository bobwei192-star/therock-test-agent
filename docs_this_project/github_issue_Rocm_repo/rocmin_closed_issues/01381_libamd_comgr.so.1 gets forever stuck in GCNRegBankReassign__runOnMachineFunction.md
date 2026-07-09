# libamd_comgr.so.1 gets forever stuck in GCNRegBankReassign::runOnMachineFunction

- **Issue #:** 1381
- **State:** closed
- **Created:** 2021-02-13T21:12:27Z
- **Updated:** 2021-02-15T06:07:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/1381

When I run F@H core_22, or the FAHBench dhfr with double precision test, the code never gets to actually start. It hangs with 100% CPU usage inside this runOnMachineFunction.

You can download FAHBench from https://fahbench.github.io/ and somewhere in there is also a link to its Git source repository.

I used the settings from this screenshot:
![Screenshot from 2021-02-09 14-29-23](https://user-images.githubusercontent.com/18293918/107861746-01431f00-6e05-11eb-8b32-5cee447b8411.png)

The Linux kernel used is 5.10.14-xanmod1. It's Ubuntu 20.04 with HWE, plus XanMod kernel, and the AMD ROCM repositories. It was working with a Vega56 card and is now not working with a 6900 XT card. The new GPU does seem to work with Mesa OpenGL, Vulkan, etc. For example, Steam and Cyberpunk 2077 run with Proton.

GDB backtrace from attaching to a hung process:

> (gdb) bt
#0 0x00007ff131d00e61 in (anonymous namespace)::GCNRegBankReassign::runOnMachineFunction(llvm::MachineFunction&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#1 0x00007ff132a80e18 in llvm::MachineFunctionPass::runOnFunction(llvm::Function&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#2 0x00007ff1356d9e17 in llvm::FPPassManager::runOnFunction(llvm::Function&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#3 0x00007ff135115c61 in (anonymous namespace)::CGPassManager::runOnModule(llvm::Module&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#4 0x00007ff1356d918f in llvm::legacy::PassManagerImpl::run(llvm::Module&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#5 0x00007ff1325de798 in (anonymous namespace)::EmitAssemblyHelper::EmitAssembly(clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) () from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#6 0x00007ff1325e034c in clang::EmitBackendOutput(clang::DiagnosticsEngine&, clang::HeaderSearchOptions const&, clang::CodeGenOptions const&, clang::TargetOptions const&, clang::LangOptions const&, llvm::DataLayout const&, llvm::Module*, clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) () from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#7 0x00007ff13258261e in clang::CodeGenAction::ExecuteAction() [clone .part.331] ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#8 0x00007ff133e8b979 in clang::FrontendAction::Execute() () from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#9 0x00007ff133e49e4b in clang::CompilerInstance::ExecuteAction(clang::FrontendAction&) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#10 0x00007ff132199c7b in clang::ExecuteCompilerInvocation(clang::CompilerInstance*) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#11 0x00007ff13192e642 in COMGR::AMDGPUCompiler::executeInProcessDriver(llvm::ArrayRef<char const*>) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#12 0x00007ff13192f918 in COMGR::AMDGPUCompiler::processFile(char const*, char const*) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#13 0x00007ff13192fe60 in COMGR::AMDGPUCompiler::processFiles(amd_comgr_data_kind_s, char const*) ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#14 0x00007ff131930306 in COMGR::AMDGPUCompiler::codeGenBitcodeToRelocatable() ()
from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#15 0x00007ff131934aa0 in dispatchCompilerAction(amd_comgr_action_kind_s, COMGR::DataAction*, COMGR::DataSet*, COMGR::DataSet*, llvm::raw_ostream&) () from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#16 0x00007ff13193a7c7 in amd_comgr_do_action () from target:/opt/rocm/lib/../opencl/lib/../../lib/libamd_comgr.so.1
#17 0x00007ff137d9f248 in device::Program::compileAndLinkExecutable(amd_comgr_data_set_s, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, amd::option::Options*, char**, unsigned long*) () from target:/opt/rocm/lib/../opencl/lib/libamdocl64.so
#18 0x00007ff137da4eee in device::Program::linkImplLC(amd::option::Options*) () from target:/opt/rocm/lib/../opencl/lib/libamdocl64.so
#19 0x00007ff137da607d in device::Program::build(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*, amd::option::Options*) () from target:/opt/rocm/lib/../opencl/lib/libamdocl64.so
#20 0x00007ff137d5cf92 in amd::Program::build(std::vector<amd::Device*, std::allocator<amd::Device*> > const&, char const*, void (*)(_cl_program*, void*), void*, bool, bool) () from target:/opt/rocm/lib/../opencl/lib/libamdocl64.so
#21 0x00007ff137d2cf93 in clBuildProgram () from target:/opt/rocm/lib/../opencl/lib/libamdocl64.so
#22 0x00007ff12b95c742 in cl::Program::build(std::vector<cl::Device, std::allocator<cl::Device> > const&, char const*, void (*)(_cl_program*, void*), void*) const () from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#23 0x00007ff12b9561df in OpenMM::OpenCLContext::createProgram(std::string, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&, char const*) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#24 0x00007ff12b95157f in OpenMM::OpenCLContext::createProgram(std::string, char const*) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#25 0x00007ff12b981aab in OpenMM::OpenCLIntegrationUtilities::OpenCLIntegrationUtilities(OpenMM::OpenCLContext&, OpenMM::System const&) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#26 0x00007ff12b9510a2 in OpenMM::OpenCLContext::OpenCLContext(OpenMM::System const&, int, int, std::string const&, OpenMM::OpenCLPlatform::PlatformData&, OpenMM::OpenCLContext*) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#27 0x00007ff12baccb40 in OpenMM::OpenCLPlatform::PlatformData::PlatformData(OpenMM::System const&, std::string const&, std::string const&, std::string const&, std::string const&, std::string const&, int, OpenMM::ContextImpl*) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#28 0x00007ff12bacb6e4 in OpenMM::OpenCLPlatform::contextCreated(OpenMM::ContextImpl&, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&) const ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMMOpenCL.so
#29 0x00007ff13d07d5f8 in OpenMM::ContextImpl::ContextImpl(OpenMM::Context&, OpenMM::System const&, OpenMM::Integrator&, OpenMM::Platform*, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&, OpenMM::ContextImpl*) () from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMM.so
#30 0x00007ff13d07a8c4 in OpenMM::Context::Context(OpenMM::System const&, OpenMM::Integrator&, OpenMM::Platform&, std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > > const&) ()
from target:/var/lib/fahclient/cores/cores.foldingathome.org/lin/64bit/22-0.0.13/Core_22.fah/libOpenMM.so
#31 0x0000000000454867 in ?? ()
#32 0x000000000043ea4d in ?? ()
#33 0x000000000047ce7b in ?? ()
#34 0x000000000047d2f5 in ?? ()
#35 0x000000000043e3ce in ?? ()
#36 0x00007ff13cc910b3 in __libc_start_main (main=0x43e3a0, argc=19, argv=0x7ffecb38a8a8, init=<optimized out>, fini=<optimized out>,
rtld_fini=<optimized out>, stack_end=0x7ffecb38a898) at ../csu/libc-start.c:308

clinfo:
> $ clinfo
Number of platforms: 1
Platform Profile: FULL_PROFILE
Platform Version: OpenCL 2.0 AMD-APP (3212.0)
Platform Name: AMD Accelerated Parallel Processing
Platform Vendor: Advanced Micro Devices, Inc.
Platform Extensions: cl_khr_icd cl_amd_event_callback
>
>
>Platform Name: AMD Accelerated Parallel Processing
Number of devices: 1
Device Type: CL_DEVICE_TYPE_GPU
Vendor ID: 1002h
Board name: Device 73bf
Device Topology: PCI[ B#12, D#0, F#0 ]
Max compute units: 40
Max work items dimensions: 3
Max work items[0]: 1024
Max work items[1]: 1024
Max work items[2]: 1024
Max work group size: 256
Preferred vector width char: 4
Preferred vector width short: 2
Preferred vector width int: 1
Preferred vector width long: 1
Preferred vector width float: 1
Preferred vector width double: 1
Native vector width char: 4
Native vector width short: 2
Native vector width int: 1
Native vector width long: 1
Native vector width float: 1
Native vector width double: 1
Max clock frequency: 2660Mhz
Address bits: 64
Max memory allocation: 14588628168
Image support: Yes
Max number of images read arguments: 128
Max number of images write arguments: 8
Max image 2D width: 16384
Max image 2D height: 16384
Max image 3D width: 16384
Max image 3D height: 16384
Max image 3D depth: 8192
Max samplers within kernel: 29631
Max size of kernel argument: 1024
Alignment (bits) of base address: 1024
Minimum alignment (bytes) for any datatype: 128
Single precision floating point capability
Denorms: Yes
Quiet NaNs: Yes
Round to nearest even: Yes
Round to zero: Yes
Round to +ve and infinity: Yes
IEEE754-2008 fused multiply-add: Yes
Cache type: Read/Write
Cache line size: 64
Cache size: 16384
Global memory size: 17163091968
Constant buffer size: 14588628168
Max number of constant args: 8
Local memory type: Scratchpad
Local memory size: 65536
Max pipe arguments: 16
Max pipe active reservations: 16
Max pipe packet size: 1703726280
Max global variable size: 14588628168
Max global variable preferred total size: 17163091968
Max read/write image args: 64
Max on device events: 1024
Queue on device max size: 8388608
Max on device queues: 1
Queue on device preferred size: 262144
SVM capabilities:
Coarse grain buffer: Yes
Fine grain buffer: Yes
Fine grain system: No
Atomics: No
Preferred platform atomic alignment: 0
Preferred global atomic alignment: 0
Preferred local atomic alignment: 0
Kernel Preferred work group size multiple: 32
Error correction support: 0
Unified memory for Host and Device: 0
Profiling timer resolution: 1
Device endianess: Little
Available: Yes
Compiler available: Yes
Execution capabilities:
Execute OpenCL kernels: Yes
Execute native function: No
Queue on Host properties:
Out-of-Order: No
Profiling : Yes
Queue on Device properties:
Out-of-Order: Yes
Profiling : Yes
Platform ID: 0x7f97188e9cf0
Name: gfx1030
Vendor: Advanced Micro Devices, Inc.
Device OpenCL C version: OpenCL C 2.0
Driver version: 3212.0 (HSA1.1,LC)
Profile: FULL_PROFILE
Version: OpenCL 2.0
Extensions: cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

rocminfo:
>$ rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
=====================
HSA System Attributes
=====================
Runtime Version: 1.1
System Timestamp Freq.: 1000.000000MHz
Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model: LARGE
System Endianness: LITTLE
>
>==========
HSA Agents
==========
*******
Agent 1
*******
Name: AMD Ryzen 9 5950X 16-Core Processor
Uuid: CPU-XX
Marketing Name: AMD Ryzen 9 5950X 16-Core Processor
Vendor Name: CPU
Feature: None specified
Profile: FULL_PROFILE
Float Round Mode: NEAR
Max Queue Number: 0(0x0)
Queue Min Size: 0(0x0)
Queue Max Size: 0(0x0)
Queue Type: MULTI
Node: 0
Device Type: CPU
Cache Info:
L1: 32768(0x8000) KB
Chip ID: 0(0x0)
Cacheline Size: 64(0x40)
Max Clock Freq. (MHz): 3400
BDFID: 0
Internal Node ID: 0
Compute Unit: 32
SIMDs per CU: 0
Shader Engines: 0
Shader Arrs. per Eng.: 0
WatchPts on Addr. Ranges:1
Features: None
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: KERNARG, FINE GRAINED
Size: 65834200(0x3ec8cd8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 2
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 65834200(0x3ec8cd8) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
ISA Info:
N/A
*******
Agent 2
*******
Name: gfx1030
Uuid: GPU-XX
Marketing Name: Device 73bf
Vendor Name: AMD
Feature: KERNEL_DISPATCH
Profile: BASE_PROFILE
Float Round Mode: NEAR
Max Queue Number: 128(0x80)
Queue Min Size: 4096(0x1000)
Queue Max Size: 131072(0x20000)
Queue Type: MULTI
Node: 1
Device Type: GPU
Cache Info:
L1: 16(0x10) KB
Chip ID: 29631(0x73bf)
Cacheline Size: 64(0x40)
Max Clock Freq. (MHz): 2660
BDFID: 3072
Internal Node ID: 1
Compute Unit: 80
SIMDs per CU: 4
Shader Engines: 8
Shader Arrs. per Eng.: 2
WatchPts on Addr. Ranges:4
Features: KERNEL_DISPATCH
Fast F16 Operation: FALSE
Wavefront Size: 32(0x20)
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Max Waves Per CU: 64(0x40)
Max Work-item Per CU: 2048(0x800)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 4294967295(0xffffffff)
y 4294967295(0xffffffff)
z 4294967295(0xffffffff)
Max fbarriers/Workgrp: 32
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 16760832(0xffc000) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Alignment: 4KB
Accessible by all: FALSE
Pool 2
Segment: GROUP
Size: 64(0x40) KB
Allocatable: FALSE
Alloc Granule: 0KB
Alloc Alignment: 0KB
Accessible by all: FALSE
ISA Info:
ISA 1
Name: amdgcn-amd-amdhsa--gfx1030
Machine Models: HSA_MACHINE_MODEL_LARGE
Profiles: HSA_PROFILE_BASE
Default Rounding Mode: NEAR
Default Rounding Mode: NEAR
Fast f16: TRUE
Workgroup Max Size: 1024(0x400)
Workgroup Max Size per Dimension:
x 1024(0x400)
y 1024(0x400)
z 1024(0x400)
Grid Max Size: 4294967295(0xffffffff)
Grid Max Size per Dimension:
x 4294967295(0xffffffff)
y 4294967295(0xffffffff)
z 4294967295(0xffffffff)
FBarrier Max Size: 32
*** Done ***