# Not more than 4 MPI processes can use one GPU in LAMMPS and GROMACS

> **Issue #851**
> **状态**: closed
> **创建时间**: 2019-07-28T20:23:11Z
> **更新时间**: 2020-01-22T19:51:20Z
> **关闭时间**: 2020-01-22T19:50:51Z
> **作者**: vvsteg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/851

## 描述

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

---

## 评论 (10 条)

### 评论 #1 — djygithub (2019-08-15T13:15:43Z)

Thanks for the LAMMPS gpu hip port, we are actively investigating.  Is there a similar gpu hip port for GROMACS?  We've noticed similar behaviour:
```
1) Tried -np = 10 on 4000000 atom model, went into an active busy and never finished, GPU at 100%, 100%-0% CPU on 10 processors off and on.


rocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$ mpirun -np 10 ../../src/lmp_hip -in in.melt -sf gpu -pk gpu 1
--------------------------------------------------------------------------
WARNING: No preset parameters were found for the device that Open MPI
detected:

  Local host:            prj47-rack-39
  Device name:           mlx5_0
  Device vendor ID:      0x02c9
  Device vendor part ID: 4119

Default device parameters will be used, which may result in lower
performance.  You can edit any of the files specified by the
btl_openib_device_param_files MCA parameter to set values for your
device.

NOTE: You can turn off this warning by setting the MCA parameter
      btl_openib_warn_no_device_params_found to 0.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           prj47-rack-39
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
LAMMPS (19 Jul 2019)
Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
Created orthogonal box = (0 0 0) to (167.96 167.96 167.96)
  1 by 2 by 5 MPI processor grid
Created 4000000 atoms
  create_atoms CPU = 0.0568209 secs

--------------------------------------------------------------------------
- Using acceleration for lj/cut:
-  with 10 proc(s) per device.
--------------------------------------------------------------------------
Device 0: Vega 10 [Radeon Instinct MI25], 64 CUs, 16/16 GB, 1.5 GHZ (Mixed Precision)
--------------------------------------------------------------------------

Initializing Device and compiling on process 0...Done.
Initializing Device 0 on core 0...Done.
Initializing Device 0 on core 1...Done.
Initializing Device 0 on core 2...Done.
Initializing Device 0 on core 3...Done.
Initializing Device 0 on core 4...[prj47-rack-39:06697] 9 more processes have sent help message help-mpi-btl-openib.txt / no device params found
[prj47-rack-39:06697] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
[prj47-rack-39:06697] 9 more processes have sent help message help-mpi-btl-openib-cpc-base.txt / no cpcs for port
Done.
Initializing Device 0 on core 5...Done.
Initializing Device 0 on core 6...Done.
Initializing Device 0 on core 7...Done.
Initializing Device 0 on core 8...Done.
Initializing Device 0 on core 9...Done.

Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 74.52 | 74.52 | 74.52 Mbytes
Step Temp E_pair E_mol TotEng Press
       0            3   -6.7733669            0    -2.273368   -3.7027193
      50    1.6689472   -4.7846766            0   -2.2812564    5.6693139
^Crocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$ cp in.melt in.meltsmall
rocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$ vi in.meltsmall

2) Switched to 4000 atom model, works just fine, doesn't scale.

rocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$ mpirun -np 1 ../../src/lmp_hip -in in.meltsmall -sf gpu -pk gpu 1
--------------------------------------------------------------------------
WARNING: No preset parameters were found for the device that Open MPI
detected:

  Local host:            prj47-rack-39
  Device name:           mlx5_0
  Device vendor ID:      0x02c9
  Device vendor part ID: 4119

Default device parameters will be used, which may result in lower
performance.  You can edit any of the files specified by the
btl_openib_device_param_files MCA parameter to set values for your
device.

NOTE: You can turn off this warning by setting the MCA parameter
      btl_openib_warn_no_device_params_found to 0.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           prj47-rack-39
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
LAMMPS (19 Jul 2019)
Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
Created orthogonal box = (0 0 0) to (16.796 16.796 16.796)
  1 by 1 by 1 MPI processor grid
Created 4000 atoms
  create_atoms CPU = 0.00051403 secs

--------------------------------------------------------------------------
- Using acceleration for lj/cut:
-  with 1 proc(s) per device.
--------------------------------------------------------------------------
Device 0: Vega 10 [Radeon Instinct MI25], 64 CUs, 16/16 GB, 1.5 GHZ (Mixed Precision)
--------------------------------------------------------------------------

Initializing Device and compiling on process 0...Done.
Initializing Device 0 on core 0...Done.

Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 2.279 | 2.279 | 2.279 Mbytes
Step Temp E_pair E_mol TotEng Press
       0            3   -6.7733683            0   -2.2744933   -3.7033503
      50    1.6758905   -4.7955428            0   -2.2823355    5.6700632
     100    1.6458363   -4.7492704            0   -2.2811331    5.8691036
     150    1.6324521   -4.7286779            0    -2.280612    5.9589665
     200    1.6630718   -4.7750897            0   -2.2811056    5.7365085
     250    1.6275673   -4.7225294            0   -2.2817888    5.9565647
Loop time of 0.0829411 on 1 procs for 250 steps with 4000 atoms

Performance: 1302129.562 tau/day, 3014.189 timesteps/s
89.7% CPU use with 1 MPI tasks x no OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 0.063057   | 0.063057   | 0.063057   |   0.0 | 76.03
Neigh   | 9.5367e-07 | 9.5367e-07 | 9.5367e-07 |   0.0 |  0.00
Comm    | 0.0095906  | 0.0095906  | 0.0095906  |   0.0 | 11.56
Output  | 0.00012898 | 0.00012898 | 0.00012898 |   0.0 |  0.16
Modify  | 0.0081568  | 0.0081568  | 0.0081568  |   0.0 |  9.83
Other   |            | 0.002007   |            |       |  2.42

Nlocal:    4000 ave 4000 max 4000 min
Histogram: 1 0 0 0 0 0 0 0 0 0
Nghost:    5499 ave 5499 max 5499 min
Histogram: 1 0 0 0 0 0 0 0 0 0
Neighs:    0 ave 0 max 0 min
Histogram: 1 0 0 0 0 0 0 0 0 0

Total # of neighbors = 0
Ave neighs/atom = 0
Neighbor list builds = 12
Dangerous builds not checked


---------------------------------------------------------------------
      Device Time Info (average):
---------------------------------------------------------------------
Data Transfer:   0.0181 s.
Data Cast/Pack:  0.0085 s.
Neighbor copy:   0.0005 s.
Neighbor build:  0.5583 s.
Force calc:      0.0171 s.
Device Overhead: 0.1027 s.
Average split:   1.0000.
Threads / atom:  4.
Max Mem / Proc:  5.76 MB.
CPU Driver_Time: 0.1039 s.
CPU Idle_Time:   0.0272 s.
---------------------------------------------------------------------


Please see the log.cite file for references relevant to this simulation

Total wall time: 0:00:00
rocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$ mpirun -np 10 ../../src/lmp_hip -in in.meltsmall -sf gpu -pk gpu 1
--------------------------------------------------------------------------
WARNING: No preset parameters were found for the device that Open MPI
detected:

  Local host:            prj47-rack-39
  Device name:           mlx5_0
  Device vendor ID:      0x02c9
  Device vendor part ID: 4119

Default device parameters will be used, which may result in lower
performance.  You can edit any of the files specified by the
btl_openib_device_param_files MCA parameter to set values for your
device.

NOTE: You can turn off this warning by setting the MCA parameter
      btl_openib_warn_no_device_params_found to 0.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           prj47-rack-39
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
LAMMPS (19 Jul 2019)
Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
Created orthogonal box = (0 0 0) to (16.796 16.796 16.796)
  1 by 2 by 5 MPI processor grid
Created 4000 atoms
  create_atoms CPU = 0.000324965 secs

--------------------------------------------------------------------------
- Using acceleration for lj/cut:
-  with 10 proc(s) per device.
--------------------------------------------------------------------------
Device 0: Vega 10 [Radeon Instinct MI25], 64 CUs, 16/16 GB, 1.5 GHZ (Mixed Precision)
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
Initializing Device 0 on core 9...[prj47-rack-39:07762] 9 more processes have sent help message help-mpi-btl-openib.txt / no device params found
[prj47-rack-39:07762] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
[prj47-rack-39:07762] 9 more processes have sent help message help-mpi-btl-openib-cpc-base.txt / no cpcs for port
Done.

Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 2.045 | 2.057 | 2.06 Mbytes
Step Temp E_pair E_mol TotEng Press
       0            3   -6.7733683            0   -2.2744933   -3.7033503
      50    1.6713349   -4.7888115            0   -2.2824359    5.6826191
     100    1.6393734   -4.7394723            0    -2.281027    5.8545519
     150     1.638166   -4.7380989            0   -2.2814642    5.8912232
     200    1.6506131   -4.7572646            0   -2.2819639    5.8083835
     250     1.654332    -4.762575            0   -2.2816973    5.8134024
Loop time of 57.1239 on 10 procs for 250 steps with 4000 atoms

Performance: 1890.628 tau/day, 4.376 timesteps/s
97.5% CPU use with 10 MPI tasks x no OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 1.879      | 12.402     | 31.697     | 296.1 | 21.71
Neigh   | 3.3379e-06 | 5.126e-06  | 6.6757e-06 |   0.0 |  0.00
Comm    | 25.325     | 44.623     | 55.131     | 155.9 | 78.12
Output  | 0.019604   | 0.096243   | 0.11173    |   8.5 |  0.17
Modify  | 0.0010233  | 0.0011042  | 0.0012636  |   0.2 |  0.00
Other   |            | 0.001299   |            |       |  0.00

Nlocal:    400 ave 413 max 386 min
Histogram: 1 0 1 0 3 1 2 1 0 1
Nghost:    1963.6 ave 1983 max 1939 min
Histogram: 1 0 1 1 0 2 1 2 1 1
Neighs:    0 ave 0 max 0 min
Histogram: 10 0 0 0 0 0 0 0 0 0

Total # of neighbors = 0
Ave neighs/atom = 0
Neighbor list builds = 12
Dangerous builds not checked


---------------------------------------------------------------------
      Device Time Info (average):
---------------------------------------------------------------------
Data Transfer:   8.8734 s.
Data Cast/Pack:  0.0016 s.
Neighbor copy:   0.0014 s.
Neighbor build:  1.7425 s.
Force calc:      0.0179 s.
Device Overhead: 111.1792 s.
Average split:   1.0000.
Threads / atom:  4.
Max Mem / Proc:  0.76 MB.
CPU Driver_Time: 12.8693 s.
CPU Idle_Time:   10.7917 s.
---------------------------------------------------------------------


Please see the log.cite file for references relevant to this simulation

Total wall time: 0:01:09
rocm@prj47-rack-39:~/hiplammps20190808/lammps/examples/melt$

```

