# JupyterLab does not work in the PyTorch docker container 

> **Issue #1158**
> **状态**: closed
> **创建时间**: 2020-06-22T14:57:11Z
> **更新时间**: 2020-06-22T18:41:33Z
> **关闭时间**: 2020-06-22T18:41:16Z
> **作者**: devksingh4
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1158

## 描述

Hello all, 
After running `python3.6 -m pip install jupyterlab && jupyter lab --allow-root` in the official docker container, JupyterLab seems to start, but the web GUI freezes at: 
![image](https://user-images.githubusercontent.com/18728114/85302096-55f8ea80-b46e-11ea-8f1b-f0a463c97370.png)

This issue only exists when `torch` is present in the environment. A new conda environment with python3.6 installed runs `jupyter lab` just fine, but when `torch` is added via symlink, Jupyter Lab freezes on the above screen. 


---

## 评论 (3 条)

### 评论 #1 — devksingh4 (2020-06-22T15:03:33Z)

System Info: 
AMD Ryzen 5 1600AF
AMD RX580 
Ubuntu 18.04.4 LTS
Kernel 5.3.0-59-generic

---

### 评论 #2 — devksingh4 (2020-06-22T18:41:16Z)

I "fixed" this issue by using the minimal Docker config and compiling pytorch from the code. I also modified the Dockerfile to use ubuntu 18.04 and python3.


---

### 评论 #3 — devksingh4 (2020-06-22T18:41:33Z)

Here is my Dockerfile if anyone stumbles onto this issue: 

```
# This dockerfile is meant to be personalized, and serves as a template and demonstration.
# Modify it directly, but it is recommended to copy this dockerfile into a new build context (directory),
# modify to taste and modify docker-compose.yml.template to build and run it.

# It is recommended to control docker containers through 'docker-compose' https://docs.docker.com/compose/
# Docker compose depends on a .yml file to control container sets
# rocm-setup.sh can generate a useful docker-compose .yml file
# `docker-compose run --rm <rocm-terminal>`

# If it is desired to run the container manually through the docker command-line, the following is an example
# 'docker run -it --rm -v [host/directory]:[container/directory]:ro <user-name>/<project-name>'.

FROM ubuntu:18.04
MAINTAINER Dev Singh <dev@devksingh.com>

# Initialize the image
# Modify to pre-install dev tools and ROCm packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends curl gnupg2 && \
  curl -sL http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | apt-key add - && \
  sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list' && \
  apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  sudo \
  libelf1 \
  build-essential \
  bzip2 \
  ca-certificates \
  cmake \
  ssh \
  apt-utils \
  pkg-config \
  g++-multilib \
  gdb \
  git \
  less \
  libunwind-dev \
  libfftw3-dev \
  libelf-dev \
  libncurses5-dev \
  libomp-dev \
  libpthread-stubs0-dev \
  make \
  miopen-hip \
  python3-dev \
  python3-future \
  python3-yaml \
  python3-pip \
  vim \
  libssl-dev \
  libboost-dev \
  libboost-system-dev \
  libboost-filesystem-dev \
  libopenblas-dev \
  rpm \
  wget \
  net-tools \
  iputils-ping \
  libnuma-dev \
  rocm-dev \
  rocrand \
  rocblas \
  rocfft \
  hipcub \
  rocthrust \
  hipsparse && \
  curl -sL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
  sh -c 'echo deb [arch=amd64] http://apt.llvm.org/xenial/ llvm-toolchain-xenial-7 main > /etc/apt/sources.list.d/llvm7.list' && \
  sh -c 'echo deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-7 main >> /etc/apt/sources.list.d/llvm7.list' && \
  apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  clang-7 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# fix capitalization in some cmake files...
RUN sed -i 's/find_dependency(hip)/find_dependency(HIP)/g' /opt/rocm/rocsparse/lib/cmake/rocsparse/rocsparse-config.cmake
RUN sed -i 's/find_dependency(hip)/find_dependency(HIP)/g' /opt/rocm/rocfft/lib/cmake/rocfft/rocfft-config.cmake
RUN sed -i 's/find_dependency(hip)/find_dependency(HIP)/g' /opt/rocm/miopen/lib/cmake/miopen/miopen-config.cmake
RUN sed -i 's/find_dependency(hip)/find_dependency(HIP)/g' /opt/rocm/rocblas/lib/cmake/rocblas/rocblas-config.cmake

# Grant members of 'sudo' group passwordless privileges
# Comment out to require sudo
#COPY sudo-nopasswd /etc/sudoers.d/sudo-nopasswd

# This is meant to be used as an interactive developer container
# Create user rocm-user as member of sudo group
# Append /opt/rocm/bin to the system PATH variable
#RUN useradd --create-home -G sudo --shell /bin/bash rocm-user
#RUN usermod -a -G video rocm-user
#    sed --in-place=.rocm-backup 's|^\(PATH=.*\)"$|\1:/opt/rocm/bin"|' /etc/environment

#USER rocm-user
#WORKDIR /home/rocm-user
WORKDIR /root
ENV PATH="${PATH}:/opt/rocm/bin" HIP_PLATFORM="hcc"

#RUN \
#  curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh && \
#  bash Anaconda3-5.0.1-Linux-x86_64.sh -b
#  rm Anaconda3-5.0.1-Linux-x86_64.sh

# The following are optional enhancements for the command-line experience
# Uncomment the following to install a pre-configured vim environment based on http://vim.spf13.com/
# 1.  Sets up an enhanced command line dev environment within VIM
# 2.  Aliases GDB to enable TUI mode by default
#RUN curl -sL https://j.mp/spf13-vim3 | bash && \
#    echo "alias gdb='gdb --tui'\n" >> ~/.bashrc

#RUN \
#  bash installers/Anaconda3-5.2.0-Linux-x86_64.sh -b

#ENV PATH="/home/rocm-user/anaconda3/bin:${PATH}" KMTHINLTO="1"
ENV KMTHINLTO="1" LANG="C.UTF-8" LC_ALL="C.UTF-8"

RUN \
  pip3 install setuptools

RUN \
  pip3 install pyyaml

RUN \
  pip3 install numpy scipy

RUN \
  pip3 install typing

RUN \
  pip3 install enum34

RUN \
  pip3 install hypothesis

RUN \
  pip3 install jupyterlab

RUN \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/clang-7 50 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/clang++-7 50
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN \ 
  curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - && \
  apt install -y nodejs

CMD ["bash", "-l"]

```

---
