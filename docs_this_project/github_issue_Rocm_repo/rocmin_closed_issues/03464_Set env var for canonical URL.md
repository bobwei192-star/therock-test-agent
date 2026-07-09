# Set env var for canonical URL

- **Issue #:** 3464
- **State:** closed
- **Created:** 2024-07-26T18:05:23Z
- **Updated:** 2024-07-26T21:37:00Z
- **Assignees:** samjwu
- **URL:** https://github.com/ROCm/ROCm/issues/3464

```
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm.docs.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
```