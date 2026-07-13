# MI100 memory Operating points

- **Issue #:** 2844
- **State:** closed
- **Created:** 2024-01-26T23:44:59Z
- **Updated:** 2024-02-13T22:50:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/2844

sorry if this is an inappropriate place for this question. I have a couple of MI100s in a server, but they idle terribly, it would appear that they have no lower vram operating power level than full speed, see:

```

# cat /sys/class/drm/card2/device/pp_dpm_mclk 
0: 1200Mhz *
```

I was wondering if you guys have access to a newer vbios that potentially includes more power levels as idle consumption like this is fairly unreasonable. Below for reference amdvbflash output:

```
adapter seg  bn dn dID       asic           flash      romsize test    bios p/n   
======= ==== == == ==== =============== ============== ======= ==== ================
  0    0000 03 00 738C MI100(Slave)    GD25Q80C        100000 pass 113-D3431401-100
```

Thank you very much for any help you can provide and i apologize for the intrusion.