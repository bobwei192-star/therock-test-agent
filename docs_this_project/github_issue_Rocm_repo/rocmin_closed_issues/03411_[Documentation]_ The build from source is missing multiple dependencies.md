# [Documentation]: The build from source is missing multiple dependencies

- **Issue #:** 3411
- **State:** closed
- **Created:** 2024-07-10T18:52:25Z
- **Updated:** 2025-06-23T14:45:16Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/3411

### Description of errors

I've been trying to follow "option 2", the non-docker build, and there are multiple packages that it requires that do not seem to be documented. I was trying to build on Ubuntu 22.04.

git requires curl/curl.h. This seems to collide with Ubuntu's packaging system badly, I ended up installing multiple curl related packages and am unsure which fixed it. Since the instructions use git to clone and install git's large file handling from repos, this is probably best fixed by not building git from source.

ninja's build uses `/usr/bin/env python` where there is no python. The most likely fix seems to be `apt install python-is-python3` but much safer would be installing ninja from apt instead of from source.

Boost required `apt install lbzip2`. Otherwise `command -f lbzip2` returns the empty string.

cp /tmp/local-pin-600 fails as the file doesn't exist, don't know what is supposed to be in it.

HIP fails to build without rpmbuild, found in `apt install rpm`

rocm-dbgapi fails to build on "no rule to make target doc". It looks like the cmake understands that doxygen is optional but other things do not. Installing doxygen gets as far as missing pdflatex. `apt install doxygen texlive` resolves those errors.

That's as far as I've got before giving up and trying docker, which seems to go into a busy loop on start that it does not recover from.

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_