# repo sync failure

- **Issue #:** 983
- **State:** closed
- **Created:** 2019-12-23T17:45:26Z
- **Updated:** 2023-12-18T15:53:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/983

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
