# [Issue]: Ubuntu 24.04 APT Issues

- **Issue #:** 5797
- **State:** closed
- **Created:** 2025-12-19T14:41:37Z
- **Updated:** 2026-01-05T15:31:26Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5797

### Problem Description

Hi,
I've been having issues installing packages using the ROCm APT repositories for quite some time now.
I use the following `Dockerfile`:
```docker

# Build Arguments
ARG ROCM_VERSION=7.1.1
# Install dependencies
RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-certificates curl  \
    build-essential  software-properties-common cmake g++-12 libstdc++-12-dev rpm libelf-dev libnuma-dev sudo  \
    libdw-dev git python3 python3-pip gnupg unzip ripgrep libelf1 file pkg-config xxd ninja-build zsh git npm  \
    python3.12-venv nodejs kmod
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 20 --slave /usr/bin/g++ g++ /usr/bin/g++-12

# ROCm installation
RUN echo "Package: *\nPin: origin ""\nPin-Priority: 600" > /etc/apt/preferences.d/rocm-pin-600
RUN curl -sL https://repo.radeon.com/rocm/rocm.gpg.key | apt-key add - \
  && printf "deb [arch=amd64] https://repo.radeon.com/rocm/apt/$ROCM_VERSION/ noble main" |  \
    tee --append /etc/apt/sources.list.d/rocm.list \
  && printf "deb [arch=amd64] https://repo.radeon.com/amdgpu/$ROCM_VERSION/ubuntu noble main" |  \
    tee /etc/apt/sources.list.d/amdgpu.list \
  && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends  \
    rocm-libs$ROCM_VERSION  \
    rocm-dev$ROCM_VERSION  \
    rocm-llvm-dev$ROCM_VERSION && apt-get clean && rm -rf /var/lib/apt/lists/*
```

As you can see I install ROCm packages with their version name appended at the end (e.g. rocm-libs7.1.1 instead of installing rocm-libs) because otherwise I would get broken dependencies:
```
5.821 The following packages have unmet dependencies:
5.932  rocm-dev : Depends: hipcc (= 1.1.1.70101-38~24.04) but 5.7.1-3 is to be installed
5.932             Depends: rocm-cmake (= 0.14.0.70101-38~24.04) but 6.0.0-1 is to be installed
5.932             Depends: rocm-utils (= 7.1.1.70101-38~24.04) but it is not going to be installed
5.939 E: Unable to correct problems, you have held broken packages.
```

Please fix the broken dependency issue in next ROCm releases.

Thank you

### Operating System

Ubuntu 24.04

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 7.1.1

### ROCm Component

_No response_

### Steps to Reproduce

Simply remove the $ROCM_VERSION from the package name and attempt to build the container.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_