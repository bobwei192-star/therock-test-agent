# rocm-smi 4.1 returns error

- **Issue #:** 1446
- **State:** closed
- **Created:** 2021-04-09T02:37:12Z
- **Updated:** 2021-04-12T07:32:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/1446

```
python3 /opt/rocm/bin/rocm_smi.py
Failed to get "domain" properity from properties files for kfd node 1.
rsmi_init() failed
Exception caught: rsmi_init.
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
```

but rocminfo work perfect