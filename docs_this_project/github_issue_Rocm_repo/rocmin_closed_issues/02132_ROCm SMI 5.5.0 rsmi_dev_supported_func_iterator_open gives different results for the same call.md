# ROCm SMI 5.5.0 rsmi_dev_supported_func_iterator_open gives different results for the same call

- **Issue #:** 2132
- **State:** closed
- **Created:** 2023-05-12T05:23:25Z
- **Updated:** 2024-08-15T14:52:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/2132

When calling `rsmi_dev_supported_func_iterator_open` the first time on an "AMD Ryzen 7 PRO 4750U with Radeon Graphics" laptop it returns `RSMI_STATUS_INTERNAL_EXCEPTION`, but calling it the second time with the same arguments returns `RSMI_STATUS_SUCCESS`. See example:

```c
#include <rocm_smi/rocm_smi.h>

int
main(int ac, char *av[])
{
    rsmi_status_t status = rsmi_init(0);
    if (status != RSMI_STATUS_SUCCESS) abort();

    uint32_t device_count;
    status = rsmi_num_monitor_devices(&device_count);
    if (status != RSMI_STATUS_SUCCESS) abort();

    uint32_t dev;
    for (dev = 0; dev < device_count; ++dev) {
        rsmi_func_id_iter_handle_t iter;
        status = rsmi_dev_supported_func_iterator_open(dev, &iter);
        fprintf(stderr, "first call dev#%d:  %d\n", dev, status);
        status = rsmi_dev_supported_func_iterator_open(dev, &iter);
        fprintf(stderr, "second call dev#%d: %d\n", dev, status);
        if (status == RSMI_STATUS_SUCCESS) {
            status = rsmi_dev_supported_func_iterator_close(&iter);
            if (status != RSMI_STATUS_SUCCESS) abort();
        }
    }

    rsmi_shut_down();

    return 0;
}
```

Output:

```
first call dev#0:  6
second call dev#0: 0
```

This behavior brakes the ROCm PAPI component, as it does two passes over all devices. First just counts the available events and the second pass queries all features of the events. With this behavior the first pass delivers a lower number of events than the second discovers and breaks it. See here: https://bitbucket.org/icl/papi/issues/134

I'm aware that this is not a supported ROCm platform, but the behavior should nevertheless be consistent.