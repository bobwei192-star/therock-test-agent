# Clarify default installation path

- **Issue #:** 1568
- **State:** closed
- **Created:** 2021-09-01T07:53:28Z
- **Updated:** 2021-09-13T07:46:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/1568

Hello
Can you clarify the documentation of the default install path? https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html talks about /opt/rocm and also about /opt/rocm-<version>/. All platforms I have access to use the latter. Some RPMs from your download area too.
Is /opt/rocm supposed to be a symlink to one of the /opt/rocm-<version>/ installations? Is one of your packages supposed to create that symlink? Or do you have 2 install strategies, one for single version under /opt/rocm, and one for multiversions under /opt/rocm-<version> but no /opt/rocm?
I am asking this because I'd the hwloc configure scripts to automatically look for ROCm SMI lib/headers under /opt/rocm but I couldn't find a single platform where it would work :/
Thanks