# rock-dkms package disappeared from the repo

- **Issue #:** 1614
- **State:** closed
- **Created:** 2021-11-05T09:23:28Z
- **Updated:** 2022-04-24T12:44:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/1614

Hi! I wanted to install ROCm recently on some cluster machines but install fails due to a missing package.
```
$ sudo apt-add-repository 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main'
...
$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rock-dkms but it is not installable
E: Unable to correct problems, you have held broken packages.
$ apt search rocm-dkms
Sorting... Done
Full Text Search... Done
rocm-dkms/Ubuntu 4.5.0.40500-56 amd64
  Radeon Open Compute (ROCm) Runtime software stack

$ apt search rock-dkms
Sorting... Done
Full Text Search... Done
```
Browsing through `https://repo.radeon.com/rocm/apt/` I saw that neither the `debian` (latest?) nor `4.5` folders have the `rock-dkms` package in them. `4.3.1` does. I installed the runtime in a docker container just Yesterday and it worked.