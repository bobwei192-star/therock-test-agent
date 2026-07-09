# V_MAD_U64_U32 and V_MAD_I64_I32 Documentation: VOP3B but undocumented SDST

- **Issue #:** 752
- **State:** closed
- **Created:** 2019-03-28T20:05:40Z
- **Updated:** 2023-08-07T23:43:54Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/752

In the Vega ISA, V_MAD_U64_U32  and V_MAD_I64_I32 are documented as follows:

    {vcc_out,D.u64} = S0.u32 * S1.u32 + S2.u64.

However, the VOP3B opcodes touch 5 registers: S0, S1, S2 (3 source registers), VDST (destination), and SDST (a 5th register, "scalar" destination). 

This seems to me to be a documentation error. Perhaps "VCC_OUT" is really sent to SDST? (If so, it should be specified that SDST represents two registers / a register pair) I haven't really tested it one way or the other yet, but its clear to me that something is documented wrong. Page 149 of the PDF, but printed as page "141 of 239".