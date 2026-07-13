# apt repository broken ?

- **Issue #:** 1186
- **State:** closed
- **Created:** 2020-07-28T23:30:56Z
- **Updated:** 2020-12-16T05:25:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1186

I'm attempting to install `rocm-dkms3.5.0` on Ubuntu 18.04.1 using
```
sudo apt install rocm-dkms3.5.0
```
This results in 404 errors and unexpected file size errors for rocm-dkms3.5.0 and its dependencies
```
The following additional packages will be installed:
  comgr dkms hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libdrm-dev libelf-dev libpthread-stubs0-dev libx11-dev
  libx11-doc libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu mesa-common-dev rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs
  rocm-gdb rocm-opencl rocm-opencl-dev rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
Suggested packages:
  menu libxcb-doc
The following NEW packages will be installed:
  comgr dkms hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libdrm-dev libelf-dev libpthread-stubs0-dev libx11-dev
  libx11-doc libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu mesa-common-dev rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs
  rocm-dkms rocm-gdb rocm-opencl rocm-opencl-dev rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
0 upgraded, 43 newly installed, 0 to remove and 0 not upgraded.
Need to get 567 MB/572 MB of archives.
After this operation, 645 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Err:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms-firmware all 1:3.5-32
  404  Not Found [IP: 13.82.220.49 80]
Err:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms all 1:3.5-32
  404  Not Found [IP: 13.82.220.49 80]
Err:3 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr amd64 1.6.0.143-rocm-rel-3.5-34-e24e8c1
  404  Not Found [IP: 13.82.220.49 80]
Err:4 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-base amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 13.82.220.49 80]
Err:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-doc amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 13.82.220.49 80]
Get:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.9-347-gd4b224f [67.2 kB]
Err:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.9-347-gd4b224f
  File has unexpected size (67202 != 67200). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:56e4d74289e1625aed9f22b897d4a542fa3a2aa17fda0cbcab80710fedb156e7
   - SHA1:1d65862a98de6f6e2109efcf346057c622e190f6 [weak]
   - MD5Sum:2e0ad38f7a419aab64f459a19609ad19 [weak]
   - Filesize:67200 [weak]
Err:7 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
  404  Not Found [IP: 13.82.220.49 80]
Err:8 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
  404  Not Found [IP: 13.82.220.49 80]
Err:9 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocminfo amd64 1.30501.0
  404  Not Found [IP: 13.82.220.49 80]
Get:10 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl amd64 2.0.20191 [550 kB]
Err:10 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl amd64 2.0.20191
  File has unexpected size (550468 != 550470). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:7d946dd6de12608d9645ac07fc101bae69fce2383906e96f6ccb5903a61d19ff
   - SHA1:7400a7aada0b3ebb9ccb9cd02f2418fb0b7e4cc3 [weak]
   - MD5Sum:47382b45e31d24cf9ef3a42bbbbed52b [weak]
   - Filesize:550470 [weak]
Get:11 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl-dev amd64 2.0.20191 [125 kB]
Err:11 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl-dev amd64 2.0.20191
  File has unexpected size (124550 != 124554). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:683eda64426dd7bb30f5c4b5537717e8561137aa695667027f5ab2344591f070
   - SHA1:a76d9c933d23947c17706e1e27acbd6552c721c6 [weak]
   - MD5Sum:25b9c58d4c011f1c7616aaca5a76d72f [weak]
   - Filesize:124554 [weak]
Err:12 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-clang-ocl amd64 0.5.0.51-rocm-rel-3.5-34-74b3b81
  404  Not Found [IP: 13.82.220.49 80]
Err:13 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-utils amd64 3.5.1-34
  404  Not Found [IP: 13.82.220.49 80]
Get:14 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 llvm-amdgpu amd64 11.0.dev [481 MB]
Err:14 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 llvm-amdgpu amd64 11.0.dev
  File has unexpected size (480521202 != 480614958). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:9ad0ddd2d3f7d35821301969f5bdd524c46fbe767171206698c79f20bfcbce34
   - SHA1:6a8a92bdf29b93e4a8c1cbd2d0b1545937dad77d [weak]
   - MD5Sum:9c15b5e4f86d6c5506c84afc9f384e72 [weak]
   - Filesize:480614958 [weak]
Err:15 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-rocclr amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 13.82.220.49 80]
Err:16 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-samples amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 13.82.220.49 80]
Get:17 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-amd-aqlprofile amd64 1.0.0 [68.9 kB]
Err:17 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-amd-aqlprofile amd64 1.0.0
  File has unexpected size (68922 != 68920). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:5dc9761754c5a3940f4ef4df8487987ba21e3b822d1c609a41eb6da57d925e79
   - SHA1:6a6ee925ccd974ede3bf95bbf3b911fab99f52af [weak]
   - MD5Sum:2128205a2ede106cc9b33102b7b72b9b [weak]
   - Filesize:68920 [weak]
Get:18 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct-dev amd64 1.0.9-347-gd4b224f [26.4 kB]
Err:18 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct-dev amd64 1.0.9-347-gd4b224f
  File has unexpected size (26420 != 26428). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:6c6e0534b9bb5d9332d9d8846c9fe53bf522eef2bd2ee54886037a666f0ebd74
   - SHA1:3345a47a074148e901ae5015c1c8e801628934f8 [weak]
   - MD5Sum:a9694c393423eb0a399db016ad2f5b5c [weak]
   - Filesize:26428 [weak]
Err:19 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-cmake amd64 0.3.0.153-rocm-rel-3.5-34-1d1caa5
  404  Not Found [IP: 13.82.220.49 80]
Err:20 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dbgapi amd64 0.21.2-rocm-rel-3.5-34
  404  Not Found [IP: 13.82.220.49 80]
Err:21 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-debug-agent amd64 1.0.0.30501-rocm-rel-3.5-34
  404  Not Found [IP: 13.82.220.49 80]
Err:22 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-device-libs amd64 1.0.0.586-rocm-rel-3.5-34-ab93876
  404  Not Found [IP: 13.82.220.49 80]
Err:23 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-gdb amd64 9.1-rocm-rel-3.5-34
  404  Not Found [IP: 13.82.220.49 80]
Err:24 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi amd64 1.0.0-201-rocm-rel-3.5-34-gcdfbef4
  404  Not Found [IP: 13.82.220.49 80]
Err:25 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi-lib64 amd64 2.4.0.15.rocm-rel-3.5-34-2143bc3
  404  Not Found [IP: 13.82.220.49 80]
Get:26 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0 [239 kB]
Err:26 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocprofiler-dev amd64 1.0.0
  File has unexpected size (238830 != 238824). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:7c7569771dd406d0066d5e64cec6008f51bafc719508a8f8bf106f5768f8ad92
   - SHA1:97bd8c8b614070ecdf0d7461cb869837e3c4d82b [weak]
   - MD5Sum:cfd100215149f3e69da8f5d1938c28f2 [weak]
   - Filesize:238824 [weak]
Get:27 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0 [393 kB]
Err:27 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0
  File has unexpected size (393098 != 393204). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:1b1e06e38e171ddb04eecb859bd45e2327a33722207b264aade52456f73511e1
   - SHA1:2c3a0bfacb9a3300c377f06fbcb958c137f2f770 [weak]
   - MD5Sum:e2950838fab61963549c74b79f6bd800 [weak]
   - Filesize:393204 [weak]
Err:28 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dev amd64 3.5.1-34
  404  Not Found [IP: 13.82.220.49 80]
Err:29 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 3.5.1-34
  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms-firmware_3.5-32_all.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_3.5-32_all.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/c/comgr/comgr_1.6.0.143-rocm-rel-3.5-34-e24e8c1_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-base/hip-base_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-doc/hip-doc_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsakmt-roct/hsakmt-roct_1.0.9-347-gd4b224f_amd64.deb  File has unexpected size (67202 != 67200). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:56e4d74289e1625aed9f22b897d4a542fa3a2aa17fda0cbcab80710fedb156e7
    - SHA1:1d65862a98de6f6e2109efcf346057c622e190f6 [weak]
    - MD5Sum:2e0ad38f7a419aab64f459a19609ad19 [weak]
    - Filesize:67200 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-rocr-dev/hsa-rocr-dev_1.1.30501.0-rocm-rel-3.5-34-def83d8_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-ext-rocr-dev/hsa-ext-rocr-dev_1.1.30501.0-rocm-rel-3.5-34-def83d8_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocminfo/rocminfo_1.30501.0_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-opencl/rocm-opencl_2.0.20191_amd64.deb  File has unexpected size (550468 != 550470). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:7d946dd6de12608d9645ac07fc101bae69fce2383906e96f6ccb5903a61d19ff
    - SHA1:7400a7aada0b3ebb9ccb9cd02f2418fb0b7e4cc3 [weak]
    - MD5Sum:47382b45e31d24cf9ef3a42bbbbed52b [weak]
    - Filesize:550470 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-opencl-dev/rocm-opencl-dev_2.0.20191_amd64.deb  File has unexpected size (124550 != 124554). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:683eda64426dd7bb30f5c4b5537717e8561137aa695667027f5ab2344591f070
    - SHA1:a76d9c933d23947c17706e1e27acbd6552c721c6 [weak]
    - MD5Sum:25b9c58d4c011f1c7616aaca5a76d72f [weak]
    - Filesize:124554 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-clang-ocl/rocm-clang-ocl_0.5.0.51-rocm-rel-3.5-34-74b3b81_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-utils/rocm-utils_3.5.1-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/l/llvm-amdgpu/llvm-amdgpu_11.0.dev_amd64.deb  File has unexpected size (480521202 != 480614958). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:9ad0ddd2d3f7d35821301969f5bdd524c46fbe767171206698c79f20bfcbce34
    - SHA1:6a8a92bdf29b93e4a8c1cbd2d0b1545937dad77d [weak]
    - MD5Sum:9c15b5e4f86d6c5506c84afc9f384e72 [weak]
    - Filesize:480614958 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-rocclr/hip-rocclr_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-samples/hip-samples_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile/hsa-amd-aqlprofile_1.0.0_amd64.deb  File has unexpected size (68922 != 68920). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:5dc9761754c5a3940f4ef4df8487987ba21e3b822d1c609a41eb6da57d925e79
    - SHA1:6a6ee925ccd974ede3bf95bbf3b911fab99f52af [weak]
    - MD5Sum:2128205a2ede106cc9b33102b7b72b9b [weak]
    - Filesize:68920 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsakmt-roct-dev/hsakmt-roct-dev_1.0.9-347-gd4b224f_amd64.deb  File has unexpected size (26420 != 26428). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:6c6e0534b9bb5d9332d9d8846c9fe53bf522eef2bd2ee54886037a666f0ebd74
    - SHA1:3345a47a074148e901ae5015c1c8e801628934f8 [weak]
    - MD5Sum:a9694c393423eb0a399db016ad2f5b5c [weak]
    - Filesize:26428 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-cmake/rocm-cmake_0.3.0.153-rocm-rel-3.5-34-1d1caa5_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dbgapi/rocm-dbgapi_0.21.2-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-debug-agent/rocm-debug-agent_1.0.0.30501-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-device-libs/rocm-device-libs_1.0.0.586-rocm-rel-3.5-34-ab93876_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-gdb/rocm-gdb_9.1-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-smi/rocm-smi_1.0.0-201-rocm-rel-3.5-34-gcdfbef4_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-smi-lib64/rocm-smi-lib64_2.4.0.15.rocm-rel-3.5-34-2143bc3_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocprofiler-dev/rocprofiler-dev_1.0.0_amd64.deb  File has unexpected size (238830 != 238824). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:7c7569771dd406d0066d5e64cec6008f51bafc719508a8f8bf106f5768f8ad92
    - SHA1:97bd8c8b614070ecdf0d7461cb869837e3c4d82b [weak]
    - MD5Sum:cfd100215149f3e69da8f5d1938c28f2 [weak]
    - Filesize:238824 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/roctracer-dev/roctracer-dev_1.0.0_amd64.deb  File has unexpected size (393098 != 393204). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:1b1e06e38e171ddb04eecb859bd45e2327a33722207b264aade52456f73511e1
    - SHA1:2c3a0bfacb9a3300c377f06fbcb958c137f2f770 [weak]
    - MD5Sum:e2950838fab61963549c74b79f6bd800 [weak]
    - Filesize:393204 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dev/rocm-dev_3.5.1-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dkms/rocm-dkms_3.5.1-34_amd64.deb  404  Not Found [IP: 13.82.220.49 80]
```
I can confirm that the deb files that result in the 404 error do not exist at the listed URLs.