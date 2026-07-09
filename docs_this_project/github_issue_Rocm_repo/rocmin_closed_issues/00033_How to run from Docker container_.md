# How to run from Docker container?

- **Issue #:** 33
- **State:** closed
- **Created:** 2016-09-27T07:18:29Z
- **Updated:** 2016-09-27T13:21:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/33

Is it possible to install and run ROCm from a docker container provided that the correct kernel is loaded?

I am running Ubuntu 16.04 and would like to install and use ROCm from a 14.04 container. I've tried using kernel 4.8.0rc8 (built from yakkety master/next) and starting docker container with `docker run -it --device=/dev/kfd <image id>`. `/opt/rocm/bin/rocm-smi -a` sees the GPU. However, vector_copy fails with `Getting a gpu agent failed.`. Debugging shows that it doesn't find any agents.
