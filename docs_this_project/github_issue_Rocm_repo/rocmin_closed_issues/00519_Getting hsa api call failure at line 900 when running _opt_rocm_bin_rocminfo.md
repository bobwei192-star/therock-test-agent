# Getting hsa api call failure at line 900 when running /opt/rocm/bin/rocminfo 

- **Issue #:** 519
- **State:** closed
- **Created:** 2018-09-01T18:35:00Z
- **Updated:** 2018-09-17T23:27:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/519

I have installed rocm-dkms in my ubuntu os 16.04 LTS as per the instructions.

When I run the command /opt/rocm/bin/rocminfo I am getting the error
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

When I run /opt/rocm/opencl/bin/x86_64/clinfo, I am getting the error
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

uname -a gives:
Linux babu-Inspiron-5548 4.15.0-33-generic #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

I am getting the below error messages in some the crash files that got generated today.
In _usr_share_apport_apport-gtk.1000.crash

I am getting the error 
```
PythonArgs: ['/usr/share/apport/apport-gtk']
Traceback:
 Traceback (most recent call last):
   File "/usr/share/apport/apport-gtk", line 597, in <module>
     app.run_argv()
   File "/usr/lib/python3/dist-packages/apport/ui.py", line 688, in run_argv
     return self.run_crashes()
   File "/usr/lib/python3/dist-packages/apport/ui.py", line 239, in run_crashes
     logind_session[1] > self.report.get_timestamp():
 TypeError: unorderable types: float() > NoneType()
UserGroups: adm cdrom dip lpadmin plugdev sambashare sudo video
_LogindSession: c2
```




Could you please help
