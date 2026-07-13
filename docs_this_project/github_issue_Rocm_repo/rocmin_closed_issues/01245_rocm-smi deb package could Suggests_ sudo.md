# rocm-smi deb package could Suggests: sudo

- **Issue #:** 1245
- **State:** closed
- **Created:** 2020-09-25T17:09:30Z
- **Updated:** 2021-04-09T06:05:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1245

Very low prio, but just small suggestion.

`rocm-smi` only requires `Depends: python3`, and nothing else (I checked the source and indeed that is true!), and that is awesome.

But setting things require running as root, or the scripts does `execvp` to re-execute using `sudo`.

So I think it would make sense to add this to control file: `Suggests: sudo`  as a non-strong dependency, and it enhanced the script, but is not required in any sense.
