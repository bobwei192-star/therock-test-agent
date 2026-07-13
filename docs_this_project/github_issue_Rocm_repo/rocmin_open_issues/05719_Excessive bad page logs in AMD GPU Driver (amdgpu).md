# Excessive bad page logs in AMD GPU Driver (amdgpu)

- **Issue #:** 5719
- **State:** open
- **Created:** 2025-11-28T15:20:56Z
- **Updated:** 2025-11-28T15:20:56Z
- **Labels:** Verified Issue, ROCm 7.1.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5719

Due to partial data corruption of Electrically Erasable Programmable Read-Only Memory (EEPROM) and limited error handling in the AMD GPU Driver(amdgpu), excessive log output might result when querying the reliability, availability, and serviceability (RAS) bad pages. This issue will be fixed in a future AMD GPU Driver(amdgpu) and ROCm release.