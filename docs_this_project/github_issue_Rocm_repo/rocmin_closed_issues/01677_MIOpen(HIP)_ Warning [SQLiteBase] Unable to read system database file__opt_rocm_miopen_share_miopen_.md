# MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:/opt/rocm/miopen/share/miopen/db/gfx906_60.kdb Performance may degrade terminate called after throwing an instance of 'boost::filesystem::filesystem_error'

- **Issue #:** 1677
- **State:** closed
- **Created:** 2022-02-15T05:53:50Z
- **Updated:** 2024-01-20T01:54:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1677

Full error message when I am trying to train a deep learning model.
```
MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:/opt/rocm/miopen/share/miopen/db/gfx906_60.kdb Performance may degrade
terminate called after throwing an instance of 'boost::filesystem::filesystem_error'`  
what():  boost::filesystem::permissions: No such file or directory: "/home/ssml/singh/.config/miopen//gfx906_60.HIP.2_11_0_993628deb.ufdb.txt"
```