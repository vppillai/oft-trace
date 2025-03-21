# Deep Coverage Failure Test

## Feature Definition 
`feat~deep-coverage~1`

Feature with direct requirement coverage but breaks in the deeper chain

Needs: req

## Requirement Definition
`req~deep-req~1`

Requirement that needs design coverage

Needs: dsn

Covers: 
- feat~deep-coverage~1

## Design Definition
`dsn~deep-design~1`
Needs: impl

Covers:
- req~deep-req~1

## Incomplete Implementation
`impl~deep-impl~1`

This implementation doesn't cover the design