# [Feature]: Better support for APUs like 5600G/5700G (Mostly work except GPU offloading of LLMs)

- **Issue #:** 2774
- **State:** closed
- **Created:** 2024-01-03T11:20:37Z
- **Updated:** 2025-01-30T22:36:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/2774

### Suggestion Description

I just picked up a small computer with 5700G+64G RAM+1T drive for $400 to experiment with ROCm and plan to use it as a smart document assistance with some RAG programs. I am excited to see the improvement of ROCm over the past year. I was a bit frustrated and disappointed that APUs with gfx90c isn't officially support but I found some good hack and discussion on #1799 to get most of these works. I am documenting my setup in case they are useful. I really like to see official support in ROCm in these APUs. 

0. Picking the hardware. The main thing is to pick a good mainboard that support adjusting VRAM size in BIOS. 5700G is capable to have up to 16G of RAM dedicated. I am using [ASRock X300TM-ITX](https://www.asrock.com/mb/AMD/X300TM-ITX/index.asp). It's suggested to use DDR4 over 3200 MHz.
1. For the OS, I use Ubuntu 22.04
2. Getting Pytorch to work (mostly works...). Since gfx90c isn't officially support, one has to set the environment `HSA_OVERRIDE_GFX_VERSION` to 9.0.0 for gfx900. This makes most of the Pytorch examples work and takes advantages of the GPU in computation.  
```
$ export HSA_OVERRIDE_GFX_VERSION=9.0.0
```
3. This hack works for tiny LLMs like Phi-2 which can be loaded into memory and compute with GPU. However, it's extremely slow. And when it come sot use mid-size model like Mistral 7B. I am testing this with Huggingface transformers libraries. 
4. Getting [llama.cpp](https://github.com/ggerganov/llama.cpp) to work. This is another popular way to run LLMs. I built it from source with the following instructions. 
```
CMAKE_ARGS="-DLLAMA_HIPBLAS=on -DAMDGPU_TARGETS=gfx900" \
      CC=/opt/rocm/bin/hipcc CXX=/opt/rocm/bin/hipcc \
      pip install llama-cpp-python
```
5. The setup works to some extend. The CPU only inference delivers a 8.8 tokens/second with Mistral 7B. The speed is usable. 
```
$ ./bin/main -m models/dolphin-2.6-mistral-7b-dpo.Q4_K_M.gguf -p "Why is sky blue in 100 words?"
```
However, it hangs while attempting to offload layers of network to GPU. 
```
$ ./bin/main -m models/dolphin-2.6-mistral-7b-dpo.Q4_K_M.gguf -p "Why is sky blue in 100 words?" -ngl 2

...

llm_load_tensors: offloaded 2/33 layers to GPU
.............................................................................................

```

I am still digging into where it goes wrong with the GPU offloading. But with the current GPU speed, this little box is already usable as a small AI Assistant box. I hope to see the GPU working and official APUs support in the ROCm.

### Operating System

Ubuntu 22.04

### GPU

5700G

### ROCm Component

6.0.0 with everything