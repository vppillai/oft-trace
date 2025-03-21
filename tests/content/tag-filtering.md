# Tag Filtering Test

## Feature (Tagged)
`feat~tagged-feature~1`

Tags: important, security, frontend

Feature with multiple tags

Needs: req

## Requirement (Security)
`req~security-req~1`

Tags: security, priority-1

Security requirement

Needs: dsn

Covers:
- feat~tagged-feature~1

## Requirement (Performance)
`req~performance-req~1`

Tags: performance, optimization

Performance requirement

Needs: dsn

Covers:
- feat~tagged-feature~1

## Design (Tagged)
`dsn~tagged-design~1`

Tags: security, backend

Security design

Needs: impl

Covers:
- req~security-req~1

## Implementation (Tagged)
`impl~security-impl~1`

Tags: security, encryption

Security implementation

Covers:
- dsn~tagged-design~1