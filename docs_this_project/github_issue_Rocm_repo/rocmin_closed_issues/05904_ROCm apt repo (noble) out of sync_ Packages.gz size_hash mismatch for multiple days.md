# ROCm apt repo (noble) out of sync: Packages.gz size/hash mismatch for multiple days

- **Issue #:** 5904
- **State:** closed
- **Created:** 2026-01-26T13:48:36Z
- **Updated:** 2026-01-27T19:18:16Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5904

NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name      : AMD Ryzen 7 5700X3D 8-Core Processor
GPU:
  Name:                    AMD Ryzen 7 5700X3D 8-Core Processor
  Marketing Name:          AMD Ryzen 7 5700X3D 8-Core Processor
  Name:                    gfx1201                            
  Marketing Name:          AMD Radeon RX 9070 XT              
      Name:                    amdgcn-amd-amdhsa--gfx1201         
      Name:                    amdgcn-amd-amdhsa--gfx12-generic  


Reproducible for 3+ days, same behaviour after clearing apt lists and from different update runs.


you can see bellow : 

Err:25 https://repo.radeon.com/rocm/apt/latest noble/main amd64 Packages
  File has unexpected size (62798 != 60911). Mirror sync in progress? [IP: 23.44.215.171 443]
  Hashes of expected file:
   - Filesize:60911 [weak]
   - SHA256:a21e883477e4f1b79c31c9334e86c88ab3db5811922331fddd81e493666e0406
   - SHA1:f5468913de65867b9181d16ce56a5dad84272f4b [weak]
   - MD5Sum:5c1137d1ebf2fa64c71ad64904f4ce61 [weak]
  Release file created at: Tue, 13 Jan 2026 02:19:55 +0000
Get:26 https://packages.mozilla.org/apt mozilla InRelease [1,520 B]
Get:27 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [21.5 kB]
Get:28 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]
Get:29 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [74.1 kB]
Get:30 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]
Get:31 https://packages.mozilla.org/apt mozilla/main all Packages [5,111 kB]
Get:32 https://packages.mozilla.org/apt mozilla/main amd64 Packages [99.4 kB]
Fetched 6,302 kB in 3s (2,061 kB/s)
Reading package lists... Done
N: Repository 'https://repo.radeon.com/rocm/apt/latest noble InRelease' changed its 'Version' value from '7.1.1' to '7.2'
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository
   'https://repo.radeon.com/rocm/apt/latest noble InRelease' does not support architecture 'i386'
E: Failed to fetch https://repo.radeon.com/rocm/apt/latest/dists/noble/main/binary-amd64/Packages.gz
   File has unexpected size (62798 != 60911). Mirror sync in progress? [IP: 23.44.215.171 443]
   Hashes of expected file:
    - Filesize:60911 [weak]
    - SHA256:a21e883477e4f1b79c31c9334e86c88ab3db5811922331fddd81e493666e0406
    - SHA1:f5468913de65867b9181d16ce56a5dad84272f4b [weak]
    - MD5Sum:5c1137d1ebf2fa64c71ad64904f4ce61 [weak]
   Release file created at: Tue, 13 Jan 2026 02:19:55 +0000
E: Some index files failed to download. They have been ignored, or old ones used instead.


