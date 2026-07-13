# Amd ROCm install problems

- **Issue #:** 884
- **State:** closed
- **Created:** 2019-09-12T07:30:51Z
- **Updated:** 2021-07-09T08:05:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/884

     Hi  Rocm Team,

     I 'm new with Amd ROCm drivers. In the old times I was able to run computing applications with catalsty drivers. 
***Using Ubuntu 16.04 full updated and upgraded.
     
     I cant install ROCm.  Have some problems in commands or in the repositorys??????

     I tried to install the ROCm driver in ubuntu,  following the guide on the page:
     
  ''Ubuntu Support - installing from a Debian repository''
The following directions show how to install ROCm on supported Debian-based systems such as Ubuntu 18.04. These directions may not work as written on unsupported Debian-based distributions. For example, newer versions of Ubuntu may not be compatible with the rock-dkms kernel driver. As such, users may want to skip the rocm-dkms and rock-dkms packages, as described above, and instead use the upstream kernel driver.

  *First make sure your system is up to date
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot

  *Add the ROCm apt repository
    For Debian-based systems like Ubuntu, configure the Debian ROCm repository as follows:
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key
sudo apt-key add - echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main'
sudo tee /etc/apt/sources.list.d/rocm.list

I typed in terminal:

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key 

******this command ABOVE work right, got and showed the key numbers in terminal.

***The next command BELOW dont work,   after I typed it,,  dont show nothing,, still stuck.........''

sudo apt-key add - echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main'

What is happening?????
What I need to do??

Please, If have a more right way to install ROCm in ubuntu, talk to me, I 'm trying many times with no success.  I have one RX Vega 56 (Vega 10), and I will get a new RX Vega 64 too!!

I appreciated all help.
