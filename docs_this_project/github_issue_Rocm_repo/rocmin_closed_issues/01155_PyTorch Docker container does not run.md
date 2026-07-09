# PyTorch Docker container does not run

- **Issue #:** 1155
- **State:** closed
- **Created:** 2020-06-21T02:54:39Z
- **Updated:** 2020-06-22T14:59:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1155

Hello, 
After following these instructions: 
[https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#recommended-install-using-published-pytorch-rocm-docker-image](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#recommended-install-using-published-pytorch-rocm-docker-image), I run `PYTORCH_TEST_WITH_ROCM=1 python test/run_test.py --verbose` and get `No module named torch`. This is running in the Docker container. 

System: 
AMD Ryzen 5 1600AF
AMD RX 580 8GB 
Ubuntu 18.04.4 LTS - Kernel 5.3.0-59
`rocminfo` shows `ROCk module is loaded`, GPU is shown as Agent 2.
