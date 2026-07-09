# Memory access fault by GPU node-4 (Agent handle: 0x152e220) on address (nil). Reason: Page not present or supervisor privilege.

- **Issue #:** 1339
- **State:** closed
- **Created:** 2020-12-16T11:13:44Z
- **Updated:** 2021-05-23T01:00:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1339

Environment:
rocm-3.9
centos 7.6.8
Issue:
My program submit an error which just like "Memory access fault by GPU node-4 (Agent handle: 0x152e220) on address (nil). Reason: Page not present or supervisor privilege.". 
However,the error has gone,when i add "printf" in device function .  Why does this happened? 
No error code as follows 
```C++
__device__ int cuda_dfs_match(const int len, const unsigned char *str, const int sequence_type, unsigned int *widths, unsigned char *bids, const barracuda_gap_opt_t *opt, alignment_store_t *aln, int best_score, const int max_aln,uint4 * bwt_occ_array,uint4 * rbwt_occ_array)
{
....

printf(" debug_1666 ");

....
}
```
I guess that "printf" makes the threads synchronize. 
Thanks