# Functions like hsa_signal_add_scacquire do not return value

- **Issue #:** 5310
- **State:** closed
- **Created:** 2025-09-12T16:08:35Z
- **Updated:** 2025-11-03T15:19:39Z
- **Labels:** Under Investigation
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5310

What does this function actually "acquire"? ~It seems such functions which do not return anything with acquire semantics are unnecessary.~

``` c++
void HSA_API hsa_signal_add_scacquire(
    hsa_signal_t signal,
    hsa_signal_value_t value);
```

~If I need to "acquire" new value after such addition I cannot use `hsa_signal_load_relaxed`. I have to use `hsa_signal_load_scacquire` and then `hsa_signal_add_scacquire` is redundant and `hsa_signal_add_relaxed` would be enough (or `hsa_signal_add_screlease` in case of `hsa_signal_add_scacq_screl`).~
