# MIOpen does not build due to missing sqlite3

- **Issue #:** 1379
- **State:** closed
- **Created:** 2021-02-11T22:28:09Z
- **Updated:** 2021-05-31T11:16:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1379

Even after sqlite3 installed, it is not building. It not clear what particular sqlite3 it is asking for.

apt install sqlite3

Reading package lists... 0%

Reading package lists... 100%

Reading package lists... Done


Building dependency tree... 0%

Building dependency tree... 0%

Building dependency tree... 50%

Building dependency tree... 50%

Building dependency tree       


Reading state information... 0%

Reading state information... 0%

Reading state information... Done

The following package was automatically installed and is no longer required:
  libfprint-2-tod1
Use 'sudo apt autoremove' to remove it.
Suggested packages:
  sqlite3-doc
The following NEW packages will be installed:
  sqlite3
0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.
Need to get 860 kB of archives.
After this operation, 2,803 kB of additional disk space will be used.

0% [Working]
            
Get:1 http://us.archive.ubuntu.com/ubuntu focal-updates/main amd64 sqlite3 amd64 3.31.1-4ubuntu0.2 [860 kB]

1% [1 sqlite3 14.2 kB/860 kB 2%]
                                
100% [Working]
              
Fetched 860 kB in 1s (1,255 kB/s)

Selecting previously unselected package sqlite3.
(Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 271130 files and directories currently installed.)
Preparing to unpack .../sqlite3_3.31.1-4ubuntu0.2_amd64.deb ...
Progress: [  0%] [.............................................................................................................................] Progress: [ 20%] [#########################....................................................................................................] Unpacking sqlite3 (3.31.1-4ubuntu0.2) ...
Progress: [ 40%] [##################################################...........................................................................] Setting up sqlite3 (3.31.1-4ubuntu0.2) ...
Progress: [ 60%] [###########################################################################..................................................] Progress: [ 80%] [####################################################################################################.........................] Processing triggers for man-db (2.9.1-1) ...

:~/ROCm/MIOpen/build# sudo apt install sqlite3apt-cache search sqlitesearchsqlitecmake -DMIOPEN_BACKEND=OpenCL ..
-- Checking for module 'sqlite3'
--   No package 'sqlite3' found
CMake Error at /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:463 (message):
  A required package was not found
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:643 (_pkg_check_modules_internal)
  CMakeLists.txt:60 (pkg_check_modules)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm/MIOpen/build/CMakeFiles/CMakeOutput.log".
:~/ROCm/MIOpen/build# sqlite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> quit()
   ...> ^C^C^Croot@guyen-Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpen/build# dpkg -l | grep sqlite3
ii  libsqlite3-0:amd64                         3.31.1-4ubuntu0.2                            amd64        SQLite 3 shared library
ii  sqlite3                                    3.31.1-4ubuntu0.2                            amd64        Command line interface for SQLite 3


:~/ROCm/MIOpen/build# cmake -DMIOPEN_BACKEND=OpenCL ..
-- The C compiler identification is GNU 9.3.0
-- The CXX compiler identification is GNU 9.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Checking for module 'sqlite3'
--   No package 'sqlite3' found
CMake Error at /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:463 (message):
  A required package was not found
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPkgConfig.cmake:643 (_pkg_check_modules_internal)
  CMakeLists.txt:60 (pkg_check_modules)


-- Configuring incomplete, errors occurred!


