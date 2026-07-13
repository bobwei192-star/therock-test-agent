# [Issue]: Error when installing rocm-hip-runtime-dev

- **Issue #:** 6367
- **State:** open
- **Created:** 2026-06-17T13:46:52Z
- **Updated:** 2026-06-17T15:30:47Z
- **Labels:** status: triage
- **Assignees:** nkulshre-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6367

### Problem Description

```
sudo apt install rocm-hip-runtime-dev rocm-developer-tools
```
```
The following packages have unmet dependencies:
 rocm-hip-runtime-dev : Depends: rocm-hip-runtime (= 7.2.4.70204-93~24.04) but it is not going to be installed
                        Depends: rocm-cmake (= 0.14.0.70204-93~24.04) but 6.0.0-1 is to be installed
                        Depends: hipcc (= 1.1.1.70204-93~24.04) but 5.7.1-3 is to be installed
```

When installing a concrete version like `rocm-hip-runtime-dev7.2.4` it works but then there are no automatic updates of course.

### Operating System

Ubuntu 24.04.4 LTS

### CPU

-

### GPU

-

### ROCm Version

rocm 7.2.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_