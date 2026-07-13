# Incomplete installation downgrading rocm from 4 to 3.9.1?

- **Issue #:** 1409
- **State:** closed
- **Created:** 2021-03-19T14:49:45Z
- **Updated:** 2021-03-22T04:07:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1409

I tried deleting the folder /opt/rocm-4.0.1 and then installing rocm-3.9.1 (since I realized it does not support Radeon RX580 anymore). But when I try to run tensorflow I get:

```
ImportError: libamdhip64.so.4: cannot open shared object file: No such file or directory
```

Is there a way to fix that?
