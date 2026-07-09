# rocminfo does not report a "Marketing Name" for MI100 or MI200 GPUs

- **Issue #:** 1778
- **State:** closed
- **Created:** 2022-08-04T17:13:00Z
- **Updated:** 2024-05-09T16:21:32Z
- **Assignees:** saadrahim
- **URL:** https://github.com/ROCm/ROCm/issues/1778

I earlier reported an issue with HIP (to the HIP group) that HIP was not returning device
properties for some GPU models.

I recalled an earlier issue with rocminfo not reporting the "Marketing Name" (human readable
GPU name) for some GPUs.

Upon examining this issue again, the same GPUs (MI100, MI200) which do not report a marketing name
via rocminfo, also do not report the device name at the HIP level.

Marketing Name is reported for an MI25.  I don't have an MI50 or MI60 to test behavior on those models.

The repeater is to run rocminfo (5.2.0 version is latest, with corresponding amdgpu driver on enterprise
linux 8 (or SLES)) and observe that "Marketing Name" is blank for MI100 and MI200, and populated for MI25.