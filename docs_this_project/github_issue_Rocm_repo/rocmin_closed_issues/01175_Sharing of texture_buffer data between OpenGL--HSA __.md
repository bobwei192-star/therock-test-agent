# Sharing of texture/buffer data between OpenGL--HSA ??

- **Issue #:** 1175
- **State:** closed
- **Created:** 2020-07-08T13:37:52Z
- **Updated:** 2021-01-28T10:49:42Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/1175

Is there (even low level) functionality to share memory objects between the HSA runtime and OpenGL? e.g. a way to convert a pointer (to an HSA-allocated buffer) into an OpenGL texture?

In other words, if it doesn't _already_ exist, where could one poke around to experiment/build something equivalent to OpenCL's `clCreateFromGLTexture` ?? 