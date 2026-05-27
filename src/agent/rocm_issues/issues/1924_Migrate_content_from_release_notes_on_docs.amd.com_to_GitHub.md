# Migrate content from release notes on docs.amd.com to GitHub

> **Issue #1924**
> **状态**: closed
> **创建时间**: 2023-03-12T06:02:01Z
> **更新时间**: 2023-04-14T13:11:10Z
> **关闭时间**: 2023-04-14T13:11:10Z
> **作者**: saadrahim
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1924

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- Naraenda

## 描述

Note: this is a development task.

In order to ensure the accuracy of this GitHub repository, release notes from docs.amd.com for all ROCm releases 5.0 to 5.4 to the file https://github.com/RadeonOpenCompute/ROCm/blob/develop/CHANGELOG.md.

A few specific instructions for the migration. Content for the math libraries should be copied from GitHub repositories via scripts. A prewritten script will be provided upon request by email.

OS and GPU support information should not be copied into the CHANGELOG.

---

## 评论 (8 条)

### 评论 #1 — Naraenda (2023-03-28T09:44:24Z)

@saadrahim Few questions:
- This should be a pure GFM file right?
- Should the math libraries changes be grouped per library or per ROCm release?
- Do we want a neater, more interactive version (foldouts, reference links) with Myst for use in the webview? I can generate this easily with how the script is setup.

We can discuss during the meeting.

---

### 评论 #2 — saadrahim (2023-03-28T13:13:44Z)

> @saadrahim Few questions:
> 
> * This should be a pure GFM file right?
Yes, must be pure GFM
> * Should the math libraries changes be grouped per library or per ROCm release?
Everything should be grouped per ROCm release.
> * Do we want a neater, more interactive version (foldouts, reference links) with Myst for use in the webview? I can generate this easily with how the script is setup.
use valid GFM html and other GitHub recommended techniques.
> 
> We can discuss during the meeting.



---

### 评论 #3 — Naraenda (2023-03-29T10:21:23Z)

@saadrahim 

- Is it possible to get the source-text of the release notes on docs.amd.com? Maybe it's already in Markdown. That would make everything a lot easier for me.

- There is a lot of duplication in the deprecation notes between the releases on docs.amd.com. Should we group these by major/minor releases? Or keep them on a per-patch basis (there will be _a lot_ of text)?

**Release Notes:** (Proposed)
- ROCm 5.4.x
  - HIPCC Deprecation
  - Patch Notes
    - ROCm 5.4.3
    - ROCm 5.4.2
    - ROCm 5.4.1
    - ROCm 5.4.0
 - ROCm 5.3.x
   - HIPCC Deprecation
   - Patch Notes
     - ROCm 5.3.3
     - ROCm 5.3.2
     - ...

**Release Notes:** (Current)
- ROCm 5.4.3
  - HIPCC Deprecation
- ROCm 5.4.2
  - HIPCC Deprecation
- ROCm 5.4.1
  - HIPCC Deprecation
- ROCm 5.4.0
  - HIPCC Deprecation
- ROCm 5.3.3
  - HIPCC Deprecation
- ...

I think having things grouped by major/minor version first allows people to get the most important things first and the patch specific changes can be read without going through all the boilerplate of all the shared items.




---

### 评论 #4 — Rmalavally (2023-03-29T14:35:53Z)

I am happy to provide the release notes' source files, which are not in Markdown. 

The replication of deprecation content is intended; they are, sometimes, a reminder/warning to our users for upcoming and actual deprecations in a release. 

---

### 评论 #5 — Naraenda (2023-03-29T14:53:52Z)

@Rmalavally 
> I am happy to provide the release notes' source files, which are not in Markdown.

Awesome, feel free to contact me via email: `nara <at> streamhpc <dot> com`

> The replication of deprecation content is intended; they are, sometimes, a reminder/warning to our users for upcoming and actual deprecations in a release.

That makes sense. Will keep the same ordering then.



---

### 评论 #6 — Rmalavally (2023-03-29T15:44:06Z)

Can you access Sharepoint or Confluence yet? 

---

### 评论 #7 — Naraenda (2023-03-29T16:04:05Z)

Not yet, but no ETA yet so it could take a while. I'll probably just convert everything manually then.

---

### 评论 #8 — Rmalavally (2023-03-29T17:01:03Z)

Please let me know when you have access, and I can share the source files with you. 

---
