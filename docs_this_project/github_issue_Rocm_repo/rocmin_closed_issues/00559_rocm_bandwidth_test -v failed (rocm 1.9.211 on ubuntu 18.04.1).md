# rocm_bandwidth_test -v failed (rocm 1.9.211 on ubuntu 18.04.1)

- **Issue #:** 559
- **State:** closed
- **Created:** 2018-09-26T17:13:28Z
- **Updated:** 2018-09-28T20:39:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/559

* OS Platform and Distribution (e.g., Linux Ubuntu 16.04):
Ubuntu 18.04.1 (Kernel version: 4.15.0-35-generic #38-Ubuntu SMP)
rocm version : 1.9.211
rocm-opencl: 1.2.0-2018090737

* GPU model and memory:
Vega Frontier Edition (connected via PCIe riser) + onboard VGA
Motherboard: Supermicro X10SRL-F
CPU: Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz

* Problem:
After a clean boot, rocm_bandwidth_test -v reports error:

$ /opt/rocm/bin/rocm_bandwidth_test -v

    RocmBandwidthTest Version: 1.0.0

    Device: 0,  Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
    Device: 1,  Vega 10 XTX [Radeon Vega Frontier Edition]

    Device Access

    D/D       0         1

    0         1         1

    1         1         1


    Data Path Validation

    D/D       0           1

    0         N/A         FAIL

    1         FAIL        PASS

Relevant logs attached.
[vega-10-rocm-logs.txt](https://github.com/RadeonOpenCompute/ROCm/files/2420813/vega-10-rocm-logs.txt)
