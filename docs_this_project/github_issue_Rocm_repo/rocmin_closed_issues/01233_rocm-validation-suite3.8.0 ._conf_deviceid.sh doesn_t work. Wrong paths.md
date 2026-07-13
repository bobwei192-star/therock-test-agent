# rocm-validation-suite3.8.0 ./conf/deviceid.sh doesn't work. Wrong paths.

- **Issue #:** 1233
- **State:** closed
- **Created:** 2020-09-22T21:44:03Z
- **Updated:** 2024-01-19T20:15:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/1233

rocm-validation-suite3.8.0 3.4.30800

```
root@debian:/opt/rocm-3.8.0/rvs# ./conf/deviceid.sh 
./conf/deviceid.sh: line 99: /opt/rocm/rvs/rvs: No such file or directory
```

Providing `ROCM_PATH` environment variable doesn't help.

`RVS_EXE_PATH=/opt/rocm-3.8.0/rvs/rvs` appears to resolve the issue, but the script does nothing.

My suggestion:

1) Use proper paths by default.
2) Respect `ROCM_PATH`
3) Terminate script early (with error message and how to fix it) if the provided or computed `RVS_EXE_PATH` doesn't point to executable file that exists.
