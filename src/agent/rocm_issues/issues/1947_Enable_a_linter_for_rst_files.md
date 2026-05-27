# Enable a linter for rst files

> **Issue #1947**
> **状态**: closed
> **创建时间**: 2023-03-14T19:42:37Z
> **更新时间**: 2023-03-24T14:34:29Z
> **关闭时间**: 2023-03-24T14:34:29Z
> **作者**: saadrahim
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1947

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- MathiasMagnus

## 描述

*(无描述)*

---

## 评论 (3 条)

### 评论 #1 — AlexVlx (2023-03-16T16:56:51Z)

We might want to consider this one: <https://pypi.org/project/restructuredtext-lint/>. It's pretty symmetric with `markdownlint`

---

### 评论 #2 — MathiasMagnus (2023-03-21T14:55:52Z)

I was happy to find out that a project took the effort in unifying the linter interfaces of a few dozen languages and formats. ([MegaLinter](https://github.com/marketplace/actions/megalinter#languages)), it's even conveniently wrapped with an Action (unlike the one Alex mentioned, but it does incorporate the very same linter), so it's 5-6 birds with one stone. When I hooked it up to CI, the Docker image they use to distribute the project for local and use in Actions is _7.57GB!!!!_ So MegaLinter goes out the window. Back to pip installing restructuredtext-lint.

---

### 评论 #3 — aaronmondal (2023-03-23T22:19:25Z)

Nix can be pretty helpful in such cases. For instance we use markdownlint [here](https://github.com/eomii/rules_ll/blob/main/pre-commit-hooks.nix#L83-L89) and use a github action that reuses the installation by caching [here](https://github.com/eomii/rules_ll/blob/main/.github/workflows/pre-commit.yml). All pre-commit hooks together are ~700 megabytes, or ~7% of the free cache limit per Github repo (i.e. its free :laughing:). Without caching these hooks take ~2 min to run. With caching this becomes ~45 seconds.

---
