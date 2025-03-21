# Complex Coverage Graph Test

## Feature Definition 
`feat~complex-root~1`

Root feature with complex coverage paths

Needs: req

## Sub-Feature
`feat~complex-sub~1`

Sub-feature with its own coverage

Needs: req

## Requirement 1
`req~complex-req1~1`

First requirement 

Needs: dsn

Covers: 
- feat~complex-root~1

## Requirement 2
`req~complex-req2~1`

Second requirement

Needs: dsn

Covers: 
- feat~complex-root~1
- feat~complex-sub~1

## Design 1
`dsn~complex-dsn1~1`
Needs: impl

Covers:
- req~complex-req1~1

## Design 2
`dsn~complex-dsn2~1`
Needs: impl

Covers:
- req~complex-req2~1
- req~complex-req1~1

## Implementation 1
`impl~complex-impl1~1`

First implementation

Covers:
- dsn~complex-dsn1~1

## Implementation 2
`impl~complex-impl2~1`

Second implementation 

Covers:
- dsn~complex-dsn2~1

## Test 1
`test~complex-test1~1`

Test case

Covers:
- impl~complex-impl1~1

## Test 2
`test~complex-test2~1`

Second test case

Covers:
- impl~complex-impl2~1