# [Feature]: A method to automatically determine the latest ROCm release that supports ROCm on WSL

- **Issue #:** 5557
- **State:** closed
- **Created:** 2025-10-22T00:42:30Z
- **Updated:** 2025-11-06T20:18:18Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5557

### Suggestion Description

I have written a simple bash script called [rocm-latest][ref-script] that parses the repo.radeon.com website to find the latest version of ROCm. It works well but I wanted to add a mode that detects the same for WSL and this is tricky. Can you advise or create a easier way to determine which release of ROCm is the most recent that includes WSL support? Right now I walk the repo looking for versions that have the wsl version of the ROCr runtime library. But that seems to generate results that do not line up with the documentation [here][ref-docs].

[ref-script]: https://github.com/sbates130272/batesste-ansible/blob/main/roles/rocm_setup/files/rocm-latest
[ref-docs]: https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/compatibility/compatibilityrad/wsl/wsl_compatibility.html

### Operating System

Ubuntu (and others)

### GPU

All

### ROCm Component

All