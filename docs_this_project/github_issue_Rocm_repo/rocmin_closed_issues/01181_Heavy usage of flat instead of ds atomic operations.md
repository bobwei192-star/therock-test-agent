# Heavy usage of flat instead of ds atomic operations 

- **Issue #:** 1181
- **State:** closed
- **Created:** 2020-07-23T07:49:07Z
- **Updated:** 2021-04-08T11:43:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1181

Hello

I observed that the lightning compiler - at least those that is included with rga prefers to use flat atomic operations in local memory instead of ds_atomics This applies as well to my Radeon VII as to RX 580 target.

I wondered why this happens and if it would not be more beneficiary to default to ds operations when available, because the flat operations

- need 8 byte instead of 4 byte (ds ops) addressing in shared memory (when in 64 bit addressing mode)
- require a "s_waitcnt    vmcnt(0) & lgkmcnt(0)" wait instead of "lgkmcnt" (ds ops) only, which causes a performance regression when the shared atomics are interleaved with global read or write operations
- On Ellesmere target only: the additional address offset causes an extra "s_load_dword" operation followed by a "lgkmcnt" wait when ever occurring - I do not know why this sreg is not loaded in the beginning of the kernel and then kept for every use - it seems this happens on Vega target correctly and saves a lot of s_load operations in a tight loop I have in my code.

- (Not a down, but strange: for pure read and write operation the ds_ operations are used... so we have indeed to different ways of addressing same space mixed in the kernel)

So I would appreciate usage of ds_ instead of flat_ operations and I do not see why this is not default. In case there is good reason to have flat_ as default maybe there is a switch that can toggle the behavior? If yes any comment about it would be heavily appreciated. 

