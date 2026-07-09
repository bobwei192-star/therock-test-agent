# [Issue]: gfx1201 (RDNA4) rejected by HIP runtime — "has 2 ISAs but can only support a single ISA"

- **Issue #:** 6110
- **State:** closed
- **Created:** 2026-04-02T18:04:28Z
- **Updated:** 2026-04-13T21:13:28Z
- **Labels:** status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6110

### Problem

HIP runtime fails to initialize on gfx1201 (RDNA4) GPUs. `hsa_agent_iterate_isas` returns two ISAs (`amdgcn-amd-amdhsa--gfx1201` and `amdgcn-amd-amdhsa--gfx12-generic`) but `rocdevice.cpp` rejects devices with more than one ISA.

### Reproduction

Any HIP program compiled for gfx1201:

```bash
hipcc test.hip -o test --offload-arch=gfx1201
AMD_LOG_LEVEL=3 ./test
```

Output:
```
rocdevice.cpp:442 : Initializing HSA stack.
rocdevice.cpp:590 : HSA device gfx1201 (PCI ID 7551) has 2 ISAs but can only support a single ISA
rocdevice.cpp:506 : Error creating new instance of Device.
free(): invalid pointer
```

### Root Cause

`rocdevice.cpp` around line 590 checks the ISA count returned by `hsa_agent_iterate_isas`. gfx1201 reports both `gfx1201` (specific) and `gfx12-generic`, but the code expects exactly one ISA per device.

The ISA table in `device.cpp:261` correctly has gfx1201 with `runtimeRocSupported = true`, but the device never reaches this lookup because it's rejected by the ISA count check.

### Workaround

LD_PRELOAD shim that intercepts `hsa_agent_iterate_isas` and filters out `gfx12-generic`:

```c
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdint.h>
#include <string.h>

typedef enum { HSA_STATUS_OK = 0 } hsa_status_t;
typedef struct { uint64_t handle; } hsa_agent_t;
typedef struct { uint64_t handle; } hsa_isa_t;
typedef hsa_status_t (*hsa_isa_callback_t)(hsa_isa_t isa, void *data);
typedef hsa_status_t (*iterate_isas_fn)(hsa_agent_t, hsa_isa_callback_t, void *);
typedef enum { HSA_ISA_INFO_NAME = 1 } hsa_isa_info_t;
typedef hsa_status_t (*isa_get_info_fn)(hsa_isa_t, hsa_isa_info_t, void *);

struct state { hsa_isa_callback_t cb; void *data; };

static hsa_status_t filter_cb(hsa_isa_t isa, void *data) {
    struct state *s = data;
    char name[256] = {0};
    static isa_get_info_fn gi = NULL;
    if (!gi) gi = (isa_get_info_fn)dlsym(RTLD_NEXT, "hsa_isa_get_info_alt");
    if (gi) gi(isa, HSA_ISA_INFO_NAME, name);
    if (strstr(name, "gfx1201")) return s->cb(isa, s->data);
    return HSA_STATUS_OK;
}

hsa_status_t hsa_agent_iterate_isas(hsa_agent_t agent, hsa_isa_callback_t cb, void *data) {
    static iterate_isas_fn real = NULL;
    if (!real) real = (iterate_isas_fn)dlsym(RTLD_NEXT, "hsa_agent_iterate_isas");
    struct state s = { .cb = cb, .data = data };
    return real(agent, filter_cb, &s);
}
```

```bash
gcc -shared -fPIC -o isa_filter.so isa_filter.c -ldl
LD_PRELOAD=./isa_filter.so ./your_hip_program
```

With the shim, gfx1201 initializes correctly and HIP compute works.

### Expected Fix

`rocdevice.cpp` should accept devices with multiple ISAs and use the most specific one (gfx1201 over gfx12-generic).

### Environment

- **GPU:** AMD Radeon AI PRO R9700 (gfx1201, RDNA4)
- **ROCm:** 7.2.0 and 7.2.1
- **OS:** Ubuntu 24.04, kernel 6.17.0
- **Impact:** Blocks all HIP compute on RDNA4 GPUs (RX 9070, 9060, R9700)