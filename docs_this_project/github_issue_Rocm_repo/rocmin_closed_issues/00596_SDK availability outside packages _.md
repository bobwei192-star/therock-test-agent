# SDK availability outside packages ?

- **Issue #:** 596
- **State:** closed
- **Created:** 2018-10-31T18:59:53Z
- **Updated:** 2018-11-06T17:43:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/596

Reading the documentation, I could see that there is support for several distributions through their package managers, which is a **good** thing. However, it seems to me that what is covered at https://github.com/RadeonOpenCompute/ROCm#ubuntu-support---installing-from-a-debian-repository is only the installation of the whole software stack to run ROCm compatible tools.

Let's say I just want to have the needed bits to be able to make builds of TensorFlow that are ROCm-enabled. For NVIDIA's CUDA and CompteCpp's SDK, I just have to download and extract a tarball that contains the headers and sometimes some tooling required for building.

Thanks for any help!