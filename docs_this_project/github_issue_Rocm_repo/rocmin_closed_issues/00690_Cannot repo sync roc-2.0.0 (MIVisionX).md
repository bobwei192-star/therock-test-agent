# Cannot repo sync roc-2.0.0 (MIVisionX)

- **Issue #:** 690
- **State:** closed
- **Created:** 2019-01-26T10:25:01Z
- **Updated:** 2019-01-29T18:10:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/690

When following the instructions for roc-2.0.0 "repo sync" fails at fetching the MIVisionX repository. In default.xml revision points to "1.0.0", but no such branch exists.

Changing revision to "refs/tags/1.0.0" makes "repo sync" succeed. I'm using repo tool version v1.12.37.