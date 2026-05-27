# rocm-smi deb package could Suggests: sudo

> **Issue #1245**
> **状态**: closed
> **创建时间**: 2020-09-25T17:09:30Z
> **更新时间**: 2021-04-09T06:05:34Z
> **关闭时间**: 2021-04-08T14:17:52Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1245

## 描述

Very low prio, but just small suggestion.

`rocm-smi` only requires `Depends: python3`, and nothing else (I checked the source and indeed that is true!), and that is awesome.

But setting things require running as root, or the scripts does `execvp` to re-execute using `sudo`.

So I think it would make sense to add this to control file: `Suggests: sudo`  as a non-strong dependency, and it enhanced the script, but is not required in any sense.


---

## 评论 (12 条)

### 评论 #1 — rkothako (2020-11-18T08:52:12Z)

Thanks @baryluk 
Can you please elaborate your query by sharing some scenario/examples

---

### 评论 #2 — rkothako (2020-11-18T11:39:17Z)

sudo is required to set any settings.
Normally we relaunch as sudo if there are any issues. But we can't make it a dependency in the packaging, unfortunately, we just have to run it as sudo if we want to change anything.
Hope this helps.

---

### 评论 #3 — baryluk (2020-11-18T18:40:53Z)

Just add `Suggests: sudo` to the debian package. It is not a dependency, but a weak dependency. It will not break anything. On Ubuntu, sudo is usually installed by default, but it is not the case on Debian and derivatives for example.

You can read more here: https://www.debian.org/doc/debian-policy/ch-relationships.html#binary-dependencies-depends-recommends-suggests-enhances-pre-depends


---

### 评论 #4 — rkothako (2020-11-19T05:58:45Z)

Hi @baryluk 
We do not wish to recommend sudo for any kind of rocm operations. Ideally all functions should work without sudo.
There are/may be some cases where some times, things work with sudo only. In those cases, users definitely try with sudo only.

Anyway I will once again check with component owner and update on this.
Thank you.

---

### 评论 #5 — rkothako (2020-11-19T15:34:08Z)

For suggests/requires/depends, these need to be packages that might not be installed. Since sudo is always installed, the only way someone would see that we're suggesting sudo is by reading the packaging (and almost no one ever does that). And since any system that doesn't have sudo installed would be broken, it's inclusion in the requires/suggests section would not be any different than the SMI currently is. Plus, it's not required for simple monitoring, it's only needed for changing settings, so there's that side of things as well

---

### 评论 #6 — baryluk (2020-11-20T15:06:04Z)

@rkothako sudo is not always installed at all. I have a system with no sudo.

Please add `Suggests: sudo`. It is simple as that.


---

### 评论 #7 — kentrussell (2020-12-03T13:03:29Z)

@baryluk I had not seen "Suggests: sudo" in the wild before, but I see it in a few spots now that you've inspired me to take a look. I honestly hadn't considered that there would be many systems running ROCm where they would not have sudo, but I'll see if we can make that change. 


---

### 评论 #8 — rkothako (2020-12-03T13:21:12Z)

Thanks @kentrussell for looking into it.

---

### 评论 #9 — kentrussell (2021-01-06T13:30:04Z)

We have merged this request internally and are tracking it to be resolved in ROCm 4.1

---

### 评论 #10 — ROCmSupport (2021-04-08T11:50:28Z)

Hi @baryluk 
Issue is fixed with 4.1 code. Can you please check and update asap.
Thank you.

---

### 评论 #11 — baryluk (2021-04-08T14:17:52Z)

Fixed. Thank you.

---

### 评论 #12 — ROCmSupport (2021-04-09T06:05:34Z)

Thanks @baryluk for the closure.

---
