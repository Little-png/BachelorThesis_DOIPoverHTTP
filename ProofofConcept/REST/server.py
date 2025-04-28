from flask import Flask, request, jsonify

import json
import random
import os

script_place = os.path.dirname(__file__)
file_place = os.path.join(script_place, '../Operations/response/')

host = "localhost"
port = "5000"

app = Flask(__name__)

@app.route("/Hello",methods=['GET'])
def hello():
	with open(file_place+'0.DOIP_Op.Hello-Response.json') as f:
		res = json.load(f)	
		f.close()			
		
	#integragte response from service into my response by editing the json 
	res = json.dumps(res)		
	return res


@app.route("/create", methods=["PUT"])
def create():
		if request.is_json:
			data = request.get_json()
			if data["properties"]["operationId"]["const"] != "0.DOIP/Op.Create":
				return "Wong DOIP Operator"
	
		#send to service
					
			with open(file_place+'0.DOIP_Op.Create-Response.json') as f:
				res = json.load(f)
				f.close()			
		
			#integragte response from service into my response by editing the json 
			return res
		else: 
			return "Not right sID"

@app.route("/update", methods=['POST'])
def update():
	
	if request.is_json:
		if data["properties"]["operationId"]["const"] != "0.DOIP/Op.Update":
			return "Wong DOIP Operator"
		#send to service
			
		with open(file_place+'0.DOIP_Op.Update-Response.json') as f:
			res = json.load(f)
			f.close()			
		
		#integragte response from service into my response by editing the json 
		res = json.dumps(res)		
		return res


@app.route("/search", methods=['POST'])
def search():	
	if request.is_json:
		data = request.get_json()
		if data["properties"]["operationId"]["const"] != "0.DOIP/Op.Search":
			return "Wrong DOIP Operator"
		query = data["properties"]["attributes"]["properties"]["query"]["description"]
		
	   	#send query to service
	   	#get response from service
		with open(file_place+'0.DOIP_Op.Search-Response.json') as f:
			res = json.load(f)
			f.close()			
		
		#integragte response from service into my response by editing the json 
		res = json.dumps(res)		
		return res
		
	else:
	 	return "0.DOIP/Status.104: The digital object is not known to the service to exist."


@app.route("/retrieve", methods=['GET'])
def retrieve(data):
	targetID = data["properties"]["targetId"]
	#get Data
	with open(file_place+'0.DOIP_Op.Retrieve-Response.json') as f:					
		res = json.load(f)
		f.close()			
		
	#integragte response from service into my response by editing the json 
	res = json.dumps(res)		
	return res
	

@app.route("/delete", methods=['DELETE'])
def delete():	
	if request.is_json:
		data = request.get_json()
		if data["properties"]["operationId"]["const"] != "0.DOIP/Op.Delete":
			return "Wrong DOIP Operator"
		exterminate = data["properties"]["output"]["description"]
		
	   	#send to service
	   	#get response from service
		with open(file_place+'0.DOIP_Op.Delete-Response.json') as f:
			res = json.load(f)
			f.close()			
		
		#integragte response from service into my response by editing the json 
		res = json.dumps(res)		
		return res
		
	else:
	 	return "0.DOIP/Status.104: The digital object is not known to the service to exist."



if __name__ == '__main__':
    app.run(debug=False, host=host, port=port)

