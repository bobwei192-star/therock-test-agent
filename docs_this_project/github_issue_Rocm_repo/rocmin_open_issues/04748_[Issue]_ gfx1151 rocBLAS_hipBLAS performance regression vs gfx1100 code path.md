# [Issue]: gfx1151 rocBLAS/hipBLAS performance regression vs gfx1100 code path

- **Issue #:** 4748
- **State:** open
- **Created:** 2025-05-16T04:40:41Z
- **Updated:** 2026-05-05T21:41:29Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4748

### Problem Description

I've been testing Strix Halo (gfx1100) hardware and rocBLAS performance is unexpectedly bad - see my llama.cpp issue report for some more details: https://github.com/ggml-org/llama.cpp/issues/13565

Running llama.cpp's `test-backend-ops perf -o MUL_MAT` test on gfx1151, there is a 2X performance difference if I use rocBLAS with gfx1151 vs gfx1100 kernels:

```
❯ llama.cpp-hip/build/bin/test-backend-ops perf -o MUL_MAT
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: AMD Radeon Graphics, gfx1151 (0x1151), VMM: no, Wave Size: 32
Testing 2 devices

Backend 1/2: ROCm0
  Device description: AMD Radeon Graphics
  Device memory: 104906 MB (104742 MB free)

  MUL_MAT(type_a=f16,type_b=f32,m=16416,n=1,k=128,bs=[8,1],nr=[4,1],per=[0,2,1,3],v=0):                  744 runs -  9930.30 us/run - 134.48 MFLOP/run -  13.54 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=128,n=1,k=16416,bs=[8,1],nr=[4,1],per=[0,1,2,3],v=1):                 4464 runs -   261.01 us/run - 134.48 MFLOP/run - 515.23 GFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1704 runs -  1090.25 us/run - 117.44 MFLOP/run - 107.72 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1704 runs -   587.86 us/run - 117.44 MFLOP/run - 199.78 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1704 runs -   587.41 us/run - 117.44 MFLOP/run - 199.93 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              22152 runs -    45.68 us/run - 117.44 MFLOP/run -   2.57 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7668 runs -   132.88 us/run - 117.44 MFLOP/run - 883.83 GFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   187.44 us/run - 117.44 MFLOP/run - 626.55 GFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   213.08 us/run - 117.44 MFLOP/run - 551.15 GFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   287.25 us/run - 117.44 MFLOP/run - 408.84 GFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              15336 runs -    68.43 us/run - 117.44 MFLOP/run -   1.72 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7668 runs -   132.25 us/run - 117.44 MFLOP/run - 887.99 GFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              11076 runs -    93.84 us/run - 117.44 MFLOP/run -   1.25 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   203.23 us/run - 117.44 MFLOP/run - 577.86 GFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   229.97 us/run - 117.44 MFLOP/run - 510.67 GFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    7668 runs -   137.48 us/run - 117.44 MFLOP/run - 854.21 GFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10224 runs -   101.01 us/run - 117.44 MFLOP/run -   1.16 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              7668 runs -   143.33 us/run - 117.44 MFLOP/run - 819.37 GFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                   10224 runs -   102.11 us/run - 117.44 MFLOP/run -   1.15 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             22152 runs -    46.19 us/run - 117.44 MFLOP/run -   2.54 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             20448 runs -    49.60 us/run - 117.44 MFLOP/run -   2.37 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    14484 runs -    72.38 us/run - 117.44 MFLOP/run -   1.62 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              7668 runs -   145.98 us/run - 117.44 MFLOP/run - 804.49 GFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    18744 runs -    53.77 us/run - 117.44 MFLOP/run -   2.18 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 426 runs -  2870.91 us/run - 234.88 MFLOP/run -  81.81 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 852 runs -  1820.67 us/run - 234.88 MFLOP/run - 129.01 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                426 runs -  5557.84 us/run - 234.88 MFLOP/run -  42.26 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              17892 runs -    56.39 us/run - 234.88 MFLOP/run -   4.17 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7242 runs -   139.84 us/run - 234.88 MFLOP/run -   1.68 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5538 runs -   190.16 us/run - 234.88 MFLOP/run -   1.24 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4686 runs -   217.05 us/run - 234.88 MFLOP/run -   1.08 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3834 runs -   288.37 us/run - 234.88 MFLOP/run - 814.52 GFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               9798 runs -   104.39 us/run - 234.88 MFLOP/run -   2.25 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6816 runs -   154.67 us/run - 234.88 MFLOP/run -   1.52 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               8094 runs -   126.92 us/run - 234.88 MFLOP/run -   1.85 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   235.60 us/run - 234.88 MFLOP/run - 996.94 GFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4686 runs -   231.78 us/run - 234.88 MFLOP/run -   1.01 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6816 runs -   148.62 us/run - 234.88 MFLOP/run -   1.58 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     9372 runs -   111.46 us/run - 234.88 MFLOP/run -   2.11 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6816 runs -   155.33 us/run - 234.88 MFLOP/run -   1.51 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    8946 runs -   112.38 us/run - 234.88 MFLOP/run -   2.09 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             16188 runs -    62.57 us/run - 234.88 MFLOP/run -   3.75 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             15336 runs -    66.92 us/run - 234.88 MFLOP/run -   3.51 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    11502 runs -    87.31 us/run - 234.88 MFLOP/run -   2.69 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6816 runs -   155.05 us/run - 234.88 MFLOP/run -   1.51 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    14910 runs -    68.88 us/run - 234.88 MFLOP/run -   3.41 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 568 runs -  2907.10 us/run - 352.32 MFLOP/run - 121.19 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 568 runs -  1816.06 us/run - 352.32 MFLOP/run - 194.00 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                284 runs -  5758.26 us/run - 352.32 MFLOP/run -  61.19 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              13064 runs -    78.03 us/run - 352.32 MFLOP/run -   4.51 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   170.39 us/run - 352.32 MFLOP/run -   2.07 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5396 runs -   194.17 us/run - 352.32 MFLOP/run -   1.81 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4828 runs -   218.78 us/run - 352.32 MFLOP/run -   1.61 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3692 runs -   291.35 us/run - 352.32 MFLOP/run -   1.21 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7384 runs -   139.20 us/run - 352.32 MFLOP/run -   2.53 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5680 runs -   179.43 us/run - 352.32 MFLOP/run -   1.96 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6532 runs -   153.43 us/run - 352.32 MFLOP/run -   2.30 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3976 runs -   270.36 us/run - 352.32 MFLOP/run -   1.30 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   238.10 us/run - 352.32 MFLOP/run -   1.48 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6248 runs -   161.69 us/run - 352.32 MFLOP/run -   2.18 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     7952 runs -   126.87 us/run - 352.32 MFLOP/run -   2.78 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5964 runs -   169.90 us/run - 352.32 MFLOP/run -   2.07 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    8236 runs -   123.76 us/run - 352.32 MFLOP/run -   2.85 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             12780 runs -    79.01 us/run - 352.32 MFLOP/run -   4.46 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             11360 runs -    88.43 us/run - 352.32 MFLOP/run -   3.98 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10508 runs -    97.46 us/run - 352.32 MFLOP/run -   3.61 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6248 runs -   164.77 us/run - 352.32 MFLOP/run -   2.14 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    11644 runs -    87.97 us/run - 352.32 MFLOP/run -   4.01 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 426 runs -  2974.42 us/run - 469.76 MFLOP/run - 157.93 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 639 runs -  1827.80 us/run - 469.76 MFLOP/run - 257.01 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                213 runs -  5619.75 us/run - 469.76 MFLOP/run -  83.59 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              11076 runs -    91.72 us/run - 469.76 MFLOP/run -   5.12 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6390 runs -   160.57 us/run - 469.76 MFLOP/run -   2.93 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   198.39 us/run - 469.76 MFLOP/run -   2.37 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4473 runs -   232.96 us/run - 469.76 MFLOP/run -   2.02 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3408 runs -   294.11 us/run - 469.76 MFLOP/run -   1.60 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   172.12 us/run - 469.76 MFLOP/run -   2.73 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4047 runs -   259.36 us/run - 469.76 MFLOP/run -   1.81 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   202.78 us/run - 469.76 MFLOP/run -   2.32 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3408 runs -   293.80 us/run - 469.76 MFLOP/run -   1.60 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4047 runs -   247.30 us/run - 469.76 MFLOP/run -   1.90 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    5751 runs -   174.78 us/run - 469.76 MFLOP/run -   2.69 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     7242 runs -   141.23 us/run - 469.76 MFLOP/run -   3.33 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5325 runs -   189.41 us/run - 469.76 MFLOP/run -   2.48 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    7242 runs -   139.61 us/run - 469.76 MFLOP/run -   3.36 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             10650 runs -    95.28 us/run - 469.76 MFLOP/run -   4.93 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              9585 runs -   104.67 us/run - 469.76 MFLOP/run -   4.49 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     9159 runs -   110.76 us/run - 469.76 MFLOP/run -   4.24 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5751 runs -   175.47 us/run - 469.76 MFLOP/run -   2.68 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10011 runs -   101.16 us/run - 469.76 MFLOP/run -   4.64 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 342 runs -  2971.47 us/run - 587.20 MFLOP/run - 197.61 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 684 runs -  1831.17 us/run - 587.20 MFLOP/run - 320.67 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                342 runs -  5760.27 us/run - 587.20 MFLOP/run - 101.94 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               9234 runs -   109.02 us/run - 587.20 MFLOP/run -   5.39 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6156 runs -   164.27 us/run - 587.20 MFLOP/run -   3.57 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4959 runs -   203.76 us/run - 587.20 MFLOP/run -   2.88 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4446 runs -   226.35 us/run - 587.20 MFLOP/run -   2.59 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3420 runs -   297.54 us/run - 587.20 MFLOP/run -   1.97 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4788 runs -   209.28 us/run - 587.20 MFLOP/run -   2.81 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3762 runs -   268.29 us/run - 587.20 MFLOP/run -   2.19 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4275 runs -   240.57 us/run - 587.20 MFLOP/run -   2.44 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3249 runs -   321.27 us/run - 587.20 MFLOP/run -   1.83 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3933 runs -   257.20 us/run - 587.20 MFLOP/run -   2.28 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    5472 runs -   188.21 us/run - 587.20 MFLOP/run -   3.12 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5814 runs -   175.27 us/run - 587.20 MFLOP/run -   3.35 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              4788 runs -   214.01 us/run - 587.20 MFLOP/run -   2.74 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6669 runs -   151.51 us/run - 587.20 MFLOP/run -   3.88 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              9234 runs -   108.93 us/run - 587.20 MFLOP/run -   5.39 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              7866 runs -   128.44 us/run - 587.20 MFLOP/run -   4.57 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     8037 runs -   126.04 us/run - 587.20 MFLOP/run -   4.66 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5472 runs -   184.44 us/run - 587.20 MFLOP/run -   3.18 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     8892 runs -   113.42 us/run - 587.20 MFLOP/run -   5.18 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 428 runs -  3066.53 us/run - 939.52 MFLOP/run - 306.38 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 642 runs -  1831.45 us/run - 939.52 MFLOP/run - 512.99 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                214 runs -  5735.47 us/run - 939.52 MFLOP/run - 163.81 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6206 runs -   163.79 us/run - 939.52 MFLOP/run -   5.74 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5243 runs -   194.27 us/run - 939.52 MFLOP/run -   4.84 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4494 runs -   225.63 us/run - 939.52 MFLOP/run -   4.16 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4280 runs -   239.53 us/run - 939.52 MFLOP/run -   3.92 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3210 runs -   313.99 us/run - 939.52 MFLOP/run -   2.99 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3103 runs -   323.30 us/run - 939.52 MFLOP/run -   2.91 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2782 runs -   364.95 us/run - 939.52 MFLOP/run -   2.57 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2675 runs -   375.36 us/run - 939.52 MFLOP/run -   2.50 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2247 runs -   462.89 us/run - 939.52 MFLOP/run -   2.03 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3210 runs -   321.86 us/run - 939.52 MFLOP/run -   2.92 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    3959 runs -   258.96 us/run - 939.52 MFLOP/run -   3.63 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5136 runs -   196.14 us/run - 939.52 MFLOP/run -   4.79 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              3959 runs -   258.99 us/run - 939.52 MFLOP/run -   3.63 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    4815 runs -   210.25 us/run - 939.52 MFLOP/run -   4.47 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6420 runs -   157.70 us/run - 939.52 MFLOP/run -   5.96 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5243 runs -   192.33 us/run - 939.52 MFLOP/run -   4.89 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5778 runs -   175.31 us/run - 939.52 MFLOP/run -   5.36 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              4387 runs -   230.05 us/run - 939.52 MFLOP/run -   4.08 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5778 runs -   173.46 us/run - 939.52 MFLOP/run -   5.42 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                94 runs - 10681.19 us/run -  60.13 GFLOP/run -   5.63 TFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                82 runs - 12307.23 us/run -  60.13 GFLOP/run -   4.89 TFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       72 runs - 14260.00 us/run -  60.13 GFLOP/run -   4.22 TFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       76 runs - 13367.83 us/run -  60.13 GFLOP/run -   4.50 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       76 runs - 13244.86 us/run -  60.13 GFLOP/run -   4.54 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       76 runs - 13461.76 us/run -  60.13 GFLOP/run -   4.47 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       78 runs - 12874.67 us/run -  60.13 GFLOP/run -   4.67 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       76 runs - 13325.63 us/run -  60.13 GFLOP/run -   4.51 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       80 runs - 12743.34 us/run -  60.13 GFLOP/run -   4.72 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       78 runs - 13003.81 us/run -  60.13 GFLOP/run -   4.62 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       78 runs - 12892.40 us/run -  60.13 GFLOP/run -   4.66 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       78 runs - 13015.83 us/run -  60.13 GFLOP/run -   4.62 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                       78 runs - 12923.68 us/run -  60.13 GFLOP/run -   4.65 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    78 runs - 12871.58 us/run -  60.13 GFLOP/run -   4.67 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     80 runs - 12796.90 us/run -  60.13 GFLOP/run -   4.70 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      78 runs - 12940.40 us/run -  60.13 GFLOP/run -   4.65 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    78 runs - 12850.27 us/run -  60.13 GFLOP/run -   4.68 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      78 runs - 12875.51 us/run -  60.13 GFLOP/run -   4.67 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      78 runs - 12890.06 us/run -  60.13 GFLOP/run -   4.66 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     78 runs - 12859.42 us/run -  60.13 GFLOP/run -   4.68 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      78 runs - 12839.21 us/run -  60.13 GFLOP/run -   4.68 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     78 runs - 12825.08 us/run -  60.13 GFLOP/run -   4.69 TFLOPS
  Backend ROCm0: OK

...

❯ HSA_OVERRIDE_GFX_VERSION=11.0.0 llama.cpp-hip/build/bin/test-backend-ops perf -o MUL_MAT
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: AMD Radeon Graphics, gfx1100 (0x1100), VMM: no, Wave Size: 32
Testing 2 devices

Backend 1/2: ROCm0
  Device description: AMD Radeon Graphics
  Device memory: 104906 MB (104742 MB free)

  MUL_MAT(type_a=f16,type_b=f32,m=16416,n=1,k=128,bs=[8,1],nr=[4,1],per=[0,2,1,3],v=0):                  744 runs -  1709.42 us/run - 134.48 MFLOP/run -  78.67 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=128,n=1,k=16416,bs=[8,1],nr=[4,1],per=[0,1,2,3],v=1):                 4464 runs -   263.71 us/run - 134.48 MFLOP/run - 509.96 GFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1704 runs -  1091.71 us/run - 117.44 MFLOP/run - 107.57 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1704 runs -   595.41 us/run - 117.44 MFLOP/run - 197.24 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1704 runs -   593.69 us/run - 117.44 MFLOP/run - 197.81 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              23004 runs -    44.95 us/run - 117.44 MFLOP/run -   2.61 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7668 runs -   133.59 us/run - 117.44 MFLOP/run - 879.12 GFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   187.25 us/run - 117.44 MFLOP/run - 627.20 GFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   213.30 us/run - 117.44 MFLOP/run - 550.58 GFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   286.58 us/run - 117.44 MFLOP/run - 409.79 GFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              15336 runs -    68.20 us/run - 117.44 MFLOP/run -   1.72 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7668 runs -   131.58 us/run - 117.44 MFLOP/run - 892.54 GFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              11076 runs -    93.74 us/run - 117.44 MFLOP/run -   1.25 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   203.25 us/run - 117.44 MFLOP/run - 577.82 GFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   229.98 us/run - 117.44 MFLOP/run - 510.65 GFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    7668 runs -   138.47 us/run - 117.44 MFLOP/run - 848.16 GFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10224 runs -   100.82 us/run - 117.44 MFLOP/run -   1.16 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              7668 runs -   143.42 us/run - 117.44 MFLOP/run - 818.88 GFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                   10224 runs -   102.44 us/run - 117.44 MFLOP/run -   1.15 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             22152 runs -    46.86 us/run - 117.44 MFLOP/run -   2.51 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             20448 runs -    50.12 us/run - 117.44 MFLOP/run -   2.34 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    15336 runs -    65.65 us/run - 117.44 MFLOP/run -   1.79 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              7668 runs -   146.33 us/run - 117.44 MFLOP/run - 802.58 GFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=1,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    18744 runs -    53.73 us/run - 117.44 MFLOP/run -   2.19 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 426 runs -  2518.50 us/run - 234.88 MFLOP/run -  93.26 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1278 runs -  1086.29 us/run - 234.88 MFLOP/run - 216.22 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1704 runs -   625.27 us/run - 234.88 MFLOP/run - 375.65 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              17040 runs -    58.76 us/run - 234.88 MFLOP/run -   4.00 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7242 runs -   140.98 us/run - 234.88 MFLOP/run -   1.67 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5538 runs -   189.56 us/run - 234.88 MFLOP/run -   1.24 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4686 runs -   217.53 us/run - 234.88 MFLOP/run -   1.08 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3834 runs -   288.10 us/run - 234.88 MFLOP/run - 815.27 GFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               9798 runs -   104.04 us/run - 234.88 MFLOP/run -   2.26 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6816 runs -   154.91 us/run - 234.88 MFLOP/run -   1.52 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               8520 runs -   119.33 us/run - 234.88 MFLOP/run -   1.97 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   236.05 us/run - 234.88 MFLOP/run - 995.05 GFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4686 runs -   233.15 us/run - 234.88 MFLOP/run -   1.01 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6816 runs -   149.38 us/run - 234.88 MFLOP/run -   1.57 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     9372 runs -   111.49 us/run - 234.88 MFLOP/run -   2.11 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6816 runs -   155.15 us/run - 234.88 MFLOP/run -   1.51 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    8946 runs -   112.20 us/run - 234.88 MFLOP/run -   2.09 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             16188 runs -    62.89 us/run - 234.88 MFLOP/run -   3.73 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             14910 runs -    67.87 us/run - 234.88 MFLOP/run -   3.46 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    11502 runs -    87.19 us/run - 234.88 MFLOP/run -   2.69 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6816 runs -   154.93 us/run - 234.88 MFLOP/run -   1.52 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=2,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    14484 runs -    69.13 us/run - 234.88 MFLOP/run -   3.40 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 568 runs -  2518.92 us/run - 352.32 MFLOP/run - 139.87 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1136 runs -  1086.60 us/run - 352.32 MFLOP/run - 324.24 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1704 runs -   625.67 us/run - 352.32 MFLOP/run - 563.11 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              13064 runs -    78.13 us/run - 352.32 MFLOP/run -   4.51 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   168.09 us/run - 352.32 MFLOP/run -   2.10 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5396 runs -   193.99 us/run - 352.32 MFLOP/run -   1.82 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4828 runs -   219.97 us/run - 352.32 MFLOP/run -   1.60 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3692 runs -   290.77 us/run - 352.32 MFLOP/run -   1.21 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               7384 runs -   139.46 us/run - 352.32 MFLOP/run -   2.53 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5680 runs -   178.67 us/run - 352.32 MFLOP/run -   1.97 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6248 runs -   161.50 us/run - 352.32 MFLOP/run -   2.18 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3976 runs -   270.17 us/run - 352.32 MFLOP/run -   1.30 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4260 runs -   238.56 us/run - 352.32 MFLOP/run -   1.48 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6248 runs -   161.97 us/run - 352.32 MFLOP/run -   2.18 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     7952 runs -   126.21 us/run - 352.32 MFLOP/run -   2.79 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5964 runs -   169.73 us/run - 352.32 MFLOP/run -   2.08 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    8236 runs -   124.08 us/run - 352.32 MFLOP/run -   2.84 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             12780 runs -    79.47 us/run - 352.32 MFLOP/run -   4.43 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             11360 runs -    88.46 us/run - 352.32 MFLOP/run -   3.98 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10224 runs -    98.64 us/run - 352.32 MFLOP/run -   3.57 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6248 runs -   165.08 us/run - 352.32 MFLOP/run -   2.13 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=3,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    11644 runs -    87.79 us/run - 352.32 MFLOP/run -   4.01 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 426 runs -  2529.64 us/run - 469.76 MFLOP/run - 185.70 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1065 runs -  1091.47 us/run - 469.76 MFLOP/run - 430.40 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1704 runs -   625.57 us/run - 469.76 MFLOP/run - 750.94 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              10863 runs -    92.99 us/run - 469.76 MFLOP/run -   5.05 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6390 runs -   157.82 us/run - 469.76 MFLOP/run -   2.98 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   198.61 us/run - 469.76 MFLOP/run -   2.37 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4473 runs -   233.16 us/run - 469.76 MFLOP/run -   2.01 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3408 runs -   293.83 us/run - 469.76 MFLOP/run -   1.60 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5964 runs -   173.85 us/run - 469.76 MFLOP/run -   2.70 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4047 runs -   257.95 us/run - 469.76 MFLOP/run -   1.82 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5112 runs -   201.31 us/run - 469.76 MFLOP/run -   2.33 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3408 runs -   294.87 us/run - 469.76 MFLOP/run -   1.59 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4047 runs -   247.92 us/run - 469.76 MFLOP/run -   1.89 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    5751 runs -   174.97 us/run - 469.76 MFLOP/run -   2.68 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     7242 runs -   140.97 us/run - 469.76 MFLOP/run -   3.33 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5538 runs -   184.97 us/run - 469.76 MFLOP/run -   2.54 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    7455 runs -   137.09 us/run - 469.76 MFLOP/run -   3.43 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):             10650 runs -    95.54 us/run - 469.76 MFLOP/run -   4.92 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              9585 runs -   104.39 us/run - 469.76 MFLOP/run -   4.50 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     9159 runs -   111.28 us/run - 469.76 MFLOP/run -   4.22 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5751 runs -   176.45 us/run - 469.76 MFLOP/run -   2.66 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=4,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    10011 runs -   101.45 us/run - 469.76 MFLOP/run -   4.63 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 513 runs -  2523.74 us/run - 587.20 MFLOP/run - 232.67 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                1026 runs -  1094.21 us/run - 587.20 MFLOP/run - 536.65 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1710 runs -   626.04 us/run - 587.20 MFLOP/run - 937.97 GFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               9234 runs -   109.00 us/run - 587.20 MFLOP/run -   5.39 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5985 runs -   167.47 us/run - 587.20 MFLOP/run -   3.51 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4959 runs -   203.88 us/run - 587.20 MFLOP/run -   2.88 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4446 runs -   225.63 us/run - 587.20 MFLOP/run -   2.60 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3420 runs -   297.15 us/run - 587.20 MFLOP/run -   1.98 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4788 runs -   210.69 us/run - 587.20 MFLOP/run -   2.79 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3762 runs -   268.60 us/run - 587.20 MFLOP/run -   2.19 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4275 runs -   240.11 us/run - 587.20 MFLOP/run -   2.45 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3078 runs -   330.14 us/run - 587.20 MFLOP/run -   1.78 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3933 runs -   256.15 us/run - 587.20 MFLOP/run -   2.29 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    5472 runs -   188.25 us/run - 587.20 MFLOP/run -   3.12 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5643 runs -   180.13 us/run - 587.20 MFLOP/run -   3.26 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              4788 runs -   214.48 us/run - 587.20 MFLOP/run -   2.74 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    6669 runs -   151.03 us/run - 587.20 MFLOP/run -   3.89 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              9234 runs -   109.05 us/run - 587.20 MFLOP/run -   5.38 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              8037 runs -   125.40 us/run - 587.20 MFLOP/run -   4.68 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     8037 runs -   126.59 us/run - 587.20 MFLOP/run -   4.64 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5472 runs -   183.69 us/run - 587.20 MFLOP/run -   3.20 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=5,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     8892 runs -   113.56 us/run - 587.20 MFLOP/run -   5.17 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 428 runs -  2535.39 us/run - 939.52 MFLOP/run - 370.56 GFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                 963 runs -  1103.59 us/run - 939.52 MFLOP/run - 851.34 GFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               1605 runs -   627.17 us/run - 939.52 MFLOP/run -   1.50 TFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               6206 runs -   163.42 us/run - 939.52 MFLOP/run -   5.75 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               5136 runs -   195.31 us/run - 939.52 MFLOP/run -   4.81 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4494 runs -   224.14 us/run - 939.52 MFLOP/run -   4.19 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               4173 runs -   239.65 us/run - 939.52 MFLOP/run -   3.92 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3210 runs -   314.30 us/run - 939.52 MFLOP/run -   2.99 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3103 runs -   322.95 us/run - 939.52 MFLOP/run -   2.91 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2782 runs -   368.17 us/run - 939.52 MFLOP/run -   2.55 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2675 runs -   374.34 us/run - 939.52 MFLOP/run -   2.51 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               2247 runs -   462.55 us/run - 939.52 MFLOP/run -   2.03 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               3103 runs -   322.90 us/run - 939.52 MFLOP/run -   2.91 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    3959 runs -   258.82 us/run - 939.52 MFLOP/run -   3.63 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5136 runs -   196.33 us/run - 939.52 MFLOP/run -   4.79 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              3959 runs -   258.47 us/run - 939.52 MFLOP/run -   3.63 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    4815 runs -   209.54 us/run - 939.52 MFLOP/run -   4.48 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              6313 runs -   158.47 us/run - 939.52 MFLOP/run -   5.93 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              5243 runs -   191.33 us/run - 939.52 MFLOP/run -   4.91 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5778 runs -   176.09 us/run - 939.52 MFLOP/run -   5.34 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):              4387 runs -   230.43 us/run - 939.52 MFLOP/run -   4.08 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=8,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     5778 runs -   174.31 us/run - 939.52 MFLOP/run -   5.39 TFLOPS
  MUL_MAT(type_a=f32,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               120 runs -  8371.19 us/run -  60.13 GFLOP/run -   7.18 TFLOPS
  MUL_MAT(type_a=f16,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):               198 runs -  5068.70 us/run -  60.13 GFLOP/run -  11.86 TFLOPS
  MUL_MAT(type_a=bf16,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      196 runs -  5120.82 us/run -  60.13 GFLOP/run -  11.74 TFLOPS
  MUL_MAT(type_a=q4_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      174 runs -  5765.95 us/run -  60.13 GFLOP/run -  10.43 TFLOPS
  MUL_MAT(type_a=q4_1,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      174 runs -  5789.61 us/run -  60.13 GFLOP/run -  10.39 TFLOPS
  MUL_MAT(type_a=q5_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      172 runs -  5823.52 us/run -  60.13 GFLOP/run -  10.33 TFLOPS
  MUL_MAT(type_a=q5_1,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      172 runs -  5825.00 us/run -  60.13 GFLOP/run -  10.32 TFLOPS
  MUL_MAT(type_a=q8_0,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      170 runs -  5948.59 us/run -  60.13 GFLOP/run -  10.11 TFLOPS
  MUL_MAT(type_a=q2_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      176 runs -  5687.52 us/run -  60.13 GFLOP/run -  10.57 TFLOPS
  MUL_MAT(type_a=q3_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      174 runs -  5753.45 us/run -  60.13 GFLOP/run -  10.45 TFLOPS
  MUL_MAT(type_a=q4_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      174 runs -  5788.98 us/run -  60.13 GFLOP/run -  10.39 TFLOPS
  MUL_MAT(type_a=q5_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      172 runs -  5860.98 us/run -  60.13 GFLOP/run -  10.26 TFLOPS
  MUL_MAT(type_a=q6_K,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                      174 runs -  5808.25 us/run -  60.13 GFLOP/run -  10.35 TFLOPS
  MUL_MAT(type_a=iq2_xxs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                   178 runs -  5671.07 us/run -  60.13 GFLOP/run -  10.60 TFLOPS
  MUL_MAT(type_a=iq2_xs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    178 runs -  5673.10 us/run -  60.13 GFLOP/run -  10.60 TFLOPS
  MUL_MAT(type_a=iq2_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     176 runs -  5685.17 us/run -  60.13 GFLOP/run -  10.58 TFLOPS
  MUL_MAT(type_a=iq3_xxs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                   176 runs -  5721.26 us/run -  60.13 GFLOP/run -  10.51 TFLOPS
  MUL_MAT(type_a=iq1_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     178 runs -  5657.11 us/run -  60.13 GFLOP/run -  10.63 TFLOPS
  MUL_MAT(type_a=iq1_m,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     178 runs -  5671.78 us/run -  60.13 GFLOP/run -  10.60 TFLOPS
  MUL_MAT(type_a=iq4_nl,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    176 runs -  5748.09 us/run -  60.13 GFLOP/run -  10.46 TFLOPS
  MUL_MAT(type_a=iq3_s,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                     176 runs -  5723.26 us/run -  60.13 GFLOP/run -  10.51 TFLOPS
  MUL_MAT(type_a=iq4_xs,type_b=f32,m=4096,n=512,k=14336,bs=[1,1],nr=[1,1],per=[0,1,2,3],v=0):                    176 runs -  5737.44 us/run -  60.13 GFLOP/run -  10.48 TFLOPS
  Backend ROCm0: OK
```

