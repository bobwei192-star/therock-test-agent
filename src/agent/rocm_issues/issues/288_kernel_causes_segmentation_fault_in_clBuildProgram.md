# kernel causes segmentation fault in clBuildProgram

> **Issue #288**
> **状态**: closed
> **创建时间**: 2017-12-27T23:12:59Z
> **更新时间**: 2018-02-22T21:53:34Z
> **关闭时间**: 2018-02-22T21:53:34Z
> **作者**: Moading
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/288

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Hi,
I'm running ROCm 1.7  with the following configuration:
Ubuntu 16.04.3, Xeon E5-2680 V3, Supermicro X10SRA-F, AMD Radeon Pro Duo (Polaris)
The setup is working and I can run OpenCL programs. ROCm is awesome!

However, one of my more complex OpenCL kernels causes a segmentation fault when calling clBuildProgram. I have generated a small program (bug.cpp) that demonstrates the problem. That program creates a context, reads the kernel from hello.cl and builds the program. 

The following command was used for compilation:
g++ bug.cpp -I/opt/rocm/opencl/include/ -L/opt/rocm/opencl/lib/x86_64/ -lOpenCL

This program works on another system (different hardware, different OS, different driver, lol).

The program runs fine in ROCm 1.7 when I remove all the lines containing the array "SM" from the OpenCL kernel. I know the kernel dos not make any sense and it contains unused variables. This is because the original kernel was reduced in order to demonstatrate the problem.




Code of bug.cpp:


#include <stdio.h>
#include <stdlib.h>

#include <CL/cl.h>

#define MEM_SIZE (128)
#define MAX_SOURCE_SIZE (0x100000)

int main()
{
	cl_device_id device_id = NULL;
	cl_context context = NULL;
	cl_program program = NULL;
	cl_kernel kernel = NULL;
	cl_platform_id platform_id = NULL;
	cl_uint ret_num_devices;
	cl_uint ret_num_platforms;
	cl_int ret;

	char string[MEM_SIZE];

	FILE *fp;
	char fileName[] = "./hello.cl";
	char *source_str;
	size_t source_size;

	/* Load the source code containing the kernel*/
	fp = fopen(fileName, "r");
	if (!fp) {
		fprintf(stderr, "Failed to load kernel.\n");
		exit(1);
	}
	source_str = (char*)malloc(MAX_SOURCE_SIZE);
	source_size = fread(source_str, 1, MAX_SOURCE_SIZE, fp);
	fclose(fp);

	/* Get Platform and Device Info */
	ret = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
	ret = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_DEFAULT, 1, &device_id, &ret_num_devices);
	printf("%i\n",ret);

	/* Create OpenCL context */
	context = clCreateContext(NULL, 1, &device_id, NULL, NULL, &ret);
	printf("%i\n",ret);

	/* Create Kernel Program from the source */
	program = clCreateProgramWithSource(context, 1, (const char **)&source_str,(const size_t *)&source_size, &ret);
	printf("%i\n",ret);

	/* Build Kernel Program */
	ret = clBuildProgram(program, 1, &device_id, "-cl-std=CL2.0", NULL, NULL);
	printf("%i\n",ret);

	/* Create OpenCL Kernel */
	kernel = clCreateKernel(program, "hello", &ret);
	printf("%i\n",ret);

	/* Finalization */
	ret = clReleaseKernel(kernel);
	ret = clReleaseProgram(program);
	ret = clReleaseContext(context);

	free(source_str);

	return 0;
}





Code in hello.cl:

__kernel void hello (__global double * a,
     __global int * b,
     __global int * c, __global double * g,
     __global int * d,
     __global int * e, __global int * f)
{
	size_t local_id=get_local_id(0);
	size_t group_id=get_group_id(0);

	__local int MI[64*64];
	__local short aa[64];
	__local short bb[64];
	__local short cc[64];

	__private int ICG=d[group_id*64+local_id];

	bb[local_id]=b[ICG];
	cc[local_id]=bb[local_id];

	__private long SM[4];
	SM[0]=0;
	SM[1]=0;
	SM[2]=0;
	SM[3]=0;

	__private int nCol=f[ICG];

	for (int iCol=0;iCol<nCol;iCol++)
	{
		__private int is=atomic_inc(&c[26]);

		e[is*3+0]=ICG;

		__private int iRand=atomic_inc(&c[8]);
		__private double R=g[iRand];
		__private int L=cc[local_id]*R;

		__private int IL=L>>6;
		__private long TM=1<<(L-IL*64);

		SM[IL]|=TM;

		__private int M=cc[local_id]*R;
		IL=M>>6;
		TM=1<<(M-IL*64);

		__private int MS;

		if (M<bb[local_id])
		{
			__private int IMS=M;
			MS=*((int*)&a[IMS*6 +0]+1);
		}
		SM[IL]|=TM;

		if (L<bb[local_id])
		{
			__private int IMS=L;
			e[is*3+1]=IMS;
		}

		if (M<bb[local_id])
		{
			__private int IMS=M;
			e[is*3+2]=IMS;
		}
	}
}




---

## 评论 (11 条)

### 评论 #1 — gstoner (2017-12-28T18:50:05Z)

We are looking into this

---

### 评论 #2 — Srinivasuluch (2018-01-12T10:28:32Z)

Hi Moading,

Tried locally on Polaris Duo, no such issue noticed. Could you please provide DID of the hardware?
#**lspci -nn | grep ATI**
Need console output of the command


---

### 评论 #3 — Moading (2018-01-13T22:03:05Z)

The device ID is 67c4

---

### 评论 #4 — Srinivasuluch (2018-01-16T04:56:51Z)

Thanks Moading for the details, we are not able to reproduce the issue with the latest driver stack. Please try with upcoming minor(1.7.1) release.

---

### 评论 #5 — acmeman925 (2018-02-15T23:14:14Z)

Are you still observing the issue.  We are unable to reproduce internally

---

### 评论 #6 — Moading (2018-02-16T08:12:34Z)

I will check again after installing the next ROCm release. There was no update since I opened this issue,

---

### 评论 #7 — gstoner (2018-02-16T15:20:21Z)

@Moading Would you be open to do beta test  

---

### 评论 #8 — Moading (2018-02-16T20:12:49Z)

Yes, sure.

---

### 评论 #9 — gstoner (2018-02-16T22:37:02Z)

@Moading   http://repo.radeon.com/misc/archive/beta/rocm-1.7.1-beta.tar.gz you need to use local repo install instruction in the tarball 


---

### 评论 #10 — Moading (2018-02-20T21:23:15Z)

I finally installed ROCm 1.7.1 beta on another machine with identical hardware. I started with a fresh install of ubuntu 16.04.3

The segmentation fault still occurs.
dmesg shows that the segfault occurs in libamdocl64.so
Should I post a core dump?

---

### 评论 #11 — Moading (2018-02-22T21:53:24Z)

After installing 1.7.1-beta.2 the problem disappeared! Nice!

---
