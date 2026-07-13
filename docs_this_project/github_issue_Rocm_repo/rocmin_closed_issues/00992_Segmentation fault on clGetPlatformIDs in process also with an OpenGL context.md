# Segmentation fault on clGetPlatformIDs in process also with an OpenGL context

- **Issue #:** 992
- **State:** closed
- **Created:** 2020-01-03T22:14:34Z
- **Updated:** 2020-04-30T10:46:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/992

I'm using ROCm 3.0 on NixOS via [this repository](https://github.com/nixos-rocm/nixos-rocm).  While NixOS is a strange distribution, ROCm has not been unusually patched from what I can see, so while the paths will look strange in the following, the actual functionality should be the same as upstream.

I have an odd issue where OpenCL via ROCm works fine, *unless* I try to initialise it in a process that has also initialised OpenGL.  For example, the following program segfaults on the `clGetPlatformIDs()` call:

```
#include <GL/glut.h>
#include <CL/cl.h>
#include <assert.h>

int main(int argc, char *argv[]) {
  glutInit(&argc, argv);

  cl_int err;
  cl_platform_id platform;
  err = clGetPlatformIDs(1, &platform, NULL);
  assert(err == CL_SUCCESS);

  return 0;
}
```

The backtrace is the following:

```
Thread 1 "glut" received signal SIGSEGV, Segmentation fault.
0x00007fff925cbcad in llvm::TargetPassConfig::addPass(llvm::Pass*, bool, bool) () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
(gdb) bt
#0  0x00007fff925cbcad in llvm::TargetPassConfig::addPass(llvm::Pass*, bool, bool) () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#1  0x00007fff925ce908 in llvm::TargetPassConfig::addRegAssignmentOptimized() () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#2  0x00007fff925cec94 in llvm::TargetPassConfig::addOptimizedRegAlloc() () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#3  0x00007fff925cf1d6 in llvm::TargetPassConfig::addMachinePasses() () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#4  0x00007fff92367d01 in addPassesToGenerateCode(llvm::LLVMTargetMachine&, llvm::legacy::PassManagerBase&, bool, llvm::MachineModuleInfoWrapperPass&) () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#5  0x00007fff9236d4fd in llvm::LLVMTargetMachine::addPassesToEmitFile(llvm::legacy::PassManagerBase&, llvm::raw_pwrite_stream&, llvm::raw_pwrite_stream*, llvm::CodeGenFileType, bool, llvm::MachineModuleInfoWrapperPass*) () from /nix/store/j4mq693adgd5v1svv84qkz4rnvdrbpgb-rocm-llvm-lib/lib/libLLVM-10git.so
#6  0x00007fff954cac9e in (anonymous namespace)::EmitAssemblyHelper::AddEmitPasses(llvm::legacy::PassManager&, clang::BackendAction, llvm::raw_pwrite_stream&, llvm::raw_pwrite_stream*) [clone .constprop.1066] () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#7  0x00007fff954cf22a in (anonymous namespace)::EmitAssemblyHelper::EmitAssembly(clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#8  0x00007fff954d0ef4 in clang::EmitBackendOutput(clang::DiagnosticsEngine&, clang::HeaderSearchOptions const&, clang::CodeGenOptions const&, clang::TargetOptions const&, clang::LangOptions const&, llvm::DataLayout const&, llvm::Module*, clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) ()
   from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#9  0x00007fff954a8f40 in clang::CodeGenAction::ExecuteAction() () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#10 0x00007fff960331f1 in clang::FrontendAction::Execute() () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#11 0x00007fff95ff76f3 in clang::CompilerInstance::ExecuteAction(clang::FrontendAction&) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#12 0x00007fff952c27db in clang::ExecuteCompilerInvocation(clang::CompilerInstance*) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#13 0x00007fff9527a3cd in COMGR::InProcessDriver::execute(llvm::ArrayRef<char const*>) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#14 0x00007fff952807c6 in COMGR::AMDGPUCompiler::processFile(char const*, char const*) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#15 0x00007fff95280c14 in COMGR::AMDGPUCompiler::processFiles(amd_comgr_data_kind_s, char const*) () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#16 0x00007fff952bd70f in amd_comgr_do_action () from /nix/store/c52nnmr5z8qjv2q7mqdykv4rxf40xl7l-comgr-3.0.0/lib/libamd_comgr.so.1
#17 0x00007fffe847a338 in device::Program::compileAndLinkExecutable(amd_comgr_data_set_s, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, amd::option::Options*, char**, unsigned long*) ()
   from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#18 0x00007fffe847e2f8 in device::Program::linkImplLC(amd::option::Options*) () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#19 0x00007fffe8481029 in device::Program::build(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*, amd::option::Options*) () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#20 0x00007fffe8492015 in amd::Program::build(std::vector<amd::Device*, std::allocator<amd::Device*> > const&, char const*, void (*)(_cl_program*, void*), void*, bool) () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#21 0x00007fffe84683cf in amd::Device::BlitProgram::create(amd::Device*, char const*, char const*) () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#22 0x00007fffe84b0dee in roc::Device::create(bool) () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#23 0x00007fffe84b0243 in roc::Device::init() () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#24 0x00007fffe846855c in amd::Device::init() () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#25 0x00007fffe8489ec2 in amd::Runtime::init() () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#26 0x00007fffe846234a in std::call_once<clIcdGetPlatformIDsKHR::$_0>(std::once_flag&, clIcdGetPlatformIDsKHR::$_0&&)::{lambda()#2}::__invoke() () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#27 0x00007ffff7c9d9c9 in __pthread_once_slow () from /nix/store/qn76sklvyalzw9ilnxz6sh0020gl2qn6-glibc-2.27/lib/libpthread.so.0
#28 0x00007fffe84622b0 in clIcdGetPlatformIDsKHR () from /nix/store/77897wl9gs9xv4qg927z0x93drfy8pag-rocm-opencl-runtime-3.0.0/lib/x86_64/libamdocl64.so
#29 0x00007ffff7fc92e1 in khrIcdVendorAdd () from /nix/store/cb6138amx915ww5syssyv61drq2xn5n0-rocm-opencl-runtime-3.0.0/lib/x86_64/libOpenCL.so.1
#30 0x00007ffff7fcb04a in khrIcdOsVendorsEnumerate () from /nix/store/cb6138amx915ww5syssyv61drq2xn5n0-rocm-opencl-runtime-3.0.0/lib/x86_64/libOpenCL.so.1
#31 0x00007ffff7c9d9c9 in __pthread_once_slow () from /nix/store/qn76sklvyalzw9ilnxz6sh0020gl2qn6-glibc-2.27/lib/libpthread.so.0
#32 0x00007ffff7fc9591 in clGetPlatformIDs () from /nix/store/cb6138amx915ww5syssyv61drq2xn5n0-rocm-opencl-runtime-3.0.0/lib/x86_64/libOpenCL.so.1
#33 0x00000000004010a3 in main (argc=<optimized out>, argv=<optimized out>) at glut.c:10
```

