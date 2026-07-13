# HIPCC is not added to the system PATH by default

- **Issue #:** 2336
- **State:** open
- **Created:** 2023-07-27T15:23:12Z
- **Updated:** 2026-01-25T03:58:01Z
- **Labels:** Verified Issue, Windows, 5.5.1
- **URL:** https://github.com/ROCm/ROCm/issues/2336

 HIPCC can be used to compile and build applications using the AMD HIP SDK. HIPCC is not added to the system path due to security concerns. Values should be added to the PATH manually.
-	Add Hip SDK Hipcc path to System variables(path) C:\Program Files\AMD\ROCm\5.5\bin, this allows users to compile without providing absolute path.
-	Add HIP_ROCCLR_HOME = C:\Program Files\AMD\ROCm\5.5\, It Enables GPU Visibility to Hip based ISV’s/apps
