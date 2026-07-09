# Inline assembly Mul:2 Div:2 modifiers ignored

- **Issue #:** 964
- **State:** closed
- **Created:** 2019-12-14T05:06:08Z
- **Updated:** 2023-12-18T19:33:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/964

Take any working code with inline assembly.  Add mul:2 or div:2 modifiers to the assembly and your code will still work!

This is the assembly code I wrote to calculate tmp = 2 * a.x * a.y:
              __asm( "v_mul_f64 %0, %1, %2 mul:2\n" : "=v" (tmp) : "v" (a.x), "v" (a.y)); 
