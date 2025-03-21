# Very Long Chain Test

## Business Requirement
`bus~business-need~1`

Top-level business requirement

Needs: feat

## Feature
`feat~feature-spec~1`

Feature specification

Needs: epic

Covers:
- bus~business-need~1

## Epic
`epic~epic-story~1`

Epic level requirement

Needs: story

Covers:
- feat~feature-spec~1

## User Story
`story~user-story~1`

User story

Needs: sys

Covers:
- epic~epic-story~1

## System Requirement
`sys~system-req~1`

System requirement

Needs: srs

Covers:
- story~user-story~1

## Software Requirement
`srs~software-req~1`

Software requirement

Needs: arch

Covers:
- sys~system-req~1

## Architecture
`arch~architecture~1`

Architecture specification

Needs: dsn

Covers:
- srs~software-req~1

## Design
`dsn~detailed-design~1`

Detailed design

Needs: impl

Covers:
- arch~architecture~1

## Implementation
`impl~code-impl~1`

Code implementation

Needs: utest

Covers:
- dsn~detailed-design~1

## Unit Test
`utest~unit-test~1`

Unit testing

Needs: itest

Covers:
- impl~code-impl~1

## Integration Test
`itest~integration-test~1`

Integration testing

Needs: stest

Covers:
- utest~unit-test~1

## System Test
`stest~system-test~1`

System testing

Needs: atest

Covers:
- itest~integration-test~1

## Acceptance Test
`atest~acceptance-test~1`

Acceptance testing

Covers:
- stest~system-test~1