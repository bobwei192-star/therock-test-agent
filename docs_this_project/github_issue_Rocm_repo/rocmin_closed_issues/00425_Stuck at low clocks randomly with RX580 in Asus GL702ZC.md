# Stuck at low clocks randomly with RX580 in Asus GL702ZC

- **Issue #:** 425
- **State:** closed
- **Created:** 2018-05-25T05:23:59Z
- **Updated:** 2019-01-05T20:05:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/425

Hi,
With ROCm 1.8 my laptop randomly loses ability to change to higher p-states, requiring shutting down the machine completely and turning it back on. Hot reboots do not work.
The amdgpu drivers in kernel ubuntu kernel 4.13 work fine.

Here is the dmesg output when trying to run a OpenCL application:
``
[ 4826.610906] amdgpu: [powerplay] Failed to notify smc display settings!
[ 5212.480671] amdgpu: [powerplay] Failed to notify smc display settings!
[ 5822.865839] amdgpu: [powerplay] Failed to notify smc display settings!
[ 6194.342332] amdgpu: [powerplay] Failed to notify smc display settings!
[ 6804.910781] amdgpu: [powerplay] Failed to notify smc display settings!
[26414.119861] amdgpu: [powerplay] Failed to start pm status log!
[26414.985049] amdgpu: [powerplay] Failed to start pm status log!
[26420.344579] amdgpu: [powerplay] Failed to start pm status log!
[26421.024833] amdgpu: [powerplay] Failed to start pm status log!
``
