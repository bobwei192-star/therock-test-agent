# [Issue]: amdgpu: Idle-Temperaturen höher als unter Windows, Zero-Fan-Modus instabil (Sapphire RX 570 Nitro+)

- **Issue #:** 5471
- **State:** closed
- **Created:** 2025-10-05T12:50:11Z
- **Updated:** 2025-10-21T14:28:18Z
- **Labels:** ROCm 6.3.1, status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5471

### Problem Description

Description:
My AMD Sapphire Radeon RX 570 Nitro+ 8GB GDDR5 graphics card gets warmer when idle under Linux (kernel 6.8.0-85-generic) than under Windows.

Idle temperatures: Linux ~53°C, Windows ~44°C

Without dynamic fan control, the fans constantly cycle on/off.

With LACT, temperatures remain normal, but the fans produce an audible whirring noise shortly before shutdown.

Expected behavior:

GPU idle temperature should not be higher than under Windows.

Zero-fan mode should work reliably without fans speeding up unnecessarily.

Steps to reproduce:

Boot the system without load.

Monitor idle temperatures (e.g., sensors or /sys/class/drm/card0/device/hwmon/hwmon*/temp1_input).

Compare with Windows idle temperatures on the same system.

Additional information:

LACT corrects the temperature issue, but causes shutdown noise.

Improving zero-fan support and fan control in the amdgpu driver may resolve the issue.

### Operating System

Linux Mint 22.2

### CPU

Ryzen 5 1600

### GPU

AMD Sapphire Nitro RX 570 8 GB

### ROCm Version

6.3.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_