# __float2half_rz has _rn behavior and is not properly truncating

- **Issue #:** 1846
- **State:** closed
- **Created:** 2022-10-28T00:35:48Z
- **Updated:** 2024-02-23T22:20:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/1846

I believe this was ROCM 5.2.0

See example code (Hippify then run):

```
#include <iostream>
#include <algorithm>
#include <array>
#include "cuda_fp16.h"

__global__ void test_rounding(){

    // Target number: 1.69140625 * 2^-13
    float one_below = __uint_as_float(0x39587FFF);//  = 1.69140613079071044921875 * 2^-13, in theory this should round (toward zero) to half value of 1.6904296875 * 2^-13 == 0xac3
    float exact = __uint_as_float(0x39588000); // = 1.69140625 * 2^-13, in theory this should round exactly to half value of 1.6914062500 * 2^-13 = 0xac4
    float one_above = __uint_as_float(0x39588001); // = 1.69140636920928955078125 * 2^-13, in theory this should round (toward zero) to half value of 1.6914062500 * 2^-13 == 0xac4

    float amd_round_down = __uint_as_float(0x39586FFF); // = 1.69091784954071044921875 * 2^-13 | For amd this round_nzs to 0xac3
    float amd_round_up = __uint_as_float(0x39587000); // = 1.69091796875 * 2^-13 | For amd this round_nzs to 0xac4

    half one_below_h = __float2half_rz(one_below);
    half exact_h = __float2half_rz(exact);
    half one_above_h = __float2half_rz(one_above);
    half amd_round_down_h = __float2half_rz(amd_round_down);
    half amd_round_up_h = __float2half_rz(amd_round_up);

    printf("one_below: %04x, exact: %04x, one_above: %04x, amd_round_down: %04x, amd_round_up: %04x\n", __float_as_uint(one_below), __float_as_uint(exact), __float_as_uint(one_above), __float_as_uint(amd_round_down), __float_as_uint(amd_round_up));
    printf("one_below_h: %02x, exact_h: %02x, one_above_h: %02x, amd_round_down_h: %02x, amd_round_up_h: %02x\n", __half_as_ushort(one_below_h), __half_as_ushort(exact_h), __half_as_ushort(one_above_h), __half_as_ushort(amd_round_down_h), __half_as_ushort(amd_round_up_h));
}

int main() {
	test_rounding<<<1,1>>>();
	cudaDeviceSynchronize();
	return 0;
}
```

I would strongly suggest doing a quick sanity checks for all rounding mode functions to make sure they aren't improperly aliased as another command by accident.