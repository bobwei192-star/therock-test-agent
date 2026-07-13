# 7900 XTX Pytorch Issues

- **Issue #:** 1977
- **State:** closed
- **Created:** 2023-03-20T17:37:56Z
- **Updated:** 2024-07-02T19:11:47Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/1977

Like a few others who have posted here I have a 7900 XTX, which isn't officially supported by the ROCm stack. I've looked on line, but I haven't found any information on when to expect support for that device. I'm currently using PyTorch and although I can install torch so it recognizes that there is a GPU, it segfaults whenever a tensor is placed onto the gpu similar to the issue submitted [here](https://github.com/RadeonOpenCompute/ROCm/issues/1973).

I find it disappointing that the 7900 XTX was released 3 months ago and 3 versions of ROCm 5.4.x have been released without support for this.

Is there any reasonably stable way to get pytorch to run on a 7900 XTX? If not, how long are we expected to wait to be able to do so?

