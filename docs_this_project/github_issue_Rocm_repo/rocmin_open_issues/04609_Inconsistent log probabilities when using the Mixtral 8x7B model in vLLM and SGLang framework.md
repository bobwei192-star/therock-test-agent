# Inconsistent log probabilities when using the Mixtral 8x7B model in vLLM and SGLang framework

- **Issue #:** 4609
- **State:** open
- **Created:** 2025-04-11T23:15:06Z
- **Updated:** 2025-04-11T23:15:06Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4609

In ROCm 6.4.0, using a Mixtral 8X7B model with different tensor parallelism (TP) sizes in the vLLM and SGLang framework might result in inconsistent log probabilities. While the output token IDs remain consistent across various TP configurations (1, 2, 4, 8), the log probabilities associated with these tokens might vary. The inconsistency might occur despite using identical quantization settings, prompts, and greedy sampling strategies. The behavior has been observed across different GPUs and is a known limitation in both frameworks, as evidenced by multiple GitHub issues. 

The inconsistency primarily impacts the applications that rely on consistent log probabilities, such as those involving uncertainty estimation or probabilistic decision-making. This known limitation results from how TP distributes computations across multiple GPUs, resulting in slight variations in floating-point arithmetic. Currently, there is no direct resolution as this is a framework-level characteristic rather than a defect.

As a workaround, you can standardize the TP sizes across all the deployments to minimize the inconsistency in the log probabilities. For information on the resolution of this inconsistency in the future, see the [SGlang](https://github.com/sgl-project/sglang) and [vLLM](https://github.com/vllm-project/vllm) GitHub repositories.