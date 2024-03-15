import requests
import json

r = requests.get("https://gutendex.com/books/")

# print(json.dumps(r.json(), indent=2))

print("Dostoevsky" in r)