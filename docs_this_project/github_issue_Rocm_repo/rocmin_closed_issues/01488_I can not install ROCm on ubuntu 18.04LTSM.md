# I can not install ROCm on ubuntu 18.04LTSM

- **Issue #:** 1488
- **State:** closed
- **Created:** 2021-06-03T12:28:37Z
- **Updated:** 2021-06-07T04:19:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1488

I do this way :
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt install rocm-dkms
      Reading package lists... Done
      Building dependency tree       
      Reading state information... Done
      Some packages could not be installed. This may mean that you have
      requested an impossible situation or if you are using the unstable
      distribution that some required packages have not yet been created
      or been moved out of Incoming.
      The following information may help to resolve the situation:
      
      The following packages have unmet dependencies:
       rocm-dkms : Depends: rocm-dev but it is not going to be installed
      E: Unable to correct problems, you have held broken packages.

how can i solved this problems?