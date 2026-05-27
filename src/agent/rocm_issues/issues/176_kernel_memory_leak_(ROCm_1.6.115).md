# kernel memory leak? (ROCm 1.6.115)

> **Issue #176**
> **状态**: closed
> **创建时间**: 2017-08-02T06:56:24Z
> **更新时间**: 2018-06-03T14:54:54Z
> **关闭时间**: 2018-06-03T14:54:54Z
> **作者**: gsedej
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/176

## 描述

Hello,
recently I found out that I am losing RAM and I can't get it back by closing programs. The only bigger change to my system was updating ROCm (kernel 4.9 to 4.11).
Anyone else noticed this issue?
(using ubuntu 16.04)

The following data is after less than 24 hours, and not working with gpu (just desktop, browser and some text editors)
When i close all programs, system is still using around 4 GB of memory
see "total size", kernel is takinga 2.9 GB of memory
slabtop
```
Active / Total Objects (% used)    : 9824285 / 9902782 (99.2%)
 Active / Total Slabs (% used)      : 324643 / 324643 (100.0%)
 Active / Total Caches (% used)     : 74 / 95 (77.9%)
 Active / Total Size (% used)       : 2888893.34K / 2904551.59K (99.5%)
 Minimum / Average / Maximum Object : 0.01K / 0.29K / 18.62K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME                   
2124486 2124486 100%    0.19K 101166       21    404664K kmalloc-192
1569945 1558847  99%    0.10K  40255       39    161020K buffer_head
1084992 1084643  99%    0.25K  33906       32    271248K kmalloc-256
1072192 1072120  99%    0.50K  33506       32    536096K kmalloc-512
1069376 1069376 100%    1.00K  33418       32   1069376K kmalloc-1024
1069320 1069281  99%    0.09K  25460       42    101840K kmalloc-96
1066848 1066848 100%    0.12K  33339       32    133356K kmalloc-128
101976  96939  95%    0.57K   3642       28     58272K radix_tree_node
 96096  87523  91%    0.19K   4576       21     18304K dentry
...
```

amdgpu is using 2.5 GB of memory
```
lsmod | grep amd
amdkfd                212992  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               2523136  254
...
```

meminfo reports 2.6 GB unreclaimable slab (SUnreclaim)
```
cat /proc/meminfo
MemTotal:       16383964 kB
MemFree:         1621620 kB
MemAvailable:    8957684 kB
Buffers:         1057460 kB
Cached:          6388512 kB
...
Slab:            2920576 kB
SReclaimable:     319692 kB
SUnreclaim:      2600884 kB
...
```

Also, i was off work for 2 weeks, the computer was on and slabtop reported used 10GB memory - around 9GB of "SUnreclaim" in meminfo

---

## 评论 (21 条)

### 评论 #1 — gsedej (2017-08-07T12:30:16Z)

after running few days over the weekend:
_(i did full uninstall and reinstall of rocm)
also my system spec:  rx480 8GB, i7 6700, ubuntu 16.04_

```
$ lsmod | grep amd
amdkfd                212992  5
amd_iommu_v2           20480  1 amdkfd
amdgpu               2523136  330
i2c_algo_bit           16384  1 amdgpu
ttm                    94208  1 amdgpu
drm_kms_helper        143360  1 amdgpu
drm                   344064  9 amdgpu,ttm,drm_kms_helper
```
stays the same as after reboot

