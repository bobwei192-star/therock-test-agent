# [Issue]:Build script multiple issues.

- **Issue #:** 4624
- **State:** closed
- **Created:** 2025-04-14T19:28:11Z
- **Updated:** 2025-06-10T03:35:09Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4624

### Problem Description

Regarding the build script presented at https://github.com/ROCm/ROCm, section "Build ROCm from source".

1) Script WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22/install-prerequisites.sh tries to run apt install, but it does not call "sudo apt install ...". 

So you need to run the install-prerequisites.sh script using `sudo sh install-prerequisites.sh`. 

OTOH same script runs pip installs. Running pip install as root clobbers system packages, is generally a bad idea.

How about writing a prerequisites install script that invokes various bits and bobs with appropriate use of sudo?

2) We declare in the build script that we are doing ROCm-6.4:

```
export ROCM_VERSION=6.4.0
~/bin/repo init -u http://github.com/ROCm/ROCm.git -b roc-6.4.x -m tools/rocm-build/rocm-${ROCM_VERSION}.xml
~/bin/repo sync
```

However in WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22 there is no branch checked out. Git says "no branch".

3) In directory WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22 are two versions of the install prerequisites shell script:

```
emerth@desktop ~/WORKSPACE $ pushd ROCm/tools/rocm-build/docker/ubuntu22
~/WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22 ~/WORKSPACE ~/WTF
emerth@desktop ~/WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22 ((no branch))$ ls -lF
total 40
-rw-rw-r-- 1 emerth emerth   312 Apr 14 18:19 Dockerfile
-rw-rw-r-- 1 emerth emerth  9835 Apr 14 18:19 install-prerequisites.sh
-rw-rw-r-- 1 emerth emerth 10875 Apr 14 18:19 install-prerequisities.sh
-rw-rw-r-- 1 emerth emerth    43 Apr 14 18:19 local-pin-600
-rw-rw-r-- 1 emerth emerth  1654 Apr 14 18:19 packages
-rw-rw-r-- 1 emerth emerth   582 Apr 14 18:19 README.md
emerth@desktop ~/WORKSPACE/ROCm/tools/rocm-build/docker/ubuntu22 ((no branch))$
```
The two versions are substantially different. 

The one which name is not an obvious typo fails to complete:

```
<SNIP>
Resolving repo.radeon.com (repo.radeon.com)... 184.30.150.219, 184.30.150.213, 2600:140a:1000:f::b81e:960e, ...
Connecting to repo.radeon.com (repo.radeon.com)|184.30.150.219|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17000 (17K) [application/octet-stream]
Saving to: ‘amdgpu-install_6.3.60300-1_all.deb’

amdgpu-install_6.3.60300-1_all.deb     100%[============================================================================>]  16.60K  --.-KB/s    in 0.003s

2025-04-14 17:52:18 (5.36 MB/s) - ‘amdgpu-install_6.3.60300-1_all.deb’ saved [17000/17000]

+ apt install -y ./amdgpu-install_6.3.60300-1_all.deb
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'amdgpu-install' instead of './amdgpu-install_6.3.60300-1_all.deb'
The following packages were automatically installed and are no longer required:
  libgoogle-glog0v5 libstdc++-12-dev rocdecode rocdecode-dev
Use 'sudo apt autoremove' to remove them.
The following packages will be DOWNGRADED:
  amdgpu-install
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
E: Packages were downgraded and -y was used without --allow-downgrades.

```
It appears to want to install drivers(?) from rocm 6.3 despite this being a build for 6.4.

The one which name is an obvious typo also has to be run as root else it fails running apt, and also fails at modifying system directories as well, some of which don't even exist (/var/lib/apt/lists/partial, /usr/local/ccache, others). AFAIK on Ubuntu there has never been a /var/lib/apt/lists/partial directory? 

At this point in the ROCm adventure I decided `WTH the machine is half trashed by now, what with all the crap the other prereq script just did`, so just run install-prequities.sh as root. Finally this script has been running for over thirty minutes wall clock time on my 5900X using an NVMe SSD - it's building stuff from GRPC, from OFED I think, lapack, boring ssl, other HPC-like stuff, it even seems to have built the entire Boost binary library suite from source. Maybe this script is not suppose to be there? If it is supposed to be there maybe it needs a name that indicates it's purpose (something like I_AM_THE_SCRIPT_THAT_WILL_TURN_YOUR_PC_INTO_A_SOFTWARE_CLONE_OF_FRONTIER_SUPERCOMPUTER.sh). Remarkably this version of the prereq script runs to completion.

4) This absolute gem:

```
emerth@desktop ~/WORKSPACE $ make -f ROCm/tools/rocm-build/ROCm.mk -j ${NPROC:-$(nproc)} rocm-dev
OUT_DIR=/home/emerth/WORKSPACE/out/ubuntu-22.04/22.04
ROCM_INSTALL_PATH=/opt/rocm-6.4.0
sudo mkdir -p -m 775 "/opt/rocm-6.4.0" && \
sudo chown -R "1000:1000" "/opt"
sudo chown -R "1000:1000" "/home/emerth"

```

**### _Just possibly there are people in the world who do not ******* want the ownership of their entire /opt and ~ directory trees overwritten?_**

5) I guess just a general bitch: If you people are going to post a script to build ROCm from source, and point people to that script, how about posting a script that bloody works, and which does not blow away file system ownerships en masse? And if such is not possible, how about posting a detailed instruction on building ROCm?



### Operating System

Ubuntu 22.04

### CPU

AMD Ryzen 9 5900X 12-Core Processor

### GPU

Radeon 780m, Radeon Pro VII, Radeon 9070XT

### ROCm Version

ROCm 6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_