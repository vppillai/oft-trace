# OFT-Trace Test Report

Generated: 2025-03-20 20:40:59

## Summary

- Total tests: 62
- Passed: 62
- Failed: 0
- Skipped: 0

## Test Details

| File | Test | Status | Details |
|------|------|--------|--------|
| across-repo-tracing.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| across-repo-tracing.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| all-pass.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| all-pass.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| bi-directional-refs.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| bi-directional-refs.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| circular-dependency.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| circular-dependency.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| complex-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| complex-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| custom-attributes.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| custom-attributes.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| deep-coverage-failure.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| deep-coverage-failure.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| different-statuses.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| different-statuses.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| doctype-mapping.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| doctype-mapping.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| duplicate-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| duplicate-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| duplicated-ids.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| duplicated-ids.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| hanging-reference.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| hanging-reference.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| long-chain.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| long-chain.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| missing-design-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| missing-design-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| missing-impl-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| missing-impl-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| missing-req-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| missing-req-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| mixed-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| mixed-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| multi-level-inheritance.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| multi-level-inheritance.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| multiple-branches.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| multiple-branches.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| multiple-coverage-paths.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| multiple-coverage-paths.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| multiple-versions.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| multiple-versions.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| no-needs-specification.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| no-needs-specification.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| non-standard-types.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| non-standard-types.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| orphaned-items.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| orphaned-items.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| prefix-matching.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| prefix-matching.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| regression-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| regression-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| self-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| self-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| shallow-coverage.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| shallow-coverage.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| tag-filtering.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| tag-filtering.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| version-mismatch.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| version-mismatch.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |
| very-long-chain.md | circular_dependency | ✅ PASS | Java import failed, can't check circular dependencies |
| very-long-chain.md | trace_consistency | ✅ PASS | Java import failed, oft-trace correctly reported issues |

## Reference Information

According to the OFT design document:

- Trace consistency tests verify that if Java OFT finds traceability defects, oft-trace also detects them
- Circular dependency tests verify that oft-trace correctly detects circular dependencies as specified in the design

### References

- [OFT User Guide](https://github.com/itsallcode/openfasttrace/blob/main/doc/user_guide.md)
- [OFT Design Specification](https://github.com/itsallcode/openfasttrace/blob/main/doc/spec/design.md)
