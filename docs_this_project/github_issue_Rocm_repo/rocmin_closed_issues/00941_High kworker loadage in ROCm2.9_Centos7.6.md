# High kworker loadage in ROCm2.9/Centos7.6

- **Issue #:** 941
- **State:** closed
- **Created:** 2019-11-20T03:33:32Z
- **Updated:** 2019-11-21T05:44:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/941

We installed the ROCm2.9 in Centos7.6. But after we ran the GPU programs, the loadage of kworker became very high even the programs had been stopped. And the performance dropped off.  The monitor tool we used is "top". 
When we ran the tensorflow_gpu with mpi, multi processes in one node, we found that the data was allocated in numa0 system memory firstly for all processes even we used the different numactl bindings for each process. And the loadage of kswap0 became very high. 
Thank you :)