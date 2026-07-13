# ubuntu & tensorflow-rocm & anaconda 

- **Issue #:** 1290
- **State:** closed
- **Created:** 2020-11-13T15:36:36Z
- **Updated:** 2020-11-18T17:26:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1290

How to install a tensorflow-rocm for an anaconda? 
conda-install trying to use old version of tensorflow-rocm from the cloud.

```
(ML) yuriy@PC-Ubuntu:~/Project$ conda install -c rocm tensorflow-rocm
Error processing line 1 of /home/yuriy/anaconda3/lib/python3.8/site-packages/google_auth-1.23.0-py3.8-nspkg.pth:

  Traceback (most recent call last):
    File "/home/yuriy/anaconda3/lib/python3.8/site.py", line 169, in addpackage
      exec(line)
    File "<string>", line 1, in <module>
    File "<frozen importlib._bootstrap>", line 553, in module_from_spec
  AttributeError: 'NoneType' object has no attribute 'loader'

Remainder of file ignored
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Solving environment: | 
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
failed                                                                                                                                                                                                     

UnsatisfiableError: The following specifications were found
to be incompatible with the existing python installation in your environment:

Specifications:

  - tensorflow-rocm -> python[version='2.7.*|3.6.*|3.5.*']

Your python: python=3.8

If python is on the left-most side of the chain, that's the version you've asked for.
When python appears to the right, that indicates that the thing on the left is somehow
not available for the python version you are constrained to. Note that conda will not
change your python version to a different minor version unless you explicitly specify
that.

```