# GROMACS regression tests fail on Vega with ROCm 1.8

> **Issue #427**
> **状态**: closed
> **创建时间**: 2018-05-31T18:12:21Z
> **更新时间**: 2018-06-11T10:59:20Z
> **关闭时间**: 2018-06-03T12:48:44Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/427

## 描述

Multiple regressiontests fail on ROCm 1.8 while these do pass with AMDGPU-PRO.

To reproduce follow the "Quick and dirty" installation instructions and the `make check` stage should reveal the issues: http://manual.gromacs.org/documentation/2018/install-guide/index.html#quick-and-dirty-installation.

---

## 评论 (6 条)

### 评论 #1 — gstoner (2018-06-01T13:46:03Z)

Here is what we see 

taccuser@ROCM-REL-VG10:~/Desktop/gromacs/gromacs-2018/build$ make check
[  0%] Built target view_objlib
[  2%] Built target tng_io_obj
[  2%] Built target fftwBuild
[  2%] Built target tng_io_zlib
[ 83%] Built target libgromacs
[ 84%] Built target mdrun_objlib
[ 84%] Built target gmx
[ 84%] Built target gmxtests
[ 84%] Built target mdrun_test_objlib
[ 84%] Built target gmock
[ 86%] Built target testutils
[ 87%] Built target mdrun-mpi-test
[ 87%] Built target testutils-mpi-test
[ 87%] Built target testutils-test
[ 87%] Built target mdlib-test
[ 87%] Built target applied-forces-test
[ 87%] Built target listed-forces-test
[ 87%] Built target onlinehelp-test-shared
[ 87%] Built target commandline-test
[ 87%] Built target ewald-test
[ 88%] Built target fft-test
[ 88%] Built target gpu_utils-test
[ 88%] Built target hardware-test
[ 89%] Built target math-test
[ 89%] Built target mdrunutility-test-shared
[ 89%] Built target mdrunutility-mpi-test
[ 89%] Built target mdrunutility-test
[ 89%] Built target onlinehelp-test
[ 90%] Built target options-test
[ 91%] Built target random-test
[ 91%] Built target table-test
[ 91%] Built target taskassignment-test
[ 92%] Built target utility-test
[ 93%] Built target fileio-test
[ 93%] Built target pull-test
[ 94%] Built target awh-test
[ 96%] Built target simd-test
[ 96%] Built target gmxana-test
[ 97%] Built target gmxpreprocess-test
[ 97%] Built target correlations-test
[ 97%] Built target analysisdata-test-shared
[ 97%] Built target analysisdata-test
[ 97%] Built target selection-test
[ 98%] Built target trajectoryanalysis-test
[ 98%] Built target energyanalysis-test
[100%] Built target compat-test
[100%] Built target mdrun-test
[100%] Built target tests
[100%] Running all tests except physical validation
Test project /home/taccuser/Desktop/gromacs/gromacs-2018/build
      Start  1: TestUtilsUnitTests
 1/39 Test  #1: TestUtilsUnitTests ...............   Passed    0.29 sec
      Start  2: TestUtilsMpiUnitTests
 2/39 Test  #2: TestUtilsMpiUnitTests ............   Passed    0.01 sec
      Start  3: MdlibUnitTest
 3/39 Test  #3: MdlibUnitTest ....................   Passed    0.11 sec
      Start  4: AppliedForcesUnitTest
 4/39 Test  #4: AppliedForcesUnitTest ............   Passed    0.03 sec
      Start  5: ListedForcesTest
 5/39 Test  #5: ListedForcesTest .................   Passed    0.08 sec
      Start  6: CommandLineUnitTests
 6/39 Test  #6: CommandLineUnitTests .............   Passed    0.22 sec
      Start  7: EwaldUnitTests
 7/39 Test  #7: EwaldUnitTests ...................   Passed    0.76 sec
      Start  8: FFTUnitTests
 8/39 Test  #8: FFTUnitTests .....................   Passed    0.08 sec
      Start  9: GpuUtilsUnitTests
 9/39 Test  #9: GpuUtilsUnitTests ................   Passed    0.15 sec
      Start 10: HardwareUnitTests
