# Missing tags for roc-2.2.0 cause repo sync failure

- **Issue #:** 737
- **State:** closed
- **Created:** 2019-03-14T13:14:21Z
- **Updated:** 2019-03-16T00:15:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/737

There is no `roc-2.2.0` tag in the `rocm_bandwidth_test`, `rocm_smi_lib`, and `roctracer`. In addition, revision `7ce124f86d0fa59387462fc09a49b25ccb81f96` doesn't seem to exist in the tree for `clang-ocl` on github. This causes `repo sync` to fail.