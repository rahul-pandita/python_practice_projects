import requests
import json
import sys

response = requests.get("https://gutendex.com/books")

b = response.json()

with open("book_list.txt", "r") as book:
    print(b["results"][0]["authors"][0]["name"])