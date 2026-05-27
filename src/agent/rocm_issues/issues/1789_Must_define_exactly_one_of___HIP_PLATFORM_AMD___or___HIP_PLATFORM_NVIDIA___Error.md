# Must define exactly one of __HIP_PLATFORM_AMD__ or __HIP_PLATFORM_NVIDIA__ Error

> **Issue #1789**
> **状态**: closed
> **创建时间**: 2022-08-18T21:00:51Z
> **更新时间**: 2022-08-19T14:47:37Z
> **关闭时间**: 2022-08-19T14:47:37Z
> **作者**: nicolemarsaglia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1789

## 描述

Hello, I am currently building on Crusher where I am linking Kokkos and Kokkos Kernels to a Ascent+Genten+VTKm build and I am encountering the following error in when I am building Ascent (all other libraries build and install): 

/opt/rocm-5.2.0/include/hip/hip_runtime.h:66:2: error: ("Must define exactly one of __HIP_PLATFORM_AMD__ or __HIP_PLATFORM_NVIDIA__");
#error("Must define exactly one of __HIP_PLATFORM_AMD__ or __HIP_PLATFORM_NVIDIA__");

I have encountered this error in two different builds: one that uses the cray compilers and one using amdclang. 

I've attached txt files of my scripts so you can see the compiler variables I set. 

If you need anymore information please let me know. Any help would be very appreciated!


Here is the verbose build line:
[ 40%] Building CXX object ascent/CMakeFiles/ascent.dir/runtimes/flow_filters/ascent_runtime_genten_filters.cpp.o
cd /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/build/ascent && /opt/rocm-5.2.0/bin/..//bin/amdclang++ -DASCENT_EXPORTS_FLAG -DHAVE_ROCBLAS -DHAVE_ROCSOLVER -DVTKMDIY_MPI_AS_LIB -DVTKMDIY_NO_THREADS -Dascent_EXPORTS -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/thirdparty_builtin/lodepng -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/thirdparty_builtin/tiny_obj -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/build/ascent -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/utils -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/runtimes -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/hola -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/flow -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/build/flow -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/flow/filters -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/runtimes/flow_filters -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/rover -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/genten-gitlab/install/include/genten -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/libs -I/gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/build/libs -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8/vtkm/thirdparty/lcl/vtkmlcl -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8/vtkm/thirdparty/diy/vtkmdiy/include -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/conduit-v0.8.3/install/include -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/conduit-v0.8.3/install/include/conduit -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8 -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8/vtkm/thirdparty/optionparser -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8/vtkm/thirdparty/diy -isystem /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/vtk-m-v1.8.0/install/include/vtkm-1.8/vtkm/thirdparty/diy/vtkmdiy/include/vtkmdiy/mpi -I/opt/rocm-5.2.0/include -Wno-pass-failed -I/opt/cray/pe/mpich/8.1.16/ofi/amd/5.0/include    -O3 -DNDEBUG -fPIC -fvisibility=hidden -ffunction-sections -std=c++14 -MD -MT ascent/CMakeFiles/ascent.dir/runtimes/flow_filters/ascent_runtime_genten_filters.cpp.o -MF CMakeFiles/ascent.dir/runtimes/flow_filters/ascent_runtime_genten_filters.cpp.o.d -o CMakeFiles/ascent.dir/runtimes/flow_filters/ascent_runtime_genten_filters.cpp.o -c /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/runtimes/flow_filters/ascent_runtime_genten_filters.cpp
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/ascent-v0.9.0-pre/src/ascent/runtimes/flow_filters/ascent_runtime_genten_filters.cpp:27:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/genten-gitlab/install/include/genten/Genten_ComputePrincipalKurtosisVectors.hpp:41:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include/Kokkos_Core.hpp:51:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include/Kokkos_Core_fwd.hpp:52:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include/Kokkos_Macros.hpp:110:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include/KokkosCore_Config_SetupBackend.hpp:47:
In file included from /gpfs/alpine/scratch/nic8504/csc340/2022_08_kokkos_genten_ascent/ascent-crusher-build-scripts/kokkos-3.6.01/install/include/setup/Kokkos_Setup_HIP.hpp:53:
/opt/rocm-5.2.0/include/hip/hip_runtime.h:66:2: error: ("Must define exactly one of __HIP_PLATFORM_AMD__ or __HIP_PLATFORM_NVIDIA__");
#error("Must define exactly one of __HIP_PLATFORM_AMD__ or __HIP_PLATFORM_NVIDIA__");
[amdclang_build.txt](https://github.com/RadeonOpenCompute/ROCm/files/9377647/amdclang_build.txt)
[cray_build.txt](https://github.com/RadeonOpenCompute/ROCm/files/9377648/cray_build.txt)



---

## 评论 (2 条)

### 评论 #1 — abbotts (2022-08-18T21:07:37Z)

@nicolemarsaglia , try adding `-D__HIP_PLATFORM_AMD__` to both your `CFLAGS` and your `CXXFLAGS`. This is needed so the HIP headers know you're building for the AMD runtime (rather than trying to target CUDA).

As a general FYI, if you run into issues on Crusher or Frontier you're more likely to get machine specific help using the OLCF support system at https://www.olcf.ornl.gov/for-users/getting-started/submit-ticket/

---

### 评论 #2 — nicolemarsaglia (2022-08-19T14:47:37Z)

Thanks, that worked!

---
