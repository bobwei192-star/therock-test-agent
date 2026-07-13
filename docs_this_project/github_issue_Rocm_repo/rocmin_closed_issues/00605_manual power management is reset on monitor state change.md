# manual power management is reset on monitor state change.

- **Issue #:** 605
- **State:** closed
- **Created:** 2018-11-07T08:02:52Z
- **Updated:** 2019-03-17T17:21:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/605

ROCm 1.9.1 OpenCL, Ubuntu 18.10, two Vega 64 GPUs reference air.

I have two GPUs that I use mainly for compute (OpenCL), but one of them also drives the monitor.

I manually set the power state on the GPUs with: rocm-smi --setsclk 5
(which brings the power use per GPU around 150W and prevents thermal throttling).

But, on some monitor actions such as:
- monitor enters "power save" mode (triggered with "Lock screen", keyboard Super+L)
- monitor power ON (following manual monitor power OFF using the monitor switch)
- monitor DP cable reconnect to the GPU (following manual DP cable unplug from GPU)

the power state is reset on the GPU that is connected to the monitor. It seems it is set to state "6" (instead of the state "5" that I set manually), which uses around 200W of power, and overheats + thermal throttling the GPU.

In practice, after each such monitor action, I have to re-issue the rocm-smi --setsclk 5 to bring the GPU back to the desired state.

This is a long-standing issue for me, not limited to ROCm 1.9.1 or Ubuntu 18.10 (I've seen it with other version previously). It happens every time, thus should be easy to reproduce.
