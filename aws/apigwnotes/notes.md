# API Gateway Deep Dive.

## Useful Links
* [ApiGateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html)
* [Rest API vs HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)


## Rest vs WebScoket APIs.

* API Gateway Rest APIs use a request/response model where a client sends a 
  request to a service and the service responds back synchronously.

* WebSocket APIs provide 2-way communication in that backend service can initiate 
  communications (not just send responses to requests). While a Rest API, receives
  and responds to requests, a WebSocket API supports 2-way communication between
  client apps and your backend. The backend can send callback messages to 
  connected clients.


**HTTP vs REST**

* HTTP APIs are cheaper and faster than REST APIs. Released in 2019, they lack all 
  the functionality that Rest APIs provide.


## API Endpoints.
An API endpoint type refers to hostname of the API. 

### Edge-optimized API endpoint.
* For geographically distributed clients.
* Requests are routed to the nearest cloudfront point of presence.

### Regional API endpoints
* Intended for clients in the same region or intended to serve a small number of
  clients with high demands. 
* Regional API reduces connection overhead.
* Pass all header names through as-is

### Private API endpoints
* Can only be accessed from your AWS VPC using an interface VPC endpoint, which is
  and endpoint network interface (ENI) that you create in your VPC.

