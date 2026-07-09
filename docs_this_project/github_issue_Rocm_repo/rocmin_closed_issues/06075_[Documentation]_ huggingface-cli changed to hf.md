# [Documentation]: huggingface-cli changed to hf

- **Issue #:** 6075
- **State:** closed
- **Created:** 2026-03-28T19:39:07Z
- **Updated:** 2026-04-21T15:31:59Z
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6075

### Description of errors

The documentation uses `huggingface-cli` in multiple places in examples.  

The CLI changed to `hf` in 1.0, re: [Say hello to `hf`: a faster, friendlier Hugging Face CLI ](https://huggingface.co/blog/hf-cli).  

The documentation should be changed to use `hf` in examples, I specifically hit the issue with [Benchmark Llama 3.3/3.1 FP4 inference with vLLM](https://rocm.docs.amd.com/en/docs-7.0-docker/benchmark-docker/inference-vllm-llama-3.1-405b-fp4.html), but a search of the documentation finds numerous other examples ([21 files under docs](https://github.com/search?q=repo%3AROCm%2FROCm+huggingface-cli&type=code)). 

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_