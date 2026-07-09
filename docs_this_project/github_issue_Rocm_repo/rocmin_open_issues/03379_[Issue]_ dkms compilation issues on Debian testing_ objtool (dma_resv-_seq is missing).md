# [Issue]: dkms compilation issues on Debian testing: objtool (dma_resv->seq is missing)

- **Issue #:** 3379
- **State:** open
- **Created:** 2024-06-29T15:03:04Z
- **Updated:** 2025-06-03T01:29:33Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3379

When compiling rocm with the stock kernel (6.8.12) from Debian testing the following error appears

```
DKMS make.log for amdgpu-6.7.0-1781449.22.04 for kernel 6.8.12-amd64 (amd64)
/tmp/amd.A0EtTvUI/Makefile:52: *** dma_resv->seq is missing. exit....  Stop.
```

However I believe this error message is misleading. The amdgpu-dkms ./configure logs show that basically all checks fail due to:
`objtool: SRCARCH variable not defined ` thus the autoconf check `AC_AMDGPU_DMA_RESV_FENCES` fails because of the build error from objtool and not because of the check. This check sets `HAVE_DMA_RESV_SEQ_BUG`, which is why the dkms builds on recent Debian fails with `dma_resv->seq is missing`.

Newer kernel build tools on Debian (linux-kbuild-6.*) ship multiple objtools:
```
/usr/lib/linux-kbuild-6.8.12/tools/objtool/objtool
/usr/lib/linux-kbuild-6.8.12/tools/objtool/objtool.real-powerpc
/usr/lib/linux-kbuild-6.8.12/tools/objtool/objtool.real-x86
```

where `objtool` expects an environment variable `SRCARCH` to be set to `x86`, otherwise it fails.

I guess somewhere in the autoconf/configure scripts this SRCARCH needs to be properly set to build on recent Debian.

As a workaround you can rename `objtool.real-x86` to `objtool` unless you want to cross-compile.


OS: Debian Testing
ROCM: 6.1.1 & 6.1.2