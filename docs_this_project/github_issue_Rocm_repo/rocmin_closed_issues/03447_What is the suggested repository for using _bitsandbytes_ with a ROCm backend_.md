# What is the suggested repository for using `bitsandbytes` with a ROCm backend?

- **Issue #:** 3447
- **State:** closed
- **Created:** 2024-07-22T15:31:16Z
- **Updated:** 2024-07-31T20:12:02Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3447

AMD has forked `bitsandbytes` [here](https://github.com/ROCm/bitsandbytes). There was a [bit of confusion](https://github.com/ROCm/ROCm/issues/3132) regarding the installation and usage of this fork and its `rocm_enabled` branch; I have not tested this fork/branch within a week or so, but it seems that it is still unclear if this will work out of the box, or even if this is the correct fork/branch to be using.

The developers at the [upstream branch](https://github.com/bitsandbytes-foundation/bitsandbytes) have recently released the `bitsandbytes/multi-backend-refactor` branch ([link](https://github.com/bitsandbytes-foundation/bitsandbytes/tree/multi-backend-refactor?tab=readme-ov-file)) that is in the testing phase for supporting AMD GPUs and Intel GPUs.

Which of these two, between `ROCm/bitsandbytes` and `bitsandbytes-foundation/bitsandbytes` should be considered the go-to? Is AMD contributing to the upstream branch? If not, why? What has been developed for the ROCm branch that is not in the `multi-backend-refactor` upstream branch?