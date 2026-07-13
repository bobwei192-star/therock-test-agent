# Missing CRAT workaround

- **Issue #:** 799
- **State:** closed
- **Created:** 2019-05-16T13:35:08Z
- **Updated:** 2023-12-14T20:40:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/799

Is there a workaround possible for APUs where the OEM/ODM has failed to include the correct CRAT table entries? For instance, I have an IBase MI988, which I know has a V1807B. Are the missing CRAT entries specific to the MI988 implementation, or will it be the same across all V1807B devices?

If the OEM can't update the BIOS with a corrected CRAT, can I find the appropriate values and hardcode them into the parsing code? Where would I find those values for this board?

Snipped from #435:

I should also point out that, even with code in ROCK to enable particular APUs, you may have difficulty getting `amdkfd` to come up on such devices. When trying to come up on an APU, the `amdkfd` driver expects your system BIOS to make a CRAT (component resource affinity table) available that describes the layout of the hardware (and the GPU in particular).

We have found that OEMs and ODMs that sold machines built using AMD APUs often did not make this table available in their system BIOS. As such, in the past we found that users were often unable to properly use APUs because of hardware settings outside of our control.

I don't know if this situation has improved with Raven Ridge, but it's something to keep in mind if you try to go off the "supported systems" path. :)

_Originally posted by @jlgreathouse in https://github.com/RadeonOpenCompute/ROCm/issues/435#issuecomment-421821479_