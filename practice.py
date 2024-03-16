import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit() 


response = requests.get("https://api.country.is/" + sys.argv[1])

print(response.json())