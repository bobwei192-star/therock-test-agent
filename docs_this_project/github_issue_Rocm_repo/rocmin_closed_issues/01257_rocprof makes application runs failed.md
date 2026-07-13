# rocprof makes application runs failed

- **Issue #:** 1257
- **State:** closed
- **Created:** 2020-10-08T23:02:45Z
- **Updated:** 2020-12-11T07:06:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1257

Using ROCm 3.8,
Without rocprof, my application always run.
With rocprof, there is a small chance my app runs but most of the time I got two kinds of errors.
1. error(4105) "queue_event_callback(), queue error handling is not supported"
2. Thread 1 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
Need to have this random and broken behavior fixed.

Here is a backtrace from gdb `rocprof --hsa-trace gdb ./bin/check_spo_batched`
```
Thread 1 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
0x00007fff75cbad05 in rocr::HSA::hsa_signal_store_relaxed(hsa_signal_s, long) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007fff75cbad05 in rocr::HSA::hsa_signal_store_relaxed(hsa_signal_s, long) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#1  0x00007fff748fc98e in roctracer::hsa_support::hsa_signal_store_relaxed_callback(hsa_signal_s, long) ()
   from /opt/rocm/roctracer/lib/libroctracer64.so.1
#2  0x00007fff7609d1ce in __tgt_rtl_run_target_team_region () from /opt/rocm/aomp/lib/libomptarget.rtl.hsa.so
#3  0x00007ffff6a65a9a in target(long, void*, int, void**, void**, long*, long*, int, int, int) ()
   from /opt/rocm/aomp/lib/libomptarget.so
#4  0x00007ffff6a5cecf in __tgt_target_teams () from /opt/rocm/aomp/lib/libomptarget.so
#5  0x0000000000417728 in qmcplusplus::einspline_spo_omp<double>::multi_evaluate_vgh(std::vector<qmcplusplus::SPOSet*, std::allocator<qmcplusplus::SPOSet*> > const&, std::vector<qmcplusplus::ParticleSet*, std::allocator<qmcplusplus::ParticleSet*> > const&, int) ()
#6  0x000000000040710d in main ()
```

Reproducer uses AOMP clang++:
```
git clone https://github.com/ye-luo/miniqmc.git
cd miniqmc/build
cmake -D CMAKE_CXX_COMPILER=clang++       -D ENABLE_OFFLOAD=1       -D OFFLOAD_TARGET=amdgcn-amd-amdhsa       -D OFFLOAD_ARCH=gfx906 ..
make -j
export OMP_NUM_THREADS=8
rocprof --hsa-trace ./bin/check_spo_batched
rocprof --hsa-trace ./bin/check_spo
```

