# [Issue]: Insufficient documentation on the repo tool and associated manifest.xml file

> **Issue #2615**
> **状态**: closed
> **创建时间**: 2023-10-30T20:45:07Z
> **更新时间**: 2024-07-25T18:21:39Z
> **关闭时间**: 2024-07-25T18:20:40Z
> **作者**: amd-isparry
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/2615

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- saadrahim

## 描述

### Problem Description

The top level README.md was altered in https://github.com/RadeonOpenCompute/ROCm/commit/1ae99c5e4bc77dd1dc4760eb29edfeb76c833229 to mention the manifest.xml file. However all it says is `The default.xml file uses the repo Manifest format.`.

There should be a link to the specification of this format.

There should be a link to the `repo` tool.

Ubuntu 20 didn't package the repo tool, apparently because of python2 to python3 changes. There should be a link to the repo tool site explaining how to install the tool.


### Operating System

N/A

### CPU

N/A

### GPU

N/A

### ROCm Version

5.7.x

### ROCm Component

Documentation

### Steps to Reproduce

_No response_

### Output of /opt/rocm/bin/rocminfo --support

Not applicable.
