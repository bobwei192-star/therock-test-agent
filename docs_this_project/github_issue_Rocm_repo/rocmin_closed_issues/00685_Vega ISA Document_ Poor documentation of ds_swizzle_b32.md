# Vega ISA Document: Poor documentation of ds_swizzle_b32

- **Issue #:** 685
- **State:** closed
- **Created:** 2019-01-23T19:17:06Z
- **Updated:** 2019-12-13T06:56:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/685

I don't know where to report documentation issues. But hopefully someone here knows where to forward this issue?

On the 28-July-2017 Vega ISA guide (which exists at https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf today), there's virtually no documentation on the ds_swizzle_b32 instruction. Page 161:

```
RETURN_DATA = swizzle(vgpr_data, offset1:offset0).
Dword swizzle, no data is written to LDS memory.
```

Fortunately, the 2016 GCN3 ISA Guide has good documentation for ds_swizzle_b32. Hopefully, the issue can be corrected before the next ISA document is released. Ideally, the Vega ISA guide could be updated as well.