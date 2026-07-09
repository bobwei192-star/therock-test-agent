# [Issue]: Problem loading repodata

- **Issue #:** 5593
- **State:** closed
- **Created:** 2025-10-29T09:26:53Z
- **Updated:** 2025-11-11T19:07:56Z
- **Labels:** status: assessed
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5593

### Problem Description

Hi, 

it seems some of the repo.radeon.com akamai edges are not synced, i get on some of our boxes (depending on internet connection it seems) a 404 for 

```
$ curl --fail-with-body https://repo.radeon.com/amdgpu/7.0.2/rhel/8.10/main/x86_64/repodata/repomd.xml 
<html>
<head><title>404 Not Found</title></head>
<body>
<h1>Release notes</h1>
For information on available ROCm releases, please refer to the
<a href="https://rocm.docs.amd.com/en/latest/">
ROCm Release Notes</a><p>
For information on available Radeon Software for Linux releases,
please refer to
<a href="https://www.amd.com/en/support/download/linux-drivers.html">
Linux&reg; Drivers for AMD Radeon&trade; and Radeon PRO&trade; Graphics</a>.<p>
</body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
```

(also fails in `dnf` )

it is resolving repo.radeon.com like this:

```
$ dig repo.radeon.com                                                                                                                                                                                                                                                            22 ↵

; <<>> DiG 9.20.11-1ubuntu2-Ubuntu <<>> repo.radeon.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58234
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 3

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;repo.radeon.com.               IN      A

;; ANSWER SECTION:
repo.radeon.com.        14      IN      CNAME   repo.radeon.com.edgekey.net.
repo.radeon.com.edgekey.net. 14 IN      CNAME   e40210.dscd.akamaiedge.net.
e40210.dscd.akamaiedge.net. 14  IN      A       95.101.35.210
e40210.dscd.akamaiedge.net. 14  IN      A       95.101.35.186
```

while other boxes that resolve the host different are working, e.g.:

```
$ dig repo.radeon.com

; <<>> DiG 9.20.11-0ubuntu0.2-Ubuntu <<>> repo.radeon.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25447
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;repo.radeon.com.		IN	A

;; ANSWER SECTION:
repo.radeon.com.	8574	IN	CNAME	repo.radeon.com.edgekey.net.
repo.radeon.com.edgekey.net. 12224 IN	CNAME	e40210.dscd.akamaiedge.net.
e40210.dscd.akamaiedge.net. 18	IN	A	2.21.79.32
```

this one works fine and returns the repo data

### Operating System

Ubuntu 25.10 (Questing Quokka)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### ROCm Version

ROCm 7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_