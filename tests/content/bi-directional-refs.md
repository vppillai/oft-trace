# Bi-Directional References Test

## Component A
`comp~component-a~1`

Component with bi-directional dependency

Needs: comp

Covers:
- comp~component-b~1

## Component B
`comp~component-b~1`

Component with bi-directional dependency

Needs: comp

Covers:
- comp~component-a~1

## Implementation A
`impl~impl-a~1`

Implementation of component A

Covers:
- comp~component-a~1

## Implementation B
`impl~impl-b~1`

Implementation of component B

Covers:
- comp~component-b~1