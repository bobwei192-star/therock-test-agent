# [Feature]: Intermediate bytecode to allow for forward compat, reduced build times and smaller binaries

- **Issue #:** 3985
- **State:** open
- **Created:** 2024-11-03T04:26:49Z
- **Updated:** 2024-12-18T23:03:55Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/3985

Do you have any plans to support an intermediary compile target a la PTX so code targeting AMD GPUs can be compiled for that intermediary and then at runtime it's translated as needed to machine code for whatever GPU is actually in use?

The current approach requires compiling machine code for all AMD GPUs ahead of time; forward compat without a recompile is impossible.

Compiling for each individual gfxXXX target in advance takes up a lot of space and takes a long time for any large ROCm project. This aspect of ROCm is significantly worse than CUDA.