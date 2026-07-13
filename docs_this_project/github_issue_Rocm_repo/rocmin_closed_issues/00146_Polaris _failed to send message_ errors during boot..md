# Polaris "failed to send message" errors during boot. 

- **Issue #:** 146
- **State:** closed
- **Created:** 2017-07-03T22:09:45Z
- **Updated:** 2018-09-10T10:20:11Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/146

On a fresh install of ROCm 1.6 on top of Ubuntu 16.04 we are getting the messages below during boot after ring tests. Each GPU hangs for about 10 seconds and boot continues normally. 

Card seems to be initialized and working properly post boot regardless (full openCL performance on par with AMDGPU-PRO). 

This issue is not present during Vega FE boot

`[    3.058782] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    3.485773] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    4.310558] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    4.723086] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    5.547875] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    5.960395] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    6.785188] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    7.197712] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    8.022497] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    8.435022] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    9.259809] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    9.672330] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[   10.502892] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[   10.924276] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[   10.938191] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[   11.346839] amdgpu: [powerplay] 
                failed to send pre message 15b ret is 0 
[   11.767822] amdgpu: [powerplay] 
                failed to send message 15b ret is 0 
[   12.196446] amdgpu: [powerplay] 
                failed to send pre message 155 ret is 0 
[   12.618252] amdgpu: [powerplay] 
                failed to send message 155 ret is 0 
[   12.628554] Virtual CRAT table created for GPU
[   12.630970] Parsing CRAT table with 1 nodes
[   12.632391] Creating topology SYSFS entries
[   12.633893] Topology: Add dGPU node [0x67df:0x1002]
[   12.635339] kfd kfd: Reserved 2 pages for cwsr.
[   12.636769] kfd kfd: added device 1002:67df
[   12.638159] [drm] Initialized amdgpu 3.16.0 20150101 for 0000:01:00.0 on minor 0
[   12.641308] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[   12.643153] acpi device:16: registered as cooling_device9
[   12.644718] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
[   12.646381] [drm] Initialized i915 1.6.0 20160919 for 0000:00:02.0 on minor 1`