# program got stuck in the hipMemcpy() function

- **Issue #:** 1627
- **State:** closed
- **Created:** 2021-11-24T06:02:23Z
- **Updated:** 2021-11-29T08:48:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1627

hello,
I installed ROCm-4.5 on my machine following [this](https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html) guide,
my GPU is  gfx906 and my system is ubuntu20.04, but things do not go well
when I use `hipcc` compiled this code(which I got in the rocblas's doc), but when I run this program, it got stuck in the first hipMemcpy() function, and with no response feedback, no error and no warning, I think I may have missed something during the installation of rocm. but I have no idea how to find out where it goes wrong.
please help me.
this is the test code:
```c++
#include <iostream>
#include <vector>
#include "hip/hip_runtime_api.h"
#include "rocblas.h"
using namespace std;

int main()
{
    rocblas_int n = 10240;
    float alpha = 10.0;
    vector<float> hx(n);
    vector<float> hz(n);
    float* dx;
    rocblas_handle handle;
    rocblas_create_handle(&handle);

    hipMalloc(&dx, n * sizeof(float));

    srand(1);
    for( int i = 0; i < n; ++i )
    {
        hx[i] = rand() % 10 + 1; 
    }

    cout << "hello?" << endl;
    hipMemcpy(dx, hx.data(), sizeof(float) * n, hipMemcpyHostToDevice);
    cout << "hello? again" << endl;

    rocblas_status status = rocblas_sscal(handle, n, &alpha, dx, 1);
    if(status == rocblas_status_success)
    {
        cout << "status == rocblas_status_success" << endl;
    }
    else
    {
        cout << "rocblas failure: status = " << status << endl;
    }
    hipMemcpy(hx.data(), dx, sizeof(float) * n, hipMemcpyDeviceToHost);

    hipFree(dx);
    rocblas_destroy_handle(handle);
    return 0;
}
// the compile command
// hipcc test03.cpp -o t3 -lrocblas -lamdhip64 -I/opt/rocm/include -L/opt/rocm/lib
```
