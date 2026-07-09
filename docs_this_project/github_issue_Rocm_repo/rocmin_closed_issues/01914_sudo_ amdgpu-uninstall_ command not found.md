# sudo: amdgpu-uninstall: command not found

- **Issue #:** 1914
- **State:** closed
- **Created:** 2023-03-03T12:47:46Z
- **Updated:** 2024-06-27T13:21:15Z
- **Labels:** Documentation
- **Assignees:** MathiasMagnus
- **URL:** https://github.com/ROCm/ROCm/issues/1914

Trying to get rocm working for something ai related, I'm on ubuntu 22.10, ran these commands 

> sudo apt-get update
> wget https://repo.radeon.com/amdgpu-install/5.4.3/ubuntu/jammy/amdgpu-install_5.4.50403-1_all.deb 
> sudo apt-get install ./amdgpu-install_5.4.50403-1_all.deb

At the end it puts "download is performed unsandboxed as root as file"

But when I check it says I have it installed 

![image](https://user-images.githubusercontent.com/15861396/222723770-d106d964-38b9-4f07-86e4-869e46c9670e.png)

I'm trying to remove it for troubleshooting with "sudo amdgpu-uninstall --rocmrelease=5.4.3" but it says "sudo: amdgpu-uninstall: command not found"

Why is that?
