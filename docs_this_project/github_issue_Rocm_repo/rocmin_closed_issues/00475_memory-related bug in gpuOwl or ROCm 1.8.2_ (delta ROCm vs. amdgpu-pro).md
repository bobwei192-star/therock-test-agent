# memory-related bug in gpuOwl or ROCm 1.8.2? (delta ROCm vs. amdgpu-pro)

- **Issue #:** 475
- **State:** closed
- **Created:** 2018-07-27T11:40:03Z
- **Updated:** 2018-07-30T23:54:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/475

On Ubuntu 18.04, Kernel 4.15, Rx Vega64. Running gpuOwl https://github.com/preda/gpuowl .
When moving from amdgpu-pro 18.20 to ROCm 1.8.2, a new error surfaced.
I don't know if this error is caused by ROCm codegen, or by my incorrect understanding of the OpenCL memory model.

In the gpuOwl app https://github.com/preda/gpuowl
(to repro: checkout the source from github, "make openowl", enter a single line containing "80899661" (without quotes) in worktodo.txt , run ./openowl . The app self-checks the computation and reports EE error when the error is present)

So it was running rock-solid on amdgpu-pro 18.20, but a new reproducible error appeared when running on ROCm 1.8.2.

This commit seems to improve the situation (making the error less frequent, or removing it):
https://github.com/preda/gpuowl/commit/c602af285d72fd340a5da0f7d149a2e3d06da1e2

The fix consisted in marking a global buffer "volatile". This clearly changes the codegen, and may explain that the error is fixed. The question is, is this volatile in that commit needed for code correctness? (or is it just hiding a ROCm bug?)

Maybe an engineer with understanding of the OpenCL memory model would like to take a look. The write-read to that global buffer are separated by

void bigBar() { barrier(CLK_GLOBAL_MEM_FENCE | CLK_LOCAL_MEM_FENCE); }

so I would have thought that that is enough to ensure proper memory ordering and visibility (without the volatile).

If anybody wants to look at this and repro, I can assist with building and running the app.
