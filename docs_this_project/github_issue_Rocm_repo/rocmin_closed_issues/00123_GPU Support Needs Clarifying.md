# GPU Support Needs Clarifying

- **Issue #:** 123
- **State:** closed
- **Created:** 2017-05-17T12:48:37Z
- **Updated:** 2017-05-22T19:20:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/123

It's not clear in the docs whether some recent but not cutting-edge cards, such as my R9 390, can use RocM. The docs. make it unclear whether the cards simply don't work, or if they just don't play well with the CPU/one-another.

I'm currently trying to use ROCm and hipCaffe, and anything CL-related, even `clinfo`, seems to freeze early and occupy a full CPU core but negligible RAM until killed. I don't know if this is because my hardware isn't supported, or if I'm missing some key component (e.g., I uninstalled AMDGPU-pro, did I need to reinstall another OpenCL driver, or did that come with the ROCm package?).

Could do with some clarification, and I'd appreciate some quick answers also.