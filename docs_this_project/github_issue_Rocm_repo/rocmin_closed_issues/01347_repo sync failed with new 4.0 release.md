# repo sync failed with new 4.0 release

- **Issue #:** 1347
- **State:** closed
- **Created:** 2020-12-19T20:58:26Z
- **Updated:** 2020-12-23T05:57:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1347

Issue #1. 
Documentation still refers to 3.10.x. The version is static, therefore it appears to be forgotten whenever new release is launched. The newest source download therefore is always guessing game.
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code

Issue #2. 
this appears successful:
 ~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-4.0.x 

Once I did repo sync, it failed: 

repo sync
Traceback (most recent call last):
  File "/root/ROCm/.repo/repo/main.py", line 56, in <module>
    from subcmds.version import Version
  File "/root/ROCm/.repo/repo/subcmds/__init__.py", line 38, in <module>
    ['%s' % name])
  File "/root/ROCm/.repo/repo/subcmds/upload.py", line 27, in <module>
    from hooks import RepoHook
  File "/root/ROCm/.repo/repo/hooks.py", line 472
    file=sys.stderr)
        ^
