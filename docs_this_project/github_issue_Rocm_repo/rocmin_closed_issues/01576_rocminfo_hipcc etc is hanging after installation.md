# rocminfo/hipcc etc is hanging after installation

- **Issue #:** 1576
- **State:** closed
- **Created:** 2021-09-24T04:13:38Z
- **Updated:** 2021-10-06T02:18:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1576

Hi, I installed latest Rocm (it shows as version 4.3.0) in Ubuntu 20.04.1 LTS. After this if I do "rocminfo" it just hangs after saying "ROCk module is loaded" , executing anything else also results the same, for example

rocminfo --help
ROCk module is loaded
^C

rocminfo --version
ROCk module is loaded
^C

I have not seen any alarming message while installing rocm (sudo apt install rocm-dkms). 

Any clue? 
