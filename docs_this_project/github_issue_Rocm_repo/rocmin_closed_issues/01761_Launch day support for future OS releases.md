# Launch day support for future OS releases

- **Issue #:** 1761
- **State:** closed
- **Created:** 2022-06-29T09:07:25Z
- **Updated:** 2023-12-20T13:20:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1761

[ROCm did not plan support for the current Ubuntu 22.04 release.](https://github.com/RadeonOpenCompute/ROCm/issues/1590#issuecomment-1167625353) This is problematic, because by default the software updater of Ubuntu suggests upgrading as soon as the release drops:

![image](https://user-images.githubusercontent.com/11575/176397752-6ef448df-7a68-4fff-b6bc-37ddb027976c.png)

Users who followed the suggestion of upgrading to new LTS releases have found themselves with dysfunctional ROCm installations. See #1590 for the current collection of problems regarding the unavailability of a ROCm release for Ubuntu 22.04. This here issue is requesting to avoid these kinds of problems by ROCm providing launch day support for Ubuntu in particular, but also for all officially supported operating systems. Note that for this purpose there are extensive prerelease phases, at least in the Ubuntu release cycle:

https://discourse.ubuntu.com/t/jammy-jellyfish-release-schedule/23906