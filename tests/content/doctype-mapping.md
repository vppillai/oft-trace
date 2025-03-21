# Document Type Mapping Test

## System Requirement
`sys~system-req~1`

System-level requirement

Needs: srs, subsys

## Software Requirement
`srs~software-req~1`

Software requirement

Needs: subsys

Covers:
- sys~system-req~1

## Subsystem Design
`subsys~subsystem-design~1`

Subsystem design document

Needs: module

Covers:
- sys~system-req~1
- srs~software-req~1

## Module Design
`module~module-design~1`

Module design

Needs: code

Covers:
- subsys~subsystem-design~1

## Code Implementation
`code~implementation~1`

Implementation in code

Covers:
- module~module-design~1