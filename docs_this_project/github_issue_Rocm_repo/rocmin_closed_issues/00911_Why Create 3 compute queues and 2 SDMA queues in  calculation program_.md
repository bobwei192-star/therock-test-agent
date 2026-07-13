# Why Create 3 compute queues and 2 SDMA queues in  calculation program?

- **Issue #:** 911
- **State:** closed
- **Created:** 2019-10-17T07:40:27Z
- **Updated:** 2023-08-07T16:11:11Z
- **Labels:** Question, Informational
- **URL:** https://github.com/ROCm/ROCm/issues/911

1.  I wrote a simple opencl calculation program, input two arrays (a, b), perform "a + b = c" calculation, when it actually run, I found that it will generate 3 calculation queues, but there are not any AQL packages in the second compute queue, because these queues actually correspond to hardware resources. If not necessary, i think it will waste hardware resources. Is there any consideration for this design?

2. The above opencl calculation program will generate two SDMA queues, one copy from the host to the device, and one from the device to the host. From my actual operation, there is no difference between the two queues. Can I use a queue? Because my usage scenario is relatively simple, what are the considerations for using two queues or what application scenarios?

Thank you 