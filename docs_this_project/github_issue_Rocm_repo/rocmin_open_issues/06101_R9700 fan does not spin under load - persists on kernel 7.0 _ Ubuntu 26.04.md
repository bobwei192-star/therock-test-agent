# R9700 fan does not spin under load - persists on kernel 7.0 / Ubuntu 26.04

- **Issue #:** 6101
- **State:** open
- **Created:** 2026-03-31T13:52:36Z
- **Updated:** 2026-06-09T22:03:02Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6101

**Hardware:** ASUS Turbo Radeon AI Pro R9700 32GB
**vBIOS:** 115-G287BP00-100
**OS:** Ubuntu 26.04 beta (Resolute Raccoon)
**Kernel:** 7.0.0-10-generic
**ROCm:** 7.2.1
**AMDGPU driver:** 6.16.13 (out-of-tree) and kernel built-in tested
**linux-firmware:** 20260319.git217ca6e4 (March 2026)

## Issue

The GPU fan does not spin under any load on Linux. During AI training the GPU reached 109°C and thermally throttled with the fan physically stationary throughout. This is a serious hardware safety issue.

## SMU Firmware Mismatch (root cause)

Present on every kernel and driver version tested:

```
amdgpu 0000:2d:00.0: smu driver if version = 0x0000002e (46)
amdgpu 0000:2d:00.0: smu fw if version = 0x00000032 (50)
amdgpu 0000:2d:00.0: smu fw version = 0x00684b00 (104.75.0)
amdgpu 0000:2d:00.0: SMU driver if version not matched
```

The card firmware is 4 interface versions ahead of what the AMDGPU driver supports. Fan control registers are inaccessible as a result.

## Technical Findings

- `rocm-smi --setfan` returns 'Not supported on this system'
- sysfs `pwm1` node is READ-ONLY (-r--r--r--)
- `fan1_enable` returns 'Invalid argument'
- GPU enters runtime power suspend under load, suppressing fan response
- Fan physically stationary at 109°C during AI training
- LACT 0.8.4 fan control grayed out

## Tested Configurations - Mismatch Persists On All

| Kernel | AMDGPU Driver | OS | Result |
|--------|--------------|-----|--------|
| 6.14.0-37 | 6.16.13 (out-of-tree) | Ubuntu 24.04 | SMU mismatch, fan not spinning |
| 6.17.0-19 | 6.16.6 (out-of-tree) | Ubuntu 24.04 | SMU mismatch, fan not spinning |
| 6.17.0-19 | 6.16.13 (out-of-tree) | Ubuntu 24.04 | SMU mismatch, fan not spinning |
| 6.18.20 | N/A | Ubuntu 24.04 | Kernel panic - unbootable |
| 6.19.10 | N/A | Ubuntu 24.04 | Kernel panic - unbootable |
| 7.0.0-10 | built-in | Ubuntu 26.04 beta | SMU mismatch, fan not spinning |linux-firmware updated to March 2026 (20260319) — no change.

## Request

The AMDGPU driver needs to be updated to support SMU interface version 50 (0x00000032) as shipped on the R9700 (gfx1201, RDNA 4). This issue makes the card unsafe for its primary use case of sustained AI/ML workloads on Linux.

Related: #5908