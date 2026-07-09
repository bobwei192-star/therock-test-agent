# rocm-opencl fails to uninstall if /opt/rocm-3.10.0/lib doesn't exist

- **Issue #:** 1327
- **State:** closed
- **Created:** 2020-12-10T19:04:55Z
- **Updated:** 2024-01-18T03:30:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1327

If a user accidental removed stuff in `/opt`, it should still be possible to uninstall stuff and reinstall them.

But `prerm` script fails.

```
Removing rocm-opencl (3.6Beta-17-g875c1f8-rocm-rel-3.10-27) ...
rmdir: failed to remove '/opt/rocm-3.10.0/lib': No such file or directory
dpkg: error processing package rocm-opencl (--remove):
 installed rocm-opencl package pre-removal script subprocess returned error exit status 1
dpkg: too many errors, stopping
```

Debian testing. But applies to Ubuntu too.


`/var/lib/dpkg/info/rocm-opencl.prerm`:

```bash
#!/bin/bash

set -e

rm_ldconfig() {
  rm -f /etc/ld.so.conf.d/x86_64-rocm-opencl.conf && ldconfig
  rm -f /etc/OpenCL/vendors/amdocl64_31000.icd
}

case "$1" in
  purge)
  ;;
  remove)
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so.1
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so.1.2
    rmdir --ignore-fail-on-non-empty /opt/rocm-3.10.0/lib
    rmdir --ignore-fail-on-non-empty /opt/rocm-3.10.0
    rm_ldconfig
  ;;
  *)
    exit 0
  ;;
esac
```

I think adding `|| true` at the end of `rmdir` lines, maybe would be an option?

Also there is some not-so-pretty handling of some symlinks in `postinst`, that requires this ugly solution in `prerm`. A better way would be to embed these symlinks in the package content itself. This way it will also be removed automatically, and it will trigger `ldconfig` afaik automatically too (or can be configured to do so). It would simplify both `postinst` and `prerm`.
