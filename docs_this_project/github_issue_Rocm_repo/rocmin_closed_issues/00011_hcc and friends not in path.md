# hcc and friends not in path

- **Issue #:** 11
- **State:** closed
- **Created:** 2016-05-17T11:30:50Z
- **Updated:** 2016-08-20T18:49:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/11

Hi -

I just installed ROCm 1.1 on an ubuntu 14.04.04 box successfully, but the paths to hcc/clang++/hipify are not in PATH/LD_LIBRARY_PATH after boot. I am not sure what the rational behind this is, but I suggest to add /opt/rocm/\* to the respective PATHs so that after a fresh boot, I can use these tools right away.

Also, I couldn't find any manpages or other terminal-based documentation bundled under `/opt/rocm`. I only saw `/opt/rocm/hip/docs/html`. Are there any plans to provide further documentation?

Just 2 suggestions/questions -
P
