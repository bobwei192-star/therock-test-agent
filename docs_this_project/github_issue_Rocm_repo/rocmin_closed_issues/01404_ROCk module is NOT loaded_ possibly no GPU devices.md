# ROCk module is NOT loaded, possibly no GPU devices

- **Issue #:** 1404
- **State:** closed
- **Created:** 2021-03-12T08:33:24Z
- **Updated:** 2024-01-23T09:48:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/1404

I tried to install rocm packages in my machine，which is Ubuntu18.04.5LTS and has four 6900XT card. Why I do this is to handle the previous issue I proposed, which encountered when I try to run pytorch examples using rocm/pytorch. the link to previous issue is https://github.com/RadeonOpenCompute/ROCm/issues/1399

The steps I try this time is shown below, which follows the instructions in link https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md#rocm-installation
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms
sudo usermod -a -G video $LOGNAME
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf   
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
sudo reboot
/opt/rocm/bin/rocminfo
and I get the following optputs

ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
rocm is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

I find that some links say that 6900XT is not supported by ROCm?
Could someone please help me? or give me some advice? 
