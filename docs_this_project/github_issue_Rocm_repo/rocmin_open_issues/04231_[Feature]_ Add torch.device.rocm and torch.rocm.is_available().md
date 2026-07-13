# [Feature]: Add torch.device.rocm and torch.rocm.is_available()

- **Issue #:** 4231
- **State:** open
- **Created:** 2025-01-06T18:19:20Z
- **Updated:** 2025-02-05T21:39:16Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/4231

Some of us want to write code that exclusively use `rocm` device in pytorch and use explicit torch.rocm.is_available() api to check and run rocm targetting code. Cuda, xpu, xps has same device and check api in torch but torch(rocm edition) just wants to override anything cuda.This is fine for cuda compat but there should also be a parallel explicit api that needs no remapping. Device.rocm comes to mind.

Writing and checking `torch.device.cuda` is real nvidia or fake mapping to internal rocm device makes code impossible to read/decipher and prone to errors.

We added rocm support to [GPTQModel](https://github.com/modelcloud/gptqmodel) and our api accepts `load(..., device="rocm")` not only makes it clean/explicit but necessary as we do internal checks on what kernels are available or not under hipified env. 