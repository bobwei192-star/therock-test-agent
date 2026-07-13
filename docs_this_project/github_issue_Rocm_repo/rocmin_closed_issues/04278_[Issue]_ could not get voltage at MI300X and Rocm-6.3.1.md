# [Issue]: could not get voltage at MI300X and Rocm-6.3.1

- **Issue #:** 4278
- **State:** closed
- **Created:** 2025-01-21T01:35:05Z
- **Updated:** 2025-01-22T14:41:36Z
- **Labels:** Under Investigation, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4278

### Problem Description

hi, I have a 8 x MI300X system, could not get voltage at MI300X and Rocm-6.3.1

When I run below command, I get:
 rocm-smi --showvoltage


============================ ROCm System Management Interface ============================
==================================== Current voltage =====================================
GPU[0]          : get_volt_metric, Not supported on the given system
GPU[1]          : get_volt_metric, Not supported on the given system
GPU[2]          : get_volt_metric, Not supported on the given system
GPU[3]          : get_volt_metric, Not supported on the given system
GPU[4]          : get_volt_metric, Not supported on the given system
GPU[5]          : get_volt_metric, Not supported on the given system
GPU[6]          : get_volt_metric, Not supported on the given system
GPU[7]          : get_volt_metric, Not supported on the given system
==========================================================================================
================================== End of ROCm SMI Log ===================================

Is it rocm-6.3.1 too new to support this feature? is that will be ok if i install a lower version of Rocm-6.0.
or it's because MI300X hardware does not open this feature?

### Operating System

Ubuntu VERSION="22.04.5 LTS (Jammy Jellyfish)"

### CPU

Intel(R) Xeon(R) Platinum 8470

### GPU

AMD MI300X

### ROCm Version

ROCm 6.3.0

### ROCm Component

rocm_smi_lib

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_