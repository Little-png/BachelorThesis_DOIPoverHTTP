import requests

import os
import json

script_place = os.path.dirname(__file__)
file_place = os.path.join(script_place, '../Operations/request/')


base_url="http://127.0.0.1:5000/"


re = requests.get(base_url+"Hello")
print(re.text)

with open(file_place+'0.DOIP_Op.Search-Request.json') as f:
    doip_search = json.load(f)
    f.close()
    
re2 = requests.post(base_url+"search", json = doip_search)
print(re2.text)


with open(file_place+'0.DOIP_Op.Create-Request.json') as f:
    doip_create = json.load(f)
    f.close()

re_c = requests.put(base_url+"create", json = doip_create)
print(re_c.text)
res = re_c.json()
