# RPM packages: Not all header files are symlinked into /opt/rocm/include

- **Issue #:** 1558
- **State:** closed
- **Created:** 2021-08-18T10:16:06Z
- **Updated:** 2024-01-17T23:18:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1558

The following official RPM packages symlink their header files into `/opt/rocm/include/`:

hipblas-0.46.0.40300-52.el7.x86_64
hipcub-2.10.9.40300-52.el7.x86_64
hipfft-1.0.3.40300-52.el7.x86_64
hipsparse-1.10.7.40300-52.el7.x86_64
hsakmt-roct-devel-20210520.3.071986.40300-52.el7.x86_64
hsa-rocr-dev-1.3.0.40300-52.el7.x86_64
miopen-hip-2.12.0.40300-52.el7.x86_64
rccl-2.8.4.40300-52.el7.x86_64
rocalution-1.12.1.40300-52.el7.x86_64
rocblas-2.39.0.40300-52.el7.x86_64
rocfft-1.0.12.40300-52.el7.x86_64
rocm-dbgapi-0.48.0.40300-52.el7.x86_64
rocprim-2.10.9.40300-52.el7.x86_64
rocprofiler-dev-1.0.0.40300-52.el7.x86_64
rocsolver-3.13.0.40300-52.el7.x86_64
rocsparse-1.20.2.40300-52.el7.x86_64
rocthrust-2.10.9.40300-52.el7.x86_64
roctracer-dev-1.0.0.40300-52.el7.x86_64

At least the following don't:

rocm-opencl-devel-2.0.0.40300-52.el7.x86_64
hip-base-4.3.21300.5994.40300-52.el7.x86_64

This makes it hard for us as an HPC provider to provide documentation and environment module files for our HPC users since we have to document multiple paths and cannot simply communicate `/opt/rocm/include/`.