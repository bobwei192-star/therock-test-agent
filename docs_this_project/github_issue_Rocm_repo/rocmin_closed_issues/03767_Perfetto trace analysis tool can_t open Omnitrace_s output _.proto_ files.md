# Perfetto trace analysis tool can't open Omnitrace's output `.proto` files

- **Issue #:** 3767
- **State:** closed
- **Created:** 2024-09-20T21:25:02Z
- **Updated:** 2025-01-10T14:57:57Z
- **Labels:** Verified Issue, 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/3767

Perfetto can no longer open [Omnitrace](https://rocm.docs.amd.com/projects/omnitrace/en/docs-6.2.1) proto files. Loading Perfetto trace output `.proto` files in the latest version of [ui.perfetto.dev](ui.perfetto.dev) can result in a dialog with the message, "Oops, something went wrong! Please file a bug." The information in the dialog will refer to an "Unknown field type."

The workaround is to open the files with a previous version of the Perfetto UI found at [https://ui.perfetto.dev/v46.0-35b3d9845/#!/](https://ui.perfetto.dev/v46.0-35b3d9845/#!/).