# report errors for miniFE in HIP

- **Issue #:** 1340
- **State:** closed
- **Created:** 2020-12-17T17:26:21Z
- **Updated:** 2020-12-18T16:38:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/1340

Running the miniFE application in HIP produces the following message. The Residual values from iteration 1 to iteration 6 or 7 are almost the same as those in the CUDA version. Then, the residual values start to increase. 
Thank you for reporting the issue to compiler/hardware developers when you could reproduce it.

https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/miniFE-hip
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/miniFE-cuda (reference)

```
cd miniFE-hip/src
make
./miniFE.x
```

```
MiniFE Mini-App, OpenMP Peer Implementation
Creating OpenMP Thread Pool...
Counted: 8 threads.
Running MiniFE Mini-App...
      creating/filling mesh...0.000146151s, total time: 0.000146151
generating matrix structure...0.00099206s, total time: 0.00113821
         assembling FE data...0.00304604s, total time: 0.00418425
      imposing Dirichlet BC...0.000735044s, total time: 0.00491929
      imposing Dirichlet BC...0.000614882s, total time: 0.00553417
making matrix indices local...0s, total time: 0.00553417
Starting CG solver ...
Initial Residual = 11.0288
Iteration = 1   Residual = 11.0288
Iteration = 2   Residual = 0.637401
Iteration = 3   Residual = 0.313825
Iteration = 4   Residual = 0.192186
Iteration = 5   Residual = 0.134297
Iteration = 6   Residual = 0.132071
Iteration = 7   Residual = 0.131733
Iteration = 8   Residual = 0.0781679
Iteration = 9   Residual = 0.160752
Iteration = 10   Residual = 0.266884
Iteration = 11   Residual = 0.284765
...
Final Resid Norm: 4.19518e+24
verifying solution at ~ (0.5, 0.5, 0.5) ...
max absolute error is 8.68034e+24:
   at position (0.5,0.5,0.5),
   computed solution: 8.68034e+24,  analytic solution: 0.166667
```