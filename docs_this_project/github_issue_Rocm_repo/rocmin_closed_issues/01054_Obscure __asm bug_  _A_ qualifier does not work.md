# Obscure __asm bug:  "A" qualifier does not work

- **Issue #:** 1054
- **State:** closed
- **Created:** 2020-03-20T04:56:56Z
- **Updated:** 2021-04-05T10:19:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1054

__asm("v_bfe_u32 %0, %1, %2, 1" : "=v" (b1) : "v" (b2), "A" (i));

where b1 and b2 are variables and "i" is a constant, generates this error:

error: invalid input constraint 'A' in asm

The "A" constraint means a constant in the -16 to 64 range according to https://gcc.gnu.org/onlinedocs/gcc/Machine-Constraints.html#Machine-Constraints
