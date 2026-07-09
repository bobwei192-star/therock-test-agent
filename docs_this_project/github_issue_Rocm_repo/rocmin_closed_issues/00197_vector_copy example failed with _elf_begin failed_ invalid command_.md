# vector_copy example failed with "elf_begin failed: invalid command"

- **Issue #:** 197
- **State:** closed
- **Created:** 2017-09-05T09:25:14Z
- **Updated:** 2018-06-03T15:03:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/197

Hi.
I have installed rocm 1.6 and trying vector_copy test but it failed:
beasterio@beasterio-pc:~/test$ ./vector_copy 
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
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
elf_begin failed: invalid command

Finalizing the program failed.

in test it uses vector_copy_base.brig, so maybe its not valid.

HelloWorld example works fine. I tried also HIP examples and they are ok too.
Ubuntu 16.04, video - Radeon rx 480.