import requests
import json
import sys

def get_api_response():
    # GETS JSON FROM GUTENBERG API AS A DICT
    response = requests.get("https://gutendex.com/books").json()
    return response
    # print(json.dumps(response.json(), indent=2))

# get_api_response()
    
def display_book_details(response):
    # Display all the details of books available on page queried
    book_details = response["results"]
    print(book_details)

display_book_details(get_api_response())