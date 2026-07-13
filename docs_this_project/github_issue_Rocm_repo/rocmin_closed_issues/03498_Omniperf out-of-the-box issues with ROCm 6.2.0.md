# Omniperf out-of-the-box issues with ROCm 6.2.0

- **Issue #:** 3498
- **State:** closed
- **Created:** 2024-08-02T18:43:42Z
- **Updated:** 2024-12-05T19:53:15Z
- **Labels:** Verified Issue, 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3498

**Error when running Omniperf with an application with command line arguments**. As a workaround, create an intermediary script to call the application with the necessary arguments, then call the script with Omniperf. This issue is fixed in a future release of Omniperf. See [#347](https://github.com/ROCm/omniperf/issues/347).

---

**Omniperf might not work with AMD Instinct MI300 accelerators out of the box**, resulting in the following error: “ERROR gfx942 is not enabled rocprofv1. Available profilers include: [‘rocprofv2’]”. As a workaround, add the environment variable export ROCPROF=rocprofv2.

---

**Omniperf’s Python dependencies may not be installed with your ROCm installation**, resulting in the following message:

“[ERROR] The ‘dash>=1.12.0’ package was not found in the current execution environment.

[ERROR] The ‘dash-bootstrap-components’ package was not found in the current execution environment.

Please verify all of the Python dependencies called out in the requirements file are installed locally prior to running omniperf.

See: /opt/rocm-6.2.0/libexec/omniperf/requirements.txt”

As a workaround, install these Python requirements manually: pip install /opt/rocm-6.2.0/libexec/omniperf/requirements.txt.