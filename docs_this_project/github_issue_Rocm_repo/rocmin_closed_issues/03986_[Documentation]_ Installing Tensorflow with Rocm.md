# [Documentation]: Installing Tensorflow with Rocm

- **Issue #:** 3986
- **State:** closed
- **Created:** 2024-11-03T14:52:19Z
- **Updated:** 2024-11-25T19:31:12Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3986

### Description of errors

Attempting to follow the official instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html) on an Ubuntu 24.04 system with a rocm 6.2 and a 7900XTX.

My understanding is that the variables I need are:

* repo = `https://repo.radeon.com/rocm/manylinux/rocm-rel-6.2/`
* wheel-version = `2.14.1` or `2.15.1`  or `2.16.1`.

But when I attempt to install tensorflow from the given repository using these instructions I get a not found error:

```
$ pip install tensorflow-rocm==2.16.1 -f https://repo.radeon.com/rocm/manylinux/rocm-rel-6.2/ --upgrade
Looking in links: https://repo.radeon.com/rocm/manylinux/rocm-rel-6.2/
ERROR: Could not find a version that satisfies the requirement tensorflow-rocm==2.16.1 (from versions: none)
ERROR: No matching distribution found for tensorflow-rocm==2.16.1


# The same happens when I try 2.14.1 or 2.15.1 or 2.16
```

Unfortunately my understanding of `pip` is limited and I do not understand why it is unable to find the version that satisfies the requirements. Am I doing something obviously wrong or is there a problem with the documentation?

I was looking forward to using my 7900xtx for some machine learning work. In fact the promised rocm support was the reason I went with this card.

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_