# Prefix Matching Test

## API Feature
`api-feat~rest-endpoints~1`

API feature with prefixed ID

Needs: api-req

## API Requirement
`api-req~authentication~1`

API requirement with prefixed ID

Needs: api-dsn

Covers:
- api-feat~rest-endpoints~1

## API Design
`api-dsn~jwt-tokens~1`

API design with prefixed ID

Needs: api-impl

Covers:
- api-req~authentication~1

## API Implementation
`api-impl~token-validation~1`

API implementation with prefixed ID

Covers:
- api-dsn~jwt-tokens~1