10/39 Test #10: HardwareUnitTests ................   Passed    0.33 sec
      Start 11: MathUnitTests
11/39 Test #11: MathUnitTests ....................   Passed    0.08 sec
      Start 12: MdrunUtilityUnitTests
12/39 Test #12: MdrunUtilityUnitTests ............   Passed    0.05 sec
      Start 13: MdrunUtilityMpiUnitTests
13/39 Test #13: MdrunUtilityMpiUnitTests .........   Passed    0.05 sec
      Start 14: OnlineHelpUnitTests
14/39 Test #14: OnlineHelpUnitTests ..............   Passed    0.15 sec
      Start 15: OptionsUnitTests
15/39 Test #15: OptionsUnitTests .................   Passed    0.07 sec
      Start 16: RandomUnitTests
16/39 Test #16: RandomUnitTests ..................   Passed    0.08 sec
      Start 17: TableUnitTests
17/39 Test #17: TableUnitTests ...................   Passed    0.14 sec
      Start 18: TaskAssignmentUnitTests
18/39 Test #18: TaskAssignmentUnitTests ..........   Passed    0.04 sec
      Start 19: UtilityUnitTests
19/39 Test #19: UtilityUnitTests .................   Passed    0.06 sec
      Start 20: FileIOTests
20/39 Test #20: FileIOTests ......................   Passed    0.07 sec
      Start 21: PullTest
21/39 Test #21: PullTest .........................   Passed    0.04 sec
      Start 22: AwhTest
22/39 Test #22: AwhTest ..........................   Passed    0.03 sec
      Start 23: SimdUnitTests
23/39 Test #23: SimdUnitTests ....................   Passed    0.06 sec
      Start 24: GmxAnaTest
24/39 Test #24: GmxAnaTest .......................   Passed    0.12 sec
      Start 25: GmxPreprocessTests
25/39 Test #25: GmxPreprocessTests ...............   Passed    0.40 sec
      Start 26: CorrelationsTest
26/39 Test #26: CorrelationsTest .................   Passed    0.27 sec
      Start 27: AnalysisDataUnitTests
27/39 Test #27: AnalysisDataUnitTests ............   Passed    0.14 sec
      Start 28: SelectionUnitTests
28/39 Test #28: SelectionUnitTests ...............   Passed    0.21 sec
      Start 29: TrajectoryAnalysisUnitTests
29/39 Test #29: TrajectoryAnalysisUnitTests ......   Passed    0.63 sec
      Start 30: EnergyAnalysisUnitTests
30/39 Test #30: EnergyAnalysisUnitTests ..........   Passed    0.11 sec
      Start 31: CompatibilityHelpersTests
31/39 Test #31: CompatibilityHelpersTests ........   Passed    0.05 sec
      Start 32: MdrunTests
32/39 Test #32: MdrunTests .......................   Passed    7.31 sec
      Start 33: MdrunMpiTests
33/39 Test #33: MdrunMpiTests ....................   Passed    0.35 sec
      Start 34: regressiontests/simple
34/39 Test #34: regressiontests/simple ...........   Passed   16.45 sec
      Start 35: regressiontests/complex
35/39 Test #35: regressiontests/complex ..........   Passed   46.35 sec
      Start 36: regressiontests/kernel
36/39 Test #36: regressiontests/kernel ...........   Passed   94.67 sec
      Start 37: regressiontests/freeenergy
37/39 Test #37: regressiontests/freeenergy .......   Passed   14.40 sec
      Start 38: regressiontests/pdb2gmx
38/39 Test #38: regressiontests/pdb2gmx ..........   Passed   20.60 sec
      Start 39: regressiontests/rotation
39/39 Test #39: regressiontests/rotation .........   Passed    7.98 sec

100% tests passed, 0 tests failed out of 39

Label Time Summary:
GTest              =  12.56 sec (33 tests)
IntegrationTest    =   7.79 sec (3 tests)
MpiTest            =   0.41 sec (3 tests)
UnitTest           =   4.77 sec (30 tests)

