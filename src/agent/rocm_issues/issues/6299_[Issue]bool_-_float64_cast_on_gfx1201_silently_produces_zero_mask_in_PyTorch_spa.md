# [Issue]:bool -> float64 cast on gfx1201 silently produces zero mask in PyTorch sparse workflow

> **Issue #6299**
> **状态**: open
> **创建时间**: 2026-05-25T12:19:55Z
> **更新时间**: 2026-05-26T19:52:56Z
> **作者**: sosya2000-gif
> **标签**: status: triage
> **URL**: https://github.com/ROCm/ROCm/issues/6299

## 标签

- **status: triage** (颜色: #585dd7)

## 负责人

- harkgill-amd

## 描述

### Problem Description

On ROCm/gfx1201, converting a bool tensor to float64 on GPU appears to silently produce an invalid all-zero mask in a sparse LOBPCG workflow.

No runtime error is raised, but downstream scientific computations collapse:

- masked sparse operator returns zero
- rho becomes zero
- lambda_H collapses to -mu

This caused silent corruption in an iterative eigensolver workflow.

The issue disappears if the float64 mask is created on CPU first and then uploaded to GPU.

### Operating System

Ubuntu 24.04.3 LTS 

### CPU

amd 5600x, 5950x

### GPU

ai pro r9700 *4ea

### ROCm Version

ROCm 7.x

### ROCm Component

_No response_

### Steps to Reproduce

import torch

device = "cuda:0"

mask_bool = torch.tensor([True, False, True, True], device=device)

# suspected broken path
mask_f = mask_bool.to(torch.float64)

print(mask_bool)
print(mask_f)
print(mask_f.sum())

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support



항목 | Node A (Living) | Node A, B (5600x, 5950x)
-- | -- | --
OS | Ubuntu 24.04.4 LTS | Ubuntu 24.04.4 LTS
CPU | AMD Ryzen 9 5950X (16core) | AMD Ryzen 5 5600X (6core)
GPU | AMD Radeon AI PRO R9700 × 2 | AMD Radeon AI PRO R9700 × 2
GPU arch | gfx1201 (RDNA 4) | gfx1201 (RDNA 4)




# workaround (works correctly)

mask_f_cpu = torch.tensor(
    [1.0, 0.0, 1.0, 1.0],
    dtype=torch.float64
)

mask_f_gpu = mask_f_cpu.to(device)

print(mask_f_gpu.sum())

### Additional Information

#!/usr/bin/env python3
"""
kc_lobpcg_debug.py — Trace LOBPCG iteration internals to find X→0 collapse.
Runs only 6 iterations, printing norms at every intermediate step.
"""
import os, struct, time, warnings
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
import numpy as np
import scipy.sparse as sp
import torch

DEVICE = torch.device("cuda:0")
DTYPE  = torch.float64
BIN    = "/tmp/D3_N5M.bin"
LAM    = 52.0


def read_bin(path):
    with open(path, "rb") as f:
        N, nnz, n_core, _ = struct.unpack("<iiii", f.read(16))
        indptr  = np.frombuffer(f.read((N+1)*4), dtype=np.int32).copy()
        indices = np.frombuffer(f.read(nnz*4),   dtype=np.int32).copy()
        data    = np.frombuffer(f.read(nnz*8),   dtype=np.float64).copy()
        base    = 16 + (N+1)*4 + nnz*4 + nnz*8
        f.seek(base + N*8*3)
        is_core = np.frombuffer(f.read(N), dtype=np.uint8).astype(bool).copy()
        f.seek(base + N*8*3 + N)
        V_orig  = np.frombuffer(f.read(N*8), dtype=np.float64).copy()
        f.seek(base + N*8*3 + N + N*8)
        V_grav  = np.frombuffer(f.read(N*8), dtype=np.float64).copy()
    L = sp.csr_matrix((data, indices, indptr), shape=(N, N))
    return N, L, np.asarray(L.diagonal()).copy(), is_core, V_orig, V_grav


def main():
    print(f"=== LOBPCG DEBUG  device={DEVICE}  λ={LAM} ===")
    N, L, L_diag, is_core, V_orig, V_grav = read_bin(BIN)
    n_core = int(is_core.sum())
    print(f"N={N:,}  n_core={n_core:,}")

    # Upload
    crow = torch.tensor(L.indptr, dtype=torch.int32, device=DEVICE)
    col  = torch.tensor(L.indices, dtype=torch.int32, device=DEVICE)
    val  = torch.tensor(L.data.astype(np.float64), dtype=DTYPE, device=DEVICE)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        L_gpu = torch.sparse_csr_tensor(crow, col, val, size=(N, N))

    L_diag_gpu = torch.tensor(L_diag, dtype=DTYPE, device=DEVICE)

    # KEY FIX: float64 from numpy (not bool→float on GPU)
    is_core_f = torch.tensor(is_core.astype(np.float64), dtype=DTYPE, device=DEVICE)
    is_core_t = is_core_f.to(torch.bool)

    H_add     = 2.0 * (torch.tensor(V_orig, dtype=DTYPE, device=DEVICE)
                       + LAM * torch.tensor(V_grav, dtype=DTYPE, device=DEVICE))

    core_diag_min = float((L_diag_gpu + H_add)[is_core_t].min().item())
    mu = max(0.0, -core_diag_min) + 2.0
    H_shift_col = (H_add + mu).unsqueeze(1)

    def Av_core(Z):
        return (torch.sparse.mm(L_gpu, Z) + H_shift_col * Z) * is_core_f.unsqueeze(1)

    denom   = (L_diag_gpu + H_add + mu).clamp(min=1e-8)
    M_inv_f = (1.0 / denom) * is_core_f

    # Spike init
    H_sel    = L_diag_gpu + H_add + 1e10 * (1.0 - is_core_f)
    best_idx = int(torch.argmin(H_sel).item())
    X        = torch.zeros(N, 1, dtype=DTYPE, device=DEVICE)
    X[best_idx, 0] = 1.0
    print(f"spike node={best_idx}  H_diag={float((L_diag_gpu+H_add)[best_idx]):.4f}  mu={mu:.4f}")

    AX    = Av_core(X)
    norms = X.norm(dim=0).clamp(min=1e-15)
    rho   = (X * AX).sum(0) / (norms**2)
    P     = torch.zeros_like(X)
    print(f"Initial: X.norm={float(X.norm()):.6f}  AX.norm={float(AX.norm()):.6f}  rho={float(rho[0]):.6f}")
    print()

    for it in range(6):
        print(f"--- it={it} ---")
        print(f"  X.norm={float(X.norm()):.6f}  X.is_contiguous={X.is_contiguous()}")

        R  = AX - rho.unsqueeze(0) * X
        Rp = M_inv_f.unsqueeze(1) * R
        print(f"  R.norm={float(R.norm()):.6e}  Rp.norm={float(Rp.norm()):.6e}")

        # Build S with is_core projection
        S_cols = [X]
        Rp_ic  = Rp * is_core_f.unsqueeze(1)
        rp_nrm = float(Rp_ic.norm().item())
        if rp_nrm > 1e-8:
            S_cols.append(Rp_ic / rp_nrm)
        if it > 0:
            P_ic  = P * is_core_f.unsqueeze(1)
            p_nrm = float(P_ic.norm().item())
            if p_nrm > 1e-8:
                S_cols.append(P_ic / p_nrm)
        S = torch.cat(S_cols, dim=1)
        m = S.shape[1]
        print(f"  S.shape={S.shape}  S contiguous={S.is_contiguous()}")

        # Check S column norms
        for j in range(m):
            s_ic_nrm = float((S[:, j] * is_core_f).norm().item())
            s_nc_nrm = float((S[:, j] * (1.0 - is_core_f)).norm().item())
            print(f"    S[:,{j}].norm={float(S[:,j].norm()):.6f}  is_core_part={s_ic_nrm:.6f}  non_core_part={s_nc_nrm:.2e}")

        Q, R_qr = torch.linalg.qr(S)
        print(f"  Q BEFORE zero: shape={Q.shape}  contiguous={Q.is_contiguous()}")
        for j in range(Q.shape[1]):
            qj = Q[:, j]
            q_ic = float((qj * is_core_f).norm().item())
            q_nc = float((qj * (1.0 - is_core_f)).norm().item())
            print(f"    Q[:,{j}].norm={float(qj.norm()):.6f}  is_core_part={q_ic:.6f}  non_core_part={q_nc:.2e}")

        Q_before = Q.clone()
        Q = Q * is_core_f.unsqueeze(1)
        print(f"  Q AFTER zero: contiguous={Q.is_contiguous()}")
        for j in range(Q.shape[1]):
            qj = Q[:, j]
            print(f"    Q[:,{j}].norm={float(qj.norm()):.8f}")

        # Check if Q changed significantly
        diff = (Q - Q_before).norm()
        print(f"  ||Q_after - Q_before||={float(diff):.2e}")

        Q = Q.contiguous()  # ensure contiguous for downstream ops

        AS = Av_core(Q)
        print(f"  AS.shape={AS.shape}")
        for j in range(AS.shape[1]):
            print(f"    AS[:,{j}].norm={float(AS[:,j].norm()):.6f}")

        G = Q.T @ AS
        G = (G + G.T) * 0.5
        print(f"  G={G.cpu().numpy().round(6)}")

        try:
            evals, evecs = torch.linalg.eigh(G)
            print(f"  evals={evals.cpu().numpy().round(6)}")
            print(f"  evecs[:,0]={evecs[:,0].cpu().numpy().round(6)}")
        except Exception as e:
            print(f"  eigh FAILED: {e}")
            break

        evals, evecs = evals[:1], evecs[:, :1]
        X_new  = Q @ evecs
        AX_new = AS @ evecs
        print(f"  X_new BEFORE proj: norm={float(X_new.norm()):.8f}  contiguous={X_new.is_contiguous()}")

        X_new  = X_new  * is_core_f.unsqueeze(1)
        AX_new = AX_new * is_core_f.unsqueeze(1)
        print(f"  X_new AFTER proj:  norm={float(X_new.norm()):.8f}")

        nrm = X_new.norm(dim=0).clamp(min=1e-15)
        print(f"  nrm={float(nrm[0]):.2e}")
        X_new  = X_new  / nrm.unsqueeze(0)
        AX_new = AX_new / nrm.unsqueeze(0)
        print(f"  X_new AFTER norm:  norm={float(X_new.norm()):.8f}")

        # Verify X_new is in is_core
        xn_ic  = float((X_new[:,0] * is_core_f).norm().item())
        xn_nc  = float((X_new[:,0] * (1.0-is_core_f)).norm().item())
        print(f"  X_new is_core_part={xn_ic:.8f}  non_core_part={xn_nc:.2e}")

        P      = X_new - X
        X, AX  = X_new, AX_new
        norms  = X.norm(dim=0).clamp(min=1e-15)
        rho    = (X * AX).sum(0) / (norms**2)
        lambda_H = float(rho[0].item()) - mu
        print(f"  → rho={float(rho[0]):.6f}  lambda_H={lambda_H:.6f}")
        print()

    print("=== DEBUG DONE ===")


if __name__ == "__main__":
    main()


---

## 评论 (1 条)

### 评论 #1 — harkgill-amd (2026-05-26T19:52:56Z)

Hey @sosya2000-gif, I gave this a try on my end with both the [release torch 7.2 wheels](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html) and [TheRock nightly 7.13 wheels](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#torch-for-gfx120x-all) but wasn't able to reproduce the all-zero mask you mentioned. Both CPU cast and GPU cast produce the same results initially and with downstream computations. Could you share your torch version, exact ROCm version and a simple reproducer - does the following still fail for you?
```
mask_bool = torch.tensor([True, False, True, True], device=device)
mask_f = mask_bool.to(torch.float64)
print(mask_bool)
print(mask_f)
print(mask_f.sum())

---
