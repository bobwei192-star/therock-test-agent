# SPIR & SPIR-V binary support

- **Issue #:** 516
- **State:** closed
- **Created:** 2018-08-28T08:55:01Z
- **Updated:** 2018-09-08T17:51:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/516

### Context
Our group is a happy user of Codeplays ComputeCpp, a fully conformant SYCL 1.2.1 implementation. With Intels rock solid OpenCL infrastructure(s, they too have many to chose from but all are SPIR enabled), it's a shame how AMD seems to have put OpenCL to the side. ([CPU support being discontinued on Windows](https://community.amd.com/message/2875387#2875387), [AMD APP SDK removed from developer.amd.com](https://community.amd.com/message/2847320#2847320), fragmentation of AMDs driver stacks…) When finally AMD and Intel had something to rival CUDA in a portable manner, AMD loses interest in supporting OpenCL, the underlying infrastructure. Luckily Codeplay goes around by adding non-conform additions to ComputeCpp, which is able to emit not just SPIR and SPIR-V, but also PTX and AMDGCN ISA. I understand that they need to do this for Nvidia who sabotages OpenCL to their dying breath, but I was expecting better of AMD.

The Wigner GPU Lab is dedicated to promote SYCL and grow its ecosystem ([BLAS](https://github.com/codeplaysoftware/sycl-blas), [ML](https://github.com/codeplaysoftware/SYCL-ML), [DNN](https://github.com/codeplaysoftware/SYCL-DNN) done by Codeplay, initial [PRNG](https://github.com/Wigner-GPU-Lab/SYCL-PRNG) by us, FFT planned if someone does not beat us to it, SPARSE up for grabs).

I would like to ask for AMD to pay a little more attention to OpenCL in general. I feel it is the best thing to do before GPGPU makes it into ISO C++, and even after that via vendor extensions of OpenCL & SYCL. IMHO the effort put into HCC would have been better put into upstream SYCL support for Clang which would have enabled a far wider audience of developers to write libraries that support AMD HW (NOT JUST GPUs!).

### Sad example
TF 1.8 supporting ROCm enabled GPUs via rocPRIM is nice, but given the limited resources AMD can put into domain library support, I feel the common denominator should be put first. Not putting enough effort into OpenCL/triSYCL/ComputeCpp support for TF is the reason why anyone coming to take a look at the installation instructions for both [Linux](https://www.tensorflow.org/install/install_linux) & [Windows](https://www.tensorflow.org/install/install_windows) are greeted by

> **TensorFlow with GPU support.** TensorFlow programs typically run significantly faster on a GPU than on a CPU. Therefore, if your system has a NVIDIA® GPU meeting the prerequisites shown below and you need to run performance-critical applications, you should ultimately install this version.

The message is simple: `GPU == CUDA` Intel CPUs and IGPs being ubiquitous in both consumer and workstations and having prime-time OpenCL support, it's a miracle how AMD who initially was all in for OpenCL cannot make it to the "front-page" together with Intel. And TF is a Google project! Google is fed up with NVCC! They "single-handedly" added CUDA support for Clang to get rid of closed-source Nvidia components. If only that effort were put into SYCL...

### Summa summarum
Please add support for SPIR & SPIR-V binaries in ROCm (and all other) AMD runtime stacks.