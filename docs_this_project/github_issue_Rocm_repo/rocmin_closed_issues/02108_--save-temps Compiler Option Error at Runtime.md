# --save-temps Compiler Option Error at Runtime

- **Issue #:** 2108
- **State:** closed
- **Created:** 2023-05-04T08:14:23Z
- **Updated:** 2024-02-16T16:26:00Z
- **Labels:** Verified Issue, 5.4.3
- **URL:** https://github.com/ROCm/ROCm/issues/2108

This issue is ported from the release notes.

Some users may encounter a “Cannot find Symbol” error at runtime when using `--save-temps`. While most `--save-temps` use cases work correctly, this error may appear occasionally.

The known workaround is not to use `--save-temps` when the error appears. 