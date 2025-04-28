# DOIP over HTTP a first approach

In this repository you will find my first approaches to implement a proxy for DOIP over HTTP. 
It essantialy contains two tries. One for the REST-style approach were I tried to conform to as many REST standarts as possible and one approach with the RPC-style. Both appraoches consist out of a client sending requests and an very basic server. The RPC-style approach is a bit more advanced as the REST approach beacuse while working on it I decided that the RPC approach is the more sensible of them both.\\
The RPC approach implements a basic concept of sessions where the server refuses to communicte if there is no session id in the message. 


## Specifications for the RPC approach

### General
The endpoint to start interactin with the server is the "/Home" endpoint. This endpoint expects a POST HTTP request for every message and otherwise trie to conform to the DOIP specifications. But sadly a whole implementation of the DOIP specification was out of scope for this bachelors thesis.

### 0.DOIP_Op.RequestSession
This is a new Operation designed by me that is intended to be the first operation that is send in every DOIP over HTTP interaction. It initiates a handsahke were the client asks for a session id and then is assinged one by the server. This session id is then expected to be present in every following message of this interaction.

### Errors

To make errors easily understandable there need to be rules which error message from which protocol is responsible for what failure.
DOIP should be allowed tu make use of the full range of error codes that are suported and they are explained here [Digital Object Interface Protocol Specification](https://https://www.dona.net/sites/default/files/2018-11/DOIPv2Spec_1.pdf)
The HTTP error codes that should be used are the ones which doesn't have to do with data transfer or are already covered by the DOIP letters. Except when a message request and response interaction went without errors it should still confirm with the 200 Ok code. 

## REST approach
The REST approach is consistent with the specifications made in my bachelors thesis. But it is not complete because the favourable approach is the RPC approach