---

### 评论 #2 — vvsteg (2019-08-15T14:04:27Z)

> Is there a similar gpu hip port for GROMACS?

As far as I know, there is only an OpenCL port of GROMACS. But it shows similar problems when running with the ROCm GPU driver in case of more than 4 MPI ranks per GPU.

---

### 评论 #3 — djygithub (2019-09-21T22:39:07Z)

Thanks again for the gpu_hip_port works, scales on MI25, MI50, and MI60 (single and multiple GPU).  Having an issue building the nvcc version on an I7-7700 with an Nvidia GTX-1050, have you seen similar or is there a workaround?  Thanks
```
/opt/rocm/hip/bin/hipcc -Wno-deprecated-declarations -DUSE_HIP_DEVICE_SORT  -DMPI_GERYON -DUCL_NO_EXIT -O3  --use_fast_math -DUSE_HIP -D_SINGLE_DOUBLE -I/usr/local/include -Xcompiler -pthread -DLAMMPS_SMALLBIG  -I./ -I/opt/rocm/hip/../include -o hip_get_devices geryon/ucl_get_devices.cpp -DUCL_HIP -Xcompiler -pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi
nvcc fatal   : Unknown option 'Wl,-rpath'
make: *** [Makefile.hip:145: hip_get_devices] Error 1
make: *** Waiting for unfinished jobs....
[david@i77700centos76 gpu]$ nvidia-smi
Sat Sep 21 15:21:57 2019
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.67       Driver Version: 418.67       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1050    Off  | 00000000:01:00.0 Off |                  N/A |
| 35%   29C    P8    N/A /  75W |      0MiB /  2000MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
[david@i77700centos76 gpu]$ dkms status
amdgpu, 2.7-22.el7, 3.10.0-957.21.3.el7.x86_64, x86_64: installed
amdgpu, 2.7-22.el7, 4.16.18, x86_64: installed
nvidia, 418.67, 3.10.0-957.21.3.el7.x86_64, x86_64: installed
nvidia, 418.67, 4.16.18, x86_64: installed
[david@i77700centos76 gpu]$ uname -a
Linux i77700centos76 4.16.18 #1 SMP Mon Jul 8 16:20:43 PDT 2019 x86_64 x86_64 x86_64 GNU/Linux
[david@i77700centos76 gpu]$
```

