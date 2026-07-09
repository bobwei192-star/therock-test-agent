# Met problems using hipcub.hpp

- **Issue #:** 2045
- **State:** closed
- **Created:** 2023-04-14T03:37:31Z
- **Updated:** 2023-04-17T14:44:30Z
- **Assignees:** MathiasMagnus
- **URL:** https://github.com/ROCm/ROCm/issues/2045

Hi, recently I need to use ROCm to compile PaddlePaddle. But I met this problem:
<img width="993" alt="96159e6e67a407900b5515b4b67063a9" src="https://user-images.githubusercontent.com/20554008/231935393-79e50863-27df-4404-83b8-5f0a16c63eeb.png">


However, I have already include the corresponding head files:
<img width="308" alt="1b26b9662d2a067e3e55c9929f25be0f" src="https://user-images.githubusercontent.com/20554008/231935183-acb43699-38ce-43db-bffd-936951706673.png">

I check the hipcub.hpp, which includes the util_type.cuh file. But it cannot find the hipcub::Traits. Can anyone help?