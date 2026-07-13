# Adrenalin AI Bundle fails to create virtual environment

- **Issue #:** 5909
- **State:** closed
- **Created:** 2026-01-28T15:25:35Z
- **Updated:** 2026-03-18T17:49:22Z
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5909

Originally reported in https://github.com/ROCm/ROCm/issues/5871#issuecomment-3792900807.

After selecting "Create a Virtual Environment" in the AI Bundle options, the command block that's supposed to house the `pip install` commands is empty.

<img width="1092" height="917" alt="Image" src="https://github.com/user-attachments/assets/5961dae0-0aee-45f8-9926-caad48c23a45" />

In this case, opting to create the virtual environment fails with the following error,

<img width="754" height="525" alt="Image" src="https://github.com/user-attachments/assets/a56d54a3-f823-483b-8255-3b3d0476f9ad" />