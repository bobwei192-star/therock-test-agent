# number of valiables  "The number of VGPRs " with 'Kalmar::runtime_exception'

- **Issue #:** 261
- **State:** closed
- **Created:** 2017-11-24T18:25:50Z
- **Updated:** 2018-06-03T15:12:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/261

hello. thank you for reading.

I got the below error during executing the kernel having many local variables.
here is my environment .
Ubuntu 16.04.3
RX 580
32GB RAM
Core i5 4670
ROCm version 1.6, HCC version 1.2

```
terminate called after throwing an instance of 'Kalmar::runtime_exception'
  what():  The number of VGPRs (153) needed by this launch (int, int, int, int, SGInfo*, int, int, int, int
, int, int, int, double*, int, int, int, int, int, int, int, int, int, int, int, int, int, double*, int, int, int, int,
int, int, int, int, int, int, int, int, int, double*, int, int, int, int, int, int, int, int, int, int, int, int, int, d
ouble*, int, int, int, int, int, int, int, int, int, int, int, int, int, double, double, double, double, double, double,
 double*, int, int, int, int, int, int, int, int, int, int, int, int, int, double*, int, int, int, int, int, int, int, i
nt, int, int, int, int, int, double, double, double, double*, int, int, int, int, int, int, int, int, int, int, int, int
, int)) exceeds HW limit due to big work group size (672) workitems!
Aborted (core dumped)
```

I can run the same code on Windows + VS2017 + RX480 with no error.

I suppose the cause of this error is because of too many local variables in the kernel as described in the error massage.
but it's strange that this error occurred despite of the same hardware on both Windows and Linux. 
could you give me any information?

p.s. this number of index variables should be needed to run numerical simulations at least.