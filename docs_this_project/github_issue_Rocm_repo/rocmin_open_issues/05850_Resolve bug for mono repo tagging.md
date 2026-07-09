# Resolve bug for mono repo tagging

- **Issue #:** 5850
- **State:** open
- **Created:** 2026-01-12T12:56:13Z
- **Updated:** 2026-01-12T12:56:23Z
- **Assignees:** srayasam-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5850

**Current setup:** If there are multiple PR IDs in the commit message of the repo which belongs to super repos, ccurrently, we have the code to take the first PR ID.
**Resolution:**
We need to take the last PR ID of the commit message which means it is the latest PR so that we can tag with that particular commit ID in regard to PR ID.