Total Test time (real) = 213.14 sec
[100%] Built target run-ctest-nophys
[100%] Built target check
taccuser@ROCM-REL-VG10:~/Desktop/gromacs/gromacs-2018/build$ 

---

### 评论 #2 — gstoner (2018-06-01T13:46:25Z)

This is ROCm 1.8 and newer 1.8.1 we working on 


---

### 评论 #3 — rkothako (2018-06-07T06:44:25Z)

Yes @pszi1ard , We are not observing any failures as Greg said.
All 39 tests PASSED on Vega10 XTX 16GB card.

---

### 评论 #4 — pszi1ard (2018-06-09T22:49:40Z)

@gstoner @rkothako Thanks for running the tests. Please help me figure out where is the discrepancy as I can 100% repro failing MdrunTests unit test on my hardware with the latest ROCm from the deb repos:
```
$ make check 
[       OK ] WithDifferentOutputGroupSettings/MdrunCompressedXOutput.ExitsNormally/2 (63 ms)
[----------] 3 tests from WithDifferentOutputGroupSettings/MdrunCompressedXOutput (196 ms total)

[----------] Global test environment tear-down
[==========] 30 tests from 11 test cases ran. (47427 ms total)
[  PASSED  ] 29 tests.
[  FAILED  ] 1 test, listed below:
[  FAILED  ] PmeTest.ReproducesEnergies

 1 FAILED TEST

      Start 33: MdrunMpiTests
33/39 Test #33: MdrunMpiTests ....................   Passed    3.34 sec
      Start 34: regressiontests/simple
34/39 Test #34: regressiontests/simple ...........   Passed    6.60 sec
      Start 35: regressiontests/complex
35/39 Test #35: regressiontests/complex ..........   Passed  196.31 sec
      Start 36: regressiontests/kernel
36/39 Test #36: regressiontests/kernel ...........   Passed   72.56 sec
      Start 37: regressiontests/freeenergy
37/39 Test #37: regressiontests/freeenergy .......   Passed   17.69 sec
      Start 38: regressiontests/pdb2gmx
38/39 Test #38: regressiontests/pdb2gmx ..........   Passed   40.21 sec
      Start 39: regressiontests/rotation
39/39 Test #39: regressiontests/rotation .........   Passed    6.51 sec

97% tests passed, 1 tests failed out of 39

Label Time Summary:
GTest              =  56.43 sec (33 tests)
IntegrationTest    =  51.00 sec (3 tests)
MpiTest            =   3.38 sec (3 tests)
UnitTest           =   5.43 sec (30 tests)

Total Test time (real) = 396.52 sec

The following tests FAILED:
         32 - MdrunTests (Failed)
Errors while running CTest
CMakeFiles/run-ctest-nophys.dir/build.make:57: recipe for target 'CMakeFiles/run-ctest-nophys' failed
make[3]: *** [CMakeFiles/run-ctest-nophys] Error 8
CMakeFiles/Makefile2:1256: recipe for target 'CMakeFiles/run-ctest-nophys.dir/all' failed
make[2]: *** [CMakeFiles/run-ctest-nophys.dir/all] Error 2
CMakeFiles/Makefile2:1067: recipe for target 'CMakeFiles/check.dir/rule' failed
make[1]: *** [CMakeFiles/check.dir/rule] Error 2
Makefile:587: recipe for target 'check' failed
make: *** [check] Error 2
```

The same build / binary on a different machine (same OS) with a Fiji passes the test however.

