# A potential OpenCL driver problem with AMD 5700G APUs

- **Issue #:** 1586
- **State:** closed
- **Created:** 2021-10-11T02:10:48Z
- **Updated:** 2024-02-03T12:06:09Z
- **URL:** https://github.com/ROCm/ROCm/issues/1586

Dear ROCm team and other OpenCL experts,

I need your help on using your APUs with OpenCL. Today I installed a new APU platform with AMD's 5700G with the intention to use its OpenCL functionality with Octave and Octave-ocl (https://sourceforge.net/projects/octave-ocl/files/). Octave is well known as an opensource alternative to Matlab, while Octave-ocl enables the similar gpuArray functionality in Octave with OpenCL devices as compared to CUDA only in Matlab. I was a tiny contributor to octave-ocl with some of my testing and coding as well as my own fork page (https://sourceforge.net/u/tangjinchuan/octave-ocl-gzu/ci/default/tree/). However, the problem I face with AMD's APU just above my limit in time.

The problem is that any time I try to use AMD's platform driver (for example, OpenCL 2.1 AMD-APP (3302.6)), the Octave program will crash.

You can try install Octave 6.3 (select a directory without any space, otherwise there will be problem), and pkg install the Octave-ocl tar.gz file.

For example:

>>pkg install ocl-1.1.1.tar.gz

% this will install the ocl pkg in octave

>>pkg load ocl

% this will load ocl pkg

>>gpuArray(1,5)

% this will generate a GPU array with 1 row, 5 colums of ones. BUt it will make the Octave program crash.

My experience：
I had no problems with ocl in Nvidia (e.g. RTX 3080), Intel CPUs/GPUs. But 5700G will give a crash. (and I remembered a very long time ago, I borrowed another older amd APUs, it also crashed the program). More info on different drivers, please see my page: https://sourceforge.net/u/tangjinchuan/wiki/browse_pages/

I had no problem with AMD's 5700G CPUs (Yes, its CPU part even though AMD dropped the Windows OpenCL support for CPUs ) even if I choose Intel's OpenCL runtime to run any OpenCL tasks.

I had no problem with AMD's 5700G GPUs if I choose Microsoft's OpenCL on DX12 runtime to run any 32bit OpenCL tasks (Unfortunately, it does not support 64bits).

To select the opencl driver, we can use >> ocl_context ("device_selection", 'GPU0')

GPUn represent the nth GPU driver, while ocl_context ("device_selection", 'CPU') ask to run CPUs. Also U can use

I tried to find the problem with Windows cmd, it gives the following results:

Microsoft Windows [Version 10.0.19043.1202]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Owner>cd C:\Octave-6.3.0\mingw64\bin

C:\Octave-6.3.0\mingw64\bin>octave-cli-6.3.0.exe
GNU Octave, version 6.3.0
Copyright (C) 2021 The Octave Project Developers.
This is free software; see the source code for copying conditions.
There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. For details, type 'warranty'.

Octave was configured for "x86_64-w64-mingw32".

Additional information about Octave is available at https://www.octave.org.

Please contribute if you find this software useful.
For more information, visit https://www.octave.org/get-involved.html

Read https://www.octave.org/bugs.html to learn how to submit bug reports.
For information about changes from previous versions, type 'news'.


Here are the step to locate the errors in cmd:

Since the GUI of Octave will disappear if executing any OpenCL related statement such as gpuArray(1,5), I tried to find what did the Octave returns before it crashed. Hence, I tried to use the CLI of Octave in cmd of Windows 10. 

1. The file should be in "C:\Octave-6.3.0\mingw64\bin>octave-cli-6.3.0.exe" or similar location. 

2. type in C:\Octave-6.3.0\mingw64\bin>octave-cli-6.3.0.exe in the cmd of Windows.

3. Now we can type any Octave related cmd. 

4. >> pkg load ocl

5. line 4 will load the ocl pkg

6. >>gpuArray(1,5)

7. At this point the cmd will return an LLVM related errors with AMD's OpenCL drivers.


