import requests
import json

base_url="https://reqres.in/"
header = {
    'Content-Type': 'application/json',
    'x-api-key': 'reqres-free-v1'
}
#payload = {
#    "name": "Subba",
#    "job": "leader"
#}
json_file = open('api/exa.json')
payload = json_file.read()

response = requests.post(base_url + 'api/users', headers=header, data=payload)

print(response.status_code)
print(response.json())