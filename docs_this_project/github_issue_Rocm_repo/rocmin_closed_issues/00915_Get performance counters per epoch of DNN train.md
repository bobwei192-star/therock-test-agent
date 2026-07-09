# Get performance counters per epoch of DNN train

- **Issue #:** 915
- **State:** closed
- **Created:** 2019-10-21T19:42:15Z
- **Updated:** 2023-12-18T17:13:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/915

I would like to get some help regarding the use of the Library public API of rocprofiler. 
I am currently using the AMD Radeon Vega Frontier Edition to train machine learning models using the PyTorch framework. As part of my task, I need to get the output of the performance counters between each epoch of the train and get it while the model is training.
The pseudocode of the application is something like:

Init Program;
for epoch in range(1,10): {
    Reset performance counters;
    Train(); //Train one epoch of the model;
    Output Performance counters value of epoch to file;
}

What is the best way to accomplish this? Since my framework is in python, I was thinking of creating a .so file with the API methods written in C++. Can I invocate APIs calls in my PyTorch script that interacts with the rocprof command-line tool?

Thank you for your help.

Setup:
- ROCM 2.8
- CentOS 7.5
- Python 3.6
- PyTorch 1.3