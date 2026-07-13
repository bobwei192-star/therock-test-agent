# 6800XT OpenCL bad parallel compute performance

- **Issue #:** 1521
- **State:** closed
- **Created:** 2021-07-13T19:52:41Z
- **Updated:** 2021-07-14T04:07:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/1521

I'm transitioning my workloads from old and failing 803gfx WX cards to new 1030gfx cards. I have a test setup with a 6800XT where i encounter an issue where first two workloads i dispatch are treated with somewhat equal priority and are executed quite fast, but every consecutive program that uses OpenCL seems to be disproportionately disadvantaged and executes at what seems like 1:3 rate, until the first workloads finish and next ones can be "promoted".

The 803gfx WX cards behaved differently, no matter how overburdened they divided compute time equally. Typically i was running 10-15 workloads in parallel. Even though the new card has more compute ability the limitation reduces it to nearly sequential ( 2x, but still not parallel 15x ) execution.

Does anything immediately comes to mind? Maybe there's some configuration specific to gaming performance that could be responsible for such behaviour? I noticed in the kernel module available options as shed_jobs, shed_policy, shed_hw_submissions, compute_multipipe but i'd love to avoid diving into a rabbit hole if you can direct me to best possible solution.

Btw, ROCm + 1030gfx, very much welcome, any time, please. ;]