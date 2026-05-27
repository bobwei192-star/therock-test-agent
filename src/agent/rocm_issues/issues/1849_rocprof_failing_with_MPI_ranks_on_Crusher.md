# rocprof failing with MPI ranks on Crusher

> **Issue #1849**
> **状态**: closed
> **创建时间**: 2022-11-01T17:32:51Z
> **更新时间**: 2024-03-11T02:05:00Z
> **关闭时间**: 2024-03-11T02:05:00Z
> **作者**: nicolemarsaglia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1849

## 描述

I'm trying to us rocprof on Crusher but it fails for the non root ranks when I increase the number of MPI ranks > 1. 

Here is the environment I built my application: 

```
module load PrgEnv-cray
module load craype-accel-amd-gfx90a
module load cmake/3.22.2
module load rocm/5.2.0
module load cray-mpich
module load cray-hdf5-parallel/1.12.1.1

# GPU-aware MPI
export MPICH_GPU_SUPPORT_ENABLED=1

export AMREX_AMD_ARCH=gfx90a

export CC=$(which cc)
export CXX="$(which CC) -x hip"
export FC=$(which ftn)
export CFLAGS="-I${ROCM_PATH}/include"
export CXXFLAGS="-I${ROCM_PATH}/include -ggdb -O3 -std=c++17 -Wall -Wno-pass-failed"
export LD=${CC}
export LDFLAGS="${CXXFLAGS} -L${ROCM_PATH}/lib -lamdhip64"
export LIBS="-lamdhip64"
```

Here is my job, with one rank, that works: 

`srun -n 1 -G 1 rocprof -o ${SLURM_JOBID}_${SLURM_PROCID}.csv --hip-trace ./kripke_par --procs 1,1,1  --zones 60,60,60 --niter 3 --dir 1:2 --grp 1:1 --legendre 4 --quad 4:4`

Next, I change my job to use 6 ranks and 6 GPUs:

`srun -n 6 -G 6 rocprof -o ${SLURM_JOBID}_${SLURM_PROCID}.csv --hip-trace ./kripke_par --procs 2,3,1  --zones 60,60,60 --niter 3 --dir 1:2 --grp 1:1 --legendre 4 --quad 4:4`

I still get output from rank 0, but I also get the following errors:
```
Traceback (most recent call last):
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 836, in <module>
    hip_trace_found = fill_api_db('HIP', db, indir, 'hip', HIP_PID, OPS_PID, [], {}, 1)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 407, in fill_api_db
    table_handle = db.add_table(table_name, api_table_descr)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/sqlitedb.py", line 48, in add_table
    cursor.execute(stm)
sqlite3.OperationalError: table HIP already exists
Traceback (most recent call last):
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 836, in <module>
    hip_trace_found = fill_api_db('HIP', db, indir, 'hip', HIP_PID, OPS_PID, [], {}, 1)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 407, in fill_api_db
    table_handle = db.add_table(table_name, api_table_descr)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/sqlitedb.py", line 48, in add_table
    cursor.execute(stm)
sqlite3.OperationalError: table HIP already exists
Traceback (most recent call last):
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 836, in <module>
    hip_trace_found = fill_api_db('HIP', db, indir, 'hip', HIP_PID, OPS_PID, [], {}, 1)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 407, in fill_api_db
    table_handle = db.add_table(table_name, api_table_descr)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/sqlitedb.py", line 48, in add_table
    cursor.execute(stm)
sqlite3.OperationalError: table HIP already exists
Traceback (most recent call last):
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 836, in <module>
    hip_trace_found = fill_api_db('HIP', db, indir, 'hip', HIP_PID, OPS_PID, [], {}, 1)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 407, in fill_api_db
    table_handle = db.add_table(table_name, api_table_descr)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/sqlitedb.py", line 48, in add_table
    cursor.execute(stm)
sqlite3.OperationalError: table HIP already exists
Traceback (most recent call last):
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 836, in <module>
    hip_trace_found = fill_api_db('HIP', db, indir, 'hip', HIP_PID, OPS_PID, [], {}, 1)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/tblextr.py", line 407, in fill_api_db
    table_handle = db.add_table(table_name, api_table_descr)
  File "/opt/rocm-5.2.0/libexec/rocprofiler/sqlitedb.py", line 48, in add_table
    cursor.execute(stm)
sqlite3.OperationalError: table HIP already exists
srun: error: crusher047: tasks 0-3,5: Exited with exit code 1
srun: launch/slurm: _step_signal: Terminating StepId=208573.0
```

Any help is appreciated! 

---

## 评论 (2 条)

### 评论 #1 — nartmada (2024-02-22T02:48:07Z)

@nicolemarsaglia, apologies for the lack of response.  Can you please try latest ROCm 6.0.2 and see if your issue still exists?  Thanks.

---

### 评论 #2 — nartmada (2024-03-11T02:05:00Z)

Closing the ticket as there is no response from @nicolemarsaglia.  Please re-open if you still observe this issue with latest ROCm 6.0.2.  Thanks.

---
