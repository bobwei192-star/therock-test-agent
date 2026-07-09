# Create a github issue template with instruction how to provide system information

- **Issue #:** 1305
- **State:** closed
- **Created:** 2020-11-25T20:22:01Z
- **Updated:** 2020-12-16T17:06:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1305

For Debian / Ubuntu based systems here is my recommended template:

* Distribution and version (`lsb_release -a`)
* GPU used
  * Attach output of `sudo lspci -vvv`
* CPU used: `lscpu`
* Kernel and system version: `uname -a`
* Installed kernels: `dpkg -l | egrep "linux-image|firmware-amd-graphics|dkms"`
* Used repositories: `grep -rH radeon /etc/apt/sources.list.d/`
* Installed relevant packages: `dpkg -l | egrep "roc[mkrt]|hsa|\bhip|opencl|clinfo|llvm" | awk '{print $1, $2, $3;}'`
* If `inxi` is installed, most of the above can be replaced by output of `inxi -SMCGrsxxz`
* Kernel modules: `sudo dkms status`
* Information if you previously had any other ROCm version installed on this system
* ROCm related information:
```sh
ls -l /opt/rocm*
/opt/rocm/bin/rocminfo
/opt/rocm/bin/rocm-smi
/opt/rocm/opencl/bin/clinfo
/opt/rocm/bin/rocm-bandwidth-test
/opt/rocm/bin/rocm-bandwidth-test -t
/opt/rocm/bin/hipconfig
pip3 list | egrep 'tensor|rocm'
```
* `sudo dmesg > dmesg.txt`
  * (Upload the `dmesg.txt` file as attachment to this issue. It is good idea to grab it soon after reboot or after experiencing an issue that you are reporting. If the dmesg doesn't contain all the information check `/var/log/kern.log*` files.)
* `/usr/bin/clinfo` (if installed)
* `grep -rH . /etc/ld.so.conf.d/`
* `/sbin/ldconfig -p | grep -i rocm`
* `ls -l /dev/kfd /dev/dri/card* /dev/dri/render*`
* As normal user: `groups`
* `grep -rH . /etc/OpenCL/vendors/`
* Environment variables used (as normal user and as root - do not use `sudo` here!):
  * `echo -e "PATH=$PATH\nROCM_PATH=$ROCM_PATH\nLD_LIBRARY_PATH=$LD_LIBRARY_PATH\nLD_PRELOAD=$LD_PRELOAD\nOCL_ICD_VENDORS=$OCL_ICD_VENDORS\nOCL_ICD_FILENAMES=$OCL_ICD_FILENAMES"
`
* `find /etc/OpenCL/vendors/ -name '*.icd' | while read OPENCL_VENDOR_PATH ; do clinfo -l > /dev/null ; echo "$? ${OPENCL_VENDOR_PATH}" ; done`

If any of the above fails, please include the full output (including invocation) of error message received.

**Note**: If using versioned pacakges, replace `/opt/rocm` with a proper path, like `/opt/rocm-3.9.0`. **Include the used path in the issue text.** Other option is to ensure there is a symbolic link, i.e. `sudo ln -s /opt/rocm-* /opt/rocm`.

