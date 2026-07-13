# vector_copy: Create the program failed

- **Issue #:** 124
- **State:** closed
- **Created:** 2017-05-17T13:43:39Z
- **Updated:** 2017-07-09T08:10:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/124

What is going wrong here? vector_copy on my Ryzen CPU + R9 480 GPU stops prematurely at the HSA finalizer loading stage:
```
./vector_copy
Profiling of privileged counters is not available
Profiling is not available
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program failed.
```