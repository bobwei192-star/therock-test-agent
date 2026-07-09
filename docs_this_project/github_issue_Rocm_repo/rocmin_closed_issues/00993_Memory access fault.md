# Memory access fault

- **Issue #:** 993
- **State:** closed
- **Created:** 2020-01-05T18:33:11Z
- **Updated:** 2020-01-05T21:06:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/993

Error is:

`Memory access fault by GPU node-1 (Agent handle: 0x555afc5a0640) on address 0x508400000. Reason: Page not present or supervisor privilege.`

Reproducer [here](https://github.com/GrokImageCompression/latke/tree/mem_error) : run the debayer test app.

I have checks in the kernel to make sure that writes are not out of bounds, but I still get an error.
It goes away if I add 1 to the size of the output buffer.

