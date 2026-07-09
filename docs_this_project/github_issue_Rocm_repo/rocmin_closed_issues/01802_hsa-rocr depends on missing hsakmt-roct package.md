# hsa-rocr depends on missing hsakmt-roct package

- **Issue #:** 1802
- **State:** closed
- **Created:** 2022-08-30T00:42:28Z
- **Updated:** 2023-02-24T21:55:30Z
- **Assignees:** frepaul
- **URL:** https://github.com/ROCm/ROCm/issues/1802

Hi,

The `hsa-rocr` DEB package that ships in the 5.2.3 apt repository lists `hsakmt-roct` as one of its dependencies; however, the latter package doesn't exist in the 5.2.3 repo. (The last repo that contains it is 4.3.1)

This seems a little broken to me. Is the dependency list of `hsa-rocr` wrong, maybe?

Thanks,
Jonathan