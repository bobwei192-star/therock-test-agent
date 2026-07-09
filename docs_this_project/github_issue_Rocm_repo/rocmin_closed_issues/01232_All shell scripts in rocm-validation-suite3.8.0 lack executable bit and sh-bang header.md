# All shell scripts in rocm-validation-suite3.8.0 lack executable bit and sh-bang header

- **Issue #:** 1232
- **State:** closed
- **Created:** 2020-09-22T21:32:32Z
- **Updated:** 2021-01-27T10:56:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1232

rocm-validation-suite3.8.0 3.4.30800

```
root@debian:/opt/rocm-3.8.0/rvs# ls -lh ./testscripts/
total 64K
-rw-r--r-- 1 1001 root  106 Sep 14 19:36 gpup.new.sh
-rw-r--r-- 1 1001 root  103 Sep 14 19:36 gst.new.sh
-rw-r--r-- 1 1001 root  104 Sep 14 19:36 iet.new.sh
-rw-r--r-- 1 1001 root  583 Sep 14 19:36 mix.new.sh
-rw-r--r-- 1 1001 root  106 Sep 14 19:36 pebb.new.sh
-rw-r--r-- 1 1001 root  105 Sep 14 19:36 peqt.new.sh
-rw-r--r-- 1 1001 root  510 Sep 14 19:36 pesm.new.sh
-rw-r--r-- 1 1001 root  102 Sep 14 19:36 pqt.new.sh
-rw-r--r-- 1 1001 root  105 Sep 14 19:36 rand.new.sh
-rw-r--r-- 1 1001 root 2.6K Sep 14 19:36 rcqt.new.sh
-rw-r--r-- 1 1001 root   55 Sep 14 19:36 rvs-mem.sh
-rw-r--r-- 1 1001 root  990 Sep 14 19:36 rvsqa.new.sh
-rw-r--r-- 1 1001 root  708 Sep 14 19:36 rvs-stress-long.sh
-rw-r--r-- 1 1001 root  174 Sep 14 19:36 smqt.new.sh
-rw-r--r-- 1 1001 root 5.9K Sep 14 19:36 ttf.new.sh
root@debian:/opt/rocm-3.8.0/rvs#
```


```
# file *
gpup.new.sh:        ASCII text
gst.new.sh:         ASCII text
iet.new.sh:         ASCII text
mix.new.sh:         ASCII text
pebb.new.sh:        ASCII text
peqt.new.sh:        ASCII text
pesm.new.sh:        ASCII text
pqt.new.sh:         ASCII text
rand.new.sh:        ASCII text
rcqt.new.sh:        ASCII text
rvs-mem.sh:         ASCII text
rvsqa.new.sh:       ASCII text
rvs-stress-long.sh: ASCII text
smqt.new.sh:        ASCII text
ttf.new.sh:         ASCII text
$
```

File content:

```
# head gpup.new.sh 
date
./conf/deviceid.sh conf/gpup_single.conf
echo 'gpup';sudo ./rvs -c conf/gpup_single.conf -d 3; date
#
```

Please add executable bits, and `#!/bin/sh` to all these scripts.
