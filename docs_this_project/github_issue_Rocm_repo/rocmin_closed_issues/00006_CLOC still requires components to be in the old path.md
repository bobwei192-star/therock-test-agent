# CLOC still requires components to be in the old path

- **Issue #:** 6
- **State:** closed
- **Created:** 2016-04-23T20:30:06Z
- **Updated:** 2016-05-01T20:34:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/6

I had just installed the ROCm using apt-get a few days ago. I saw the cloc is integrated into the package. However, in cloc.sh and snack.sh, the default path is still pointing to /opt/amd/llvm and /opt/amd/hsa. Should these default paths be updated? Is there a way that we can configure the tools to still make them usable? I did not see a clang in the llvm path, so which clang we can use for now? Can the one in /opt/rocm/hcc-hsail/bin work together with cloc?
