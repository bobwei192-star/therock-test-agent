# ROCm Data Center Tool incorrect RHEL9 package version

- **Issue #:** 4089
- **State:** closed
- **Created:** 2024-12-03T22:20:00Z
- **Updated:** 2024-12-03T22:59:36Z
- **Labels:** Verified Issue, ROCm 6.2.0, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4089

In previous versions of ROCm Data Center Tool (RDC) included with ROCm 6.2 for RHEL9, RDC’s version number was incorrectly set to 1.0.0. ROCm 6.3 includes RDC with the correct version number.

>[!IMPORTANT]
>If you’re using RHEL9, you must first uninstall the existing ROCm 6.2 RDC 1.0.0 package with `sudo yum remove rdc` before upgrading to the ROCm 6.3 RDC package `sudo yum install rdc`.