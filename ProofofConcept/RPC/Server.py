from flask import Flask, request, jsonify

import os
import json
import random

script_place = os.path.dirname(__file__)
file_place = os.path.join(script_place, '../Operations/response/')


#This is a temporary solution to store the session ids for this thesis but in the future they should be stored with appropriate care. 
sIDs = []


host = "localhost"
port = "5000"

supported_operations =["0.DOIP/Op.Create","0.DOIP/Op.Update","0.DOIP/Op.Search","0.DOIP/Op.Delete","0.DOIP/Op.Hello","0.DOIP/Op.Retrieve","0.DOIP/Op.ListOperations"]

app = Flask(__name__)

@app.route("/Home", methods=["POST"])
def hub():
	#Check for message format
	if request.is_json:
		data = request.get_json()
		
		#Check check if the request wants to establish a session or alternativly already provides a session id otherwise refuse further work
		op = data["properties"]["operationId"]["const"]
		if op == "0.DOIP/Op.RequestSession":
			return reqse()
		else:
			if data["properties"]["sessionId"]["description"] in sIDs:
					
				if op == "0.DOIP/Op.Create":
					return create(data)
				elif op ==  "0.DOIP/Op.Update":
					return update(data)
				elif op ==  "0.DOIP/Op.Search":
					return search(data)
				elif op == "0.DOIP/Op.Delete":
					return delete(data)
				elif op == "0.DOIP/Op.Hello":
					return hello(data)
				elif op == "0.DOIP/Op.Retrieve":
					return retrieve(data)
				elif op == "0.DOIP/Op.ListOperations":
					return listops(data)	
				else: 
					return "Keine Gültige Operation"	
			else:
				return "Need sessionId"


	else:
		return "Wrong foramt"


# From here on out is the basic implementation for each DOIP operation.
def hello(data):
	with open(file_place+'0.DOIP_Op.Create-Response.json') as f:
		res = json.load(f)
		f.close()
	return res

#This is the implementation for the custom operation 0.DOIP_Op.RequestSession
def reqse():
	sID = addSID()
	with open(file_place+'0.DOIP_Op.RequestSession-Response.json') as f:
		res = json.load(f)
		f.close()
	res["properties"]["results"]["sessionID"] = sID
	return res

def create(data):
	new_do = data["properties"]["input"]
	#format for the service to understand
	#send to service
	
	with open(file_place+'0.DOIP_Op.Create-Response.json') as f:
		res = json.load(f)
		f.close()			
	
	#integragte response from service into my response by editing the json 
	#res = json.dumps(res)
	res = data		
	return res
	
	
def update(data):				
	new_do = data["properties"]["input"]
	#format for the service to understand
	#send to service
	
	with open(file_place+'0.DOIP_Op.Create-Response.json') as f:
		res = json.load(f)
		f.close()			
		
 	#integragte response from service into my response by editing the json 
	res = json.dumps(res)		
	return res


def search(data):	
	query = data["properties"]["attributes"]["properties"]["query"]["description"]
	
   	#send query to service
   	#get response from service
	with open(file_place+'0.DOIP_Op.Search-Response.json') as f:
		res = json.load(f)
		f.close()			
	
	#integragte response from service into my response by editing the json 
	res = json.dumps(res)		
	return res
	
	

def retrieve(data):
	# get data
	if data:
		return data
	else:
		return "Wrong DO"

def delete():	
	exterminate = data["properties"]["output"]["description"]
		
   	#send to service
   	#get response from service
	with open(file_place+'0.DOIP_Op.Delete-Response.json') as f:
		res = json.load(f)
		f.close()			
		
	#integragte response from service into my response by editing the json 
	res = json.dumps(res)		
	return res

def listops(data):
	with open(file_place+'0.DOIP_Op.Delete-Response.json') as f:
		res = json.load(f)
		f.close()
	res["output"] = supported_operations
	return res
	

#Create and store session ids	
def addSID():
	#Very basic way of creating session ids, in an real sceanrio there need to be a guarante that session ids are unique 
	sID = random.randrange(100)
	sID = str(sID)
	sIDs.append(sID)
	print(sIDs)
	return sID
		

if __name__ == '__main__':
    app.run(debug=False, host=host, port=port)

