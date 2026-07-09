# Hard system crash when running: tf_cnn_benchmarks.py 

- **Issue #:** 809
- **State:** closed
- **Created:** 2019-06-03T05:22:09Z
- **Updated:** 2019-06-14T14:55:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/809

So my system shuts off when I run the following command:

python3 tf_cnn_benchmarks.py --num_gpus=10 --batch_size=64 --model=resnet50 --variable_update=parameter_server --local_parameter_device=cpu

It happens during the warmup phase. I've got no logs as the crash kills the system and everything is lost when I turn back on. It's reproducible. I have rocm-smi running when it happens and the gpu aren't under a consistent load yet. They're still bouncing up and down from 20-90w and 0-100% load.

I'm on FC30 (kernel 5.1, amdgpu 3.30) with rocm 2.4 from the el7 repos. The system is an Epyc 7551p on a gigabye mz31. The GPUs are 5x Radeon Pro Duos that are power limited 100 watts per GPU from the factory.

My first thought was a power draw issues, but I'm using a single rail 1500w (thermaltake DPS) power supply and I ran a torture test without a crash, let alone a hard crash:
(1) Pegged all 32 cores / 64 thread. 
(2) Constantly read from the drive.
(3) Ran an opencl(darktable) workload on my primary (nvidia p4000) gpu.
(4) Ran an eth mining workload(not ideal, but it was a way of making sure it wasn't rocm related) on all ten cards each drawing about (according to rocm-smi) ~80w.

I'm lost as to where I should start poking.