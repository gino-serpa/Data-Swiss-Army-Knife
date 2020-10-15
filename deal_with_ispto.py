''' confusing code
The output2 data file was created with:

curl -X GET --header 'Accept: application/json' 'https://developer.uspto.gov/ibd-api/v1/patent/application?searchText=5G&start=0&rows=100'

> output2
'''
import json
import gzip
import requests
'''
with gzip.open('output2',"rb") as f:
    d=json.loads(f.read().decode("ascii"))

print(d)
'''
