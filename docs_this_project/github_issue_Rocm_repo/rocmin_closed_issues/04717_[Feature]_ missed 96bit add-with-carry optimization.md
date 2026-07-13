# [Feature]: missed 96bit add-with-carry optimization

- **Issue #:** 4717
- **State:** closed
- **Created:** 2025-05-07T14:47:34Z
- **Updated:** 2025-08-11T10:50:33Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4717

### Suggestion Description

```
typedef uint uint32;
typedef ulong uint64;
typedef struct { uint64 s0; uint32 s1; } uint96;

uint96 uint96_add_64(const uint96 x, const uint64 y)
        uint96 r;
	const uint64 s0 = x.s0 + y;
	r.s0 = s0;
	r.s1 = x.s1 + (s0 < y);
	return r;
}
```

On RDNA 3, it gets optimized to
```
	s_waitcnt vmcnt(0) expcnt(0) lgkmcnt(0)
	v_add_co_u32 v0, vcc_lo, v3, v0
	v_add_co_ci_u32_e32 v1, vcc_lo, v4, v1, vcc_lo
	s_delay_alu instid0(VALU_DEP_1)
	v_cmp_lt_u64_e32 vcc_lo, v[0:1], v[3:4]
	v_add_co_ci_u32_e32 v2, vcc_lo, 0, v2, vcc_lo
	s_setpc_b64 s[30:31]
```

Could the v_cmp_lt_u64_e32 instruction be eliminated? It appears to be the same issue reported in https://github.com/ROCm/ROCm/issues/477, yet it still seems to persist on recent GPUs.

### Operating System

_No response_

### GPU

7900 XTX

### ROCm Component

_No response_