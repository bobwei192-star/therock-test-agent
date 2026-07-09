# [Feature]: Update amdgpu-install to support modern apt source formats

- **Issue #:** 5558
- **State:** open
- **Created:** 2025-10-22T16:03:46Z
- **Updated:** 2025-10-24T03:17:59Z
- **Labels:** Feature Request, status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5558

### Suggestion Description

I have avoided using amdgpu-install mainly because it uses the legacy apt source format, so I sort of dismissed it as a tool that was just going to add more cruft I would have to update on my own each time I use it.  I can see how it is very useful steering different install patterns and so I am proposing this update to avoid problems as users move beyond Ubuntu 24.04. 

amdgpu-install uses the legacy format and creates a .list file similar to below: 

```
$ cat /etc/apt/sources.list.d/rocm.list 
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/7.0.2 noble main

```
What it should be doing is creating something similar to this

```
$ cat /etc/apt/sources.list.d/rocm.sources 
Types: deb
URIs: https://repo.radeon.com/rocm/apt/7.0.2/
Suites: noble
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/rocm.gpg

```
The amdgpu-dkms (6.14.14) is ABI compatible with Ubuntu 25.04, and new amdgpu (6.17.0-5) ships with Ubuntu 25.10.

In versions of Ubuntu newer than 24.04, and other debian based distros with modern apt,  the system will prompt you to `sudo apt modernize-sources` if it detects you are using the legacy format, like the one provided by amdgpu-install.

The net result, is you will start to see something like the following when the first update to ROCm is handled by amdgpu-install during an apt upgrade. 
  
```
Warning: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Translations (main/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Translations (main/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Translations (main/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/amdgpu.list:1 and /etc/apt/sources.list.d/amdgpu.sources:1
Warning: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Translations (main/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
Warning: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/rocm.list:1 and /etc/apt/sources.list.d/rocm.sources:1
```

There is also the potential for conflict, if the contents of the new and old formats do not match, which I believe prioritizes the newer format, not the one being maintained by amdgpu-install.   The potential for unnecessary issues could be avoided by cleaning this up today. 

I am not sure about 22.04, but certainly 24.04 can use the newer apt format, so a planned migration now, is going to save a lot of headache down the road. 

A few links would need updates at the same time as well:
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-debian.html
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager/package-manager-ubuntu.html

### Operating System

Ubuntu, Debian

### GPU

_No response_

### ROCm Component

_No response_