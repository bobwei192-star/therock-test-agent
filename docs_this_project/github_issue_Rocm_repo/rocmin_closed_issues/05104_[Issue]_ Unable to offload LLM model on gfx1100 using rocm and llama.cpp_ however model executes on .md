# [Issue]: Unable to offload LLM model on gfx1100 using rocm and llama.cpp, however model executes on cpu

- **Issue #:** 5104
- **State:** closed
- **Created:** 2025-07-26T03:45:52Z
- **Updated:** 2025-07-29T20:24:11Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5104

### Problem Description

```
$ echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";

OS:
NAME="elementary OS"
VERSION="8"

$ echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;

CPU: 
model name	: AMD Ryzen 9 7950X3D 16-Core Processor

$ echo "GPU:" && /opt/rocm-6.4.2/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";

GPU:
  Name:                    AMD Ryzen 9 7950X3D 16-Core Processor
  Marketing Name:          AMD Ryzen 9 7950X3D 16-Core Processor
  Name:                    gfx1100                            
  Marketing Name:          Radeon RX 7900 GRE                 
      Name:                    amdgcn-amd-amdhsa--gfx1100         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
  Name:                    gfx900                             
  Marketing Name:          Radeon RX Vega                     
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-   
      Name:                    amdgcn-amd-amdhsa--gfx9-generic:xnack-

```

I'm trying to run llm models using llama.cpp and HIP options on the program. I have tried to run the program with multiple environment variable options (ROCR_VISIBLE_DEVICES and HIP_VISIBLE_DEVICES). However when I isolate the gfx1100 device, then in some cases the llm loads and executes from cpu and system memory (gpu in case of llama-bench and cpu in the case of llama-cli). 

I have opened this issue on llama.cpp as well because I'm not sure where exactly is the problem: https://github.com/ggml-org/llama.cpp/issues/14696

Much thanks for any guidance and insights in the matter.

### Operating System

elementary OS 8 (ubuntu 24.04)

### CPU

AMD Ryzen 9 7950X3D

### GPU

7900 GRE & Vega 64

### ROCm Version

6.4.2

### ROCm Component

HIP

### Steps to Reproduce

