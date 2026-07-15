
wsl2 里无法识别gpu
Based on the screenshot you provided, this appears to be a terminal interface for an autonomous AI agent (named TheRock) that is debugging a test failure.

Here is a breakdown of what is happening in the image:

Initial Error (Round 1): The agent ran a test for a component called hiprand-quick. The test failed with the error: ctest not found. Make sure CTest/CMake is installed. The agent recognized that it needed to retrieve the full logs before attempting to debug automatically.

Log Analysis:

The agent ran cat on the stdout.log to confirm the test environment (it detected AMDGpu, hipRAND, etc.).

It ran cat on the stderr.log, which confirmed the specific "ctest not found" error message.

Automated Debugging and Analysis:

The agent invoked a tool called therock-debugger to perform an analysis.

It successfully completed the debugging task (completed in 1m 18s) and produced 3 output files.

The agent then used a Python command to validate a JSON file (round1.json), successfully confirming that round1.json: valid JSON.

Current Action (Subagent Status):

Time: 4m 12s into the process.

Status: It verified that the 3 files exist and that the JSON is valid.

Next Step: It is currently Delegating... and invoking another tool, therock-repairer, to execute safe_auto repairs.

A subagent named TheRock-Loop (with a "Big Pickle" subtitle) is currently active in a subordinate process, running step 1 of 1.

Summary: The AI agent has identified a configuration issue (ctest not found), successfully collected logs, performed a preliminary analysis, verified the data structure, and is currently passing the repair task off to a specialized repair subagent.

