# Vega 56/64 overclock/undervolt under ROCm and upstream Linux kernels in Ubuntu 16.04/18.04 [How-to]

- **Issue #:** 463
- **State:** closed
- **Created:** 2018-07-22T09:38:11Z
- **Updated:** 2018-12-31T23:14:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/463

Hello,
I want to share with you some information on how to overclock/undervolt GFX9 GPUs (Vega 56/Vega 64) under Ubuntu 16.04 and 18.04:

- Install updates:
```
sudo apt update && sudo apt dist-upgrade -y
sudo reboot
```

- Install ROCm https://github.com/RadeonOpenCompute/ROCm:
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install libnuma-dev 
sudo apt install rocm-dkms
sudo usermod -a -G video $LOGNAME 
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules
sudo reboot
```
If you have problems with the standard installation of rocm-dkms, install it **without rocm-dkms and rock-dkms packages**  _(verify packages list, it can vary)_:
```
sudo apt install comgr dkms hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rocm-clang-ocl rocm-dev rocm-device-libs rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo rocr_debug_agent
```
- Install additional packages:
```
sudo apt install git flex bison libssl-dev cmake libelf-dev libpci-dev pkg-config clinfo lm-sensors htop screen libjansson4 -y
```

- Install M-Bab's kernel https://github.com/M-Bab/linux-kernel-amdgpu-binaries:
```
git --git-dir=/dev/null clone --depth=1 https://github.com/M-Bab/linux-kernel-amdgpu-binaries
cd linux-kernel-amdgpu-binaries
sudo dpkg -i linux-headers*ubuntu*.deb linux-image*ubuntu*.deb firmware-radeon-ucode_*_all.deb
sudo reboot
```

- **(Optional, only if you have problems with M-Bab's kernel)** Compile ROCK-Kernel-Driver (fkxamd/drm-next-wip branch or master branch) and install it:
```
git clone --depth 1 https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver -b fkxamd/drm-next-wip
cd ROCK-Kernel-Driver 
cp /boot/config-`uname -r` .config
yes '' | make oldconfig
make -j `getconf _NPROCESSORS_ONLN` deb-pkg LOCALVERSION=-fxkamd
dpkg -i *deb
sudo reboot
```

- **(Obsolete, ROCm 1.9 is ABI compatible with KFD in upstream Linux kernels)** Compile ROCT-Thunk-Interface (fxkamd/drm-next-wip branch or master branch) and replace original ROCm libhsakmt.so* binaries (or remove all files from /opt/rocm/libhsakmt/lib/ and put compiled files to this folder):
```
git clone --depth 1 https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface -b fxkamd/drm-next-wip
cd ROCT-Thunk-Interface
mkdir -p build
cd build
cmake ..
make
sudo cp -a /opt/rocm/libhsakmt/lib/ /opt/rocm/libhsakmt/lib.bak
sudo cp libhsakmt.so* /opt/rocm/libhsakmt/lib
sudo reboot
```

- Edit grub GRUB_CMDLINE_LINUX_DEFAULT:
```
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram"
sudo update-grub
sudo reboot
```

- Try overclock/undervolt:
```
sudo -i

# Allow manual mode:
echo "manual"> /sys/class/drm/card0/device/power_dpm_force_performance_level

# GPU Clock/Voltage:
# echo "s $STATE_INT $MHz $mVOLT"> /sys/class/drm/card0/device/pp_od_clk_voltage
# for example: 
echo "s 5 1650 960"> /sys/class/drm/card0/device/pp_od_clk_voltage

# HBM2 Memory Clock/Votage:
# echo "m $STATE_INT $MHz $mVOLT"> /sys/class/drm/card0/device/pp_od_clk_voltage
# for example: 
echo "m 3 1015 950"> /sys/class/drm/card0/device/pp_od_clk_voltage

# Check clocks/states
cat /sys/class/drm/card0/device/pp_od_clk_voltage

# Save changes
echo "c"> /sys/class/drm/card0/device/pp_od_clk_voltage 
```
If you want to thank me - please send some BTC **3JS1m8XSvS4fcprByLRuMjjjuck9dne4rm**

Thanks to everyone who shared interesting information on the web.

Please share your experience with other, maybe our world become less hot and more productive )