# [OpenCL] Warning: Use of non-host signal in host signal wait API (4.1.0)

- **Issue #:** 1426
- **State:** closed
- **Created:** 2021-03-24T20:06:53Z
- **Updated:** 2021-03-25T11:14:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1426

Hello, after the update to 4.1.0 I am getting a lot of this warning when running opencl applications:

`Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), <<private builds directory>>/hsa-rocr/src/ROCR-Runtime-rocm-4.1.0/src/core/runtime/default_signal.cpp:87`

It looks like it is making reference to the directory it was built from.