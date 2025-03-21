# Regression Test with Direct vs. Indirect Coverage

## Root Feature
`feat~regression~1`

Feature for testing regression in coverage

Needs: req

## Requirement
`req~regression-req~1`

Requirement for regression testing

Needs: dsn

Covers:
- feat~regression~1

## Design
`dsn~regression-design~1`
Needs: impl

Covers:
- req~regression-req~1

## Implementation
`impl~regression-impl-direct~1`

Implementation with direct coverage to req (should not be needed)

Covers:
- dsn~regression-design~1
- req~regression-req~1

## Test
`test~regression-test~1`

Test that covers implementation

Covers:
- impl~regression-impl-direct~1