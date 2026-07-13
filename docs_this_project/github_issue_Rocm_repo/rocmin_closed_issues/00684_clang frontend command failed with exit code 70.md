# clang frontend command failed with exit code 70

- **Issue #:** 684
- **State:** closed
- **Created:** 2019-01-22T17:56:45Z
- **Updated:** 2019-01-22T20:08:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/684

When i  run deepdream tutorial on ipython notebook. i got a error.

at terminal 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fatal error: error in backend: Cannot select: 0x3f42450: v2i64 = bitcast 0x3ee6118
  0x3ee6118: v4f32 = BUILD_VECTOR 0x3e69bb0, 0x3e84ed0, 0x3e69bb0, 0x3e84ed0
    0x3e69bb0: f32 = fmul 0x3e9bc68, 0x3e9bc68
      0x3e9bc68: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<0>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3e67780: i32 = Constant<0>
      0x3e9bc68: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<0>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3e67780: i32 = Constant<0>
    0x3e84ed0: f32 = fmul 0x3e8e3d0, 0x3e8e3d0
      0x3e8e3d0: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<1>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3eed148: i32 = Constant<1>
      0x3e8e3d0: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<1>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3eed148: i32 = Constant<1>
    0x3e69bb0: f32 = fmul 0x3e9bc68, 0x3e9bc68
      0x3e9bc68: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<0>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3e67780: i32 = Constant<0>
      0x3e9bc68: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<0>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3e67780: i32 = Constant<0>
    0x3e84ed0: f32 = fmul 0x3e8e3d0, 0x3e8e3d0
      0x3e8e3d0: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<1>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3eed148: i32 = Constant<1>
      0x3e8e3d0: f32 = extract_vector_elt 0x3ee5d08, Constant:i32<1>
        0x3ee5d08: v2f32 = bitcast 0x3eef850
          0x3eef850: v2i32,ch = load<(load 8 from %ir.623, !tbaa !19, addrspace 1)> 0x3cc4598, 0x3f05360, undef:i64
            0x3f05360: i64 = add 0x3f41fa0, 0x3ead890
              0x3f41fa0: i64,ch = CopyFromReg 0x3cc4598, Register:i64 %0
                0x3ef0a00: i64 = Register %0
              0x3ead890: i64 = shl 0x3e805d8, Constant:i32<2>
                0x3e805d8: i64 = sign_extend 0x3eeec20
                  0x3eeec20: i32 = add 0x3ef0318, Constant:i32<602112>


                0x3eeda38: i32 = Constant<2>
            0x3ebe500: i64 = undef
        0x3eed148: i32 = Constant<1>
In function: MIOpenLRNAcrossChannels4
clang: error: clang frontend command failed with exit code 70 (use -v to see invocation)
clang version 8.0 
Target: amdgcn-amd-amdhsa-amdgizcl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
clang: note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
clang: note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
MIOpen Error: /home/dlowell/MIOpenPrivate/src/tmp_dir.cpp:18: Can't execute cd /tmp/miopen-MIOpenLRNFwd.cl-1c76-4e4f-bfb2-7408; /opt/rocm/bin/clang-ocl  -DMLO_LRN_KERNEL_SZ=11 -DMLO_LRN_PAD=5 -DMLO_LRN_KERNEL_SZ1=11 -DMLO_LRN_PAD1=5 -DMLO_LRN_KERNEL_SZ0=11 -DMLO_LRN_PAD0=5 -DMLO_LRN_N_OUTPUTS=192 -DMLO_LRN_N_INPUTS=192 -DMLO_LRN_N_HORIZ_OUT_PIX=1 -DMLO_LRN_N_VERT_OUT_PIX=1 -DMLO_LRN_GROUP_SZ0=64 -DMLO_LRN_GROUP_SZ1=1 -DMLO_LRN_GROUP_LG2SZ0=1 -DMLO_LRN_GROUP_LG2SZ1=1 -DMLO_LRN_BOT_BATCH_STRIDE=602112 -DMLO_LRN_BOT_CHANNEL_STRIDE=3136 -DMLO_LRN_BOT_STRIDE=56 -DMLO_LRN_TOP_BATCH_STRIDE=602112 -DMLO_LRN_TOP_CHANNEL_STRIDE=3136 -DMLO_LRN_TOP_STRIDE=56 -DMLO_LRN_BOT_WIDTH=56 -DMLO_LRN_BOT_HEIGHT=56 -DMLO_LRN_TOP_WIDTH=56 -DMLO_LRN_TOP_HEIGHT=56 -DMLO_LRN_SCALE_BATCH_STRIDE=602112 -DMLO_LRN_SCALE_CHANNEL_STRIDE=3136 -DMLO_LRN_SCALE_STRIDE=56 -DMLO_LRN_TOPDF_BATCH_STRIDE=1 -DMLO_LRN_TOPDF_CHANNEL_STRIDE=1 -DMLO_LRN_TOPDF_STRIDE=1 -DMLO_LRN_BOTDF_BATCH_STRIDE=1 -DMLO_LRN_BOTDF_CHANNEL_STRIDE=1 -DMLO_LRN_BOTDF_STRIDE=1 -DMLO_LRN_BATCH_SZ=1 -DMLO_LRN_N_INPUTS=192 -DMLO_LRN_N_OUTPUTS=192 -DMLO_LRN_DO_SCALE=1 -DMLO_OUT_VERT_ALIGNED=1 -DMLO_OUT_HORIZ_ALIGNED=0 -DMLO_MAP_SZ4=1568 -DMLO_C1x1_PIXLEFT=0 -DMLO_DIVBY4=1 -DMLO_READ_TYPE=_FLOAT2 -DMLO_READ_UNIT=2 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_FP16=0 -mcpu=gfx803 -Wno-everything MIOpenLRNFwd.cl -o /tmp/miopen-MIOpenLRNFwd.cl-1c76-4e4f-bfb2-7408/MIOpenLRNFwd.cl.o
2019-01-23 02:43:31.467471: E tensorflow/stream_executor/rocm/rocm_dnn.cc:4259] failed to run miopenLRNForward
2019-01-23 02:45:18.275 [NotebookApp] Saving notebook at /Desktop/deepdreamへのリンク/deepdream.ipynb

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

