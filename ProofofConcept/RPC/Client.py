import requests

import os
import json

script_place = os.path.dirname(__file__)
file_place = os.path.join(script_place, '../Operations/request/')



base_url="http://127.0.0.1:5000/Home"
sessionId = ''


#Function to add the session id to a given request body
def includeSesId(req, sId):
	req["properties"]["sessionId"]["description"] = sId
	return req


#Open a request body
with open(file_place+'0.DOIP_Op.Hello-Request.json') as f:
    doip_hello = json.load(f)
    f.close()

#Sending a request to the server
re_hello = requests.post(base_url, json = doip_hello)

#Printing the response
print("Lets try to communicate with the server without a session id--------------")
print(re_hello.text)
print("END--------------------------")



with open(file_place+'0.DOIP_Op.RequestSession-Request.json') as f:
    doip_RS = json.load(f)
    f.close()

re_RS = requests.post(base_url, json = doip_RS)
print("Lets request a sessionid-------------------")
print(re_RS.json())
resp = re_RS.json()
print("END--------------------------")
sessionId = resp["properties"]["results"]["sessionID"]


print("\n")
print("Now lets try again to communnicate with the server but while using the session id----")
print("\n")

doip_hello = includeSesId(doip_hello, sessionId)
re_hello = requests.post(base_url, json = doip_hello)
print(re_hello.json())




print("\n \n")


with open(file_place+'0.DOIP_Op.Search-Request.json') as f:
    doip_search = json.load(f)
    f.close()

doip_search = includeSesId(doip_search, sessionId)    
re2 = requests.post(base_url, json = doip_search)
print(re2.text)


print("\n \n")


with open(file_place+'0.DOIP_Op.Create-Request.json') as f:
    doip_create = json.load(f)
    f.close()

doip_create = includeSesId(doip_create, sessionId)
re_c = requests.post(base_url, json = doip_create)
print(re_c.text)
res = re_c.json()





