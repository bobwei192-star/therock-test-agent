# ROCk module is NOT loaded, possibly no GPU devices

- **Issue #:** 1506
- **State:** closed
- **Created:** 2021-06-25T18:47:40Z
- **Updated:** 2021-07-27T12:06:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1506

I have tried to install ROCm in my pc which has AMD Radeon (TM)RX Vega 10 Graphics as my GPU using steps provided in
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu website 
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms
groups
sudo usermod -a -G video $LOGNAME
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
reboot
when i excute these command 
/opt/rocm/bin/rocminfo
I am getting 
ROCk module is NOT loaded, possibly no GPU devices
and when I excute 
/opt/rocm/opencl/bin/x86_64/clinf command
i am getting error    as
 bash: /opt/rocm/opencl/bin/x86_64/clinfo: No such file or directory
but facing these errors can you people please help me with these error.
