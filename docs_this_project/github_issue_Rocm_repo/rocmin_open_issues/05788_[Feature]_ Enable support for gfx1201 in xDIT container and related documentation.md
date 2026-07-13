# [Feature]: Enable support for gfx1201 in xDIT container and related documentation

- **Issue #:** 5788
- **State:** open
- **Created:** 2025-12-17T22:53:35Z
- **Updated:** 2026-01-30T09:54:36Z
- **Labels:** Feature Request, status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5788

### Suggestion Description

There are exciting developments in the world of using multiple-GPUs for diffusion inference with xDIT. Unfortunately, the upstream documentation for xDIT does not produce a working environment for ROCm devices, and the AMD-supplied container refuses to run on gfx1201 for the Radeon Pro AI 9700 XT, which I bought three of. What I am hoping can be provided is the following:

1. Update the xDIT-ROCm container and associated docs to support gfx1201, and preferably also RDNA 3.5, which I also have and am looking forward to using. Ideally, ROCm-related frameworks should run on any ROCm-supported hardware, with a warning rather than a refusal if a specific architecture is not known to work.
2. Expand the xDIT ROCm docs to include non-Docker installations on Linux.

### Operating System

_No response_

### GPU

Radeon Pro AI 9700 XT (gfx1201)

### ROCm Component

_No response_