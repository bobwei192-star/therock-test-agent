# [Issue]: Jax example fails with wheel from PyPI, but not with docker container

- **Issue #:** 4311
- **State:** closed
- **Created:** 2025-01-29T10:11:21Z
- **Updated:** 2025-02-12T09:18:17Z
- **Labels:** Under Investigation, ROCm 6.0.0, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/4311

### Problem Description

Upon running the [jax quickstart](https://jax.readthedocs.io/en/latest/quickstart.html) tutorial, I get an XLA-related error in the `batched_apply_matrix()` function (I'm attaching a [minimal example](https://github.com/user-attachments/files/18585609/jax_example.txt) to the post), with the following stacktrace:

```
F0129 11:09:12.654758   18620 stream_executor_util.cc:515] Non-OK-status: kernel->Launch(se::ThreadDim(threads_per_block, 1, 1), se::BlockDim(blocks_per_grid, 1, 1), stream, buffer, host_buffer_bytes, static_cast<int64_t>(buffer.size()))
Status: INTERNAL: Failed to launch ROCm kernel: RepeatBufferKernel with block dimensions: 256x1x1: hipError_t(303)
*** Check failure stack trace: ***
    @     0x14dea86e8d54  absl::lts_20230802::log_internal::LogMessage::SendToLog()
    @     0x14dea86e86f4  absl::lts_20230802::log_internal::LogMessage::Flush()
    @     0x14dea86e91b9  absl::lts_20230802::log_internal::LogMessageFatal::~LogMessageFatal()
    @     0x14dea5055837  xla::gpu::InitializeTypedBuffer<>()
    @     0x14dea50500af  xla::primitive_util::FloatingPointTypeSwitch<>()
    @     0x14dea504e4c3  xla::gpu::InitializeBuffer()
    @     0x14dea504a634  stream_executor::RedzoneAllocator::CreateBuffer()
    @     0x14dea3957536  xla::gpu::RedzoneBuffers::CreateInputs()
    @     0x14dea39571df  xla::gpu::RedzoneBuffers::FromInstruction()
    @     0x14dea3947b6a  xla::gpu::GemmFusionAutotunerImpl::MeasurePerformance()
    @     0x14dea3948ba7  xla::gpu::GemmFusionAutotunerImpl::Profile()
    @     0x14dea39496d9  xla::gpu::GemmFusionAutotunerImpl::Autotune()
    @     0x14dea394c29b  xla::gpu::GemmFusionAutotuner::Run()
    @     0x14dea3962abf  xla::HloPassPipeline::RunHelper()
    @     0x14dea395fd15  xla::HloPassPipeline::RunPassesInternal<>()
    @     0x14dea395f66a  xla::HloPassPipeline::Run()
    @     0x14dea02554ee  xla::gpu::GpuCompiler::OptimizeHloPostLayoutAssignment()
    @     0x14dea0247ab1  xla::gpu::AMDGPUCompiler::OptimizeHloPostLayoutAssignment()
    @     0x14dea0250644  xla::gpu::GpuCompiler::OptimizeHloModule()
    @     0x14dea02591c2  xla::gpu::GpuCompiler::RunHloPasses()
    @     0x14dea0230a6f  xla::Service::BuildExecutable()
    @     0x14dea01a9187  xla::LocalService::CompileExecutables()
    @     0x14dea01a3bf4  xla::LocalClient::Compile()
    @     0x14dea01450fb  xla::PjRtStreamExecutorClient::CompileInternal()
    @     0x14dea01463d0  xla::PjRtStreamExecutorClient::Compile()
    @     0x14dea00b244a  std::__detail::__variant::__gen_vtable_impl<>::__visit_invoke()
    @     0x14dea00a1ddc  pjrt::PJRT_Client_Compile()
    @     0x14e210a0676d  xla::InitializeArgsAndCompile()
    @     0x14e210a06e9e  xla::PjRtCApiClient::Compile()
    @     0x14e218458f38  xla::ifrt::PjRtLoadedExecutable::Create()
    @     0x14e218463010  xla::ifrt::PjRtCompiler::Compile()
    @     0x14e2172e4cff  xla::PyClient::CompileIfrtProgram()
    @     0x14e2172e595b  xla::PyClient::Compile()
    @     0x14e2172eca26  nanobind::detail::func_create<>()::{lambda()#1}::__invoke()
    @     0x14e218430ec8  nanobind::detail::nb_func_vectorcall_complex()
    @     0x14e233ae882c  nanobind::detail::nb_bound_method_vectorcall()
    @     0x14e2345e6d33  PyObject_Vectorcall

[18620] signal 6 (-6): Aborted
in expression starting at none:0
gsignal at /lib64/libc.so.6 (unknown line)
abort at /lib64/libc.so.6 (unknown line)
```

And many more mangled names from `xla_rocm_plugin.so`. The code also fails if I pull an official ROCm container from DockerHub and install jax with `pip3 install jax[rocm]` according to [AMD instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html#using-a-rocm-base-docker-image-and-installing-jax), but runs successfully if I use the rocm-jax container from DockerHub. I believe there is an issue with the PyPI wheels (see below).

### Operating System

Manjaro Linux

### CPU

AMD Ryzen 5 7600 with Radeon Graphics

### GPU

AMD Radeon RX6950XT, MI Instinct 250X

### ROCm Version

ROCm 6.0.0, ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

1. Install ROCm and the jax pip wheel with `pip install jax[rocm]`
2. Realise that the PyPI wheel does not include any `[rocm]` extensions, so manual installation of `jax-rocm60-plugin` and `jax-rocm60-pjrt` is needed.
3. Run the attached MWE based on the jax quick start guide as `LLVM_PATH=/opt/rocm/llvm ROCM_PATH=/opt/rocm python jax_example;py`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

There must be something wrong with the wheels published on PyPI since the `rocm` extensions aren't even provided and the `plugin` and `pjrt` packages need manual installation, both on bare-metal and in the ROCm Docker containers. 