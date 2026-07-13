# [Issue]: 9070xt OOM (Out of memory error) in Comfyui or Stable Diffusion web UI

- **Issue #:** 5216
- **State:** open
- **Created:** 2025-08-21T15:04:13Z
- **Updated:** 2025-09-05T18:48:40Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5216

### Problem Description

After installing Rocm and the driver according to the official documentation 

(https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)

,python=3.10, I installed Torch using 

pip3 install torch torchvision --index-url https://download.pytorch.org/whl/rocm6.4

. I then git cloned ComfyUi, using the -r flag to install dependencies, and then directly launched python main.py with the default workflow and 512x512 resolution. This caused an OOM error and crash during VAE decoding. I tried using --vae-cpu on ComfyUI, but the speed was incredibly slow. SDL VAE processing typically takes several minutes. This issue persists on Linux, WSL, and Windows. Is it a 9070 issue? It hasn't been resolved since June. The system was newly installed, with no other software installed or variables set.

The image cannot be generated normally in sd1.5. Using sdxl 1024x1024 will also cause OOM errors in VAE. When checking the GPU status in the Windows environment, only 8G video memory is used during the sampling process, but when it comes to VAE decoding, 16G video memory will be used instantly.

### Operating System

Linux Ubuntu 24.04.3 LTS, WSL2 Ubantu 24.04, Windows10

### CPU

14600kf

### GPU

9070xt

### ROCm Version

6.4.1, 6.4.3

### ROCm Component

_No response_

### Steps to Reproduce

1.Install the new ubantu24.04.3

2.Install rocm

wget https://repo.radeon.com/amdgpu-install/6.4.3/ubuntu/noble/amdgpu-install_6.4.60403-1_all.deb
sudo apt install ./amdgpu-install_6.4.60403-1_all.deb
sudo apt update
sudo apt install python3-setuptools python3-wheel
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
sudo apt install rocm

3.Install driver

wget https://repo.radeon.com/amdgpu-install/6.4.3/ubuntu/noble/amdgpu-install_6.4.60403-1_all.deb
sudo apt install ./amdgpu-install_6.4.60403-1_all.deb
sudo apt update
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt install amdgpu-dkms

sudo reboot
4.git clone https://github.com/comfyanonymous/ComfyUI.git

5.
cd ~/ComfyUI
pip3 install -r requirements.txt

cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager
cd ComfyUI-Manager
pip3 install -r requirements.txt

6.
cd ~/ComfyUI
python main.py

After the window starts, click the first sample workflow. If it prompts that the file is missing, click Download, put the downloaded file in the checkpoint directory, and then click Run to execute the workflow.
Then you will get OOM error.

Then your PC will become very lag and you will get an OOM error after a while.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_