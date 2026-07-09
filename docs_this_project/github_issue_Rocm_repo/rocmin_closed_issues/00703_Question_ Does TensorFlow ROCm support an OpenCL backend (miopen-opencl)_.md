# Question: Does TensorFlow ROCm support an OpenCL backend (miopen-opencl)?

- **Issue #:** 703
- **State:** closed
- **Created:** 2019-02-11T21:19:03Z
- **Updated:** 2019-02-15T16:47:02Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/703

First, apologies if I'm posting these questions to the incorrect place.  Let me know if there's a forum where I should post instead.

My understanding is that the TensorFlow ROCm version requires both miopen-hip and rocm-opencl rocm-opencl-dev, along with miopengemm.  My confusion is that miopen-hip doesn't exploit OpenCL, right? But if that's the case, why do we need to install rocm-opencl?  To exploit particular toolchains as part of the OpenCL packaging?  Are there particular tensorflow routines that use OpenCL directly?  And conversely, since rocm-opencl already is an installation requirement, is miopen-opencl functionally supported with TensorFlow ROCm, rather than miopen-hip?  If miopen is meant to provide an abstraction layer for deep learning, from a functional (and not performance) perspective, why does the backend matter?  Is there more support for hip-ified kernels for tensorflow at this point, and that's the main reason?

Thanks for any clarification you might be able to provide.