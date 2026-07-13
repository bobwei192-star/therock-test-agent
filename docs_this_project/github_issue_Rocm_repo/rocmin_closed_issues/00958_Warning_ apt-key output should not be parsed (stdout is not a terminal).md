# Warning: apt-key output should not be parsed (stdout is not a terminal)

- **Issue #:** 958
- **State:** closed
- **Created:** 2019-12-05T19:28:30Z
- **Updated:** 2019-12-05T23:02:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/958

I am having trouble adding the ROCm apt repository.

after entering:
```
wget -qO – http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | 
sudo apt-key add -echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | 
sudo tee /etc/apt/sources.list.d/rocm.list
```
The warning message starting with:
> Warning: apt-key output should not be parsed (stdout is not a terminal)

is outputted into the rocm.list file too.

Is there another way to add this repository?

I am on Ubuntu 19.10 if that is relevant