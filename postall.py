import json
import requests
import os
import time

## url = "http://localhost:52773/csp/healthshare/demo/fhir/r4/"
url = 'http://52.56.68.107:52773/csp/healthshare/fhir/fhir/r4/'

headers = {'Content-type': 'application/fhir+json'}

directory = r"C:\Users\hwoodall\synthea\output\fhir"
## directory = r"C:\Users\hwoodall\synthea-us-data\test\dummyoutput" 

lookback=36000

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if (os.path.isfile(f)):
        if (os.path.getmtime(f)>=(time.time()-lookback)):
            t = open(f)
            data = json.load(t)
            x= requests.post(url,json = data, headers = headers)
            print(f,x.status_code)

