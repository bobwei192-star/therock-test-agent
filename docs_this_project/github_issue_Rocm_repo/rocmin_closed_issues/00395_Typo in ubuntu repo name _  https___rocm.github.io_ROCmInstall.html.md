# Typo in ubuntu repo name @  https://rocm.github.io/ROCmInstall.html

- **Issue #:** 395
- **State:** closed
- **Created:** 2018-04-25T21:42:14Z
- **Updated:** 2018-04-25T21:45:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/395

    wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
    sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'

should be

    wget -qO - http://repo.radeon.com/rocm/apt/debian/debian/rocm.gpg.key | sudo apt-key add -
    sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'