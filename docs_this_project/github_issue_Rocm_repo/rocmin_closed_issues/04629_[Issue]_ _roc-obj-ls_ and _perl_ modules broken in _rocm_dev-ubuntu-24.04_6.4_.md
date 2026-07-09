# [Issue]: `roc-obj-ls` and `perl` modules broken in `rocm/dev-ubuntu-24.04:6.4`

- **Issue #:** 4629
- **State:** closed
- **Created:** 2025-04-15T15:26:19Z
- **Updated:** 2025-04-24T19:10:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4629

### Problem Description

The script `roc-obj-ls` and perl modules are broken in `rocm/dev-ubuntu-24.04:6.4`.

Calling `roc-obj-ls` results in an error message like:

```
Can't locate File/Which.pm in @INC (you may need to install the File::Which module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.38.2 /usr/local/share/perl/5.38.2 /usr/lib/x86_64-linux-gnu/perl5/5.38 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.38 /usr/share/perl/5.38 /usr/local/lib/site_perl) at /usr/bin/roc-obj-ls line 25.
1.404 BEGIN failed--compilation aborted at /usr/bin/roc-obj-ls line 25.
```

This is a reproducer:

<details>
<summary>
Dockerfile
</summary>

```
FROM rocm/dev-ubuntu-24.04:6.4

COPY <<EOF saxpy.cpp
#include <hip/hip_runtime.h>

__global__ void saxpy_kernel(const float a, const float* d_x, float* d_y, const unsigned int size)
{
    const unsigned int global_idx = blockIdx.x * blockDim.x + threadIdx.x;

    if(global_idx < size) {
        d_y[global_idx] = a * d_x[global_idx] + d_y[global_idx];
    }
}
EOF

RUN <<EOF
    hipcc --offload-arch=gfx906 -c saxpy.cpp -o saxpy.o

    roc-obj-ls -v saxpy.o
EOF
```
</details>

Running this file with `docker buildx build -f Dockerfile .` produces the above mentioned error message.

Issue observed while upgrading our code base to rocm 6.4 with @romintomasetti.

### Operating System

Ubuntu 24.04

### CPU

AND Ryzen 5950x

### GPU

Radeon Pro VII

### ROCm Version

ROCm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_