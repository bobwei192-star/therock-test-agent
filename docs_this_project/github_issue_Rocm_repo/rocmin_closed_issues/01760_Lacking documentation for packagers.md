# Lacking documentation for packagers

- **Issue #:** 1760
- **State:** closed
- **Created:** 2022-06-24T16:32:28Z
- **Updated:** 2025-03-21T19:05:16Z
- **Labels:** Documentation
- **Milestone:** Explanatory Documentation Requests
- **URL:** https://github.com/ROCm/ROCm/issues/1760

Since ROCm 5.0, the provided installation documentation heavily leans on AMD's binary packaging and installation script. These methods may be convenient for some but are not appropriate for distribution packagers and are not a substitute for proper build documentation.

This is in large part why [no widely-used Linux distribution](https://repology.org/project/rocm-smi/versions) ships packaging for anything newer than ROCm 4.5. If ROCm is going to be a serious alternative to CUDA, there needs to be a stronger effort put into dissemination, including facilitating packaging. This would require a maintained document (ideally in this repository) which:

 * briefly summarises ROCm's components, their dependencies, and, in the case of forks (e.g. LLVM), how they relate to their upstream projects
 * either describes how to build each individual component or refers to up-to-date documentation in that component's repository which describes the same
 * describes any necessary environment configuration (e.g. which device nodes must be accessible to users)
 * optional but recommended: describes how downstream packages (e.g. `pytorch`, `tensorflow`) should be packaged to allow users to benefit from ROCm

Such documentation shouldn't be difficult to develop and yet will help avoid issues such as https://github.com/ROCm-Developer-Tools/ROCclr/issues/34, making ROCm a more attractive project to packagers.