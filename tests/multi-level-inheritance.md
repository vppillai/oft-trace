# Multi-Level Inheritance Test

## Base Feature
`feat~base-feature~1`

Base feature that others inherit from

Needs: req

## Inherited Feature
`feat~inherited-feature~1`

Feature that inherits from base

Needs: req

Covers:
- feat~base-feature~1

## Further Inherited Feature
`feat~further-inherited~1`

Feature that inherits from the inherited feature

Needs: req

Covers:
- feat~inherited-feature~1

## Requirement
`req~multi-level-req~1`

Requirement covering all levels

Needs: dsn

Covers:
- feat~base-feature~1
- feat~inherited-feature~1
- feat~further-inherited~1

## Design
`dsn~multi-level-design~1`
Needs: impl

Covers:
- req~multi-level-req~1

## Implementation
`impl~multi-level-impl~1`

Implementation for all levels

Covers:
- dsn~multi-level-design~1