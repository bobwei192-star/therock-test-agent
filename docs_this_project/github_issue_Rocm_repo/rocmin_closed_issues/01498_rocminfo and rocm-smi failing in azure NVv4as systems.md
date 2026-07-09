# rocminfo and rocm-smi failing in azure NVv4as systems 

- **Issue #:** 1498
- **State:** closed
- **Created:** 2021-06-22T11:51:25Z
- **Updated:** 2024-03-27T05:55:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1498

Hey

I've installed ROCm pn the system, however running basic ROCm commands give me errors as shown below.

System details : 
Ubuntu 18.04 LTS
kernel : 5.4
Azure size : Standard NV4as_v4 (4 vcpus, 14 GiB memory)


azureuser@mi25:/proc$ rocminfo
ROCk module is NOT loaded, possibly no GPU devices
azureuser@mi25:/proc$ rocm-smi
ERROR:root:Driver not initialized (amdgpu not found in modules)

The Output of lshw is as shown below

![image](https://user-images.githubusercontent.com/21343683/122918760-17498900-d37d-11eb-9a95-cce9a94bfea7.png)

The Output of lspci is below

![image](https://user-images.githubusercontent.com/21343683/122918919-465ffa80-d37d-11eb-9f96-72ef56952f4b.png)

I'm not sure what's going wrong, I'm fairly sure I've followed the installation steps accurately and have tried reinstalling it as well.

