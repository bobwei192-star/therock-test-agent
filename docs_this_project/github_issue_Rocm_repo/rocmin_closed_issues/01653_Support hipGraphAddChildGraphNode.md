# Support hipGraphAddChildGraphNode

- **Issue #:** 1653
- **State:** closed
- **Created:** 2022-01-01T19:07:19Z
- **Updated:** 2024-02-01T17:28:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1653

Currently, with the experimental HIP graph API it is not possible to embed one graph inside of another (cf cuGraphAddChildGraphNode).  The node type is listed in the relevant node type enum as hipGraphNodeTypeGraph, but there is no corresponding function.

Child graph nodes are useful if one wishes to include third party library calls in a graph, for example to rocBLAS.  Here, one can use the stream capturing functionality to obtain a graph which corresponds to the relevant third party kernels and then embed this as a child graph node.