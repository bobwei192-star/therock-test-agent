# ldconfig files deleted upon RPM upgrade/reinstall

> **Issue #534**
> **状态**: closed
> **创建时间**: 2018-09-15T00:42:02Z
> **更新时间**: 2019-03-12T12:19:22Z
> **关闭时间**: 2019-03-12T12:19:22Z
> **作者**: xw285cornell
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/534

## 描述

We just found an issue when upgrading or reinstalling the RPMs. The post-install script of the rpm says this: 

```
postuninstall scriptlet (using /bin/sh):
rm -f /etc/ld.so.conf.d/hsa-rocr-dev.conf && ldconfig
```

But when one upgrades (or re-installs) a RPM, that first installs the new one, runs the post-install scriplet, which will create the file, then it removes the old version, and runs the postuninstall scriplet. Therefore the ldconfig file is deleted. 

We think the postrun scriptlet should be something like: 

``` 
if [ $1 -eq 0]; then
  # the old script, like rm -f /etc/ld....
fi
```

---

## 评论 (3 条)

### 评论 #1 — kentrussell (2018-09-17T10:03:52Z)

Yeah this is something we hit with the ROCT as well, and was incredibly annoying to try to figure out. We used the same resolution that you suggested though. I'll see if we can get someone on the ROCr team to take a look at it.

---

### 评论 #2 — kentrussell (2018-09-25T11:13:13Z)

I've got a fix internally. Won't hit 1.9.1 but should be in 1.9.2 .

---

### 评论 #3 — kentrussell (2019-03-12T12:19:22Z)

Issue addressed since 1.9.2

---
