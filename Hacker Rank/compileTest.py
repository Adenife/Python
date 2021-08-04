import requests
import json

url = "https://api.jdoodle.com/v1/execute"
user_input = {'clientId':'ffa160624c55cedd473b7de24432cdff',
                'clientSecret':'cecb3534614b64945e742ac3c61834cfd13e0164f86b347a939c17e4934d3c3e',
                'script':'for i in range(10): print(i)',
                'language':'python3',
                'versionIndex':'3'}

r = requests.post(url, json=user_input)

if r.status_code != 200:
  print("Error:", r.status_code)

data = r.json()
output = data['output']
status = data['statusCode']
memr = data['memory']
cput = data['cpuTime']
print(f"Output: {output} \nStatus Code: {status} \nMemory used: {memr} \nCPU Time: {cput}")