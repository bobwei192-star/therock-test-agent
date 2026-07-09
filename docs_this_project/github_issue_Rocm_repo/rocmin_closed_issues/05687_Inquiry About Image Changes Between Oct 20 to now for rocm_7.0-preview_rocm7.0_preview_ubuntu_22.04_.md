# Inquiry About Image Changes Between Oct 20 to now for rocm/7.0-preview:rocm7.0_preview_ubuntu_22.04_vllm_0.10.1_instinct_beta

- **Issue #:** 5687
- **State:** closed
- **Created:** 2025-11-21T07:13:54Z
- **Updated:** 2026-02-20T19:07:24Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5687

I am currently using the Docker image:
rocm/7.0-preview:rocm7.0_preview_ubuntu_22.04_vllm_0.10.1_instinct_beta
 
Recently, I pulled this image again and noticed that although the tag remains the same, the source code inside the preinstalled vllm package (specifically the filesystem under /opt/venv/lib/python3.10/site-packages/vllm) is different from what I obtained in an earlier pull. Because I need to modify the VLLM source code to support MXFP emulation experiments qdq.
 
This caused the current image to be slower than the previous one, but I accidentally deleted the previous image version. I thought it would be the same, so I re-pulled this image, but the VLLM inference speed has become slower.
 
So, were there any updates, rebuilds, or modifications made to this image between October 20 to now? Even if the tag did not change, any rebuild that altered the content would be important for me to know.
 
If there were changes, is it possible to obtain or access the image version that between Oct 20-Oct 24? If you're not sure, could you tell me who I can contact to know this problem?
