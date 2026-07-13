# [Issue]: Critical: ROCm 6.4.4 Core Dump with RDNA 4 (RX 9060 XT) - Basic Operations Fail

- **Issue #:** 5657
- **State:** closed
- **Created:** 2025-11-12T13:43:12Z
- **Updated:** 2025-12-03T15:24:01Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5657

### Problem Description

Subject: Critical: ROCm 6.4.4 Core Dump with RDNA 4 (RX 9060 XT) - Basic Operations Fail

Hardware:

AMD Radeon RX 9060 XT (gfx1100, Device ID: 7590)

Ubuntu 24.04.3 (officially supported)

Kernel 6.14.0-35-generic

Issue:
Basic GPU operations crash with core dump, including:

PyTorch: torch.tensor([1.0]).cuda() causes system crash

HIP: Simple vector addition kernel fails with addrlib.cpp assertion

Error:

text
test_hip: ./src/image/addrlib/src/core/addrlib.cpp:240: 
static ADDR_E_RETURNCODE rocr::Addr::Lib::Create(const rocr::ADDR_CREATE_INPUT*, rocr::ADDR_CREATE_OUTPUT*): 
Assertion `false' failed.
Aborted (core dumped)
Environment:

ROCm 6.4.4 (fresh install from official repo)

PyTorch 2.9.1+rocm6.4

All components verified at version 6.4.4

Expected:
Basic operations should work per AMD's compatibility statement.

Actual:
System crashes on fundamental GPU operations, making ROCm unusable with RDNA 4.

Request:
Please investigate this RDNA 4 compatibility issue and provide fix timeline.

### Operating System

Ubuntu 24.04.3

### CPU

Dell 7480 i7

### GPU

AMD Radeon RX 9060 XT (gfx1100, Device ID: 7590)

### ROCm Version

ROCm 6.4.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_