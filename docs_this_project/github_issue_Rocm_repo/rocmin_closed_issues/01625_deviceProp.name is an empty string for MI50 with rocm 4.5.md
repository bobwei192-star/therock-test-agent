# deviceProp.name is an empty string for MI50 with rocm 4.5 

- **Issue #:** 1625
- **State:** closed
- **Created:** 2021-11-22T22:07:50Z
- **Updated:** 2024-02-09T04:36:25Z
- **Labels:** Verified Issue, 4.5.0
- **Assignees:** gargrahul
- **URL:** https://github.com/ROCm/ROCm/issues/1625

In the case of using rocm 4.5 the `deviceProp.name` string does not contain the expected device name. 

The following code can reproduce the issue:

```
#include<iostream>
#include <hip/hip_runtime.h>
int main(){
  hipDeviceProp_t deviceProp;
  hipGetDeviceProperties(&deviceProp, 0);
  std::cout << deviceProp.name << std::endl;
}
```
This behaviour has been observed on a system with an MI50 accelerator