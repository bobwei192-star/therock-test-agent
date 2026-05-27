# unable to download repo source

> **Issue #1494**
> **状态**: closed
> **创建时间**: 2021-06-16T15:36:08Z
> **更新时间**: 2021-06-17T04:47:32Z
> **关闭时间**: 2021-06-17T04:47:31Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1494

## 描述

worked on earlier versions 4.1, 4.2 but not 4.3:
```

apt install curl -y && curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-4.3.x
~/bin/repo sync

```
Result:
```
Downloading Repo source from https://gerrit.googlesource.com/git-repo
remote: Counting objects: 11, done
remote: Finding sources: 100% (94/94)
remote: Total 94 (delta 48), reused 94 (delta 48)
Unpacking objects: 100% (94/94), done.
repo: Updating release signing keys to keyset ver 2.3
Downloading manifest from https://github.com/RadeonOpenCompute/ROCm.git
fatal: Couldn't find remote ref refs/heads/roc-4.3.x
manifests: sleeping 4.0 seconds before retrying
fatal: Couldn't find remote ref refs/heads/roc-4.3.x
fatal: cannot obtain manifest https://github.com/RadeonOpenCompute/ROCm.git
repo sync...
Traceback (most recent call last):
  File "/root/ROCm-4.3/.repo/repo/main.py", line 627, in <module>
    _Main(sys.argv[1:])
  File "/root/ROCm-4.3/.repo/repo/main.py", line 603, in _Main
    result = run()
  File "/root/ROCm-4.3/.repo/repo/main.py", line 596, in <lambda>
    run = lambda: repo._Run(name, gopts, argv) or 0
  File "/root/ROCm-4.3/.repo/repo/main.py", line 262, in _Run
    result = cmd.Execute(copts, cargs)
  File "/root/ROCm-4.3/.repo/repo/subcmds/sync.py", line 960, in Execute
    self._UpdateManifestProject(opt, mp, manifest_name)
  File "/root/ROCm-4.3/.repo/repo/subcmds/sync.py", line 876, in _UpdateManifestProject
    partial_clone_exclude=self.manifest.PartialCloneExclude)
  File "/root/ROCm-4.3/.repo/repo/project.py", line 1117, in Sync_NetworkHalf
    and self._ApplyCloneBundle(initial=is_new, quiet=quiet, verbose=verbose)):
  File "/root/ROCm-4.3/.repo/repo/project.py", line 2254, in _ApplyCloneBundle
    bundle_url = remote.url + '/clone.bundle'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
ROCm source is downloaded to /root/ROCm-4.3
push /root/ROCm-4.3 to get there...

```

---

## 评论 (2 条)

### 评论 #1 — xuhuisheng (2021-06-16T23:07:41Z)

The ROCm-4.3 haven't released yet. Please use roc-4.2.x right now.

---

### 评论 #2 — ROCmSupport (2021-06-17T04:47:31Z)

Thanks @gggh000 for reaching us out.
ROCm 4.3 is not released yet, it is expected to be released by end of this month. Please stay tuned.
Until then recommend to use 4.2 sources.
Thank you.

---
