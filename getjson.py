import json
import requests

url = "http://52.56.68.107:52773/csp/healthshare/fhir/fhir/r4/Patient"


x = requests.get(url)
string = x.text
substring = '"Patient","id":"'
start_index = 0
while start_index < len(string):
    index = string.find(substring, start_index)
    if index == -1:
        break
    print(string[index:index+20])
    start_index = index + len(substring)

