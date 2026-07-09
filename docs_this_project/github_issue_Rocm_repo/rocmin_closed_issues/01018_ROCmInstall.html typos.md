# ROCmInstall.html typos

- **Issue #:** 1018
- **State:** closed
- **Created:** 2020-02-21T12:28:56Z
- **Updated:** 2020-12-01T17:46:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1018

not sure what happened over at https://rocm.github.io/ROCmInstall.html
but it looks like some "|" pipe characters are not there, or rendering anymore

```
	echo 'ADD_EXTRA_GROUPS=1' 		
 sudo tee -a /etc/adduser.conf   
	echo 'EXTRA_GROUPS=video' 		
 sudo tee -a /etc/adduser.conf
```

this doesn't make sense as it's missing the pipe before "sudo"