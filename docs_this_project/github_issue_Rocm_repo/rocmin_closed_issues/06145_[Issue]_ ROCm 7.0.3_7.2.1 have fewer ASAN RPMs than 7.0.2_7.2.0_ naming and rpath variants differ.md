# [Issue]: ROCm 7.0.3/7.2.1 have fewer ASAN RPMs than 7.0.2/7.2.0; naming and rpath variants differ

- **Issue #:** 6145
- **State:** closed
- **Created:** 2026-04-13T14:14:38Z
- **Updated:** 2026-04-27T18:37:06Z
- **Labels:** status: assessed
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6145

### Problem Description


rocm 7.0.3 and 7.2.1 has fewer packages than e.g. 7.0.2 and 7.2.0.
It seems mainly to be asan packages that are missing.

For example, in 7.2.0, there are:
  roctracer-asan-4.1.70200.70200-sles156.43.x86_64.rpm
  roctracer-asan7.2.0-4.1.70200.70200-sles156.43.x86_64.rpm
  roctracer-asan-rpath7.2.0-4.1.70200.70200-sles156.43.x86_64.rpm

where
  roctracer-asan-rpath7.2.0-4.1.70200.70200-sles156.43.x86_64.rpm 
and
  roctracer-asan7.2.0-4.1.70200.70200-sles156.43.x86_64.rpm
seem to contain the same things, which is maybe not intentional.

In 7.2.1, there is only
  roctracer-asan-4.1.70201.70201-sles156.81.x86_64.rpm

So no rpath version, which may or may not be intentional, and you went with the
  roctracer-asan-4.1.70201.70201-sles156.81.x86_64.rpm
instead of the
  roctracer-asan7.2.1-4.1.70201.70201-sles156.81.x86_64.rpm
which I don't know if it is intentional, since now it is much tricker to point out a specific version of things in the same way as you could before.

Is this a mistake, or should we adapt to this?

Best regards,
Ragnar

### Operating System

sles15sp7

### CPU

AMD EPYC 7A53 64-Core Processor

### GPU

AMD Instinct MI250X

### ROCm Version

ROCm 7.2.1 (and 7.0.3)

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_