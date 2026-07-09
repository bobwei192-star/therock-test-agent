# Darktable opencl results are wrong with rocm (compared to amdgpu-pro and others)

- **Issue #:** 704
- **State:** closed
- **Created:** 2019-02-12T22:15:17Z
- **Updated:** 2023-12-11T23:57:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/704

The Local Contrast module in Darktable uses an OpenCL kernel for applying a local laplacian filter. As far as I know the OpenCL version always resulted in the same output as a cpu based algorithm. This is also the case with the amdgpu-pro drivers which gives very nice results. With Rocm however the results are, to put it mildly, very ugly.

[Bug 12423 @ Darktable](https://redmine.darktable.org/issues/12423)

So far we have localized the issue to somewhere in the [laplacian_assemble kernel](https://github.com/darktable-org/darktable/blob/6ed9ce3cfbd4089c70d14b820f2afc4a431d10ea/data/kernels/locallaplacian.cl#L159). 
Note that this kernel is run a number of times with different sizes of the same image and the results are merged into one final output. This means that any error will quickly propagate to a big artifact on the end result. With rocm the results already look different from amdpro on the smallest image scale (8x6 pixels). This was tested by dumping all the inputs and outputs and comparing the results from both opencl drivers. 

The compiler option used in Darktable is -cl-fast-relaxed-math. Removing it has no effect. I have tested also a couple of different settings but no changes in the results: -cl-denorms-are-zero -cl-no-signed-zeros. 

I have run out of ideas on how to check why the results are different. It looks more like an issue in the compiled binary than in the kernel itself.

Package: rocm-libs version: 2.1.96
Package: rocm-dkms version: 2.1.96
Package: rocm-opencl version: 1.2.0-2019020110

The issue has been reported also with different gpus: AMD RX-560, RX-570, Vega 56.