Interestingly, if I do the OpenCL initialisation first, then it is the call to `glutInit()` that fails, but with a similar stack trace:

```
Thread 1 "glut" received signal SIGSEGV, Segmentation fault.
0x00007ffee30ef4fd in llvm::TargetPassConfig::addPass(llvm::Pass*, bool, bool) () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
(gdb) bt
#0  0x00007ffee30ef4fd in llvm::TargetPassConfig::addPass(llvm::Pass*, bool, bool) () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#1  0x00007ffee30f2138 in llvm::TargetPassConfig::addRegAssignmentOptimized() () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#2  0x00007ffee30f24c4 in llvm::TargetPassConfig::addOptimizedRegAlloc() () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#3  0x00007ffee30f2a5e in llvm::TargetPassConfig::addMachinePasses() () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#4  0x00007ffee2eab841 in addPassesToGenerateCode(llvm::LLVMTargetMachine&, llvm::legacy::PassManagerBase&, bool, llvm::MachineModuleInfo&) () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#5  0x00007ffee2eafd0d in llvm::LLVMTargetMachine::addPassesToEmitFile(llvm::legacy::PassManagerBase&, llvm::raw_pwrite_stream&, llvm::raw_pwrite_stream*, llvm::TargetMachine::CodeGenFileType, bool, llvm::MachineModuleInfo*) () from /nix/store/hzk4k1lpp5qcsfm5y940sgjx60v0mgf2-llvm-9.0.0-lib/lib/libLLVM-9.so
#6  0x00007ffee70399bf in ac_create_llvm_passes () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#7  0x00007ffee6f816ba in si_init_compiler () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#8  0x00007ffee6f83aa2 in radeonsi_screen_create_impl () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#9  0x00007ffee6fff5cc in amdgpu_winsys_create () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#10 0x00007ffee6f84211 in radeonsi_screen_create () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#11 0x00007ffee6dc9076 in pipe_radeonsi_create_screen () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#12 0x00007ffee6e69c48 in pipe_loader_create_screen () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#13 0x00007ffee6dcd55b in dri2_init_screen () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#14 0x00007ffee6dca7a6 in driCreateNewScreen2 () from /run/opengl-driver/lib/dri/radeonsi_dri.so
#15 0x00007fffefda901a in dri3_create_screen () from /run/opengl-driver/lib/libGLX_mesa.so.0
#16 0x00007fffefd95ad9 in __glXInitialize () from /run/opengl-driver/lib/libGLX_mesa.so.0
#17 0x00007fffefd91224 in GetGLXPrivScreenConfig () from /run/opengl-driver/lib/libGLX_mesa.so.0
#18 0x00007fffefd9178d in glXQueryExtensionsString () from /run/opengl-driver/lib/libGLX_mesa.so.0
#19 0x00007ffff7f047fe in fgPlatformInitialize () from /nix/store/fnh3vij5aj7hy6mr4awcxwniynkczpqn-freeglut-3.0.0/lib/libglut.so.3
#20 0x00007ffff7efaa8c in glutInit () from /nix/store/fnh3vij5aj7hy6mr4awcxwniynkczpqn-freeglut-3.0.0/lib/libglut.so.3
#21 0x00000000004010ae in main (argc=<optimized out>, argv=0x7fffffffd5d8) at glut.c:11
```

I'm not even sure that ROCm is at fault here, since the `radeonsi_dri.so` driver is from Mesa.

It's not a GLUT-specific problem, because the same segmentation fault occurs when using SDL.