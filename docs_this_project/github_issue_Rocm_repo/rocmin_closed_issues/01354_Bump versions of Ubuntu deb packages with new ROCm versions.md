# Bump versions of Ubuntu deb packages with new ROCm versions

- **Issue #:** 1354
- **State:** closed
- **Created:** 2020-12-30T14:06:50Z
- **Updated:** 2021-01-05T05:53:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1354

The Ubuntu deb packages change while retaining the same version, e.g. for `llvm-amdgpu` for ROCm 4.0, which is unchanged at 12.0dev from ROCm 3.10 (at least).
Now, you officially instruct  to remove ROCm and reinstall but people *do* upgrade and then end with [seemingly missing bits](https://discuss.pytorch.org/t/setup-py-says-use-rocm-off-while-i-set-use-rocm-1/107141/2). These stem from llvm-amdgpu remaining at the 3.10 version when the rest is in 4.0. When one forces reinstallation through  `apt-get install --reinstall llvm-amdgpu`, things work again.
A proper fix would be if you could make sure that the libraries have strictly increasing version numbers from release to release (e.g. by adding `+rocm-4.0` to the version, e.g. `12.0dev+rocm-4.0`would be a very good way and very similar to what Debian does when they want to upgrade through rebuilds).
Thank you!
