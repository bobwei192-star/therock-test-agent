# [Issue]: Wrong return result from cooperative_groups::grid_group::group_dim on 9070XT

- **Issue #:** 5236
- **State:** closed
- **Created:** 2025-08-29T08:06:48Z
- **Updated:** 2025-09-15T14:04:51Z
- **Labels:** Under Investigation
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5236

### Problem Description

cooperative_groups::grid_group::group_dim returns  blockDim not gridDim on 9070XT, this let the behavior of cooperative_groups::grid_group::group_dim same as cooperative_groups::thread_block::group_dim.

cooperative_groups::grid_group::group_dim shall return gridDim to align the behavior of described in ROCm document https://rocm.docs.amd.com/projects/HIP/en/latest/doxygen/html/group___cooperative_g.html#ga33c3fba456790c2addf3bfa4be211053

The dim of grid group shall be gridDim not blockDim or the functionality totally doesn't make sense.

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 7900X3D 12-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 7.0.0 rc1

### ROCm Component

HIP

### Steps to Reproduce

Sample code:

```
#include <hip/hip_runtime.h>
#include <hip/hip_cooperative_groups.h>


__global__ void test() {
    auto grid = cooperative_groups::this_grid();
    auto thread_block = cooperative_groups::this_thread_block();
    
    if(grid.thread_rank() == 0 && blockIdx.x == 0 && blockIdx.y == 0) {
        printf("grid group_dim x: %i, y: %i, z: %i\n", grid.group_dim().x, grid.group_dim().y, grid.group_dim().z);
        printf("block group_dim x: %i, y: %i, z: %i\n", thread_block.group_dim().x, thread_block.group_dim().y, thread_block.group_dim().z);
    }
}

int main(int argc, char* argv[]) {
    test<<<dim3(32, 16, 1), dim3(32, 4, 1), 0, 0>>>();
    return 0;
} 
```

Compile command:
```
/opt/rocm/lib/llvm/bin/clang++ --offload-arch=gfx1201 -xhip main.hip -o main
```

Output:
```
grid group_dim x: 32, y: 4, z: 1
block group_dim x: 32, y: 4, z: 1
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_