# printf on device fails to print some elements after string justification

- **Issue #:** 5425
- **State:** closed
- **Created:** 2025-09-24T16:47:58Z
- **Updated:** 2026-01-14T18:09:02Z
- **Labels:** status: fix submitted
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5425

a.cpp:
``` hip
#include <hip/hip_runtime.h>

__global__ void kernel()
{
	printf("device\n");
	printf("  %10s %i\n", "123", 1);
	printf("  %10s %i\n", "12345678", 1);
}

int main()
{
	printf("host\n");
	printf("  %10s %i\n", "123", 1);
	printf("  %10s %i\n", "12345678", 1);
	hipLaunchKernelGGL(kernel, 1, 1, 0, 0);
	hipDeviceSynchronize();
}
```

```
hipcc a.cpp
```

output:
```
host
         123 1
    12345678 1
device
         123     12345678 1
```

rocm 6.4.3