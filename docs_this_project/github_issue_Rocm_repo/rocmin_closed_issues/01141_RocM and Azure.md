# RocM and Azure

- **Issue #:** 1141
- **State:** closed
- **Created:** 2020-06-07T11:44:53Z
- **Updated:** 2021-02-15T06:34:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/1141

Did someone has experience on installing RocM on Azure ? Because starting from few days I am not able to make RocM working anymore. As soon as I install rocm-dkms package the amdgpu driver crash on start. 

[ 11.589569] amdgpu c7e9:00:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:217 vmid:0 pasid:0, for process pid 0 thread pid 0) 
[ 11.591955] amdgpu c7e9:00:00.0: amdgpu: in page starting at address 0x000000f400100000 from client 27 [ 11.659995] amdgpu c7e9:00:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:217 vmid:0 pasid:0, for process pid 0 thread pid 0) 
[ 11.659995] amdgpu c7e9:00:00.0: amdgpu: in page starting at address 0x000000f400101000 from client 27 
[ 12.004451] amdgpu c7e9:00:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] ERROR ring kiq_2.1.0 test failed (-110) 
[ 12.049879] [drm:amdgpu_gfx_enable_kcq [amdgpu]] ERROR KCQ enable failed 
[ 12.092608] [drm:amdgpu_device_init [amdgpu]] ERROR hw_init of IP block <gfx_v9_0> failed -110 [ 12.141149] amdgpu c7e9:00:00.0: amdgpu: amdgpu_device_ip_init failed 
[ 12.193592] amdgpu c7e9:00:00.0: amdgpu: Fatal error during GPU init

I tried SLES15 Ubuntu 18.04 and CentOS 8.1 following the instruction here:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

Partition used
Standard NV4as_v4 (4 vcpus, 14 GiB memory)

AMD Gpu is a Radeon Instinct MI25 partitioned