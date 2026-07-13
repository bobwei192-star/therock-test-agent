# RFC to Add OpenCL 2.2 support with OpenCL C++ to ROCm

- **Issue #:** 159
- **State:** closed
- **Created:** 2017-07-10T19:31:45Z
- **Updated:** 2020-11-19T11:57:06Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/159

To support better modularity, composability, really useful constructs such as classes, lambdas, and templates, compile time polymorphism (**very useful for performance gains over C and has a large following in CUDA**), genericity including the use of type traits, and ultimately sophisticated maximum performance focused device-side libraries such as CUB, please support OpenCL C++ in ROCm.

While ROCm already supports multiple families (HCC, OpenMP, HIP, AMP?) offering similar capabilities in separate components, none offer the simultaneous promise of an industry backed standard and a fine level control. HCC/AMP/OpenMP lack finer levels of control (in particular memory related) necessary for the highest performance code. HCC effectively compare to the vendor lock-in CUDA offers, although the project is opensource, and this ultimately islands code, in a sense.  This choice over vendors (or similarly unreliance on a single vendor) is often what drives the choice of developers and project managers to invest in OpenCL.  HIP is the most attractive option of these and essentially CUDA-lite, but not quite in runtime or operations supported and its not clear what it does and doesn't have - which is to say it doesn't follow a standard in earnest.  One more feature OpenCL has on all of these approaches is JIT compilation  - an incredibly powerful option in the right hands [(Watch this GTC video of NVidia's Jitify project for a great overview of the technique and it's importance, which OpenCL made easy from day 1!)](http://on-demand-gtc.gputechconf.com/gtcnew/on-demand-gtc.php?searchByKeyword=jitify&searchItems=&sessionTopic=&sessionEvent=&sessionYear=&sessionFormat=&submit=&select=)


ROCm has the opportunity to be first for widespread conformance and whip the rest of industry into shape.  It is not clear, with the exception of HIP, why someone would choose to invest in the other options over OpenCL C++ when they do not offer the promise of an industry standard and inherent performance from tighter control (gauging HCC and OpenMP as comparable to AMP).

Please keep this ticket open to collect support.

[This slide](http://images.anandtech.com/doci/9039/OCL21_Cpp.png) mentions a birds eye view of the feature, original source is slide 5 from [The 2016 OpenCL state of the union](http://www.iwocl.org/wp-content/uploads/iwocl-2016-opencl-state-union.pdf).  Note this feature was added ala carte to OpenCL 2.1, but more in the family in OpenCL 2.2.


