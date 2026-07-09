# rocm-smi: not reporting GPU power (regression in 1.7)

- **Issue #:** 305
- **State:** closed
- **Created:** 2018-01-21T12:02:48Z
- **Updated:** 2018-06-03T15:30:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/305

With ROCm 1.7, Ubuntu 16.04.3, Vega64:

The rocm-smi that comes with 1.7 (located at /opt/rocm/bin/rocm-smi ) does not report GPU power when invoked with "rocm-smi -a". It says:
GPU[0] 		: Cannot get GPU power Consumption: Average GPU Power not supported

But, some old rocm-smi script (from 1.6 era) did detect and report correctly the power on "rocm-smi -a".

What's more, the new (1.7) rocm-smi does detect GPU power when invoked without arguments:
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   50.0c   8.0W     852Mhz   500Mhz   12.94%   auto      0%

So this seems to be a simple regression in the script itself.