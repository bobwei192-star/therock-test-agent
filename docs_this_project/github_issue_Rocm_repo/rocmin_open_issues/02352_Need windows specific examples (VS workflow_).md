# Need windows specific examples (VS workflow?)

- **Issue #:** 2352
- **State:** open
- **Created:** 2023-07-29T13:21:55Z
- **Updated:** 2023-08-24T13:47:28Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2352

With the release of HIP SDK for windows, it would be nice to see some (any) windows specific examples. Everything out there is make/cmake based. Great for existing cmake projects or new projects that can choose to use cmake. But, what about direct integration with existing Visual Studio projects. CUDA Toolkit installation automatically configures visual studio to use the nvcc compiler to build .cu files seamlessly. All the HIP examples out there mix HIP code directly in the .cpp files. Does this mean all compilation has to go through the AMD HIP compiler? How do we get this to play nicely with existing projects developed in Visual Studio?