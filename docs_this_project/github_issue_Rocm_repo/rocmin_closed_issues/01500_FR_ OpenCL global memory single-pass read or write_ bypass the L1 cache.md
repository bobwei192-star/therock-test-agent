# FR: OpenCL global memory single-pass read or write: bypass the L1 cache

- **Issue #:** 1500
- **State:** closed
- **Created:** 2021-06-23T12:58:11Z
- **Updated:** 2021-06-24T20:02:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1500

In OpenCL, when accessing global memory, I see two distinct cases: in one case, a large region of data is sequentially read once, or sequentially wrote once. In another case, a smaller block of data is accessed repeteadly.

In the first case (let's call it "single pass sequential"), going through the L1 cache provides no speed benefit AFAIK, but it does pollute the L1 cache with data that is not going to be accessed again. So, it would be useful to have a way to indicate this access pattern for an OpenCL buffer, and the compiler would skip the L1 cache in that case -- hopefully resulting in both faster access and better use of L1 (by avoiding evicting other cached data).

Maybe a mecanism already exist for achieving this?
