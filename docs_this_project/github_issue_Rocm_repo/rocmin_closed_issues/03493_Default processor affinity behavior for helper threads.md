# Default processor affinity behavior for helper threads

- **Issue #:** 3493
- **State:** closed
- **Created:** 2024-08-02T18:21:21Z
- **Updated:** 2024-12-03T22:20:12Z
- **Labels:** Verified Issue, 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3493

Processor affinity is a critical setting to ensure that ROCm helper threads run on the correct cores. By default, ROCm helper threads are spawned on all available cores, ignoring the parent thread’s processor affinity. This can lead to threads competing for available cores, which may result in suboptimal performance. This behavior occurs by default if the environment variable `HSA_OVERRIDE_CPU_AFFINITY_DEBUG` is not set or is set to `1`. If `HSA_OVERRIDE_CPU_AFFINITY_DEBUG` is set to `0`, the ROCr runtime uses the parent process’s core affinity mask when creating helper threads. The parent’s affinity mask should then be set to account for the presence of additional threads by ensuring the affinity mask contains enough cores. Depending on the affinity settings of the software environment, batch system, launch commands like `numactl`/`taskset`, or explicit mask manipulation by the application itself, changing the setting may be advantageous to performance.

To ensure the parent’s core affinity mask is honored by the ROCm helper threads, set the `HSA_OVERRIDE_CPU_AFFINITY_DEBUG` environment variable as follows:

`export HSA_OVERRIDE_CPU_AFFINITY_DEBUG=0`

To ensure ROCm helper threads run on all available cores, set the `HSA_OVERRIDE_CPU_AFFINITY_DEBUG` environment variable as follows:

`export HSA_OVERRIDE_CPU_AFFINITY_DEBUG=1`

Or the default:

`unset HSA_OVERRIDE_CPU_AFFINITY_DEBUG`

If unsure of the default processor affinity settings for your environment, run the following command from the shell:

`bash -c "echo taskset -p \$\$"`