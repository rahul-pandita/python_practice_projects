import requests
import json
import sys

def get_api_response():
    # GETS JSON FROM GUTENBERG API AS A DICT
    response = requests.get("https://gutendex.com/books").json()
    
    # Display all the details of books available on page queried
    book_details = response["results"]

    # return a list containing all the detail for available books
    return book_details


def display_book_titles(books_list):
    book_titles = []

    # print out all available books
    for book in books_list:
        book_titles.append(book["title"])
        
    print("\n".join(book_titles))
    return book_titles


display_book_titles(get_api_response())
