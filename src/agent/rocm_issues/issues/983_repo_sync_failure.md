# repo sync failure

> **Issue #983**
> **状态**: closed
> **创建时间**: 2019-12-23T17:45:26Z
> **更新时间**: 2023-12-18T15:53:56Z
> **关闭时间**: 2023-12-18T15:53:55Z
> **作者**: TomSang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/983

## 描述

I met the following repo sync failure.  Does  anybody know how to fix it?

tom@tom0-hpz-24g:~/projs/amd/RadeonOpenCompute/rocm$ repo sync 
Traceback (most recent call last):
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/main.py", line 530, in <module>
    _Main(sys.argv[1:])
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/main.py", line 505, in _Main
    result = run()
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/main.py", line 498, in <lambda>
    run = lambda: repo._Run(name, gopts, argv) or 0
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/main.py", line 201, in _Run
    result = cmd.Execute(copts, cargs)
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/subcmds/sync.py", line 949, in Execute
    submodules_ok=opt.fetch_submodules)
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/command.py", line 169, in GetProjects
    for p in project.GetDerivedSubprojects())
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/project.py", line 2055, in GetDerivedSubprojects
    for rev, path, url in self._GetSubmodules():
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/project.py", line 2047, in _GetSubmodules
    return get_submodules(self.gitdir, rev)
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/project.py", line 1960, in get_submodules
    sub_paths, sub_urls = parse_gitmodules(gitdir, rev)
  File "/home/tom/projs/amd/RadeonOpenCompute/rocm/.repo/repo/project.py", line 1992, in parse_gitmodules
    os.write(fd, p.stdout)
TypeError: a bytes-like object is required, not 'str'


---

## 评论 (3 条)

### 评论 #1 — vladistan (2020-07-18T19:16:51Z)

I just started to have the same issue. My stack dump is exactly the same,  with the exception of home directory.  So  not posting it.   I believe it is related to recent repo tool / python upgrade and having left over python files in the project directory

---

### 评论 #2 — nartmada (2023-12-13T23:24:26Z)

Hi @tomsang, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #3 — nartmada (2023-12-18T15:53:55Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
