# [Issue]: gfx120X-all: rocm-sdk init searches for hipblas.dll in wrong folder

- **Issue #:** 5885
- **State:** closed
- **Created:** 2026-01-22T18:30:57Z
- **Updated:** 2026-02-02T19:21:34Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5885

### Problem Description

While trying to compile bitsandbytes, I created a venv, then:
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/ torch torchaudio torchvision
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/ "rocm[libraries,devel]"

At  "rocm-sdk init" it throws this error:
(venv) J:\ComfyUI\bitsandbytes\bnb\venv\Scripts>rocm-sdk init
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Scripts\rocm-sdk.exe\__main__.py", line 7, in <module>
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Lib\site-packages\rocm_sdk\__main__.py", line 150, in main
    args.func(args)
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Lib\site-packages\rocm_sdk\__main__.py", line 43, in _do_init
    root_path = _devel.get_devel_root()
                ^^^^^^^^^^^^^^^^^^^^^^^
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Lib\site-packages\rocm_sdk\_devel.py", line 63, in get_devel_root
    _expand_devel_contents(rocm_sdk_devel_path, site_lib_path)
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Lib\site-packages\rocm_sdk\_devel.py", line 154, in _expand_devel_contents
    _lock_and_expand(
  File "J:\ComfyUI\bitsandbytes\bnb\venv\Lib\site-packages\rocm_sdk\_devel.py", line 208, in _lock_and_expand
    dest_path.hardlink_to(hardlink_target)
  File "C:\Users\Wildfire\AppData\Local\Programs\Python\Python312\Lib\pathlib.py", line 1396, in hardlink_to
    os.link(target, self)
FileNotFoundError: [WinError 3] Das System kann den angegebenen Pfad nicht finden: 'J:\\ComfyUI\\bitsandbytes\\bnb\\venv\\Lib\\site-packages\\_rocm_sdk_devel\\bin\\..\\..\\_rocm_sdk_libraries_gfx1151\\bin\\hipblas.dll' -> 'J:\\ComfyUI\\bitsandbytes\\bnb\\venv\\Lib\\site-packages\\_rocm_sdk_devel\\bin\\hipblas.dll'

To workaround this issue, you have to rename _rocm_sdk_libraries_gfx120X-all to _rocm_sdk_libraries_gfx1151.

### Operating System

Windows 11

### CPU

AMD Ryzen 9 9900

### GPU

AMD RX 9060 XT

### ROCm Version

/.1

### ROCm Component

_No response_

### Steps to Reproduce

pip install --index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/ torch torchaudio torchvision
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx120X-all/ "rocm[libraries,devel]"

rocm-sdk init

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_