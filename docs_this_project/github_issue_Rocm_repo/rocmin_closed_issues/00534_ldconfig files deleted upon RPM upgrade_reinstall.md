# ldconfig files deleted upon RPM upgrade/reinstall

- **Issue #:** 534
- **State:** closed
- **Created:** 2018-09-15T00:42:02Z
- **Updated:** 2019-03-12T12:19:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/534

We just found an issue when upgrading or reinstalling the RPMs. The post-install script of the rpm says this: 

```
postuninstall scriptlet (using /bin/sh):
rm -f /etc/ld.so.conf.d/hsa-rocr-dev.conf && ldconfig
```

But when one upgrades (or re-installs) a RPM, that first installs the new one, runs the post-install scriplet, which will create the file, then it removes the old version, and runs the postuninstall scriplet. Therefore the ldconfig file is deleted. 

We think the postrun scriptlet should be something like: 

``` 
if [ $1 -eq 0]; then
  # the old script, like rm -f /etc/ld....
fi
```