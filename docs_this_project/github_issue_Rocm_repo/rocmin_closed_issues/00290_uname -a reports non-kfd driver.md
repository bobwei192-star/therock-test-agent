# uname -a reports non-kfd driver

- **Issue #:** 290
- **State:** closed
- **Created:** 2017-12-28T05:10:23Z
- **Updated:** 2017-12-28T18:50:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/290

I have recently installed rocm-1.7. I tried the HelloWorld sample after that and the run was successful. I have updated the GRUB_DEFAULT variable too and have run update-grub. But when I do uname -a, I am getting the below:
dnnroot@ubuntu:~$ uname -a
Linux ubuntu 4.4.0-104-generic #127-Ubuntu SMP Mon Dec 11 12:16:42 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

The above issue is not allowing me to run tests on HipCaffe Docker image, where the output while trying to train AlexNet is as below:
root@7eaaf0c1a5a0:/home/rocm-user# script -c "caffe train -solver=/Netinfo/AlexNet/solver.prototxt -gpu 0" /Data/Testing/HPE_P100_1.txt
Script started, file is /Data/Testing/HPE_P100_1.txt
I1228 04:53:44.488523    29 caffe.cpp:217] Using GPUs 0
There is no device can be used to do the computation
Script done, file is /Data/Testing/HPE_P100_1.txt

But when I run rocm-smi, I get the following output:
root@7eaaf0c1a5a0:/opt/rocm/bin# ./rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  DID    Temp     AvgPwr   SCLK     MCLK     Fan      Perf    OverDrive  ECC
  0   687f   52.0c    N/A      852Mhz   500Mhz   12.94%   auto      0%       N/A
  1   67ef   42.0c    N/A      214Mhz   1750Mhz  13.73%   auto      0%       N/A
================================================================================
====================           End of ROCm SMI Log          ====================

Please suggest why "uname -a" is not reporting "4.11.0-kfd-compute-rocm-rel" as it used to report on rocm-1.6. This issue is not allowing me to run HipCaffe properly.