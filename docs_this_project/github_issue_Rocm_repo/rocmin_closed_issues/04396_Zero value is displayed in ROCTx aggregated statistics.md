# Zero value is displayed in ROCTx aggregated statistics

- **Issue #:** 4396
- **State:** closed
- **Created:** 2025-02-19T20:00:18Z
- **Updated:** 2025-05-05T16:10:53Z
- **Labels:** Verified Issue, ROCm 6.3.3
- **URL:** https://github.com/ROCm/ROCm/issues/4396

The ROCTx markers are standalone markers within the ROCProfiler-SDK library. Each marker reports only a single timestamp, which is recorded as the `start_timestamp` and `end_timestamp`. As a result, the value for aggregated statistics presented in `TotalDurationNs`, `maxNs`, and `minNs`, is zero. The zero value indicates that the actual execution time is not associated with the markers, which is an expected behavior.