Running mamf-finder w/o hipBLASLt shows similar very poor perf:

```
Tried  3375 shapes => the best outcomes were:
mean:   5.0 TFLOPS @ 4096x9216x1024 (MxNxK)
median: 5.0 TFLOPS @ 12288x3072x1024 (MxNxK)
max:    5.1 TFLOPS @ 11264x3072x1024 (MxNxK)
Elapsed time: 1 day, 10:40:32
```

vs w/ hipBLASLt:

```
Tried  3375 shapes => the best outcomes were:
mean:   35.1 TFLOPS @ 15360x3072x1024 (MxNxK)
median: 35.1 TFLOPS @ 15360x3072x1024 (MxNxK)
max:    36.9 TFLOPS @ 6144x3072x3072 (MxNxK)

Elapsed time: 6:04:34
```

### Operating System

Fedora Linux 43  (Workstation Edition Prerelease)

### CPU

AMD Ryzen AI MAX+ 395 Strix Halo

### GPU

gfx1151

### ROCm Version

6.3.42134-0 , 6.4.43480-9f04e2822

### ROCm Component

rocBLAS

### Steps to Reproduce

Checkout and build llama.cpp: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md#hip

or use my mamf-finder repo: https://github.com/shisa-ai/mamf-finder

Additional Strix Halo testing/notes here: https://llm-tracker.info/_TOORG/Strix-Halo

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_