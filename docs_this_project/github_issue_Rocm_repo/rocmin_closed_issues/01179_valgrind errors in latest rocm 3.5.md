# valgrind errors in latest rocm 3.5

- **Issue #:** 1179
- **State:** closed
- **Created:** 2020-07-12T23:09:16Z
- **Updated:** 2020-12-16T17:26:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/1179

```
==7058== Conditional jump or move depends on uninitialised value(s)
==7058==    at 0x10779AB0: llvm::ConstantExpr::getGetElementPtr(llvm::Type*, llvm::Constant*, llvm::ArrayRef<llvm::Value*>, bool, llvm::Optional<unsigned int>, llvm::Type*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035DB7D: (anonymous namespace)::SymbolicallyEvaluateGEP(llvm::GEPOperator const*, llvm::ArrayRef<llvm::Constant*>, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035E163: (anonymous namespace)::ConstantFoldInstOperandsImpl(llvm::Value const*, unsigned int, llvm::ArrayRef<llvm::Constant*>, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035CA2E: (anonymous namespace)::ConstantFoldConstantImpl(llvm::Constant const*, llvm::DataLayout const&, llvm::TargetLibraryInfo const*, llvm::SmallDenseMap<llvm::Constant*, llvm::Constant*, 4u, llvm::DenseMapInfo<llvm::Constant*>, llvm::detail::DenseMapPair<llvm::Constant*, llvm::Constant*> >&) [clone .part.313] (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035CCE9: llvm::ConstantFoldConstant(llvm::Constant const*, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035CF87: (anonymous namespace)::SymbolicallyEvaluateGEP(llvm::GEPOperator const*, llvm::ArrayRef<llvm::Constant*>, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035E163: (anonymous namespace)::ConstantFoldInstOperandsImpl(llvm::Value const*, unsigned int, llvm::ArrayRef<llvm::Constant*>, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035CA2E: (anonymous namespace)::ConstantFoldConstantImpl(llvm::Constant const*, llvm::DataLayout const&, llvm::TargetLibraryInfo const*, llvm::SmallDenseMap<llvm::Constant*, llvm::Constant*, 4u, llvm::DenseMapInfo<llvm::Constant*>, llvm::detail::DenseMapPair<llvm::Constant*, llvm::Constant*> >&) [clone .part.313] (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x1035CCE9: llvm::ConstantFoldConstant(llvm::Constant const*, llvm::DataLayout const&, llvm::TargetLibraryInfo const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x10078B08: combineInstructionsOverFunction(llvm::Function&, llvm::InstCombineWorklist&, llvm::AAResults*, llvm::AssumptionCache&, llvm::TargetLibraryInfo&, llvm::DominatorTree&, llvm::OptimizationRemarkEmitter&, llvm::BlockFrequencyInfo*, llvm::ProfileSummaryInfo*, unsigned int, llvm::LoopInfo*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x10079FE9: llvm::InstructionCombiningPass::runOnFunction(llvm::Function&) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058==    by 0x10812912: llvm::FPPassManager::runOnFunction(llvm::Function&) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7058== 
```

and

```
==7091== Conditional jump or move depends on uninitialised value(s)
==7091==    at 0x10779AB0: llvm::ConstantExpr::getGetElementPtr(llvm::Type*, llvm::Constant*, llvm::ArrayRef<llvm::Value*>, bool, llvm::Optional<unsigned int>, llvm::Type*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x106EBA13: (anonymous namespace)::BitcodeReader::parseConstants() (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x106F4784: (anonymous namespace)::BitcodeReader::parseFunctionBody(llvm::Function*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x106FC66E: (anonymous namespace)::BitcodeReader::materialize(llvm::GlobalValue*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x1082E8E9: llvm::Module::materialize(llvm::GlobalValue*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x107D06E3: llvm::GlobalValue::materialize() (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0xF5BE6CE: (anonymous namespace)::IRLinker::materialize(llvm::Value*, bool) [clone .constprop.460] (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x102B973B: (anonymous namespace)::Mapper::mapValue(llvm::Value const*) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0x102BEDE0: llvm::ValueMapper::mapValue(llvm::Value const&) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0xF5C18E8: (anonymous namespace)::IRLinker::run() [clone .constprop.453] (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0xF5C3F2B: llvm::IRMover::move(std::unique_ptr<llvm::Module, std::default_delete<llvm::Module> >, llvm::ArrayRef<llvm::GlobalValue*>, std::function<void (llvm::GlobalValue&, std::function<void (llvm::GlobalValue&)>)>, bool) (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
==7091==    by 0xF5C8F61: (anonymous namespace)::ModuleLinker::run() [clone .constprop.230] (in /opt/rocm-3.5.0/lib/libamd_comgr.so.1.6.30500)
```

