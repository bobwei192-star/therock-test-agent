# [Documentation]: Inconsistent install instructions for `ROCm/bitsandbytes`

- **Issue #:** 3132
- **State:** closed
- **Created:** 2024-05-15T16:24:22Z
- **Updated:** 2024-08-02T19:01:33Z
- **Assignees:** eliotli, SeanSong-amd
- **URL:** https://github.com/ROCm/ROCm/issues/3132

### Description of errors

There are some recent blog posts [1,2,3] that provide the following install instructions for `ROCm/bitsandbytes` for ROCm v6.x:
```
git clone --recurse https://github.com/ROCm/bitsandbytes.git
cd bitsandbytes
git checkout rocm_enabled
make hip
python setup.py install
```

One can easily verify that the `rocm_enabled` branch does not include a `Makefile`.

In the README for this branch, it does provide the following instructions for installing `ROCm/bitsandbytes`: 
```
git clone --recurse https://github.com/ROCm/bitsandbytes
cd bitsandbytes
# Checkout branch as needed
# for rocm 5.7 - rocm5.7_internal_testing
# for rocm 6.x - rocm6.2_internal_testing
git checkout <branch>
make hip
python setup.py install
```

These instructions seem to work. 

However, in the README for the branch `rocm6.2_internal_testing`, the same incorrect install steps are provided for `ROCm/bitsandbytes`:
```
# Install BitsandBytes
git clone --recurse https://github.com/ROCmSoftwarePlatform/bitsandbytes
cd bitsandbytes
git checkout rocm_enabled
make hip
python setup.py install
```

The same incorrect instructions are in the README for the branch `rocm5.7_internal_testing`.

The branch `rocm6.2_internal_testing` needs to be corrected to have the following install instructions:
```
git clone --recurse https://github.com/ROCm/bitsandbytes
cd bitsandbytes
git checkout rocm6.2_internal_testing
make hip
python setup.py install
```

And the branch `rocm5.7_internal_testing` needs to be corrected to have the following install instructions
```
git clone --recurse https://github.com/ROCm/bitsandbytes
cd bitsandbytes
git checkout rocm5.7_internal_testing
make hip
python setup.py install
```

This would provide working, consistent install instructions between the three branches `rocm5.7_internal_testing`, `rocm6.2_internal_testing`, and `rocm_enabled`.

Other branches might have incorrect instructions, but I have not checked branches besides these three.


[1] [https://rocm.blogs.amd.com/artificial-intelligence/starcoder-fine-tune/README.html](https://rocm.blogs.amd.com/artificial-intelligence/starcoder-fine-tune/README.html)

[2] [https://rocm.blogs.amd.com/artificial-intelligence/llama2-Qlora/README.html](https://rocm.blogs.amd.com/artificial-intelligence/llama2-Qlora/README.html)

[3] [https://rocm.blogs.amd.com/artificial-intelligence/llama2-lora/README.html](https://rocm.blogs.amd.com/artificial-intelligence/llama2-lora/README.html)