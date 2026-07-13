# [Issue]: HIPCC: Unusual performance drop when copying an array of struct and not going through a local variable

- **Issue #:** 4331
- **State:** open
- **Created:** 2025-02-03T15:25:36Z
- **Updated:** 2025-02-04T15:17:42Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4331

### Problem Description

HIPCC seems to be producing slower code when loading/storing a structure from/to global memory directly vs. going through a local variable before storing to gmem.

The first example (top row of editor/compiler pair) loads the structure from global memory (from `input`) and directly stores to `output`.
The second (bottom row) example does the same but it goes through a local variable before storing to `output`.

The second example is ~3x faster on my machine. Is that expected?

RGP profiler captures of the code on my machine (ROCm 5.7.1):

Slower example:
![Image](https://github.com/user-attachments/assets/6d80dfca-7433-409b-87d2-ffbaec4f57bc)

Faster example with a local variable:
![Image](https://github.com/user-attachments/assets/79bc4efa-3d20-4af4-aa15-d8ed96605ccc)

### Operating System

Windows 11

### CPU

Intel i5 13600KF

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 5.7.1 (local machine), ROCm 6.1.2 (through [Compiler Explorer](https://godbolt.org/))

### ROCm Component

HIP, HIPCC

### Steps to Reproduce

ROCm 6.1.2 compiler explorer reproducer: https://godbolt.org/z/MME7z5Pj5

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_