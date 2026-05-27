# Debian repository source .DEB files missing

> **Issue #251**
> **状态**: closed
> **创建时间**: 2017-11-13T08:24:25Z
> **更新时间**: 2018-11-27T08:19:31Z
> **关闭时间**: 2018-06-03T15:10:40Z
> **作者**: madscientist159
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/251

## 描述

The source .deb files needed to recompile ROCm from source under the Debian packaging system are missing.  Please either upload the Debian packaging source .dsc / tarballs to the repository, or provide the packaging files in a separate repository.

Thanks! :smile:

---

## 评论 (1 条)

### 评论 #1 — madscientist159 (2018-11-27T08:04:52Z)

What was this closed with no comment?  Is the intent that we need to write Debian packaging files from scratch or is there another way to get them?

EDIT:  Looks like the packages are generated directly via CPack.  Going to need some hacking on the sources to get "real" Debian source files, but at least I know where to look now.

---
