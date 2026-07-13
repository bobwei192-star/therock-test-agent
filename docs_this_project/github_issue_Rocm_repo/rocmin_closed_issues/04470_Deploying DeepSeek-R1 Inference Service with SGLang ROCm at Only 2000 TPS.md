# Deploying DeepSeek-R1 Inference Service with SGLang ROCm at Only 2000 TPS

- **Issue #:** 4470
- **State:** closed
- **Created:** 2025-03-10T12:00:15Z
- **Updated:** 2025-03-16T02:35:54Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4470

I followed the [operational procedures](https://rocm.blogs.amd.com/artificial-intelligence/DeepSeekR1_Perf/README.html) outlined in the article and ran tests on the MI325 x8, hoping to replicate the same results. Unfortunately, with a BatchSize=160, the TPS only reached around 2000. Do you have any suggestions?

CMD:

``` bash
python3 -m sglang.launch_server \
  --model deepseek-ai/DeepSeek-R1 \
  --port 8000 \
  --trust-remote-code \
  --tp 8
```