```
$ cat /proc/meminfo 
MemTotal:       16383964 kB
MemFree:         1597308 kB
MemAvailable:    4923676 kB
Buffers:         1059516 kB
Cached:          2204912 kB
SwapCached:        25280 kB
Active:          4688088 kB
Inactive:        1544580 kB
Active(anon):    3077868 kB
Inactive(anon):   184328 kB
Active(file):    1610220 kB
Inactive(file):  1360252 kB
Unevictable:          64 kB
Mlocked:              64 kB
SwapTotal:       7609340 kB
SwapFree:        6873852 kB
Dirty:                 8 kB
Writeback:             0 kB
AnonPages:       2939164 kB
Mapped:           322816 kB
Shmem:            293956 kB
Slab:            8191340 kB
SReclaimable:     608476 kB
SUnreclaim:      7582864 kB
KernelStack:       13696 kB
PageTables:        57496 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    15801320 kB
Committed_AS:   10553764 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
HardwareCorrupted:     0 kB
AnonHugePages:   1992704 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:     4455248 kB
DirectMap2M:    12273664 kB
DirectMap1G:           0 kB
```
7.5 GB of unreclaimable slab
```
$ sudo slabtop -o
 Active / Total Objects (% used)    : 25592017 / 25754483 (99.4%)
 Active / Total Slabs (% used)      : 889552 / 889552 (100.0%)
 Active / Total Caches (% used)     : 77 / 121 (63.6%)
 Active / Total Size (% used)       : 8464811.48K / 8499206.88K (99.6%)
 Minimum / Average / Maximum Object : 0.01K / 0.33K / 18.62K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME                   
7060536 7060536 100%    0.19K 336216       21   1344864K kmalloc-192            
3558192 3557983  99%    0.25K 111194       32    889552K kmalloc-256            
3540480 3539806  99%    0.50K 110640       32   1770240K kmalloc-512            
3540306 3540306 100%    0.09K  84293       42    337172K kmalloc-96             
3537832 3537800  99%    1.00K 110559       32   3537888K kmalloc-1024           
3535776 3535616  99%    0.12K 110493       32    441972K kmalloc-128            
188175 114247  60%    0.10K   4825       39     19300K buffer_head            
 93504  90843  97%    0.06K   1461       64      5844K anon_vma_chain         
 86709  53630  61%    0.19K   4129       21     16516K dentry                 
 85760  78550  91%    0.06K   1340       64      5360K kmalloc-64             
 85008  83471  98%    0.19K   4048       21     16192K cred_jar               
 56661  55772  98%    0.08K   1111       51      4444K anon_vma               
 47736  47736 100%    0.12K   1404       34      5616K kernfs_node_cache      
 46208  41086  88%    0.03K    361      128      1444K kmalloc-32             
 43008  43008 100%    0.01K     84      512       336K kmalloc-8              
 36932  25214  68%    0.57K   1319       28     21104K radix_tree_node        
 26040  17010  65%    1.05K    868       30     27776K ext4_inode_cache       
 25596  24421  95%    0.58K    948       27     15168K inode_cache            
 20736  20736 100%    0.02K     81      256       324K kmalloc-16             
 19686   8715  44%    0.04K    193      102       772K ext4_extent_status     
 12816  12217  95%    0.65K    534       24      8544K proc_inode_cache       
 12495  10297  82%    0.05K    147       85       588K ftrace_event_field     
 10808  10808 100%    0.07K    193       56       772K Acpi-Operand           
  8260   8260 100%    0.14K    295       28      1180K ext4_groupinfo_4k      
  7199   6261  86%    0.68K    313       23      5008K shmem_inode_cache      
  6426   6426 100%    0.04K     63      102       252K Acpi-Namespace         
  6250   6234  99%    0.62K    250       25      4000K sock_inode_cache       
  6048   6017  99%    0.12K    189       32       756K pid                    
  6016   6016 100%    0.03K     47      128       188K jbd2_revoke_record_s   
  5024   5024 100%    1.00K    157       32      5024K signal_cache           
  2990   2990 100%    0.09K     65       46       260K trace_event_file       
  2984   2914  97%    3.62K    373        8     11936K task_struct            
  2944   2944 100%    0.06K     46       64       184K ext4_io_end            
  2783   2783 100%    0.69K    121       23      1936K files_cache            
  2720   2635  96%    2.00K    170       16      5440K kmalloc-2048           
  2624   2624 100%    0.06K     41       64       164K kmem_cache_node        
  2450   2450 100%    0.31K     98       25       784K kmem_cache             
  2130   2130 100%    2.06K    142       15      4544K sighand_cache          
  2080   2059  98%    4.00K    260        8      8320K kmalloc-4096           
  2006   1938  96%    0.12K     59       34       236K jbd2_journal_head      
  1360   1360 100%    0.02K      8      170        32K numa_policy            
  1155   1155 100%    0.38K     55       21       440K mnt_cache              
   768    768 100%    0.02K      3      256        12K jbd2_revoke_table_s    
   730    730 100%    0.05K     10       73        40K Acpi-Parse             
   680    680 100%    0.05K      8       85        32K jbd2_journal_handle    
   672    672 100%    0.25K     21       32       168K dquot                  
   575    575 100%    0.31K     23       25       184K nf_conntrack           
   561    561 100%    0.08K     11       51        44K Acpi-State             
   546    546 100%    0.10K     14       39        56K blkdev_ioc             
   507    507 100%    0.81K     13       39       416K bdev_cache             
   312    312 100%    0.20K      8       39        64K file_lock_cache        
   306    306 100%    0.94K      9       34       288K UDP                    
   296    296 100%    0.21K      8       37        64K posix_timers_cache     
   280    280 100%    0.56K     10       28       160K task_group             
   276    276 100%    0.69K     12       23       192K squashfs_inode_cache   
   273    273 100%    0.75K     13       21       208K fuse_inode             
   272    264  97%    8.00K     68        4      2176K kmalloc-8192           
   272    235  86%    1.94K     17       16       544K TCP                    
   264    264 100%    0.32K     11       24        88K taskstats              
   264    264 100%    0.24K      8       33        64K tw_sock_TCP            
   256    256 100%    0.12K      8       32        32K ext4_allocation_context
```