----------------------------------------------------
Now, as a side-note, unfortunately, due to a bug in our end-to-end regressiontest script, some failing tests don't get reported. Can you also try running them manually, please, i.e.:
```
$ cd ~/Desktop/gromacs/gromacs-2018/build/tests/regressiontests-release-2018-352b8a5
$ PATH="$HOME/Desktop/gromacs/gromacs-2018/build/bin:$PATH"  perl gmxtest.pl -xml complex -nt 1

            :-) GROMACS - gmx mdrun, 2018.2-dev-20180522-52677c5 (-:

                            GROMACS is written by:
     Emile Apol      Rossen Apostolov      Paul Bauer     Herman J.C. Berendsen
    Par Bjelkmar    Aldert van Buuren   Rudi van Drunen     Anton Feenstra
  Gerrit Groenhof    Aleksei Iupinov   Christoph Junghans   Anca Hamuraru
 Vincent Hindriksen Dimitrios Karkoulis    Peter Kasson        Jiri Kraus
  Carsten Kutzner      Per Larsson      Justin A. Lemkul    Viveca Lindahl
  Magnus Lundborg   Pieter Meulenhoff    Erik Marklund      Teemu Murtola
    Szilard Pall       Sander Pronk      Roland Schulz     Alexey Shvetsov
   Michael Shirts     Alfons Sijbers     Peter Tieleman    Teemu Virolainen
 Christian Wennberg    Maarten Wolf
                           and the project leaders:
        Mark Abraham, Berk Hess, Erik Lindahl, and David van der Spoel

Copyright (c) 1991-2000, University of Groningen, The Netherlands.
Copyright (c) 2001-2017, The GROMACS development team at
Uppsala University, Stockholm University and
the Royal Institute of Technology, Sweden.
check out http://www.gromacs.org for more information.

GROMACS is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation; either version 2.1
of the License, or (at your option) any later version.

GROMACS:      gmx mdrun, version 2018.2-dev-20180522-52677c5
Executable:   /nethome/pszilard-projects/gromacs/gromacs-18/build_test/bin/gmx
Data prefix:  /nethome/pszilard-projects/gromacs/gromacs-18 (source tree)
Working dir:  /nethome/pszilard-projects/gromacs/gromacs-18/build_test/tests/regressiontests-release-2018-352b8a5
Command line:
  gmx mdrun -h


Thanx for Using GROMACS - Have a Nice Day

Unknown Error: box[    0] ( 2.46918e+00  0.00000e+00  0.00000e+00) - ( 2.68268e+00  0.00000e+00  0.00000e+00)
!
Unknown Error: box[    1] ( 0.00000e+00  2.46918e+00  0.00000e+00) - ( 0.00000e+00  2.68268e+00  0.00000e+00)
!
Unknown Error: box[    2] ( 0.00000e+00  0.00000e+00  2.46918e+00) - ( 0.00000e+00  0.00000e+00  2.68268e+00)
!
FAILED. Check checkpot.out (41 errors), checkforce.out (2153 errors) file(s) in nbnxn-free-energy for nbnxn-free-energy
Unknown Error: box[    0] ( 2.46920e+00  0.00000e+00  0.00000e+00) - ( 2.67389e+00  0.00000e+00  0.00000e+00)
!
Unknown Error: box[    1] ( 0.00000e+00  2.46920e+00  0.00000e+00) - ( 0.00000e+00  2.67389e+00  0.00000e+00)
!
Unknown Error: box[    2] ( 0.00000e+00  0.00000e+00  2.46920e+00) - ( 0.00000e+00  0.00000e+00  2.67389e+00)
!
FAILED. Check checkpot.out (40 errors), checkforce.out (2147 errors) file(s) in nbnxn-free-energy-vv for nbnxn-free-energy-vv

Abnormal return value for ' gmx mdrun -ntmpi 1 -npme 0   -ntomp 8  -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-ljpme-geometric for nbnxn-ljpme-geometric
FAILED. Check checkpot.out (13 errors), checkforce.out (37 errors) file(s) in nbnxn-ljpme-LB for nbnxn-ljpme-LB
FAILED. Check checkpot.out (13 errors), checkforce.out (38 errors) file(s) in nbnxn-ljpme-LB-geometric for nbnxn-ljpme-LB-geometric

Abnormal return value for ' gmx mdrun -ntmpi 1 -npme 0   -ntomp 8  -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-force-switch for nbnxn-vdw-force-switch

Abnormal return value for ' gmx mdrun -ntmpi 1 -npme 0   -ntomp 8  -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-potential-switch for nbnxn-vdw-potential-switch

Abnormal return value for ' gmx mdrun -ntmpi 1    -ntomp 8  -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-potential-switch-argon for nbnxn-vdw-potential-switch-argon
FAILED. Check checkpot.out (4 errors) file(s) in nbnxn_rzero for nbnxn_rzero

Abnormal return value for ' gmx mdrun -ntmpi 1 -npme 0   -ntomp 8  -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in octahedron for octahedron

Abnormal return value for ' gmx mdrun -ntmpi 1 -npme 0   -ntomp 8  -notunepme -cpi ./continue -noappend >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in tip4p_continue for tip4p_continue
11 out of 51 complex tests FAILED

```

