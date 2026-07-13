# roctracer headers do not follow include rules

- **Issue #:** 1830
- **State:** closed
- **Created:** 2022-10-11T15:32:56Z
- **Updated:** 2024-02-19T12:20:00Z
- **Labels:** Verified Issue, 5.3.0, 5.3.1, 5.2.0, 5.4.0, 5.3.2
- **Assignees:** nunnikri, frepaul, raramakr
- **URL:** https://github.com/ROCm/ROCm/issues/1830

Starting with [ROCm 5.2](https://docs.amd.com/bundle/ROCm-Release-Notes-v5.2/page/Deprecations_and_Warnings.html), the headers advertise to use `/opt/rocm-ver/include/` as the `-I`-flag and prefix the headers with the component `roctracer`. But the headers from roctracers are not usable this way:

An example when including `<roctracer/roctracer.h>:

```
/opt/rocm-5.2.3/include/roctracer/roctracer.h:45:10: error: 'ext/prof_protocol.h' file not found with <angled> include; use "quotes" instead
#include <ext/prof_protocol.h>  
         ^~~~~~~~~~~~~~~~~~~~~  
         "ext/prof_protocol.h"  
1 error generated.
```

Here is a script to check all headers:


```sh
find /opt/rocm-5.2.3/include/roctracer -maxdepth 1 -type f -printf '%f\n' |
    while read header
    do
        cat >includetest.cc <<EOF
#include <roctracer/$header>
EOF
        echo $header
        amdclang++ \
            -D__HIP_PLATFORM_AMD__ \
            -E includetest.cc \
            -o includetest.i \
            -I/opt/rocm-5.2.3/include 2>&1 | head -n 23
    done
