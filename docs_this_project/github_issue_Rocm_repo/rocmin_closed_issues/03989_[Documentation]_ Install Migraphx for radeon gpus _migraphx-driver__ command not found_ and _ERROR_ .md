# [Documentation]: Install Migraphx for radeon gpus <migraphx-driver : command not found> and <ERROR: Could not find a version that satisfies the requirement onnxruntime-rocm>

- **Issue #:** 3989
- **State:** closed
- **Created:** 2024-11-04T19:44:28Z
- **Updated:** 2024-11-06T21:50:16Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3989

### Description of errors

Hello, theses two lines:
```
echo 'export PATH=$PATH:/opt/rocm-6.2.3/bin' >> ~/.bashrc
source ~/.bashrc
```
needs to be added in the documentation here https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-migraphx.html after the command "sudo apt install migraphx" or else the command "migraphx-driver perf --test" will not be found.

another important error is this one: "ERROR: Could not find a version that satisfies the requirement onnxruntime-rocm" after typing the command 
```pip3 install onnxruntime-rocm -f https://repo.radeon.com/rocm/manylinux/rocm-rel-6.0/```
because the right command is this one:
```
pip3 install onnxruntime-rocm -f https://repo.radeon.com/rocm/manylinux/rocm-rel-6.2.3/
```
You can modify the second error in this webpage: https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-migraphx.html#install-migraphx-for-onnx-runtime
### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_