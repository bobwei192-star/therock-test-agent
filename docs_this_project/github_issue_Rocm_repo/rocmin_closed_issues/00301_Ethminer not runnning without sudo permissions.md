# Ethminer not runnning without sudo permissions.

- **Issue #:** 301
- **State:** closed
- **Created:** 2018-01-17T03:16:07Z
- **Updated:** 2018-06-03T15:33:09Z
- **URL:** https://github.com/ROCm/ROCm/issues/301

[OPENCL]:Using platform: AMD Accelerated Parallel Processing
[OPENCL]:Using device: gfx701(OpenCL 1.2 )
DAG  20:04:06.781|ethminer  DAG Generation Failure. Reason: Permission denied
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<dev::ExternalFunctionFailure>'
  what():  std::exception
Aborted (core dumped)

I am running ubuntu 16.04.3, with kernel 4.8.17. When ethminer tries to initialize the gpu, this output occurs, then the program aborts. So far not a great deal, as running ethminer as root with sudo works just fine.
Also great job with this new release of ROCm! Before I got 6mhs on 1.6, but now (At a glance while it runs), I seem to be getting a somewhat better hashrate than amdgpu-pro 17.40! 