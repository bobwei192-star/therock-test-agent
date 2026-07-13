# Full RX 7xxx Series Product Stack Support When?

- **Issue #:** 2627
- **State:** closed
- **Created:** 2023-11-03T03:36:20Z
- **Updated:** 2024-11-15T16:09:29Z
- **Labels:** Question, Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/2627

### Suggestion Description

Was previewing the ROCm documentation for a few hours and was interested in seeing how I would go about installing this software stack because I would like to do some independent AI stuff.
Checked to see if I had a supported GPU, and I do not.
Unfortunately, my 7900XT (the 2nd highest card in the product stack) is not supported on Linux.
I'm just a bit baffled by this because Windows has support for this card, and forcing me to switch to a platform where most AI development is _not_ happening seems a bit egregious.
Even the humble RX 7600 has full support for the Runtime and HIP SDK on Windows.

![Screenshot_20231102_233131](https://github.com/RadeonOpenCompute/ROCm/assets/43391426/dad8a704-0d8f-493f-bf81-c88506116503)

I guess the part that is more or less confusing to me is that the Radeon Pro WX7800 exists and that is just, to my understanding, essentially a 7900XT chip, but with 32GB of memory over the consumer card's 20GB of memory.

![Screenshot_20231102_233232](https://github.com/RadeonOpenCompute/ROCm/assets/43391426/46750f36-a13c-4e3d-aeab-7109d06a546b)

Also, a card that is listed as unsupported by AMD gets full ROCm support officially? It just seems a bit odd that the Radeon VII consumer card gets ROCm support, but objectively more powerful cards do not.

![Screenshot_20231102_233102](https://github.com/RadeonOpenCompute/ROCm/assets/43391426/1526e061-d951-4229-967e-edf6c1ff70d2)

At it's base, I just want to know if there is a time line for the entire product stack to be supported. 

TL;DR: Is there any plan to expand support to the remaining/entire Radeon consumer product stack on Linux?


### Operating System

_No response_

### GPU

AMD Radeon RX 7900 XT

### ROCm Component

_No response_