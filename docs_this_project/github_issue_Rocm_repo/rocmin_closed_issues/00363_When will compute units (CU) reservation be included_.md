# When will compute units (CU) reservation be included?

- **Issue #:** 363
- **State:** closed
- **Created:** 2018-03-15T12:58:36Z
- **Updated:** 2020-09-10T16:24:27Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/363

I noticed this great technique compute units reservation in Polaris whitepaper, which says programmers can partition the device via API extensions.  But I don't think it's included in the open-source software stack.

This technique is great for real-time systems.  Also, currently not implemented clCreateSubDevices in OpenCL runtime can be enabled with this technique.

Will this be included in ROCm?  When?

Thanks,
Ming