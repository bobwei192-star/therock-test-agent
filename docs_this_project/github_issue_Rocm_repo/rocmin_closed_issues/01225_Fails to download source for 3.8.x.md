# Fails to download source for 3.8.x

- **Issue #:** 1225
- **State:** closed
- **Created:** 2020-09-21T20:38:38Z
- **Updated:** 2020-10-08T05:42:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1225

The following url claims, to download the 3.8.x but it does not work:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code
...
Downloading the ROCm Source Code
The following example shows how to use the repo binary to download the ROCm source code. If you choose a directory other than ~/bin/ to install the repo, you must use that chosen directory in the code as shown below:

mkdir -p ~/ROCm/
cd ~/ROCm/
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-3.8.x
repo sync
...

run from linux terminal failed:
Downloading manifest from https://github.com/RadeonOpenCompute/ROCm.git
fatal: Couldn't find remote ref refs/heads/roc-3.8.x
manifests:
fatal: Couldn't find remote ref refs/heads/roc-3.8.x

fatal: Couldn't find remote ref refs/heads/roc-3.8.x
manifests:
fatal: Couldn't find remote ref refs/heads/roc-3.8.x

