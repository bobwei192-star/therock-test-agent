# AMD SMI CLI triggers repeated kernel errors on GPUs with partitioning support

- **Issue #:** 5720
- **State:** closed
- **Created:** 2025-11-28T17:28:49Z
- **Updated:** 2026-01-28T16:18:33Z
- **Labels:** Verified Issue, ROCm 7.1.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5720

Running the `amd-smi` CLI on GPUs with partitioning support, such as the AMD
Instinct MI300 series, might produce repeated kernel error messages in the
system logs. This occurs when `amd-smi` attempts to open the GPU
partition device nodes `/dev/dri/renderD*` during the permission checks. On
GPUs with partitioning support, unconfigured partition devices are
intentionally invalid until configured. As a result, the AMD GPU Driver (amdgpu)
logs errors in `dmesg`, such as: 

```
amdgpu 0000:15:00.0: amdgpu: renderD153 partition 1 not valid!
```

These repeated kernel logs can clutter the system logs and may cause
unnecessary concern about GPU health. However, this is a non-functional issue
and does not affect AMD SMI functionality or GPU performance. This issue will
be fixed in a future ROCm release.