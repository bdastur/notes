# API Gateway Deep Dive.

## Useful Links
* [ApiGateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html)



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


