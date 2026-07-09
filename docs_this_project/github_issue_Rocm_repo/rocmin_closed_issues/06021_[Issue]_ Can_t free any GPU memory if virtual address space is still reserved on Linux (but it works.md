# [Issue]: Can't free any GPU memory if virtual address space is still reserved on Linux (but it works on Windows?)

- **Issue #:** 6021
- **State:** closed
- **Created:** 2026-03-06T16:02:06Z
- **Updated:** 2026-04-01T11:18:05Z
- **Labels:** status: assessed, status: fix submitted
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6021

### Problem Description

When trying to implement ROCm support in comfy-aimdo, I'm running into a problem with freeing memory.

aimdo first reserves virtual address space in a large chunk with hipMemAddressReserve, and then later maps actual memory reservations into the address space. Later, it will free individual chunks from the reserved address space (when it needs to offload GPU memory), and this apparently works on CUDA and reportedly on ROCm Windows, but on Linux, it seems that no GPU memory is freed until the *entire* address space is also freed with hipMemAddressFree, which makes comfy-aimdo unable to offload any memory.

My expectation is that memory would be freed at  `hipMemRelease`, which would allow keeping the address space reserved while freeing physical memory. but that does not happen.

### Operating System

RHEL 9, RHEL 10 (re-tested after OS upgrade, problem still occurs)

### CPU

Intel Haswell

### GPU

XTX 7900

### ROCm Version

Tested with 7.2 and 7.11-preview

### ROCm Component

HIP

### Steps to Reproduce

Small reproducer. Run without a parameter to use hipMemAddressRelease (which correctly frees memory but forces releasing the address space as well) and with a parameter to run without hipMemAddressRelease to observe that memory remains in use.

The allocs here allocate the address space in smaller chunks, but you could also allocate the whole address space in one go in the main function and let the allocs map physical memory into it in chunks, which matches what comfy-aimdo wants to do.
```
#include <hip/hip_runtime.h>
#include <stdio.h>
#include <stdbool.h>

static size_t alloc_count = 0;
static bool free_address = true;

typedef struct {
        void* ptr;
        hipMemGenericAllocationHandle_t h;
} alloc_t;

#define LOG(x, ...) printf(x "\n" __VA_OPT__(,) __VA_ARGS__)

static inline bool check_impl(hipError_t result, const char *label) {
        if (result != hipSuccess) {
                LOG("HIP ERROR (%s): %s", label, hipGetErrorString(result));
        }
        return (result == hipSuccess);
}

#define CHECK(x) check_impl((x), #x)
#define CHECK_RET(x) do { if (!CHECK(x)) return false; } while(0)
void print_mem() {
        size_t mem_free, mem_total;
        hipMemGetInfo(&mem_free, &mem_total);
        LOG("Memory free: %zuMiB in_use: %zuMiB", mem_free / (1024*1024), (mem_total-mem_free)/(1024*1024));
}

#define ALIGNMENT (1024*1024)
#define ALLOC_COUNT 1024
#define CHUNK (2ULL*1024*1024)
bool alloc(alloc_t* dest) {
        size_t s = CHUNK;
        hipMemAllocationProp p = {
                .type = hipMemAllocationTypePinned,
                .location.type = hipMemLocationTypeDevice,
                .location.id = 0,
        };
        CHECK_RET(hipMemAddressReserve(&dest->ptr, s, ALIGNMENT, 0, 0));
        CHECK_RET(hipMemCreate(&dest->h, s, &p, 0));
        CHECK_RET(hipMemMap(dest->ptr, s, 0, dest->h, 0));
        alloc_count++;
        return true;
}
bool dealloc(alloc_t* dest) {
        CHECK_RET(hipMemUnmap(dest->ptr, CHUNK));
        CHECK_RET(hipMemRelease(dest->h));
        if (free_address) CHECK_RET(hipMemAddressFree(dest->ptr, CHUNK));
        alloc_count--;
        return true;
}


void exercise() {
        size_t allocs = 0;
        alloc_t *allocations[ALLOC_COUNT] = {0};
        print_mem();
        for (size_t i = 0; i < ALLOC_COUNT; i++) {
                alloc_t *a = malloc(sizeof(*a));
                alloc(a);
                allocations[i] = a;
        }
        LOG("Alloc count: %zu", alloc_count);
        LOG("Finished allocating %d chunks", ALLOC_COUNT);
        print_mem();
        for (size_t i = 0; i < ALLOC_COUNT; i++) {
                if (i % 2) {
                        dealloc(allocations[i]);
                        free(allocations[i]);
                }
        }
        LOG("Freed half, alloc count: %zu", alloc_count);
        print_mem();

        for (size_t i = 0; i < ALLOC_COUNT; i++) {
                if (!(i % 2)) {
                        dealloc(allocations[i]);
                        free(allocations[i]);
                }
        }
        LOG("Finished freeing %d chunks", ALLOC_COUNT);
        LOG("Alloc count: %zu", alloc_count);
        print_mem();
}

int main(int argc, char** argv) {
        if (argc > 1) {
                LOG("Running without hipMemAddressFree");
                free_address = false;
        } else {
                LOG("Running with hipMemAddressFree");
        }
        for (int i = 0; i < 2; i++) exercise();
}
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Runs of the test code from my machine:
```
$ hipcc $(hipconfig -C) test.c && ./a.out test
Running without hipMemAddressFree
Memory free: 24524MiB in_use: 36MiB
Alloc count: 1024
Finished allocating 1024 chunks
Memory free: 22330MiB in_use: 2230MiB
Freed half, alloc count: 512
Memory free: 22330MiB in_use: 2230MiB
Finished freeing 1024 chunks
Alloc count: 0
Memory free: 22330MiB in_use: 2230MiB
Memory free: 22330MiB in_use: 2230MiB
Alloc count: 1024
Finished allocating 1024 chunks
Memory free: 20282MiB in_use: 4278MiB
Freed half, alloc count: 512
Memory free: 20282MiB in_use: 4278MiB
Finished freeing 1024 chunks
Alloc count: 0
Memory free: 20282MiB in_use: 4278MiB```

```$ hipcc $(hipconfig -C) test.c && ./a.out
Running with hipMemAddressFree
Memory free: 24524MiB in_use: 36MiB
Alloc count: 1024
Finished allocating 1024 chunks
Memory free: 22330MiB in_use: 2230MiB
Freed half, alloc count: 512
Memory free: 23354MiB in_use: 1206MiB
Finished freeing 1024 chunks
Alloc count: 0
Memory free: 24378MiB in_use: 182MiB
Memory free: 24378MiB in_use: 182MiB
Alloc count: 1024
Finished allocating 1024 chunks
Memory free: 22330MiB in_use: 2230MiB
Freed half, alloc count: 512
Memory free: 23354MiB in_use: 1206MiB
Finished freeing 1024 chunks
Alloc count: 0
Memory free: 24378MiB in_use: 182MiB```
