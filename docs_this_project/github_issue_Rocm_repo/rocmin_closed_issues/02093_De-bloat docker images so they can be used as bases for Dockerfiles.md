# De-bloat docker images so they can be used as bases for Dockerfiles

- **Issue #:** 2093
- **State:** closed
- **Created:** 2023-04-28T04:27:47Z
- **Updated:** 2024-10-10T18:14:22Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/2093

Related to https://github.com/RadeonOpenCompute/ROCm-docker/issues/92

I had to use `podman` to download `rocm5.4.2_ubuntu20.04_py3.8_pytorch_2.0.0_preview`, because `docker` gets stuck downloading some of the layers... 

Podman reports the image as consuming 38GB of disk space!
```
docker.io/rocm/pytorch   rocm5.4.2_ubuntu20.04_py3.8_pytorch_2.0.0_preview  96c28752acb8  3 weeks ago   37.5 GB
```

38 GB is unusable for anyone without terabytes of free disk space.

Each layer operation uses 38GB (+ whatever the layer does), meaning a relatively simple **7 layer** `Dockerfile` based from `rocm5.4.2_ubuntu20.04_py3.8_pytorch_2.0.0_preview` requires more that **450 GB** of free space to build!

I don't know how these images are being built, but there has to be a better way...  Please de-bloat them, so others can make use of them as bases.