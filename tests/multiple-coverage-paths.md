# Multiple Coverage Paths Test

## Feature Definition 
`feat~multiple-paths~1`

Feature with multiple coverage paths

Needs: req

## Requirement Definition 1
`req~path1-req~1`

First requirement path

Needs: dsn

Covers: 
- feat~multiple-paths~1

## Requirement Definition 2
`req~path2-req~1`

Second requirement path

Needs: arch

Covers: 
- feat~multiple-paths~1

## Design Definition
`dsn~path1-design~1`
Needs: impl

Covers:
- req~path1-req~1

## Architecture Definition
`arch~path2-arch~1`
Needs: impl

Covers:
- req~path2-req~1

## Implementation 1
`impl~path1-impl~1`

Implementation for path 1

Covers:
- dsn~path1-design~1

## Implementation 2
`impl~path2-impl~1`

Implementation for path 2

Covers:
- arch~path2-arch~1