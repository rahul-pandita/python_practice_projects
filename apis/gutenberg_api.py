import requests
import json
import sys

response = requests.get("https://gutendex.com/books")

with open("book_list.txt", "w") as books:
    books.write(json.dumps(response.json(), indent=2))

# print(json.dumps(response.json(), indent=2))