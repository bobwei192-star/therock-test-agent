# [Documentation] Explicit tensorflow wheel naming convention for installation

- **Issue #:** 2327
- **State:** closed
- **Created:** 2023-07-21T15:21:23Z
- **Updated:** 2024-10-01T16:59:36Z
- **Labels:** Documentation
- **Assignees:** sunway513
- **URL:** https://github.com/ROCm/ROCm/issues/2327

The compatibility matrix between Tensorflow and ROCm is indicated in : 
https://rocm.docs.amd.com/en/latest/release/3rd_party_support_matrix.html

Nevertheless it might not be obvious that the wheel naming convention is TFversion.0.ROCmversion which might lead user to install Tensorflow wheel for not the right ROCm version.

On https://rocm.docs.amd.com/en/latest/how_to/tensorflow_install/tensorflow_install.html , it is indicated : 
For details on tensorflow-rocm wheels and ROCm version compatibility, see:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md
which is much more explicit but did not contain the latest compatibility matrix. (i.e ROCm 5.6 & Tensorflow 2.12)
