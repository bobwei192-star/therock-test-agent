# FR: generate MUL:2, MUL:4, DIV:2  for VOP3 instructions (OpenCL performance)

- **Issue #:** 1405
- **State:** open
- **Created:** 2021-03-13T08:11:20Z
- **Updated:** 2024-10-22T21:13:19Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1405

A function such as:
double sum2(double x, double y) { return 2 * (x + y); }
could be compiled to a single VOP3 GCN instructions such as:
```
v_add_f64 %0, %1, %2 MUL:2
```

But this efficient code is not generated because MUL:2 and the like only function correctly with denormals disabled and non-IEEE mode. (denormals and IEEE mode can be set thus:
```
// turn IEEE mode and denormals off so that mul:2 and div:2 work
#define ENABLE_MUL2() { \
    __asm volatile ("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 9, 1), 0");\
    __asm volatile ("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 4, 4), 7");\
}
```

Feature request: please provide an OpenCL compilation flag that enables MUL:2 and the like, at the same time disabling denormals and IEEE mode as required. This would allow a developer to choose between the two good things: denormals on one side, and more performance on the other side (by making better use of the power of VOP3 instructions).
