# Environment flags with ROCm5.0

- **Issue #:** 1697
- **State:** closed
- **Created:** 2022-03-02T21:16:15Z
- **Updated:** 2022-03-08T07:19:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1697

I've just completed some big tasks, where GPU per task was necessary, now I'd like to run several smaller jobs concurrently on my GPUs. The main problem i'm having right now is memory occupancy with certain workloads hogging 100% regardless of actual use. In that case performance degrades dramatically due to constant memory swapping.

I vaguely remember from old ROCm versions, there were environment flags you can set for certain needs, like limiting max GPU RAM use per process and so on, unfortunately i lost track of those. At the same time i'm sure there are other tweaks possible to be applied in this manner. Is there somewhere a comprehensive or at least mostly complete reference for those?

Regards