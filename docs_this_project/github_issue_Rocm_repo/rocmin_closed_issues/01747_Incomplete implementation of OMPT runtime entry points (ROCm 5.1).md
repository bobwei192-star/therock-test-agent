# Incomplete implementation of OMPT runtime entry points (ROCm 5.1)

- **Issue #:** 1747
- **State:** closed
- **Created:** 2022-06-02T10:05:09Z
- **Updated:** 2023-12-22T19:46:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1747

In my work on OMPT target support, I've found a number of runtime entry points that are not yet implemented (and correctly return `NULL` when queried). This issue is to help prioritize the ongoing implementation effort.

**High importance for tools**

`translate_time`
`get_device_time`

At least one of these two entry points is necessary in order to map trace record timestamps into any other time stream in a portable way. `translate_time` has the advantage of compatibility with host-side queries of the OpenMP runtime but `wtime_t` is a less useful format than a `uint64_t` nanosecond-resolution timestamp.

**Not sure of importance, but surprised by the omission**

`get_device_num_procs`

This seems like low-hanging fruit. I don't think I need it in the near term though.

`pause_trace`

Isn't stop just a pause/flush?

**Important for clean code that we don't have to fix later**

`get_record_type`

Presently only OMPT type records are supported, not native records, which is fine. We should still be able to write tool code that checks the record type rather than blindly assuming OMPT formats via `static_cast`.

**Not important to us right now**

`get_record_native`
`get_record_abstract`
`set_trace_native`

Only supporting the OMPT format is fine for now.