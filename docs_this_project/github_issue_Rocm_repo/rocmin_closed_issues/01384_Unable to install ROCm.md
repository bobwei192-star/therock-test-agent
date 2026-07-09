# Unable to install ROCm

- **Issue #:** 1384
- **State:** closed
- **Created:** 2021-02-18T15:13:48Z
- **Updated:** 2022-09-17T03:17:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1384

Hi, 

I hope it is not a copy of another issue, i've been searching for days for the solution.

After installing/uninstalling several times ROCm 4.0 on Ubuntu 20.04.2 TLS (kernel 5.4), I always come to the same issue:
<pre><font color="#4E9A06"><b>hugo@hugo-HP-ZBook-15u-G6</b></font>:<font color="#3465A4"><b>~</b></font>$ /opt/rocm/bin/rocminfo 
<font color="#CC0000">ROCk module is NOT loaded, possibly no GPU devices</font>
<font color="#CC0000">Unable to open /dev/kfd read-write: No such file or directory</font>
<font color="#D3D7CF">hugo is member of video group</font>
<font color="#CC0000">hsa api call failure at: /src/rocminfo/rocminfo.cc:1142</font>
<font color="#CC0000">Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.</font>
</pre>

I have a AMD Radeon Pro WX3200, which uses a Polaris 12 (which is in the list of supported GPU)

Does anyone has a solution for such issue?