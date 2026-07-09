# Bristol Ridge.- Asrock A320M PRO4 system: vector_copy runs OK from console, but hangs in an ssh terminal

- **Issue #:** 191
- **State:** closed
- **Created:** 2017-08-31T16:14:07Z
- **Updated:** 2017-09-06T10:44:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/191

**EDIT: To summarize, disabling MSI interrupt mode caused a number of things to stop hanging.**

Has anyone seen this? I have vector_copy running OK in a local login console. When I ssh to the same machine, as the same user, running the same binary, it hangs after "Dispatching the kernel succeeded":

john@dash80:~/foo/sample$ ./vector_copy 
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx801.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
^C

... until I CTRL-C it. These are the only differences in environment variables, they look innocuous to me:

$ diff env.broke env.ok
> HUSHLOGIN=FALSE
7,16d7
< LANGUAGE=en_US:en
< LC_ADDRESS=en_US.UTF-8
< LC_IDENTIFICATION=en_US.UTF-8
< LC_MEASUREMENT=en_US.UTF-8
< LC_MONETARY=en_US.UTF-8
< LC_NAME=en_US.UTF-8
< LC_NUMERIC=en_US.UTF-8
< LC_PAPER=en_US.UTF-8
< LC_TELEPHONE=en_US.UTF-8
< LC_TIME=en_US.UTF-8
30,33c21
< SSH_CLIENT=10.1.10.10 58700 22
< SSH_CONNECTION=10.1.10.10 58700 10.1.10.139 22
< SSH_TTY=/dev/pts/0
< TERM=xterm
---
> TERM=linux
38,39c26,29
< XDG_SESSION_COOKIE=82e17aa530f16aa39d3f90245120ccef-1504192969.909757-1513324773
< XDG_SESSION_ID=2
---
> XDG_SEAT=seat0
> XDG_SESSION_COOKIE=82e17aa530f16aa39d3f90245120ccef-1504192925.158758-1897242416
> XDG_SESSION_ID=1
> XDG_VTNR=1

Before I spend time on this, is it a known issue? This should work, right?

FWIW, after the hang, I can still run vector_copy at the local console and it runs fine. I can even run it at the console _while another vector_copy instance in the ssh is hanging_ and it runs fine on the console. So the GPU isn't getting completely hung; it's probably not a CP hang.

Thanks
John