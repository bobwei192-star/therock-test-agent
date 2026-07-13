# Using RX6650XT, rocm5.4.2 reports an error when running stable diffusion

- **Issue #:** 2329
- **State:** closed
- **Created:** 2023-07-22T06:48:07Z
- **Updated:** 2024-02-26T08:16:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/2329

python launch.py --precision full --no-half
Python 3.9.17 (main, Jul  5 2023, 20:41:20) 
[GCC 11.2.0]
Version: v1.4.1
Commit hash: f865d3e11647dfd6c7b2cdf90dde24680e58acd8
Installing requirements
Launching Web UI with arguments: --precision full --no-half
No module 'xformers'. Proceeding without it.
Loading weights [18ed2b6c48] from /home/ubuntu/sd/stable-diffusion-webui/models/Stable-diffusion/xxmix9realistic_v40.safetensors
preload_extensions_git_metadata for 7 extensions took 0.00s
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
Startup time: 2.9s (import torch: 0.9s, import gradio: 0.5s, import ldm: 0.2s, other imports: 0.5s, load scripts: 0.3s, create ui: 0.4s, gradio launch: 0.1s).
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' naive_conv.cpp: HIPRTC_ERROR_COMPILATION (6)
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: naive_conv.cpp
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-8f15a2/input/naive_conv.cpp:39:10: fatal error: 'limits' file not found
#include <limits> // std::numeric_limits
         ^~~~~~~~
1 error generated when compiling for gfx1030.
terminate called after throwing an instance of 'miopen::Exception'
  what():  /long_pathname_so_that_rpms_can_package_the_debug_info/data/driver/MLOpen/src/hipoc/hipoc_program.cpp:304: Code object build failed. Source: naive_conv.cpp
Aborted (core dumped)
