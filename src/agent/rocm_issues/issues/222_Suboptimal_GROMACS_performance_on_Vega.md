# Suboptimal GROMACS performance on Vega

> **Issue #222**
> **状态**: closed
> **创建时间**: 2017-10-06T01:18:23Z
> **更新时间**: 2018-09-17T21:59:46Z
> **关闭时间**: 2018-08-24T16:49:52Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/222

## 描述

The main kernel (force-only, name-pattern nbnxn_kernel_*_*_F_opencl_gfxXXX) runs up to 22% slower on Vega than on Fiji. Other kernels are a mixed bag. One of the likely contributors is that most kernels end up using quite a bit more registers when compiled for gfx900, e.g.

nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx803 registers: 81, 54
nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx900 registers: 85, 54

nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx803  registers: 84, 68
nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx900 registers 93, 68

For the former "F" kernels, performance across the relevant range of input sizes:
```
Input	Kernel time/iteration (ms)
size	Fiji	Vega	
0.96	0.0727	0.0615	84.59%
1.5	0.1018	0.0799	78.49%
3	0.1165	0.0995	85.41%
6	0.1539	0.169	109.81%
12	0.2582	0.2987	115.69%
24	0.4327	0.5242	121.15%
48	0.7794	0.9545	122.47%
96	1.4489	1.7762	122.59%
192	2.7754	3.3861	122.00%
384	5.6074	6.7722	120.77%
768	11.0613	13.5129	122.16%
1536	21.6894	26.646	122.85%
3072	43.3131	53.2424	122.92%

```


---

## 评论 (30 条)

### 评论 #1 — gstoner (2017-10-13T01:17:13Z)

@pszi1ard  I need to follow up with you on this and tool 

---

### 评论 #2 — gstoner (2017-10-16T23:47:19Z)

@pszi1ard  Hey we loaded a new version of ROCm 1.6.4 at repo.radeon.com can you test it. 

---

### 评论 #3 — pszi1ard (2017-10-17T19:02:01Z)

Some improvements on the register usage side, but still higher than on Fiji:
nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx803 registers: 81, 54
nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx900 registers: **83**, 54

nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx803 registers: 84, 68
nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx900 registers **85**, 68

When it comes to global memory and PCIe bandwidth, not much has changed (if anything Vega D2H bandwidth might be a bit down): both Vega and Fiji global memory bandwidths are unchanged (and low).

---

### 评论 #4 — gstoner (2017-10-17T21:00:51Z)

Some strange going on since you D2H log is showing your clipping 2-3GB/S 

================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 12.762500              0.080235              12.222000               0.083783
    2K                 12.638400              0.162046              12.353000               0.165790
    4K                 12.867100              0.318331              12.702000               0.322469
    8K                 13.326700              0.614706              13.066000               0.626971
   16K                 14.255100              1.149343              13.995000               1.170704
   32K                 15.923300              2.057865              15.444000               2.121730
   64K                 19.457500              3.368161              19.133000               3.425286
  128K                 26.205300              5.001736              25.940000               5.052891
  256K                 39.380900              6.656628              39.010000               6.719918
  512K                 65.807800              7.966958              65.486000               8.006108
    1M                118.311300              8.862856             117.859000               8.896868
    2M                221.706500              9.459136             221.189000               9.481267
    4M                429.735700              9.760194             428.219000               9.794764
    8M                841.345400              9.970469             840.796000               9.976984
   16M               1664.901700             10.077001            1663.707000              10.084237
   32M               3311.324500             10.133236            3309.414000              10.139086
   64M               6608.728400             10.154580            6606.718000              10.157670
  128M              13200.614400             10.167536           13198.751000              10.168972
  256M              26387.797500             10.172712           26382.996000              10.174563
  512M              52766.415200             10.174481           52756.801000              10.176336

---

### 评论 #5 — gstoner (2017-10-17T21:01:30Z)

What is the transfer size of packet for D2H fo gromacs 


---

### 评论 #6 — gstoner (2017-10-17T21:01:55Z)

Here is what i see on EPYC 

p47:~/MI25_Test_Kit$ ./gpu_memory_benchmark -f 0 -t 8 -b

Benchmark Mode Result

