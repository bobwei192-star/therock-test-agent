# [Documentation]: Precision support - Libraries input/output type support

- **Issue #:** 3434
- **State:** open
- **Created:** 2024-07-18T15:50:01Z
- **Updated:** 2024-12-10T14:58:05Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/3434

### Description of errors

The support matrix discussed below needs to provide information on all ROCm libraries, not just the six provided.

Currently the documentation for precision support ([here](https://rocm.docs.amd.com/en/latest/compatibility/precision-support.html#libraries-input-output-type-support)) aims to provide an overview for supported and unsupported precisions (e.g., `float16`) across various ROCm libraries. However, only 3 roc + 3 hip libraries are provided. This is a tiny amount of the actual number of ROCm libaries ([here](https://rocm.docs.amd.com/en/latest/reference/api-libraries.html)); particularly, the Math libraries, which are arguably some of the most relevant for non-standard precisions, are severely lacking in the supported/unsupported matrix.

Also, the libraries hipRAND and hipCUB have implied hyperlinks in the form of "(details)", but these are just text and do not link to anything.


### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_