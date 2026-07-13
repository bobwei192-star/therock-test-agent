# [Documentation]: Current device requirements for HIP API calls

- **Issue #:** 3543
- **State:** closed
- **Created:** 2024-08-08T05:26:16Z
- **Updated:** 2024-10-30T15:16:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3543

I would like to know what HIP API functions require the current device to match the one from explicit arguments like streams or graphs.

For example `hipFreeAsync`. Does it require the current device to match the one associated with the stream argument?
There are some obvious functions that would depend on the current device, like `hipMalloc`.
It seems the [HIP documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/) is lacking this information.
I am concerned for pretty much all functions from the API. Does the omission of restrictions in the doc mean it is allowed?