```
$ llama-cli --version

ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 2 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
  Device 1: Radeon RX Vega, gfx900:xnack- (0x900), VMM: no, Wave Size: 64
version: 5898 (cbc68be5)
built with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for x86_64-linux-gnu

$ llama-cli -m Qwen3-14B-Q8_0.gguf 
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 2 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
  Device 1: Radeon RX Vega, gfx900:xnack- (0x900), VMM: no, Wave Size: 64
build: 5898 (cbc68be5) with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for x86_64-linux-gnu
main: llama backend init
main: load the model and apply lora adapter, if any
llama_model_load_from_file_impl: using device ROCm0 (Radeon RX 7900 GRE) - 16312 MiB free
llama_model_load_from_file_impl: using device ROCm1 (Radeon RX Vega) - 8160 MiB free
llama_model_loader: loaded meta data with 27 key-value pairs and 443 tensors from Qwen3-14B-Q8_0.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Qwen3 14B
llama_model_loader: - kv   3:                           general.basename str              = Qwen3
llama_model_loader: - kv   4:                         general.size_label str              = 14B
llama_model_loader: - kv   5:                          qwen3.block_count u32              = 40
llama_model_loader: - kv   6:                       qwen3.context_length u32              = 32768
llama_model_loader: - kv   7:                     qwen3.embedding_length u32              = 5120
llama_model_loader: - kv   8:                  qwen3.feed_forward_length u32              = 17408
llama_model_loader: - kv   9:                 qwen3.attention.head_count u32              = 40
llama_model_loader: - kv  10:              qwen3.attention.head_count_kv u32              = 8
llama_model_loader: - kv  11:                       qwen3.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  12:     qwen3.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  13:                 qwen3.attention.key_length u32              = 128
llama_model_loader: - kv  14:               qwen3.attention.value_length u32              = 128
llama_model_loader: - kv  15:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  16:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  17:                      tokenizer.ggml.tokens arr[str,151936]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,151936]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  20:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  22:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  23:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  24:                    tokenizer.chat_template str              = {%- if tools %}\n    {{- '<|im_start|>...
llama_model_loader: - kv  25:               general.quantization_version u32              = 2
llama_model_loader: - kv  26:                          general.file_type u32              = 7
llama_model_loader: - type  f32:  161 tensors
llama_model_loader: - type q8_0:  282 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q8_0
print_info: file size   = 14.61 GiB (8.50 BPW) 
load: special tokens cache size = 26
load: token to piece cache size = 0.9311 MB
print_info: arch             = qwen3
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 5120
print_info: n_layer          = 40
print_info: n_head           = 40
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 5
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 17408
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: model type       = 14B
print_info: model params     = 14.77 B
print_info: general.name     = Qwen3 14B
print_info: vocab type       = BPE
print_info: n_vocab          = 151936
print_info: n_merges         = 151387
print_info: BOS token        = 151643 '<|endoftext|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: PAD token        = 151643 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: FIM PRE token    = 151659 '<|fim_prefix|>'
print_info: FIM SUF token    = 151661 '<|fim_suffix|>'
print_info: FIM MID token    = 151660 '<|fim_middle|>'
print_info: FIM PAD token    = 151662 '<|fim_pad|>'
print_info: FIM REP token    = 151663 '<|repo_name|>'
print_info: FIM SEP token    = 151664 '<|file_sep|>'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: EOG token        = 151662 '<|fim_pad|>'
print_info: EOG token        = 151663 '<|repo_name|>'
print_info: EOG token        = 151664 '<|file_sep|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors: offloading 0 repeating layers to GPU
load_tensors: offloaded 0/41 layers to GPU
load_tensors:   CPU_Mapped model buffer size = 14965.61 MiB
............................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.58 MiB
llama_kv_cache_unified:        CPU KV buffer size =   640.00 MiB
llama_kv_cache_unified: size =  640.00 MiB (  4096 cells,  40 layers,  1 seqs), K (f16):  320.00 MiB, V (f16):  320.00 MiB
llama_kv_cache_unified: LLAMA_SET_ROWS=0, using old ggml_cpy() method for backwards compatibility
llama_context:      ROCm0 compute buffer size =  1094.99 MiB
llama_context:  ROCm_Host compute buffer size =    18.01 MiB
llama_context: graph nodes  = 1606
llama_context: graph splits = 524 (with bs=512), 121 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
ggml_cuda_compute_forward: MUL failed
ROCm error: invalid device function
  current device: 0, in function ggml_cuda_compute_forward at /home/praful/llama.cpp/ggml/src/ggml-cuda/ggml-cuda.cu:2482
  err
/home/praful/llama.cpp/ggml/src/ggml-cuda/ggml-cuda.cu:79: ROCm error
[New LWP 626504]
[New LWP 626503]
[New LWP 626502]
[New LWP 626501]
[New LWP 626500]
[New LWP 626499]
[New LWP 626498]
[New LWP 626497]
[New LWP 626496]
[New LWP 626495]
[New LWP 626494]
[New LWP 626493]
[New LWP 626492]
[New LWP 626491]
[New LWP 626490]
[New LWP 626424]
[New LWP 626293]
[New LWP 626031]
warning: could not find '.gnu_debugaltlink' file for /lib/x86_64-linux-gnu/liblber.so.2
warning: could not find '.gnu_debugaltlink' file for /lib/x86_64-linux-gnu/libbrotlidec.so.1
warning: could not find '.gnu_debugaltlink' file for /lib/x86_64-linux-gnu/libbrotlicommon.so.1
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007009c1b107e3 in __GI___wait4 (pid=626505, stat_loc=0x0, options=0, usage=0x0) at ../sysdeps/unix/sysv/linux/wait4.c:30
warning: 30	../sysdeps/unix/sysv/linux/wait4.c: No such file or directory
#0  0x00007009c1b107e3 in __GI___wait4 (pid=626505, stat_loc=0x0, options=0, usage=0x0) at ../sysdeps/unix/sysv/linux/wait4.c:30
30	in ../sysdeps/unix/sysv/linux/wait4.c
#1  0x00007009c218fde3 in ggml_print_backtrace () from /home/praful/llama.cpp/build/bin/libggml-base.so
#2  0x00007009c218ff8b in ggml_abort () from /home/praful/llama.cpp/build/bin/libggml-base.so
#3  0x00007009be2e7f22 in ggml_cuda_error(char const*, char const*, char const*, int, char const*) () from /home/praful/llama.cpp/build/bin/libggml-hip.so
#4  0x00007009be2eed2a in ggml_backend_cuda_graph_compute(ggml_backend*, ggml_cgraph*) () from /home/praful/llama.cpp/build/bin/libggml-hip.so
#5  0x00007009c21a7b33 in ggml_backend_sched_graph_compute_async () from /home/praful/llama.cpp/build/bin/libggml-base.so
#6  0x00007009c22b75d1 in llama_context::graph_compute(ggml_cgraph*, bool) () from /home/praful/llama.cpp/build/bin/libllama.so
#7  0x00007009c22b7c03 in llama_context::process_ubatch(llama_ubatch const&, llm_graph_type, llama_memory_context_i*, ggml_status&) () from /home/praful/llama.cpp/build/bin/libllama.so
#8  0x00007009c22bb584 in llama_context::decode(llama_batch const&) () from /home/praful/llama.cpp/build/bin/libllama.so
#9  0x00007009c22bc7df in llama_decode () from /home/praful/llama.cpp/build/bin/libllama.so
#10 0x00005ee35b50d42a in common_init_from_params(common_params&) ()
#11 0x00005ee35b4183da in main ()
[Inferior 1 (process 626028) detached]
Aborted (core dumped)


$ llama-bench -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 

ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 2 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
  Device 1: Radeon RX Vega, gfx900:xnack- (0x900), VMM: no, Wave Size: 64
| model                          |       size |     params | backend    | ngl |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
/home/praful/llama.cpp/ggml/src/ggml-cuda/ggml-cuda.cu:79: ROCm error
[New LWP 20492]
[New LWP 19320]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007d701c9107e3 in __GI___wait4 (pid=20819, stat_loc=0x0, options=0, usage=0x0) at ../sysdeps/unix/sysv/linux/wait4.c:30
warning: 30	../sysdeps/unix/sysv/linux/wait4.c: No such file or directory
#0  0x00007d701c9107e3 in __GI___wait4 (pid=20819, stat_loc=0x0, options=0, usage=0x0) at ../sysdeps/unix/sysv/linux/wait4.c:30
30	in ../sysdeps/unix/sysv/linux/wait4.c
#1  0x00007d701cfeade3 in ggml_print_backtrace () from /home/praful/llama.cpp/build/bin/libggml-base.so
#2  0x00007d701cfeaf8b in ggml_abort () from /home/praful/llama.cpp/build/bin/libggml-base.so
#3  0x00007d701a0e7f22 in ggml_cuda_error(char const*, char const*, char const*, int, char const*) () from /home/praful/llama.cpp/build/bin/libggml-hip.so
#4  0x00007d701a0eed2a in ggml_backend_cuda_graph_compute(ggml_backend*, ggml_cgraph*) () from /home/praful/llama.cpp/build/bin/libggml-hip.so
#5  0x00007d701d002b33 in ggml_backend_sched_graph_compute_async () from /home/praful/llama.cpp/build/bin/libggml-base.so
#6  0x00007d701d1125d1 in llama_context::graph_compute(ggml_cgraph*, bool) () from /home/praful/llama.cpp/build/bin/libllama.so
#7  0x00007d701d112c03 in llama_context::process_ubatch(llama_ubatch const&, llm_graph_type, llama_memory_context_i*, ggml_status&) () from /home/praful/llama.cpp/build/bin/libllama.so
#8  0x00007d701d116584 in llama_context::decode(llama_batch const&) () from /home/praful/llama.cpp/build/bin/libllama.so
#9  0x00007d701d1177df in llama_decode () from /home/praful/llama.cpp/build/bin/libllama.so
#10 0x00005f577da92a11 in test_prompt(llama_context*, int, int, int) ()
#11 0x00005f577da8e994 in main ()
[Inferior 1 (process 19317) detached]
Aborted (core dumped)

$ export ROCR_VISIBLE_DEVICES=0

$ llama-bench -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
| model                          |       size |     params | backend    | ngl |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
| qwen3 14B Q8_0                 |  14.61 GiB |    14.77 B | ROCm       |  99 |           pp512 |       1143.73 ± 3.81 |
| qwen3 14B Q8_0                 |  14.61 GiB |    14.77 B | ROCm       |  99 |           tg128 |         32.53 ± 0.12 |

build: cbc68be5 (5898)

$ export ROCR_VISIBLE_DEVICES=1

$ llama-bench -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: Radeon RX Vega, gfx900:xnack- (0x900), VMM: no, Wave Size: 64
| model                          |       size |     params | backend    | ngl |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
main: error: failed to load model '.lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf'

export ROCR_VISIBLE_DEVICES=0

$llama-cli -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 

ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
build: 5898 (cbc68be5) with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for x86_64-linux-gnu
main: llama backend init
main: load the model and apply lora adapter, if any
llama_model_load_from_file_impl: using device ROCm0 (Radeon RX 7900 GRE) - 16312 MiB free
llama_model_loader: loaded meta data with 27 key-value pairs and 443 tensors from .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Qwen3 14B
llama_model_loader: - kv   3:                           general.basename str              = Qwen3
llama_model_loader: - kv   4:                         general.size_label str              = 14B
llama_model_loader: - kv   5:                          qwen3.block_count u32              = 40
llama_model_loader: - kv   6:                       qwen3.context_length u32              = 32768
llama_model_loader: - kv   7:                     qwen3.embedding_length u32              = 5120
llama_model_loader: - kv   8:                  qwen3.feed_forward_length u32              = 17408
llama_model_loader: - kv   9:                 qwen3.attention.head_count u32              = 40
llama_model_loader: - kv  10:              qwen3.attention.head_count_kv u32              = 8
llama_model_loader: - kv  11:                       qwen3.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  12:     qwen3.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  13:                 qwen3.attention.key_length u32              = 128
llama_model_loader: - kv  14:               qwen3.attention.value_length u32              = 128
llama_model_loader: - kv  15:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  16:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  17:                      tokenizer.ggml.tokens arr[str,151936]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,151936]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  20:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  22:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  23:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  24:                    tokenizer.chat_template str              = {%- if tools %}\n    {{- '<|im_start|>...
llama_model_loader: - kv  25:               general.quantization_version u32              = 2
llama_model_loader: - kv  26:                          general.file_type u32              = 7
llama_model_loader: - type  f32:  161 tensors
llama_model_loader: - type q8_0:  282 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q8_0
print_info: file size   = 14.61 GiB (8.50 BPW) 
load: special tokens cache size = 26
load: token to piece cache size = 0.9311 MB
print_info: arch             = qwen3
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 5120
print_info: n_layer          = 40
print_info: n_head           = 40
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 5
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 17408
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: model type       = 14B
print_info: model params     = 14.77 B
print_info: general.name     = Qwen3 14B
print_info: vocab type       = BPE
print_info: n_vocab          = 151936
print_info: n_merges         = 151387
print_info: BOS token        = 151643 '<|endoftext|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: PAD token        = 151643 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: FIM PRE token    = 151659 '<|fim_prefix|>'
print_info: FIM SUF token    = 151661 '<|fim_suffix|>'
print_info: FIM MID token    = 151660 '<|fim_middle|>'
print_info: FIM PAD token    = 151662 '<|fim_pad|>'
print_info: FIM REP token    = 151663 '<|repo_name|>'
print_info: FIM SEP token    = 151664 '<|file_sep|>'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: EOG token        = 151662 '<|fim_pad|>'
print_info: EOG token        = 151663 '<|repo_name|>'
print_info: EOG token        = 151664 '<|file_sep|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors: offloading 0 repeating layers to GPU
load_tensors: offloaded 0/41 layers to GPU
load_tensors:   CPU_Mapped model buffer size = 14965.61 MiB
............................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.58 MiB
llama_kv_cache_unified:        CPU KV buffer size =   640.00 MiB
llama_kv_cache_unified: size =  640.00 MiB (  4096 cells,  40 layers,  1 seqs), K (f16):  320.00 MiB, V (f16):  320.00 MiB
llama_kv_cache_unified: LLAMA_SET_ROWS=0, using old ggml_cpy() method for backwards compatibility
llama_context:      ROCm0 compute buffer size =  1094.99 MiB
llama_context:  ROCm_Host compute buffer size =    18.01 MiB
llama_context: graph nodes  = 1606
llama_context: graph splits = 524 (with bs=512), 121 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 16
main: chat template is available, enabling conversation mode (disable it with -no-cnv)
main: chat template example:
<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant


system_info: n_threads = 16 (n_threads_batch = 16) / 32 | ROCm : NO_VMM = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | AVX512 = 1 | AVX512_VBMI = 1 | AVX512_VNNI = 1 | AVX512_BF16 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 | 

main: interactive mode on.
sampler seed: 813641237
sampler params: 
	repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
	dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 4096
	top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.800
	mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-n-sigma -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist 
generate: n_ctx = 4096, n_batch = 2048, n_predict = -1, n_keep = 0

== Running in interactive mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to the AI.
 - To return control without starting a new line, end your input with '/'.
 - If you want to submit another line, end your input with '\'.
 - Not using system message. To change it, set a different value via -sys PROMPT


> 

$ export HIP_VISIBLE_DEVICES=0

$ llama-bench -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
| model                          |       size |     params | backend    | ngl |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
| qwen3 14B Q8_0                 |  14.61 GiB |    14.77 B | ROCm       |  99 |           pp512 |       1051.76 ± 3.47 |
| qwen3 14B Q8_0                 |  14.61 GiB |    14.77 B | ROCm       |  99 |           tg128 |         29.21 ± 0.01 |

build: cbc68be5 (5898)

llama-cli -m .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf 
ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 ROCm devices:
  Device 0: Radeon RX 7900 GRE, gfx1100 (0x1100), VMM: no, Wave Size: 32
build: 5898 (cbc68be5) with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for x86_64-linux-gnu
main: llama backend init
main: load the model and apply lora adapter, if any
llama_model_load_from_file_impl: using device ROCm0 (Radeon RX 7900 GRE) - 16312 MiB free
llama_model_loader: loaded meta data with 27 key-value pairs and 443 tensors from .lmstudio/models/lmstudio-community/Qwen3-14B-GGUF/Qwen3-14B-Q8_0.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = qwen3
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = Qwen3 14B
llama_model_loader: - kv   3:                           general.basename str              = Qwen3
llama_model_loader: - kv   4:                         general.size_label str              = 14B
llama_model_loader: - kv   5:                          qwen3.block_count u32              = 40
llama_model_loader: - kv   6:                       qwen3.context_length u32              = 32768
llama_model_loader: - kv   7:                     qwen3.embedding_length u32              = 5120
llama_model_loader: - kv   8:                  qwen3.feed_forward_length u32              = 17408
llama_model_loader: - kv   9:                 qwen3.attention.head_count u32              = 40
llama_model_loader: - kv  10:              qwen3.attention.head_count_kv u32              = 8
llama_model_loader: - kv  11:                       qwen3.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  12:     qwen3.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  13:                 qwen3.attention.key_length u32              = 128
llama_model_loader: - kv  14:               qwen3.attention.value_length u32              = 128
llama_model_loader: - kv  15:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  16:                         tokenizer.ggml.pre str              = qwen2
llama_model_loader: - kv  17:                      tokenizer.ggml.tokens arr[str,151936]  = ["!", "\"", "#", "$", "%", "&", "'", ...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,151936]  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:                      tokenizer.ggml.merges arr[str,151387]  = ["Ġ Ġ", "ĠĠ ĠĠ", "i n", "Ġ t",...
llama_model_loader: - kv  20:                tokenizer.ggml.eos_token_id u32              = 151645
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 151643
llama_model_loader: - kv  22:                tokenizer.ggml.bos_token_id u32              = 151643
llama_model_loader: - kv  23:               tokenizer.ggml.add_bos_token bool             = false
llama_model_loader: - kv  24:                    tokenizer.chat_template str              = {%- if tools %}\n    {{- '<|im_start|>...
llama_model_loader: - kv  25:               general.quantization_version u32              = 2
llama_model_loader: - kv  26:                          general.file_type u32              = 7
llama_model_loader: - type  f32:  161 tensors
llama_model_loader: - type q8_0:  282 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q8_0
print_info: file size   = 14.61 GiB (8.50 BPW) 
load: special tokens cache size = 26
load: token to piece cache size = 0.9311 MB
print_info: arch             = qwen3
print_info: vocab_only       = 0
print_info: n_ctx_train      = 32768
print_info: n_embd           = 5120
print_info: n_layer          = 40
print_info: n_head           = 40
print_info: n_head_kv        = 8
print_info: n_rot            = 128
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 128
print_info: n_embd_head_v    = 128
print_info: n_gqa            = 5
print_info: n_embd_k_gqa     = 1024
print_info: n_embd_v_gqa     = 1024
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-06
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 17408
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 32768
print_info: rope_finetuned   = unknown
print_info: model type       = 14B
print_info: model params     = 14.77 B
print_info: general.name     = Qwen3 14B
print_info: vocab type       = BPE
print_info: n_vocab          = 151936
print_info: n_merges         = 151387
print_info: BOS token        = 151643 '<|endoftext|>'
print_info: EOS token        = 151645 '<|im_end|>'
print_info: EOT token        = 151645 '<|im_end|>'
print_info: PAD token        = 151643 '<|endoftext|>'
print_info: LF token         = 198 'Ċ'
print_info: FIM PRE token    = 151659 '<|fim_prefix|>'
print_info: FIM SUF token    = 151661 '<|fim_suffix|>'
print_info: FIM MID token    = 151660 '<|fim_middle|>'
print_info: FIM PAD token    = 151662 '<|fim_pad|>'
print_info: FIM REP token    = 151663 '<|repo_name|>'
print_info: FIM SEP token    = 151664 '<|file_sep|>'
print_info: EOG token        = 151643 '<|endoftext|>'
print_info: EOG token        = 151645 '<|im_end|>'
print_info: EOG token        = 151662 '<|fim_pad|>'
print_info: EOG token        = 151663 '<|repo_name|>'
print_info: EOG token        = 151664 '<|file_sep|>'
print_info: max token length = 256
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors: offloading 0 repeating layers to GPU
load_tensors: offloaded 0/41 layers to GPU
load_tensors:   CPU_Mapped model buffer size = 14965.61 MiB
............................................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = 0
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (4096) < n_ctx_train (32768) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.58 MiB
llama_kv_cache_unified:        CPU KV buffer size =   640.00 MiB
llama_kv_cache_unified: size =  640.00 MiB (  4096 cells,  40 layers,  1 seqs), K (f16):  320.00 MiB, V (f16):  320.00 MiB
llama_kv_cache_unified: LLAMA_SET_ROWS=0, using old ggml_cpy() method for backwards compatibility
llama_context:      ROCm0 compute buffer size =  1094.99 MiB
llama_context:  ROCm_Host compute buffer size =    18.01 MiB
llama_context: graph nodes  = 1606
llama_context: graph splits = 524 (with bs=512), 121 (with bs=1)
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
main: llama threadpool init, n_threads = 16
main: chat template is available, enabling conversation mode (disable it with -no-cnv)
main: chat template example:
<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant


system_info: n_threads = 16 (n_threads_batch = 16) / 32 | ROCm : NO_VMM = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | AVX512 = 1 | AVX512_VBMI = 1 | AVX512_VNNI = 1 | AVX512_BF16 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 | 

main: interactive mode on.
sampler seed: 2541227824
sampler params: 
	repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
	dry_multiplier = 0.000, dry_base = 1.750, dry_allowed_length = 2, dry_penalty_last_n = 4096
	top_k = 40, top_p = 0.950, min_p = 0.050, xtc_probability = 0.000, xtc_threshold = 0.100, typical_p = 1.000, top_n_sigma = -1.000, temp = 0.800
	mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampler chain: logits -> logit-bias -> penalties -> dry -> top-n-sigma -> top-k -> typical -> top-p -> min-p -> xtc -> temp-ext -> dist 
generate: n_ctx = 4096, n_batch = 2048, n_predict = -1, n_keep = 0

== Running in interactive mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to the AI.
 - To return control without starting a new line, end your input with '/'.
 - If you want to submit another line, end your input with '\'.
 - Not using system message. To change it, set a different value via -sys PROMPT


> 

```




### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
$ rocminfo 

ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 9 7950X3D 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 7950X3D 16-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5763                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65427024(0x3e65650) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65427024(0x3e65650) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65427024(0x3e65650) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65427024(0x3e65650) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-fd9ca3bcfec72db2               
  Marketing Name:          Radeon RX 7900 GRE                 
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      6144(0x1800) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   1927                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            80                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 542                                
  SDMA engine uCode::      24                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1100         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0215085621863084               
  Marketing Name:          Radeon RX Vega                     
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      4096(0x1000) KB                    
  Chip ID:                 26751(0x687f)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1630                               
  BDFID:                   6656                               
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 472                                
  SDMA engine uCode::      434                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx9-generic:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             

```

### Additional Information

In the last two instances, while the model loads, it does so on cpu and not the gpu. I don't understand why this is the case. 