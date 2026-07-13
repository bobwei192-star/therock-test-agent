# Dell R7525 with 3xMI100 clinfo kills machine with multiGPU PCIe

- **Issue #:** 1493
- **State:** closed
- **Created:** 2021-06-15T07:15:46Z
- **Updated:** 2022-04-20T07:11:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1493

Hi!

I have a Dell R7525 with 3xMI100 installed. No Infinity fabric, only PCIe connection. I have had the below issues from the very first install of the machine. They happen with Centos7.9 and latest Ubuntu LTS server HWE. They also occur with ROCm 4.1.1 and 4.2. The problem goes away if I disable any two of the three MI100 cards.

After following [the installation instructions](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html), I tried the two suggested commands:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
The first runs fine, the **clinfo crashes the machine** on Ubuntu while Centos doesn't quite die, and I was able to capture the attached [dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6653439/dmesg.txt).

I tried various tests from [the validation suite](https://rocmdocs.amd.com/en/latest/Other_Solutions/rocm-validation-suite.html).
The following modules run fine: `gpup`, `peqt`, `pebb`. However, **the pqt module crashed the machine** (got NMIs):

```
- name: action_4
  device: 55570
  module: pqt
  log_interval: 800
  duration: 5000
  peers: 51147
  test_bandwidth: true
  bidirectional: true
  block_size: 1000000 2000000 10000000
```

Later, if I **disable any two of the three MI100 cards** in BIOS, `clinfo` runs fine. 

My colleagues have used the system for some development. This is of course not satisfactory; all three cards must be stably usable. If the peer2peer performance must be low, we can live with that, but the system must remain stable.

Any help would be appreciated.

Best regards,
 - Simppa -