# Across-Repository Tracing Test

## Feature
`feat~cross-repo~1`

Feature that references requirements in other repositories

Needs: req

## Requirement (External)
`req~external-req~1`

Requirement from an external system/repository

Needs: dsn

Covers: 
- feat~cross-repo~1

## Design
`dsn~external-design~1`
Needs: impl

Covers:
- req~external-req~1

## Implementation
`impl~external-impl~1`

Implementation that connects to external systems

Covers:
- dsn~external-design~1