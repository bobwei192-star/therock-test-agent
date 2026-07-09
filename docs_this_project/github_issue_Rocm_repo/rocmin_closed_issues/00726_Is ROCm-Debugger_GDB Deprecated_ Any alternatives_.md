# Is ROCm-Debugger/GDB Deprecated? Any alternatives?

- **Issue #:** 726
- **State:** closed
- **Created:** 2019-03-08T09:00:42Z
- **Updated:** 2019-03-21T22:06:12Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/726

I was recently looking at how I might easily disassemble a GPU kernel created by a HC Program I have been working on. I found that the view ISA function in CodeXL doesn't support gfx906 yet and then found [ROCm-Debugger which seems to be able to do this.](https://github.com/RadeonOpenCompute/ROCm-Debugger/blob/master/TUTORIAL.md#how-do-i-view-the-gpu-isa-disassembly)
However it hasn't been updated since 2017.
It's instructions state that:
> Note that both rocm-gpudebugsdk and rocm-gdb debian packages are included as part of the ROCm repo install.

But this is **no longer the case**, [others users have discovered this already but their issue has not received any attention.](https://github.com/RadeonOpenCompute/ROCm-Debugger/issues/10)
The [current ROCM documentation states](https://rocm-documentation.readthedocs.io/en/latest/ROCm_Tools/ROCm-Tools.html#rocm-gdb):
> ROCm-GDB
> The ROCm-GDB is being revised to work with the ROCr Debug Agent to support debugging GPU kernels on Radeon Open Compute platforms (ROCm) and will be available in an upcoming release.

This seems unlikely given that development stopped two years ago and had been regular before that.
Are there plans to resurrect ROCm-GDB? **Any other ways to extract and disassemble a kernel from a HC Program?** I will try using the [rocr_debug_agent](https://github.com/ROCm-Developer-Tools/rocr_debug_agent#code-object-saving) but it looks like a step backwards in usability and functionality compared to ROCM-gdb which looked to have had similar usage to gdb.

Also, I think that all the ROCm and GPUOpen repos could use a spring clean more generally, because there seem to be loads of _other_ dead/zombie repos similar to rocm-gdb, where development stopped a while ago or moved elsewhere. However **google still ranks these repos high up in search results** (which is how I found them).
It would be useful if outdated repos were marked as _Deprecated_ so that nobody is confused by why the instructions in them don't work or conflict with the main documentation.