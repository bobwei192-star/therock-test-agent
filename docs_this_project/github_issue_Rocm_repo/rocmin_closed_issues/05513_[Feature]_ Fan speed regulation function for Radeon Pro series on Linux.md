# [Feature]: Fan speed regulation function for Radeon Pro series on Linux

- **Issue #:** 5513
- **State:** closed
- **Created:** 2025-10-14T07:25:04Z
- **Updated:** 2026-01-02T18:25:26Z
- **Labels:** Feature Request, status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5513

### Suggestion Description

**Fan regulation function needed!**
Fan speed could affect the performance hugely! When conducting AI training, I notice that the temperature of my W7900 is extremely high, with a junction temperature up to 90 degrees while the fan speed is just about 50%. High temperatures would have a serious negative on the lifetime of the card and might lead to stability issues.
**Linux is not yet supported through rocm-smi**
I notice that the current fan regulation function is only limited to windows system. ROCm-smi on Linux seems to be banned for pro series. When setting fan speed, an output shows that regulate successfully will be given. But there's no actual difference. The output is as follows.

<img width="975" height="512" alt="Image" src="https://github.com/user-attachments/assets/cfeafbd6-11c8-4581-8fce-49030a48c56d" />


### Operating System

Ubuntu 24.04.5 LTS

### GPU

Radeon Pro W7900/W7900 Dual Slot

### ROCm Component

_No response_