# Does ROCm support Tonga?

- **Issue #:** 509
- **State:** closed
- **Created:** 2018-08-22T19:25:03Z
- **Updated:** 2019-03-15T09:33:15Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/509

I'm writing about ROCm in the context of GPU compute languages and putting together tables of GPUs and the degree of support.
It says [here](https://llvm.org/docs/AMDGPUUsage.html#processors) that there is support for Tonga (R9 285, R9 385, R9 380 and some FirePros). But I can't find any mention of this on the ROCm github. Is Tonga actually supported?
As far as the level of support goes, am I right that because the tensorflow port only supports gfx803, 900 and 906(whats that?) anything older than gfx803 lacks instructions and so is only experimental like the support for Hawaii?