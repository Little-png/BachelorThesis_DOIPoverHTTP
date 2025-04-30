# DOIP over HTTP a first approach

This repository contains my first approaches to implement a proxy for DOIP over HTTP. 
It essantialy contains two diffrent ideas. One is a REST-style approach were I tried to conform to as many REST standarts as possible and the other is a the RPC-style. Both approaches consist out of a client sending requests and an very basic server. The RPC-style approach is a bit more advanced than the REST approach because while working on both, I decided that the RPC approach is the more feasible of them both.
The RPC approach implements a basic concept of sessions where the server refuses to communicate if there is no session ID in the message. This warranted a change in every DOIP response or request Message, so I added a field where a session ID can be assinged for every message.


## Specifications for the RPC approach

### General
The endpoint to start interacting with the server is the "/Home" endpoint. This endpoint expects a POST HTTP request for every message and otherwise tries to conform to the DOIP specifications. Unfortunately a whole implementation of the DOIP specifications was out of scope for this bachelors thesis.

### 0.DOIP_Op.RequestSession
I designed this new operation with the intend to be the first operation that is sent in every DOIP over HTTP interaction. It initiates a handshake where the client first asks for a session ID and then is assinged one by the server. This session ID is then expected to be present in every following message of this interaction.

### Errors

To make errors easy to understand, there need to be rules which error message from which protocol is corresponding to what error.
DOIP should be allowed tu make use of the full range of error codes that are suported and they are explained in the [Digital Object Interface Protocol Specification](https://https://www.dona.net/sites/default/files/2018-11/DOIPv2Spec_1.pdf)
The HTTP error codes that should be used are the ones which doesn't have to do with data transfer or are already covered by the DOIP letters. Except when a message request and response interaction went without errors it should still confirm with the 200 OK code. 

## REST approach
The REST approach is consistent with the specifications laid out my bachelors thesis. But it is not complete because the favourable approach is the RPC approach.