---

### 评论 #4 — vvsteg (2019-09-24T12:01:46Z)

On my system with OpenMPI the compilation is successful if I use
```
MPI_COMP_OPTS = $(shell mpicxx --showme:compile)
MPI_LINK_OPTS = $(shell mpicxx --showme:link)
```
in Makefile.hip.

The resulting line looks like this:
```
/opt/rocm/hip/bin/hipcc -Wno-deprecated-declarations -DUSE_HIP_DEVICE_SORT  -DMPI_GERYON -DUCL_NO_EXIT -fPIC -O3  -ffast-math -DUSE_HIP -D_SINGLE_SINGLE -I/usr/lib/x86_64-linux-gnu/openmpi/include/openmpi -I/usr/lib/x86_64-linux-gnu/openmpi/include/openmpi/opal/mca/event/libevent2022/libevent -I/usr/lib/x86_64-linux-gnu/openmpi/include/openmpi/opal/mca/event/libevent2022/libevent/include -I/usr/lib/x86_64-linux-gnu/openmpi/include -pthread -DLAMMPS_SMALLBIG  -I./ -I/opt/rocm/hip/../include -o hip_get_devices geryon/ucl_get_devices.cpp -DUCL_HIP -pthread -L/usr//lib -L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi_cxx -lmpi
```

