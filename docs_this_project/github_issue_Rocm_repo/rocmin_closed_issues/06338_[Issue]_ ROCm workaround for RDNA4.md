# [Issue]: ROCm workaround for RDNA4

- **Issue #:** 6338
- **State:** closed
- **Created:** 2026-06-07T20:00:57Z
- **Updated:** 2026-06-25T15:16:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/6338

### Problem Description

OS:
NAME="Ubuntu"
VERSION="24.04.4 LTS (Noble Numbat)"
CPU: 
model name	: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
GPU:
bash: /opt/rocm/bin/rocminfo: No such file or directory
beug@AIMax:~$ 

[SOLVED] OpenAI Whisper on AMD RDNA4 (Radeon 8060S) with ROCm via Docker

Hey everyone,

I wanted to share my experience getting Whisper to run GPU-accelerated on an AMD Radeon 8060S (RDNA4 architecture) since I couldn't find any working solution online and it took me many hours to figure out.

The core problem is that RDNA4 GPUs (gfx1201) are not yet officially supported by ROCm. This means that almost every pre-built Docker image or Python package that claims ROCm compatibility will simply fail, because the GPU is not recognized. The workaround is to set the environment variable HSA_OVERRIDE_GFX_VERSION=11.5.1, which makes ROCm treat the card as a known, compatible GPU.

What didn't work: WhisperX (missing modules), insanely-fast-whisper (dependency hell), various pre-built ROCm-Whisper Docker images from Docker Hub (missing whisper module, segfaults, exit code 139).

What finally worked: Using rocm/pytorch:latest as the base image (which ships with torch 2.10 + ROCm 7.2) and manually installing openai-whisper and ffmpeg on top. With the GFX override set, the large-v3 model loads and runs correctly on the GPU. We verified this with a full transcription producing over 69,000 characters.

If you are in a similar situation, build your own image from rocm/pytorch:latest, install whisper manually, always pass -e HSA_OVERRIDE_GFX_VERSION=11.5.1 to your docker run command, and don't waste time trying to patch existing images.

Hope this saves someone else a few hours!


Here is the Dockerfile that worked for me:

FROM rocm/pytorch:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install openai-whisper
RUN pip install openai-whisper

# Set working directory
WORKDIR /app

Build it with:

docker build -t whisper-rocm-final .

Run it with:

docker run --rm \
  --device=/dev/kfd --device=/dev/dri \
  -v "$HOME/your-audio-folder":/input \
  -v "$HOME/your-output-folder":/output \
  -e HSA_OVERRIDE_GFX_VERSION=11.5.1 \
  whisper-rocm-final \
  python3 -c "
import whisper, torch
model = whisper.load_model('large-v3', device='cuda')
result = model.transcribe('/input/yourfile.mp3', language='de', fp16=True)
with open('/output/output.txt', 'w') as f:
    f.write(result['text'])
print('Done! Characters:', len(result['text']))
"

System info:

    GPU: AMD Radeon 8060S (RDNA4, gfx1201)
    ROCm: 7.2
    PyTorch: 2.10
    Base image: rocm/pytorch:latest
    Whisper model: large-v3


### Operating System

Ubuntu 24.04.4 LTS (Noble Numbat)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD Radeon 8060S (RDNA4, gfx1201)

### ROCm Version

ROCm: 7.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_