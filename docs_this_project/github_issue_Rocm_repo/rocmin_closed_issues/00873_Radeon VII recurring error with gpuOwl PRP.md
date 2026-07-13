# Radeon VII recurring error with gpuOwl PRP

- **Issue #:** 873
- **State:** closed
- **Created:** 2019-08-23T05:24:41Z
- **Updated:** 2023-12-18T22:24:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/873

At first I have ignored this error thinking it was a buggy gpu, but now with the second Radeon VII it is happening exactly the same error: all-zero residues, like if the program is reading from some wrong location, or a memory page has been evicted underneath.
(non-zero residues redacted).
System: Debian 10

2019-08-23 07:08:23 90166123    73860000 81.91%;  996 us/sq; ETA 0d 04:31; xxxxxxxxxxxxxxxx
2019-08-23 07:08:33 90166123    73870000 81.93%;  996 us/sq; ETA 0d 04:30; xxxxxxxxxxxxxxxx
 2019-08-23 07:08:43 90166123    73880000 81.94%;  993 us/sq; ETA 0d 04:29; 0000000000000000                                                 
 2019-08-23 07:08:53 90166123    73890000 81.95%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:03 90166123    73900000 81.96%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:13 90166123    73910000 81.97%;  991 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:23 90166123    73920000 81.98%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:33 90166123    73930000 81.99%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:09:43 90166123    73940000 82.00%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:09:53 90166123    73950000 82.01%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:03 90166123    73960000 82.03%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:12 90166123    73970000 82.04%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:22 90166123    73980000 82.05%;  991 us/sq; ETA 0d 04:27; 0000000000000000                                                 
2019-08-23 07:10:32 90166123    73990000 82.06%;  991 us/sq; ETA 0d 04:27; 0000000000000000                                                 
2019-08-23 07:10:43 90166123 EE 74000000 82.07%;  992 us/sq; ETA 0d 04:27; 0000000000000000 (check 1.10s)                                   
2019-08-23 07:10:43 90166123.owl loaded: k 73000000, block 1000, res64 xxxxxxxxxxxxxxxx
2019-08-23 07:10:55 90166123    73010000 80.97%; 1133 us/sq; ETA 0d 05:24; xxxxxxxxxxxxxxxx
