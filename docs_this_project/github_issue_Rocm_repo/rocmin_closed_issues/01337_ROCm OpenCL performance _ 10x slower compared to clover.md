# ROCm OpenCL performance > 10x slower compared to clover

- **Issue #:** 1337
- **State:** closed
- **Created:** 2020-12-14T07:04:16Z
- **Updated:** 2021-01-28T06:53:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/1337

Setup:
Amd Threadripper 1950X, 32GB DDR4-3400
2x R9 Nano
Gentoo linux 5.9, no rocm kernel module (due too not supported for 5.9 kernels)
Issue:
benchmarking rocm 3.9 and 3.10 on a system with 2x R9 nano gpus is > 10x slower on ROCm compared to clover (if it runs at all, is highly unstable):
` echo $(date +%%%s.%N%% && ./a.out && date +%%%s.%N%%) >> rocm.txt `
gives (executed 3 times):
```
%1607587105.151533938% Result: 11168608085589920491 Runtime: 0.012519ms %1607587130.296327194%
%1607670831.441274542% Result: 11168608085589920491 Runtime: 0.013072ms %1607670855.944835450% 
%1607670999.627702896% Result: 11168608085589920491 Runtime: 0.012555ms %1607671024.114541166%
```
while on clover, it becomes:
```
%1607525532.830965431% Result: 11168608085589920491 Runtime: 0.000692ms %1607525557.858665546% 
%1607525898.437019510% Result: 11168608085589920491 Runtime: 0.001562ms %1607525923.446692449% 
%1607525926.138453752% Result: 11168608085589920491 Runtime: 0.000700ms %1607525950.744559860%
```
the benchmark was a slightly modified version of opencl-benchmark [here](https://github.com/huytd/opencl-benchmark) on github, modified to ensure its correctness (replaced malloc with calloc, specified opencl version 110) while calculating numbers + increased the load to get more accurate results:
```
kernel void hello(global ulong *val) {                                                                                                                           
size_t i = get_global_id(0);                                                                                                                                   
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] += j;                                                                                                                                                 
}                                                                                                                                                              
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] -= j;                                                                                                                                                 
}                                                                                                                                                            
//    val[i] = 0;                                                                                                                                                
for (ulong j = 0; j < 200000000; j++) {                                                                                                                          
val[i] += (j >> 1) * j;                                                                                                                                      
}                                                                                                                                                            
/*  for (ulong j = 0; j < 10000000000; j++) {                                       // system locks up                                                                               
val[i] += j >> 2;                                                                                                                                            
} */                                                                                                                                                         
}
```
If you need it, let me know