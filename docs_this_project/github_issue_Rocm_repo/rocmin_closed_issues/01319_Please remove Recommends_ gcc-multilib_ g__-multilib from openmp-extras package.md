# Please remove Recommends: gcc-multilib, g++-multilib from openmp-extras package

- **Issue #:** 1319
- **State:** closed
- **Created:** 2020-12-04T01:50:36Z
- **Updated:** 2020-12-09T09:24:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1319

ROCm 3.10

```
$ apt-cache show openmp-extras3.10.0 | grep Recommends
Recommends: gcc, g++, gcc-multilib, g++-multilib
$
```

This is unnecessary. And AFAIK doesn't enhance the package in anyway.

Use instead:

```
Suggests: gcc, g++
```


that is without `gcc-multilib` (which does for example conflict with `gcc-10-i686-linux-gnu` for cross-compiling), and downgrade to `Suggests`.

There is nothing in this package that interact with GCC in anyway, nor is GCC interacting with anything in this package.

