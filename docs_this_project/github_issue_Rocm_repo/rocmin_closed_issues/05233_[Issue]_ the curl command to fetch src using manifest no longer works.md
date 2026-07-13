# [Issue]: the curl command to fetch src using manifest no longer works

- **Issue #:** 5233
- **State:** closed
- **Created:** 2025-08-27T20:45:51Z
- **Updated:** 2025-09-01T15:58:28Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5233

### Problem Description

curl https://storage.googleapis.com/git-repo-downloads/repo | $SUDO tee ~/bin/repo
chmod a+x ~/bin/repo
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-$CONFIG_VERSION.x

Used to work in 6.x or before but broken in 7.0.0. Got this error: 

Fatal: couldn't find remote ref refs/heads/roc-7.0.x
manifests: sleeping 4.0 seconds before retrying
fatal: cannot obtain manifest https://github.com/RadeonOpenCompute/ROCm.git
================================================================================
Repo command failed: UpdateManifestError
        Unable to sync manifest default.xml
Error: Unable to do initialize repo.




### Operating System

Linux

### CPU

AMD

### GPU

MI300

### ROCm Version

7.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

curl https://storage.googleapis.com/git-repo-downloads/repo | $SUDO tee ~/bin/repo
chmod a+x ~/bin/repo
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-$CONFIG_VERSION.x
There CONFIG_VERSION used to have consistent format: <major>.<minor> i.e. 6.3 For ROCm6.3.