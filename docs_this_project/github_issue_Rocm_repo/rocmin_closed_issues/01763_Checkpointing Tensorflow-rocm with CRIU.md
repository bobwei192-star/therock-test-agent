# Checkpointing Tensorflow-rocm with CRIU

- **Issue #:** 1763
- **State:** closed
- **Created:** 2022-07-01T22:36:11Z
- **Updated:** 2022-07-08T22:51:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1763

Note: I also submitted the same issue over in CRIU, however have hit a dead end.
So I'm trying to checkpoint and restore a tensorflow-rocm (2.9.1) application running on my GPU (Raedeon RX 6950 XT), however, have been so far unsuccessful and have been unable to see why.

Steps

Install Ubuntu 20.0.4
Install rocm-5.1.3
Install Tensorflow-rocm
Install CRIU 3.17

Run a sample TensorFlow program (I used mnist.py)
Use time criu dump -t <PID> -vvvv -o dump.log --shell-job -L/usr/local/lib/criu/ && echo OK

The dumping has been successful, however, I was unable to restore the process and met with this error:

`
(00.019208)   2266: amdgpu_plugin: Restoring 1 devices
(00.020766)   2266: amdgpu_plugin: amdgpu_plugin: passing drm render fd = 9 to driver
(00.020786)   2266: amdgpu_plugin: Restore devices Ok (ret:0)
(00.020799)   2266: amdgpu_plugin: Restoring 100 BOs
(00.020802)   2266: amdgpu_plugin: Restore BOs Ok
(00.021950)   2266: amdgpu_plugin: amdgpu_plugin: Thread[0x3984] started
(00.022795)   2266: amdgpu_plugin: amdgpu-pages-187-3984.img:Opened file for read with size:16808726528
(62.699087)   2266: Error (amdgpu_plugin.c:640): amdgpu_plugin: failed to create userptr for sdma: Device or resource busy
(62.700140)   2266: Error (amdgpu_plugin.c:1022): amdgpu_plugin: Failed to fill the BO using sDMA: bo_buckets[56]
(62.700222)   2266: amdgpu_plugin: amdgpu_plugin: Thread[0x3984] done num_bos:8 ret:-14
(63.209360)   2266: amdgpu_plugin: Thread[0x3984] finished ret:-14
(63.210279)   2266: Error (amdgpu_plugin.c:1850): amdgpu_plugin: amdgpu_plugin: Failed to restore (ret:-14)
(63.210739)   2266: Error (criu/files-ext.c:53): Unable to restore 0xbb
(63.210820)   2266: Error (criu/files.c:1213): Unable to open fd=3 id=0xbb
(63.212439) Error (criu/cr-restore.c:2536): Restoring FAILED.
(63.213136) amdgpu_plugin: amdgpu_plugin: finished  amdgpu_plugin (AMDGPU/KFD)
`
I'm running as root and the restore line I used was criu restore -vvvv -o restore.log --shell-job -L/usr/local/lib/criu/ && echo OK.

I tried my best to search around and found a few others details that might be informative.
The error
`
(62.699087)   2266: Error (amdgpu_plugin.c:640): amdgpu_plugin: failed to create userptr for sdma: Device or resource busy
`
can be found in the dump log as well.

the tensorflow process had fd 0-8, which could be located, all of which are symbolic link files. However during restoring it became "0  1  10  11  114  116  12  120  121  122  123  124  126  127  13  14  15  16  17  18  19  2  3  4  5  6  7  8  9," where 3,5,6,7,8,10,11,114,116, and 12 are archives.

I looked into the test log so I know there is no problem with the tensorflow program itself, I've tried to find solutions and see if anyone else is in the same boat but so far have been unsuccessful

Note: When running criu check --all it displays:
Looks good but some kernel features are missing
which, depending on your process tree, may cause
dump or restore failure.

