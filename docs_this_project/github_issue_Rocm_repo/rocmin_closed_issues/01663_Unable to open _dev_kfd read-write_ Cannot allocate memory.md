# Unable to open /dev/kfd read-write: Cannot allocate memory

- **Issue #:** 1663
- **State:** closed
- **Created:** 2022-02-03T00:34:09Z
- **Updated:** 2022-02-07T11:13:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1663

I have installed rocm on Ubuntu 20.04. I tried rocminfo, and got

amdgpu:~/amd$ sudo /opt/rocm-4.5.2/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
jbberry is member of render group

Additional info;
jbberry@ortce-amdgpu:~/amd$ dkms status
amdgpu, 5.11.32-1350682, 5.4.0-97-generic, x86_64: installed

jbberry@ortce-amdgpu:~/amd$ uname -r
5.4.0-97-generic
