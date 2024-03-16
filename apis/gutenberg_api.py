import requests
import json
import sys

response = requests.get("https://gutendex.com/books")

b = response.json()

results = b["results"]

with open("book_list.txt", "r") as book:
    for result in results:
        print(result["authors"][0]["name"])

    # print(b["results"][0]["authors"][0]["name"])