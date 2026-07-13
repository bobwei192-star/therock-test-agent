# Error in Linux Quickstart Documentation

- **Issue #:** 2231
- **State:** closed
- **Created:** 2023-06-09T12:32:20Z
- **Updated:** 2023-06-09T19:56:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/2231

On the page [https://rocm.docs.amd.com/en/latest/deploy/linux/quick_start.html](https://rocm.docs.amd.com/en/latest/deploy/linux/quick_start.html) there is an error in the `Add the repositories` Ubuntu 22.04 section. The line `echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600` is misplaced and causes issues with apt.