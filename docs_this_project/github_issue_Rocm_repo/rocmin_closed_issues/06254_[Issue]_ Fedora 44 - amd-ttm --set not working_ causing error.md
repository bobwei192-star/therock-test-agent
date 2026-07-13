# [Issue]: Fedora 44 - amd-ttm --set not working, causing error

- **Issue #:** 6254
- **State:** closed
- **Created:** 2026-05-13T13:08:54Z
- **Updated:** 2026-05-13T16:14:37Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6254

### Problem Description

Fedora 44 - amd-ttm --set 100 not working, causing error as below?


darren@fedora:~$ amd-ttm --set 100
🐧 Successfully set TTM pages limit to 26214400 pages (100.00 GB)
🐧 Configuration written to /etc/modprobe.d/ttm.conf
○ NOTE: You need to reboot for changes to take effect.
Would you like to reboot the system now? (y/n): y
Traceback (most recent call last):
  File "/home/darren/.local/bin/amd-ttm", line 6, in <module>
    sys.exit(amd_ttm())
             ~~~~~~~^^
  File "/home/darren/.local/share/pipx/venvs/amd-debug-tools/lib64/python3.14/site-packages/amd_debug/__init__.py", line 29, in amd_ttm
    return ttm.main()
           ~~~~~~~~^^
  File "/home/darren/.local/share/pipx/venvs/amd-debug-tools/lib64/python3.14/site-packages/amd_debug/ttm.py", line 150, in main
    ret = tool.set(args.set)
  File "/home/darren/.local/share/pipx/venvs/amd-debug-tools/lib64/python3.14/site-packages/amd_debug/ttm.py", line 101, in set
    return maybe_reboot()
  File "/home/darren/.local/share/pipx/venvs/amd-debug-tools/lib64/python3.14/site-packages/amd_debug/ttm.py", line 28, in maybe_reboot
    return reboot()
  File "/home/darren/.local/share/pipx/venvs/amd-debug-tools/lib64/python3.14/site-packages/amd_debug/common.py", line 276, in reboot
    loop = asyncio.get_event_loop()
  File "/usr/lib64/python3.14/asyncio/events.py", line 715, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.


### Operating System

Fedora 44

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

gfx1151 AMD Radeon 8060S Graphics  

### ROCm Version

7.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_