# ROCm Linux packaging approaching bloatware: 29GB

- **Issue #:** 4224
- **State:** open
- **Created:** 2025-01-06T01:40:59Z
- **Updated:** 2026-06-02T16:00:30Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4224

Why is Linux official Ubuntu 24.04 ROCm 6.3.1 pkgs installing 29G of files under `/opt/rocm-6.3.1`? 

This is borderline bloatware on a new level. Did devs forget to follow standard procedures and share libs? Sorry if this sound negative because I don't know how else to describe it.

Maybe there is a valid reason but please explain the reasons if possible. Cuda toolkit is 3GB for comparison.

I want ROCm to succeed but not with this bloatware size that no sane user would want on any platform.

* Can we and how do we compile rocm so only set arch is included? For examplex, only compile for RDNA2 7900XTX? Trying to think of a way to reduce this monstrosity.



