# rocm-smi fails to set profile

- **Issue #:** 1089
- **State:** closed
- **Created:** 2020-04-24T18:17:42Z
- **Updated:** 2021-03-17T06:57:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1089

System: Raven Ridge 2700u
rocm-smi from ROCm 2.2 works.

$ sudo /opt/rocm-3.3.0/bin/rocm-smi --setprofile 3


========================ROCm System Management Interface========================
Traceback (most recent call last):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2995, in <module>
    setProfile(deviceList, args.setprofile)
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 2434, in setProfile
    if writeProfileSysfs(device, profile):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 677, in writeProfileSysfs
    if not verifySetProfile(device, value):
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 583, in verifySetProfile
    maxProfileLevel = getMaxLevel(device, 'profile')
  File "/opt/rocm-3.3.0/bin/rocm-smi", line 856, in getMaxLevel
    return int(levels.splitlines()[-1][0])
ValueError: invalid literal for int() with base 10: ' '