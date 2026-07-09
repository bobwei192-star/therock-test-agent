# llc path error at hipconfig

- **Issue #:** 297
- **State:** closed
- **Created:** 2018-01-04T10:01:42Z
- **Updated:** 2018-06-03T15:42:12Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/297

rocm1.7
hipconfig line 132 :system("$HCC_HOME/compiler/bin/llc --version");
need change to : system("$HCC_HOME/bin/llc --version");