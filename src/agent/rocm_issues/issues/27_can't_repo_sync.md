# can't repo sync

> **Issue #27**
> **状态**: closed
> **创建时间**: 2016-08-31T05:21:00Z
> **更新时间**: 2017-01-03T19:17:42Z
> **关闭时间**: 2017-01-03T19:17:42Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/27

## 描述

The repo configuration is set to use ssh, which makes it unusable for people for people who are not github users (at the least) and I believe github users who don't have commit access (like myself).

Perhaps I missed something that lets ssh cloning work in these cases?

ps.  Please support and build binaries for OpenSUSE! 


---

## 评论 (3 条)

### 评论 #1 — ghost (2016-08-31T18:30:49Z)

Hey nevion,

The reason we use ssh by default is to avoid numerous password prompts when cloning multiple repositories. Github users without commit access should be able to clone without issue. But non-GitHub users are left out in the dust if they want to repo sync.

I can understand your desire for performing an anonymous http clone. I'll add this to my todo list. If you need this urgently, we'll gladly accept a pull request that adds a secondary manifest that uses anonymous http.


---

### 评论 #2 — nevion (2016-08-31T18:58:26Z)

I hacked the repo manifest remote urls to this:

```
remote name="roc-github"
        fetch="https://github.com/RadeonOpenCompute/" />
<remote name="pctools-github"
         fetch="https://github.com/GPUOpen-ProfessionalCompute-Tools/" />
```

And it mostly successfully clone'd the repos, although I got some curl 404 errors along the way (I don't know what for yet), such as curl: (22) The requested URL returned error: 404 Not Found
Server does not provide clone.bundle; ignoring.

I'm not sure how to switch manifest files without ln -s'ing another file in or overwriting manifest.xml, or if this is the best way for ROCm, but it seems to have worked.    I'll update if I get build errors from it.


---

### 评论 #3 — jedwards-AMD (2016-09-02T18:12:12Z)

The cur: (22) error codes are a well known curl defect, and have nothing to do with the repositories.


---
