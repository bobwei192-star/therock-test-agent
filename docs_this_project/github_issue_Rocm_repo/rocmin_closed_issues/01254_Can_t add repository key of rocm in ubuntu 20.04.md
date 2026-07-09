# Can't add repository key of rocm in ubuntu 20.04

- **Issue #:** 1254
- **State:** closed
- **Created:** 2020-10-07T04:22:14Z
- **Updated:** 2020-11-05T09:01:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1254

hello rocm team 
plz help, the terminal is showning 

`wget -q -O - http://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
gpg: invalid key resource URL '/tmp/apt-key-gpghome.KMH3OusvRn/home:manuelschneid3r.asc.gpg'
gpg: keyblock resource '(null)': General error
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 1488EB46E192A257: 1 signature not checked due to a missing key
gpg: key 3B4FE6ACC0B21F32: 3 signatures not checked due to missing keys
gpg: key D94AA3F0EFE21092: 3 signatures not checked due to missing keys
gpg: key 871920D1991BC93C: 1 signature not checked due to a missing key
gpg: Total number processed: 7
gpg:       skipped new keys: 7
`