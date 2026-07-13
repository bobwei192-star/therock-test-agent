# Low bandwidth with xGMI/MI100/CPU7003

- **Issue #:** 2499
- **State:** closed
- **Created:** 2023-09-25T20:03:36Z
- **Updated:** 2024-07-19T18:28:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/2499

Hi. 
 We try to build HPC server for deep learning based on AMD solution with 8xMI100 and AMD CPU 7003. There are two hives and all GPU inside single hive connected by Infinity Fabric. We have **ROCm 5.6** installed. It seems server has very poore bandwidth performance.
Here is output of  ./rocm_bandwidth_test command:

![image](https://github.com/RadeonOpenCompute/ROCm/assets/18306546/75968856-7b94-4bfc-ab48-7cfbc6820530)

 Screenshot above shows:
1. Bidirectional speed between two GPU's in same hive is about 70GB/s, but according to official documentation must be about 92GB/s.
2. Bidirectional transfer speed  from GPU and CPU is about 50GB/s but should be about 64GB/s
3. Bidirectional transfer speed between CPU form one NUMA to GPU from second NUMA  is about  28GB/s  but it is significaly less then expected.

We followed with this Guide https://rocm.docs.amd.com/en/docs-5.1.3/how_to/tuning_guides/mi100.html to setup.

**Platform:**
![image](https://github.com/RadeonOpenCompute/ROCm/assets/18306546/64dc3816-adb4-42de-baa6-0807cd4f5b73)

**System:**
Alma Linux 9
ROCm 5.6