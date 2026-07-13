# Paths convention within /opt/rocm/ 

- **Issue #:** 647
- **State:** closed
- **Created:** 2018-12-24T12:31:20Z
- **Updated:** 2019-10-22T15:42:09Z
- **URL:** https://github.com/ROCm/ROCm/issues/647

Can someone fix paths within a framework. 
There are a lot of mess like:
`/opt/rocm/[something]/include` and `/opt/rocm/include/[something]/`
`/opt/rocm/[something]/bin` and `/opt/rocm/bin/[something]/`
They differ per project and always are hardcoded.

It's strange to see [below] in TensorFlow code.
```
   # Add MIOpen headers
   inc_dirs.append("/opt/rocm/miopen/include")	  
    # Add rtg headers
   inc_dirs.append("/opt/rocm/include/migraph")
``` 

Same with build scripts.  