# [RHEL8] rpm rdc lists libz.so.1 as provides

- **Issue #:** 1365
- **State:** closed
- **Created:** 2021-01-22T14:18:31Z
- **Updated:** 2021-04-07T06:32:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1365

At least rdc-0.4.0.40000-23.el8.x86_64.rpm, and probably other versions list libz.so.1 as provides. This causes severe issues on systems that do not have any rpm installed that provides libz.so.1, e.g. zlib.
E.g. when trying to bootstrap a new root file system using yum --installroot, yum ends up installing **rdc** instead of **zlib** as a dependecy. With rdc not installing libz.so.1 to a common path, commands may fail due to missing libz.so.1.

Hence rdc should not list libz.so.1 as provides. It probably should not bundle libz.so.1 at all and instead use the system provided shared library.

```
rpm -q --provides ./rocm/rdc-0.4.0.40000-23.el8.x86_64.rpm
warning: ./rocm/rdc-0.4.0.40000-23.el8.x86_64.rpm: Header V4 RSA/SHA1 Signature, key ID 1a693c5c: NOKEY
libabsl_bad_optional_access.so()(64bit)
libabsl_base.so()(64bit)
libabsl_dynamic_annotations.so()(64bit)
libabsl_int128.so()(64bit)
libabsl_log_severity.so()(64bit)
libabsl_raw_logging_internal.so()(64bit)
libabsl_spinlock_wait.so()(64bit)
libabsl_str_format_internal.so()(64bit)
libabsl_strings.so()(64bit)
libabsl_strings_internal.so()(64bit)
libabsl_throw_delegate.so()(64bit)
libaddress_sorting.so.9()(64bit)
libcrypto.so()(64bit)
libgpr.so.9()(64bit)
libgrpc++.so.1()(64bit)
libgrpc++_alts.so.1()(64bit)
libgrpc++_error_details.so.1()(64bit)
libgrpc++_reflection.so.1()(64bit)
libgrpc++_unsecure.so.1()(64bit)
libgrpc.so.9()(64bit)
libgrpc_cronet.so.9()(64bit)
libgrpc_plugin_support.so.1()(64bit)
libgrpc_unsecure.so.9()(64bit)
libgrpcpp_channelz.so.1()(64bit)
libprotobuf-lite.so.3.11.2.0()(64bit)
libprotobuf.so.3.11.2.0()(64bit)
libprotoc.so.3.11.2.0()(64bit)
librdc.so.0()(64bit)
librdc_bootstrap.so.0()(64bit)
librdc_client.so.0()(64bit)
librdc_client_smi.so.0()(64bit)
libssl.so()(64bit)
libupb.so.9()(64bit)
libz.so.1()(64bit)
libz.so.1(ZLIB_1.2.0)(64bit)
libz.so.1(ZLIB_1.2.0.2)(64bit)
libz.so.1(ZLIB_1.2.0.8)(64bit)
libz.so.1(ZLIB_1.2.2)(64bit)
libz.so.1(ZLIB_1.2.2.3)(64bit)
libz.so.1(ZLIB_1.2.2.4)(64bit)
libz.so.1(ZLIB_1.2.3.3)(64bit)
libz.so.1(ZLIB_1.2.3.4)(64bit)
libz.so.1(ZLIB_1.2.3.5)(64bit)
libz.so.1(ZLIB_1.2.5.1)(64bit)
libz.so.1(ZLIB_1.2.5.2)(64bit)
libz.so.1(ZLIB_1.2.7.1)(64bit)
libz.so.1(ZLIB_1.2.9)(64bit)
rdc = 0.4.0.40000-23.el8
rdc(x86-64) = 0.4.0.40000-23.el8
```