|----------|---------------------|-----------------|----------------|--------------------|
|Data Size  |       Avg Time(us)     | Avg BW(GB/s)    |   Min Time(us)  |       Peak BW(GB/s).|
|    1k                18.520800              0.055289              13.656000               0.074985
|   2K                 15.625500              0.131068              13.545000               0.151200
|   4K                 15.588300              0.262761              13.646000               0.300161
|    8K                 16.930800              0.483852              14.177000               0.577837
|    16K                 18.839500              0.869662              14.687000               1.115544
|    32K                 21.969700              1.491509              15.639000               2.095275
|    64K                 22.192900              2.953017              17.984000               3.644128
|   128K                 40.251900              3.256293              22.923000               5.717925
|   256K                 78.562200              3.336770              33.353000               7.859683
  512K                120.168500              4.362940              53.130000               9.868022
    1M                235.025700              4.461538              93.046000              11.269437
    2M                454.138800              4.617866             172.585000              12.151415
    4M                533.782900              7.857696             333.378000              12.581226
    8M               1156.005500              7.256547             652.410000              12.857878
   16M               2025.732600              8.282049            1290.061000              13.004979
   32M               3458.726200              9.701384            2564.433000              13.084542
   64M               5930.747900             11.315413            5113.257000              13.124485
  128M              10497.422000             12.785780           10211.324000              13.144008
  256M              20910.831500             12.837149           20409.853000              13.152248
  512M              41265.533000             13.010153           40801.303000              13.158181

---

### 评论 #7 — pszi1ard (2017-10-17T23:01:35Z)

> What is the transfer size of packet for D2H fo gromacs

In single-GPU runs typically 100Kb-1Mb, one H2D and one D2H per step, when strong-scaling it can be as small as 10-20 Kb and two transfers both ways. In some cases very small (tens to hundreds of bytes) transfers are also required, so latency is also important.

---

### 评论 #8 — pszi1ard (2017-10-17T23:05:50Z)

Here are my performance numbers on an Intel x99 platform with the Vega Frontier:
```
./gpu_memory_benchmark -f 0      -t 2 -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 12.533200              0.081703              12.200000               0.083934
    2K                 12.543700              0.163269              12.313000               0.166328
    4K                 12.780700              0.320483              12.539000               0.326661
    8K                 13.262600              0.617677              13.024000               0.628993
   16K                 14.368300              1.140288              14.110000               1.161162
   32K                 16.036500              2.043339              15.720000               2.084478
   64K                 19.530100              3.355641              19.155000               3.421352
  128K                 26.286800              4.986229              25.974000               5.046277
  256K                 39.308900              6.668821              38.885000               6.741520
  512K                 65.604000              7.991708              65.391000               8.017739
    1M                118.365500              8.858798             117.865000               8.896415
    2M                221.759000              9.456897             221.452000               9.470007
    4M                429.789800              9.758966             428.860000               9.780124
    8M                841.641700              9.966959             841.024000               9.974279
   16M               1665.270400             10.074770            1664.851000              10.077308
   32M               3311.814100             10.131738            3310.745000              10.135009
   64M               6602.370200             10.164359            6601.135000              10.166261
  128M              13184.114800             10.180261           13180.434000              10.183104
  256M              26345.754400             10.188946           26342.481000              10.190212
  512M              52669.658300             10.193172           52666.968000              10.193693

./gpu_memory_benchmark -f 2 -t 0      -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 12.337000              0.083002              12.027000               0.085142
    2K                 12.235000              0.167389              12.080000               0.169536
    4K                 12.363600              0.331295              12.134000               0.337564
    8K                 12.670100              0.646562              12.458000               0.657569
   16K                 13.237200              1.237724              12.998000               1.260502
   32K                 14.621600              2.241068              14.278000               2.294999
   64K                 17.371300              3.772660              17.030000               3.848268
  128K                 22.923900              5.717701              22.556000               5.810959
  256K                 35.128100              7.462516              34.610000               7.574227
  512K                 56.659300              9.253344              55.932000               9.373668
    1M                106.671300              9.829973              99.839000              10.502669
    2M                273.602400              7.664962             203.775000              10.291508
    4M                586.556400              7.150726             485.646000               8.636546
    8M               1139.917300              7.358962             865.675000               9.690251
   16M               1931.029600              8.688223            1565.613000              10.716068
   32M               3443.301600              9.744843            3196.719000              10.496522
   64M               6585.798900             10.189935            6117.735000              10.969560
  128M              12281.606500             10.928353           11666.830000              11.504216
  256M              23276.077600             11.532676           22623.668000              11.865249
  512M              45279.919000             11.856711           44712.184000              12.007262

./gpu_memory_benchmark -f 2 -t 2 -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 12.405800              0.082542              12.078000               0.084782
    2K                 12.284200              0.166718              12.149000               0.168574
    4K                 12.275300              0.333678              12.141000               0.337369
    8K                 12.402000              0.660539              12.296000               0.666233
   16K                 13.049100              1.255566              12.914000               1.268701
   32K                 13.228900              2.477001              12.993000               2.521973
   64K                 13.404400              4.889141              13.257000               4.943502
  128K                 14.127300              9.277923              13.900000               9.429640
  256K                 13.822800             18.964609              13.662000              19.187820
  512K                 15.188300             34.519202              15.049000              34.838727
    1M                 17.568200             59.686024              17.378000              60.339280
    2M                 22.200300             94.465030              21.945000              95.564001
    4M                 31.961900            131.228244              31.570000             132.857270
    8M                 51.848300            161.791380              51.461000             163.009036
   16M                 91.178900            184.003273              90.701000             184.972779
   32M                170.122100            197.237349             169.271000             198.229065
   64M                327.929500            204.644181             326.227000             205.712170
  128M                643.712300            208.505769             641.730000             209.149842
  256M               1276.864600            210.230165            1271.332000             211.145048
  512M               2538.724900            211.472662            2528.659000             212.314477
```