---

### 评论 #5 — rkothako (2018-06-11T10:45:47Z)

Thanks @pszi1ard, I am able to reproduce this issue.
Actually issue is observed in one of 3 machines only, that too only 1 of 39 tests failed. Remaining 38 tests PASSED.
The following tests FAILED:
         32 - MdrunTests (Failed)

We logged an internal ticket and working on this.

taccuser@ROCM-REL-FIJI:~/Desktop/gromacs/gromacs-2018/build/tests/regressiontests-2018$ perl gmxtest.pl -xml complex -nt 1
                       :-) GROMACS - gmx mdrun, 2018 (-:

                            GROMACS is written by:
     Emile Apol      Rossen Apostolov  Herman J.C. Berendsen    Par Bjelkmar   
 Aldert van Buuren   Rudi van Drunen     Anton Feenstra    Gerrit Groenhof  
 Christoph Junghans   Anca Hamuraru    Vincent Hindriksen Dimitrios Karkoulis
    Peter Kasson        Jiri Kraus      Carsten Kutzner      Per Larsson    
  Justin A. Lemkul    Viveca Lindahl    Magnus Lundborg   Pieter Meulenhoff 
   Erik Marklund      Teemu Murtola       Szilard Pall       Sander Pronk   
   Roland Schulz     Alexey Shvetsov     Michael Shirts     Alfons Sijbers  
   Peter Tieleman    Teemu Virolainen  Christian Wennberg    Maarten Wolf   
                           and the project leaders:
        Mark Abraham, Berk Hess, Erik Lindahl, and David van der Spoel

Copyright (c) 1991-2000, University of Groningen, The Netherlands.
Copyright (c) 2001-2017, The GROMACS development team at
Uppsala University, Stockholm University and
the Royal Institute of Technology, Sweden.
check out http://www.gromacs.org for more information.

GROMACS is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation; either version 2.1
of the License, or (at your option) any later version.

GROMACS:      gmx mdrun, version 2018
Executable:   /home/taccuser/Desktop/gromacs/gromacs-2018/build/bin//gmx
Data prefix:  /home/taccuser/Desktop/gromacs/gromacs-2018 (source tree)
Working dir:  /home/taccuser/Desktop/gromacs/gromacs-2018/build/tests/regressiontests-2018
Command line:
  gmx mdrun -h


Thanx for Using GROMACS - Have a Nice Day


Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-ljpme-geometric for nbnxn-ljpme-geometric
FAILED. Check checkpot.out (13 errors), checkforce.out (37 errors) file(s) in nbnxn-ljpme-LB for nbnxn-ljpme-LB
FAILED. Check checkpot.out (13 errors), checkforce.out (38 errors) file(s) in nbnxn-ljpme-LB-geometric for nbnxn-ljpme-LB-geometric

Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-force-switch for nbnxn-vdw-force-switch

Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-potential-switch for nbnxn-vdw-potential-switch

Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in nbnxn-vdw-potential-switch-argon for nbnxn-vdw-potential-switch-argon
FAILED. Check checkpot.out (4 errors) file(s) in nbnxn_rzero for nbnxn_rzero

Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in octahedron for octahedron

Abnormal return value for ' gmx mdrun -ntmpi 1      -notunepme -cpi ./continue -noappend >mdrun.out 2>&1' was -1
FAILED. Check mdrun.out, md.log file(s) in tip4p_continue for tip4p_continue
9 out of 51 complex tests FAILED

---

### 评论 #6 — pszi1ard (2018-06-11T10:59:20Z)

Thanks for checking, please let me know if I can assist in fixing this issue.

---
