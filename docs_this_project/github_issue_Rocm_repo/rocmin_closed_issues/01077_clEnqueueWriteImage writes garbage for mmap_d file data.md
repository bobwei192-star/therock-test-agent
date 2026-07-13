# clEnqueueWriteImage writes garbage for mmap'd file data

- **Issue #:** 1077
- **State:** closed
- **Created:** 2020-04-08T02:12:33Z
- **Updated:** 2021-03-17T08:08:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1077

I tried to use `mmap()` to load raw float32 image data but it didn't work.

Here is an excerpt from my OpenCL program.  Works fine on CPU (pocl) whether `USE_MMAP` is defined or not. On GPU (rocm) it works only when `USE_MMAP` is *not* defined.  On GPU with `USE_MMAP` defined, the image contains uninitialized garbage data, verified by comparing to CPU the 1x1 reduction level from later code (not shown here).  The results on GPU with `USE_MMAP` are different each run.

```
  // load image
  {
#ifdef USE_MMAP
    int fd = open(input_filename, O_RDONLY);
    if (fd == -1)
    {
      abort();
    }
    float *ptr = mmap
      (NULL, bytes, PROT_READ, MAP_PRIVATE | MAP_POPULATE, fd, 0);
    if (ptr == MAP_FAILED)
    {
      abort();
    }
#else
    size_t bytes = sizeof(float) * 4 * input_width * input_height;
    float *ptr = malloc(bytes);
    if (! ptr)
    {
      abort();
    }
    FILE *f = fopen(input_filename, "rb");
    if (! f)
    {
      abort();
    }
    if (1 != fread(ptr, bytes, 1, f))
    {
      abort();
    }
    fclose(f);
#endif
    size_t origin[3] = { 0, 0, 0 };
    size_t region[3] = { input_width, input_height, 1 };
    E(clEnqueueWriteImage
      ( queue, image[0], CL_TRUE, origin, region, 0, 0, ptr
      , 0, NULL, &e_mipmap_reduce[0]
      ));
#ifdef USE_MMAP
    munmap(ptr, bytes);
    close(fd);
#else
    free(ptr);
#endif
  }
```

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux bullseye/sid
Release:	testing
Codename:	bullseye
```

```
$ uname -a
Linux eiskaffee 5.4.0-4-amd64 #1 SMP Debian 5.4.19-1 (2020-02-13) x86_64 GNU/Linux
```

```
$ apt-cache policy rocm-dev
rocm-dev:
  Installed: 3.3.0-19
  Candidate: 3.3.0-19
  Version table:
 *** 3.3.0-19 500
        500 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
        100 /var/lib/dpkg/status
```

GPU is AMD Radeon RX 580.