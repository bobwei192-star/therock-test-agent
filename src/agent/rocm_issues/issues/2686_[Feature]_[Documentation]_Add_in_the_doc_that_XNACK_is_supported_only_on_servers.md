# [Feature]: [Documentation] Add in the doc that XNACK is supported only on servers hosting AMD GPU cards which are ALL supporting XNACK 

> **Issue #2686**
> **状态**: open
> **创建时间**: 2023-12-01T10:46:04Z
> **更新时间**: 2024-05-17T17:02:23Z
> **作者**: pierreantoineH
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/2686

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- SwRaw

## 描述

### Suggestion Description

It has been observed that on a server hosting both MI210's cards (suporting XNACK+) and  Radeon Pro W6800 cards, HMM is not working on MI210. When the Radeon Pro W6800 cards is removed from the server, XNACK is working on MI210 cards.
Per the current understanding, SVM memory manager only supports the same XNACK mode for all GPUs, thus this behavior is expected. 
Is it possible to indicate in the documentation that XNACK is supported only on servers hosting AMD GPU cards which are ALL supporting XNACK ? 

### Operating System

_No response_

### GPU

MI210 + W6800

### ROCm Component

ROCm Documentation
