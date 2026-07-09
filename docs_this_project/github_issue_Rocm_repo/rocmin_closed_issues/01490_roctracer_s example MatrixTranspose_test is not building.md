# roctracer's example MatrixTranspose_test is not building

- **Issue #:** 1490
- **State:** closed
- **Created:** 2021-06-04T21:23:49Z
- **Updated:** 2021-06-18T04:37:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1490

roctracer/test/MatrixTranspose_test:
ubuntu 1804
rocm 4.2 (also tried 4.1)
from roctracer/test/MatrixTranspose_test:
issue "make" and it outputs following errors:

```
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g -I../../inc -I/opt/rocm/hsa/include/hsa -I/opt/rocm/hsa/include -I/opt/rocm/hip/include -I/opt/rocm/include -DLOCAL_BUILD=1 -DHIP_VDI=0 -DITERATIONS=100 -DAMD_INTERNAL_BUILD=1 -DHIP_TEST=1 --rocm-path=/opt/rocm -c -o MatrixTranspose.o MatrixTranspose.cpp
In file included from MatrixTranspose.cpp:234:
../../inc/roctracer_hip.h:41:10: fatal error: 'hip_ostream_ops.h' file not found
#include <hip_ostream_ops.h>
         ^~~~~~~~~~~~~~~~~~~
1 error generated when compiling for gfx900.
Makefile:43: recipe for target 'MatrixTranspose.o' failed
make: *** [MatrixTranspose.o] Error 1
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# nano -w MatrixTranspose.cpp
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g -I../../inc -I/opt/rocm/hsa/include/hsa -I/opt/rocm/hsa/include -I/opt/rocm/hip/include -I/opt/rocm/include -DLOCAL_BUILD=1 -DHIP_VDI=0 -DITERATIONS=100 -DAMD_INTERNAL_BUILD=1 -DHIP_TEST=1 --rocm-path=/opt/rocm -c -o MatrixTranspose.o MatrixTranspose.cpp
In file included from MatrixTranspose.cpp:234:
../../inc/roctracer_hip.h:41:10: fatal error: 'hip_ostream_ops.h' file not found
#include <hip_ostream_ops.h>
         ^~~~~~~~~~~~~~~~~~~
1 error generated when compiling for gfx900.
Makefile:43: recipe for target 'MatrixTranspose.o' failed
make: *** [MatrixTranspose.o] Error 1
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# nano -w ../../inc/roctracer_hip.h
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# nano -w ../../inc/roctracer_hip.h
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test#
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test#
root@guest:~/ROCm-4.2/roctracer/test/MatrixTranspose_test#

```

There appears to be another similar MatrixTranspose folder but without test suffix in roctracer/test/MatrixTranspose.
this one builds OK.
Comparing these two, files I imagine the MatrixTranspose_test is the one that leverages the roctracer by modifying the same file in MatrixTranspose folder but in doing so build has failed (above.)
Diff shows numerious differences, one looking more like C style and other one is C++ style includes.


```
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCH   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCH
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWIS   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWIS
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
THE SOFTWARE.                                                   THE SOFTWARE.
*/                                                              */

#include <iostream>                                           | #include <stdarg.h>
                                                              > #include <stdio.h>
                                                              > #include <stdlib.h>
                                                              >
                                                              > #ifdef __cplusplus
                                                              > #include <cstdlib>
                                                              > using namespace std;
                                                              > #else
                                                              > #include <stdlib.h>
                                                              > #endif

// hip header file                                            <
#include <hip/hip_runtime.h>                                  <
#include "roctracer_ext.h"                                    <
// roctx header file                                            // roctx header file
#include <roctx.h>                                              #include <roctx.h>
                                                              > // roctracer extension API
                                                              > #include <roctracer_ext.h>

                                                              > #ifdef __cplusplus
                                                              > static thread_local const size_t msg_size = 512;
                                                              > static thread_local char* msg_buf = NULL;
                                                              > static thread_local char* message = NULL;
                                                              > #else
                                                              > static const size_t msg_size = 512;
                                                              > static char* msg_buf = NULL;
                                                              > static char* message = NULL;
                                                              > #endif
                                                              > void SPRINT(const char* fmt, ...) {
                                                              >   if (msg_buf == NULL) {
                                                              >     msg_buf = (char*) calloc(msg_size, 1);
                                                              >     message = msg_buf;
                                                              >   }
                                                              >
                                                              >   va_list args;
                                                              >   va_start(args, fmt);
:

```