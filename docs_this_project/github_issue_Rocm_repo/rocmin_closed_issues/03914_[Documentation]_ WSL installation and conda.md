# [Documentation]: WSL installation and conda

- **Issue #:** 3914
- **State:** closed
- **Created:** 2024-10-17T14:20:34Z
- **Updated:** 2024-12-19T06:05:33Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/3914

### Description of errors

after following the installation for WSL on ubuntu when you check for a working torch install you get t his error when you have an active conda environment.  

`
ImportError: /home/schoch/miniconda3/envs/Pose2Sim/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/schoch/miniconda3/envs/Pose2Sim/lib/python3.10/site-packages/torch/lib/libhsa-runtime64.so)
`

This can be fixed by running: `conda install -c conda-forge gcc=12.1.0`

Should be useful to wsl users and considered to be added to the rocm wsl install documentation.

It may also trip users up that python 3.10 is required, it doesn't actually say that in the install docs.

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_