# [Feature]: Support 64-bit global work size in OpenCL

- **Issue #:** 5524
- **State:** open
- **Created:** 2025-10-15T17:08:05Z
- **Updated:** 2025-10-31T15:41:33Z
- **Labels:** Feature Request, status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5524

### Problem Description

AMD's OpenCL driver fails to dispatch kernels with 64-bit global range >2³² (>4 billion threads), making the kernel throw OpenCL error -63.

Impact: Due to this bug, FluidX3D simulations on Instinct MI355X will not work with VRAM allocation >225GB. The full 288GB VRAM capacity cannot be used. Other software will potentially also be broken.

### Operating System

Linux, Windows

### CPU

AMD EPYC, Intel Core i7-8700K

### GPU

reproduced on AMD Instinct MI355X and AMD RX 7700 XT

### ROCm Version

latest as of today

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

To reproduce:
0. You need an AMD GPU with at least 6GB VRAM.
1. `git clone https://github.com/ProjectPhysX/OpenCL-Wrapper.git`
2. modify `src/main.cpp` to
```c
#include "opencl.hpp"

int main() {
	Device device(select_device_with_most_flops()); // compile OpenCL C code for the fastest available device
	
	//const ulong N = 4ull*1024ull*1024ull*1024ull-64ull; // works
	const ulong N = 4ull*1024ull*1024ull*1024ull+64ull; // broken

	Memory<char> A(device, N); // allocate memory on both host and device
	Kernel add_kernel(device, N, "add_kernel", A); // kernel that runs on the device

	print_info("Value before kernel execution: A[0] = "+to_string((int)A[0]));
	A.write_to_device(); // copy data from host memory to device memory
	add_kernel.run(); // run add_kernel on the device
	A.read_from_device(); // copy data from device memory to host memory
	print_info("Value after kernel execution: A[0] = "+to_string((int)A[0]));

	wait();
	return 0;
}
```
3. modify `src/kernel.cpp` to
```c
#include "kernel.hpp" // note: unbalanced round brackets () are not allowed and string literals can't be arbitrarily long, so periodically interrupt with )+R(
string opencl_c_container() { return R( // ########################## begin of OpenCL C code ####################################################################

kernel void add_kernel(global char* A) {
	A[get_global_id(0)] = 7;
}

);} // ############################################################### end of OpenCL C code #####################################################################
```
4. Compile and run (on Linux via `./make.sh`, on Windows via Visual Studio Community)
5. expected output: 7, output for N>2³²: kernel errors with OpenCL error code -63

Can be reproduced on both Linux and Windows with lartest drivers as of today.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Please add OpenCL to "ROCm Component" field!