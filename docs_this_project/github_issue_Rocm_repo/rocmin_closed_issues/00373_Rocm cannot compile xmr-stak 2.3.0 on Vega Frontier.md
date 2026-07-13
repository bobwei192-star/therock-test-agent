# Rocm cannot compile xmr-stak 2.3.0 on Vega Frontier

- **Issue #:** 373
- **State:** closed
- **Created:** 2018-03-26T01:28:50Z
- **Updated:** 2018-03-26T15:37:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/373

In preparation for POW change, i tried the newly released xmr-stak 2.3.0 and get the following error. 

-------------------------------------------------------------------
xmr-stak 2.3.0 a036cd8

Brought to you by fireice_uk and psychocrypt under GPLv3.
Based on CPU mining code by wolf9466 (heavily optimized by fireice_uk).
Based on OpenCL mining code by wolf9466.

Configurable dev donation level is set to 2.0%

You can use following keys to display reports:
'h' - hashrate
'r' - results
'c' - connection
-------------------------------------------------------------------
[2018-03-25 20:13:36] : Mining coin: monero
[2018-03-25 20:13:36] : Compiling code and initializing GPUs. This will take a w                                               hile...
[2018-03-25 20:13:36] : Device 0 work size 8 / 32.
[2018-03-25 20:13:37] : OpenCL device 0 - Precompiled code /home/xxx/.openclcach                                               e/dbb76e4a654cad114d7de496f11795ef645d53a661526a91abd792b656235acf.openclbin not                                                found. Compiling ...
[2018-03-25 20:13:37] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgr                                               am.
Build log:
Error: Failed to compile opencl source (from CL to LLVM IR).

Previous version works.

Might be a compilier issue, any help will be appreciated.

Thank you!