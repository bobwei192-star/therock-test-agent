# [Issue]: Rocm 7.1.1 on Ubuntu 24.04 64bit env may install 32bit libraries

- **Issue #:** 5806
- **State:** closed
- **Created:** 2025-12-20T05:01:17Z
- **Updated:** 2026-03-02T19:30:47Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5806

### Problem Description

Why is RoCM install on a 64bit system bundling and requring 32bit libraries? Can we remove these as the pkg 24GB total install is already on the very large side and should be trimmed as much as possible.

### Operating System

Ubuntu 24.04

### CPU

AMD Milan

### GPU

AMD Radeon 7900XTX

### ROCm Version

RoCM 7.1.1

### Additional Information

```
server:/$ dpkg --print-architecture
amd64
server:/$ dpkg --print-foreign-architectures
[empty]
server:/$ sudo apt list | grep installed | grep i386
[empty]
```

```
apt install rocm
```

```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  amd-smi-lib amdgpu-core comgr composablekernel-dev g++-13-multilib g++-multilib gcc-13-multilib gcc-multilib gdal-data gdal-plugins half hip-dev hip-doc hip-runtime-amd hip-samples hipblas hipblas-common-dev hipblas-dev hipblaslt
  hipblaslt-dev hipcc hipcub-dev hipfft hipfft-dev hipfort-dev hipify-clang hiprand hiprand-dev hipsolver hipsolver-dev hipsparse hipsparse-dev hipsparselt hipsparselt-dev hiptensor hiptensor-dev hsa-amd-aqlprofile hsa-rocr
  hsa-rocr-dev i965-va-driver icu-devtools intel-media-va-driver lib32asan8 lib32atomic1 lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32quadmath0 lib32stdc++-13-dev lib32stdc++6 lib32ubsan1 libaacs0 libaec0 libamd3 libaom3
  libarmadillo12 libarpack2t64 libavcodec-dev libavcodec60 libavformat-dev libavformat60 libavutil-dev libavutil58 libbdplus0 libblas3 libblosc1 libbluray2 libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libcamd3 libccolamd3
  libcfitsio10t64 libcharls2 libcholmod5 libchromaprint1 libcjson1 libcodec2-1.2 libcolamd3 libdav1d7 libdc1394-25 libdc1394-dev libde265-0 libdeflate-dev libdouble-conversion3 libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common
  libdrm-amdgpu-dev libdrm-amdgpu-radeon1 libdrm2-amdgpu libexif-dev libexif-doc libfile-copy-recursive-perl libfile-which-perl libfreexl1 libfyba0t64 libgd3 libgdal34t64 libgdcm-dev libgdcm3.0t64 libgeos-c1t64 libgeos3.12.1t64
  libgeotiff5 libgl2ps1.4 libglew2.2 libgme0 libgphoto2-6t64 libgphoto2-dev libgphoto2-l10n libgphoto2-port12t64 libgsm1 libhdf4-0-alt libhdf5-103-1t64 libhdf5-hl-100t64 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwy1t64 libicu-dev libigdgmm12 libimath-dev libinput-bin libinput10 libjbig-dev libjpeg-dev libjpeg-turbo8-dev libjpeg8-dev libjsoncpp25 libjxl0.7 libkmlbase1t64 libkmldom1t64 libkmlengine1t64
  liblapack3 liblept5 liblerc-dev liblzma-dev libmbedcrypto7t64 libmd4c0 libminizip1t64 libmp3lame0 libmpg123-0t64 libmtdev1t64 libncurses-dev libnetcdf19t64 libnorm1t64 libodbc2 libodbcinst2 libogdi4.1 libopencv-calib3d-dev
  libopencv-calib3d406t64 libopencv-contrib-dev libopencv-contrib406t64 libopencv-core-dev libopencv-core406t64 libopencv-dev libopencv-dnn-dev libopencv-dnn406t64 libopencv-features2d-dev libopencv-features2d406t64
  libopencv-flann-dev libopencv-flann406t64 libopencv-highgui-dev libopencv-highgui406t64 libopencv-imgcodecs-dev libopencv-imgcodecs406t64 libopencv-imgproc-dev libopencv-imgproc406t64 libopencv-java libopencv-ml-dev
  libopencv-ml406t64 libopencv-objdetect-dev libopencv-objdetect406t64 libopencv-photo-dev libopencv-photo406t64 libopencv-shape-dev libopencv-shape406t64 libopencv-stitching-dev libopencv-stitching406t64 libopencv-superres-dev
  libopencv-superres406t64 libopencv-video-dev libopencv-video406t64 libopencv-videoio-dev libopencv-videoio406t64 libopencv-videostab-dev libopencv-videostab406t64 libopencv-viz-dev libopencv-viz406t64 libopencv406-jni
  libopenexr-dev libopenmpt0t64 libpcre2-16-0 libpgm-5.3-0t64 libpng-dev libpng-tools libproj25 libprotobuf32t64 libqhull-r8.0 libqt5core5t64 libqt5dbus5t64 libqt5gui5t64 libqt5network5t64 libqt5opengl5t64 libqt5qml5
  libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5test5t64 libqt5waylandclient5 libqt5waylandcompositor5 libqt5widgets5t64 librabbitmq4 librav1e0 libraw1394-11 libraw1394-dev libraw1394-tools librist4 librttopo1 libsharpyuv-dev
  libshine3 libsnappy1v5 libsocket++1 libsodium23 libsoxr0 libspatialite8t64 libspeex1 libsrt1.5-gnutls libssh-gcrypt-4 libsuitesparseconfig7 libsuperlu6 libsvtav1enc1d1 libswresample-dev libswresample4 libswscale-dev libswscale7
  libsz2 libtbb-dev libtbb12 libtbbbind-2-5 libtbbmalloc2 libtesseract5 libtiff-dev libtiffxx6 libtwolame0 libudfread0 liburiparser1 libva-drm2 libva-x11-2 libva2 libvorbisfile3 libvpl2 libvpx9 libvtk9.1t64 libwacom-common
  libwacom9 libwebp-dev libwebpdecoder3 libx265-199 libx32asan8 libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxerces-c3.2t64 libxml2-dev
  libxvidcore4 libzmq5 libzvbi-common libzvbi0t64 mesa-common-dev mesa-va-drivers migraphx migraphx-dev miopen-hip miopen-hip-dev mivisionx mivisionx-dev ocl-icd-opencl-dev opencl-c-headers opencl-clhpp-headers opencv-data
  openmp-extras-dev openmp-extras-runtime proj-bin proj-data python3-argcomplete qt5-gtk-platformtheme qttranslations5-l10n qtwayland5 rccl rccl-dev rocalution rocalution-dev rocblas rocblas-dev rocfft rocfft-dev rocm-cmake
  rocm-core rocm-dbgapi rocm-debug-agent rocm-developer-tools rocm-device-libs rocm-gdb rocm-hip rocm-language-runtime rocm-llvm rocm-opencl rocm-opencl-dev rocm-opencl-sdk rocm-openmp rocm-smi-lib rocminfo rocprim-dev rocprofiler
  rocprofiler-compute rocprofiler-dev rocprofiler-plugins rocprofiler-register rocprofiler-sdk rocprofiler-sdk-rocpd rocprofiler-sdk-roctx rocprofiler-systems rocrand rocrand-dev rocsolver rocsolver-dev rocsparse rocsparse-dev
  rocthrust-dev roctracer roctracer-dev rocwmma-dev rpp rpp-dev unixodbc-common va-driver-all valgrind
Suggested packages:
  lib32stdc++6-13-dbg libx32stdc++6-13-dbg i965-va-driver-shaders libcuda1 libnvcuvid1 libnvidia-encode1 libbluray-bdj libgd-tools geotiff-bin gdal-bin libgeotiff-epsg glew-utils gphoto2 libhdf4-doc libhdf4-alt-dev hdf4-tools
  libheif-plugin-x265 libheif-plugin-ffmpegdec libheif-plugin-jpegdec libheif-plugin-jpegenc libheif-plugin-j2kdec libheif-plugin-j2kenc libheif-plugin-rav1e libheif-plugin-svtenc icu-doc liblzma-doc ncurses-doc odbc-postgresql
  tdsodbc ogdi-bin opencv-doc qgnomeplatform-qt5 qt5-image-formats-plugins qt5-qmltooling-plugins libraw1394-doc speex libtbb-doc mpi-default-bin vtk9-doc vtk9-examples libwacom-bin opencl-clhpp-headers-doc valgrind-dbg
  valgrind-mpi kcachegrind alleyoop valkyrie
The following NEW packages will be installed:
  amd-smi-lib amdgpu-core comgr composablekernel-dev g++-13-multilib g++-multilib gcc-13-multilib gcc-multilib gdal-data gdal-plugins half hip-dev hip-doc hip-runtime-amd hip-samples hipblas hipblas-common-dev hipblas-dev hipblaslt
  hipblaslt-dev hipcc hipcub-dev hipfft hipfft-dev hipfort-dev hipify-clang hiprand hiprand-dev hipsolver hipsolver-dev hipsparse hipsparse-dev hipsparselt hipsparselt-dev hiptensor hiptensor-dev hsa-amd-aqlprofile hsa-rocr
  hsa-rocr-dev i965-va-driver icu-devtools intel-media-va-driver lib32asan8 lib32atomic1 lib32gcc-13-dev lib32gcc-s1 lib32gomp1 lib32itm1 lib32quadmath0 lib32stdc++-13-dev lib32stdc++6 lib32ubsan1 libaacs0 libaec0 libamd3 libaom3
  libarmadillo12 libarpack2t64 libavcodec-dev libavcodec60 libavformat-dev libavformat60 libavutil-dev libavutil58 libbdplus0 libblas3 libblosc1 libbluray2 libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libcamd3 libccolamd3
  libcfitsio10t64 libcharls2 libcholmod5 libchromaprint1 libcjson1 libcodec2-1.2 libcolamd3 libdav1d7 libdc1394-25 libdc1394-dev libde265-0 libdeflate-dev libdouble-conversion3 libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common
  libdrm-amdgpu-dev libdrm-amdgpu-radeon1 libdrm2-amdgpu libexif-dev libexif-doc libfile-copy-recursive-perl libfile-which-perl libfreexl1 libfyba0t64 libgd3 libgdal34t64 libgdcm-dev libgdcm3.0t64 libgeos-c1t64 libgeos3.12.1t64
  libgeotiff5 libgl2ps1.4 libglew2.2 libgme0 libgphoto2-6t64 libgphoto2-dev libgphoto2-l10n libgphoto2-port12t64 libgsm1 libhdf4-0-alt libhdf5-103-1t64 libhdf5-hl-100t64 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwy1t64 libicu-dev libigdgmm12 libimath-dev libinput-bin libinput10 libjbig-dev libjpeg-dev libjpeg-turbo8-dev libjpeg8-dev libjsoncpp25 libjxl0.7 libkmlbase1t64 libkmldom1t64 libkmlengine1t64
  liblapack3 liblept5 liblerc-dev liblzma-dev libmbedcrypto7t64 libmd4c0 libminizip1t64 libmp3lame0 libmpg123-0t64 libmtdev1t64 libncurses-dev libnetcdf19t64 libnorm1t64 libodbc2 libodbcinst2 libogdi4.1 libopencv-calib3d-dev
  libopencv-calib3d406t64 libopencv-contrib-dev libopencv-contrib406t64 libopencv-core-dev libopencv-core406t64 libopencv-dev libopencv-dnn-dev libopencv-dnn406t64 libopencv-features2d-dev libopencv-features2d406t64
  libopencv-flann-dev libopencv-flann406t64 libopencv-highgui-dev libopencv-highgui406t64 libopencv-imgcodecs-dev libopencv-imgcodecs406t64 libopencv-imgproc-dev libopencv-imgproc406t64 libopencv-java libopencv-ml-dev
  libopencv-ml406t64 libopencv-objdetect-dev libopencv-objdetect406t64 libopencv-photo-dev libopencv-photo406t64 libopencv-shape-dev libopencv-shape406t64 libopencv-stitching-dev libopencv-stitching406t64 libopencv-superres-dev
  libopencv-superres406t64 libopencv-video-dev libopencv-video406t64 libopencv-videoio-dev libopencv-videoio406t64 libopencv-videostab-dev libopencv-videostab406t64 libopencv-viz-dev libopencv-viz406t64 libopencv406-jni
  libopenexr-dev libopenmpt0t64 libpcre2-16-0 libpgm-5.3-0t64 libpng-dev libpng-tools libproj25 libprotobuf32t64 libqhull-r8.0 libqt5core5t64 libqt5dbus5t64 libqt5gui5t64 libqt5network5t64 libqt5opengl5t64 libqt5qml5
  libqt5qmlmodels5 libqt5quick5 libqt5svg5 libqt5test5t64 libqt5waylandclient5 libqt5waylandcompositor5 libqt5widgets5t64 librabbitmq4 librav1e0 libraw1394-11 libraw1394-dev libraw1394-tools librist4 librttopo1 libsharpyuv-dev
  libshine3 libsnappy1v5 libsocket++1 libsodium23 libsoxr0 libspatialite8t64 libspeex1 libsrt1.5-gnutls libssh-gcrypt-4 libsuitesparseconfig7 libsuperlu6 libsvtav1enc1d1 libswresample-dev libswresample4 libswscale-dev libswscale7
  libsz2 libtbb-dev libtbb12 libtbbbind-2-5 libtbbmalloc2 libtesseract5 libtiff-dev libtiffxx6 libtwolame0 libudfread0 liburiparser1 libva-drm2 libva-x11-2 libva2 libvorbisfile3 libvpl2 libvpx9 libvtk9.1t64 libwacom-common
  libwacom9 libwebp-dev libwebpdecoder3 libx265-199 libx32asan8 libx32atomic1 libx32gcc-13-dev libx32gcc-s1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-13-dev libx32stdc++6 libx32ubsan1 libxerces-c3.2t64 libxml2-dev
  libxvidcore4 libzmq5 libzvbi-common libzvbi0t64 mesa-common-dev mesa-va-drivers migraphx migraphx-dev miopen-hip miopen-hip-dev mivisionx mivisionx-dev ocl-icd-opencl-dev opencl-c-headers opencl-clhpp-headers opencv-data
  openmp-extras-dev openmp-extras-runtime proj-bin proj-data python3-argcomplete qt5-gtk-platformtheme qttranslations5-l10n qtwayland5 rccl rccl-dev rocalution rocalution-dev rocblas rocblas-dev rocfft rocfft-dev rocm rocm-cmake
  rocm-core rocm-dbgapi rocm-debug-agent rocm-developer-tools rocm-device-libs rocm-gdb rocm-hip rocm-language-runtime rocm-llvm rocm-opencl rocm-opencl-dev rocm-opencl-sdk rocm-openmp rocm-smi-lib rocminfo rocprim-dev rocprofiler
  rocprofiler-compute rocprofiler-dev rocprofiler-plugins rocprofiler-register rocprofiler-sdk rocprofiler-sdk-rocpd rocprofiler-sdk-roctx rocprofiler-systems rocrand rocrand-dev rocsolver rocsolver-dev rocsparse rocsparse-dev
  rocthrust-dev roctracer roctracer-dev rocwmma-dev rpp rpp-dev unixodbc-common va-driver-all valgrind
0 upgraded, 347 newly installed, 0 to remove and 0 not upgraded.
Need to get 5,952 MB/5,955 MB of archives.
After this operation, 24.3 GB of additional disk space will be used.
```