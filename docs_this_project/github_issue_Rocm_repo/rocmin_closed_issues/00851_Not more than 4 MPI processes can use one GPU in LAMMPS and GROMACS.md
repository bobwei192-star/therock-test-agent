# Not more than 4 MPI processes can use one GPU in LAMMPS and GROMACS

- **Issue #:** 851
- **State:** closed
- **Created:** 2019-07-28T20:23:11Z
- **Updated:** 2020-01-22T19:51:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/851

With ROCm since the version 1.8 up to the current version 2.6 it has not been possible to use more than 4 MPI processes sharing one GPU for running LAMMPS and GROMACS molecular dynamics codes that use GPU offloading scheme of calculation (we use Ubuntu 18.04 with 4.15 kernel).

For example, if we run
```
cd lammps/examples/melt/
mpirun -np $NP  ../../src/lmp_hip -in in.melt -sf gpu -pk gpu 1
```
then for NP=1, 2 and (usually) 4 everything runs correctly. But if NP>4 the program either hangs during initialization (or a few first steps), or runs VERY slowly, or ends with the errors like

```
mpirun -np 10 ../../src/lmp_hip_all -in in.melt -sf gpu -pk gpu 1
LAMMPS (19 Jul 2019)
Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
Created orthogonal box = (0 0 0) to (167.96 167.96 167.96)
  1 by 2 by 5 MPI processor grid
Created 4000000 atoms
  create_atoms CPU = 0.18675 secs

--------------------------------------------------------------------------
- Using acceleration for lj/cut:
-  with 10 proc(s) per device.
--------------------------------------------------------------------------
Device 0: Vega 20, 60 CUs, 16/16 GB, 1.8 GHZ (Mixed Precision)
--------------------------------------------------------------------------

Initializing Device and compiling on process 0...Done.
Initializing Device 0 on core 0...Done.
Initializing Device 0 on core 1...Done.
Initializing Device 0 on core 2...Done.
Initializing Device 0 on core 3...Done.
Initializing Device 0 on core 4...Done.
Initializing Device 0 on core 5...Done.
Initializing Device 0 on core 6...Done.
Initializing Device 0 on core 7...Done.
Initializing Device 0 on core 8...Done.
Initializing Device 0 on core 9...Done.

Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Memory access fault by GPU node-4 (Agent handle: 0x28e9e40) on address 0x17000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21748] *** Process received signal ***
[jiht202overpc:21748] Signal: Aborted (6)
[jiht202overpc:21748] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x15262a0) on address 0x2a000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21756] *** Process received signal ***
[jiht202overpc:21756] Signal: Aborted (6)
[jiht202overpc:21756] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x22d45b0) on address 0x44000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21754] *** Process received signal ***
[jiht202overpc:21754] Signal: Aborted (6)
[jiht202overpc:21754] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x2b16e20) on address 0x34000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21747] *** Process received signal ***
[jiht202overpc:21747] Signal: Aborted (6)
[jiht202overpc:21747] Signal code:  (-6)
[jiht202overpc:21753] *** Process received signal ***
[jiht202overpc:21753] Signal: Aborted (6)
[jiht202overpc:21753] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x1fe75d0) on address 0x41000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21755] *** Process received signal ***
[jiht202overpc:21755] Signal: Aborted (6)
[jiht202overpc:21755] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x2003590) on address 0x25000. Reason: Page not present or supervisor privilege.
Memory access fault by GPU node-4 (Agent handle: 0x2df7de0) on address 0x19d000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21752] *** Process received signal ***
[jiht202overpc:21752] Signal: Aborted (6)
[jiht202overpc:21752] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x168cca0) on address 0x78000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21751] *** Process received signal ***
[jiht202overpc:21751] Signal: Aborted (6)
[jiht202overpc:21751] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x32fd870) on address 0x1f000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21750] *** Process received signal ***
[jiht202overpc:21750] Signal: Aborted (6)
[jiht202overpc:21750] Signal code:  (-6)
[jiht202overpc:21749] *** Process received signal ***
[jiht202overpc:21749] Signal: Aborted (6)
[jiht202overpc:21749] Signal code:  (-6)
Memory access fault by GPU node-4 (Agent handle: 0x199eef0) on address 0x9000. Reason: Page not present or supervisor privilege.
[jiht202overpc:21748] [ 0] /lib/x86_64-linux-gnu/libpthread.so.0(+0x12890)[0x7fb741106890]
[jiht202overpc:21748] [ 1] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0xc7)[0x7fb73f385e97]
[jiht202overpc:21748] [ 2] /lib/x86_64-linux-gnu/libc.so.6(abort+0x141)[0x7fb73f387801]
[jiht202overpc:21748] [ 3] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4f793)[0x7fb740234793]
[jiht202overpc:21748] [ 4] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4cd05)[0x7fb740231d05]
[jiht202overpc:21748] [ 5] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x12677)[0x7fb7401f7677]
[jiht202overpc:21748] [ 6] /lib/x86_64-linux-gnu/libpthread.so.0(+0x76db)[0x7fb7410fb6db]
[jiht202overpc:21748] [ 7] /lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7fb73f46888f]
[jiht202overpc:21748] *** End of error message ***
[jiht202overpc:21756] [ 0] /lib/x86_64-linux-gnu/libpthread.so.0(+0x12890)[0x7f5204d0a890]
[jiht202overpc:21756] [ 1] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0xc7)[0x7f5202f89e97]
[jiht202overpc:21756] [ 2] /lib/x86_64-linux-gnu/libc.so.6(abort+0x141)[0x7f5202f8b801]
[jiht202overpc:21756] [ 3] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4f793)[0x7f5203e38793]
[jiht202overpc:21756] [ 4] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4cd05)[0x7f5203e35d05]
[jiht202overpc:21756] [ 5] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x12677)[0x7f5203dfb677]
[jiht202overpc:21756] [ 6] /lib/x86_64-linux-gnu/libpthread.so.0(+0x76db)[0x7f5204cff6db]
[jiht202overpc:21756] [ 7] /lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7f520306c88f]
[jiht202overpc:21756] *** End of error message ***
[jiht202overpc:21747] [ 0] /lib/x86_64-linux-gnu/libpthread.so.0(+0x12890)[0x7f7307699890]
[jiht202overpc:21747] [ 1] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0xc7)[0x7f7305918e97]
[jiht202overpc:21747] [ 2] /lib/x86_64-linux-gnu/libc.so.6(abort+0x141)[0x7f730591a801]
[jiht202overpc:21747] [ 3] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4f793)[0x7f73067c7793]
[jiht202overpc:21747] [ 4] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4cd05)[0x7f73067c4d05]
[jiht202overpc:21747] [ 5] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x12677)[0x7f730678a677]
[jiht202overpc:21747] [ 6] /lib/x86_64-linux-gnu/libpthread.so.0(+0x76db)[0x7f730768e6db]
[jiht202overpc:21747] [ 7] /lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7f73059fb88f]
[jiht202overpc:21747] *** End of error message ***
[jiht202overpc:21755] [ 0] /lib/x86_64-linux-gnu/libpthread.so.0(+0x12890)[0x7f45e3e5b890]
[jiht202overpc:21755] [ 1] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0xc7)[0x7f45e20dae97]
[jiht202overpc:21755] [ 2] /lib/x86_64-linux-gnu/libc.so.6(abort+0x141)[0x7f45e20dc801]
[jiht202overpc:21755] [ 3] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4f793)[0x7f45e2f89793]
[jiht202overpc:21755] [ 4] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x4cd05)[0x7f45e2f86d05]
[jiht202overpc:21755] [ 5] /opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x12677)[0x7f45e2f4c677]
[jiht202overpc:21755] [ 6] /lib/x86_64-linux-gnu/libpthread.so.0(+0x76db)[0x7f45e3e506db]
[jiht202overpc:21755] [ 7] /lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7f45e21bd88f]
[jiht202overpc:21755] *** End of error message ***
--------------------------------------------------------------------------
mpirun noticed that process rank 9 with PID 0 on node jiht202overpc exited on signal 6 (Aborted).
--------------------------------------------------------------------------
```

This problem has been observed with OpenCL backends of LAMMPS and GROMACS (for LAMMPS [some manual modifications have been required](https://github.com/lammps/lammps/issues/1368) in order to make the code OpenCL 2.0 compliant).

We have just finished the [HIP-backend for LAMMPS](https://github.com/lammps/lammps/pull/1590). Unfortunately the problem remains for this case as well (however, only for HIP_PLATFORM=hcc but not for HIP_PLATFORM=nvcc).

This behaviour has been reproduced on Radeon RX 480, Radeon RX Vega and Radeon VII.

P.S. @pszi1ard could you please comment if you have observed the similar behaviour for GROMACS?