# Self-Coverage Test

## Feature/Requirement Combo
`feat~self-coverage~1`

Item with self-coverage (covers itself)

Needs: dsn

Covers:
- feat~self-coverage~1

## Design
`dsn~self-design~1`
Needs: impl

Covers:
- feat~self-coverage~1

## Implementation
`impl~self-impl~1`

Implementation for self-coverage

Covers:
- dsn~self-design~1