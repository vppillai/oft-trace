# Long Chain Test

## Feature
`feat~long-chain~1`

Feature at the start of a long chain

Needs: req

## Requirement
`req~long-chain-req~1`

Requirement for long chain

Needs: epic

Covers: 
- feat~long-chain~1

## Epic
`epic~long-chain-epic~1`

Epic level item

Needs: arch

Covers:
- req~long-chain-req~1

## Architecture
`arch~long-chain-arch~1`

Architecture item

Needs: dsn

Covers:
- epic~long-chain-epic~1

## Design
`dsn~long-chain-dsn~1`

Design item

Needs: impl

Covers:
- arch~long-chain-arch~1

## Implementation
`impl~long-chain-impl~1`

Implementation item

Needs: utest

Covers:
- dsn~long-chain-dsn~1

## Unit Test
`utest~long-chain-utest~1`

Unit test item

Needs: itest

Covers:
- impl~long-chain-impl~1

## Integration Test
`itest~long-chain-itest~1`

Integration test item

Covers:
- utest~long-chain-utest~1