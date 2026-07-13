# sudo apt-get install rocm opencl-rocm does not work

- **Issue #:** 130
- **State:** closed
- **Created:** 2017-06-16T09:38:11Z
- **Updated:** 2017-07-01T21:46:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/130

Linux 16.04.02, AMD W9100 graphic card.
I follow the readme.md in ROCm project, on branch roc-1.5.0 .
I try to install opencl, but failed.
1. wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
2. sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
3. sudo apt-get update
4. sudo apt-get install rocm opencl-rocm
5. sudo apt-get install rocm opencl-rocm-dev

both 4 and 5 failed, can get the package.
I want to know why?