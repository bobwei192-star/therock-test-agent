# AMDGPUpro 17.30 Codegen: redundant v_trunc after v_rndne ?

- **Issue #:** 210
- **State:** closed
- **Created:** 2017-09-15T11:33:05Z
- **Updated:** 2018-02-16T02:08:19Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/210

On Ubuntu 17.04, AMDGPU-pro 17.30, Vega64.

I see this sequence generated:
```
v_rndne_f64_e32 v[10:11], v[10:11]                   // 00000001041C: 7E14330A
v_trunc_f64_e32 v[10:11], v[10:11]                   // 000000010420: 7E142F0A
```
Corresponding to *rint(double)* in the context of:
```
long toLong(double x) { return rint(x); }
```

My understanding is that *rndne* (round-to-nearest-even) already produces an integral value. So why is the *trunc* needed afterwards?
