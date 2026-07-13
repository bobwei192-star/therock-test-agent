# [OMPT] `ompt_get_num_devices` returns a value of `1` regardless of the number of devices present

- **Issue #:** 2057
- **State:** closed
- **Created:** 2023-04-17T11:48:20Z
- **Updated:** 2024-08-07T19:25:20Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2057

**Description:**

The OMPT interface offers several functions to allow the interface to retrieve information, for example about the number of GPUs present. This function is called `ompt_get_num_devices`. The function pointer will be returned upon calling the lookup function passed during the tool initialization. 

The lookup functions are required by the OpenMP standard. [Section 19.5 of the OpenMP Standard 5.2 specifications](https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-5-2.pdf#page=493) states the following restriction:
> Tool callbacks may not use OpenMP directives or call any runtime library routines described in Chapter 18.

While the function `omp_get_num_devices` works fine (outside of callback regions in the OMPT interface), `ompt_get_num_devices` does not. Regardless when the function is called, the returned value is always a fixed value of `1`. This can be explained by the [source code behind this function](https://github.com/RadeonOpenCompute/llvm-project/blob/amd-stg-open/openmp/runtime/src/ompt-general.cpp#L857):

```C
OMPT_API_ROUTINE int ompt_get_num_devices(void) {
  return 1; // only one device (the current device) is available
}
```

This issue can affect the proper initialization of the OMPT interface when trying to allocate buffers. Without this function, one would need to check the `device_num` in each `ompt_device_initialize` to allocate buffers accordingly. This is possible, but not ideal. 

**Reproduce the issue:**
On a system with more than one available AMD GPU, you can use the following source code:

```C
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <omp-tools.h>

ompt_finalize_tool_t ompt_finalize_tool;

static int
initialize_tool( ompt_function_lookup_t lookup,
                 int                    initialDeviceNum,
                 ompt_data_t*           toolData )
{
    ompt_set_callback_t set_callback =
        ( ompt_set_callback_t )lookup( "ompt_set_callback" );
    assert( set_callback != 0 );
    ompt_finalize_tool =
        ( ompt_finalize_tool_t )lookup( "ompt_finalize_tool" );
    assert( ompt_finalize_tool != 0 );
    ompt_get_num_devices_t get_num_devices =
        ( ompt_get_num_devices_t )lookup( "ompt_get_num_devices" );
    assert( get_num_devices != 0 );
    int num_devices = get_num_devices();
    assert( num_devices > 1 );

    return 1;
}

static void
finalize_tool( ompt_data_t* toolData )
{
    printf("%s\n", __FUNCTION__);
}

ompt_start_tool_result_t*
ompt_start_tool( unsigned int omp_version, /* == _OPENMP */
                 const char*  runtime_version )
{
    static ompt_start_tool_result_t tool = { &initialize_tool,
                                             &finalize_tool,
                                             ompt_data_none };
    return &tool;
}

#define N 10
int main(void) {
    int a[N];
    #pragma omp target map(a[:N])
    {
        a[N-1] = 0;
    }
    ompt_finalize_tool();
    return a[N - 1];
}
```

Compiling and running the tool with ROCm 5.4.x yields the following output

```bash
> amdclang -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a -O3 -g error_ompt_get_num_devices.c -o error_ompt_get_num_devices
> ./error_ompt_get_num_devices 
error_ompt_get_num_devices: error_ompt_get_num_devices.c:23: int initialize_tool(ompt_function_lookup_t, int, ompt_data_t *): Assertion `num_devices > 1' failed.
Aborted
```