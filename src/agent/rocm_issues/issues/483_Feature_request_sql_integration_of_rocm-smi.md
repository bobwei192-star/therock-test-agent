# Feature request sql integration of rocm-smi 

> **Issue #483**
> **状态**: closed
> **创建时间**: 2018-07-31T12:59:33Z
> **更新时间**: 2018-08-19T16:41:21Z
> **关闭时间**: 2018-08-19T16:41:21Z
> **作者**: ghost
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/483

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

*(无描述)*

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2018-08-13T17:01:45Z)

Hi @tekcomm 

Sorry for the delay in responding to this. I think this sounds like an interesting feature, though I'm not sure if our internal development teams would have time to put this on our roadmap -- development and verification resources being what they are, I can't promise that we would be able to spare the resources for a feature that (while admittedly potentially useful) doesn't have a lot of customer demand.

That said, I see that your git repo is a README that describes the end result, but doesn't include the code. Would you be interested in sending me a note, potentially with access to the code you use to do this? If it's not a tremendous amount of extra complexity, I could try to see if our teams would upstream your rocm-smi changes.

Thanks!

---

### 评论 #2 — jlgreathouse (2018-08-13T19:10:51Z)

Great, thanks for putting the code up. Let me take a look at it, and then pass around the details internally.

First question that comes to mind: I suspect our normal users wouldn't want to always have SQL printed to the screen, so we would want to have a command-line option for this. When that command line option is set, do you have any thoughts on what we should do with errors? Right now, we log errors directly to stdout, which seems like it would interfere with your SQL insert statements. For instance, on my system where one of my GPUs doesn't support power monitoring:
```
$ ./rocm_smi-mysql
INSERT INTO miner_stats (gpu,temp,avgpwr,sclk,mclk,fan,perf,od,hostname) VALUES GPU[1]          : WARNING: Empty SysFS value: power
('g1','46.0','Error','300','150','20.0,'auto','0','sysname'),('g0','42.0','4.0','852','167','11.76,'auto','0','sysname');
WARNING: One or more commands failed
```

The two WARNING lines -- in this mode should they be suppressed? Or logged somewhere else (e.g. stderr so that you can redirect them away from the normal stdout SQL statement)? Thoughts on this, since you're the first (and so far only) user of this proposed mode. :)

---

### 评论 #3 — jlgreathouse (2018-08-13T19:44:50Z)

Let me take a stab at some changes that I'll pass around internally. If they aren't too bad, I'll submit a PR to your repo so you can try them out and see if they meet your needs.

---

### 评论 #4 — jlgreathouse (2018-08-14T22:32:29Z)

Looks like it'll be a bit before I can try some internal changes -- we might need to sync on this after ROCm 1.9 comes out. rocm-smi in 1.9 will have some changes that we'll need to work with if we want to explore this request.

---
