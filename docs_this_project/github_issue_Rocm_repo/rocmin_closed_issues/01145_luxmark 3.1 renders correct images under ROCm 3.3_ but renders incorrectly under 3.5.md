# luxmark 3.1 renders correct images under ROCm 3.3, but renders incorrectly under 3.5

- **Issue #:** 1145
- **State:** closed
- **Created:** 2020-06-10T18:00:38Z
- **Updated:** 2021-09-13T04:55:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/1145

I've checked ROCm 2.10, 3.0, 3.1, 3.3, and 3.5 by running luxmark 3.1. ROCm versions 2.10 up to 3.3 run just fine, and produce correct images (luxmark checks if the resulting images are correct).

However, 3.5 produces the following incorrect image.

![Screenshot from 2020-06-10 18-58-56](https://user-images.githubusercontent.com/2095835/84300929-3f3fc300-ab53-11ea-8fe3-84d2ea6ef1d8.png)

The black parts are incorrect. The builtin check shows the following result:

![Screenshot from 2020-06-10 19-52-50](https://user-images.githubusercontent.com/2095835/84301402-ffc5a680-ab53-11ea-90b5-2a0367185133.png)

ROCm 3.3, and earlier ran fine, as does luxmark 4.0 under any version of ROCm from 2.10 up to 3.5. Oddly enough, if I run LuxVR from within luxmark, it runs correctly.

![Screenshot from 2020-06-10 19-56-21](https://user-images.githubusercontent.com/2095835/84301745-97c39000-ab54-11ea-9b4b-96faa90c1be4.png)
