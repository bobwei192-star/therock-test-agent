# unable to open /dev/kfd read-write: Bad address

- **Issue #:** 1205
- **State:** closed
- **Created:** 2020-08-25T20:33:31Z
- **Updated:** 2022-11-07T23:40:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1205

after Fresh install of ubuntu 20.04 and ROCm 3.7 latest until today. when verifying installing throw 
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
the first command dont work even when removed the (base) of conda 
my specs , acer315-42G  Ryzen 5 3500u with Vega 8 , radeon 540x 

<pre>(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ cd kfd
bash: cd: kfd: Not a directory
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ groups
mohamed adm cdrom sudo dip video plugdev render lpadmin lxd sambashare
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ ls -la /dev/kfd
crw-rw---- 1 root render 236, 0 Aug 25 21:05 <span style="background-color:#2E3436"><font color="#C4A000"><b>/dev/kfd</b></font></span>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ /opt/rocm/bin/rocminfo
<font color="#D3D7CF">ROCk module is loaded</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: Bad address</font>
<font color="#D3D7CF">mohamed is member of render group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ sudo /opt/rocm/bin/rocminfo
<font color="#D3D7CF">ROCk module is loaded</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: Bad address</font>
<font color="#D3D7CF">mohamed is member of render group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
(base) <font color="#4E9A06"><b>mohamed@acer</b></font>:<font color="#3465A4"><b>/dev</b></font>$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3182.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
</pre>