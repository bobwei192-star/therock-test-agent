# aqlprofiles and opencl-icd-loaders build will fail on rpm-based systems, …

- **Issue #:** 3868
- **State:** closed
- **Created:** 2024-10-06T13:17:16Z
- **Updated:** 2025-06-26T14:31:00Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3868

… even the supported ones.
Hi,
while my studies of the build_*.sh scrpits I found these two mentioned above.
Both seem to be binary only packages and the precompiled binaries are only distributed as deb for the supported incarnations of Ubuntu, but when building under RHEL or SLES this packages will fail, hence there is no building path which leads to success. Three reasons for that:
1. These systems will fail the implemented distro check
2.  In regular, they won't have dpkg installed.
3. It is not known which deb to choose to meet the versions of dependencies

Is it possible to provide the binary blobs as tar-balls and repack it after checking which package management is used?

Here are my suggestions for those checks:

```bash
isDpkgAvail(){
  if  [ "" != $(which dpkg) ]; then
    return 0
 else
    return -1
  fi
}

isRpmAvail(){
  if [ "" != $(which rpm) ]; then
    return 0
  else
    return -1
  fi
}
```
