# ubuntu & tensorflow-rocm & anaconda 

> **Issue #1290**
> **状态**: closed
> **创建时间**: 2020-11-13T15:36:36Z
> **更新时间**: 2020-11-18T17:26:30Z
> **关闭时间**: 2020-11-18T17:26:30Z
> **作者**: YuriyTigiev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1290

## 描述

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

---

## 评论 (6 条)

### 评论 #1 — iHandle (2020-11-15T02:20:31Z)

Activate your anaconda environment, then `pip install tensorflow-rocm`.

---

### 评论 #2 — YuriyTigiev (2020-11-15T07:04:58Z)

Is it enough to install the tensorflow-rocm or I also should install the tensorflow? for simple code
Should I used 
`import tensorflow-rocm as tf`  instead of ` import tensorflow as tf` ?


---

### 评论 #3 — iHandle (2020-11-15T08:47:26Z)

> Is it enough to install the tensorflow-rocm or I also should install the tensorflow? for simple code
> Should I used
> `import tensorflow-rocm as tf` instead of ` import tensorflow as tf` ?

It is enough to install just the `tensorflow-rocm`. Actually, I think there will be something wrong if you install both.

`import tensorflow as tf` is the correct way to import.

---

### 评论 #4 — rkothako (2020-11-16T06:05:48Z)

Yes, actually need to install tf as **conda install tenorflow-rocm** in anaconda environment.
And then launch tf as **import tensorflow as tf**.

---

### 评论 #5 — rkothako (2020-11-16T06:57:09Z)

Hi @YuriyTigiev 
Request to close this ticket if the answers are helpful.
Thank you.

---

### 评论 #6 — ROCmSupport (2020-11-18T07:15:50Z)

Hi @YuriyTigiev
Request to close this ticket now.
Thank you.

---
