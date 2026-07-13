# Not possible to build ROCm from source code

- **Issue #:** 1238
- **State:** closed
- **Created:** 2020-09-23T15:49:08Z
- **Updated:** 2020-10-14T12:31:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1238

System information

    OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Debian buster
    Python version: 3.7
    ROCm/MIOpen version: 3.8
    GPU model and memory: Vega 64

Describe the problem
Core components nor metapackages are not present when using the instructions below:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#downloading-the-rocm-source-code

Since the new deb packages depend on python 3.8, you have blocked the possibility to all Debian buster users.
Since you don't have older versions in your repository, we can't downgrade to 3.7.
Since your instructions to build the library from source are not working we are totally stuck.

    Do we have any way (apart from reinstall a new OS) to have a working system?
