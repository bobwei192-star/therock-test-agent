# Formatting for some tables looks odd

- **Issue #:** 1955
- **State:** closed
- **Created:** 2023-03-16T14:15:40Z
- **Updated:** 2023-03-24T14:32:24Z
- **Labels:** Documentation
- **Assignees:** Naraenda
- **URL:** https://github.com/ROCm/ROCm/issues/1955

![image](https://user-images.githubusercontent.com/6463881/225644616-3d6ac409-5e5a-46c6-9a7a-11f45069ea59.png)

Was discussing with @AlexVlx

Mainly this seems to result from putting the table header in a single column (so you get fixed width + wrap).  Not clear what the best solution is here, perhaps splitting it to be e.g., "Table 1" in the top row (to keep it from wrapping / looking out of place), and put a 'caption' below in some other format?