Do you use MPICH or MVAPICH on your system?

---

### 评论 #5 — djygithub (2019-09-24T15:28:09Z)

Using openmpi 4 should I try MPICH? Thanks.
```
[david@i77700centos76 bin]$ ./ompi_info
                 Package: Open MPI david@i77700centos76 Distribution
                Open MPI: 4.0.1
  Open MPI repo revision: v4.0.1
   Open MPI release date: Mar 26, 2019
[david@i77700centos76 gpu]$ mpicxx --showme compile
g++ compile -I/usr/local/include -pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi
[david@i77700centos76 gpu]$ mpicxx --showme link
g++ link -I/usr/local/include -pthread -Wl,-rpath -Wl,/usr/local/lib -Wl,--enable-new-dtags -L/usr/local/lib -lmpi
[david@i77700centos76 gpu]$
```
This is the line that successfully built a hip version on another machine:
```
/opt/rocm/hip/bin/hipcc -g -O3 -pthread -Wl,-rpath -Wl,/home/superdome01/openmpi401install/lib -Wl,--enable-new-dtags -L/home/superdome01/openmpi401install/lib -lmpi      compute_rdf.o pair_dpd.o atom_vec_tri.o pair_lj_cut_coul_dsf.o compute_heat_flux.o npair_full_multi.o fix_gravity.o lattice.o nstencil_half_bin_2d_newtoff.o nstencil_half_multi_2d_newton_tri.o write_dump.o reset_ids.o compute_omega_chunk.o compute_temp_partial.o ntopo_improper_template.o comm_tiled.o compute_property_local.o thermo.o npair_half_bin_atomonly_newton.o nbin.o region_plane.o kspace_deprecated.o random_mars.o compute_bond_local.o pair_coul_streitz.o fix_lineforce.o ntopo_bond_partial.o npair.o pair_ufm.o imbalance.o create_box.o compute_com.o compute_ke.o pair_lj_expand.o delete_bonds.o nstencil_full_multi_3d.o compute_temp_sphere.o library.o compute_erotate_sphere_atom.o nstencil_half_ghost_bin_2d_newtoff.o compute_gyration_chunk.o fix_move.o pair_lj_gromacs_coul_gromacs.o npair_copy.o fix_spring_self.o pair_hybrid.o compute_angle.o dump_movie.o atom_vec_line.o respa.o compute_improper_local.o input.o fix_wall.o pair_lj96_cut.o compute_pe_atom.o pair_beck.o compute_reduce.o npair_skip_size_off2on.o min_hftn.o compute_pair_local.o pair_zero.o compute_temp_region.o angle_zero.o imbalance_var.o fix_recenter.o fix_wall_lj93.o reader.o improper_hybrid.o npair_full_nsq_ghost.o fix_box_relax.o pair_lj_cut_coul_debye.o read_restart.o npair_half_nsq_newtoff_ghost.o fix_store.o atom_vec_body.o compute_group_group.o nstencil_half_ghost_bin_3d_newtoff.o universe.o compute_erotate_sphere.o pair_born_coul_wolf.o compute_dipole_chunk.o fix_print.o improper_zero.o compute_contact_atom.o pair_morse.o region_intersect.o compute_hexorder_atom.o fix_langevin.o output.o compute_angmom_chunk.o npair_halffull_newtoff.o integrate.o angle_hybrid.o npair_full_bin.o pair_born.o nstencil_half_bin_2d_newton_tri.o fix_ave_correlate.o compute_msd_chunk.o compute_coord_atom.o neigh_request.o domain.o compute_msd.o ntopo_angle_template.o region.o compute_improper.o read_data.o fix_store_state.o pair_lj_smooth.o fix_enforce2d.o pair_soft.o nstencil_full_bin_3d.o compute_cna_atom.o utils.o npair_full_nsq.o fix_temp_csld.o pair_lj_cut_coul_cut.o fix_spring_chunk.o fix_deprecated.o region_union.o finish.o min_fire.o neighbor.o fix_nph_sphere.o pair_table.o fix_vector.o imbalance_group.o nstencil.o fix_tmd.o npair_skip_size.o npair_skip_respa.o molecule.o random_park.o compute_temp_deform.o npair_half_bin_newtoff.o velocity.o fix_nph.o pair_lj_smooth_linear.o min_cg.o hashlittle.o procmap.o compute_gyration.o pair_born_coul_dsf.o imbalance_neigh.o npair_half_size_nsq_newton.o npair_halffull_newton.o fix_temp_rescale.o npair_skip.o nstencil_full_ghost_bin_2d.o math_special.o pair_mie_cut.o force.o ntopo_dihedral_template.o variable.o set.o compute_dihedral_local.o compute_angle_local.o ntopo_improper_partial.o bond.o displace_atoms.o improper.o reader_xyz.o compute_com_chunk.o compute_adf.o nstencil_half_multi_2d_newtoff.o pair_deprecated.o min_linesearch.o angle_deprecated.o write_coeff.o neigh_list.o fix_viscous.o rerun.o compute.o read_dump.o atom.o fix_press_berendsen.o nstencil_half_multi_2d_newton.o fix_wall_harmonic.o minimize.o compute_chunk_atom.o compute_pair.o min.o npair_half_size_bin_newtoff.o math_extra.o dihedral_zero.o pair_buck_coul_cut.o ntopo_bond_template.o compute_centro_atom.o pair_zbl.o pair_buck.o comm.o atom_vec_charge.o compute_deprecated.o ntopo_angle_all.o npair_skip_size_off2on_oneside.o imbalance_store.o atom_vec.o fix_wall_reflect.o region_deprecated.o fix_indent.o bond_hybrid.o fix_planeforce.o compute_stress_atom.o fix_respa.o fix_spring.o fix_nvt_sllod.o nstencil_full_bin_2d.o compute_reduce_chunk.o npair_half_size_bin_newton.o npair_half_respa_bin_newton.o rcb.o compute_reduce_region.o error.o compute_pressure.o nbin_standard.o npair_half_multi_newtoff.o fix_property_atom.o npair_half_nsq_newtoff.o compute_cluster_atom.o delete_atoms.o ntopo_dihedral_partial.o pair_lj_cubic.o compute_displace_atom.o body.o compute_dihedral.o npair_half_bin_newton.o pair_coul_wolf.o main.o npair_half_size_bin_newton_tri.o pair_coul_dsf.o pair_lj_cut_coul_wolf.o nstencil_half_multi_3d_newtoff.o nstencil_half_bin_2d_newton.o npair_half_respa_bin_newton_tri.o image.o fix.o balance.o compute_global_atom.o lammps.o fix_dt_reset.o region_sphere.o comm_brick.o ntopo_dihedral_all.o fix_addforce.o citeme.o nstencil_half_bin_3d_newton.o npair_half_bin_newton_tri.o region_cylinder.o atom_vec_sphere.o create_bonds.o write_data.o pair_lj_gromacs.o compute_bond.o compute_fragment_atom.o fix_ave_histo_weight.o pair_dpd_tstat.o fix_restrain.o fix_store_force.o fix_balance.o create_atoms.o compute_torque_chunk.o pair.o bond_deprecated.o timer.o pair_coul_debye.o fix_external.o compute_inertia_chunk.o compute_property_chunk.o pair_lj_cut.o nstencil_half_bin_3d_newton_tri.o fix_nvt_sphere.o fix_drag.o replicate.o fix_npt.o lmppython.o pair_hybrid_overlay.o compute_ke_atom.o fix_ave_histo.o dihedral_deprecated.o write_restart.o dump_image.o bond_zero.o fix_read_restart.o compute_property_atom.o ntopo_bond_all.o compute_chunk_spread_atom.o fix_deform.o fix_minimize.o fix_wall_lj1043.o ntopo_improper_all.o dihedral.o pair_gauss.o dump_dcd.o change_box.o region_prism.o min_quickmin.o verlet.o npair_full_bin_atomonly.o npair_full_bin_ghost.o kspace.o compute_temp_chunk.o atom_vec_ellipsoid.o atom_vec_hybrid.o nstencil_full_multi_2d.o atom_map.o min_sd.o pair_coul_cut.o fix_momentum.o npair_half_respa_nsq_newton.o npair_half_size_nsq_newtoff.o fix_adapt.o group.o dump_xyz.o pair_yukawa.o compute_temp_ramp.o imbalance_time.o fix_nvt.o nstencil_full_ghost_bin_3d.o fix_heat.o nstencil_half_bin_3d_newtoff.o modify.o improper_deprecated.o npair_half_multi_newton.o update.o fix_nve_limit.o reader_native.o atom_vec_atomic.o fix_temp_berendsen.o fix_setforce.o compute_temp_profile.o dihedral_hybrid.o dump_custom.o fix_controller.o dump_atom.o compute_orientorder_atom.o fix_ave_chunk.o region_block.o deprecated.o fix_npt_sphere.o dump.o memory.o dump_local.o fix_spring_rg.o dump_cfg.o angle.o fix_ave_atom.o fix_temp_csvr.o fix_wall_region.o nstencil_half_multi_3d_newton.o compute_slice.o npair_half_multi_newton_tri.o fix_halt.o compute_temp_com.o fix_nh.o fix_wall_lj126.o compute_aggregate_atom.o info.o fix_nve_sphere.o npair_half_nsq_newton.o compute_pe.o region_cone.o compute_vacf.o fix_neigh_history.o dump_deprecated.o npair_half_respa_bin_newtoff.o fix_aveforce.o irregular.o compute_temp.o compute_vcm_chunk.o special.o npair_half_respa_nsq_newtoff.o run.o nstencil_half_multi_3d_newton_tri.o npair_half_bin_newtoff_ghost.o fix_nve_noforce.o ntopo.o fix_ave_time.o ntopo_angle_partial.o fix_nve.o fix_nh_sphere.o fix_group.o       -o ../lmp_hip
size ../lmp_hip
   text    data     bss     dec     hex filename
3867752    8233   15264 3891249  3b6031 ../lmp_hip
make[1]: Leaving directory `/home/superdome01/lammps/src/Obj_hip'
[superdome01@Superdome01 src]$
[superdome01@Superdome01 ~]$ mpicxx --showme:link
-pthread -Wl,-rpath -Wl,/home/superdome01/openmpi401install/lib -Wl,--enable-new-dtags -L/home/superdome01/openmpi401install/lib -lmpi
[superdome01@Superdome01 ~]$ mpicxx --showme:compile
-I/home/superdome01/openmpi401install/include -pthread
[superdome01@Superdome01 ~]$
```

---

### 评论 #6 — djygithub (2019-09-24T18:33:35Z)

Removed openmpi, installed mpich, updated Makefile.hip with -show compile and -show link, O flag used twice.  Took out O3 and resubmitted, nvcc fatal Unknown option pipe:
```
/opt/rocm/hip/bin/hipcc -Wno-deprecated-declarations -DUSE_HIP_DEVICE_SORT  -DMPI_GERYON -DUCL_NO_EXIT -O3  --use_fast_math -DUSE_HIP -D_SINGLE_DOUBLE g++ -m64 -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -Wl,-z,noexecstack compile -I/usr/include/mpich-3.2-x86_64 -L/usr/lib64/mpich-3.2/lib -lmpicxx -Wl,-rpath -Wl,/usr/lib64/mpich-3.2/lib -Wl,--enable-new-dtags -lmpi -DLAMMPS_SMALLBIG  -I./ -I/opt/rocm/hip/../include -o hip_get_devices geryon/ucl_get_devices.cpp -DUCL_HIP
nvcc fatal   : redefinition of argument 'optimize'
make: *** [Makefile.hip:145: hip_get_devices] Error 1
make: *** Waiting for unfinished jobs....
[david@i77700centos76 gpu]$ mpicxx -show compile
g++ -m64 -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -Wl,-z,noexecstack compile -I/usr/include/mpich-3.2-x86_64 -L/usr/lib64/mpich-3.2/lib -lmpicxx -Wl,-rpath -Wl,/usr/lib64/mpich-3.2/lib -Wl,--enable-new-dtags -lmpi
[david@i77700centos76 gpu]$ mpicxx -show link
g++ -m64 -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -Wl,-z,noexecstack link -I/usr/include/mpich-3.2-x86_64 -L/usr/lib64/mpich-3.2/lib -lmpicxx -Wl,-rpath -Wl,/usr/lib64/mpich-3.2/lib -Wl,--enable-new-dtags -lmpi
[david@i77700centos76 gpu]$ /opt/rocm/hip/bin/hipcc -Wno-deprecated-declarations -DUSE_HIP_DEVICE_SORT  -DMPI_GERYON -DUCL_NO_EXIT -O3  --use_fast_math -DUSE_HIP -D_SINGLE_DOUBLE g++ -m64  -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -Wl,-z,noexecstack compile -I/usr/include/mpich-3.2-x86_64 -L/usr/lib64/mpich-3.2/lib -lmpicxx -Wl,-rpath -Wl,/usr/lib64/mpich-3.2/lib -Wl,--enable-new-dtags -lmpi -DLAMMPS_SMALLBIG  -I./ -I/opt/rocm/hip/../include -o hip_get_devices geryon/ucl_get_devices.cpp -DUCL_HIP
nvcc fatal   : Unknown option 'pipe'

