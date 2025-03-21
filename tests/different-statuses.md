# Different Statuses Test

## Feature (Approved)
`feat~status-feature~1`

Status: approved

Feature with different status items in trace chain

Needs: req

## Requirement (Draft)
`req~status-req~1`

Status: draft

Requirement in draft status

Needs: dsn

Covers: 
- feat~status-feature~1

## Design (Proposed)
`dsn~status-dsn~1`

Status: proposed

Design in proposed status

Needs: impl

Covers:
- req~status-req~1

## Implementation (Rejected)
`impl~status-impl-rejected~1`

Status: rejected

Rejected implementation

Covers:
- dsn~status-dsn~1

## Implementation (Accepted)
`impl~status-impl-accepted~1`

Status: accepted

Accepted implementation

Covers:
- dsn~status-dsn~1