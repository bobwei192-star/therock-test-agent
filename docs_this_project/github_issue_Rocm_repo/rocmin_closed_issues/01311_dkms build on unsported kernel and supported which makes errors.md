# dkms build on unsported kernel and supported which makes errors 

- **Issue #:** 1311
- **State:** closed
- **Created:** 2020-11-30T18:45:16Z
- **Updated:** 2021-05-12T09:44:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/1311

I have to kernels 5.8 which came with the os and 5.4 which I installed manually when I try to download using the official guide it tries to build dkms for both kernels which will cause errors due to incompatibility is there a way that I can make the dkms only build for certain kernel(5.4) not 5.8? I know this can be implemented by adding BUILD_EXCLUSIVE_KERNEL="^(5\.[0-6]\.)" to dkms.conf but I don't know how to do that with apt-get