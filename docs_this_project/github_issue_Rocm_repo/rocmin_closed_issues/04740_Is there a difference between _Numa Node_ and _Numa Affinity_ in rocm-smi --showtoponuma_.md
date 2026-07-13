# Is there a difference between "Numa Node" and "Numa Affinity" in rocm-smi --showtoponuma?

- **Issue #:** 4740
- **State:** closed
- **Created:** 2025-05-14T14:00:21Z
- **Updated:** 2025-05-15T14:10:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/4740

On all our systems, `rocm-smi --showtoponuma` reports the same "Numa Node" and "Numa Affinity" values for each individual GPU. For example:

```
$ rocm-smi --showtoponuma

============================ ROCm System Management Interface ============================
======================================= Numa Nodes =======================================
GPU[0]		: (Topology) Numa Node: 0
GPU[0]		: (Topology) Numa Affinity: 0
GPU[1]		: (Topology) Numa Node: 0
GPU[1]		: (Topology) Numa Affinity: 0
GPU[2]		: (Topology) Numa Node: 0
GPU[2]		: (Topology) Numa Affinity: 0
GPU[3]		: (Topology) Numa Node: 0
GPU[3]		: (Topology) Numa Affinity: 0
GPU[4]		: (Topology) Numa Node: 1
GPU[4]		: (Topology) Numa Affinity: 1
GPU[5]		: (Topology) Numa Node: 1
GPU[5]		: (Topology) Numa Affinity: 1
GPU[6]		: (Topology) Numa Node: 1
GPU[6]		: (Topology) Numa Affinity: 1
GPU[7]		: (Topology) Numa Node: 1
GPU[7]		: (Topology) Numa Affinity: 1
================================== End of ROCm SMI Log ===================================
```

Is there a difference between these two values, or can we assume they will always be equal? Are there systems or GPUs where "Numa Node" and "Numa Affinity" differ?