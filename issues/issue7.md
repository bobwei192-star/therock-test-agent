
项目设计未能考虑 wsl2环境下测试 如下 典型而wsl2环境
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ uname -a
Linux NucBoxEVO-X2 6.18.35.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Wed Jun 17 23:14:00 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/dxg
crw-rw-rw- 1 root root 10, 258 Jul 15 15:21 /dev/dxg
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/dri
ls: cannot access '/dev/dri': No such file or directory
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/kfd
ls: cannot access '/dev/kfd': No such file or directory
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$