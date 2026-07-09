# [Documentation]: Incorrect wget URL in Radeon docs

- **Issue #:** 5615
- **State:** closed
- **Created:** 2025-11-02T06:44:35Z
- **Updated:** 2025-11-04T15:31:27Z
- **Labels:** status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5615

### Description of errors

In the Radeon specific ROCm 7.1 install guide, the wget command points to an invalid repo path because the version number (7.1) is missing from the beggining of the URL.

### Attach any links, screenshots, or additional evidence you think will be helpful.

From the non radeon docs 
"wget https://repo.radeon.com/amdgpu-install/7.1/ubuntu/noble/amdgpu-install_7.1.70100-1_all.deb"

From the radeon docs
"wget https://repo.radeon.com/amdgpu-install/ubuntu/noble/amdgpu-install_7.1.70100-1_all.deb"