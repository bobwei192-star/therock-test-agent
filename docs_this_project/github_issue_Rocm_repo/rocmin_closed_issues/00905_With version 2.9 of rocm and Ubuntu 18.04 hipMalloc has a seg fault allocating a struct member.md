# With version 2.9 of rocm and Ubuntu 18.04 hipMalloc has a seg fault allocating a struct member.

- **Issue #:** 905
- **State:** closed
- **Created:** 2019-10-09T19:13:27Z
- **Updated:** 2023-12-13T10:23:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/905

The line where hipMalloc is being used to allocate a struct member has a segmentation fault under rocm 2.9, but previously worked under the last several versions of ROCm.

#define PIXELS_PER_LINE 1024
#define LINE_BYTES_UINT32 PIXELS_PER_LINE   * sizeof(uint32_t)

struct BaselineData
{
    uint32_t* minLine;
};

void initBaselineData_d(struct BaselineData *& data)
{
  std::cout << "HIP_CHECK(hipMalloc(&data,sizeof(struct BaselineData)));"         << std::endl;
  HIP_CHECK(hipMalloc(&data,sizeof(struct BaselineData)));
  std::cout << "HIP_CHECK(hipMalloc(&(data->minLine), LINE_BYTES_UINT32));"       << std::endl;
HIP_CHECK(hipMalloc(&(data->minLine), LINE_BYTES_UINT32));
}