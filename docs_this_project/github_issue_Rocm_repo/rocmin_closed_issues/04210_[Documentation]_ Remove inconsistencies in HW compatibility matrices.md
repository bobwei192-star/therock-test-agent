# [Documentation]: Remove inconsistencies in HW compatibility matrices

- **Issue #:** 4210
- **State:** closed
- **Created:** 2024-12-30T20:56:48Z
- **Updated:** 2025-06-26T18:45:41Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4210

### Description of errors

The compatiblity matrices are amongst the first pages that a prospective ROCm user reads. And this first impression is not the best, to say the least. The confusion about ROCm compatibility with certain GPUs is apparent in many Stack Overflow and Reddit posts as well as issues in this bug tracker, cf. #2788, #2972, #3863,...

There are at least 5 different places where HW compatibility is listed in the ROCm documentation and most contradict each other:
1. https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html
2. https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html
3. https://rocm.docs.amd.com/projects/radeon/en/latest/index.html
4. https://rocm.docs.amd.com/projects/radeon/en/latest/docs/compatibility/native_linux/native_linux_compatibility.html
5. https://rocm.docs.amd.com/projects/radeon/en/latest/docs/compatibility/wsl/wsl_compatibility.html

Note that 1. and 2. are from the "core" documentation while 3., 4., 5. are from the "radeon" documentation.

I have the feeling that it may be better to drop 4. and 5. entirely to have a "single source of truth", but you will know better whether this would have unwanted side effects.

Comparing 1. and 2.:
* AMD Instinct hardware is obviously not supported on Windows. It would be nice if this was mentioned on 2. explicitly instead of just implicitly omitting the "AMD Instinct" tab.
* "Radeon Pro" models: 1. lacks a row for W6600 and W5500 while 2. lacks a row for V710. Again, I would prefer explicitly mentioning incompatibility over just omitting the models, so the reader knows that Linux and Windows indeed support different models and this is not just a documentation inconsistency.
* "Radeon" models: 1. lacks rows for 7600, 7700 XT, 7800 XT, and all 6000 models while 2. lacks rows for 7900 GRE and Radeon VII. Note that 5. lists the 7900 GRE as supported under Windows, so at least this model should probably be added to 2. AFAIU from many forum posts and issue comments, 7600, 7700 XT, and 7800 XT work fine under Linux, so they should probably be added to 1., even if they are not "officially" or "fully" supported, maybe with an exclamation mark instead of a checkmark (students and hobbyists will accept some pain if support is "limited").

Regarding 3., 4., 5.:
* The "Radeon" documentation has obviously generally not been updated to ROCm 6.3.x / Ubuntu 24.04 / lower-end Radeon 7000 cards. This is a real pity as support for lower-end Radeon 7000 cards seems to be an FAQ. I couldn't even find these "Radeon" docs on Github, are they hosted somewhere else?
* Page 5. lists "Radeon PRO W7800 48GB" while 4. doesn't; is this a real compatibility difference or just a documentation inconsistency?
* Pages 3. and 5. do not list the 7600/7700 XT/7800 XT that were added to 2. with #2788.

Neither 1., 2., 3., 4., or 5. list the RX 7600 XT (16 GB). @nartmada mentions in #2972 that the 7600 XT is indeed not supported, but it is unclear whether this information is meanwhile outdated. Again, I would prefer to explicitly list this card as "unsupported" if this is the case, to avoid first user confusion. If the 7600 XT is _really_ not supported, I'd consider this to be quite unfortunate, as the 7600 XT would be the ideal GPU for students and hobbyists on a tight budget who want to get in the ROCm game - remember, today's students and hobbyists are tomorrow's professional users!

Finally, I am a little confused about https://rocm.docs.amd.com/projects/radeon/en/latest/docs/compatibility/shared/compatibility.html which looks like an abandoned older compatibility matrix. It seems outdated (despite for "latest" in the URL), points to ROCm 6.0.2/5.7. Maybe check for links to this page and remove it?

Thanks and have a nice end of 2024!


### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_