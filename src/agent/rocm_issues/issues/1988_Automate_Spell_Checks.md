# Automate Spell Checks

> **Issue #1988**
> **状态**: closed
> **创建时间**: 2023-03-23T15:28:03Z
> **更新时间**: 2023-04-24T13:13:56Z
> **关闭时间**: 2023-04-24T13:13:56Z
> **作者**: saadrahim
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1988

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- Naraenda

## 描述

Per PR spell checks is needed. GitHub action is probably the best way. Grammar and automated stylistic checks should be looked at as well.

---

## 评论 (2 条)

### 评论 #1 — Naraenda (2023-04-17T12:21:38Z)

@saadrahim 
I've found a few spelling checkers and my preference goes to `Github Spellcheck Action`, `CSpell`. Both also work with CPP, so it might be interesting to use in the library repositories too. `CSpell` seems to be the most powerful one. `LanguageTool` is also interesting as it does grammar checking, but probably will requiring hosting the language server ourselves due to API limits.

## GitHub Spellcheck Action
⭐ 109 | 🌐 https://github.com/rojopolis/spellcheck-github-actions
- Uses [PySpelling (⭐56)](https://github.com/facelessuser/pyspelling)
- Internally uses [Aspell](https://github.com/GNUAspell/aspell) (English, German, Spanish) via Debian Package
  - Hunspell *could* be added.
- Pretty straightforward and simple to use.
- Uses additive word lists.
- Supports multiple Markdown extensions

## CSpell
⭐ 797 | 🌐 https://github.com/streetsidesoftware/cspell
- Allows enabling and disabling of spellchecking in source.
- Can fetch word lists from external sources. (Do we want this word list in rocm-docs-core?) Or you can just use a word list.
- Can also use RegEx to set ignored words.
- Can be integrated via [MegaLinter](https://github.com/oxsecurity/megalinter). (Do we want to combine this together with the `markdownlint` action?)

## LanguageTool
⭐ 8.5k | 🌐 https://github.com/languagetool-org/languagetool
- Runs as a server: either self-hosted or via an API.
- There's a small GitHub Action made by a 3rd party: https://github.com/reviewdog/action-languagetool
  - Posts suggestions as code review comments.
- It appears that there is also a CLI. But there isn't much documentation.


## Check Spelling
⭐ 181 | 🌐 https://github.com/check-spelling/check-spelling
- Uses: [Spelling (⭐124)](https://github.com/jsoref/spelling)
- Generates comments in PR regarding misspellings.
- Works with a word list with a smaller add/reject list. Also accepts Perl RegEx.


---

### 评论 #2 — Naraenda (2023-04-24T13:13:56Z)

Fixed in #2070

---
