# better document the need for LD_LIBRARY_PATH or ld.so.conf

- **Issue #:** 1665
- **State:** closed
- **Created:** 2022-02-03T08:45:12Z
- **Updated:** 2024-10-29T14:17:09Z
- **Labels:** Under Investigation, Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1665

Hello
We're using rsmilib in hwloc, and hwloc is used in MPI. Some MPI users are surprised to see rsmi-related link error at runtime (they don't even know MPI uses hwloc). The issue is that some platforms don't have the path of lib rsmi in LD_LIBRARY_PATH or ld.so.conf. That's easy to fix, but it's not something that end-user should do here, since they don't use rsmi directly. It's rather something to fix on the admin side, the one who installed MPI and/or hwloc.

I see in https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#post-install-actions-and-verification-process that "Users might set LD_LIBRARY_PATH to load the ROCm library version of choice." but I think this should be improved:
* change "might" into something stronger, maybe make it mandatory like competitors do
* talk about /etc/ld.so.conf being an easier alternative for admins
* say that RPM/DEB packages take care of adding the relevant files in /etc/ld.so.conf.d/rocm-foo.conf (I don't see it installed on platforms I have access to, but I see the code in your github repos).

Thanks
Brice