error occurred code

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

---------------------------------------------------------------------------
InternalError                             Traceback (most recent call last)
<ipython-input-14-b253b18ff9a7> in <module>()
     35     showarray(visstd(img))
     36 
---> 37 render_naive(T(layer)[:,:,:,channel])

<ipython-input-14-b253b18ff9a7> in render_naive(t_obj, img0, iter_n, step)
     27     img = img0.copy()
     28     for i in range(iter_n):
---> 29         g, score = sess.run([t_grad, t_score], {t_input:img})
     30         # normalizing the gradient, so the same step size should work
     31         g /= g.std()+1e-8         # for different layers and networks

/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.pyc in run(self, fetches, feed_dict, options, run_metadata)
    927     try:
    928       result = self._run(None, fetches, feed_dict, options_ptr,
--> 929                          run_metadata_ptr)
    930       if run_metadata:
    931         proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)

/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.pyc in _run(self, handle, fetches, feed_dict, options, run_metadata)
   1150     if final_fetches or final_targets or (handle and feed_dict_tensor):
   1151       results = self._do_run(handle, final_targets, final_fetches,
-> 1152                              feed_dict_tensor, options, run_metadata)
   1153     else:
   1154       results = []

/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.pyc in _do_run(self, handle, target_list, fetch_list, feed_dict, options, run_metadata)
   1326     if handle is None:
   1327       return self._do_call(_run_fn, feeds, fetches, targets, options,
-> 1328                            run_metadata)
   1329     else:
   1330       return self._do_call(_prun_fn, handle, feeds, fetches)

/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.pyc in _do_call(self, fn, *args)
   1346           pass
   1347       message = error_interpolation.interpolate(message, self._graph)
-> 1348       raise type(e)(node_def, op, message)
   1349 
   1350   def _extend_graph(self):

