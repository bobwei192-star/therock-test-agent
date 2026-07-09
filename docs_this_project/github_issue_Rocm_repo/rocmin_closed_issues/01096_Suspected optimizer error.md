# Suspected optimizer error

- **Issue #:** 1096
- **State:** closed
- **Created:** 2020-05-03T17:45:53Z
- **Updated:** 2020-05-07T03:07:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/1096

To enable using OMOD mul:2, I have these asm instructions near the start of my kernel.
    __asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 9, 1), 0");
    __asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 4, 4), 7");
In looking at disassembly, the optimizer is happily moving floating point ops ahead of these instructions (presumably to hide memory load latency).  

Fortunately, my OMOD instructions are a little further down and I have not been affected by this potential problem.