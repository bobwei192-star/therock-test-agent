# ROCm OpenCL: kernel hangs with read_imageui() call 

- **Issue #:** 158
- **State:** closed
- **Created:** 2017-07-08T20:14:17Z
- **Updated:** 2017-10-17T01:04:37Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/158

So, having some difficulties getting my kernels to run.

My program flow works like this:

1. map an opencl image, and create map completion event `MAP_COMPLETION_EVENT`
1. also unmap the same image, but the unmap call waits on user event `USER_EVENT`, and creates an unmap completion event `UNMAP_COMPLETION_EVENT`
1. when I receive the `MAP_COMPLETION_EVENT` event, copy data to mapped pointer and then set `USER_EVENT`
1. this will trigger the actual unmap, which will then set `UNMAP_COMPLETION_EVENT`
1. the kernel that uses the above image is enqueued but waits for `UNMAP_COMPLETION_EVENT`

I verified that I get as far as step 4 (the image is indeed unmapped and sends the event) but the kernel never actually runs.

What is best way of trouble shooting this ?


Also, I do enqueue a large number of kernels, but they will not run until they get their `UNMAP_COMPLETION_EVENT` events. 

