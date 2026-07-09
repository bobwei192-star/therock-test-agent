# Port `roc-obj-*` utilities over to Windows (and install with the HIP SDK)

- **Issue #:** 2396
- **State:** closed
- **Created:** 2023-08-22T10:52:16Z
- **Updated:** 2024-03-31T14:01:30Z
- **Assignees:** david-salinas, kzhuravl
- **URL:** https://github.com/ROCm/ROCm/issues/2396

These Perl utilities occasionally call into Linux utilities like `dd` which clearly don't exist on Windows.

Please port them to work on Windows.