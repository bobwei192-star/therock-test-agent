# install rocm-dkms 4.1.0 failed

- **Issue #:** 1438
- **State:** closed
- **Created:** 2021-04-02T03:35:29Z
- **Updated:** 2021-04-16T11:10:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1438

My Os is Ubuntu18.04, and old-verison is rocm-4.0.0,
I have removed rock-dkms before the upgrade, and install rock-dkms as https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html, howerver, when I execute

`sudo apt install rocm-dkms`

I encountered the following errors：

```
depmod.....

DKMS: install completed.
update-initramfs: Generating /boot/initrd.img-4.15.0-140-generic
find: ‘/lib/firmware/updates/amdgpu’: No such file or directory
W: Possible missing firmware /lib/firmware/amdgpu/dimgrey_cavefish_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/green_sardine_ta.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
Setting up rocm-opencl-dev (2.0.0.40100-26) ...
Setting up rocm-clang-ocl (0.5.0.40100-26) ...
Setting up rocm-dbgapi (0.42.0.40100-26) ...
Setting up rocm-smi-lib (3.0.0.40100-26) ...
Setting up hip-samples (4.1.21072.5776.40100-26) ...
Setting up libpython3.8-stdlib:amd64 (3.8.0-3~18.04.1) ...
Setting up hsa-amd-aqlprofile (1.0.0.40100-26) ...
Setting up libpython3.8:amd64 (3.8.0-3~18.04.1) ...
Setting up openmp-extras (12.41.0.40100-26) ...
Setting up rocm-utils (4.1.0.40100-26) ...
Setting up rocm-gdb (10.1.40100-26) ...
Setting up rocm-dev (4.1.0.40100-26) ...
/opt/rocm-4.1.0/bin/ca not found
update-alternatives: using /opt/rocm-4.1.0/bin/clang-ocl to provide /usr/bin/clang-ocl (clang-ocl) in auto mode
/opt/rocm-4.1.0/bin/extractkernel not found
/opt/rocm-4.1.0/bin/findcode.sh not found
/opt/rocm-4.1.0/bin/finduncodep.sh not found
/opt/rocm-4.1.0/bin/hipcc not found
/opt/rocm-4.1.0/bin/hipcc_cmake_linker_helper not found
/opt/rocm-4.1.0/bin/hipconfig not found
/opt/rocm-4.1.0/bin/hipconvertinplace-perl.sh not found
/opt/rocm-4.1.0/bin/hipconvertinplace.sh not found
/opt/rocm-4.1.0/bin/hipdemangleatp not found
/opt/rocm-4.1.0/bin/hipexamine-perl.sh not found
/opt/rocm-4.1.0/bin/hipexamine.sh not found
/opt/rocm-4.1.0/bin/hipify-cmakefile not found
/opt/rocm-4.1.0/bin/hipify-perl not found
/opt/rocm-4.1.0/bin/lpl not found
update-alternatives: using /opt/rocm-4.1.0/bin/rocgdb to provide /usr/bin/rocgdb (rocgdb) in auto mode
/opt/rocm-4.1.0/bin/rocm_agent_enumerator not found
/opt/rocm-4.1.0/bin/rocminfo not found
update-alternatives: using /opt/rocm-4.1.0/bin/rocm-smi to provide /usr/bin/rocm-smi (rocm-smi) in auto mode
update-alternatives: using /opt/rocm-4.1.0/bin/rocprof to provide /usr/bin/rocprof (rocprof) in auto mode
update-alternatives: using /opt/rocm-4.1.0 to provide /opt/rocm (rocm) in auto mode
Setting up rocm-dkms (4.1.0.40100-26) ...
Processing triggers for libc-bin (2.27-3ubuntu1.4) ...
```

when I execute /opt/rocm/bin/rocminfo, an error is prompted：
`-bash: /opt/rocm/bin/rocminfo: No such file or directory`

when I execute /opt/rocm/opencl/bin/clinfo, an error is prompted：
```
dlerror: libhsakmt.so.1: cannot open shared object file: No such file or directory
/opt/rocm/opencl/bin/clinfo: Relink `/usr/lib/x86_64-linux-gnu/libnvidia-opencl.so.1' with `/lib/x86_64-linux-gnu/librt.so.1' for IFUNC symbol `clock_gettime'
Segmentation fault (core dumped)
```
 I have reboot, and reexecute sudo apt install rocm-dkms, it prompt:
```
Reading package lists... Done
Building dependency tree
Reading state information... Done
rocm-dkms is already the newest version (4.1.0.40100-26).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```
but, execeute /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo, still the same error.

May I ask why, thank you.
