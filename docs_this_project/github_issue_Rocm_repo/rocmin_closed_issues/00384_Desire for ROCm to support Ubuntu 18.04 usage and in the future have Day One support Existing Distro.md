# Desire for ROCm to support Ubuntu 18.04 usage and in the future have Day One support Existing Distros

- **Issue #:** 384
- **State:** closed
- **Created:** 2018-04-10T14:58:02Z
- **Updated:** 2018-08-28T08:36:03Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/384

I am installing a new cluster based on Ubuntu Server and Vega cards and I didn't want to do a `do-release-upgrade` two weeks from now, so I installed Ubuntu Server 18.04 daily on one of the nodes and wanted to give ROCm a spin with minimal sysadmin effort. _(Subiquity is a nightmare, but that is a totally different matter.)_

As was indicated in #361 I installed `linux-image-4.16.1-041601-lowlatency_4.16.1-041601.201804081334_amd64.deb` with matching headers from `http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.16.1/` and tried installing the ROCm packages from the xenial repo provided, as I didn't want to build everything from source. I purposly omitted rocm-dkms, because that was the whole point in trying the out-of-tree kernel. The current rocm-dkms package is a patch for 4.13, and I didn't want to open Pandoras box of building a kernel module for a version it was not meant for. I thought something from the Canonical kernel PPA held less surprises.

`lspci` sees the cards alright, I added my user to the `video` group as well, however when I issue `rocm-smi` it fails to detect any of the 2 cards installed, hence clinfo does not see them as well. amdkfd is loaded as well.

```
lsmod | grep kfd
amdkfd                200704  2
amd_iommu_v2           20480  1 amdkfd
```

I hope this thread can become a step-by-step guide for dummies/low-life sysadmins in getting ROCm to work on a mainline, out-of-tree kernel. How does the dev team spin up a node for testing on a headless Ubuntu 18.04?