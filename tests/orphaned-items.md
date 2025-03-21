# Orphaned Items Test

## Feature Definition 
`feat~root-feature~1`

Root feature with complete coverage

Needs: req

## Requirement Definition
`req~req-coverage~1`

Requirement with complete coverage

Needs: dsn

Covers: 
- feat~root-feature~1

## Design Definition
`dsn~design-coverage~1`
Needs: impl

Covers:
- req~req-coverage~1

## Implementation
`impl~impl-coverage~1`

Implementation with proper coverage

Covers:
- dsn~design-coverage~1

## Orphaned Feature 
`feat~orphaned-feature~1`

A feature that is not covered by any requirement

Needs: req

## Orphaned Design
`dsn~orphaned-design~1`
Needs: impl

## Orphaned Implementation
`impl~orphaned-impl~1`