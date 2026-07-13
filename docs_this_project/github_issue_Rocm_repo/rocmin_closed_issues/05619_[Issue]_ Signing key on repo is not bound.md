# [Issue]: Signing key on repo is not bound

- **Issue #:** 5619
- **State:** closed
- **Created:** 2025-11-03T19:42:31Z
- **Updated:** 2025-11-04T19:10:31Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5619

### Problem Description

sudo apt update gives:

```
Warning: https://repo.radeon.com/rocm/6.4.4/ubuntu/dists/noble/InRelease: Policy will reject signature within a year, see --audit for details
Audit: https://repo.radeon.com/amdgpu/6.4.4/ubuntu/dists/noble/InRelease: Sub-process /usr/bin/sqv returned an error code (1), error message is:
   Signing key on CA8BB4727A47B4D09B4EE8969386B48A1A693C5C is not bound:
              No binding signature at time 2025-09-18T22:16:53Z
     because: Policy rejected non-revocation signature (PositiveCertification) requiring second pre-image resistance
     because: SHA1 is not considered secure since 2026-02-01T00:00:00Z
```

### Operating System

Irrelevant

### CPU

Irrelevant

### GPU

Irrelevant

### ROCm Version

Irrelevant

### ROCm Component

_No response_

### Steps to Reproduce

run `sudo apt update`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_