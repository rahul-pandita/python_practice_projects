import requests
import json
import sys

r = requests.get("https://xkcd.com/2907/")

print(r.text)

# status code
# print(r)

# print out attributes of r object
# print(dir(r))

# print(help(r))