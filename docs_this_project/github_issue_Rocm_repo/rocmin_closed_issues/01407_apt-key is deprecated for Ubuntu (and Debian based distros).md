# apt-key is deprecated for Ubuntu (and Debian based distros)

- **Issue #:** 1407
- **State:** closed
- **Created:** 2021-03-16T13:25:42Z
- **Updated:** 2021-03-22T11:18:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/1407

When you follow the installation instructions you get:

```sh
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
```

Helpful documentation:
https://www.linuxuprising.com/2021/01/apt-key-is-deprecated-how-to-add.html

Instructions should be changed to something like:

```sh
wget -O- https://repo.radeon.com/rocm/rocm.gpg.key | gpg --dearmor > rocm.gpg
sudo mv rocm.gpg /usr/share/keyrings/
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian/ xenial main' |\
  sudo tee -a /etc/apt/sources.list.d/rocm.list
```