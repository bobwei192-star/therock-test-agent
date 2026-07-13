# "broken packages" failure on "Option 3: Install using minimal ROCm docker file" in the Rocmdocs site

- **Issue #:** 1457
- **State:** closed
- **Created:** 2021-04-19T14:16:30Z
- **Updated:** 2021-06-02T11:55:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1457

I'm performing step 3 of the manual: https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#pytorch
and during command "`sudo docker build .`"
I get:
```
The following packages have unmet dependencies:
 rocm-dev : Depends: rocm-gdb but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
