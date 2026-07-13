# Does ROCm support MPS?

- **Issue #:** 1734
- **State:** closed
- **Created:** 2022-05-02T05:55:31Z
- **Updated:** 2024-02-01T13:42:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/1734

MPS takes work (e.g. CUDA kernel launches) that is issued from separate processes, and runs them on the device as if they emanated from a single process. As if they are running in a single context. 

I want 2 processes(parent and son process) to share a context. Can ROCm or a AMD GPU have this MPS-like feature?