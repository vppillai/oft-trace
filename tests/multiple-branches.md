# Multiple Branches Test

## Root Feature
`feat~branching~1`

Feature that branches into multiple component trees

Needs: req

## Requirement (Frontend)
`req~frontend-req~1`

Frontend requirement

Needs: fdsn

Covers:
- feat~branching~1

## Requirement (Backend)
`req~backend-req~1`

Backend requirement

Needs: bdsn

Covers:
- feat~branching~1

## Frontend Design
`fdsn~frontend-design~1`

Frontend design

Needs: fimpl

Covers:
- req~frontend-req~1

## Backend Design
`bdsn~backend-design~1`

Backend design

Needs: bimpl

Covers:
- req~backend-req~1

## Frontend Implementation
`fimpl~frontend-impl~1`

Frontend implementation

Covers:
- fdsn~frontend-design~1

## Backend Implementation
`bimpl~backend-impl~1`

Backend implementation

Covers:
- bdsn~backend-design~1