# Warning: Use of non-host signal in host signal wait API (version 4.1.0)

- **Issue #:** 1436
- **State:** closed
- **Created:** 2021-04-01T20:29:50Z
- **Updated:** 2023-07-24T10:45:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1436

I've built the ROCm 4.1.0 toolchain from source similar to #1426, but on Ubuntu 20.04 with AMD Threadripper 1950x and AMD Radeon Vega 64 Frontier Edition.  I get multiple warnings like this when running simple hipified code:

```Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), <<private builds directory>>/ROCm/ROCR-Runtime/src/core/runtime/default_signal.cpp:87```

The code apparently executes correctly, but do you know the significance of these warnings?  I've looked at the source for the signals warning, but it's not clear if these have performance implications or can just be safely ignored.