# [Issue]: rocminfo fails with HSA_STATUS_ERROR_OUT_OF_RESOURCES under WSL oracleLinux

- **Issue #:** 3561
- **State:** closed
- **Created:** 2024-08-10T15:54:15Z
- **Updated:** 2025-11-05T19:29:38Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3561

### Problem Description

```
> sudo rocminfo

WSL environment detected.
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1306
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
```
> uname -m && cat /etc/*release

x86_64
Oracle Linux Server release 9.4
NAME="Oracle Linux Server"
VERSION="9.4"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="9.4"
PLATFORM_ID="platform:el9"
PRETTY_NAME="Oracle Linux Server 9.4"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:oracle:linux:9:4:server"
HOME_URL="https://linux.oracle.com/"
BUG_REPORT_URL="https://github.com/oracle/oracle-linux"

ORACLE_BUGZILLA_PRODUCT="Oracle Linux 9"
ORACLE_BUGZILLA_PRODUCT_VERSION=9.4
ORACLE_SUPPORT_PRODUCT="Oracle Linux"
ORACLE_SUPPORT_PRODUCT_VERSION=9.4
Red Hat Enterprise Linux release 9.4 (Plow)
Oracle Linux Server release 9.4
```
```
> yum list installed | grep -i -e 'rocm' -i -e 'amd'

amd-smi-lib.x86_64                             24.6.2.60200-66.el9              @ROCm-6.2
amdgpu-core.noarch                             1:6.2.60200-2009582.el9          @amdgpu
amdgpu-dkms.noarch                             1:6.8.5.60200-2009582.el9        @amdgpu
amdgpu-dkms-firmware.noarch                    1:6.8.5.60200-2009582.el9        @amdgpu
comgr.x86_64                                   2.8.0.60200-66.el9               @ROCm-6.2
composablekernel-devel.x86_64                  1.1.0.60200-66.el9               @ROCm-6.2
dkms.noarch                                    3.0.13-1.el9                     @amdgpu
half.x86_64                                    1.12.0.60200-66.el9              @ROCm-6.2
hip-devel.x86_64                               6.2.41133.60200-66.el9           @ROCm-6.2
hip-doc.x86_64                                 6.2.41133.60200-66.el9           @ROCm-6.2
hip-runtime-amd.x86_64                         6.2.41133.60200-66.el9           @ROCm-6.2
hip-samples.x86_64                             6.2.41133.60200-66.el9           @ROCm-6.2
hipblas.x86_64                                 2.2.0.60200-66.el9               @ROCm-6.2
hipblas-devel.x86_64                           2.2.0.60200-66.el9               @ROCm-6.2
hipblaslt.x86_64                               0.8.0.60200-66.el9               @ROCm-6.2
hipblaslt-devel.x86_64                         0.8.0.60200-66.el9               @ROCm-6.2
hipcc.x86_64                                   1.1.1.60200-66.el9               @ROCm-6.2
hipcub-devel.x86_64                            3.2.0.60200-66.el9               @ROCm-6.2
hipfft.x86_64                                  1.0.14.60200-66.el9              @ROCm-6.2
hipfft-devel.x86_64                            1.0.14.60200-66.el9              @ROCm-6.2
hipfort-devel.x86_64                           0.4.0.60200-66.el9               @ROCm-6.2
hipify-clang.x86_64                            18.0.0.60200-66.el9              @ROCm-6.2
hiprand.x86_64                                 2.11.0.60200-66.el9              @ROCm-6.2
hiprand-devel.x86_64                           2.11.0.60200-66.el9              @ROCm-6.2
hipsolver.x86_64                               2.2.0.60200-66.el9               @ROCm-6.2
hipsolver-devel.x86_64                         2.2.0.60200-66.el9               @ROCm-6.2
hipsparse.x86_64                               3.1.1.60200-66.el9               @ROCm-6.2
hipsparse-devel.x86_64                         3.1.1.60200-66.el9               @ROCm-6.2
hipsparselt.x86_64                             0.2.1.60200-66.el9               @ROCm-6.2
hipsparselt-devel.x86_64                       0.2.1.60200-66.el9               @ROCm-6.2
hiptensor.x86_64                               1.3.0.60200-66.el9               @ROCm-6.2
hiptensor-devel.x86_64                         1.3.0.60200-66.el9               @ROCm-6.2
hsa-amd-aqlprofile.x86_64                      1.0.0.60200.60200-66.el9         @ROCm-6.2
hsa-rocr.x86_64                                1.14.0.60200-66.el9              @ROCm-6.2
hsa-rocr-devel.x86_64                          1.14.0.60200-66.el9              @ROCm-6.2
hsakmt-roct-devel.x86_64                       20240607.3.8.60200-66.el9        @ROCm-6.2
libdrm-amdgpu.x86_64                           1:2.4.120.60200-2009582.el9      @amdgpu
libdrm-amdgpu-common.noarch                    1.0.0.60200-2009582.el9          @amdgpu
libdrm-amdgpu-devel.x86_64                     1:2.4.120.60200-2009582.el9      @amdgpu
libva-amdgpu.x86_64                            2.16.0.60200-2009582.el9         @amdgpu
libvdpau-amdgpu.x86_64                         6.2-2009582.el9                  @amdgpu
libwayland-amdgpu-client.x86_64                1.22.0.60200-2009582.el9         @amdgpu
libwayland-amdgpu-cursor.x86_64                1.22.0.60200-2009582.el9         @amdgpu
libwayland-amdgpu-egl.x86_64                   1.22.0.60200-2009582.el9         @amdgpu
libwayland-amdgpu-server.x86_64                1.22.0.60200-2009582.el9         @amdgpu
llvm-amdgpu-libs.x86_64                        1:18.1.60200-2009582.el9         @amdgpu
mesa-amdgpu-dri-drivers.x86_64                 1:24.2.0.60200-2009582.el9       @amdgpu
mesa-amdgpu-filesystem.x86_64                  1:24.2.0.60200-2009582.el9       @amdgpu
mesa-amdgpu-libGL.x86_64                       1:24.2.0.60200-2009582.el9       @amdgpu
mesa-amdgpu-va-drivers.x86_64                  1:24.2.0.60200-2009582.el9       @amdgpu
migraphx.x86_64                                2.10.0.60200-66.el9              @ROCm-6.2
migraphx-devel.x86_64                          2.10.0.60200-66.el9              @ROCm-6.2
miopen-hip.x86_64                              3.2.0.60200-66.el9               @ROCm-6.2
miopen-hip-devel.x86_64                        3.2.0.60200-66.el9               @ROCm-6.2
mivisionx.x86_64                               3.0.0.60200-66                   @ROCm-6.2
mivisionx-devel.x86_64                         3.0.0.60200-66                   @ROCm-6.2
omnitrace.x86_64                               1.11.2.60200-66.el9              @ROCm-6.2
openmp-extras-devel.x86_64                     18.62.0.60200-66.el9             @ROCm-6.2
openmp-extras-runtime.x86_64                   18.62.0.60200-66.el9             @ROCm-6.2
rccl.x86_64                                    2.20.5.60200-66.el9              @ROCm-6.2
rccl-devel.x86_64                              2.20.5.60200-66.el9              @ROCm-6.2
rocalution.x86_64                              3.2.0.60200-66.el9               @ROCm-6.2
rocalution-devel.x86_64                        3.2.0.60200-66.el9               @ROCm-6.2
rocblas.x86_64                                 4.2.0.60200-66.el9               @ROCm-6.2
rocblas-devel.x86_64                           4.2.0.60200-66.el9               @ROCm-6.2
rocdecode.x86_64                               0.6.0.60200-66                   @ROCm-6.2
rocdecode-devel.x86_64                         0.6.0.60200-66                   @ROCm-6.2
rocfft.x86_64                                  1.0.28.60200-66.el9              @ROCm-6.2
rocfft-devel.x86_64                            1.0.28.60200-66.el9              @ROCm-6.2
rocm.x86_64                                    6.2.0.60200-66.el9               @ROCm-6.2
rocm-cmake.x86_64                              0.13.0.60200-66.el9              @ROCm-6.2
rocm-core.x86_64                               6.2.0.60200-66.el9               @ROCm-6.2
rocm-dbgapi.x86_64                             0.76.0.60200-66.el9              @ROCm-6.2
rocm-debug-agent.x86_64                        2.0.3.60200-66.el9               @ROCm-6.2
rocm-dev.x86_64                                6.2.0.60200-66.el9               @ROCm-6.2
rocm-developer-tools.x86_64                    6.2.0.60200-66.el9               @ROCm-6.2
rocm-device-libs.x86_64                        1.0.0.60200-66.el9               @ROCm-6.2
rocm-gdb.x86_64                                14.2.60200-66.el9                @ROCm-6.2
rocm-hip-libraries.x86_64                      6.2.0.60200-66.el9               @ROCm-6.2
rocm-hip-runtime.x86_64                        6.2.0.60200-66.el9               @ROCm-6.2
rocm-hip-runtime-devel.x86_64                  6.2.0.60200-66.el9               @ROCm-6.2
rocm-hip-sdk.x86_64                            6.2.0.60200-66.el9               @ROCm-6.2
rocm-language-runtime.x86_64                   6.2.0.60200-66.el9               @ROCm-6.2
rocm-llvm.x86_64                               18.0.0.24292.60200-66.el9        @ROCm-6.2
rocm-ml-libraries.x86_64                       6.2.0.60200-66.el9               @ROCm-6.2
rocm-ml-sdk.x86_64                             6.2.0.60200-66.el9               @ROCm-6.2
rocm-opencl.x86_64                             2.0.0.60200-66.el9               @ROCm-6.2
rocm-opencl-devel.x86_64                       2.0.0.60200-66.el9               @ROCm-6.2
rocm-opencl-icd-loader.x86_64                  1.2.60200-66.el9                 @ROCm-6.2
rocm-opencl-runtime.x86_64                     6.2.0.60200-66.el9               @ROCm-6.2
rocm-opencl-sdk.x86_64                         6.2.0.60200-66.el9               @ROCm-6.2
rocm-openmp-sdk.x86_64                         6.2.0.60200-66.el9               @ROCm-6.2
rocm-smi-lib.x86_64                            7.3.0.60200-66.el9               @ROCm-6.2
rocm-utils.x86_64                              6.2.0.60200-66.el9               @ROCm-6.2
rocminfo.x86_64                                1.0.0.60200-66.el9               @ROCm-6.2
rocprim-devel.x86_64                           3.2.0.60200-66.el9               @ROCm-6.2
rocprofiler.x86_64                             2.0.60200.60200-66.el9           @ROCm-6.2
rocprofiler-devel.x86_64                       2.0.60200.60200-66.el9           @ROCm-6.2
rocprofiler-plugins.x86_64                     2.0.60200.60200-66.el9           @ROCm-6.2
rocprofiler-register.x86_64                    0.4.0.60200-66.el9               @ROCm-6.2
rocprofiler-sdk.x86_64                         0.4.0-66.el9                     @ROCm-6.2
rocprofiler-sdk-roctx.x86_64                   0.4.0-66.el9                     @ROCm-6.2
rocrand.x86_64                                 3.1.0.60200-66.el9               @ROCm-6.2
rocrand-devel.x86_64                           3.1.0.60200-66.el9               @ROCm-6.2
rocsolver.x86_64                               3.26.0.60200-66.el9              @ROCm-6.2
rocsolver-devel.x86_64                         3.26.0.60200-66.el9              @ROCm-6.2
rocsparse.x86_64                               3.2.0.60200-66.el9               @ROCm-6.2
rocsparse-devel.x86_64                         3.2.0.60200-66.el9               @ROCm-6.2
rocthrust-devel.x86_64                         3.0.1.60200-66.el9               @ROCm-6.2
roctracer.x86_64                               4.1.60200.60200-66.el9           @ROCm-6.2
roctracer-devel.x86_64                         4.1.60200.60200-66.el9           @ROCm-6.2
rocwmma-devel.x86_64                           1.5.0.60200-66.el9               @ROCm-6.2
rpp.x86_64                                     1.8.0.60200-66.el9               @ROCm-6.2
rpp-devel.x86_64                               1.8.0.60200-66.el9               @ROCm-6.2
wayland-amdgpu-devel.x86_64                    1.22.0.60200-2009582.el9         @amdgpu
```

### Operating System

Oracle Linux Server 9.4 (WSL2)

### CPU

AMD Ryzen 7 7800X3D 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

sudo rocminfo

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

WSL environment detected.
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1306
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

### Additional Information

_No response_