# Missing aufs kernel module in ROCm kernel makes running docker daemon much harder

- **Issue #:** 53
- **State:** closed
- **Created:** 2016-12-09T07:25:49Z
- **Updated:** 2017-01-04T14:06:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/53

Current ROCm distribution of Linux kernel (4.6.0-kfd-compute-rocm-rel-1.3-74) doesn't provide kernel module for aufs file system. This makes docker daemon fail when starting and makes the description (https://github.com/RadeonOpenCompute/ROCm-docker) of installation of docker containers on the ROCm kernel incomplete.

systemctl status docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since pią 2016-12-09 08:22:57 CET; 5s ago
     Docs: https://docs.docker.com
  Process: 2911 ExecStart=/usr/bin/dockerd -H fd:// $DOCKER_OPTS (code=exited, status=1/FAILURE)
 Main PID: 2911 (code=exited, status=1/FAILURE)

gru 09 08:22:56 computer systemd[1]: Starting Docker Application Container Engine...
gru 09 08:22:56 computer dockerd[2911]: time="2016-12-09T08:22:56.334816244+01:00" level=info msg="libcontainerd: new containerd process, pid: 2923"
gru 09 08:22:57 computer dockerd[2911]: time="2016-12-09T08:22:57.394559569+01:00" level=error msg="[graphdriver] prior storage driver \"aufs\" failed: driver not supported"
gru 09 08:22:57 computer dockerd[2911]: time="2016-12-09T08:22:57.394752192+01:00" level=fatal msg="Error starting daemon: error initializing graphdriver: driver not supported"
gru 09 08:22:57 computer systemd[1]: docker.service: Main process exited, code=exited, status=1/FAILURE
gru 09 08:22:57 computer systemd[1]: Failed to start Docker Application Container Engine.
gru 09 08:22:57 computer systemd[1]: docker.service: Unit entered failed state.
gru 09 08:22:57 computer systemd[1]: docker.service: Failed with result 'exit-code'.
