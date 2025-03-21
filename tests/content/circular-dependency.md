# Circular Dependency Test

## Feature Definition 
`feat~circular~1`

Feature involved in circular dependency

Needs: req

## Requirement Definition
`req~circular-req~1`

Requirement involved in circular dependency

Needs: dsn

Covers: 
- feat~circular~1

## Design Definition
`dsn~circular-design~1`
Needs: arch

Covers:
- req~circular-req~1

## Architecture Definition
`arch~circular-arch~1`
Needs: impl

Covers:
- dsn~circular-design~1

## Implementation
`impl~circular-impl~1`

Implementation that creates a circular reference

Covers:
- arch~circular-arch~1
- req~circular-req~1