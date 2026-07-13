# hsa-ext-rocr-dev is broken since ROCm 2.9

- **Issue #:** 981
- **State:** closed
- **Created:** 2019-12-23T07:57:16Z
- **Updated:** 2023-12-14T11:35:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/981

When hsa-ext-rocr-dev is upgraded from ROCm repo 2.10 or 3.0 for image support clinfo segfaults and so does Darktable. Last version that worked was hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm from ROCm 2.9. Downgrading to package hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm solves the issue.

ROCm 2.2 to 2.9 works
2.10 and 3.0 does not.

AMD Raven Ridge APU 2700u Fedora 31 x64