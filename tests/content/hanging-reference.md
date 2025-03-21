# Hanging Reference Test

## Feature
`feat~hanging-ref~1`

Feature with reference to non-existent item

Needs: req

## Requirement
`req~hanging-req~1`

Requirement with references to non-existent items

Needs: dsn

Covers:
- feat~hanging-ref~1
- feat~non-existent~1

## Design
`dsn~hanging-design~1`
Needs: impl

Covers:
- req~hanging-req~1
- req~also-non-existent~1

## Implementation
`impl~hanging-impl~1`

Implementation with proper coverage

Covers:
- dsn~hanging-design~1