InternalError: NormalizeBackwardWithDimensions launch failed
	 [[node gradients/import/localresponsenorm1_grad/LRNGrad (defined at <ipython-input-14-b253b18ff9a7>:25)  = LRNGrad[T=DT_FLOAT, alpha=0.0001, beta=0.5, bias=2, depth_radius=5, _device="/job:localhost/replica:0/task:0/device:GPU:0"](gradients/import/maxpool1_grad/MaxPoolGrad, import/conv2d2/_177, import/localresponsenorm1/_175)]]
	 [[{{node gradients/sub_grad/Reshape/_197}} = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_750_gradients/sub_grad/Reshape", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]

Caused by op u'gradients/import/localresponsenorm1_grad/LRNGrad', defined at:
  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/IPython/kernel/zmq/kernelapp.py", line 469, in main
    app.start()
  File "/usr/lib/python2.7/dist-packages/IPython/kernel/zmq/kernelapp.py", line 459, in start
    ioloop.IOLoop.instance().start()
  File "/usr/lib/python2.7/dist-packages/zmq/eventloop/ioloop.py", line 162, in start
    super(ZMQIOLoop, self).start()
  File "/usr/local/lib/python2.7/dist-packages/tornado/ioloop.py", line 866, in start
    handler_func(fd_obj, events)
  File "/usr/local/lib/python2.7/dist-packages/tornado/stack_context.py", line 275, in null_wrapper
    return fn(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/zmq/eventloop/zmqstream.py", line 440, in _handle_events
    self._handle_recv()
  File "/usr/lib/python2.7/dist-packages/zmq/eventloop/zmqstream.py", line 472, in _handle_recv
    self._run_callback(callback, msg)
  File "/usr/lib/python2.7/dist-packages/zmq/eventloop/zmqstream.py", line 414, in _run_callback
    callback(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tornado/stack_context.py", line 275, in null_wrapper
    return fn(*args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/IPython/kernel/zmq/ipkernel.py", line 281, in dispatcher
    return self.dispatch_shell(stream, msg)
  File "/usr/lib/python2.7/dist-packages/IPython/kernel/zmq/ipkernel.py", line 245, in dispatch_shell
    handler(stream, idents, msg)
  File "/usr/lib/python2.7/dist-packages/IPython/kernel/zmq/ipkernel.py", line 389, in execute_request
    shell.run_cell(code, store_history=store_history, silent=silent)
  File "/usr/lib/python2.7/dist-packages/IPython/core/interactiveshell.py", line 2741, in run_cell
    interactivity=interactivity, compiler=compiler)
  File "/usr/lib/python2.7/dist-packages/IPython/core/interactiveshell.py", line 2833, in run_ast_nodes
    if self.run_code(code):
  File "/usr/lib/python2.7/dist-packages/IPython/core/interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-14-b253b18ff9a7>", line 37, in <module>
    render_naive(T(layer)[:,:,:,channel])
  File "<ipython-input-14-b253b18ff9a7>", line 25, in render_naive
    t_grad = tf.gradients(t_score, t_input)[0] # behold the power of automatic differentiation!
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/gradients_impl.py", line 674, in gradients
    unconnected_gradients)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/gradients_impl.py", line 864, in _GradientsHelper
    lambda: grad_fn(op, *out_grads))
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/gradients_impl.py", line 409, in _MaybeCompile
    return grad_fn()  # Exit early
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/gradients_impl.py", line 864, in <lambda>
    lambda: grad_fn(op, *out_grads))
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/nn_grad.py", line 572, in _LRNGrad
    alpha, beta)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/ops/gen_nn_ops.py", line 4478, in lrn_grad
    alpha=alpha, beta=beta, name=name)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/op_def_library.py", line 787, in _apply_op_helper
    op_def=op_def)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/util/deprecation.py", line 488, in new_func
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3274, in create_op
    op_def=op_def)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 1770, in __init__
    self._traceback = tf_stack.extract_stack()

...which was originally created as op u'import/localresponsenorm1', defined at:
  File "<string>", line 1, in <module>
[elided 14 identical lines from previous traceback]
  File "/usr/lib/python2.7/dist-packages/IPython/core/interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-12-3b9bb4599327>", line 13, in <module>
    tf.import_graph_def(graph_def, {'input':t_preprocessed})
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/util/deprecation.py", line 488, in new_func
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/importer.py", line 443, in import_graph_def
    _ProcessNewOps(graph)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/importer.py", line 234, in _ProcessNewOps
    for new_op in graph._add_new_tf_operations(compute_devices=False):  # pylint: disable=protected-access
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3440, in _add_new_tf_operations
    for c_op in c_api_util.new_tf_operations(self)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3299, in _create_op_from_tf_operation
    ret = Operation(c_op, self)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 1770, in __init__
    self._traceback = tf_stack.extract_stack()

InternalError (see above for traceback): NormalizeBackwardWithDimensions launch failed
	 [[node gradients/import/localresponsenorm1_grad/LRNGrad (defined at <ipython-input-14-b253b18ff9a7>:25)  = LRNGrad[T=DT_FLOAT, alpha=0.0001, beta=0.5, bias=2, depth_radius=5, _device="/job:localhost/replica:0/task:0/device:GPU:0"](gradients/import/maxpool1_grad/MaxPoolGrad, import/conv2d2/_177, import/localresponsenorm1/_175)]]
	 [[{{node gradients/sub_grad/Reshape/_197}} = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_750_gradients/sub_grad/Reshape", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



I tried " sudo apt-get clang" 
but nothing changed.



How do i solve this problem?