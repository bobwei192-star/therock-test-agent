# ROCm on a Steam Deck would be appreciated

- **Issue #:** 1815
- **State:** closed
- **Created:** 2022-09-29T18:48:24Z
- **Updated:** 2025-03-07T23:10:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1815

Got my Steam Deck todsay and the first thing I did with it was this

> Python 3.10.2 (main, Jan 15 2022, 19:56:27) [GCC 11.1.0] on linux
> Type "help", "copyright", "credits" or "license" for more information.
> >>> import torch
> >>> if torch.cuda.is_available() and torch.version.hip:
> ...     print('We have ROCm')
> ... else:
> ...     print('CPU Only')
> ...
> "hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
> Aborted (core dumped)
> (134)(deck@steamdeck ~)$

Are we going to get HIP / ROCm for the Steam Deck?

CC https://github.com/pytorch/pytorch/issues/85909

