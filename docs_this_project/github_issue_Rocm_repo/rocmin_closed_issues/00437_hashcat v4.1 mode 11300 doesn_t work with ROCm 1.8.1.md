# hashcat v4.1 mode 11300 doesn't work with ROCm 1.8.1

- **Issue #:** 437
- **State:** closed
- **Created:** 2018-06-18T19:34:07Z
- **Updated:** 2018-09-19T02:48:57Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/437

So I thought this issue was with hashcat but the admins on that project are stating the issue is with ROCm. Im going to post the issue I opened with hashcat and their response. I cant write code so please be gentle. How can I fix the JiT compiler issue?
--------------------------------------------------------------------------------------------------------------------------------

Ive been doing some testing and hashcat v3.5 and 4.1 do not work correctly when using mode 11300 (bicoin wallet) with ROCm 1.8.1.

Im using xubuntu 16.04.4, 4.13.0-45-generic.

I created a test wallet.dat with a known password and used btcrecover scripts to extract the hash. With ROCm 1.8.1 installed, hashcat does not find the password with the password in a wordlist. I thought it could be the drivers so I did a clean install and tried the AMDGPU-PRO Beta Mining Driver 17.40 with optional rocm. With the AMDGPU driver installed v.3.5 does find the password in the wordlist, but v4.1 still does not.


---------------------------------------------------------------------------------------------------------------------------------

The good thing is, hashcat informs you about the invalid kernel processing on startup:* Device #2: ATTENTION! OpenCL kernel self-test failed. However, it's not a hashcat problem. I've traced the intermediate keys up to the comparison kernel (where AES comes into play). Both the AES key and the IV is correctly computed on rocm.

The next step would be to initialize the AES key scheduler array and on here (using the same shared library code) rocm start computing invalid values. All other tested OpenCL runtimes (NVidia, Intel, pocl, etc) compute it correctly.

The key scheduler access a shared memory region of the GPU to make it faster. You can however disable this behavior and make it access constant memory region. If we do this you can see how rocm starts to crack without changing any of the code portion. You can reproduce locally by commenting out line 24 in inc_vendor.cl and remove the kernel/ cache folder entirely.

Note that the same shared AES function are used in many other kernels (truecrypt 6221 for example) and they work fine over there. This is not a problem in how shared memory is accessed.I was able to further track down the issue to this data copy from constant memory to shared memory in m11300_comp() function in m11300.cl:

    s_td0[i] = td0[i];

 So basically there's nothing we can do to make this more easy. If this doesn't work it's for sure a JiT compiler problem.
--


