# Radeon VII problem on ROCm 2.6

- **Issue #:** 843
- **State:** closed
- **Created:** 2019-07-11T10:06:46Z
- **Updated:** 2019-10-05T19:29:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/843

Hi, 

Installed Ubuntu 18.04.2 with kernel 4.15.0-54 with ROCm 2.6 installed, found the computing feature can't be set successfully, what's problem going on?

test@test:~/rvs/build/bin$ sudo /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2924.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
test@test:~/rvs/build/bin$ sudo /opt/rocm/bin/rocm-smi


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf  PwrCap  VRAM%  GPU%  
1    35.0c  17.0W   931Mhz  351Mhz  0.0%  auto  225.0W    0%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
test@test:~/rvs/build/bin$ ./rvs -g

ROCm Validation Suite (version 0.0.32)

Supported GPUs available:
20:00.0 - GPU[ 2 -  2996] Vega 20 (Device 26273)
test@test-G481-HA0-00:~/rvs/build/bin$ ./rvs -d 5 -c conf/gst_1.conf 
[DEBUG ] [  1968.962527] property: [name]   val:[action_1]
[DEBUG ] [  1968.962549] property: [device]   val:[26273]
[DEBUG ] [  1968.962555] property: [module]   val:[gst]
[DEBUG ] [  1968.962559] property: [parallel]   val:[false]
[DEBUG ] [  1968.962563] property: [count]   val:[2]
[DEBUG ] [  1968.962567] property: [wait]   val:[100]
[DEBUG ] [  1968.962571] property: [duration]   val:[18000]
[DEBUG ] [  1968.962575] property: [ramp_interval]   val:[7000]
[DEBUG ] [  1968.962580] property: [log_interval]   val:[1000]
[DEBUG ] [  1968.962584] property: [max_violations]   val:[1]
[DEBUG ] [  1968.962590] property: [copy_matrix]   val:[false]
[DEBUG ] [  1968.962594] property: [target_stress]   val:[5000]
[DEBUG ] [  1968.962599] property: [tolerance]   val:[0.07]
[DEBUG ] [  1968.962605] property: [matrix_size]   val:[5760]
[DEBUG ] [  1968.962609] property: [cli.-c]   val:[conf/gst_1.conf]
[DEBUG ] [  1968.962612] property: [cli.-d]   val:[5]
[DEBUG ] [  1968.962614] property: [cli.pwd]   val:[/home/test/rvs/build/bin/]
GPU device 0 doesn't not exist

Aborted (core dumped)
