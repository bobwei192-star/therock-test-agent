# rcprof for OpenCL applications: support, documentation, and issues

- **Issue #:** 163
- **State:** closed
- **Created:** 2017-07-17T15:08:24Z
- **Updated:** 2018-06-03T14:47:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/163

rcprof seems to be missing explicit OpenCL support; I'm aware that the runtimes are changing/merging, but it's not immediately obvious (nor seems to be documented) why the options `-t`  `-p` `-O` don't work and throw errors like the following:
```
libRCPCLOccupancyAgent.so is missing
Make sure you have libRCPCLOccupancyAgent.so under /opt/rocm/profiler/bin/
No profile mode specified. Nothing will be done.
```

Now, the HSA profiling modes do generate some data, but:
- `rcprof -A` often hangs and never finishes
- `rcprof -a foo.atp -T` generates some data, but a lot of it is HSA api data or related memory leak warnings that I never asked for nor do I know how to interpret
- `rcprof -C` keeps throwing the errors below (possibly for every kernel invocation)

I've attached some output from GROMACS test runs which illustrate both the hanging, dump of HSA API trace: https://goo.gl/oT52xL