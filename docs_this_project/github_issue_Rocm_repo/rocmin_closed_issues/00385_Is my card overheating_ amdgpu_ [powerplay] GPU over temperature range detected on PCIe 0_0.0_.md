# Is my card overheating? amdgpu: [powerplay] GPU over temperature range detected on PCIe 0:0.0!

- **Issue #:** 385
- **State:** closed
- **Created:** 2018-04-12T21:07:52Z
- **Updated:** 2018-04-16T11:44:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/385

Sorry if I'm posting this in the wrong place. If this a problem with AMDGPU or something else let me know.
I'm running ROCm and tensorflow workloads. rocm-smi reports temperature at  85c, fan speed at 40%. 
I am wondering why it is spamming my logs with ~400 of these warnings in a couple minutes and not ramping up fans to cool itself down.