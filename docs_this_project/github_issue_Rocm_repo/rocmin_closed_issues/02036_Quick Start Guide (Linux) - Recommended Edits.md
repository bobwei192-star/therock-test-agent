# Quick Start Guide (Linux) - Recommended Edits

- **Issue #:** 2036
- **State:** closed
- **Created:** 2023-04-11T20:36:20Z
- **Updated:** 2024-01-10T22:06:54Z
- **Labels:** Documentation
- **Milestone:** 5.6.1
- **Assignees:** MathiasMagnus
- **URL:** https://github.com/ROCm/ROCm/issues/2036

Recommended edits:

1. Style

- ~~link to DKMS should follow conventions (i.e., spell out "Dynamic Kernel Module Support", use entire term as link to URL)~~

- unclear if "rocm-hip-libraries" is supposed to include a link (probably it should...)

2. Structure and Content
-  missing an overview of the process, a brief introduction providing a concise high-level review of the steps the user will have to take, e.g. verify prerequisites, add repositories, install drivers, etc.

- Unclear use of "each", spell out to what this refers: "This requires the Linux kernel headers and modules to be installed for each."

- ideally, to conclude the Quick Start process we should consider adding (1) a simple and clear criteria for successful installation (2) troubleshooting of possible errors (or link to troubleshooting page), and (3) possibly an uninstall procedure

- There is currently a major visual and flow/narration discrepancy between "Quick Start (Linux)" and the " Quick Start (Windows)".  These should be calibrated, I suggest by combining the advantages of both: 1. following the same structural themes in both, 2. adding more visual representations to the Linux Quick Start Guide