# How to assemble disassembly of a kernel so it's executable again?

- **Issue #:** 4549
- **State:** closed
- **Created:** 2025-04-01T03:39:32Z
- **Updated:** 2025-04-02T17:39:31Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4549

I have a CK example binary (`build/bin/example_gemm_xdl_int8`) that I can disassemble to get the *.s (disassembly) file. If I now want to add a couple of assembly instructions there and restitch the unified binary back together, what are my options? 