# Help with RadeonVII error "atombios stuck in a loop" (not a ROCm issue)

- **Issue #:** 1320
- **State:** closed
- **Created:** 2020-12-05T11:24:30Z
- **Updated:** 2020-12-08T05:48:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1320

This is not a ROCm issue, I know; but maybe somebody in the know could kindly help me a bit:

On Ubuntu 20.04 (Linux kernel 5.3.0-18) a Radeon VII GPU fails at initialization (boot) time with this message in dmesg:
```
[drm:atom_op_jump [amdgpu]] *ERROR* atombios stuck in loop for more than 5secs aborting
[drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9300 (len 1031, WS 12, PS 8) @ 0x93A0
[drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9274 (len 63, WS 0, PS 8) @ 0x9295
amdgpu 0000:67:00.0: gpu post error!
amdgpu 0000:67:00.0: Fatal error during GPU init
[drm] amdgpu: finishing device.
```

What does this mean -- is the GPU hardware-damaged beyond repair? or is there anything that can be done to fix the GPU?

Thank you!
