# Installing with Ryzen 3 2200G breaks Ubuntu (16.04 LTS and 18.04 LTS)

- **Issue #:** 829
- **State:** closed
- **Created:** 2019-06-26T10:23:52Z
- **Updated:** 2023-12-21T14:35:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/829

Hi

I tried to install ROCm today on a machine equipped with a Ryzen 3 2200G. The operating system is a freshly installed Ubuntu 16.04 LTS (also tried with 18.04 LTS).

I followed all instructions, and after installing
`rocm-dkms`
and subsequent rebooting, Ubuntu does not start anymore. It goes past the initial bios screen, then the monitor turns black and nothing happens. There still is a signal coming to the monitor, since it does not turn off, but all I see is black.

I could not manage to fix the problem, only re-installing Ubuntu helped.

If I run `/opt/rocm/bin/rocminfo` after the install, it gives me some weird error and refers to a directory `home/jenkins/...`, even though there is no such user on the system.

If I run `/opt/rocm/opencl/bin/x86_64/clinfo`, I get an error 1001 (Could not get device IDs...).

Any ideas why this could be happening?

