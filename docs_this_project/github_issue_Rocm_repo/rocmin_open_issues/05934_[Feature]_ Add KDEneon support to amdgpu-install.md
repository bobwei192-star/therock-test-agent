# [Feature]: Add KDEneon support to amdgpu-install

- **Issue #:** 5934
- **State:** open
- **Created:** 2026-02-06T10:34:33Z
- **Updated:** 2026-02-06T15:17:46Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/5934

### Suggestion Description

The `amdgpu-install` checks the distribution via the `/etc/os-release` file. Like other distributions KDE neon does change the `ID` parameter which causes the installation to fail.

In the past I did always manually patch the `amdgpu-install` file to simply include `neon` as a possible option for the `debian` based switch (see below). This works flawlessly since KDE neon is Debian based.

```bash
    # [...]
	case "$ID" in
		ubuntu|linuxmint|debian|neon)
			PKGUPDATE="apt-get update"
			PKGMAN=apt-get
			OS_CLASS=debian
			:
			;;
    # [...]
```

This does get quite cumbersome with time as I have to manually patch the files every time I want to install updates. I'm rather confident we can just add the KDEneon identifier as it has already been working without issues for more than two years now.

New users and not so advanced users might face a challenge they are not able to overcome to use the amd drivers on their KDE neon system.


### Operating System

KDE neon 6.5.5

### GPU

_No response_

### ROCm Component

_No response_