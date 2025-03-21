# Non-Standard Artifact Types Test

## Feature
`feat~custom-types~1`

Feature requiring non-standard artifact types

Needs: usecase, story

## Use Case
`usecase~main-flow~1`

Custom type: Use case artifact

Needs: story

Covers:
- feat~custom-types~1

## User Story
`story~customer-need~1`

Custom type: User story artifact

Needs: mockup

Covers:
- usecase~main-flow~1

## UI Mockup
`mockup~frontend-design~1`

Custom type: UI mockup artifact

Needs: code

Covers:
- story~customer-need~1

## Frontend Code
`code~ui-implementation~1`

Custom type: Code artifact

Covers:
- mockup~frontend-design~1