# wget failed to fetch ROCm packages

- **Issue #:** 1153
- **State:** closed
- **Created:** 2020-06-17T16:36:56Z
- **Updated:** 2020-06-17T18:00:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/1153

Hi, 

I have been trying to install rocm-kernel using the apt command on Ubuntu following the Quick Start Guide in https://rocmdocs.amd.com/en/latest/ROCm_Virtualization_Containers/quickstart.html. 

However, whenever I run the get command, the command seems to be stuck. So, I went to ping packages.amd.com and I notice there are no outputs. When I ping the same address on a Windows PC, I got "Request timed out." I am wondering if the quick start guide is out of date or if the link to the packages has changed. Would someone please advise? Thanks in advance.

The wget command I ran is: wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -

Also, I am not sure if this is the correct location for reporting an AMD site failure for ROCm. Please redirect me to the correct site if this is not relevant to ROCm.