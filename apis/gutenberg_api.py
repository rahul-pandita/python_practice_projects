import requests
import json
import sys

def get_api_response():
    # GETS JSON FROM GUTENBERG API AS A DICT
    response = requests.get("https://gutendex.com/books")
    print(json.dumps(response.json(), indent=2))

get_api_response()