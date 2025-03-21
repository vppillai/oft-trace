# Mixed Coverage Test

## Feature Definition 
`feat~mixed-feature~1`

Feature with mixed coverage (some paths covered, some not)

Needs: req

## Requirement 1 (Covered)
`req~mixed-req1~1`

Fully covered requirement path

Needs: dsn

Covers: 
- feat~mixed-feature~1

## Requirement 2 (Uncovered)
`req~mixed-req2~1`

Uncovered requirement path

Needs: dsn

Covers: 
- feat~mixed-feature~1

## Design 1 (Covered)
`dsn~mixed-dsn1~1`
Needs: impl

Covers:
- req~mixed-req1~1

## Design 2 (Uncovered)
`dsn~mixed-dsn2~1`
Needs: impl

## Implementation
`impl~mixed-impl~1`

Implementation covering only one path

Covers:
- dsn~mixed-dsn1~1