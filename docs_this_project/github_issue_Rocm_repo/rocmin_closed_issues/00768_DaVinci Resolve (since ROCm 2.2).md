# DaVinci Resolve (since ROCm 2.2)

- **Issue #:** 768
- **State:** closed
- **Created:** 2019-04-14T18:32:38Z
- **Updated:** 2024-08-15T14:14:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/768

ROCm 2.3 appears not to work with DaVinci Resolve, where 2.2 seems to have worked.  Launching with 2.3 seems to cause a segmentation fault.  (Note:  Other software works fine with ROCm 2.3).

See [this](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=56878&start=1400#p498899) post, describing ROCm 2.3 failing for DaVinci Resolve.

See [this](https://youtu.be/nuXsElMbtmI?t=803) for ROCm 2.2 working for DaVinci Resolve with linux-kernel 4.18.  Also note that this user only installed the rocm-utils package (which includes OpenCL), while the documentation recommends installing rocm-dev for only OpenCL.  However, installing rocm-dev in ROCm 2.2 prevented my linux-kernels 4.18 - 5.0 from booting.  I was unaware that this entire package was not needed.

_Unfortunately, the Debian repositories seem to have removed the older versions, making it difficult to revert to 2.2 on Debian-based systems like Ubuntu (where normally one could just select an older version from an installer)._  **(Updated:  See below)**

My requests are:

1. Please update the documentation to remove the step of installing rocm-dev for OpenCL-only installations.
2. _Please provide the older ROCm 2.2 in the debian respositories for users who wish to easily control, revert, and test various versions with various software_  **(Updated:  See below)**
3. Please identify and fix the root cause of DaVinci Resolve failing to work with ROCm 2.3

Note:
For testing, Davinci Resolve can be downloaded for free from their website [here](https://www.blackmagicdesign.com/support/).

It is designed for red-hat-based systems; but it can be easily installed on Debian-based systems (like Ubuntu), using [these instructions](http://www.danieltufvesson.com/makeresolvedeb).