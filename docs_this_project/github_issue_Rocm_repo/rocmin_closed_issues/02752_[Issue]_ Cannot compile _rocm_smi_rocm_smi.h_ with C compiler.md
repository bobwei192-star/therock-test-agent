# [Issue]: Cannot compile `rocm_smi/rocm_smi.h` with C compiler

- **Issue #:** 2752
- **State:** closed
- **Created:** 2023-12-19T13:44:06Z
- **Updated:** 2024-01-09T17:22:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/2752

### Problem Description

This header does not compile with any C compiler. I already reported this to @vlaindic via mail.

### Operating System

Docker image rocm/dev-ubuntu-22.04:6.0

### CPU

any

### GPU

Other

### Other

any

### ROCm Version

ROCm 6.0.0

### ROCm Component

rocm_smi_lib

### Steps to Reproduce

```console
$ docker run --rm -it rocm/dev-ubuntu-22.04:6.0
# echo '#include <rocm_smi/rocm_smi.h>' >test.c
# /opt/rocm-6.0.0/bin/amdclang -I/opt/rocm-6.0.0/include -c test.c
In file included from test.c:1:
/opt/rocm-6.0.0/include/rocm_smi/rocm_smi.h:5370:51: error: must use 'struct' tag to refer to type 'metrics_table_header_t'
rsmi_dev_metrics_header_info_get(uint32_t dv_ind, metrics_table_header_t* header_value);
                                                  ^
                                                  struct 
1 error generated.
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_