octave:1> pkd load ocl
error: 'pkd' undefined near line 1, column 1
octave:2> pkg load ocl
octave:3> ocl_ones(1,5)
error: Invalid record (Producer: 'LLVM3.9.0svn' Reader: 'LLVM 3.9.0svn')

C:\Octave-6.3.0\mingw64\bin>octave-cli-6.3.0.exe

Also, my platform info get from Octave-ocl

>> ocl_context('get_resources')
ans =

scalar structure containing the fields:

platforms =
{
[1,1] =

scalar structure containing the fields:

platform_index = 0
name = AMD Accelerated Parallel Processing
version = OpenCL 2.1 AMD-APP (3302.6)
profile = FULL_PROFILE
vendor = Advanced Micro Devices, Inc.
extensions = cl_khr_icd cl_khr_d3d10_sharing cl_khr_d3d11_sharing cl_khr_dx9_media_sharing cl_amd_event_callback cl_amd_offl
ine_devices

[2,1] =

scalar structure containing the fields:

platform_index = 1
name = OpenCLOn12
version = OpenCL 1.2 D3D12 Implementation
profile = FULL_PROFILE
vendor = Microsoft
extensions = cl_khr_icd

[3,1] =

scalar structure containing the fields:

platform_index = 2
name = Intel(R) OpenCL
version = OpenCL 2.1 WINDOWS
profile = FULL_PROFILE
vendor = Intel(R) Corporation
extensions = cl_khr_icd cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomic
s cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_byte_addressable_store cl_khr_dep
th_images cl_khr_3d_image_writes cl_khr_il_program cl_intel_unified_shared_memory_preview cl_intel_subgroups cl_intel_subgroups_char c
l_intel_subgroups_short cl_intel_subgroups_long cl_intel_spirv_subgroups cl_intel_required_subgroup_size cl_intel_exec_by_local_thread
cl_intel_vec_len_hint cl_khr_spir cl_khr_fp64 cl_khr_image2d_from_buffer

}

