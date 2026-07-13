# How soon can Rocm support the Rx 7000 series GPU be expected?

- **Issue #:** 1776
- **State:** closed
- **Created:** 2022-08-02T19:37:25Z
- **Updated:** 2023-02-07T16:29:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1776

At the time of writing, the Rx 7000 series GPU from AMD is not event out yet. So this might seem like a stupid question, but I doubt it is unreasonable, as AMD had been constantly messed up Rocm Navi support schedule in the pass.
- AMD 5000 series came out in 2019 and even the high end like Navi 10 (5700/XT and W5700) still not get officially supported.
- AMD 6000 series came out in 2020, and in May 2021, AMD said [Navi support is coming very soon](https://github.com/RadeonOpenCompute/ROCm/issues/1465#issuecomment-831065316). That _Soon™_ obviously translated to a [2022 release date,](https://docs.amd.com/bundle/ROCm_Release_Notes_v5.0/page/ROCm_Installation_Updates.html) and it ONLY support navi 21. So suck to be using a laptop GPU, or anything like the 6750 XT or below. 
- Funny thing is, while the Rx 6800, 6800XT and 6900 XT are functional, they are technically NOT supported per the AMD Document. 

So yeah, In shorts, AMD has been very on schedule with Rocm release for Navi, and has been awesome with the amount of GPUs they support, and has been really good with the documents as well /s. 

With the impending release of the Rx 7000 series, I, and I believe not a few people, really want to get an estimated release date of Rocm support for the architecture, so that they can consider buying a 7000 series GPU or get a high-end 6000 one for cheap. The need for Rocm on consumer cards are real, and I think, with the already available, but arguably very limited, support for Navi 21, strong support for Navi 31 will probably be possible and can be a big break for AMD Rocm. But it's also very likely that no one from AMD will help, and the support for 7000 series will drag on until at least 2024.

Oh well, at least, "first" to rant about support for 7000 series GPU, I guess.