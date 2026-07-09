# Error in manifest file for ROCm 2.2

- **Issue #:** 733
- **State:** closed
- **Created:** 2019-03-13T16:57:02Z
- **Updated:** 2019-03-13T20:56:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/733

The contents of default.xml seem to be almost duplicated, causing a parsing error when checking out with repo, when the parser encounters a second xml declaration in the middle of the manifest block:
```
fatal: manifest 'default.xml' not available
fatal: error parsing manifest /home/fstokes/build/ROCm-2.2/.repo/manifests/default.xml: XML or text declaration not at start of entity: line 57, column 0
```