devices =
{
[1,1] =
{
[1,1] =

scalar structure containing the fields:

platform_index = 0
device_index = 0
name = gfx90c
vendor = Advanced Micro Devices, Inc.
type = 4
version =

scalar structure containing the fields:

driver: 1x18 sq_string
device: 1x27 sq_string
opencl_c: 1x13 sq_string
profile: 1x12 sq_string
vendorid: 1x1 scalar

compute =

scalar structure containing the fields:

units: 1x1 scalar
max_dimension: 1x1 scalar
max_workgroup_size: 1x1 scalar
max_workitems_size: 1x3 matrix
clock_frequency: 1x1 scalar

mem =

scalar structure containing the fields:

global: 1x1 scalar struct
local: 1x1 scalar struct
const: 1x1 scalar struct
param: 1x1 scalar struct
address_bits: 1x1 scalar
align: 1x1 scalar struct
little_endian: 1x1 scalar
host_unified: 1x1 scalar
vector_width: 1x1 scalar struct

caps =

scalar structure containing the fields:

device_available: 1x1 scalar
compiler_available: 1x1 scalar
queue_props: 1x1 scalar
execution: 1x1 scalar
profile_timer_res: 1x1 scalar
error_correction: 1x1 scalar
half: 1x1 scalar struct
single: 1x1 scalar struct
double: 1x1 scalar struct
images: 1x1 scalar struct
extensions: 1x683 sq_string


}

[2,1] =
{
[1,1] =

scalar structure containing the fields:

platform_index = 1
device_index = 0
name = AMD Radeon(TM) Graphics
vendor = Microsoft
type = 4
version =

scalar structure containing the fields:

driver: 1x5 sq_string
device: 1x31 sq_string
opencl_c: 1x13 sq_string
profile: 1x12 sq_string
vendorid: 1x1 scalar

compute =

scalar structure containing the fields:

units: 1x1 scalar
max_dimension: 1x1 scalar
max_workgroup_size: 1x1 scalar
max_workitems_size: 1x3 matrix
clock_frequency: 1x1 scalar

mem =

scalar structure containing the fields:

global: 1x1 scalar struct
local: 1x1 scalar struct
const: 1x1 scalar struct
param: 1x1 scalar struct
address_bits: 1x1 scalar
align: 1x1 scalar struct
little_endian: 1x1 scalar
host_unified: 1x1 scalar
vector_width: 1x1 scalar struct

caps =

scalar structure containing the fields:

device_available: 1x1 scalar
compiler_available: 1x1 scalar
queue_props: 1x1 scalar
execution: 1x1 scalar
profile_timer_res: 1x1 scalar
error_correction: 1x1 scalar
half: 1x1 scalar struct
single: 1x1 scalar struct
double: 1x1 scalar struct
images: 1x1 scalar struct
extensions: 1x168 sq_string


[2,1] =

scalar structure containing the fields:

platform_index = 1
device_index = 1
name = Microsoft Basic Render Driver
vendor = Microsoft
type = 4
version =

scalar structure containing the fields:

driver: 1x5 sq_string
device: 1x31 sq_string
opencl_c: 1x13 sq_string
profile: 1x12 sq_string
vendorid: 1x1 scalar

compute =

scalar structure containing the fields:

units: 1x1 scalar
max_dimension: 1x1 scalar
max_workgroup_size: 1x1 scalar
max_workitems_size: 1x3 matrix
clock_frequency: 1x1 scalar

mem =

scalar structure containing the fields:

global: 1x1 scalar struct
local: 1x1 scalar struct
const: 1x1 scalar struct
param: 1x1 scalar struct
address_bits: 1x1 scalar
align: 1x1 scalar struct
little_endian: 1x1 scalar
host_unified: 1x1 scalar
vector_width: 1x1 scalar struct

caps =

scalar structure containing the fields:

device_available: 1x1 scalar
compiler_available: 1x1 scalar
queue_props: 1x1 scalar
execution: 1x1 scalar
profile_timer_res: 1x1 scalar
error_correction: 1x1 scalar
half: 1x1 scalar struct
single: 1x1 scalar struct
double: 1x1 scalar struct
images: 1x1 scalar struct
extensions: 1x168 sq_string


}

[3,1] =
{
[1,1] =

scalar structure containing the fields:

platform_index = 2
device_index = 0
name = AMD Ryzen 7 5700G with Radeon Graphics
vendor = Intel(R) Corporation
type = 2
version =

scalar structure containing the fields:

driver: 1x21 sq_string
device: 1x20 sq_string
opencl_c: 1x13 sq_string
profile: 1x12 sq_string
vendorid: 1x1 scalar

compute =

scalar structure containing the fields:

units: 1x1 scalar
max_dimension: 1x1 scalar
max_workgroup_size: 1x1 scalar
max_workitems_size: 1x3 matrix
clock_frequency: 1x1 scalar

mem =

scalar structure containing the fields:

global: 1x1 scalar struct
local: 1x1 scalar struct
const: 1x1 scalar struct
param: 1x1 scalar struct
address_bits: 1x1 scalar
align: 1x1 scalar struct
little_endian: 1x1 scalar
host_unified: 1x1 scalar
vector_width: 1x1 scalar struct

caps =

scalar structure containing the fields:

device_available: 1x1 scalar
compiler_available: 1x1 scalar
queue_props: 1x1 scalar
execution: 1x1 scalar
profile_timer_res: 1x1 scalar
error_correction: 1x1 scalar
half: 1x1 scalar struct
single: 1x1 scalar struct
double: 1x1 scalar struct
images: 1x1 scalar struct
extensions: 1x587 sq_string


}

}

summary =
{
[1,1] =

scalar structure containing the fields:

type = GPU
fp64 = 1
version = 2
platform_index = 0
device_index = 0
name = gfx90c

[2,1] =

scalar structure containing the fields:

type = CPU
fp64 = 1
version = 2
platform_index = 2
device_index = 0
name = AMD Ryzen 7 5700G with Radeon Graphics

[3,1] =

scalar structure containing the fields:

type = GPU
fp64 = 0
version = 1
platform_index = 1
device_index = 0
name = AMD Radeon(TM) Graphics

[4,1] =

scalar structure containing the fields:

type = GPU
fp64 = 0
version = 1
platform_index = 1
device_index = 1
name = Microsoft Basic Render Driver

}


>>


Best wishes,

Jinchuan Tang