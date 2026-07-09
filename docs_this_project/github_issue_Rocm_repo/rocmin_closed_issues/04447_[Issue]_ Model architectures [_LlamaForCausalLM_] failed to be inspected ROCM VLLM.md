# [Issue]: Model architectures ['LlamaForCausalLM'] failed to be inspected ROCM VLLM

- **Issue #:** 4447
- **State:** closed
- **Created:** 2025-03-05T06:59:38Z
- **Updated:** 2025-07-15T05:38:45Z
- **Labels:** Under Investigation, ROCm 6.3.1
- **URL:** https://github.com/ROCm/ROCm/issues/4447

### Problem Description

I have an AMD GPU (RX 6800 XT) and am unable to run Docker with vLLM. Below are the details of my setup:

export MODEL=amd/Llama-3.1-8B-Instruct-FP8-KV
export DOCKER_IMG=rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6
export HOST_PORT=80
export HF_TOKEN="xxxxxxxxxxx" 

docker run --rm --device=/dev/kfd --device=/dev/dri --group-add video --shm-size 16G \
    -p $HOST_PORT:$HOST_PORT \
    --security-opt seccomp=unconfined \
    --security-opt apparmor=unconfined \
    --cap-add=SYS_PTRACE \
    -v $(pwd):/workspace \
    --env HUGGINGFACE_HUB_CACHE=/workspace \
    --env VLLM_USE_TRITON_FLASH_ATTN=0 \
    --env PYTORCH_TUNABLEOP_ENABLED=1 \
    --env TORCH_USE_HIP_DSA=1 \
    --env HF_TOKEN=$HF_TOKEN \
    --env AMD_SERIALIZE_KERNEL=1 \ 
    $DOCKER_IMG python3 -m vllm.entrypoints.openai.api_server \
    --model $MODEL \
    --swap-space 16 \
    --disable-log-requests \
    --dtype float16 \
    --quantization fp8 \
    --kv-cache-dtype fp8 \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.9 \
    --host 0.0.0.0 \
    --port $HOST_PORT \
    --distributed-executor-backend "mp"


### Operating System

ubuntu-24.04.1-live-server-amd64

### CPU

 Intel(R) Core(TM) i7-10700F CPU @ 2.90GHz

### GPU

[AMD/ATI] Navi 21 [Radeon RX 6800/6800 XT / 6900 XT]

### ROCm Version

6.3.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_