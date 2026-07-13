# [Issue]: Continued System Crashes with BOINC OpenCL Apps Since RDNA3 Release

- **Issue #:** 3575
- **State:** closed
- **Created:** 2024-08-13T06:31:06Z
- **Updated:** 2025-02-22T05:06:38Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3575

### Problem Description

Since launch of RDNA3, I have not been able to resume running BOINC many OpenCL apps that had been working for many years on AMDGPU.  Recently, ROCm 6.1 was released through my distro's official pkg repo, so I thought I would try again.  Things are better; I was able to get expected performance, no crashes, and no invalid results for the Einstein@Home O3MDF Gravitational Wave app.  However, BRP7 (Meerkat) app crashed the whole system.

### Operating System

Fedora Linux 40 (Workstation Edition)

### CPU

AMD Ryzen 9 5950X 16-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

Install BOINC & join Einstein@Home
Enable only BRP7 (Meerkat) app
System is very likely to crash moments after starting a work unit.  Some work units were completed as valid, however, so it isn't wasn't 100%. I estimate less than 2 hours MTBF.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

[rocminfo-support.log](https://github.com/user-attachments/files/16595198/rocminfo-support.log)


### Additional Information

[journal-10.log](https://github.com/user-attachments/files/16595278/journal-10.log)
[Task 1642166730 _ Einstein@Home.pdf](https://github.com/user-attachments/files/16595290/Task.1642166730._.Einstein%40Home.pdf)
