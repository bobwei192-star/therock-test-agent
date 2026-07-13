# GPG issue on ubuntu

- **Issue #:** 2362
- **State:** closed
- **Created:** 2023-08-02T21:40:21Z
- **Updated:** 2023-12-11T22:39:32Z
- **Assignees:** Naraenda
- **URL:** https://github.com/ROCm/ROCm/issues/2362

I followed https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/install.html to re-add key but I keep getting
```
The following signatures were invalid: EXPKEYSIG 9386B48A1A693C5C James Adrian Edwards (ROCm Release Manager) <JamesAdrian.Edwards@amd.com>
```
I tried to verify the key and got
```
sha1sum /etc/apt/keyrings/rocm.gpg 
ececf5eea22ced391975f46ba3e11ad58a12c794  /etc/apt/keyrings/rocm.gpg
```
which is different from 73f5d8100de6048aa38a8b84cd9a87f05177d208 mentioned in https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/install.html

How to fix this?
