# Duplicated IDs Test

## Feature
`feat~duplicate-id~1`

First declaration of duplicate feature ID

Needs: req1

## Feature (Duplicate)
`feat~duplicate-id~1`

Second declaration of the same feature ID (intentional)

Needs: req2

## Requirement 1
`req~req1~1`

First requirement covering first duplicate

Needs: dsn

Covers:
- feat~duplicate-id~1

## Requirement 2
`req~req2~1`

Second requirement covering second duplicate

Needs: dsn

Covers:
- feat~duplicate-id~1

## Design
`dsn~duplicate-design~1`
Needs: impl

Covers:
- req~req1~1
- req~req2~1

## Implementation
`impl~duplicate-impl~1`

Implementation for duplicates

Covers:
- dsn~duplicate-design~1