---

### 评论 #9 — pszi1ard (2017-10-17T23:07:27Z)

And this is Fiji, this look really bad:
```
./gpu_memory_benchmark -f 0      -t 1 -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 35.657600              0.028718              22.542000               0.045426
    2K                 35.603100              0.057523              34.473000               0.059409
    4K                 35.926800              0.114010              34.814000               0.117654
    8K                 36.372100              0.225228              35.377000               0.231563
   16K                 37.473200              0.437219              36.339000               0.450865
   32K                 40.007700              0.819042              38.431000               0.852645
   64K                 43.839000              1.494925              42.969000               1.525193
  128K                 52.991400              2.473458              52.170000               2.512402
  256K                 70.927200              3.695959              69.805000               3.755376
  512K                106.170800              4.938156              85.047000               6.164685
    1M                177.890300              5.894509             165.299000               6.343511
    2M                325.171000              6.449382             300.179000               6.986338
    4M                633.247300              6.623485             610.467000               6.870648
    8M               1430.001700              5.866152            1374.239000               6.104184
   16M               2764.360800              6.069112            2637.112000               6.361966
   32M               5872.450400              5.713872            5685.395000               5.901865
   64M              11759.369300              5.706842           11060.123000               6.067642
  128M              22980.787400              5.840432           22864.856000               5.870045
  256M              43573.965500              6.160455           43220.192000               6.210881
  512M              80551.669700              6.664926           79902.397000               6.719084

./gpu_memory_benchmark -f 1 -t 0      -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 37.078600              0.027617              34.758000               0.029461
    2K                 35.635900              0.057470              34.452000               0.059445
    4K                 35.714400              0.114688              34.891000               0.117394
    8K                 36.109200              0.226867              32.356000               0.253183
   16K                 37.521000              0.436662              36.322000               0.451076
   32K                 39.075400              0.838584              37.361000               0.877064
   64K                 43.627000              1.502189              40.944000               1.600625
  128K                 53.008500              2.472660              51.787000               2.530983
  256K                 70.481700              3.719320              69.623000               3.765193
  512K                106.752300              4.911257             105.588000               4.965413
    1M                178.156200              5.885712             156.248000               6.710972
    2M                322.662400              6.499524             315.902000               6.638616
    4M                614.859300              6.821567             610.366000               6.871785
    8M               1388.899000              6.039754            1375.367000               6.099178
   16M               2743.273100              6.115766            2412.498000               6.954292
   32M               5839.240100              5.746370            5562.187000               6.032597
   64M              11759.709300              5.706677           11701.196000               5.735214
  128M              22980.096000              5.840608           22855.037000               5.872567
  256M              43763.902900              6.133718           43497.076000               6.171345
  512M              80734.697900              6.649816           78170.282000               6.867967

./gpu_memory_benchmark -f 1 -t 1 -b
================ Benchmark Mode Result ===================================
Data Size             Avg Time(us)         Avg BW(GB/s)          Min Time(us)         Peak BW(GB/s)
    1k                 36.272400              0.028231              34.043000               0.030080
    2K                 34.982000              0.058544              33.999000               0.060237
    4K                 35.266400              0.116145              33.826000               0.121090
    8K                 36.356800              0.225322              33.925000               0.241474
   16K                 38.547900              0.425030              36.224000               0.452297
   32K                 40.147000              0.816200              37.759000               0.867820
   64K                 43.739900              1.498312              42.822000               1.530428
  128K                 52.625000              2.490679              51.638000               2.538286
  256K                 70.180400              3.735288              69.091000               3.794184
  512K                106.474700              4.924062             105.422000               4.973231
    1M                178.652800              5.869351             176.445000               5.942792
    2M                325.552000              6.441834             299.354000               7.005592
    4M                618.739100              6.778793             565.930000               7.411348
    8M               1386.523600              6.050101            1314.483000               6.381679
   16M               2709.173100              6.192744            2367.479000               7.086532
   32M               5846.720100              5.739018            5663.761000               5.924408
   64M              11680.165400              5.745541           11387.905000               5.892995
  128M              22835.302700              5.877642           22330.984000               6.010381
  256M              44134.967600              6.082149           41747.038000               6.430048
  512M              82943.254200              6.472750           78545.529000               6.835156

---

### 评论 #10 — gstoner (2017-10-17T23:08:59Z)

There was a bug in SDMA firmware for FIJI, they shut it off.  I am chasing down the firmware team 

---

### 评论 #11 — pszi1ard (2017-10-17T23:52:12Z)

As a reference, here's what I get on an identical machine with an NVIDIA card:
```
Transfer Size (Bytes)	NVIDIA	Vega || GB/s
1024			0.31	0.08
2048			0.61	0.17
4096			1.14	0.33
8192			2.10	0.63
16384			3.45	1.16
32768			5.82	2.08
65536			7.63	3.42
131072			9.32	5.05
262144			10.37	6.74
524288			11.11	8.02
1048576			11.45	8.90
2097152			11.56	9.47
4194304			11.71	9.78
16777216		11.84	10.08
33554432		11.86	10.14
```

---

### 评论 #12 — pszi1ard (2017-10-18T15:36:10Z)

> There was a bug in SDMA firmware for FIJI, they shut it off. I am chasing down the firmware team

@gstoner Thanks!

What about the Vega gmem bandwidth, aren't those on the low side too? Regrading the register count, are there any best practices/tricks I should be doing on the kernel level to reduce register use?

---

### 评论 #13 — boxerab (2017-10-18T16:45:18Z)

@pszi1ard the best guide I've found for managing registers is this:

https://gpuopen.com/optimizing-gpu-occupancy-resource-usage-large-thread-groups/

Also, this talk:

https://www.youtube.com/watch?v=Bmy3Tt3Ottc

---

### 评论 #14 — gstoner (2017-10-22T22:29:03Z)

Here something  I need to clean up but, but it how to get the best out of LC compiler 

Here is the short summary of thy ways to get rid of scratch:
In most cases, scratch is not a result of compiler spilling something and thus allocating to scratch. 

Usually, it is a private array or arrays in the kernel itself.

Private arrays and variables have to be allocated to scratch by their semantics. The compiler can optimize them out and allocate to VGPRs under certain conditions.

If all VGPRs are not exhausted but you see scratch access that means it is such a private array.

A private array can be eliminated and allocated to VGPRs if the compiler can always tell which array element is used in every instruction accessing it. For example:
float a[64];
for (int i=0; i < 64; i++)
  use(a[i]);

In this code offset to “a” used inside the loop is dynamic because it is different with every loop iteration. It depends on the value of “I” and such array cannot be eliminated as is.
It can be eliminated if we have:
use(a[0]);
use(a[1]);
use(a[2]);
…
use(a[61]);
use(a[62]);
use(a[63]);

Here all indexes are constant and we can use a register for each of the elements of “a”. Note that if a dynamic index has left anywhere in the code the whole array cannot be optimized out.
The above transformation is basically a full unroll of the loop.

The compiler does its best to do a full unroll of loops where it detects a private array addressing depending on a variable which changes inside the loop. That is not always possible though. There are several main reasons why it cannot:
1.	Loop cannot be unrolled because its bounds are unknown. For example:

for (i = get_local_id(0); i < 256; i++) { … }

Here the lower bound of the loop is not known at the compile time because it is not constant and not uniform. Change the loop like:

for (i = 0; i < 256; i++) {
  if (i < get_local_id(0)) continue;
  …
}

Another example:

for (i = 0; i < min(limit, 256); i++) { … }

Here the upper bound is not constant and the loop cannot be fully unrolled. Transform:

for (i = 0; i < 256; i++) {
  if (i >= limit) continue;
  …
}

In general, do not have any conditionals or dynamic stuff contributing to the loop bounds or increment.

2.	In certain situations use of signed types for loop induction variable is a problem to determine loop bounds because we have to handle signed integer overflow.
Use unsigned indexes where you can.

3.	Even though we are doing our best to unroll loops whose indexes contribute to the private addressing there is always a limit for unroll.
When you have a nest of loops we have to choose which of them to unroll to make it beneficial and not to blow out code size too much.

5 or 6 loops deep nests are common in MIOpen which creates a difficult optimization problem. If you can have less loop nest depth, make it less.

If you cannot try to identify which of loop variables contribute to indexing and help compiler by placing #pragma unroll statement before the loop. A statement without an integer after it shall request full unroll.

But in any case, make sure that loop can be unrolled in principle (it does not have dependencies like described in the 1).

4.	Sometimes we do not honor unroll pragmas even then. That is in case if code size going to increase too much.
Probably in 5 or 6 deep loop nest there is another loop which gets unrolled and then unrolling an outer loop would blow up the code size beyond the threshold:

#pragma unroll
for (i = 0; i < 256; i++) {
  for (j = 0; j < 256; j++) {
    …
  }
  use(a[i]);
}

We would like to unroll the outer loop because a[i] depends on its induction variable. But we might have already unrolled the inner loop due to other considerations and now the size of the fully unrolled outer loop would become too big after unroll.
You can disable unroll of an inner loop (#pragma nounroll) or limit it (like #pragma unroll 4):

#pragma unroll
for (i = 0; i < 256; i++) {
  #pragma nounroll
  for (j = 0; j < 256; j++) {
    …
  }
  use(a[i]);
}
Also avoid taking pointer of private variables.
If you have a private array which you can split into two, split it, it will be easier to analyze.



---

### 评论 #15 — pszi1ard (2017-10-25T10:09:34Z)

@gstoner That a great guide, you should consider adding it to some wiki.

The issues you list however do not apply in our case, I think. We only have a loop nesting of depth 3, the inner two have compile-time constant trip counts and are manually unrolled (though I wonder if the compiler does emit warnings if it ignores a #pragma unroll?). There is a local array, but it's indexed with an unrolled loop's counter. Therefore, it's still not clear to me what else could be done in the source to reduce register use -- which is I suspect too high as it's ~18 more than what nvcc uses for the identically structured CUDA kernels.

---

### 评论 #16 — gstoner (2017-10-25T11:59:48Z)

I working on our new documentation site where we will include this. http://rocm-documentation.readthedocs.io/en/latest/index.html 

---

### 评论 #17 — pszi1ard (2017-12-11T14:08:00Z)

Any update on this? We have switched into beta release gear and when that ends we won't be able to do any tweaks on our side to make the performance competitive on Vega. (Before the end of the year we'll have a final 2018 release BTW).

---

### 评论 #18 — pszi1ard (2018-05-16T17:33:44Z)

Just noticed, I mis-posted my ROCm 1.8 Vega specific feedback; see here: https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-389601236

Briefly: I'd like to get help tracking down the difference between the ROCm and AMDGPU-PRO legacy compiler that seems to lead to major performance penalty on ROCm. Suggestions on how to get action on this are welcome.

---

### 评论 #19 — pszi1ard (2018-05-29T12:08:53Z)

@gstoner Actually, some of our kernels seem to produce incorrect results with ROCm 1.8 on Vega, while AMDGPU-PRO seems fine. Should I file a separate issue? Can please look into this?

---

### 评论 #20 — gstoner (2018-05-29T12:54:48Z)

Yes 18.20 is different compiler then in ROCm

Greg

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Szilárd Páll <notifications@github.com>
Sent: Tuesday, May 29, 2018 7:08:55 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Suboptimal GROMACS performance on Vega (#222)


@gstoner<https://github.com/gstoner> Actually, some of our kernels seem to produce incorrect results with ROCm 1.8 on Vega, while AMDGPU-PRO seems fine. Should I file a separate issue? Can please look into this?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/222#issuecomment-392753090>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudNug-H6tD40aQAOm3CPql2KdHwsks5t3TpXgaJpZM4Pv5fU>.


---

### 评论 #21 — pszi1ard (2018-05-29T12:57:57Z)

> Yes 18.20 is different compiler then in ROCm

I know. As advised, will file a _new github issue_. Under which project, ROCm or ROCm-OpenCL-Runtime?

---

### 评论 #22 — gstoner (2018-05-29T13:10:54Z)

Yes and steps to recreate

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Szilárd Páll <notifications@github.com>
Sent: Tuesday, May 29, 2018 7:57:59 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Suboptimal GROMACS performance on Vega (#222)


Yes 18.20 is different compiler then in ROCm
I know. As advised, will file a new github issue.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/222#issuecomment-392766257>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSjuiU8A61nTbJ4Ey6ZBfGdbsR_4ks5t3UXXgaJpZM4Pv5fU>.


---

### 评论 #23 — gstoner (2018-05-31T14:41:53Z)

Ok we to the bottom of your performance issue on Vega, 

Gfx9 and later: denorms on by default; you can turn them off with -cl-denorms-are-zero
Gfx8 and earlier – denorms are off by default

---

### 评论 #24 — pszi1ard (2018-05-31T18:16:55Z)

@gstoner filed a new issue under ROCm: https://github.com/RadeonOpenCompute/ROCm/issues/427

Thanks for checking the perf regression.  Is this only hardware generation-dependent? 
What about AMDGPU-PRO? Given that with AMDGPU-PRO 17.50 I measured significantly faster kernel times, denorms must be off there too? 

---

### 评论 #25 — gstoner (2018-05-31T18:20:56Z)

They are off on the hsail path




---

### 评论 #26 — pszi1ard (2018-05-31T18:24:09Z)

> They are off on the hsail path

Meaning that -cl-denorms-are-zero is _on_ on <= GFX8 with ROCm and also with the Pro stack?

---

### 评论 #27 — gstoner (2018-05-31T18:25:22Z)

LC had it on by default only for GFX9 GPU.  The other GPU’s (GFX8 and GFX7)  denorm has big penalty So it off by default

HSAIL compiler it is off all gpus


---

### 评论 #28 — gstoner (2018-06-01T01:15:15Z)

Meaning that -cl-denorms-are-zero is on on <= GFX8 with ROCm and also with the Pro stack?

No they are off 

---

### 评论 #29 — pszi1ard (2018-08-24T16:49:39Z)

The performance issue has been solved (also in the last GROMACS release); for the record, the initially posted numbers have changed the following way with 1.8.2 + flushing denorms:


```
size	Fiji	Vega		Fiji*	Vega*
0.96	0.0727	0.0615		0.0648	0.0504
1.5	0.1018	0.0799		0.0909	0.0675
3	0.1165	0.0995		0.1035	0.0757
6	0.1539	0.169		0.1515	0.1059
12	0.2582	0.2987		0.2459	0.1682
24	0.4327	0.5242		0.416	0.2797
48	0.7794	0.9545		0.7576	0.5051
96	1.4489	1.7762		1.398	0.9184
192	2.7754	3.3861		2.6616	1.7504
384	5.6074	6.7722		5.2908	3.5299
768	11.0613	13.5129		10.5129	7.0194
1536	21.6894	26.646		20.6894	14.4534
3072	43.3131	53.2424		41.4343	28.6263
```

---

### 评论 #30 — pszi1ard (2018-09-17T21:59:46Z)

Note that ROCm 1.9 introduced up to 5-6% regression wrt the numbers reported above. Not huge, but enough to note, IMO. I was wondering what is the threshold that flags regressions in your internal benchmarks?

---