```

---

### 评论 #7 — vvsteg (2019-10-07T11:35:45Z)

Sorry for the long silence.

I have installed OpenMPI 3.1.4 and compiled LAMMPS with `nvcc` for my Nvidia GPU after I changed

```
MPI_LINK_OPTS := $(subst -pthread,-Xcompiler -pthread,$(MPI_LINK_OPTS))
```
to
```
MPI_LINK_OPTS := -Xcompiler -pthread -L/home/vlad/openmpi-3.1.4/lib -lmpi
```

The corresponding change should be made in Makefile.hip as well.


There is no such a problem with OpenMPI-2.1.1 that is a default one on my box.
OpenMPI-2.1.1 has a simpler linking rule:
```
mpicxx --showme:link
-pthread -L/usr//lib -L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi_cxx -lmpi
```


But for OpenMPI-3.1.4 the linking rule is more compicated
```
/home/vlad/openmpi-3.1.4/bin/mpicxx --showme:link
-pthread -Wl,-rpath -Wl,/home/vlad/openmpi-3.1.4/lib -Wl,--enable-new-dtags -L/home/vlad/openmpi-3.1.4/lib -lmpi
```

The problem is that `nvcc` compiler has some difficulties in passing `-Wl` linker options to `gcc` compiler. Fortunately, it works after removing these `-Wl` options (as shown above).

There is no such a problem with compilation for Radeon VII with `hipcc`. OpenMPI 3.1.4 just works without any tricks in existing makefiles.


---

### 评论 #8 — vvsteg (2019-10-07T18:21:59Z)

Using mpich you have only the command
```
mpicxx -show
```
If you add `compile` or `link` they go to the line.

Moreover, while passing these arguments to `MPI_LINK_OPTS`, one should remove `g++` from the beginning of the line!

At the moment, I see no clever way how to design Makefile.hip with a universal linking procedure for any MPI library.

Fortunately, these problems have been found for `nvcc` HIP backend only. Building with `hipcc` works well with the current variant of Makefile.hip. 

---

### 评论 #9 — skyreflectedinmirrors (2019-10-18T21:40:50Z)

@vvsteg -- I've been looking at the nvcc backend issue on behalf of @djygithub.  I think the main problem here is that we need to separate out which files actually require MPI compilation flags so that we don't have to deal NVCC's linking issues.  You can see an example of this in the `Nvidia.makefile` included in the GPU lib.  I'll try to take another look at this next week to see if we can improve the build system.

I also have some thoughts on the MPI-processes issue, but have to dig further.

Nick C., AMD Research

---

### 评论 #10 — vvsteg (2020-01-22T19:50:51Z)

The problem does not exist with ROCm 3.0. So I am closing the issue.

---
