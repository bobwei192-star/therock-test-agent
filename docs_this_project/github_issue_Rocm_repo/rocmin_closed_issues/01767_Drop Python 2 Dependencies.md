# Drop Python 2 Dependencies

- **Issue #:** 1767
- **State:** closed
- **Created:** 2022-07-08T10:21:59Z
- **Updated:** 2024-07-29T20:59:04Z
- **Labels:** Under Investigation
- **Assignees:** saadrahim
- **URL:** https://github.com/ROCm/ROCm/issues/1767

Currently, various components of ROCm rely on Python 2 as a dependency. This is problematic, because Python 2 is discontinued and Linux distributions tend to no longer include it in the repositories of their current OS releases. ROCm should therefore work towards dropping Python 2 dependencies in all its components.