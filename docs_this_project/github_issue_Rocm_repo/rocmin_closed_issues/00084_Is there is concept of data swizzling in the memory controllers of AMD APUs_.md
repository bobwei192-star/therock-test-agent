# Is there is concept of data swizzling in the memory controllers of AMD APUs?

- **Issue #:** 84
- **State:** closed
- **Created:** 2017-02-02T04:19:43Z
- **Updated:** 2017-07-02T17:27:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/84

Data Swizzing means, the data lines are swapped before written to the RAM . So that on reading back the controller knows the exact swap pattern in data lines. This is provided for encryption. 