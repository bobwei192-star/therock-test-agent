# ROCm Stack is about 40% slower than AMDGPU-PRO 

- **Issue #:** 452
- **State:** closed
- **Created:** 2018-07-07T13:31:18Z
- **Updated:** 2018-07-07T14:59:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/452

Hi,

Well... The ROCm stack is a nice thing, but it's so horribly slow!

For a Boundary Element Method solver, I utilize the GPU via OpenCL.
The application I developed has a small benchmark tool, which calculates the number of integrals calculated per second.

WIth AMDGPU-PRO 18.20-606296 (Ubuntu 16.04.4, Kernel 4.15) I get around 5.1GInt/s (Gigaintegrals per second) at n = 22000. With ROCm (Ubuntu 16.04.4, Kernel 4.13), I get around 3.18GInt/s.
GPU is Radeon Vega Frontier

The only problem with AMDGPU-PRO is that I cannot allocate Buffers larger than 4GByte... With ROCm I can.

//EDIT:
When adding ` -cl-denorms-are-zero` to the OpenCL kernel compilation parameters with ROCm, the performance is identical. Flags are `-O3 -cl-no-signed-zeros`

Does the AMDGPU-PRO driver automatically add this flag?