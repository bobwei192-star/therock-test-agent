# [Issue]: Broken Debian 13 required rocm to install outdated packages that are no longer provided

- **Issue #:** 5577
- **State:** closed
- **Created:** 2025-10-27T16:07:20Z
- **Updated:** 2025-10-29T20:03:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/5577

### Problem Description

> [!NOTE]
> I am aware that **Debian 13** is currently not officially supported for the **RX 7800 RX**. [I was recommended](https://github.com/ROCm/ROCm/discussions/2599#discussioncomment-14794484) to report this issue nonetheless, since this should also be a problem for consumers with an **AMD Instinct MI300X GPU**.

I am unable to `sudo apt install rocm` as described in the documentation guide, because some packages do not have the required version. I tried this a few weeks back, so I don't have the complete 

<details>
<summary>
CLI output of trying to install the rocm package.
</summary>

```bash
$ sudo apt install rocm
Installing:                     
  rocm

Installing dependencies:
  amd-smi-lib           lib32stdc++-14-dev           libgeotiff5               libopencv-imgproc-dev       libtbb12               rocblas-dev
  amdgpu-core           lib32ubsan1                  libgl2ps1.4               libopencv-imgproc410        libtbbbind-2-5         rocfft
  comgr                 libaec0                      libgphoto2-dev            libopencv-java              libtbbmalloc2          rocfft-dev
  composablekernel-dev  libamd-comgr2                libhdf4-0-alt             libopencv-ml-dev            libtcl8.6              rocm-cmake
  g++-14-multilib       libamd3                      libhdf5-310               libopencv-ml410             libtesseract5          rocm-core
  g++-multilib          libamdhip64-5                libhdf5-hl-310            libopencv-objdetect-dev     libtk8.6               rocm-dbgapi
  gcc-14-multilib       libarmadillo14               libhsa-runtime64-1        libopencv-objdetect410      libucx0                rocm-debug-agent
  gcc-multilib          libarpack2t64                libhsakmt1                libopencv-photo-dev         libvtk9.3              rocm-developer-tools
  gdal-data             libavcodec-dev               libhwloc-plugins          libopencv-photo410          libx32asan8            rocm-device-libs
  gdal-plugins          libavformat-dev              libhwloc15                libopencv-shape-dev         libx32atomic1          rocm-gdb
  gdb                   libavutil-dev                libibmad5                 libopencv-shape410          libx32gcc-14-dev       rocm-hip
  half                  libbabeltrace1               libibumad3                libopencv-stitching-dev     libx32gcc-s1           rocm-hip-runtime
  hip-dev               libblosc1                    libimath-dev              libopencv-stitching410      libx32gomp1            rocm-hip-runtime-dev
  hip-doc               libc6-dbg                    libipt2                   libopencv-superres-dev      libx32itm1             rocm-language-runtime
  hip-runtime-amd       libc6-dev-i386               libjs-sphinxdoc           libopencv-superres410       libx32quadmath0        rocm-llvm
  hip-samples           libc6-dev-x32                libjs-underscore          libopencv-video-dev         libx32stdc++-14-dev    rocm-opencl
  hipblas               libc6-x32                    libkmlbase1t64            libopencv-video410          libx32stdc++6          rocm-opencl-dev
  hipblas-common-dev    libcamd3                     libkmldom1t64             libopencv-videoio-dev       libx32ubsan1           rocm-opencl-sdk
  hipblas-dev           libccolamd3                  libkmlengine1t64          libopencv-videoio410        libxerces-c3.2t64      rocm-openmp
  hipblaslt             libcfitsio10t64              libleptonica6             libopencv-videostab-dev     libze1                 rocm-smi-lib
  hipblaslt-dev         libcharls2                   libllvm17t64              libopencv-videostab410      mariadb-common         rocminfo
  hipcc                 libcholmod5                  libmariadb3               libopencv-viz-dev           mesa-common-dev        rocprim-dev
  hipcub-dev            libdc1394-dev                libmunge2                 libopencv-viz410            migraphx               rocprofiler
  hipfft                libdebuginfod-common         libnetcdf22               libopencv410-jni            migraphx-dev           rocprofiler-compute
  hipfft-dev            libdebuginfod1t64            libnuma-dev               libopenexr-dev              miopen-hip             rocprofiler-dev
  hipfort-dev           libdrm-amdgpu-amdgpu1        libodbc2                  libopenmpi40                miopen-hip-dev         rocprofiler-plugins
  hipify-clang          libdrm-amdgpu-common         libodbccr2                libpmix2t64                 mivisionx              rocprofiler-register
  hiprand               libdrm-amdgpu-dev            libodbcinst2              libpq5                      mivisionx-dev          rocprofiler-sdk
  hiprand-dev           libdrm-amdgpu-radeon1        libogdi4.1                libproj25                   mysql-common           rocprofiler-sdk-rocpd
  hipsolver             libdrm2-amdgpu               libopencv-calib3d-dev     libpsm2-2                   ocl-icd-opencl-dev     rocprofiler-sdk-roctx
  hipsolver-dev         libelf-dev                   libopencv-calib3d410      libpython3-dev              opencl-c-headers       rocprofiler-systems
  hipsparse             libevent-core-2.1-7t64       libopencv-contrib-dev     libpython3.13-dev           opencl-clhpp-headers   rocrand
  hipsparse-dev         libevent-pthreads-2.1-7t64   libopencv-contrib410      libqhull-r8.0               opencv-data            rocrand-dev
  hipsparselt           libexif-dev                  libopencv-core-dev        libqt5opengl5t64            openmp-extras-dev      rocsolver
  hipsparselt-dev       libexif-doc                  libopencv-core410         libqt5test5t64              openmp-extras-runtime  rocsolver-dev
  hiptensor             libexpat1-dev                libopencv-dev             libraw1394-dev              proj-bin               rocsparse
  hiptensor-dev         libfabric1                   libopencv-dnn-dev         libraw1394-tools            proj-data              rocsparse-dev
  hsa-amd-aqlprofile    libfile-copy-recursive-perl  libopencv-dnn410          librttopo1                  python3-argcomplete    rocthrust-dev
  hsa-rocr              libfile-which-perl           libopencv-features2d-dev  libsocket++1                python3-dev            roctracer
  hsa-rocr-dev          libfreexl1                   libopencv-features2d410   libsource-highlight-common  python3-pip            roctracer-dev
  lib32asan8            libfyba0t64                  libopencv-flann-dev       libsource-highlight4t64     python3.13-dev         rocwmma-dev
  lib32atomic1          libgdal36                    libopencv-flann410        libspatialite8t64           rccl                   rpp
  lib32gcc-14-dev       libgdcm-dev                  libopencv-highgui-dev     libswresample-dev           rccl-dev               rpp-dev
  lib32gomp1            libgdcm3.0t64                libopencv-highgui410      libswscale-dev              rocalution             unixodbc-common
  lib32itm1             libgeos-c1t64                libopencv-imgcodecs-dev   libsz2                      rocalution-dev         valgrind
  lib32quadmath0        libgeos3.13.1                libopencv-imgcodecs410    libtbb-dev                  rocblas

Suggested packages:
  lib32stdc++6-14-dbg   gdbserver    libgeotiff-epsg  libhwloc-contrib-plugins  ogdi-bin        libtbb-doc  mpi-default-bin  opencl-clhpp-headers-doc
  libx32stdc++6-14-dbg  geotiff-bin  libhdf4-alt-dev  odbc-postgresql           opencv-doc      tcl8.6      vtk9-doc         valgrind-mpi
  gdb-doc               gdal-bin     hdf4-tools       tdsodbc                   libraw1394-doc  tk8.6       vtk9-examples    kcachegrind

Summary:
  Upgrading: 0, Installing: 276, Removing: 0, Not Upgrading: 8
  Download size: 441 kB / 5,121 MB
  Space needed: 22.2 GB / 1,333 GB available

Continue? [Y/n] Y
Err:1 http://deb.debian.org/debian trixie/main amd64 mariadb-common all 1:11.8.2-1
  404  Not Found [IP: 2a04:4e42:2::644 80]
Err:2 http://deb.debian.org/debian trixie/main amd64 libmariadb3 amd64 1:11.8.2-1
  404  Not Found [IP: 2a04:4e42:2::644 80]
Err:3 http://deb.debian.org/debian trixie/main amd64 libpq5 amd64 17.5-1
  404  Not Found [IP: 2a04:4e42:2::644 80]
Error: Failed to fetch http://deb.debian.org/debian/pool/main/m/mariadb/mariadb-common_11.8.2-1_all.deb  404  Not Found [IP: 2a04:4e42:2::644 80]
Error: Failed to fetch http://deb.debian.org/debian/pool/main/m/mariadb/libmariadb3_11.8.2-1_amd64.deb  404  Not Found [IP: 2a04:4e42:2::644 80]
Error: Failed to fetch http://deb.debian.org/debian/pool/main/p/postgresql-17/libpq5_17.5-1_amd64.deb  404  Not Found [IP: 2a04:4e42:2::644 80]
Error: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```
</details>

### Operating System

Debian 13 (trixie)

### CPU

AMD Ryzen 7 7800X3D 8-Core Processor

### GPU

AMD Radeon RX 7800 XT

### ROCm Version

ROCm 7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

Follow [the installation guide for Debian 13, described at rocmdocs.amd.com](https://rocmdocs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#rocm-installation)

```bash
wget https://repo.radeon.com/amdgpu-install/7.0.2/ubuntu/noble/amdgpu-install_7.0.2.70002-1_all.deb
sudo apt install ./amdgpu-install_7.0.2.70002-1_all.deb
sudo apt update
sudo apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm # fails
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

`rocminfo` was installed with `sudo apt install rocminfo` before. It caused issues while following the setup guide, so I removed those packages Debian provides. There should no longer be any of those Debian provided rocm packages on my system, as filtering `apt list` on "rocm" doesn't produce any matches. Feel free to ask me on other filters.

```bash
apt list --installed | grep rocm

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
```