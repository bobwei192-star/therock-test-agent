# Warning: apt-key output should not be parsed (stdout is not a terminal)

> **Issue #958**
> **状态**: closed
> **创建时间**: 2019-12-05T19:28:30Z
> **更新时间**: 2019-12-05T23:02:40Z
> **关闭时间**: 2019-12-05T23:02:40Z
> **作者**: jonnyli
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/958

## 描述

I am having trouble adding the ROCm apt repository.

after entering:
```
wget -qO – http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | 
sudo apt-key add -echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | 
sudo tee /etc/apt/sources.list.d/rocm.list
```
The warning message starting with:
> Warning: apt-key output should not be parsed (stdout is not a terminal)

is outputted into the rocm.list file too.

Is there another way to add this repository?

I am on Ubuntu 19.10 if that is relevant

---

## 评论 (4 条)

### 评论 #1 — seesturm (2019-12-05T20:55:10Z)

I guess the instructions got broken with [this commit](https://github.com/RadeonOpenCompute/ROCm/commit/f0d15004a0c7fa61c87e014da347c9765f7cdcd9#diff-04c6e90faac2675aa89e2176d2eec7d8). Before this commit the instructions were
```shell
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```

---

### 评论 #2 — jonnyli (2019-12-05T21:52:53Z)

@seesturm the instructions you listed is the same, the issue is that apt-key is throwing a warning message implying this isn't a recommended approach. 


---

### 评论 #3 — dmcdougall (2019-12-05T22:04:52Z)

The irony here is that the "recommended approach" would need to parse the output of `apt-key` to get rid of the warning that says not to parse the output of `apt-key`.

We should probably just separate out the last step and instruct the user to manually add to the `rocm.list` file.

---

### 评论 #4 — jonnyli (2019-12-05T22:27:20Z)

@seesturm my bad.... I misread the lines. Still learning Linux...
So the first line is to download the gpg key and name it -
the second line is actually creating the list of the repo.
Is that right?

---
