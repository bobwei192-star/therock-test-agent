# Cannot access GPU inside docker images for PyTorch (and Tensorflow)

- **Issue #:** 2741
- **State:** closed
- **Created:** 2023-12-17T16:57:53Z
- **Updated:** 2023-12-18T20:14:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/2741

**Problem Description**
I'm trying to install ROCm PyTorch on a fresh Ubuntu 22.04.3 install, following all the recommend steps in the [rocm installation page](https://rocm.docs.amd.com/en/docs-5.7.1/deploy/linux/installer/install.html) and using docker containers as specified [in the docs](https://rocm.docs.amd.com/en/docs-5.7.1/how_to/pytorch_install/pytorch_install.html) (Option 1):

However, no GPU is detected in the docker container: `cuda.is_available()` returns `False` and `rocminfo` doesen't detect the GPU.

You can find a detailed terminal session with all the commands and output [in this gist](https://gist.github.com/marcopigg/689eb21d01df5fbb7cd0c22d0bbcf40b) (I skipped the output from the initial install commands).

Note also that `docker run` doesn't work without the `--privileged` option.

I don't think the issue is in PyTorch as I have the same problem with the `rocm/tensorflow` containers. No GPU is passed to the docker image.

The iGPU is disabled in BIOS.

**Operating System**
Ubuntu 22.04.3

**CPU**
AMD Ryzen 7700X

**GPU**
AMD Radeon RX 7900 XTX

**ROCm Version**
5.7.1

EDIT: updated gist with docker version (24.0.7, build afdd53b)