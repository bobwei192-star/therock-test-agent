# The directory profiler/bin doesn't exist in the folder /opt/rocm

- **Issue #:** 1285
- **State:** closed
- **Created:** 2020-11-12T18:27:54Z
- **Updated:** 2020-11-16T07:01:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1285

I have installed ROCM  by instruction from https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
After installation both utilits works properly 
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo

in the documentation one of the step is add a PATH parameter

`echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh`

but directory /opt/rocm/profiler/bin doesn't exist. Is it ok ?

```
(base) yuriy@yuriy-System-Product-Name:~$ cd /opt/rocm 
(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ ls -l 
total 36
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 amdgcn
drwxr-xr-x 2 root root 4096 ნოე 12 21:45 bin
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 hsa
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 include
drwxr-xr-x 3 root root 4096 ნოე 12 22:04 lib
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 oam
drwxr-xr-x 5 root root 4096 ნოე 12 21:45 opencl
drwxr-xr-x 6 root root 4096 ნოე 12 21:45 rocm_smi
drwxr-xr-x 9 root root 4096 ნოე 12 21:45 share
(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ 
```

