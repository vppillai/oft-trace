# Duplicate Coverage Test

## Feature
`feat~duplicate~1`

Feature with duplicate coverage

Needs: req

## Requirement 1
`req~dup-req1~1`

First requirement

Needs: dsn

Covers: 
- feat~duplicate~1

## Requirement 2
`req~dup-req2~1`

Second requirement

Needs: dsn

Covers: 
- feat~duplicate~1

## Design 1
`dsn~dup-dsn1~1`
Needs: impl

Covers:
- req~dup-req1~1
- req~dup-req2~1

## Implementation
`impl~dup-impl~1`

Implementation that covers multiple designs

Covers:
- dsn~dup-dsn1~1
- req~dup-req1~1