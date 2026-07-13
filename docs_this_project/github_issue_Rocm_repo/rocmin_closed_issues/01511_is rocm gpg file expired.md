# is rocm gpg file expired

- **Issue #:** 1511
- **State:** closed
- **Created:** 2021-07-04T13:20:25Z
- **Updated:** 2021-07-06T03:41:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/1511

 ~ wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
gpg: invalid key resource URL '/tmp/apt-key-gpghome.cxQTQYrmSe/home:manuelschneid3r.asc.gpg'
gpg: keyblock resource '(null)': General error
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key D94AA3F0EFE21092: 3 signatures not checked due to missing keys
gpg: key 871920D1991BC93C: 1 signature not checked due to a missing key
gpg: Total number processed: 7
gpg:       skipped new keys: 7

pop os 21.04
