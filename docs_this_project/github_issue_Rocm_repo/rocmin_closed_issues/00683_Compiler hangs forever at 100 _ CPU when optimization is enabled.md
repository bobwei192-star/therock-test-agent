# Compiler hangs forever at 100 % CPU when optimization is enabled

- **Issue #:** 683
- **State:** closed
- **Created:** 2019-01-20T09:13:20Z
- **Updated:** 2020-12-02T03:10:50Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/683

The attached kernel [kernel.cl.zip](https://github.com/RadeonOpenCompute/ROCm/files/2776416/kernel.cl.zip) (from https://github.com/PlasmaPower/nano-vanity/commit/fc81a55f629200a6abd5233d45751dc677e16ee0) does not compile when optimization is enabled. Instead the compiler hangs forever at 100 % CPU.

How to reproduce:

1. Get a single-use Ubuntu 16.04 machine (no GPU required; 18.04 does not work due to kernel version compatibility of rocm-dkms)
2. Login as root

```
apt update && apt upgrade -y && apt autoremove -y && apt install -y htop libnuma-dev && reboot
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
apt update && apt install -y rocm-dkms
git clone https://github.com/PlasmaPower/nano-vanity.git && cd nano-vanity
git checkout fc81a55f629200a6abd5233d45751dc677e16ee0
./merge-kernel.py > kernel.cl

/opt/rocm/opencl/bin/x86_64/clang -include/opt/rocm/opencl/include/opencl-c.h -cl-std=CL1.2 -c -O0 kernel.cl
# good: creates kernel.o

/opt/rocm/opencl/bin/x86_64/clang -include/opt/rocm/opencl/include/opencl-c.h -cl-std=CL1.2 -c kernel.cl
# bad: does not terminate
```

Maybe there is some error which clang does not report. However, since CPU is at 100 % as long as the compiler runs it is more likely to be an infinite loop in the optimization process.

[It was confirmed](https://community.amd.com/message/2894839#2894839) that the same kernel compiles without issues in the CodeXL toolchain on Windows.