---

### 评论 #2 — gstoner (2017-08-07T13:06:17Z)

We looking into this.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: gsedej <notifications@github.com>
Sent: Monday, August 7, 2017 7:30:19 AM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: Re: [RadeonOpenCompute/ROCm] kernel memory leak? (ROCm 1.6.115) (#176)


after running few days over the weekend:
(i did full uninstall and reinstall of rocm)
also my system spec: rx480 8GB, i7 6700, ubuntu 16.04

$ lsmod | grep amd
amdkfd                212992  5
amd_iommu_v2           20480  1 amdkfd
amdgpu               2523136  330
i2c_algo_bit           16384  1 amdgpu
ttm                    94208  1 amdgpu
drm_kms_helper        143360  1 amdgpu
drm                   344064  9 amdgpu,ttm,drm_kms_helper


stays the same as after reboot

$ cat /proc/meminfo
MemTotal:       16383964 kB
MemFree:         1597308 kB
MemAvailable:    4923676 kB
Buffers:         1059516 kB
Cached:          2204912 kB
SwapCached:        25280 kB
Active:          4688088 kB
Inactive:        1544580 kB
Active(anon):    3077868 kB
Inactive(anon):   184328 kB
Active(file):    1610220 kB
Inactive(file):  1360252 kB
Unevictable:          64 kB
Mlocked:              64 kB
SwapTotal:       7609340 kB
SwapFree:        6873852 kB
Dirty:                 8 kB
Writeback:             0 kB
AnonPages:       2939164 kB
Mapped:           322816 kB
Shmem:            293956 kB
Slab:            8191340 kB
SReclaimable:     608476 kB
SUnreclaim:      7582864 kB
KernelStack:       13696 kB
PageTables:        57496 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    15801320 kB
Committed_AS:   10553764 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
HardwareCorrupted:     0 kB
AnonHugePages:   1992704 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:     4455248 kB
DirectMap2M:    12273664 kB
DirectMap1G:           0 kB


7.5 GB of unreclaimable slab

$ sudo slabtop -o
 Active / Total Objects (% used)    : 25592017 / 25754483 (99.4%)
 Active / Total Slabs (% used)      : 889552 / 889552 (100.0%)
 Active / Total Caches (% used)     : 77 / 121 (63.6%)
 Active / Total Size (% used)       : 8464811.48K / 8499206.88K (99.6%)
 Minimum / Average / Maximum Object : 0.01K / 0.33K / 18.62K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
7060536 7060536 100%    0.19K 336216       21   1344864K kmalloc-192
3558192 3557983  99%    0.25K 111194       32    889552K kmalloc-256
3540480 3539806  99%    0.50K 110640       32   1770240K kmalloc-512
3540306 3540306 100%    0.09K  84293       42    337172K kmalloc-96
3537832 3537800  99%    1.00K 110559       32   3537888K kmalloc-1024
3535776 3535616  99%    0.12K 110493       32    441972K kmalloc-128
188175 114247  60%    0.10K   4825       39     19300K buffer_head
 93504  90843  97%    0.06K   1461       64      5844K anon_vma_chain
 86709  53630  61%    0.19K   4129       21     16516K dentry
 85760  78550  91%    0.06K   1340       64      5360K kmalloc-64
 85008  83471  98%    0.19K   4048       21     16192K cred_jar
 56661  55772  98%    0.08K   1111       51      4444K anon_vma
 47736  47736 100%    0.12K   1404       34      5616K kernfs_node_cache
 46208  41086  88%    0.03K    361      128      1444K kmalloc-32
 43008  43008 100%    0.01K     84      512       336K kmalloc-8
 36932  25214  68%    0.57K   1319       28     21104K radix_tree_node
 26040  17010  65%    1.05K    868       30     27776K ext4_inode_cache
 25596  24421  95%    0.58K    948       27     15168K inode_cache
 20736  20736 100%    0.02K     81      256       324K kmalloc-16
 19686   8715  44%    0.04K    193      102       772K ext4_extent_status
 12816  12217  95%    0.65K    534       24      8544K proc_inode_cache
 12495  10297  82%    0.05K    147       85       588K ftrace_event_field
 10808  10808 100%    0.07K    193       56       772K Acpi-Operand
  8260   8260 100%    0.14K    295       28      1180K ext4_groupinfo_4k
  7199   6261  86%    0.68K    313       23      5008K shmem_inode_cache
  6426   6426 100%    0.04K     63      102       252K Acpi-Namespace
  6250   6234  99%    0.62K    250       25      4000K sock_inode_cache
  6048   6017  99%    0.12K    189       32       756K pid
  6016   6016 100%    0.03K     47      128       188K jbd2_revoke_record_s
  5024   5024 100%    1.00K    157       32      5024K signal_cache
  2990   2990 100%    0.09K     65       46       260K trace_event_file
  2984   2914  97%    3.62K    373        8     11936K task_struct
  2944   2944 100%    0.06K     46       64       184K ext4_io_end
  2783   2783 100%    0.69K    121       23      1936K files_cache
  2720   2635  96%    2.00K    170       16      5440K kmalloc-2048
  2624   2624 100%    0.06K     41       64       164K kmem_cache_node
  2450   2450 100%    0.31K     98       25       784K kmem_cache
  2130   2130 100%    2.06K    142       15      4544K sighand_cache
  2080   2059  98%    4.00K    260        8      8320K kmalloc-4096
  2006   1938  96%    0.12K     59       34       236K jbd2_journal_head
  1360   1360 100%    0.02K      8      170        32K numa_policy
  1155   1155 100%    0.38K     55       21       440K mnt_cache
   768    768 100%    0.02K      3      256        12K jbd2_revoke_table_s
   730    730 100%    0.05K     10       73        40K Acpi-Parse
   680    680 100%    0.05K      8       85        32K jbd2_journal_handle
   672    672 100%    0.25K     21       32       168K dquot
   575    575 100%    0.31K     23       25       184K nf_conntrack
   561    561 100%    0.08K     11       51        44K Acpi-State
   546    546 100%    0.10K     14       39        56K blkdev_ioc
   507    507 100%    0.81K     13       39       416K bdev_cache
   312    312 100%    0.20K      8       39        64K file_lock_cache
   306    306 100%    0.94K      9       34       288K UDP
   296    296 100%    0.21K      8       37        64K posix_timers_cache
   280    280 100%    0.56K     10       28       160K task_group
   276    276 100%    0.69K     12       23       192K squashfs_inode_cache
   273    273 100%    0.75K     13       21       208K fuse_inode
   272    264  97%    8.00K     68        4      2176K kmalloc-8192
   272    235  86%    1.94K     17       16       544K TCP
   264    264 100%    0.32K     11       24        88K taskstats
   264    264 100%    0.24K      8       33        64K tw_sock_TCP
   256    256 100%    0.12K      8       32        32K ext4_allocation_context


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/176#issuecomment-320650522>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubVNBeSHN9jre2-Hr94sbGVyspzyks5sVwNagaJpZM4OqrM0>.


---

### 评论 #3 — gsedej (2017-08-17T12:54:06Z)

I did update to `4.11.0-kfd-compute-rocm-rel-1.6-127`, but the leak looks still present. After 1 hour of usage it grew from 88MB to 590MB of unreclaimable.

```
$ cat /proc/meminfo | grep -i -e recl -e slabSlab:             195928 kB
SReclaimable:     107428 kB
SUnreclaim:        88500 kB

1 hour of usage
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             728732 kB
SReclaimable:     153524 kB
SUnreclaim:       575208 kB
$ uptime
 14:48:07 up 57 min,  1 user,  load average: 3,91, 4,07, 3,77
$ uname -a
Linux seraph 4.11.0-kfd-compute-rocm-rel-1.6-127 #1 SMP Wed Aug 2 13:47:23 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux
```

Does anyone else have this issue or is it just me? I might have some weird configuration of system (oibaf ppa, many caffe/ehereum/opencl stuff installed)  

---

### 评论 #4 — gsedej (2017-08-18T10:47:39Z)

I did proper reinstall of rocm, but issue is still present. I did some usage reading trough time.

```
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             190408 kB
SReclaimable:     103340 kB
SUnreclaim:        87068 kB
$ uptime 
 08:56:10 up 0 min,  1 user,  load average: 1,95, 0,68, 0,24

$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             228428 kB
SReclaimable:     117868 kB
SUnreclaim:       110560 kB
(around 10 minutes later)

$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             496488 kB
SReclaimable:     131184 kB
SUnreclaim:       365304 kB
$ uptime 
 09:35:46 up 40 min,  1 user,  load average: 0,32, 0,48, 0,66

$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:            1267656 kB
SReclaimable:     228636 kB
SUnreclaim:      1039020 kB
$ uptime 
 11:03:12 up  2:07,  1 user,  load average: 1,11, 0,87, 0,83

$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:            1437076 kB
SReclaimable:     231128 kB
SUnreclaim:      1205948 kB
$ uptime 
 11:25:18 up  2:30,  1 user,  load average: 1,55, 1,26, 1,08


```

---

### 评论 #5 — gstoner (2017-08-19T18:44:00Z)

 I am working with the Linux kernel driver team on this. 

Greg

---

### 评论 #6 — gsedej (2017-08-21T06:33:27Z)

Thanks. I just wanted to provide more info and status after update.

Anyway, after weekend, 3 days of uptime, "only" 2GB of SUnreclaim. Still bad, but kind of a progress (vs 8GB during past weekend)

```
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:            2851268 kB
SReclaimable:     702244 kB
SUnreclaim:      2149024 kB
$ uptime 
 08:30:08 up 2 days, 23:34,  1 user,  load average: 0,34, 0,62, 0,36
```

---

### 评论 #7 — gstoner (2017-08-21T16:26:34Z)

Do you have any other devices in your system?

What we are seeing with ROCM1.6.3 RC2 (1.6-142) after 3 days of uptime with the same ELM GL board reported the issue is not observed, we check two more test systems but Unreclaim memory is not showing an issue. 

Can you let us know additional services/processes you are running on your system?

Here is what we saw on the same GPU. 
 
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             613276 kB
SReclaimable:     542200 kB
SUnreclaim:        71076 kB
$ uptime
16:51:26 up 3 days, 22:09,  3 users,  load average: 0.00, 0.00, 0.00 

---

### 评论 #8 — gsedej (2017-08-22T08:54:55Z)

I have only 1x RX 480 (sapphire 8GB) on i7 6700 (non-k). The intel integrated gpu should be disabled (lspci does not list it). OS is ubuntu 16.04, running default Unity desktop.

I am also reading gpu temperature/fan with psensor and also "radeon-profile" (graphics interface for radeon/amgdpu setting) to control fan.

So during the weekend I let ethmine work (at manual 1000MHz "powersave"). On friday before i left (2 hours after reboot) it was  "SUnreclaim: 1205948 kB". On monday morning when i come to office it was 2149024 kB. 

During the day I was heavily using browsing and gimp (masking data for neural networks). Firefox with 3 windows and each ~10 tabs (not all tabs are actually loaded). Also the gimp had ~15 images loaded at some point. Before I left home it was 5454200 kB. Next day in the morning (today) 5546952 kB (ethmine was running). At the moment of writing it was already  7790508 kB.

I do have installed oibaf ppa gpu drivers updates to mesa 17.3. I will remove this ppa and try again.

---

### 评论 #9 — gsedej (2017-08-22T09:19:01Z)

Quick update, the ppa removal (purge) did not help. With using ubuntu 16.04 default driver and ROCm, slab usage quickly grows.
```
after reboot
SUnreclaim:       157212 kB
after 15 of usage
SUnreclaim:       355952 kB
```

I will uninstall ROCm and check if it's still problem

---

### 评论 #10 — gsedej (2017-08-22T09:41:58Z)

another update. I ininstalled ROCm completely and ran the default kernel 4.8. The issue is not present.

```
after reboot
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             230964 kB
SReclaimable:     126272 kB
SUnreclaim:       104692 kB

after 15 minutes of usage (firefox, gimp, etc...)
cat /proc/meminfo | grep -i -e recl -e slab
Slab:             236212 kB
SReclaimable:     129772 kB
SUnreclaim:       106440 kB
```

so the issue is not present without ROCm.

I can also install ubuntu kernel 4.11  http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.11/

---

### 评论 #11 — gsedej (2017-08-22T10:11:07Z)

So I did also install the mentioned kernel 4.11 and the issue is not present.

```
gsedej@seraph:~$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             208656 kB
SReclaimable:     109436 kB
SUnreclaim:        99220 kB
$ uptime 
 12:02:43 up 5 min,  1 user,  load average: 0,55, 0,62, 0,32



~$ uptime 
 12:09:22 up 12 min,  1 user,  load average: 0,61, 0,67, 0,45$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             213224 kB
SReclaimable:     112636 kB
SUnreclaim:       100588 kB
```

Can I provide more data?

---

### 评论 #12 — gsedej (2017-08-22T10:26:27Z)

I installed ROCm and the issue becomes present again
```
restart
cat /proc/meminfo | grep -i -e recl -e slab
Slab:             193364 kB
SReclaimable:     103384 kB
SUnreclaim:        89980 kB

after 10 minutes of usage
cat /proc/meminfo | grep -i -e recl -e slab
Slab:             353628 kB
SReclaimable:     119016 kB
SUnreclaim:       234612 kB
```

Just now I saw you asked for **processes and services**. Here is my data:
processes: http://paste.ubuntu.com/25368829/
services: http://paste.ubuntu.com/25368830/


---

### 评论 #13 — gstoner (2017-08-22T13:18:33Z)

Can you tell us what motherboard you are using.   It might be driver interaction

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: gsedej <notifications@github.com>
Sent: Tuesday, August 22, 2017 4:19:02 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] kernel memory leak? (ROCm 1.6.115) (#176)


Quick update, the ppa removal (purge) did not help. With using ubuntu 16.04 default driver and ROCm, slab usage quickly grows.

after reboot
SUnreclaim:       157212 kB
after 15 of usage
SUnreclaim:       355952 kB


I will uninstall ROCm and check if it's still problem

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/176#issuecomment-323969186>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQgrAvr5JCXLgyi1sFud4KPpuDduks5sap0GgaJpZM4OqrM0>.


---

### 评论 #14 — gstoner (2017-08-22T13:18:33Z)

I spend some time on our servers to see if I can replicate this personally.    Let you know what I find.  I have five servers same config I am working with

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: gsedej <notifications@github.com>
Sent: Tuesday, August 22, 2017 5:26:29 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] kernel memory leak? (ROCm 1.6.115) (#176)


I installed ROCm and the issue becomes present again

restart
cat /proc/meminfo | grep -i -e recl -e slab
Slab:             193364 kB
SReclaimable:     103384 kB
SUnreclaim:        89980 kB

after 10 minutes of usage
cat /proc/meminfo | grep -i -e recl -e slab
Slab:             353628 kB
SReclaimable:     119016 kB
SUnreclaim:       234612 kB


Just now I saw you asked for processes and services. Here is my data:
processes: http://paste.ubuntu.com/25368829/
services: http://paste.ubuntu.com/25368830/

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/176#issuecomment-323985770>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Dudqgw0SAE5doP89A9MpvWzLGWIkzks5saqzVgaJpZM4OqrM0>.


---

### 评论 #15 — gsedej (2017-08-22T13:28:16Z)

The motherboard is Gigabyte Z170-HD3P https://www.gigabyte.com/Motherboard/GA-Z170-HD3P-rev-10#ov

The bios is updated to the lastest.

Try to use as desktop. It might be related to some features that that are not in mailine kernel, like DAL/DC (display abastract layer) or audio over display port.

---

### 评论 #16 — gstoner (2017-08-22T13:31:53Z)

Yes, it could be in these outer components.  Let me see if the core is leaking first then we layer in the Desktop components 

---

### 评论 #17 — gsedej (2017-10-12T09:50:47Z)

So I disabled "audio" and "DC" in kernel and **there is no more leak**.

What I did is modified grub config in `/ect/default/grub`
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.vm_fragment_size=9 amdgpu.audio=0 amdgpu.dc=0"
```
and then
`sudo update-grub`
_note: I also enabled big memory fragments_


---

### 评论 #18 — gstoner (2017-10-13T01:08:09Z)

That was a pretty crazy debug 

thank you. 

---

### 评论 #19 — manifesti (2017-10-13T03:02:51Z)

I seem to be running against the exact same problem as @gsedej.

I have 2x RX 570 mining with xmr-stak-amd, and after a days worth of mining and general computing on the side, "something" fills my RAM (and swap). I'm unable to even open a static page in a browser without waiting for a minute, much less keep Atom on at the same time. 

I tried the fix in gsedejs post, but all that got me was a black screen upon rebooting (I didn't enable big memory fragments though).

Here is my /proc/meminfo right after a reboot (will probably update with the clogged one for comparison once I wake up)

OS is Ubuntu 16.04.3, processor is an i5-4430.
```
MemTotal:        8077152 kB
MemFree:         4690520 kB
MemAvailable:    5862476 kB
Buffers:          252848 kB
Cached:          1115320 kB
SwapCached:            0 kB
Active:          1978924 kB
Inactive:         834908 kB
Active(anon):    1446988 kB
Inactive(anon):    56848 kB
Active(file):     531936 kB
Inactive(file):   778060 kB
Unevictable:          48 kB
Mlocked:              48 kB
SwapTotal:       9797628 kB
SwapFree:        9797628 kB
Dirty:              2380 kB
Writeback:             0 kB
AnonPages:       1341252 kB
Mapped:           426196 kB
Shmem:             58176 kB
Slab:             257036 kB
SReclaimable:     166476 kB
SUnreclaim:        90560 kB
KernelStack:        9968 kB
PageTables:        37992 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    13836204 kB
Committed_AS:    5784536 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
HardwareCorrupted:     0 kB
AnonHugePages:    339968 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:      338044 kB
DirectMap2M:     4808704 kB
DirectMap1G:     3145728 kB
```

---

### 评论 #20 — gsedej (2017-10-13T06:26:46Z)

So just to confirm, the issue is not present when disabling audio and dc. It still need to be tested wheter of those make leak. Currently I can't use HDMI/DP audio on monitor, so it's still affects me.

The DAL/DC (+audio) looks like it's going to merge in kernel 4.15 or 4.16, which means the bugs can be reported directly to kernel modul developers. Currently, probably no one cares, since ROCm is using old kernel 4.11 (now it's soon going to be released 4.14 ).

The numbers:
```
$ cat /proc/meminfo | grep -i -e recl -e slab
Slab:             181700 kB
SReclaimable:      97832 kB
SUnreclaim:        83868 kB
up 1 min,

$ date; uptime; cat /proc/meminfo | grep -i -e recl -e slab
 11:28:15 **up 10 min**,  1 user,  load average: 0,28, 0,40, 0,27
Slab:             209032 kB
SReclaimable:     118676 kB
SUnreclaim:        90356 kB

$ date; uptime; cat /proc/meminfo | grep -i -e recl -e slab
 11:56:30 up 38 min,  1 user,  load average: 0,58, 0,64, 0,60
Slab:             228584 kB
SReclaimable:     132664 kB
SUnreclaim:        95920 kB

$ date; uptime; cat /proc/meminfo | grep -i -e recl -e slab
 13:54:04 up  2:36,  1 user,  load average: 1,15, 0,51, 0,52
Slab:             263324 kB
SReclaimable:     159060 kB
SUnreclaim:       104264 kB

$ date; uptime; cat /proc/meminfo | grep -i -e recl -e slab
 08:17:26 up 20:59,  1 user,  load average: 0,61, 0,24, 0,13
Slab:             739712 kB
SReclaimable:     630036 kB
SUnreclaim:       109676 kB
```
The  `SUnreclaim` grow just around 20MB, compared to few hundred/day.

---

### 评论 #21 — gstoner (2017-10-13T10:39:48Z)

With 1.6.4 here is what I am seeing.     We care, I just have to work with another team to address the issue,  we source our core Linux driver from the Linux team it is shared component we roll the ROCm userland on.  

fpadmin@rocm-p47:~/miopen-benchmark$ lsmod | grep amd
amd64_edac_mod         28672  0
edac_mce_amd           28672  1 amd64_edac_mod
edac_core              53248  2 amd64_edac_mod
kvm_amd              2179072  0
kvm                   581632  1 kvm_amd
amdkfd                212992  4
amd_iommu_v2           20480  1 amdkfd
amdgpu               2523136  0
i2c_algo_bit           16384  2 amdgpu,ast
ttm                    94208  2 amdgpu,ast
drm_kms_helper        143360  2 amdgpu,ast
drm                   344064  5 amdgpu,ast,ttm,drm_kms_helper

---
