# Warning with deprecated apt-key add and not using trusted.gpg.d

- **Issue #:** 1869
- **State:** closed
- **Created:** 2022-11-29T16:36:49Z
- **Updated:** 2024-02-01T20:59:42Z
- **Labels:** Verified Issue, 5.3.0, Documentation
- **Assignees:** frepaul
- **URL:** https://github.com/ROCm/ROCm/issues/1869

`apt-key add` is deprecated.

# Expected Behavior

The documentation should not suggest `wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -` at https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/How_to_Install_ROCm.html . I should not see any warning when adding or when running `apt update`. The key should be in `trusted.gpg.d` not `trusted.gpg`. This improves security by ensuring the key is not accidentally used for other repositories.

Something new like whatever `add-apt-repository` does should be used.

# Actual Behavior

```
# apt update
Hit:1 [...]
Fetched 48.9 kB in 1s (33.5 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
7 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://repo.radeon.com/amdgpu/22.10/ubuntu/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
W: https://repo.radeon.com/rocm/apt/5.3/dists/focal/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```