# API Gateway.

## Concepts.

*API Gateway*:



## API Gateway with authorization method.
1. create new authorizer
  - point to the autorizer lambda
  - Select 'Token' for the Lambda event payload, add a token source 'a key that will be passed in header'
    eg: jwt_token. Token validation: enter pass (can be any string)
  - turn authorization for the specific method and select the new authorizer.

```
> curl https://lx0tbp52uh.execute-api.us-east-1.amazonaws.com/beta --header "jwt_token: pass"
{"statusCode": 200, "body": "\"Hello from Lambda!\""}%
```

## API Gateway with api key authentication.
1. Create a new API key.
2. attach it to a usage plan
3. associate the usage plan to the api.
4. turn api key required for the methods.

```
> curl https://lx0tbp52uh.execute-api.us-east-1.amazonaws.com/beta --header "jwt_token: pass" --header "x-api-key:HhxxxxxxxxxxxxxLAh"
{"statusCode": 200, "body": "\"Hello from Lambda (Version 2.0!\""}%
```
