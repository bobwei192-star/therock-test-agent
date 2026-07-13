# amd-smi does not work

- **Issue #:** 4216
- **State:** closed
- **Created:** 2025-01-02T20:47:57Z
- **Updated:** 2025-03-21T06:04:43Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4216

### Problem Description

The amd-smi command does not work after installing rocm.

LM 22.  rocm 6.2.1.

Error message:

```bash
amd-smi --help
/opt/rocm-6.2.1/libexec/amdsmi_cli/BDF.py:126: SyntaxWarning: invalid escape sequence '\.'
  bdf_regex = "(?:[0-6]?[0-9a-fA-F]{1,4}:)?[0-2]?[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}\.[0-7]"
Still couldn't import 'amdsmi related scripts'. Make sure it's installed in /usr/bin/../libexec/amdsmi_cli
```

I've already done a reinstall via amdgpu_install.

### Operating System

LM 22

### CPU

AMD Ryzen 9 7950X3D

### GPU

AMD Navi 33 [Radeon RX 7600/7600 XT/7600M XT/7600S/7700S / PRO     W7600]

### ROCm Version

ROCm 6.2.1

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_