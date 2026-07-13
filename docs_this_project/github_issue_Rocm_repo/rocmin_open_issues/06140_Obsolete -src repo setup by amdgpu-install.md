# Obsolete -src repo setup by amdgpu-install 

- **Issue #:** 6140
- **State:** open
- **Created:** 2026-04-11T00:14:38Z
- **Updated:** 2026-05-13T16:50:07Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6140

Installing the `amdgpu-install` package gives a repo file `/etc/yum.repos.d/amdgpu.repo` with the repository definition of:

```
[amdgpu-src]
name=AMDGPU 30.30.1 repository
baseurl=https://repo.radeon.com/amdgpu/30.30.1/el/$amdgpudistro/main/source
enabled=0
gpgcheck=1
gpgkey=file:///etc/amdgpu-install/rocm.gpg.key
```

However, when attempting to use said repository it reports back a 404 error:
```
dnf --repo=amdgpu-src list available
AMDGPU 30.30.1 repository                                                                                                                                                                                       
Errors during downloading metadata for repository 'amdgpu-src':
  - Status code: 404 for https://repo.radeon.com/amdgpu/30.30.1/el/9.7/main/source/repodata/repomd.xml
Error: Failed to download metadata for repo 'amdgpu-src': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```
I checked the index listing and it seems source is not there like x86_64 as an option https://repo.radeon.com/amdgpu/30.30/el/9.7/main/

Is this repository meant to be there and if so can this be fixed? Sorry in advance if this is not the place to file this issue. 