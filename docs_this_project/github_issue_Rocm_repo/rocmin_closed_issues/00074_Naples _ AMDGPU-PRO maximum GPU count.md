# Naples / AMDGPU-PRO maximum GPU count 

- **Issue #:** 74
- **State:** closed
- **Created:** 2017-01-11T12:44:51Z
- **Updated:** 2017-02-22T15:53:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/74

This question is a follow-up of the original question asked at [devgurus](https://community.amd.com/thread/210699). Copy-pasting text there:

With AMD's Naples server dies allegedly sporting 128 PCI-E 3.0 lanes, it occured to out group to revisit the question of maximum number of GPUs one can leverage in such a system, without having to jump through flaming hoops. 8 channel DDR4 sounds like a sound foundation to decent main memory bandwidth. With P2P transfer between the GPUs depending on the use case, one might be content with

- x16 / GPU = 8 GPUs
- x8 / GPU = 16 GPUs
- x4 / GPU = 32 GPUs

Some configurations will require extenders such as [these](https://community.amd.com/external-link.jspa?url=http%3A%2F%2Fmagma.com%2Fproducts%2Fpcie-expansion%2Fexpressbox-3600%2F) Magma extenders. Now I recall that shoving that many GPUs into a single system is no small feat, due to the issue of BIOS wanting to allocate memory for every PCIE device with only 32 bits, several hundred MBs per device. With Naples around the corner and it having such a ridiculous amount of PCIE lanes: 

1. Is there a limit imposed by any part of the AMDGPU-PRO stack on the number of maximum GPUs one can put in a system?
2. Will Naples help in regard to BIOS issues or is that strictly a matter of the motherboard vendor (extended memory and such)?
3. Is there sample code in the ROCm repo to get P2P transfer? (Through ANY of the supported APIs?)

Answers are much appreciated.