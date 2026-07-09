# Cannot install HCC deb package on ASROCK

- **Issue #:** 541
- **State:** closed
- **Created:** 2018-09-16T22:56:26Z
- **Updated:** 2018-09-17T02:08:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/541

I updated to 18.10 and encountered the following error while installing rocm.

Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hcc amd64 1.2.18354 [304 MB]
58% [1 hcc 220 MB/304 MB 72%]                                                                                                                                         727 kB/s 1min 55s^Fetched 304 MB in 5min 15s (965 kB/s)
(Reading database ... 132208 files and directories currently installed.)
Preparing to unpack .../hcc_1.2.18354_amd64.deb ...
Unpacking hcc (1.2.18354) ...
dpkg-deb (subprocess): decompressing archive member: internal gzip read error: '<fd:4>: incorrect data check'
dpkg-deb: error: <decompress> subprocess returned error exit status 2
dpkg: error processing archive /var/cache/apt/archives/hcc_1.2.18354_amd64.deb (--unpack):
 cannot copy extracted data for './opt/rocm/hcc/share/scan-view/ScanView.py' to '/opt/rocm/hcc/share/scan-view/ScanView.py.dpkg-new': unexpected end of file or stream
Errors were encountered while processing:
 /var/cache/apt/archives/hcc_1.2.18354_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)

I've tried the following:

apt --fix-broken install 
apt install -f
apt-get clean and reinstalling but i encounter the same error.

System specs:
ASRock x399 | 1950x | Vega Frontier | 4.18.0-7-generic

The same packages were just installed sucessfully on an MSI  x399 rig. 