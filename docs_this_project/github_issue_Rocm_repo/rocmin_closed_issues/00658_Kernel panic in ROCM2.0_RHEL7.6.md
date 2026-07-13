# Kernel panic in ROCM2.0/RHEL7.6

- **Issue #:** 658
- **State:** closed
- **Created:** 2019-01-02T22:26:20Z
- **Updated:** 2023-12-12T19:15:58Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/658

Boot failure after installing ROCM on RHEL7.6 (Radeon Pro WX 5100).
Get a kernel oops (paging failure) inside kfree() in amdgpu_driver_postclose_kms() and (perhaps) amdgpu_vm_fini(). 

Symptoms: 
- Multiple "missing firmware" messages on install (attached) 
[rocminstall.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722233/rocminstall.txt)
- Kernel messages from boot (captured via netconsole) (attached)
[netconsole_boot.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722241/netconsole_boot.txt)
- Kernel messages from running rocminfo from single user mode (attached)
[netconsole_rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722245/netconsole_rocminfo.txt)
- Kernel messages from running clinfo from single user mode (attached)
[netconsole_clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2722246/netconsole_clinfo.txt)



 