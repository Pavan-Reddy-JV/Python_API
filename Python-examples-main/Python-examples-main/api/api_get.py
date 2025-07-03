import requests
import json

header = {
    'Accept':'text/plain',
    'content_type' : 'application/json'
}
url = "https://facebee.free.beeceptor.com/todos"
response = requests.get(url,headers=header)

print(response.status_code)
#print(json.dumps(response.json, indent=4))
