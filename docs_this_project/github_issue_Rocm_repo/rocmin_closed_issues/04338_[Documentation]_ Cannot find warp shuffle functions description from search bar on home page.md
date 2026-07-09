# [Documentation]: Cannot find warp shuffle functions description from search bar on home page

- **Issue #:** 4338
- **State:** closed
- **Created:** 2025-02-04T21:12:32Z
- **Updated:** 2025-03-20T21:58:42Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4338

### Description of errors

A search for "shuffle" in the [home page of ROCm docs](https://rocm.docs.amd.com/en/latest/) yields one result, and not the actual page that I was looking for.

<img width="1265" alt="Image" src="https://github.com/user-attachments/assets/00bfd5ff-0cca-4b8c-a8a6-b7c3cf7a0805" />

The page I wanted to get to was the following:

[https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html#warp-shuffle-functions](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html#warp-shuffle-functions)

Please fix the search functionality so that it is easier to find what we want from the main page. Users would not know which sub-section of the docs to go and search in.

### Attach any links, screenshots, or additional evidence you think will be helpful.

Other similar examples: can't find `rocprofv3` documentation for instance. I was looking for the page on "[Using rocprofv3](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html#using-rocprofv3)", but see this instead:

<img width="1283" alt="Image" src="https://github.com/user-attachments/assets/c87c721b-7513-453a-ae1c-de045a642d79" />

or any HIP API call such as `hipMalloc` that should have returned [the API page](https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management.html#_CPPv4I0E9hipMalloc10hipError_tPP1T6size_t), but search results show this instead: 

<img width="1187" alt="Image" src="https://github.com/user-attachments/assets/9284e391-34cc-46d4-87b3-8fe70bea93f2" />