# Memory access fault by GPU with ROCm 3.3

- **Issue #:** 1103
- **State:** closed
- **Created:** 2020-05-08T13:59:31Z
- **Updated:** 2021-03-04T09:59:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/1103

Mfakto is a trial factoring program: https://github.com/preda/mfakto
Parameters are -d 02 second GPU, --perftest 1 do a performance test once.
to compile go to ./mfakto/src and do 'make'


```
 ./mfakto -d 02 --perftest 1
mfakto 0.15pre6 (64bit build)


Runtime options
  Inifile                   mfakto.ini
  Verbosity                 1
  SieveOnGPU                yes
  MoreClasses               yes
  GPUSievePrimes            81157
  GPUSieveProcessSize       24Ki bits
  GPUSieveSize              96Mi bits
  FlushInterval             0
  WorkFile                  worktodo.txt
  ResultsFile               results.txt
  Checkpoints               enabled
  CheckpointDelay           300s
  Stages                    enabled
  StopAfterFactor           class
  PrintMode                 compact
  V5UserID                  none
  ComputerID                none
  TimeStampInResults        yes
  VectorSize                2
  GPUType                   AUTO
  SmallExp                  no
  UseBinfile                
Select device - Get device info:
WARNING: Unknown GPU name, assuming GCN. Please post the device name "gfx900 (Advanced Micro Devices, Inc.)" to http://www.mersenneforum.org/showthread.php?t=15646 to have it added to mfakto. Set GPUType in mfakto.ini to select a GPU type yourself to avoid this warning.

OpenCL device info
  name                      gfx900 (Advanced Micro Devices, Inc.)
  device (driver) version   OpenCL 2.0  (3098.0 (HSA1.1,LC))
  maximum threads per block 1024
  maximum threads per grid  1073741824
  number of multiprocessors 64 (4096 compute elements)
  clock rate                1630MHz

Automatic parameters
  threads per grid          2097152
  optimizing kernels for    GCN

Compiling kernels.


Perftest

Generate list of the first 1075766 primes: 115.81 ms

1. CPU-Sieve-Init (once per class, 960 times per test, avg. for 1 iterations)
	Init_class(sieveprimes=   5000):     0.40 ms
	Init_class(sieveprimes=  20000):     1.66 ms
	Init_class(sieveprimes=  80000):     7.17 ms
	Init_class(sieveprimes= 200000):    19.00 ms
	Init_class(sieveprimes= 500000):    50.22 ms
	Init_class(sieveprimes=1000000):   104.54 ms

2. CPU-Sieve (output rate M/s)
Sieve size is fixed at compile time, cannot test with variable sizes. Just running 3 fixed tests.

SievePrimes:     254     396     611     945    1460    2257    3487    5389    8328   12871   19890   30738   47503   73411  113449  175323  270944  418716  647083 1000000
SieveSizeLimit
    36 kiB     554.3   519.8   481.7   443.5   407.8   374.3   343.4   313.6   284.1   253.4   220.5   198.2   161.8   125.3   100.1    80.8    65.4    52.5    40.7    31.6
    36 kiB     559.6   520.8   482.0   433.5   397.9   370.7   338.0   313.3   284.3   255.6   224.8   201.5   163.4   125.8   100.7    80.6    65.2    51.6    41.2    31.6
    36 kiB     561.2   521.1   479.8   439.9   404.9   372.1   337.2   311.9   283.3   254.7   224.5   201.4   163.8   127.0   100.8    81.0    65.5    51.8    40.7    31.2

Best SieveSizeLimit for
SievePrimes:     254     396     611     945    1460    2257    3487    5389    8328   12871   19890   30738   47503   73411  113449  175323  270944  418716  647083 1000000
at kiB:           36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36      36
max M/s:       561.2   521.1   482.0   443.5   407.8   374.3   343.4   313.6   284.3   255.6   224.8   201.5   163.8   127.0   100.8    81.0    65.5    52.5    41.2    31.6
Survivors:    36.41%  34.06%  32.06%  30.28%  28.69%  27.27%  26.00%  24.84%  23.78%  22.82%  21.94%  21.12%  20.36%  19.66%  19.01%  18.40%  17.83%  17.29%  16.79%  16.32%
removal rate   980.0  1009.0  1021.5  1021.3  1013.5   998.3   977.4   949.0   911.1   864.6   800.1   753.0   640.7   519.0   429.2   359.1   301.8   251.3   204.2   161.8


3. Memory copy to GPU (blocks of 8388608 bytes)

  Standard copy, standard queue:
      80 MB in   18.8 ms (4469.4 MB/s) (real)

  Standard copy, profiled queue:
      80 MB in   18.5 ms (4544.5 MB/s) (real)
      80 MB in   18.4 ms (4550.3 MB/s) (profiled data)
       8 MB in    1.7 ms (4885.5 MB/s) (profiled data, peak)

  Standard copy, two queues:
      80 MB in   17.2 ms (4884.8 MB/s) (real)

Reinitializing with gpu_sieving enabled.
Select device - Get device info:

OpenCL device info
  name                      gfx900 (Advanced Micro Devices, Inc.)
  device (driver) version   OpenCL 2.0  (3098.0 (HSA1.1,LC))
  maximum threads per block 1024
  maximum threads per grid  1073741824
  number of multiprocessors 64 (4096 compute elements)
  clock rate                1630MHz

Automatic parameters
  threads per grid          2097152
  optimizing kernels for    GCN

Compiling kernels.

4. GPU sieve, 1 iterations each
  GPUSievePrimes (adjusted) 52534
  GPUsieve minimum exponent 646182

 gpusieve_init: 31.683000 ms (CPU work)
 gpusieve_init_exponent: 0.077500 ms (CalcModularInverses)
Memory access fault by GPU node-2 (Agent handle: 0x5655578ffa70) on address 0x7efaf0674000. Reason: Page not present or supervisor privilege.
Aborted

```

I have found that this is an old known issue on ROCm and I would like to know if there is already a fix.
