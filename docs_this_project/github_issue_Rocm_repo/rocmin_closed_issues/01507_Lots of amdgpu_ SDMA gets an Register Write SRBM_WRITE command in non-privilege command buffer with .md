# Lots of amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer with kernel 5.13

- **Issue #:** 1507
- **State:** closed
- **Created:** 2021-06-28T19:46:06Z
- **Updated:** 2021-06-29T10:02:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1507

Using ROCm 3.3.0, Linux kernel 5.13.0, Radeon VII, OpenCL without rock-dkms, I get a lot of such messages in dmesg (about one per second) when running gpuowl

```
[51970.530596] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51970.530608] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x0000000003640000 src_id:247 ring:8 vmid:9 pasid:32773, for process good pid 3871 thread good pid 3871
[51972.307138] amdgpu 0000:b5:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51972.307150] amdgpu 0000:b5:00.0: amdgpu: [sdma1] address:0x0000000003428000 src_id:247 ring:7 vmid:8 pasid:32776, for process good pid 3884 thread good pid 3884
[51973.621251] amdgpu 0000:6a:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51973.621263] amdgpu 0000:6a:00.0: amdgpu: [sdma1] address:0x000000000e980000 src_id:247 ring:3 vmid:8 pasid:32784, for process good pid 3910 thread good pid 3910
[51976.184582] amdgpu 0000:6a:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51976.184595] amdgpu 0000:6a:00.0: amdgpu: [sdma1] address:0x000000000c4d8000 src_id:247 ring:4 vmid:9 pasid:32775, for process good pid 3879 thread good pid 3879
[51979.923365] amdgpu 0000:b5:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51979.923376] amdgpu 0000:b5:00.0: amdgpu: [sdma1] address:0x0000000003500000 src_id:247 ring:8 vmid:9 pasid:32772, for process good pid 3868 thread good pid 3868
[51980.374640] amdgpu 0000:67:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51980.374652] amdgpu 0000:67:00.0: amdgpu: [sdma1] address:0x0000000009780000 src_id:247 ring:8 vmid:8 pasid:32783, for process good pid 3896 thread good pid 3896
[51982.615614] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51982.615627] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x000000000af18000 src_id:247 ring:7 vmid:8 pasid:32777, for process good pid 3891 thread good pid 3891
[51983.028571] amdgpu 0000:67:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51983.028583] amdgpu 0000:67:00.0: amdgpu: [sdma1] address:0x0000000008d20000 src_id:247 ring:9 vmid:9 pasid:32774, for process good pid 3874 thread good pid 3874
[51986.599941] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51986.599952] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x0000000003718000 src_id:247 ring:8 vmid:9 pasid:32773, for process good pid 3871 thread good pid 3871
[51986.601194] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51986.601203] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x00000000037f0000 src_id:247 ring:8 vmid:9 pasid:32773, for process good pid 3871 thread good pid 3871
[51986.626717] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51986.626731] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x00000000038c8000 src_id:247 ring:8 vmid:9 pasid:32773, for process good pid 3871 thread good pid 3871
[51987.459300] amdgpu 0000:19:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51987.459313] amdgpu 0000:19:00.0: amdgpu: [sdma1] address:0x0000000003ab8000 src_id:247 ring:8 vmid:9 pasid:32773, for process good pid 3871 thread good pid 3871
[51988.168639] amdgpu 0000:b5:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51988.168651] amdgpu 0000:b5:00.0: amdgpu: [sdma1] address:0x0000000003500000 src_id:247 ring:7 vmid:8 pasid:32776, for process good pid 3884 thread good pid 3884
[51989.442239] amdgpu 0000:6a:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51989.442252] amdgpu 0000:6a:00.0: amdgpu: [sdma1] address:0x000000000ea58000 src_id:247 ring:3 vmid:8 pasid:32784, for process good pid 3910 thread good pid 3910
[51991.994879] amdgpu 0000:6a:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51991.994891] amdgpu 0000:6a:00.0: amdgpu: [sdma1] address:0x000000000c5b0000 src_id:247 ring:4 vmid:9 pasid:32775, for process good pid 3879 thread good pid 3879
[51995.783937] amdgpu 0000:b5:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51995.783949] amdgpu 0000:b5:00.0: amdgpu: [sdma1] address:0x00000000035d8000 src_id:247 ring:8 vmid:9 pasid:32772, for process good pid 3868 thread good pid 3868
[51996.067632] amdgpu 0000:67:00.0: amdgpu: SDMA gets an Register Write SRBM_WRITE command in non-privilege command buffer
[51996.067644] amdgpu 0000:67:00.0: amdgpu: [sdma1] address:0x0000000009858000 src_id:247 ring:8 vmid:8 pasid:32783, for process good pid 3896 thread good pid 3896
```