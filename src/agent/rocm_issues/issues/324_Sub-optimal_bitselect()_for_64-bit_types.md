# Sub-optimal bitselect() for 64-bit types

> **Issue #324**
> **状态**: closed
> **创建时间**: 2018-02-03T12:22:39Z
> **更新时间**: 2018-02-13T19:21:19Z
> **关闭时间**: 2018-02-13T19:21:19Z
> **作者**: todxx
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/324

## 描述

Compilation of the bitselect() function with 64-bit base types results in a sub-optimal xor-and-xor sequence instead of using v_bfi_b32 as all other types seem to.  This seems to happen with long, ulong, double types and their derived vector types.  Example kernel and output below.
Example kernel:
```
typedef long my_type;
__kernel
void bitsel(__global my_type (*data)[4])
{
    my_type a = data[get_global_id(0)][0];
    my_type b = data[get_global_id(0)][1];
    my_type mask = data[get_global_id(0)][2];

    my_type result = bitselect(a, b, mask);
    data[get_global_id(0)][3] = result;
}
```
Emitted assembly:
```
    s_load_dword s4, s[4:5], 0x4                               // 000000001100: C0020102 00000004
    s_load_dwordx2 s[0:1], s[6:7], 0x0                         // 000000001108: C0060003 00000000
    s_load_dwordx2 s[2:3], s[6:7], 0x8                         // 000000001110: C0060083 00000008
    s_waitcnt lgkmcnt(0)                                       // 000000001118: BF8CC07F
    s_and_b32 s4, s4, 0xffff                                   // 00000000111C: 8604FF04 0000FFFF
    s_mul_i32 s8, s8, s4                                       // 000000001124: 92080408
    v_add_co_u32_e32 v0, vcc, s8, v0                           // 000000001128: 32000008
    v_mov_b32_e32 v1, s3                                       // 00000000112C: 7E020203
    v_add_co_u32_e32 v0, vcc, s2, v0                           // 000000001130: 32000002
    v_addc_co_u32_e32 v1, vcc, 0, v1, vcc                      // 000000001134: 38020280
    v_lshlrev_b64 v[0:1], 5, v[0:1]                            // 000000001138: D28F0000 00020085
    v_mov_b32_e32 v2, s1                                       // 000000001140: 7E040201
    v_add_co_u32_e32 v4, vcc, s0, v0                           // 000000001144: 32080000
    v_addc_co_u32_e32 v5, vcc, v2, v1, vcc                     // 000000001148: 380A0302
    global_load_dwordx4 v[0:3], v[4:5], off                    // 00000000114C: DC5C8000 007F0004
    global_load_dwordx2 v[6:7], v[4:5], off offset:16          // 000000001154: DC548010 067F0004
    s_waitcnt vmcnt(1)                                         // 00000000115C: BF8C0F71
    v_xor_b32_e32 v2, v2, v0                                   // 000000001160: 2A040102
    v_xor_b32_e32 v3, v3, v1                                   // 000000001164: 2A060303
    s_waitcnt vmcnt(0)                                         // 000000001168: BF8C0F70
    v_and_b32_e32 v2, v2, v6                                   // 00000000116C: 26040D02
    v_and_b32_e32 v3, v3, v7                                   // 000000001170: 26060F03
    v_xor_b32_e32 v0, v2, v0                                   // 000000001174: 2A000102
    v_xor_b32_e32 v1, v3, v1                                   // 000000001178: 2A020303
    global_store_dwordx2 v[4:5], v[0:1], off offset:24         // 00000000117C: DC748018 007F0004
    s_endpgm  
```
For reference, changing my_type to uint2 emits the preferred assembly:
 ```
   s_load_dword s4, s[4:5], 0x4                               // 000000001100: C0020102 00000004
    s_load_dwordx2 s[0:1], s[6:7], 0x0                         // 000000001108: C0060003 00000000
    s_load_dwordx2 s[2:3], s[6:7], 0x8                         // 000000001110: C0060083 00000008
    s_waitcnt lgkmcnt(0)                                       // 000000001118: BF8CC07F
    s_and_b32 s4, s4, 0xffff                                   // 00000000111C: 8604FF04 0000FFFF
    s_mul_i32 s8, s8, s4                                       // 000000001124: 92080408
    v_add_co_u32_e32 v0, vcc, s8, v0                           // 000000001128: 32000008
    v_mov_b32_e32 v1, s3                                       // 00000000112C: 7E020203
    v_add_co_u32_e32 v0, vcc, s2, v0                           // 000000001130: 32000002
    v_addc_co_u32_e32 v1, vcc, 0, v1, vcc                      // 000000001134: 38020280
    v_lshlrev_b64 v[0:1], 5, v[0:1]                            // 000000001138: D28F0000 00020085
    v_mov_b32_e32 v2, s1                                       // 000000001140: 7E040201
    v_add_co_u32_e32 v0, vcc, s0, v0                           // 000000001144: 32000000
    v_addc_co_u32_e32 v1, vcc, v2, v1, vcc                     // 000000001148: 38020302
    global_load_dwordx2 v[2:3], v[0:1], off                    // 00000000114C: DC548000 027F0000
    global_load_dwordx2 v[4:5], v[0:1], off offset:8           // 000000001154: DC548008 047F0000
    global_load_dwordx2 v[6:7], v[0:1], off offset:16          // 00000000115C: DC548010 067F0000
    s_waitcnt vmcnt(0)                                         // 000000001164: BF8C0F70
    v_bfi_b32 v3, v7, v5, v3                                   // 000000001168: D1CA0003 040E0B07
    v_bfi_b32 v2, v6, v4, v2                                   // 000000001170: D1CA0002 040A0906
    global_store_dwordx2 v[0:1], v[2:3], off offset:24         // 000000001178: DC748018 007F0200
    s_endpgm 
```
I am running on rocm 1.7 and targeting Vega.


---

## 评论 (2 条)

### 评论 #1 — arsenm (2018-02-07T00:26:42Z)

Fixed by https://github.com/llvm-mirror/llvm/commit/9051a39c8ae2f6475239e1fe283a8d6feb36fa7c

---

### 评论 #2 — todxx (2018-02-07T03:28:49Z)

Awesome! Thanks @arsenm !

---