e": "Cannot load librocdxg.so, failed:librocdxg.so: cannot open shared object file: No such file or directory"
      },
      {
        "category": "path_hardcode",
        "line": "/therock/src/rocm-libraries/projects/hiprand/test/test_hiprand_api.cpp:85: Failure"
      },
      {
        "category": "missing_runtime_library",
        "line": "2: Cannot load librocdxg.so, failed:librocdxg.so: cannot open shared object file: No such file or directory"
      },
      {
        "category": "path_hardcode",
        "line": "2: rocRAND internal error: hipErrorNoDevice in function ~poisson_distribution_manager at /therock/src/rocm-libraries/projects/rocrand/library/src/rng/distribution/poisson.hpp:216"
      },
      {
        "category": "missing_runtime_library",
        "line": "Cannot load librocdxg.so, failed:librocdxg.so: cannot open shared object file: No such file or directory"
      },
      {
        "category": "path_hardcode",
Click to collapse
+ Thought: 4.1s
Round 2 的真实失败已显现：ctest 修复成功，但 3/4 个测试因 WSL2 无 GPU 设备 而失败。这是 gpu_runtime_error，属于环境限制。继续编排 — debugger → repairer → 最终状态：
Therock-Debugger Task — Debug Round 2 failure
↳ 22 toolcalls · 1m 48s
ctrl+x down view subagents
▣  Therock-Loop · Big Pickle
(1 of 1)33.1K (17%) wsl  repairs/round2_repair_plan.json
2. /home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.md

Both should document that no repair actions are possible (manual_required) and explain the WSL2 limitation.

Return the paths and a brief summary.
+ Thought: 257ms
Read runs/20260715_161056_e77dea2f/round_analysis/round2.json 
Read runs/20260715_161056_e77dea2f 
Read runs/20260715_161056_e77dea2f/global_state.json 
+ Thought: 188ms
Read runs/20260715_161056_e77dea2f/failures 
Read runs/20260715_161056_e77dea2f/environment_summary.json 
Read runs/20260715_161056_e77dea2f/repairs 
+ Thought: 1.1s
Good, I have all the context. Let me now create the repair plan documents. Since the classification is gpu_runtime_error with repair_policy: manual_required, no automated or manual repair actions are possible within this agent's scope.
~ Preparing write...
▣  Therock-Repairer · Big Pickle
Based on the new text in your screenshot, the autonomous agent has progressed to its second round of debugging, and it has reached a critical conclusion regarding the environment.

Here is a breakdown of what the agent has discovered and decided:

1. The Root Cause Shift (Round 2)
Previous Step: The agent fixed the ctest missing error.

New Step: After fixing that, the tests ran again but still failed.

Actual Error: The logs show multiple failures due to Cannot load librocdxg.so (a ROCm GPU library) and a subsequent error stating hipErrorNoDevice.

Agent's Conclusion: The agent has correctly identified this as a gpu_runtime_error. It explicitly notes that these errors are happening because "WSL2 无 GPU 设备" (WSL2 has no GPU device). This isn't a bug in the code being tested; it's a hardware/environment limitation of the test runner.

2. The Agent's Decision (manual_required)
Since the issue is the physical absence of a GPU in the WSL2 environment, the AI agent realizes it cannot fix this by modifying code.

It has determined that the repair_policy is manual_required.

It states: "no automated or manual repair actions are possible within this agent's scope." It cannot magically create a GPU device, nor can it change how WSL2 is configured to interact with hardware outside of its current permissions.

3. Current Action (The Output)
The agent is currently in the Therock-Repairer subagent mode. It has read all the relevant history (round2.json, global_state.json, environment_summary.json, etc.) and is now in the process of writing two documentation files:

repairs/round2_repair_plan.json

repairs/round2_repair_plan.md

Purpose of these files: Both documents will explicitly state that no automated repair was possible and explain the WSL2 GPU limitation to the human operator. It is essentially "closing the loop" with a factual report explaining why the test environment cannot pass these specific ROCm/hipRAND tests.

Summary for you
The AI has done a fantastic job diagnosing the environment. It has exhausted its ability to fix code and is now generating a report to tell you: "The tests require a physical GPU, but your WSL2 instance doesn't have one. Please run these tests in an environment with an AMD GPU attached."

### Option 3: Accept Platform Limitation

Accept that GPU-dependent tests cannot run on WSL2-DXG. The linkage test confirms library build correctness.

- **Effort:** None
- **Pragmatic assessment:** The build itself is verified correct. The failing tests are purely runtime GPU validation, which requires hardware+driver support that this platform cannot provide.

---

## Path Hardcode Note

The `path_hardcode_detection` matches for `/therock/src/rocm-libraries/...` are **compile-time source paths** embedded in GTest assertion messages within the test binaries. They are NOT actionable path issues and should be ignored.

---

## Audit Trail

| Artifact | Path |
|----------|------|
| Repair plan (JSON) | `repairs/round2_repair_plan.json` |
| Repair plan (MD) | `repairs/round2_repair_plan.md` |
| Failure evidence | `failures/hiprand-quick_failure.json` |
| Round analysis | `round_analysis/round2.json` |
| stdout log | `logs/hiprand-quick.round2.stdout.log` |
| stderr log | `logs/hiprand-quick.round2.stderr.log` |

**No `actions.jsonl` or `tool_calls.jsonl` generated** -- no repair actions were executed.

+ Thought: 66ms
Now let me verify both files exist and are well-formed:
$ ls -la /home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.* && echo "---" && python3 -c "import json; json.load(open('/home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.json')); print('JSON: valid')"
-rw-r--r-- 1 sut1 sut1 4905 Jul 15 16:17 /home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.json
-rw-r--r-- 1 sut1 sut1 4315 Jul 15 16:17 /home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.md
---
JSON: valid
+ Thought: 194ms
Both files verified. Here's the summary:
Repair Plan Generated
Files created:
/home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.json (4.9 KB, valid JSON)
/home/sut1/TheRock/runs/20260715_161056_e77dea2f/repairs/round2_repair_plan.md (4.3 KB)
Summary
No repair actions possible. The repair_policy is manual_required and the classification is gpu_runtime_error.
Aspect	Detail
Root Cause	WSL2-DXG platform lacks /dev/kfd (Kernel Fusion Driver), which ROCm requires for GPU discovery via the HSA runtime layer
Failing tests	3 GPU-dependent tests (test_hiprand_api, test_hiprand_cpp_wrapper, test_hiprand_kernel) all fail identically with HIP error 100
Passing test	test_hiprand_linkage passes (linkage-only, no GPU needed)
Round 1 fix verified	ctest availability fix from round 1 is working correctly -- 4 tests now discovered and executed
Path hardcodes	The /therock/src/rocm-libraries/... matches are GTest compile-time source paths, not actionable issues
Resolution options documented: native Linux (preferred), WSL2 GPU passthrough (experimental), or accept the platform limitation.
▣  Therock-Repairer · Big Pickle · 52.6s
Subagent(4 of 4)20.6K (10%)
This is a great snapshot of the agent successfully completing its task. The AI has correctly diagnosed the situation and generated a clear, professional report for the human user.

Here is the final summary of what the Therock-Repairer subagent has just accomplished:

1. The Final Diagnosis
The agent has confirmed the WSL2-DXG environment does not support the ROCm runtime. It has officially classified the root cause as gpu_runtime_error due to the lack of the /dev/kfd (Kernel Fusion Driver) file. Without this, the HSA (Heterogeneous System Architecture) runtime cannot discover the GPU, leading to the hipErrorNoDevice (Error 100) failures.

2. Actionable Outputs
Since it cannot write code to fix this environmental limitation, it has completed its job by delivering:

A valid JSON file (round2_repair_plan.json) for potential downstream automation or data ingestion.

A readable Markdown file (round2_repair_plan.md) for you to read and reference.

3. Great Clarifications Provided by the Agent
Linkage test passed: It explicitly notes that test_hiprand_linkage passes. This confirms the libraries were built correctly and the build environment is fine.

Path Hardcode vs. Compile-Time: It correctly identifies that the path_hardcode_detection flagged earlier is not a real configuration issue, but simply the compile-time source paths showing up in GTest assertion messages.

Verified Round 1 fix: It confirms that the "ctest fix" from the first round worked, as all 4 tests are now successfully being discovered and executed (they just fail due to the GPU environment).

4. Next Steps for You (Per the Agent's Report)
The agent's markdown report has documented the following three resolution options for you:

Native Linux: Run the tests on a native Linux machine with an AMD GPU installed (This is the preferred method).

WSL2 GPU Passthrough: Attempt to set up GPU passthrough on your WSL2 instance (labeled as experimental and unreliable).

Accept Platform Limitation: Mark these specific 3 tests as skipped and accept that this WSL2 environment can only verify build linkage, not runtime GPU functionality.

Overall status: The AI agent has completed 100% of its automated pipeline. It cannot move past this because it requires human intervention to choose between Options 1, 2, or 3. You are ready to review the .md report and decide how to proceed.

