# Document building standalone dkms modules (that can be built against multiple kernels and work) from the contents of https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd

- **Issue #:** 1912
- **State:** open
- **Created:** 2023-02-25T20:31:06Z
- **Updated:** 2024-03-17T15:10:01Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1912

Are there any official (I have found some obsolete unofficial, but I guess there should be the ones AMD uses itself somewhere...) docs/recepies/scripts for generating Debian packages from the contents of https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd ? I ask because it seems the official packages targeting obsolete (I mean, considered obsolete by the ones having [SNS syndrome](https://ircbots.debian.net/factoids/factoid.php?key=sns)) versions of Ubuntu are incompatible with vanilla Debian, and so it'd be nice to build own ones.